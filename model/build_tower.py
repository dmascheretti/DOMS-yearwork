"""Transmission line tower: mesh generator for dmb_fem2 (.inp) + FE preview.

Units: m, kg, N, s. Origin at ground level on the tower's vertical axis.
Each "member" is a straight beam between two key points, split into n
elements so that no element exceeds the L_max of its section (lesson L10).
"""
import math
import sys
import numpy as np
from scipy.linalg import eigh

# ---------------- data from the assignment sheet ----------------
L1, L2, L3, L4 = 14.0, 7.5, 24.0, 4.0
H1, H2, H3 = 6.0, 12.0, 3.0
SECTIONS = {               # m [kg/m], EA [N], EI [N m^2]
    "R": (42.0, 1.11e9, 1.72e7),
    "G": (12.8, 3.38e8, 1.11e6),
    "B": (22.2, 5.87e8, 4.00e6),
}
F_MAX_HZ, SAFETY = 16.0, 1.5
H_MODES = [3e-3, 5e-3, 6e-3]

# ---------------- max element length (quasi-static elements) ----------------
OMEGA_MAX = 2 * math.pi * F_MAX_HZ * SAFETY
L_MAX = {k: math.sqrt(math.pi**2 / OMEGA_MAX * math.sqrt(EI / m))
         for k, (m, EA, EI) in SECTIONS.items()}


def leg_x(h):
    """x of the right leg at height h (legs taper from L1/2 at h=0 to L2/2 at h=36)."""
    return L1 / 2 - (L1 / 2 - L2 / 2) * h / (3 * H2)


# ---------------- key points (named) ----------------
P = {}
for side, s in (("L", -1), ("R", +1)):
    for h in (0, 6, 12, 18, 24, 30, 36):
        P[f"leg{side}{h}"] = (s * leg_x(h), float(h))
    P[f"inner{side}6"] = (s * 0.5 * L1 / 2, 6.0)             # midpoint of line C -> O at h = 6
    P[f"tip{side}"] = (s * L3 / 2, 30.0)                      # A (right) / D (left)
    P[f"postB{side}"] = (s * (L3 / 2 - L4), 30.0)             # foot of the cross-arm post
    xp = L3 / 2 - L4
    yp = 30.0 + (36.0 - 30.0) * (L3 / 2 - xp) / (L3 / 2 - L2 / 2)
    P[f"postT{side}"] = (s * xp, yp)                          # top of the post, on the upper chord
    P[f"peak{side}"] = (s * L2 / 2, 3 * H2 + H3)              # earth-wire peak above the leg top
P["C"], P["B"], P["top"] = (0.0, 12.0), (0.0, 24.0), (0.0, 36.0)

# ---------------- members: (point a, point b, section) ----------------
M = []
for s in ("L", "R"):
    hs = (0, 6, 12, 18, 24, 30, 36)
    M += [(f"leg{s}{a}", f"leg{s}{b}", "R") for a, b in zip(hs, hs[1:])]   # legs
    M += [(f"leg{s}0", f"inner{s}6", "R"), (f"inner{s}6", "C", "R")]       # bottom bay inner members
    M += [(f"leg{s}6", f"inner{s}6", "G")]                                 # short green horizontal
    M += [("C", f"leg{s}18", "G"), (f"leg{s}18", "B", "G")]                # lower diamond
    M += [("B", f"leg{s}30", "G"), (f"leg{s}30", "top", "G")]              # upper diamond
    M += [(f"leg{s}30", f"postB{s}", "B"), (f"postB{s}", f"tip{s}", "B")]  # cross-arm lower chord
    M += [(f"tip{s}", f"postT{s}", "B"), (f"postT{s}", f"leg{s}36", "B")]  # cross-arm upper chord
    M += [(f"postB{s}", f"postT{s}", "B"), (f"postT{s}", f"leg{s}30", "B")]  # post + diagonal
    M += [(f"leg{s}36", f"peak{s}", "B"), (f"peak{s}", "top", "B")]        # earth-wire peak
for h in (12, 24, 36):                                                    # red horizontals
    mid = {12: "C", 24: "B", 36: "top"}[h]
    M += [(f"legL{h}", mid, "R"), (mid, f"legR{h}", "R")]

# ---------------- mesh ----------------
nodes, key_node = [], {}


def node_at(xy):
    for i, q in enumerate(nodes):
        if abs(q[0] - xy[0]) < 1e-9 and abs(q[1] - xy[1]) < 1e-9:
            return i
    nodes.append(xy)
    return len(nodes) - 1


# key points first, in a readable order (constrained base nodes first)
order = ["legL0", "legR0"] + [k for k in P if k not in ("legL0", "legR0")]
for k in order:
    key_node[k] = node_at(P[k])

beams = []
for a, b, sec in M:
    (xa, ya), (xb, yb) = P[a], P[b]
    length = math.hypot(xb - xa, yb - ya)
    n = max(1, math.ceil(length / L_MAX[sec] - 1e-12))
    ids = [key_node[a]]
    for j in range(1, n):
        ids.append(node_at((xa + (xb - xa) * j / n, ya + (yb - ya) * j / n)))
    ids.append(key_node[b])
    for p, q in zip(ids, ids[1:]):
        beams.append((p, q, sec, length / n))

# ---------------- simple FE model (same theory as L10) ----------------
nn = len(nodes)
ndof = 3 * nn
K = np.zeros((ndof, ndof))
Mm = np.zeros((ndof, ndof))
for p, q, sec, Le in beams:
    m, EA, EI = SECTIONS[sec]
    (xa, ya), (xb, yb) = nodes[p], nodes[q]
    c, s = (xb - xa) / Le, (yb - ya) / Le
    L = Le
    k = np.zeros((6, 6))
    k[np.ix_([0, 3], [0, 3])] = EA / L * np.array([[1, -1], [-1, 1]])
    kb = EI / L**3 * np.array([[12, 6*L, -12, 6*L], [6*L, 4*L*L, -6*L, 2*L*L],
                               [-12, -6*L, 12, -6*L], [6*L, 2*L*L, -6*L, 4*L*L]])
    k[np.ix_([1, 2, 4, 5], [1, 2, 4, 5])] = kb
    mm = np.zeros((6, 6))
    mm[np.ix_([0, 3], [0, 3])] = m * L / 6 * np.array([[2, 1], [1, 2]])
    mb = m * L / 420 * np.array([[156, 22*L, 54, -13*L], [22*L, 4*L*L, 13*L, -3*L*L],
                                 [54, 13*L, 156, -22*L], [-13*L, -3*L*L, -22*L, 4*L*L]])
    mm[np.ix_([1, 2, 4, 5], [1, 2, 4, 5])] = mb
    lam = np.array([[c, s, 0], [-s, c, 0], [0, 0, 1]])
    T = np.zeros((6, 6)); T[:3, :3] = lam; T[3:, 3:] = lam
    dofs = [3*p, 3*p+1, 3*p+2, 3*q, 3*q+1, 3*q+2]
    K[np.ix_(dofs, dofs)] += T.T @ k @ T
    Mm[np.ix_(dofs, dofs)] += T.T @ mm @ T

constrained = [3*key_node["legL0"] + i for i in range(3)] + [3*key_node["legR0"] + i for i in range(3)]
free = [i for i in range(ndof) if i not in constrained]
Kff, Mff = K[np.ix_(free, free)], Mm[np.ix_(free, free)]
w2, phi = eigh(Kff, Mff)
freqs = np.sqrt(np.abs(w2)) / (2 * math.pi)

# Rayleigh damping: h_i = alpha/(2 w_i) + beta w_i/2, least squares on 3 modes
w = 2 * math.pi * freqs[:3]
A = np.column_stack([1 / (2 * w), w / 2])
alpha, beta = np.linalg.lstsq(A, np.array(H_MODES), rcond=None)[0]

# ---------------- write .inp ----------------
out = sys.argv[1] if len(sys.argv) > 1 else "tower.inp"
with open(out, "w") as f:
    f.write("! Transmission line tower - dmb_fem2 input file\n")
    f.write("! units: m, kg, N. Origin on the tower axis at ground level.\n")
    f.write("! L_max: red %.2f m, green %.2f m, blue %.2f m (16 Hz x 1.5)\n" % (L_MAX["R"], L_MAX["G"], L_MAX["B"]))
    f.write("*NODES\n")
    clamped = {key_node["legL0"], key_node["legR0"]}
    for i, (x, y) in enumerate(nodes):
        bc = "1 1 1" if i in clamped else "0 0 0"
        f.write(f"{i+1:4d}   {bc}   {x:10.4f} {y:10.4f}\n")
    f.write("*ENDNODES\n\n*BEAMS\n")
    for j, (p, q, sec, Le) in enumerate(beams):
        m, EA, EI = SECTIONS[sec]
        f.write(f"{j+1:4d}  {p+1:4d} {q+1:4d}   {m:6.1f}  {EA:.3e}  {EI:.3e}\n")
    f.write("*ENDBEAMS\n\n*DAMPING\n")
    f.write(f"{alpha:.6e} {beta:.6e}\n")

# ---------------- report ----------------
total_mass = sum(SECTIONS[s][0] * Le for _, _, s, Le in beams)
print(f"nodes {nn}, beams {len(beams)}, dof {ndof}, mass {total_mass:.0f} kg")
print("L_max:", {k: round(v, 2) for k, v in L_MAX.items()})
print("key nodes:", {k: key_node[k] + 1 for k in ("tipR", "tipL", "B", "C", "legL0", "legR0")})
print("first 8 frequencies [Hz]:", np.round(freqs[:8], 3))
print("modes below 16 Hz:", int(np.sum(freqs < 16)))
print(f"alpha = {alpha:.4e} 1/s, beta = {beta:.4e} s")
print("damping check h_i:", np.round(alpha / (2 * w) + beta * w / 2, 5))
np.save(out.replace(".inp", "_nodes.npy"), np.array(nodes))
np.save(out.replace(".inp", "_beams.npy"), np.array([(p, q, "RGB".index(s)) for p, q, s, _ in beams]))
