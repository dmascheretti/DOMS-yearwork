// Render every ```latex block of the exported guide to a PNG image with KaTeX.
// usage: node render_formulas.js <guide.md> <katex dist dir> <out dir>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [mdPath, katexDir, outDir] = process.argv.slice(2);
const md = fs.readFileSync(mdPath, 'utf8');
const formulas = [...md.matchAll(/```latex\n([\s\S]*?)\n```/g)].map(m => m[1].trim());
fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, 'formulas.json'), JSON.stringify(formulas, null, 1));

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 2, viewport: { width: 1100, height: 600 } });
  const html = `<!doctype html><html><head><meta charset="utf-8">
    <link rel="stylesheet" href="file://${katexDir}/katex.min.css">
    <script src="file://${katexDir}/katex.min.js"></script>
    <style>body{margin:0;background:#fff} #f{display:inline-block;min-width:1000px;text-align:center;padding:4px 10px;background:#fff;font-size:21px}
    .katex-display{margin:0}</style></head><body><div id="f"></div></body></html>`;
  const htmlPath = path.join(outDir, 'render.html');
  fs.writeFileSync(htmlPath, html);
  await page.goto('file://' + htmlPath, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const errors = [];
  for (let i = 0; i < formulas.length; i++) {
    const err = await page.evaluate(tex => {
      const el = document.getElementById('f');
      try { katex.render(tex, el, { displayMode: true, throwOnError: true }); return null; }
      catch (e) { return String(e); }
    }, formulas[i]);
    if (err) errors.push([i, err]);
    await page.evaluate(() => document.fonts.ready);
    const el = await page.$('#f');
    const name = 'f' + String(i + 1).padStart(2, '0') + '.png';
    await el.screenshot({ path: path.join(outDir, name) });
  }
  console.log('rendered', formulas.length, 'errors', JSON.stringify(errors));
  await browser.close();
})();
