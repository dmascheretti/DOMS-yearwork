# Dynamics of Mechanical Systems — Year Work 2026/2027

Year work and oral-exam preparation for *Dynamics of Mechanical Systems* (Proff. S. Bruni, G. Bucca).
The assignment is the dynamic analysis of a **high-voltage transmission line tower** with the course FE
software `dmb_fem2` (MATLAB).

## Repository layout

| Folder | Content |
| --- | --- |
| `model/` | FE model of the tower: `tower.inp` (dmb_fem2 input), `build_tower.py` (generates the .inp and a FE preview), `plot_mesh.py`, `tower_mesh.png` |
| `scripts/` | MATLAB scripts for the tasks the GUI does not cover (constraint forces, 2-mode model, impulse response) — to do |
| `results/` | Plots for the printed copy required at the oral — to do |
| `study-guide/` | Oral-exam study guide (all 14 lessons): PDF exports and Markdown source, plus the tools used to typeset it |

## Task status

| Task | Status |
| --- | --- |
| 1. FE model valid in 0–16 Hz (safety factor 1.5) | Draft `model/tower.inp` — geometry of peaks and cross-arms to be checked against the figure |
| 2. Natural frequencies and modes in 0–16 Hz | Preview computed (see below); to confirm in dmb_fem2 |
| 3. FRFs a)–e) | To do (dmb_fem2 Frequency response menu) |
| 4. FRFs of constraint forces f), g) | To do (script on exported `_mkr.mat`) |
| 5. Modal model with 2 modes | To do |
| 6. Response to conductor failure (impulse) | To do |
| 7. Structural modification (−25 % FRF c, ≤ +5 % mass) | To do |

## Model summary (`model/tower.inp`)

- Origin on the tower axis at ground level; units m, kg, N.
- Maximum element length from the quasi-static criterion Ω_max = 2π·16·1.5 rad/s:
  red (IPE300) 6.47 m, green (IPE140) 4.39 m, blue 5.27 m.
- 39 nodes, 60 beam elements, 117 d.o.f., total mass ≈ 7767 kg. O1 and O2 clamped.
- Key nodes: **A = 21**, **D = 10**, **B = 26**, **C = 25**, **O1 = 1**, **O2 = 2**.
- Rayleigh damping fitted by least squares on h1, h2, h3:
  α = 1.638·10⁻³ s⁻¹, β = 1.534·10⁻⁴ s.
- Preview natural frequencies (Python, consistent mass): 6.15, 11.29, 11.52, 12.53, 15.16, 15.72, 15.90 Hz
  → 7 modes below 16 Hz. Small differences from dmb_fem2 are expected.

Regenerate the model (needs Python with numpy, scipy, matplotlib):

```bash
cd model && python3 build_tower.py tower.inp && python3 plot_mesh.py tower
```

## Study guide

- `study-guide/Oral_Exam_Guide_typeset.pdf` — typeset with KaTeX (best for reading/printing).
- `study-guide/Oral_Exam_Guide_doc_export.pdf` — export of the online doc (formulas as images/text).
- `study-guide/guide.md` — source text. Formulas are ```` ```latex ```` blocks.
- `study-guide/tools/` — scripts used to convert the Markdown to PDF (pandoc + KaTeX + headless Chromium)
  and to render formulas as images. `header.html` points to a local KaTeX install; adjust the path before reuse.
