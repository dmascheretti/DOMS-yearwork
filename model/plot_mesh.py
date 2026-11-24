"""Plot the tower mesh with node numbers, coloured like the assignment figure."""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

base = sys.argv[1]
nodes = np.load(base + "_nodes.npy")
beams = np.load(base + "_beams.npy")
colors = {0: "#d62728", 1: "#2ca02c", 2: "#1f4fd6"}

fig, ax = plt.subplots(figsize=(8, 10))
for p, q, c in beams:
    ax.plot(*nodes[[p, q]].T, color=colors[c], lw=2)
ax.plot(*nodes.T, "ko", ms=3)
for i, (x, y) in enumerate(nodes):
    ax.annotate(str(i + 1), (x, y), xytext=(3, 3), textcoords="offset points", fontsize=8)
for name, xy in {"A": (12, 30), "D": (-12, 30), "B": (0, 24), "C": (0, 12), "O1": (-7, 0), "O2": (7, 0)}.items():
    ax.annotate(name, xy, xytext=(-14, -14), textcoords="offset points", fontsize=11, weight="bold")
ax.set_aspect("equal")
ax.grid(alpha=0.3)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_title("Tower FE mesh (red IPE300, green IPE140, blue) - node numbers")
fig.tight_layout()
fig.savefig(base + "_mesh.png", dpi=110)
