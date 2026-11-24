"""Plain-text (Unicode) versions of the simpler formulas, and the doc ops that swap them in."""
import json

TEXT = {
    2: "T = Σᵢ ½ (mᵢ ẋ_Gi² + mᵢ ẏ_Gi² + Jᵢ θ̇ᵢ²)",
    3: "T = ½ m(x) ẋ²,   m(x) = Σᵢ (mᵢ λ_mi,x² + mᵢ λ_mi,y² + Jᵢ λ_mi,θ²)",
    6: "V_el ≈ ½ kᵢ Δᵢ₀² + kᵢ Δᵢ₀ λ_ki x + ½ (kᵢ λ_ki² + kᵢ Δᵢ₀ ν_ki) x²",
    7: "m₀ ẍ + c₀ ẋ + k x = f₀(t),   k = k_el^I + k_el^II + k_g",
    8: "∂(xᵀ[A]x)/∂x = 2 xᵀ[A]   (for a symmetric matrix [A])",
    9: "[m] ẍ + [c] ẋ + [k] x = f(t)",
    13: "(−ω²[m] + [k]) x₀ = 0,   det(−ω²[m] + [k]) = 0",
    14: "x(t) = Σⱼ₌₁ⁿ x₀⁽ʲ⁾ Cⱼ cos(ωⱼ t + φⱼ)",
    15: "(−Ω²[m] + iΩ[c] + [k]) X = F   ⇒   X = [G(iΩ)] F",
    16: "T = ½ q̇ᵀ [Φ]ᵀ[m][Φ] q̇,   V = ½ qᵀ [Φ]ᵀ[k][Φ] q,   δW = δqᵀ [Φ]ᵀ f",
    17: "[Φ]ᵀ[m][Φ] q̈ + [Φ]ᵀ[c][Φ] q̇ + [Φ]ᵀ[k][Φ] q = [Φ]ᵀ f",
    18: "−ωⱼ² [m] x₀⁽ʲ⁾ + [k] x₀⁽ʲ⁾ = 0,   −ωᵢ² [m] x₀⁽ⁱ⁾ + [k] x₀⁽ⁱ⁾ = 0",
    19: "(ωᵢ² − ωⱼ²) · x₀⁽ʲ⁾ᵀ [m] x₀⁽ⁱ⁾ = 0",
    20: "[c] = α[m] + β[k]   ⇒   [Φ]ᵀ[c][Φ] = α[m̄] + β[k̄]",
    21: "m̄ᵢ q̈ᵢ + c̄ᵢ q̇ᵢ + k̄ᵢ qᵢ = f̄ᵢ(t),   f̄ᵢ = x₀⁽ⁱ⁾ᵀ f,   ωᵢ² = k̄ᵢ / m̄ᵢ",
    25: "εₓ = (1/E) [σₓ − ν(σ_y + σ_z)],   γ_xy = τ_xy / G,   G = E / (2(1 + ν))",
    27: "u(x, t) = f₁(x − ct) + f₂(x + ct)",
    28: "β̈(t) / β(t) = c² · α″(x) / α(x) = −ω²",
    29: "β̈ + ω²β = 0  ⇒  β = C cos(ωt + φ);     α″ + (ω/c)² α = 0  ⇒  α = A cos(ωx/c) + B sin(ωx/c)",
    30: "sin(ωL/c) = 0   ⇒   ωₖ = (kπ/L)·c = (kπ/L)·√(E/ρ),   αₖ(x) = sin(kπx/L),   k = 1, 2, …",
    31: "εₓ = −z ∂²w/∂x²,   σₓ = −E z ∂²w/∂x²",
    32: "M = EI ∂²w/∂x²,   I = ∫ z² dA  (over the section A)",
    33: "EI ∂⁴w/∂x⁴ + m ∂²w/∂t² = 0",
    34: "β̈ + ω²β = 0,   α^IV − γ⁴α = 0,   γ⁴ = m ω² / (EI)",
    35: "α(x) = A cos γx + B sin γx + C cosh γx + D sinh γx",
    36: "γₖL = kπ   ⇒   ωₖ = (kπ/L)² · √(EI/m),   αₖ = sin(kπx/L)",
    37: "det[H(γ)] = 0   ⇒   cos γL · cosh γL = −1   (cantilever)",
    38: "γ_xy = −z ∂ϑ/∂x,   γ_zx = y ∂ϑ/∂x   ⇒   τ = G r ∂ϑ/∂x",
    40: "∂M_t/∂x = ρ I_P ∂²ϑ/∂t²   ⇒   G I_T ∂²ϑ/∂x² = ρ I_P ∂²ϑ/∂t²,   c = √(G I_T / (ρ I_P))",
    41: "w(x, t) = Σₖ₌₁^∞ φₖ(x) qₖ(t) ≈ Σₖ₌₁ⁿ φₖ(x) qₖ(t) = Φᵀ(x) q(t)",
    44: "c̄ᵢᵢ = hᵢ c_cr,i = 2 hᵢ m̄ᵢᵢ ωᵢ = 2 hᵢ √(k̄ᵢᵢ m̄ᵢᵢ)",
    46: "u(ξ, t) = (1 − ξ/L) uᵢ + (ξ/L) uⱼ",
    55: "fᵢ(ξ, η, ζ) = ⅛ (1 + ξξᵢ)(1 + ηηᵢ)(1 + ζζᵢ),   u = {u, v, w}ᵀ = [f] xₖ",
    59: "x(ξ, η, ζ) = Σᵢ₌₁⁸ Nᵢ xᵢ,   y = Σ Nᵢ yᵢ,   z = Σ Nᵢ zᵢ",
    63: "aᴸ = [Λ_LG] aᴳ,   [Λ_LG] = [Λ_II→L] [Λ_I→II] [Λ_G→I],   [Λ_GL] = [Λ_LG]⁻¹ = [Λ_LG]ᵀ",
    64: "ωᴳ = [A_G] θ̇,   ωᴸ = [A_L] θ̇,   θ = {σ, β, ρ}ᵀ",
    65: "T = ½ v_Gᵀ [m] v_G + ½ ωᴸᵀ [J_Gᴸ] ωᴸ = ½ ẋᵀ [M(x)] ẋ",
    66: "[J_Oᴸ] = [x̃_Gᴸ]ᵀ [m] [x̃_Gᴸ] + [J_Gᴸ]",
    67: "m_s ẍ + c_s ẋ + k_s x = F(x, ẋ)        [m_s] ẍ + [c_s] ẋ + [k_s] x = F(x, ẋ)",
    68: "k_f = −∂F/∂x (at equilibrium),   c_f = −∂F/∂ẋ (at equilibrium)   ⇒   m_s ẍ + (c_s + c_f) ẋ + (k_s + k_f) x = 0",
    69: "m ẍ + (c − αP) ẋ + k x = (f_d0 − αV) P",
    70: "[K_F] = −∂F/∂x (at equilibrium),   [C_F] = −∂F/∂ẋ (at equilibrium)   ⇒   [M_s] ẍ + [C_T] ẋ + [K_T] x = 0",
    74: "T_tf + T_tr = mV(β̇ + ψ̇),   a T_tf − b T_tr = J_G ψ̈   ⇒   [A] ż + [B] z = C δ",
    75: "p = mVJ_G > 0,   q = m(C_F a² + C_R b²) + J_G(C_F + C_R) > 0,   r = (C_F C_R L² / V)(1 + KV²)",
    76: "ε_ll = −ε_lr = −sσ̇/V + γy/R₀,   ε_tl = ε_tr = ẏ/V − σ   (sign as in the notes)",
}

# formula number -> (block id suffix, hash, rev of the ack that wrote it)
IDS = {}
h1 = "4129d4f6 f0666990 d4050e7f 6d514aaa f08bea9f f87be0bc 74c44d4f 9ea9a8e8 dfe4f8a6 0bd723e4 b6ed2c57 044b1e3e 6ff3b20f c2269bc5 4d59c36f 7f60c619 3f685723 ad905cad 36720a05 73979da5 61a462f8 26670867 b6039953 f6c9c25d 9d38add0 a14a5ccb 6aba622c ca6eeab2 0c45fcd0 3228be4f 58b8d01c 43b844f2 ce3df852 9e739e49 6a5cbcff d3609ffb 85bb449d 97f477f6 e2b837c0".split()
h2 = "3f9947c3 22c5fe9b b917bc7e 88150a85 b59acefd 5f37c7ff 91c985ce 7207002c 552c94dd 1e964349 92096209 d053cf27 4b2e40b4 4cdd4d9a d7397ddb a8bd6fcf 9249e090 c344a5fa cae39684 abc7638c 7ad1f2dc 434bf6d6 af77d75c f7e5c0a0 0d92f2c5 c53cc1c2 806b6e4d aac1661e 5c710bb5 190cd6b8 a40ea55a fc1836dc 3a6c304b 74a01722 4d46d6ba 3ce59b3d 36de4b21 a47230bb".split()
for n in range(1, 40):
    IDS[n] = (96344 + 2 * (n - 1), h1[n - 1], 26)
for n in range(40, 78):
    IDS[n] = (96422 + 2 * (n - 40), h2[n - 40], 27)


def esc(s):
    for ch in "_*":
        s = s.replace(ch, "\\" + ch)
    return s


assert len(TEXT) == 45
ops = []
for n in sorted(TEXT):
    i, h, r = IDS[n]
    ops.append({"op": "replace", "target": {"kind": "blocks", "ids": ["mkcjrr84crg.%d" % i]},
                "ifHash": h, "ifRev": r,
                "with": {"from": {"kind": "inline", "content": esc(TEXT[n])}, "as": "markdown"}})
print(json.dumps({"ops": ops}, ensure_ascii=False, separators=(",", ":")))
