const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'load' });
  await p.waitForSelector('body[data-math-done="1"]');
  await p.evaluate(() => document.fonts.ready);
  const errs = await p.$$eval('.katex-error', els => els.map(e => e.getAttribute('title') || e.textContent));
  console.log('katex errors:', errs.length, JSON.stringify(errs.slice(0, 5)));
  await p.pdf({
    path: process.argv[3], format: 'A4', printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#666"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '16mm', bottom: '16mm', left: '15mm', right: '15mm' }
  });
  await p.setViewportSize({ width: 900, height: 1300 });
  const h = await p.$$('h2');
  const picks = [1, 6, 9];
  for (let i = 0; i < picks.length; i++) {
    await p.evaluate(e => e.scrollIntoView(), h[picks[i]]);
    await p.screenshot({ path: process.argv[4] + '/prev' + i + '.png' });
  }
  await b.close();
})();
