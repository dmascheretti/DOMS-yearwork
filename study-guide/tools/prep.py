"""Turn the exported guide markdown into pandoc-ready markdown:
- ```latex blocks -> $$ display math $$
- plain-text subscripts/superscripts (x\_i, x\_{ab}, e^{iΩt}) -> <sub>/<sup>
"""
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()

text = re.sub(r"```latex\n(.*?)\n```",
              lambda m: "$$\n" + m.group(1).strip() + "\n$$", text, flags=re.S)
text = text.replace("<byline of the exported doc>",
                    "Study guide based on the lecture notes of Proff. Bruni & Bucca")

# letters a token may end with before a subscript (incl. Greek and combining marks)
BASE = r"[A-Za-z0-9\u0370-\u03ff\u0300-\u036f\)\]'’″]"


def fix_prose(chunk):
    # x\_{...} and x_{...}
    chunk = re.sub(r"(?<=" + BASE + r")\\?_\{([^{}]+)\}", r"<sub>\1</sub>", chunk)
    # x\_abc  (subscript = run of letters/digits/Greek)
    chunk = re.sub(r"(?<=" + BASE + r")\\?_([A-Za-z0-9\u0370-\u03ff]+)", r"<sub>\1</sub>", chunk)
    # e^{...}
    chunk = re.sub(r"\\?\^\{([^{}]+)\}", r"<sup>\1</sup>", chunk)
    return chunk


parts = re.split(r"(\$\$.*?\$\$)", text, flags=re.S)
parts = [p if p.startswith("$$") else fix_prose(p) for p in parts]
open(dst, "w", encoding="utf-8").write("".join(parts))
