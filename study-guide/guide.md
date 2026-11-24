# Dynamics of Mechanical Systems — Oral Exam Guide

Study guide based on the lecture notes of Proff. Bruni & Bucca

## How to use this guide

The whole course is one idea applied over and over: write the equations of motion, linearise them, find natural frequencies and modes, then use the modes to understand the response. Every chapter below follows the same layout so you can copy it into your iPad notes:

1. **The big idea**: what the chapter is about, in a few sentences you could say at the start of an answer.
2. **Step-by-step derivations**: every passage, in the notation of Bruni & Bucca's notes (column vector = underlined letter, matrix = \[m\]).
3. **On your blackboard**: the short list of formulas and sketches you must be able to write from memory. Copy these onto the blackboard and rewrite them until you can do it without looking.
4. **Likely oral questions**: each with an answer outline in the order you should say it.
5. **Traps and follow-ups**: what the professor typically asks next.

The Drive folder contains the 14 lecture notes only, no exercise sheets. Where the guide says "worked example", it refers to the examples inside the notes (for example the slider-crank in L01 and the 2-dof system in L02–L03). Send the exercise sheets and I'll add a section linking each one to the theory it uses.

### Course map

| Block | Lessons | The question it answers |
| --- | --- | --- |
| Lumped-parameter systems (rigid bodies + springs + dampers) | L01–L04 | How do I write, linearise and solve the equations of a 1-dof or n-dof system, and how do I measure its modal parameters? |
| Distributed-parameter systems (beams) | L05–L09 | What changes when mass and stiffness are spread along the body: PDEs, infinite modes, boundary conditions |
| Finite elements | L10–L11 | How to turn a continuous structure back into an n-dof system that a computer can solve |
| Rigid body in space | L12 | How do I write the kinetic energy of a body in 3D (inertia tensor, Cardan angles), and when is a rotor balanced? |
| Stability | L13–L14 | When does a system subjected to force fields (or a vehicle) become unstable, and how do I check it with eigenvalues? |

### The thread that links everything

L01 gives you \[m\], \[c\], \[k\]. L02 solves the free and forced motion: eigenvalues, modes, FRF. L03 uses the modes to decouple the system. L04 does the reverse and extracts the modes from measurements. L05–L09 redo L01–L03 for a continuum: the eigenproblem becomes a boundary-value problem and the modes become functions. L10–L11 discretise the continuum back into \[m\] and \[k\]. L13–L14 come back to the state-space eigenvalues of L02: a positive real part means instability. Professors love questions that cross these links, so the last section collects them.

## L01 — Dynamics of lumped-parameter systems

**Big idea:** a lumped system has a finite number n of independent coordinates. Lagrange's equations give n equations of motion without constraint forces. For small motion around equilibrium, every term linearises to a constant \[m\], \[c\], \[k\] built from Jacobians (and Hessians for stiffness).

### 1. Basic vocabulary (say these definitions exactly)

- **Constraint:** prevents some motion and generates constraint forces (usually unknown). General form f(y, ẏ) = 0.
- **Holonomic constraint:** can be written as f(y) = 0, so it forbids *positions*, not just *motions*. Non-holonomic constraints restrict velocities only.
- **Independent coordinates:** with n\_y kinematic variables and n\_c holonomic constraint equations, n = n\_y − n\_c coordinates x can vary freely, and every kinematic variable is y = y(x).
- **Virtual displacement:** infinitesimal, compatible with the constraints, at frozen time.
- **Principle of virtual work (PVW):** in static equilibrium, the total virtual work of all forces is zero for every virtual displacement.

### 2. Four ways to write the equation of motion

The notes use the same 1-dof mass-spring-damper for all four, and all give mẍ + cẋ + kx = f(t).

| Method | What you write | When it is best |
| --- | --- | --- |
| Newton | ΣF = m a\_G, ΣM\_O = J\_O ω̇ (O fixed or the c.o.m.) | Single body, few constraints |
| D'Alembert | Add inertia force F\_in = −m a\_G and moment M\_in = −J\_G ω̇, then write equilibrium | Same as Newton, but shows the inertia terms explicitly |
| Virtual work | δW + δW\_in = 0 for every virtual displacement | Many bodies and constraints: ideal (non-dissipative) constraints do no work, so their forces drop out |
| Lagrange | Energy form of the PVW (below) | Systematic, any number of dofs, the standard tool in this course |

**Worked example in the notes: slider-crank.** Newton/D'Alembert needs 3 bodies × 3 equations = 9 equations with 8 unknown constraint forces. Lagrange gives the single equation for the crank angle α directly. Use it in the oral to justify why we prefer Lagrange.

### 3. Lagrange's equation

```latex
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot x}\right) - \frac{\partial T}{\partial x} + \frac{\partial D}{\partial \dot x} + \frac{\partial V}{\partial x} = \frac{\delta W}{\delta x}
```

T = kinetic energy, D = dissipation function, V = potential energy (elastic + gravity), δW = virtual work of the remaining (time-dependent) forces. For n dofs, write it with derivatives with respect to the vector x, which gives one matrix equation.

### 4. The general nonlinear 1-dof equation (derivation to know)

**Kinetic energy.** For n\_B rigid bodies in planar motion (König's theorem):

```latex
T = \sum_{i} \tfrac{1}{2}\left(m_i \dot x_{Gi}^2 + m_i \dot y_{Gi}^2 + J_i \dot\theta_i^2\right)
```

Each position depends on x only, so ẋ\_Gi = λ\_mix(x) ẋ, where λ is the **Jacobian** (derivative of the kinematic relationship). Substituting:

```latex
T = \tfrac{1}{2}\, m(x)\, \dot x^2, \qquad m(x) = \sum_i \left(m_i \lambda_{mix}^2 + m_i \lambda_{miy}^2 + J_i \lambda_{mi\theta}^2\right)
```

m(x) is the **generalised mass**. It is constant only if all kinematic relationships are linear. Applying Lagrange:

```latex
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot x}\right) - \frac{\partial T}{\partial x} = m(x)\ddot x + \tfrac{1}{2}\frac{dm}{dx}\dot x^2
```

**Dissipation.** D = ½ Σ c\_i Δ̇\_i² with Δ̇\_i = λ\_ci(x) ẋ, so D = ½ c(x) ẋ² and ∂D/∂ẋ = c(x) ẋ.

**Conservative forces.** ∂V/∂x = −f\_c(x).

**Time-dependent forces.** δW = Σ(λ\_fix f\_ix + λ\_fiy f\_iy) δx = f(x, t) δx.

Result:

```latex
m(x)\ddot x + \tfrac{1}{2}\frac{dm}{dx}\dot x^2 + c(x)\dot x - f_c(x) = f(x,t)
```

### 5. Linearisation around equilibrium (the core of the chapter)

**Why linearise:** a nonlinear equation (even the pendulum m l² θ̈ + m g l sinθ = 0) has no closed-form solution. Numerical integration works for analysis, but gives no insight for design (you can't see how a parameter affects the motion).

**Equilibrium:** x = x₀ constant, no time-dependent forces, so f\_c(x₀) = 0. It may have several solutions; you linearise around one.

**Procedure:** shift the coordinate so x = 0 is the equilibrium, expand each term in a power series and keep only first-order terms. Products like x·ẋ and f(t)·x are dropped.

| Term | Linearised result | Rule to remember |
| --- | --- | --- |
| Inertia | m(0) ẍ (the ẋ² term is second order) | Evaluate the Jacobians at equilibrium, before even writing T |
| Damping | c(0) ẋ | Same: Jacobians at equilibrium |
| Elastic | k\_el = Σ k\_i λ\_ki(0)² + Σ k\_i Δ\_i0 ν\_ki(0) | Needs the second-order expansion of the spring elongation |
| Gravity | k\_g = Σ m\_i g ν\_gi(0) | Needs the Hessian of the c.o.m. height |
| Forcing | f₀(t) = Σ(λ\_fix(0) f\_ix + λ\_fiy(0) f\_iy) | Jacobians at equilibrium |

**Why potential energy needs second order.** The force is −∂V/∂x, so to get a force linear in x you need V up to x². Expand the spring elongation: Δ\_i(x) ≈ Δ\_i0 + λ\_ki x + ½ ν\_ki x², then square it:

```latex
V_{el} \approx \tfrac{1}{2}k_i\Delta_{i0}^2 + k_i\Delta_{i0}\lambda_{ki}x + \tfrac{1}{2}\left(k_i\lambda_{ki}^2 + k_i\Delta_{i0}\nu_{ki}\right)x^2
```

- The constant term disappears after differentiation.
- The linear term cancels against the linear term of gravity (**stationarity of potential energy** at equilibrium).
- What remains is the stiffness: first-order part k\_i λ² plus **second-order elastic stiffness** k\_i Δ\_i0 ν.

The second-order stiffness exists only if the spring is **preloaded** (Δ\_i0 ≠ 0) **and** the Hessian is non-zero. It is not necessarily small: the notes give the railway suspension whose lateral stiffness drops when the car is fully loaded.

**Gravitational stiffness** k\_g = m g ν\_g(0): gravity appears in the linearised equation only if the height of a c.o.m. depends nonlinearly on x. Example: pendulum, h = −l cosθ so ν = l and k\_g = m g l.

**Final linearised 1-dof equation:**

```latex
m_0\ddot x + c_0\dot x + k\,x = f_0(t), \qquad k = k_{el}^{I} + k_{el}^{II} + k_g
```

**Linear systems** (all kinematic relationships linear): constant Jacobians, zero Hessians, so the equation is exact even for large motion, there is no second-order stiffness, no gravity term, and exactly one equilibrium position (V is exactly quadratic).

### 6. Extension to n dofs: the matrix form

Define the derivative of a scalar with respect to a vector as a row vector. Key result for symmetric \[A\]:

```latex
\frac{\partial}{\partial \underline{x}}\left(\underline{x}^T[A]\underline{x}\right) = 2\,\underline{x}^T[A]
```

Systematic recipe (memorise the pattern):

1. Collect the physical velocities ẏ\_m = \[λ\_m\] ẋ, with \[m\_ph\] = diag(m₁, m₁, J₁, …) → **\[m\] = \[λ\_m\]ᵀ \[m\_ph\] \[λ\_m\]**.
2. Damper elongation rates ẏ\_d = \[λ\_d\] ẋ, \[c\_ph\] = diag(c\_i) → **\[c\] = \[λ\_d\]ᵀ \[c\_ph\] \[λ\_d\]**.
3. Spring elongations y\_k = Δ₀ + \[λ\_k\] x → **\[k\_el^I\] = \[λ\_k\]ᵀ \[k\_ph\] \[λ\_k\]**, plus **\[k\_el^II\] = Σ Δ\_i0 k\_i \[ν\_ki\]**.
4. Gravity → **\[k\_g\] = Σ m\_i g \[ν\_hi\]** (Hessian of the c.o.m. height).
5. Forces δy\_f = \[λ\_f\] δx → **f = \[λ\_f\]ᵀ F**.

```latex
[m]\ddot{\underline{x}} + [c]\dot{\underline{x}} + [k]\underline{x} = \underline{f}(t)
```

All Jacobians are evaluated at equilibrium. \[m\] and \[k\] come out symmetric because of the λᵀ\[·\]λ structure.

### On your blackboard (L01)

- [ ] Lagrange's equation (scalar and matrix form)
- [ ] T = ½ m(x) ẋ² and m(x) = Σ(m λ² + J λ\_θ²)
- [ ] General nonlinear 1-dof equation with the ½(dm/dx) ẋ² term
- [ ] Expansion of V\_el to second order and the three-term discussion (constant, linear cancels, quadratic)
- [ ] k = k\_el^I + k\_el^II + k\_g with all three formulas
- [ ] Matrix recipe: \[m\] = λᵀ m\_ph λ, \[c\], \[k\_el\], \[k\_g\], f = λ\_fᵀ F
- [ ] Pendulum: k\_g = m g l as the example of gravitational stiffness

### Likely oral questions (L01)

1. **Why do we use Lagrange's equations instead of Newton?** Ideal constraints do no virtual work, so constraint forces never appear. One equation per dof, a systematic procedure. Cite the slider-crank: 9 equations vs 1.
2. **Derive the equation of motion of a generic 1-dof system.** Write T with Jacobians → m(x), then D → c(x), V → f\_c(x), δW → f(x,t), then apply Lagrange. Point out the ½(dm/dx) ẋ² term.
3. **How do you linearise? Why is each rule true?** Inertia and damping: evaluate at equilibrium because the extra terms are products of small quantities. Stiffness: needs V to second order. End with the final m₀ẍ + c₀ẋ + kx = f₀.
4. **What is the second-order (geometric) stiffness? When is it zero?** k\_i Δ\_i0 ν\_ki. Zero if the spring is unloaded at equilibrium or the elongation is linear in x. Not always negligible (railway suspension).
5. **When does gravity appear in the linearised equations?** Only through the Hessian of the c.o.m. height. With x = 0 at equilibrium and linear height relationships, gravity disappears (it only sets the static deflection).
6. **What is a linear system and what are its properties?** Constant Jacobians, zero Hessians, one equilibrium, exact equations for large motion.
7. **Write the linearised equations of an n-dof system in matrix form.** The recipe of section 6.

### Traps and follow-ups (L01)

- "Why does the linear term in V disappear?" → stationarity of total potential energy at equilibrium: the elastic linear term cancels with the gravity linear term. It does not vanish on its own.
- "Is linearisation valid around any configuration?" → around an equilibrium (or steady state), for small motion only. Different equilibria give different linear models.
- "Why is \[m\] symmetric and positive definite?" → \[λ\]ᵀ\[m\_ph\]\[λ\] with positive masses; T > 0 for every non-zero velocity.
- Sign of k: a negative k (e.g. inverted pendulum, k\_g = −m g l) means unstable equilibrium. This links to L02 and L13.

## L02 — Solving the equations of motion (1-dof and n-dof)

**Big idea:** the total motion is the free motion (homogeneous solution, which dies out with damping) plus the steady-state forced motion (particular solution). Free motion gives natural frequencies and modes, forced motion gives the frequency response function (FRF).

### 1. Free motion of 1 dof

Try x = x₀ e^{λt} in mẍ + cẋ + kx = 0, which gives the characteristic equation mλ² + cλ + k = 0:

```latex
\lambda_{1,2} = -\frac{c}{2m} \pm \sqrt{\left(\frac{c}{2m}\right)^2 - \frac{k}{m}}
```

Definitions: ω = √(k/m) (undamped natural frequency), c\_cr = 2mω (critical damping), h = c/c\_cr (damping ratio).

| Case | Roots | Free motion |
| --- | --- | --- |
| c = 0 | λ = ±iω | x = A cosωt + B sinωt = C cos(ωt + φ), harmonic forever |
| 0 < h < 1 | λ = −hω ± iω\_d, ω\_d = ω√(1−h²) | x = C e^{−hωt} cos(ω\_d t + φ), decaying oscillation |
| h > 1 | two real negative roots | x = A e^{−α₁t} + B e^{−α₂t}, no oscillation |

**Why complex-conjugate constants:** the general solution c₁e^{−iωt} + c₂e^{iωt} must be real, so c₁ = (A + iB)/2 and c₂ = (A − iB)/2. Using Euler's formula this gives A cosωt + B sinωt. A and B come from the initial conditions (A = x₀, B = v₀/ω). ω does not depend on them.

Critical damping is the **minimum** damping that gives a non-oscillatory free motion. For h = 0.01, ω\_d ≈ ω.

### 2. Forced motion of 1 dof (harmonic force)

x(t) = x\_g(t) + x\_p(t). With damping x\_g dies out, so x\_p is the **steady-state** response.

**Complex trick:** write the cos equation and the sin equation, multiply the second by i and add: mẍ\* + cẋ\* + kx\* = F e^{iΩt}. Try x\* = X e^{iΩt}:

```latex
\left(-\Omega^2 m + i\Omega c + k\right) X = F \quad\Rightarrow\quad X = G(i\Omega)\,F, \quad G(i\Omega) = \frac{1}{k - \Omega^2 m + i\Omega c}
```

The real response is x\_p = |X| cos(Ωt + ψ): same frequency as the force, amplitude |G|·F, phase ψ = ∠G.

Non-dimensional form (useful on the blackboard):

```latex
G(i\Omega) = \frac{1/k}{1 - (\Omega/\omega)^2 + 2ih\,(\Omega/\omega)}
```

**Three frequency ranges (phasor interpretation).** Each term of −Ω²mX + iΩcX + kX = F is a rotating vector.

| Range | Which term balances the force | Magnitude of G | Phase |
| --- | --- | --- | --- |
| Quasi-static, Ω ≪ ω | Elastic, kX | ≈ 1/k, flat | ≈ 0 |
| Resonance, Ω ≈ ω | Inertia and elastic cancel (mΩ² = k), only damping is left | Peak ≈ 1/(2hk) | −π/2 |
| Seismographic, Ω ≫ ω | Inertia, mΩ²X | ≈ 1/(mΩ²), falls as Ω⁻² | ≈ −π |

Sketch the Bode diagram (magnitude and phase) for h = 0, 0.05, 0.1, 0.707 and be ready to explain every part of it with the table above.

### 3. n dof: free undamped motion

&#91;m\]ẍ + \[k\]x = 0. Try x = x₀ e^{iωt}:

```latex
\left(-\omega^2 [m] + [k]\right)\underline{x}_0 = \underline{0}, \qquad \det\left(-\omega^2[m] + [k]\right) = 0
```

**Why the exponent is purely imaginary:** \[m\] and \[k\] are symmetric and positive definite. \[m\] because T = ½ẋᵀ\[m\]ẋ > 0 for any motion. \[k\] because a stable equilibrium is a minimum of V (Dirichlet/Lagrange theorem), so V = ½xᵀ\[k\]x > 0.

The determinant is a polynomial of degree 2n in ω: n natural frequencies ω₁ … ωₙ. For each ω\_j the matrix is singular: delete one equation, set one entry of x₀ to 1, and solve for the **mode** x₀^(j). It is defined up to an arbitrary constant.

General free motion:

```latex
\underline{x}(t) = \sum_{j=1}^{n} \underline{x}_0^{(j)}\, C_j \cos(\omega_j t + \varphi_j)
```

ω\_j and x₀^(j) depend only on \[m\] and \[k\]. C\_j and φ\_j depend only on the initial conditions: from \[Φ\]A = x(0) and \[Φ\]B\* = ẋ(0).

**Practical method:** pre-multiply by \[m\]⁻¹. The ω\_j² are the **eigenvalues** and the modes are the **eigenvectors** of \[m\]⁻¹\[k\]. Eigenvectors are linearly independent, so the **modal matrix** \[Φ\] = \[x₀^(1) … x₀^(n)\] is non-singular.

**Physical meaning of a mode (worked example in the notes).** Two masses m, springs k–2k–k: ω₁ = √(k/m) with mode {1, 1} (masses move together, the middle spring is not deformed), and ω₂ = √(5k/m) with mode {1, −1} (they move in opposition). The ratio of absolute values is the amplitude ratio. The relative sign is the relative phase (same sign = in phase, opposite = counter-phase). Undamped modes are real, so coordinates are always exactly in phase or exactly in counter-phase.

### 4. n dof: free damped motion

Try x = x₀ e^{λt}: det(λ²\[m\] + λ\[c\] + \[k\]) = 0, giving 2n complex λ. In practice, rewrite in **state form** ż = \[A\]z with z = {ẋ; x} and compute the eigenvalues of the 2n×2n matrix \[A\].

- **Low damping:** n complex-conjugate pairs λ = −α\_j ± iω\_j. The motion is n decaying oscillations. The eigenvectors are **complex**, so each coordinate has its own phase and reaches its maximum at a different time.
- **High damping:** some λ become real and negative, giving non-oscillatory decaying terms.
- &#91;c\] positive definite means a dissipative system, so all real parts are negative.

### 5. n dof: forced harmonic response and the FRF matrix

```latex
\left(-\Omega^2[m] + i\Omega[c] + [k]\right)\underline{X} = \underline{F} \quad\Rightarrow\quad \underline{X} = [G(i\Omega)]\,\underline{F}
```

(−Ω²\[m\] + iΩ\[c\] + \[k\]) is the **mechanical impedance matrix**. Its inverse \[G(iΩ)\] is the **FRF matrix**. Element G\_ij is the response (amplitude and phase) of coordinate i to a unit harmonic force on coordinate j. Use superposition to combine forces.

With damping the impedance is never singular. Without damping it is singular exactly at Ω = ω\_j: the response grows linearly in time (ideal resonance).

### 6. Periodic excitation

Any periodic force is a Fourier series f(t) = F₀ + Σ(A\_k cos kΩ₀t + B\_k sin kΩ₀t), with Ω₀ = 2π/T. By linearity, the steady response is the sum of the responses to each harmonic, each computed with G(ikΩ₀). A harmonic kΩ₀ close to ω can cause resonance even if the fundamental is far from it. Transient and random excitation are outside the course.

### On your blackboard (L02)

- [ ] Characteristic equation and the three damping cases, with ω, c\_cr = 2mω, h, ω\_d = ω√(1−h²)
- [ ] Complex method: X = F / (k − mΩ² + icΩ) and the non-dimensional form
- [ ] Bode diagram of a 1-dof system for several h, with the three ranges labelled
- [ ] Phasor diagram at resonance (inertia and elastic cancel)
- [ ] Eigenproblem (−ω²\[m\] + \[k\])x₀ = 0 and the link with eig(\[m\]⁻¹\[k\])
- [ ] The 2-dof example: ω₁, ω₂, modes {1,1} and {1,−1}, drawn as snapshots
- [ ] Impedance and FRF matrix, meaning of G\_ij

### Likely oral questions (L02)

1. **Free motion of a damped 1-dof system: discuss all cases.** Characteristic equation, define c\_cr and h, three cases with the shape of x(t). Say why critical damping is the boundary.
2. **Derive the FRF of a 1-dof system and comment on its Bode diagram.** Complex method, then the three ranges with the phasor balance in each. Mention the peak 1/(2hk) and phase −π/2 at resonance.
3. **How do you find natural frequencies and modes of an n-dof system? Why are the frequencies real?** Eigenproblem, det = 0, symmetric positive definite matrices. Then the eigenvalue formulation of \[m\]⁻¹\[k\].
4. **What is the physical meaning of a mode of vibration?** Use the 2-dof example with snapshots: amplitude ratios and relative signs.
5. **How do initial conditions enter the free response?** Only through C\_j, φ\_j (or A, B), solved with \[Φ\]A = x(0), \[Φ\]B\* = ẋ(0). \[Φ\] is invertible.
6. **What changes in the free motion when there is damping?** Complex λ with negative real part, complex modes, phase differences between coordinates, possible non-oscillatory terms. State-space eigenvalues.
7. **Define the FRF matrix and explain G\_ij.** Inverse of the impedance matrix, response of i to unit force on j.

### Traps and follow-ups (L02)

- The peak of |G| is not exactly at ω: it is at ω√(1−2h²) for displacement. The free damped oscillation is at ω\_d = ω√(1−h²). Don't mix them up.
- "What happens at resonance with zero damping?" → the impedance is singular and the amplitude grows linearly in time, not instantly infinite.
- "Why is the steady-state response at the force frequency, not at ω?" → x\_p is the particular solution. The natural frequency only appears in the transient x\_g.
- "Why can we restrict ourselves to harmonic forces?" → linearity + Fourier series.

## L03 — The mode superposition approach

**Big idea:** change coordinates using the modal matrix, x = \[Φ\]q. Mass and stiffness become diagonal (always), and damping becomes diagonal under proportional damping. The n-dof system splits into n independent 1-dof systems, whose solutions you already know from L02. This gives physical insight that a numerical solution cannot.

### 1. Modal approach as a change of coordinates

Any non-singular \[A\] defines new coordinates. The best choice makes the matrices diagonal, and that choice is \[Φ\] (non-singular, as shown in L02). Substitute x = \[Φ\]q and ẋ = \[Φ\]q̇ in T, D, V, δW:

```latex
T = \tfrac{1}{2}\dot{\underline{q}}^T[\Phi]^T[m][\Phi]\dot{\underline{q}}, \quad V = \tfrac{1}{2}\underline{q}^T[\Phi]^T[k][\Phi]\underline{q}, \quad \delta W = \delta\underline{q}^T[\Phi]^T\underline{f}
```

Apply Lagrange with q as coordinates:

```latex
[\Phi]^T[m][\Phi]\,\ddot{\underline{q}} + [\Phi]^T[c][\Phi]\,\dot{\underline{q}} + [\Phi]^T[k][\Phi]\,\underline{q} = [\Phi]^T\underline{f}
```

### 2. Orthogonality of the modes (derivation to know by heart)

Write the eigenproblem for modes j and i:

```latex
-\omega_j^2[m]\underline{x}_0^{(j)} + [k]\underline{x}_0^{(j)} = 0, \qquad -\omega_i^2[m]\underline{x}_0^{(i)} + [k]\underline{x}_0^{(i)} = 0
```

1. Pre-multiply the first by x₀^(i)ᵀ and the second by x₀^(j)ᵀ.
2. Transpose the first. Because \[m\] and \[k\] are symmetric, x₀^(i)ᵀ\[m\]x₀^(j) = x₀^(j)ᵀ\[m\]x₀^(i), and the same for \[k\].
3. Subtract the two equations. The stiffness terms cancel:

```latex
\left(\omega_i^2 - \omega_j^2\right)\,\underline{x}_0^{(j)T}[m]\,\underline{x}_0^{(i)} = 0
```

4. If ω\_i ≠ ω\_j, then x₀^(j)ᵀ\[m\]x₀^(i) = 0. Putting this back into either equation also gives x₀^(j)ᵀ\[k\]x₀^(i) = 0.

So the modal mass matrix and modal stiffness matrix are **diagonal**. The proof assumes distinct frequencies, but the result holds in general.

### 3. Damping: when is it diagonal too?

Not in general. The key case is **proportional (Rayleigh) damping**:

```latex
[c] = \alpha[m] + \beta[k] \quad\Rightarrow\quad [\Phi]^T[c][\Phi] = \alpha[\bar m] + \beta[\bar k]
```

α is in s⁻¹ and β in s. It is used when the real damping is unknown or too complex to model, typically the internal (material) damping of structures and FE models (L10). The modal damping ratio follows as h\_i = α/(2ω\_i) + βω\_i/2: the mass part dominates at low frequency and the stiffness part at high frequency.

With diagonal matrices, each modal coordinate obeys:

```latex
\bar m_i\,\ddot q_i + \bar c_i\,\dot q_i + \bar k_i\,q_i = \bar f_i(t), \qquad \bar f_i = \underline{x}_0^{(i)T}\underline{f}, \qquad \omega_i^2 = \bar k_i/\bar m_i
```

### 4. The 4-step solution procedure

1. From \[m\] and \[k\], compute the ω\_i and modes → \[Φ\].
2. Transform into n decoupled 1-dof equations.
3. Solve each 1-dof equation analytically (L02).
4. Go back to physical coordinates: x = \[Φ\]q = Σ x₀^(i) q\_i.

### 5. Physical insight (this is what the professor wants to hear)

**Motion is a sum of modal shapes.** x = x₀^(1)q₁ + … + x₀^(n)qₙ: each mode contributes its shape, with amplitude q\_i, and there is no cross-influence.

**Resonant mode.** If the excitation frequency Ω is near ω\_i, the system is lightly damped and the modes are well separated, then q\_i dominates. The system vibrates in the shape of mode i. The largest amplitudes are where that mode has its largest entries, and a **node** of the mode shows no resonance peak.

**Modal force.** f̄\_i = Σ x₀j^(i) f\_j: the force is weighted by the mode shape at its point of application. A force applied at a node of mode i cannot excite mode i, even at Ω = ω\_i, because it puts no energy into that mode. To excite a mode strongly, push where its shape is largest.

### 6. Worked example (2 dof, the notes' example)

Masses m, m. Springs k, 2k, k. Dampers c, 2c, c. Force f₀cosΩt on the left mass.

- Equations: \[m\] = diag(m, m), \[k\] = \[3k −2k; −2k 3k\], \[c\] = \[3c −2c; −2c 3c\]. The damping is proportional to the stiffness, so it is diagonalised.
- ω₁ = √(k/m), ω₂ = √(5k/m). Modes {1, 1} and {1, −1} (the notes normalise the first entry to 1), so \[Φ\] = \[1 1; 1 −1\].
- Modal matrices: m̄ = diag(2m, 2m), k̄ = diag(2k, 10k), c̄ = diag(2c, 10c), f̄ = \[Φ\]ᵀ{f, 0} = {f, f}.
- Decoupled equations: 2m q̈₁ + 2c q̇₁ + 2k q₁ = f(t) and 2m q̈₂ + 10c q̇₂ + 10k q₂ = f(t).
- Undamped steady state: q₀₁ = (f₀/2k)/(1 − (Ω/ω₁)²) and q₀₂ = (f₀/10k)/(1 − (Ω/ω₂)²).
- Back to physical coordinates: x₁ = q₁ + q₂ (sum) and x₂ = q₁ − q₂ (difference). With damping, the same sums are done in complex algebra.

**What to say about the Bode diagrams:**

- Two resonance peaks on both masses, at ω₁ and ω₂.
- Near ω₁ the masses move together (shape of mode 1). Near ω₂ they move in opposition (shape of mode 2).
- On the driven mass, between the peaks, there is an **anti-resonance**: the amplitude drops to zero (undamped) and the phase jumps by +π. It is the "dual" of a resonance, where the amplitude goes to infinity and the phase drops by −π. It is where the two modal contributions cancel.
- With light damping (c = 0.4k in the notes, giving h₁ = 0.04 and h₂ = 0.089), the picture is the same but peaks are finite, phase changes are smooth and the anti-resonance is a sharp minimum, not zero.

Modal damping ratio: h\_i = c̄\_i / (2√(k̄\_i m̄\_i)).

### On your blackboard (L03)

- [ ] x = \[Φ\]q and the transformed equation with \[Φ\]ᵀ\[·\]\[Φ\]
- [ ] Full orthogonality proof (4 steps)
- [ ] Rayleigh damping \[c\] = α\[m\] + β\[k\] and h\_i = α/(2ω\_i) + βω\_i/2
- [ ] Modal force f̄\_i = x₀^(i)ᵀ f and the node argument
- [ ] The 2-dof example: \[Φ\], modal mass and stiffness, the two Bode diagrams with resonances and anti-resonance

### Likely oral questions (L03)

1. **What is the modal approach and why is it useful?** Change of coordinates that decouples the equations. n known 1-dof solutions, physical insight, a basis for reduced models.
2. **Prove the orthogonality of the modes.** The 4 steps. Mention that symmetry of \[m\] and \[k\] is essential.
3. **When is the damping matrix diagonalised?** Proportional damping. Say why it is used (unknown internal damping).
4. **What is a node? What happens if you apply a force at a node?** f̄\_i = 0, no resonance of that mode.
5. **What is an anti-resonance? Where can you find one?** Minimum of the FRF between two resonances where modal contributions cancel, phase +π. Typically in the driving-point FRF.
6. **Why does the system vibrate in a modal shape near resonance?** The resonant modal coordinate dominates if damping is low and modes are well separated.

### Traps and follow-ups (L03)

- "Is the modal matrix unique?" → no, each mode has arbitrary scaling, so modal masses and stiffnesses depend on normalisation, but ω\_i = √(k̄\_i/m̄\_i) does not.
- "What if damping is not proportional?" → \[Φ\]ᵀ\[c\]\[Φ\] has off-diagonal terms. If they are small (low damping), neglect them. Otherwise use complex modes from the state-space problem (mentioned in L04).
- "How many modes do you need?" → those with ω\_i inside or slightly above the frequency range of the excitation. Higher modes respond quasi-statically. This is the idea behind modal truncation (L09, L10).

## L04 — Identification of modal parameters

**Big idea:** L03 went from the model to the modes. L04 goes the other way: measure the FRF of the real system, then fit the modal expression of the FRF to extract natural frequencies, damping ratios and mode shapes. This is used for **model updating** (tune the model) and **model validation** (check it), or directly to understand and fix a real system.

### 1. Analytical FRF in modal form (derivation)

One harmonic force F\_k e^{iΩt} on coordinate k. In modal coordinates (assuming damping is diagonalised), the modal force on mode i is x₀k^(i) F\_k:

```latex
\bar m_{ii}\ddot q_i + \bar c_{ii}\dot q_i + \bar k_{ii} q_i = x_{0k}^{(i)} F_k e^{i\Omega t} \;\Rightarrow\; Q_i = \frac{x_{0k}^{(i)} F_k}{-\Omega^2\bar m_{ii} + i\Omega\bar c_{ii} + \bar k_{ii}}
```

The response at j is x\_j = Σ x₀j^(i) q\_i, so:

```latex
G_{jk}(i\Omega) = \sum_{i=1}^{n} \frac{x_{0j}^{(i)}\,x_{0k}^{(i)}}{-\Omega^2\bar m_{ii} + i\Omega\bar c_{ii} + \bar k_{ii}}
```

The FRF is a sum of n single-dof FRFs, each weighted by the product of the mode shape at the output (j) and at the input (k). It contains every modal parameter, so fitting it to measurements identifies them.

### 2. Measuring the FRF

SIMO test: one input force at k (load cell), n\_m outputs at j (often accelerometers, integrated twice, watching for drift).

**Harmonic excitation (shaker).** Force F\_k cosΩt, steady response x\_j0 cos(Ωt + ∠X\_j). The phase comes from the time delay: ∠X\_j = −Δt·Ω. Then G\_jk = (x\_j0/F\_k) e^{i∠X\_j}. Repeat for many Ω (step by step or with a slow swept sine).

**Impulsive excitation (instrumented hammer).** An ideal impulse has a flat spectrum, so one hit excites a whole frequency band.

- A **stiffer tip** gives a shorter impact and a wider frequency band. A softer tip concentrates energy at low frequency.
- Sample at f\_s for a duration T: n\_s = f\_s·T samples, compute the DFT.
- Frequency resolution f₀ = 1/T. Maximum frequency f\_s/2 (Shannon).
- G\_jk(iΩ\_l) = X\_j,l / F\_k,l (complex ratio of the DFT lines).
- Don't use frequency lines where the force spectrum is too low: poor signal-to-noise ratio.

### 3. Identification: one mode at a time

If the modes are **well separated** and the system is **lightly damped**, near each resonance only the resonant term of G\_jk matters. So you identify one mode per frequency window.

**Method A: residual minimisation (more accurate, needs a computer)**

```latex
G_{jk}(i\Omega) \approx \frac{A_j + iB_j}{-\Omega^2\bar m_{ii} + i\Omega\bar c_{ii} + \bar k_{ii}} + (C_j + iD_j) + \frac{E_j + iF_j}{\Omega^2}
```

- First term: the resonant mode (exact).
- C + iD: residual of the higher modes (they respond quasi-statically, roughly constant).
- (E + iF)/Ω²: residual of the lower modes (seismographic range, falling as 1/Ω²).
- Gains are complex because with non-proportional damping you need complex modes.
- Unknowns: 3 + 6n\_m. Equations: n\_f·n\_m (frequency lines × outputs). Overdetermined, nonlinear least squares, solved iteratively.
- A\_j gives the mode shape at j (up to a scale factor). **Checks:** B\_j ≪ A\_j (real modes are acceptable), and C, D, E, F ≪ A\_j (residuals small). If not, reject the result.

**Method B: analytical formulae (keep only the resonant term)**

| Parameter | Method | Formula |
| --- | --- | --- |
| Natural frequency ω\_i | Frequency of the magnitude peak (exact peak at ω\_i√(1−2h²) ≈ ω\_i) | — |
| Damping h\_i (phase derivative) | Slope of the phase at resonance | d∠G/dΩ at ω\_i = −1/(h\_i ω\_i) |
| Damping h\_i (half-power points) | Frequencies ω₁, ω₂ where the magnitude is Q/√2 | h\_i = (ω₂² − ω₁²)/(4ω\_i²) ≈ (ω₂ − ω₁)/(2ω\_i) |
| Mode shape at j | Imaginary part of G\_jk at ω\_i | G\_jk(iω\_i) = −i x₀j^(i) x₀k^(i)/(ω\_i c̄\_ii) |

**Phase-derivative derivation (be ready to sketch it).** With a = Ω/ω\_i, the phase is ∠G = −arctan(2h a/(1 − a²)). Differentiate with the chain rule and evaluate at a = 1: d∠G/da = −1/h. Since da/dΩ = 1/ω\_i, d∠G/dΩ = −1/(hω\_i). Low damping gives a steep phase drop. Average over several outputs j to reduce error.

**Mode shape: why the imaginary part, not the magnitude.** At Ω = ω\_i, k̄ = ω\_i² m̄, so the resonant term is purely imaginary. The non-resonant modes are in their quasi-static or seismographic range, so their contribution is nearly real. Taking the imaginary part rejects them better than taking the magnitude.

### On your blackboard (L04)

- [ ] Modal FRF formula G\_jk = Σ x₀j x₀k / (k̄ − Ω²m̄ + iΩc̄)
- [ ] Sketch: total FRF magnitude with the single-mode contributions dashed underneath
- [ ] Hammer test: force spectrum flat up to a cut-off set by the tip; f₀ = 1/T, f\_max = f\_s/2
- [ ] The approximated FRF with the two residual terms and what each represents
- [ ] Half-power points sketch and formula; phase-derivative formula
- [ ] Mode shape = Im(G\_jk) at ω\_i

### Likely oral questions (L04)

1. **Why identify modal parameters?** Model updating, model validation, direct diagnosis of a real system.
2. **Derive the modal expression of the FRF.** Single force on k, modal decoupling, back-transformation. Interpret: sum of 1-dof FRFs weighted by mode shapes at input and output.
3. **How do you measure an FRF with a hammer? What limits the frequency range?** Tip stiffness (force spectrum), Shannon (f\_s/2), resolution 1/T, signal-to-noise ratio.
4. **Why can you identify one mode at a time? When does it fail?** Separated modes and low damping. Fails with close modes or high damping.
5. **Explain the residual terms.** Higher modes quasi-static, constant. Lower modes seismographic, ∝ 1/Ω².
6. **Derive the half-power or phase-derivative formula for damping.** One of the two.
7. **How do you get the mode shape from FRFs? Why the imaginary part?** Non-resonant terms are nearly real.

### Traps and follow-ups (L04)

- "What is the logarithmic decrement and why is it limited?" → ln of the ratio of successive peaks of the free decay ≈ 2πh. It gives damping only, and for n dof the modal contributions are mixed in the free decay.
- "Why is a stiffer hammer tip not always better?" → it spreads the same energy over a wider band, so less energy per frequency line and a worse signal-to-noise ratio at low frequency.
- "Driving-point vs transfer FRF?" → j = k: all terms x₀k² are positive, so you get an anti-resonance between every pair of resonances.

## L05 — Introduction to distributed-parameter systems

**Big idea:** when you cannot split a system into rigid masses and massless springs, inertia and elasticity are spread through the body. You then need solid mechanics (strain, stress, constitutive law). Beams make it manageable: each section moves as a rigid body, so one coordinate x describes everything.

### 1. Lumped or distributed? It depends on the frequency range

The choice depends on the **aim of the study and the frequency band**. Example from the notes: a car body as a rigid body is fine for comfort, road holding and handling up to about 10–15 Hz. For noise up to a few kHz you need the flexible vibration of the body, doors, roof and panels. A turbine-generator shaft in bending must be a continuous beam.

### 2. Rigid vs deformable motion

Rigid motion: distances between points and angles between segments do not change. In 2D it is described by 3 parameters (2 translations of a point + 1 rotation). Deformable motion changes lengths and angles, so you measure these changes with **strains** (non-dimensional).

### 3. Strain (small displacements)

Displacements u(x,y), v(x,y) are infinitesimal, so higher powers are neglected.

- **Normal strain** (change in length of a fibre): ε\_x = ∂u/∂x, ε\_y = ∂v/∂y. Derivation: segment AB = dx becomes dx + u(x+dx) − u(x) = dx + (∂u/∂x)dx.
- **Shear strain** (change of the right angle between two fibres): γ\_xy = γ₁ + γ₂ = ∂v/∂x + ∂u/∂y.
- **3D:** three normal strains (ε\_x, ε\_y, ε\_z) and three shear strains (γ\_xy, γ\_yz, γ\_zx), six in total.

### 4. Stress

Force per unit area on an infinitesimal face, in N/m² = Pa. **Normal stress** σ\_x = dF\_n/dA. **Shear stress** τ\_xy: the first index is the normal to the face, the second the direction of the force. A face with normal −x carries stresses opposite to the +x face (Newton's third law).

**Symmetry of the stress tensor:** moment equilibrium of the infinitesimal element about its centre gives τ\_xy = τ\_yx (and the same for yz and zx). In dynamics the inertia moment is a higher-order infinitesimal, so symmetry still holds. So there are 6 independent stress components, matching the 6 strains.

### 5. Constitutive law

Tensile test: real materials show a nonlinear curve with hysteresis (energy dissipation). For metals below the yield strength, hysteresis is small, and below the proportionality limit the curve is linear: **σ = Eε**. Dissipation is then reintroduced with simplified damping models (e.g. Rayleigh damping, L03 and L10).

Isotropic linear elastic law (generalised Hooke's law):

```latex
\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right], \quad \gamma_{xy} = \frac{\tau_{xy}}{G}, \quad G = \frac{E}{2(1+\nu)}
```

Steel: E ≈ 206 000 MPa, ν ≈ 0.28, G ≈ 80 000 MPa. Only two of the three constants are independent.

### 6. Beams

A beam has one dimension much larger than the other two: a section extruded along an axis. The course uses straight axis and constant section.

**Key assumption:** each section moves as a rigid body. So the deformation is described by the rigid motion of each section as a function of x and t, and the stresses on a section can be summarised by their resultants, the **internal forces**:

- **N** axial force (positive in tension)
- **T** shear force
- **M** bending moment
- **M\_t** torsional moment (3D only)

Sign conventions are opposite on the two faces of a cut, so Newton's third law is built in.

**Three deformation modes:**

| Mode | What the sections do | Internal force | Lesson |
| --- | --- | --- | --- |
| Axial | Translate along the axis | N | L06 |
| Bending | Translate perpendicular to the axis and rotate | T, M | L07 |
| Torsion | Rotate about the axis (+ warping if not polar-symmetric) | M\_t | L08 |

For sections with two axes of symmetry the three are **decoupled**: study them separately and superpose.

### On your blackboard (L05)

- [ ] Sketch of an infinitesimal rectangle deformed by u(x) only, by v(y) only, and in shear, with ε\_x = ∂u/∂x and γ\_xy = ∂u/∂y + ∂v/∂x
- [ ] Element with τ\_xy and τ\_yx and the moment balance giving symmetry
- [ ] Generalised Hooke's law and G = E/(2(1+ν))
- [ ] Beam internal forces N, T, M with sign conventions
- [ ] Table of the three deformation modes

### Likely oral questions (L05)

1. **When do you need a distributed-parameter model instead of a lumped one?** When you can't separate inertia and elasticity. It depends on the frequency range (car example).
2. **Define normal and shear strain and derive them.** Infinitesimal rectangle, first-order expansion.
3. **Why is the stress tensor symmetric? Does it still hold in dynamics?** Moment balance; the inertia term is a higher-order infinitesimal.
4. **What constitutive law do we use and what does it neglect?** Linear isotropic elastic law; it neglects hysteresis, so damping is added separately.
5. **What is a beam and why is it simpler than a generic solid?** Rigid sections, one space coordinate, internal forces; decoupled axial, bending, torsion.

### Traps and follow-ups (L05)

- "Why can we neglect the term from the inertia moment in the symmetry proof?" → it is proportional to dx·dy·(dx² + dy²), one order higher than the stress terms.
- "How many independent elastic constants for an isotropic material?" → two (E and ν, or E and G).
- "When are axial, bending and torsion coupled?" → non-symmetric sections, or beams not on a common axis (frames, L07 figure).

## L06 — Axial vibration of beams

**Big idea:** axial vibration obeys the 1D wave equation. In an infinite medium the solution is two waves travelling at c = √(E/ρ). In a finite beam, reflections create standing waves: separation of variables plus boundary conditions gives an infinite sequence of natural frequencies and mode shapes.

**Assumptions:** linear elastic material, constant section, homogeneous material, only axial forces (so only N ≠ 0), and the Poisson contraction of the section is neglected. Then every point of a section moves by u(x, t).

### 1. Equation of motion (derivation)

1. Stress and force: σ\_x = N/A and ε\_x = ∂u/∂x, so **N = EA ∂u/∂x**.
2. D'Alembert on the element dx: −N(x) + N(x+dx) = dm ∂²u/∂t², with dm = ρA dx = m dx (m = mass per unit length).
3. Expand N(x+dx) = N + (∂N/∂x)dx, so ∂N/∂x = m ∂²u/∂t².
4. Substitute N:

```latex
EA\,\frac{\partial^2 u}{\partial x^2} = m\,\frac{\partial^2 u}{\partial t^2} \quad\Longleftrightarrow\quad \frac{\partial^2 u}{\partial t^2} = c^2\frac{\partial^2 u}{\partial x^2}, \qquad c = \sqrt{\frac{EA}{m}} = \sqrt{\frac{E}{\rho}}
```

c depends only on the material, not on the section. For steel, c ≈ 5000 m/s. The same equation describes torsion of shafts, strings and 1D acoustics.

**Discrete vs continuous:** n functions x\_i(t) and n ODEs become one function u(x, t) and one PDE. It is the limit n → ∞.

### 2. Propagative solution (d'Alembert)

```latex
u(x,t) = f_1(x - ct) + f_2(x + ct)
```

Check: both terms satisfy the equation with f'' on each side. Interpretation: f₁ is a waveform that keeps its shape and moves right at speed c (at t = 0 it is the initial deformation, at time t it is shifted by ct). f₂ moves left. An initial deformation launches two waves in opposite directions. Useful for infinite media.

### 3. Stationary solution (separation of variables)

In a finite beam, waves reflect at the ends and interfere, giving standing waves: u(x, t) = α(x)β(t). Substituting:

```latex
\frac{\ddot\beta(t)}{\beta(t)} = c^2\,\frac{\alpha''(x)}{\alpha(x)} = -\omega^2
```

The left side depends only on t, the right only on x, so both equal a constant. It must be **negative** (−ω²): a positive constant would give exponentially growing β(t), impossible for a conservative stable system.

```latex
\ddot\beta + \omega^2\beta = 0 \Rightarrow \beta = C\cos(\omega t + \varphi); \qquad \alpha'' + \left(\frac{\omega}{c}\right)^2\alpha = 0 \Rightarrow \alpha = A\cos\frac{\omega x}{c} + B\sin\frac{\omega x}{c}
```

This is valid for any boundary conditions. The boundary conditions give the natural frequencies.

### 4. Clamped–clamped beam

u(0, t) = 0 gives A = 0. u(L, t) = 0 gives B sin(ωL/c) = 0. B = 0 is the trivial solution, so:

```latex
\sin\frac{\omega L}{c} = 0 \;\Rightarrow\; \omega_k = \frac{k\pi}{L}\,c = \frac{k\pi}{L}\sqrt{\frac{E}{\rho}}, \qquad \alpha_k(x) = \sin\frac{k\pi x}{L}, \quad k = 1, 2, \dots
```

Infinitely many frequencies, **evenly spaced** (ω\_k ∝ k). General free motion: u = Σ B\_k sin(kπx/L) cos(ω\_k t + φ\_k), with B\_k, φ\_k from the initial conditions. Mode 1: all sections in phase, max at mid-span. Mode 2: halves in counter-phase, node at mid-span. Higher modes have more nodes. In general, higher frequency means a more "winding" mode shape.

**Other boundary conditions you should be able to do:**

| Case | Conditions | Frequency equation | ω\_k |
| --- | --- | --- | --- |
| Clamped–clamped | u = 0 at both ends | sin(ωL/c) = 0 | kπc/L |
| Free–free | N = 0, so ∂u/∂x = 0, at both ends | sin(ωL/c) = 0, plus a rigid mode at ω = 0 | kπc/L, mode cos(kπx/L) |
| Clamped–free | u(0) = 0, ∂u/∂x(L) = 0 | cos(ωL/c) = 0 | (2k−1)πc/(2L) |

A free end means zero axial force, which is a **natural** boundary condition (on the derivative). A clamped end is a **geometric** one (on u itself).

### On your blackboard (L06)

- [ ] Element dx with N(x), N(x+dx) and the inertia force; derivation of the wave equation
- [ ] c = √(E/ρ) and why it does not depend on the section
- [ ] Propagative solution with the sketch of two travelling waves
- [ ] Separation of variables and why the constant is −ω²
- [ ] Clamped–clamped: ω\_k = kπc/L, sketch of the first 3 modes with nodes
- [ ] Clamped–free result as a quick variant

### Likely oral questions (L06)

1. **Derive the equation of axial vibration of a beam.** The 4 steps above. State the assumptions.
2. **What is c and what does it depend on?** Propagation speed, √(E/ρ), material only.
3. **Propagative vs stationary solution: when do you use each?** Infinite medium vs finite beam with reflections.
4. **Find the natural frequencies of a clamped–clamped (or clamped–free) bar.** Separation of variables, apply BCs, avoid the trivial solution.
5. **Why must the separation constant be negative?** Otherwise exponential growth: physically impossible.
6. **Compare a continuous system with an n-dof system.** Infinite modes, PDE instead of ODEs, eigenproblem becomes a boundary-value problem.

### Traps and follow-ups (L06)

- "Why do axial frequencies not depend on A?" → stiffness EA and mass ρA both scale with A.
- "Free–free bar: what about ω = 0?" → it is the rigid translation mode.
- "Are axial frequencies usually high or low compared to bending?" → high. That is why bending (L07) is usually the critical one.

## L07 — Bending vibration of beams

**Big idea:** bending of a slender (Euler–Bernoulli) beam gives a 4th-order-in-space PDE. Separation of variables gives a combination of cos, sin, cosh, sinh, and four boundary conditions (two per end) lead to the frequency equation det\[H(γ)\] = 0. Bending frequencies are usually the lowest and most important in practice.

### 1. Assumptions

1. Linear elastic material.
2. Constant section, homogeneous material.
3. Plane bending in x–z; the section has two axes of symmetry, so the two bending planes are decoupled from each other and from torsion.
4. **Euler–Bernoulli:** shear deformation and rotary inertia are neglected. Valid for slender beams (h/L ≪ 1). For thick beams (h/L around 1/10 or more) use Timoshenko theory.

### 2. Kinematics of pure bending

Sections stay plane and **perpendicular to the deformed axis**, so the rotation is α = ∂w/∂x. A point at height z moves by u = −z ∂w/∂x. Then:

```latex
\varepsilon_x = -z\frac{\partial^2 w}{\partial x^2}, \qquad \sigma_x = -Ez\frac{\partial^2 w}{\partial x^2}
```

Stress is linear across the section (zero on the neutral axis). Integrating over the section: N = 0 (stress is antisymmetric in z), and the moment is

```latex
M = EI\,\frac{\partial^2 w}{\partial x^2}, \qquad I = \int_A z^2\,dA
```

Rectangle b×h: I = bh³/12. Solid circle: I = πD⁴/64. EI is the **bending stiffness**.

### 3. Equation of motion (derivation)

Element dx with T, M on each face and inertia force m dx ∂²w/∂t² (no inertia torque: rotary inertia neglected).

1. **Moment balance** about the element centre, dropping dx² terms: **T = ∂M/∂x**.
2. **Vertical force balance:** ∂T/∂x = −m ∂²w/∂t².
3. Combine with M = EI ∂²w/∂x²:

```latex
EI\,\frac{\partial^4 w}{\partial x^4} + m\,\frac{\partial^2 w}{\partial t^2} = 0
```

The notes write it as EI w'''' = −m ẅ, the same equation. Unlike the axial case, this is **not** a simple wave equation: bending waves are dispersive (speed depends on frequency), which is why the notes skip the propagative solution.

### 4. Stationary solution

w = α(x)β(t), separation constant −ω²:

```latex
\ddot\beta + \omega^2\beta = 0, \qquad \alpha^{IV} - \gamma^4\alpha = 0, \quad \gamma^4 = \frac{m\,\omega^2}{EI}
```

Try α = e^{λx}: λ⁴ = γ⁴, so λ = ±iγ, ±γ. Choosing the constants so that α is real:

```latex
\alpha(x) = A\cos\gamma x + B\sin\gamma x + C\cosh\gamma x + D\sinh\gamma x
```

Four constants, so four boundary conditions (in general, as many as the order of the spatial derivative).

### 5. Boundary conditions (must know)

| End | Conditions | Type |
| --- | --- | --- |
| Clamped | w = 0, ∂w/∂x = 0 | Two geometric |
| Free | M = 0 → ∂²w/∂x² = 0; T = 0 → ∂³w/∂x³ = 0 | Two natural (from equilibrium of an end element as dx → 0) |
| Pinned | w = 0, ∂²w/∂x² = 0 | One geometric, one natural |

At a clamp you cannot write natural conditions: the unknown reaction force and moment would appear.

### 6. Pinned–pinned beam (analytical)

At x = 0: w = 0 gives A + C = 0, and w'' = 0 gives −A + C = 0, so A = C = 0. At x = L: B sinγL + D sinhγL = 0 and −B sinγL + D sinhγL = 0, so D sinhγL = 0 and D = 0 (sinh is zero only at 0). Non-trivial solution: sinγL = 0.

```latex
\gamma_k L = k\pi \;\Rightarrow\; \omega_k = \left(\frac{k\pi}{L}\right)^2\sqrt{\frac{EI}{m}}, \qquad \alpha_k = \sin\frac{k\pi x}{L}
```

Same mode shapes as the clamped–clamped axial bar, but frequencies grow with **k²** (spacing increases), and with 1/L².

### 7. General boundary conditions: the cantilever

Clamped at 0, free at L. The four conditions give \[H(γ)\]{A, B, C, D} = 0, a homogeneous system. Non-trivial solutions require

```latex
\det[H(\gamma)] = 0 \quad\Rightarrow\quad \cos\gamma L\,\cosh\gamma L = -1 \;\text{(cantilever)}
```

This is a transcendental equation with infinitely many roots, solved numerically: γ₁L ≈ 1.875, γ₂L ≈ 4.694, γ₃L ≈ 7.855, and for large k, γ\_kL ≈ (2k−1)π/2. Then ω\_k = γ\_k² √(EI/m). The mode comes from substituting γ\_k back and fixing one constant.

### 8. Systems of beams

Beam on three supports (A pinned, C pinned in the middle, B pinned): one solution with 4 constants per span, 8 unknowns. Boundary conditions: 2 at A, 2 at B, and 4 at C: w₁ = 0, w₂ = 0, equal rotation, and equal moment (moment equilibrium of the element over the support). Vertical equilibrium at C cannot be used because the pin reaction is unknown. Same γ in both spans (same ω, EI, m). Again det\[H\] = 0, now 8×8. For frames (beams on different axes, e.g. a portal) axial and bending couple and it gets worse. This motivates **FEM** (L10).

### On your blackboard (L07)

- [ ] Euler–Bernoulli assumptions and when they fail
- [ ] Kinematics u = −z w', ε = −z w'', M = EI w''
- [ ] Element with T and M, the two balances, final PDE
- [ ] γ⁴ = mω²/EI and the cos/sin/cosh/sinh solution
- [ ] Table of boundary conditions (clamped, free, pinned)
- [ ] Pinned–pinned full derivation and ω\_k = (kπ/L)²√(EI/m)
- [ ] Cantilever: det\[H\] = 0 and the first root 1.875
- [ ] Beam on three supports: count of unknowns and conditions

### Likely oral questions (L07)

1. **Derive the bending equation of motion.** Assumptions, M = EI w'', element balances.
2. **What are the Euler–Bernoulli assumptions and when are they not valid?** Slender beam, neglect shear and rotary inertia; thick beams need Timoshenko.
3. **Write the boundary conditions for clamped, free and pinned ends. Geometric vs natural?** Table; natural ones come from equilibrium of the end element.
4. **Find the natural frequencies of a pinned–pinned beam.** Full derivation.
5. **How do you do it for a cantilever, or for a beam on several supports?** \[H(γ)\], det = 0, numerical roots, matching conditions at internal supports.
6. **Compare axial and bending frequencies.** k vs k², L vs L², bending lower for slender beams.

### Traps and follow-ups (L07)

- "Why can't you write vertical equilibrium at the intermediate support?" → the unknown pin reaction would enter.
- "How does an axial preload change bending frequencies?" → tension stiffens (raises ω), compression softens (towards buckling). It is the continuous analogue of the second-order stiffness in L01.
- "Why is the procedure for systems of beams impractical?" → a new \[H\] for every geometry, coupling for frames. Hence FEM.

## L08 — Torsional vibration of beams

**Big idea:** torsion of a shaft with a polar-symmetric section is mathematically identical to axial vibration: the same wave equation, with the rotation ϑ(x, t) instead of u, and c = √(G/ρ) instead of √(E/ρ). Everything from L06 transfers.

**Assumptions:** small displacements, linear elastic, constant section, homogeneous, no damping, loads only at the ends, **polar symmetry** of the section (so no warping and each section rotates rigidly).

### 1. Kinematics, strain and stress

A section rotates by ϑ(x). A point (y, z) moves by u = 0, v = −zϑ, w = yϑ. So the only strains are shears:

```latex
\gamma_{xy} = -z\,\frac{\partial\vartheta}{\partial x}, \quad \gamma_{zx} = y\,\frac{\partial\vartheta}{\partial x} \quad\Rightarrow\quad \tau = G\,r\,\frac{\partial\vartheta}{\partial x}
```

The total shear stress is circumferential and proportional to the distance r from the centre. No normal stress, so N = 0 and M = 0: torsion is decoupled from axial and bending. Shear forces are zero by antisymmetry. Integrating the moment of the stresses:

```latex
M_t = G I_P\,\frac{\partial\vartheta}{\partial x}, \qquad I_P = \int_A (y^2 + z^2)\,dA = \frac{\pi D^4}{32}\;\text{(solid)}, \quad \frac{\pi(D_e^4 - D_i^4)}{32}\;\text{(hollow)}
```

For non-circular sections: M\_t = G I\_T ∂ϑ/∂x, with I\_T (torsional constant) from handbooks, and I\_T ≠ I\_P.

### 2. Equation of motion

Element dx: M\_t(x) on the left, M\_t(x+dx) on the right, and inertia moment ρ I\_P dx ∂²ϑ/∂t². D'Alembert:

```latex
\frac{\partial M_t}{\partial x} = \rho I_P\frac{\partial^2\vartheta}{\partial t^2} \;\Rightarrow\; G I_T\frac{\partial^2\vartheta}{\partial x^2} = \rho I_P\frac{\partial^2\vartheta}{\partial t^2}, \qquad c = \sqrt{\frac{G I_T}{\rho I_P}}
```

For polar symmetry (I\_T = I\_P): **c = √(G/ρ)**, material only. Since G < E, torsional waves are slower than axial ones (factor √(1/(2(1+ν))) ≈ 0.62 for steel).

### 3. Solutions

Identical to L06: ϑ = f₁(x − ct) + f₂(x + ct), or stationary ϑ = \[A cos(ωx/c) + B sin(ωx/c)\] cos(ωt + φ).

| Boundary | Condition |
| --- | --- |
| Fixed end | ϑ = 0 (geometric) |
| Free end | M\_t = 0 → ∂ϑ/∂x = 0 (natural) |
| End with a disc of inertia J | G I\_P ∂ϑ/∂x = ∓J ∂²ϑ/∂t² (moment balance of the disc) |

Fixed–fixed: ω\_k = kπc/L. Fixed–free: ω\_k = (2k−1)πc/(2L).

### On your blackboard (L08)

- [ ] Displacement field v = −zϑ, w = yϑ and the resulting shear strains
- [ ] Sketch of circumferential shear stress growing with r
- [ ] M\_t = G I\_P ϑ' and I\_P for solid and hollow sections
- [ ] Element balance and the wave equation with c = √(G/ρ)
- [ ] The parallel with axial vibration (one table: u ↔ ϑ, EA ↔ GI\_P, m ↔ ρI\_P)

### Likely oral questions (L08)

1. **Derive the equation of torsional vibration.** Kinematics, stress, M\_t, element balance.
2. **Why is torsion decoupled from bending and axial?** No normal stress, so no N or M. Shear forces vanish by antisymmetry.
3. **What changes for a non-circular section?** Warping, I\_T ≠ I\_P, c depends on geometry.
4. **Compare torsional and axial vibration.** Same equation and solutions, c = √(G/ρ) vs √(E/ρ).

### Traps and follow-ups (L08)

- "A shaft with a heavy disc at the end: how do you find its frequencies?" → the disc inertia enters a boundary condition (natural, with an inertia term), giving a transcendental frequency equation. If the shaft inertia is small compared to the disc, you recover the 1-dof result ω = √(GI\_P/(LJ)).
- This is the continuous version of the torsional lumped models used for drivelines.

## L09 — Mode superposition for distributed-parameter systems

**Big idea:** expand the continuous displacement as a sum of mode shapes times modal coordinates, w(x,t) = Σ φ\_k(x) q\_k(t). Truncate to n modes and the beam becomes an n-dof system (a **discretisation**). Lagrange gives diagonal modal mass and stiffness, so you get n decoupled 1-dof equations, exactly like L03.

### 1. Modal expansion and truncation

```latex
w(x,t) = \sum_{k=1}^{\infty}\varphi_k(x)\,q_k(t) \;\approx\; \sum_{k=1}^{n}\varphi_k(x)\,q_k(t) = \underline{\Phi}^T(x)\,\underline{q}(t)
```

For the pinned–pinned beam φ\_k = sin(kπx/L): the expansion is a Fourier sine series, so it is mathematically justified. For other cases an **expansion theorem** guarantees it (Meirovitch).

**How many modes?** Choose n so that ω\_{n+1} ≫ Ω\_max (the highest forcing frequency). The neglected modes contribute little because:

1. their modal stiffness is very large (for bending it grows with k⁴), so their quasi-static displacement is small;
2. they are excited in their quasi-static range, so there is no dynamic amplification (factor ≈ 1).

### 2. Equations of motion with Lagrange

**Kinetic energy.** T = ½∫ m (∂w/∂t)² dx. Substitute ∂w/∂t = Φᵀq̇:

```latex
T = \tfrac{1}{2}\dot{\underline q}^T[\bar m]\dot{\underline q}, \qquad [\bar m] = \int_0^L \underline\Phi(x)\,m\,\underline\Phi^T(x)\,dx
```

Pinned–pinned: m̄\_ij = m∫sin(iπx/L)sin(jπx/L)dx = mL/2 if i = j, 0 otherwise. **Diagonal** (orthogonality of sines; in general an orthogonality theorem holds).

**Potential energy.** Gravity cancels with the static elastic preload if you measure w from static equilibrium (same argument as L01). Clapeyron's theorem: dV = ½ M dϑ, with dϑ = w'' dx and M = EI w'' (shear deformation neglected):

```latex
V = \tfrac{1}{2}\int_0^L EI\left(\frac{\partial^2 w}{\partial x^2}\right)^2 dx = \tfrac{1}{2}\underline q^T[\bar k]\underline q, \qquad [\bar k] = \int_0^L \underline\Phi''(x)\,EI\,\underline\Phi''^T(x)\,dx
```

Pinned–pinned: k̄\_ii = EI (iπ/L)⁴ L/2, off-diagonal 0. Check: ω\_i = √(k̄\_ii/m̄\_ii) = (iπ/L)²√(EI/m), the exact L07 result. **The modal approach preserves the first n natural frequencies.**

**Damping.** Real dissipation (material hysteresis, air) is too complex to model. Use an equivalent diagonal viscous damping matched to measured damping ratios (L04):

```latex
\bar c_{ii} = h_i\,c_{cr,i} = 2h_i\,\bar m_{ii}\,\omega_i = 2h_i\sqrt{\bar k_{ii}\,\bar m_{ii}}
```

**Forces.**

| Load | Virtual work | Modal force |
| --- | --- | --- |
| Concentrated F(t) at x̃ | δw(x̃)F = δqᵀΦ(x̃)F | f̄(t) = Φ(x̃) F(t): mode shape at the load point |
| Distributed p₀(x)e^{iΩt} | ∫δw p dx | f̄ = ∫Φ(x)p₀(x)dx · e^{iΩt} |

Consequences: a force at a **node** of mode i does not excite mode i. On a symmetric system, a **symmetric load** excites only the symmetric modes (k = 1, 3, 5…) and an antisymmetric load only the antisymmetric ones (k = 2, 4…).

Final result: \[m̄\]q̈ + \[c̄\]q̇ + \[k̄\]q = f̄(t), all diagonal, so n independent 1-dof equations m̄\_ii q̈\_i + c̄\_ii q̇\_i + k̄\_ii q\_i = f̄\_i.

### On your blackboard (L09)

- [ ] Expansion w = Φᵀ(x) q(t) and the truncation criterion ω\_{n+1} ≫ Ω\_max, with the two reasons
- [ ] T and \[m̄\] = ∫Φ m Φᵀ dx; pinned–pinned m̄ = mL/2
- [ ] V from Clapeyron, \[k̄\] = ∫Φ'' EI Φ''ᵀ dx; k̄\_ii ∝ i⁴
- [ ] Check that ω\_i is recovered exactly
- [ ] Modal damping c̄\_ii = 2h\_i m̄\_ii ω\_i
- [ ] Modal force for a point load and a distributed load; symmetric/antisymmetric argument

### Likely oral questions (L09)

1. **How do you apply the modal approach to a beam?** Expansion, truncation, Lagrange, diagonal matrices.
2. **How many modes do you keep and why are the others negligible?** The two reasons (stiffness, quasi-static range).
3. **Compute the modal mass and stiffness of a pinned–pinned beam.** Integrals of sin² and orthogonality.
4. **How do you model damping in a continuous system?** Equivalent modal viscous damping from measured h\_i.
5. **Which modes are excited by a load at mid-span? By a uniform load?** Mid-span is a node of even modes, so only odd modes. Uniform load is symmetric, so only odd modes.
6. **Why is this called discretisation? How does it relate to FEM?** Both reduce infinite dofs to n. Here the shape functions are the exact global modes; in FEM they are local polynomials (L10).

### Traps and follow-ups (L09)

- "Why does gravity disappear from V?" → heights depend linearly on w and coordinates are measured from static equilibrium. Same as the linear system result in L01.
- "Why is the stiffness written with w'' and not w'?" → the strain energy of bending depends on curvature, M dϑ/2 with dϑ = w''dx.
- Moving loads (bridges, rails) are mentioned in the notes as a third case: the load position x̃(t) = vt changes in time, so f̄\_i = φ\_i(vt)F, which gives excitation at frequency kπv/L.

## L10 — The Finite Element Method for beam systems

**Big idea:** analytical solutions (L06–L08) only work for simple cases and need a new treatment for every geometry. FEM divides the structure into elements, describes the motion inside each element with **shape functions** of the nodal displacements, and builds \[m\], \[k\] with Lagrange. The result is an n-dof system (\[m\]ẍ + \[c\]ẋ + \[k\]x = f) that any computer can solve. The course covers planar frames with axial + bending.

### The 10 steps (learn the list in order: it is the skeleton of any FEM answer)

1. Meshing
2. Global and local references
3. Remove constraints, replace them with unknown reactions
4. Shape functions
5. Element energies in the local reference → \[m\_k^L\], \[k\_k^L\], forces
6. Local → global transformation \[Λ\_k\]
7. Numbering and assembly
8. Structural damping (Rayleigh)
9. Reintroduce constraints, partition the matrices
10. Solve: modes, FRF, response to constraint motion

### Step 1: meshing

Put a node at every **discontinuity**: change of section, junction of beams with different directions, lumped mass, spring or damper. Then limit the element length. FEM is **exact for static nodal loads**, and in dynamics each element must work in its **quasi-static** range, well below its own first frequency:

```latex
\Omega_{max} < \omega_{1,k} = \left(\frac{\pi}{L_k}\right)^2\sqrt{\frac{EJ}{m}} \quad\Rightarrow\quad L_k < \sqrt{\frac{\pi^2}{\Omega_{max}}\sqrt{\frac{EJ}{m}}}
```

In practice use a safety factor (e.g. ω₁,k ≥ 1.5–2 × Ω\_max). Element ω uses the pinned–pinned formula from L07.

### Steps 2–3: references and constraints

Global axes (x\_G, y\_G) for the whole frame. Each element has a local x\_L along its axis and y\_L rotated +90°. Constraints are replaced by their reactions (H, V, M) so every node starts with 3 free dofs (u, v, ϑ). They come back in step 9.

### Step 4: shape functions

Element dofs in local axes: x\_k^L = {u\_i, v\_i, ϑ\_i, u\_j, v\_j, ϑ\_j}.

**Axial:** linear, u(ξ) = a + bξ. Imposing u(0) = u\_i and u(L) = u\_j:

```latex
u(\xi,t) = \left(1 - \frac{\xi}{L}\right)u_i + \frac{\xi}{L}\,u_j
```

**Bending:** cubic, v(ξ) = a + bξ + cξ² + dξ³. Four conditions: v and ∂v/∂ξ at both nodes. This gives the Hermite cubics:

```latex
f_{v1} = 1 - 3\frac{\xi^2}{L^2} + 2\frac{\xi^3}{L^3}, \quad f_{v2} = \xi - 2\frac{\xi^2}{L} + \frac{\xi^3}{L^2}, \quad f_{v3} = 3\frac{\xi^2}{L^2} - 2\frac{\xi^3}{L^3}, \quad f_{v4} = -\frac{\xi^2}{L} + \frac{\xi^3}{L^2}
```

Why linear and cubic? They are the exact static solutions of a beam loaded only at its ends (u'' = 0 and v'''' = 0). That is why FEM is exact for static nodal loads.

In matrix form: u = f\_uᵀ x\_k^L and v = f\_vᵀ x\_k^L.

### Step 5: element matrices

```latex
T_k = \tfrac{1}{2}\int_0^{L}m\left(\dot u^2 + \dot v^2\right)d\xi \Rightarrow [m_k^L] = \int_0^L m\,\underline f_u\underline f_u^T d\xi + \int_0^L m\,\underline f_v\underline f_v^T d\xi
```

```latex
V_k = \tfrac{1}{2}\int_0^L EA\,(u')^2 d\xi + \tfrac{1}{2}\int_0^L EJ\,(v'')^2 d\xi \Rightarrow [k_k^L] = \int_0^L EA\,\underline f_u'\underline f_u'^T d\xi + \int_0^L EJ\,\underline f_v''\underline f_v''^T d\xi
```

Results to recognise (bending part, dofs v\_i, ϑ\_i, v\_j, ϑ\_j):

```latex
[k^{bend}] = \frac{EJ}{L^3}\begin{bmatrix} 12 & 6L & -12 & 6L \\ 6L & 4L^2 & -6L & 2L^2 \\ -12 & -6L & 12 & -6L \\ 6L & 2L^2 & -6L & 4L^2 \end{bmatrix}, \qquad [k^{ax}] = \frac{EA}{L}\begin{bmatrix}1 & -1\\-1 & 1\end{bmatrix}
```

Consistent mass: axial mL\[1/3 1/6; 1/6 1/3\]; bending mL × \[13/35, 11L/210, 9/70, −13L/420; …; 1/105 L² and −1/140 L² on the rotation terms\]. You don't need every entry: know how it is obtained and its structure (symmetric, couples neighbouring dofs, "consistent" because it uses the same shape functions as the stiffness). Signs in your notes depend on the rotation convention.

**Forces.** Concentrated force inside the element: F\_k^L = f\_u(ξ̃)f\_x + f\_v(ξ̃)f\_y. Distributed load: F\_k^L = ∫(f\_u p\_x + f\_v p\_y)dξ (equivalent nodal loads). A force on a node is applied directly to the global nodal dof. Reactions: δL\_R = δx\_cᵀR.

### Step 6: local → global

For an element at angle α to x\_G, at each node:

```latex
\begin{Bmatrix}u_L\\v_L\\\vartheta_L\end{Bmatrix} = \begin{bmatrix}\cos\alpha & \sin\alpha & 0\\ -\sin\alpha & \cos\alpha & 0\\ 0 & 0 & 1\end{bmatrix}\begin{Bmatrix}u_G\\v_G\\\vartheta_G\end{Bmatrix}
```

&#91;Λ\_k\] = diag(λ, λ) is constant for small displacements. Then \[m\_k^G\] = \[Λ\_k\]ᵀ\[m\_k^L\]\[Λ\_k\], \[k\_k^G\] likewise, F\_k^G = \[Λ\_k\]ᵀF\_k^L. Rotations don't change (planar case).

### Step 7: assembly

Order all nodal dofs in x = {x\_f; x\_c} (free first, constrained last). The **extraction matrix** \[E\_k\] picks out the element's dofs: x\_k^G = \[E\_k\]x. Then

```latex
[m] = \sum_k [E_k]^T[m_k^G][E_k], \qquad [k] = \sum_k [E_k]^T[k_k^G][E_k], \qquad \underline f = \sum_k [E_k]^T\underline F_k^G + \ldots
```

In practice: each element's 6×6 block is added into the rows and columns of its nodes. Where two elements share a node, their blocks overlap and are summed.

### Step 8: structural damping

&#91;c\] = α\[m\] + β\[k\] (Rayleigh). In modal coordinates h\_i = α/(2ω\_i) + βω\_i/2. Given measured h\_i for n modes, write n equations in 2 unknowns and solve by least squares: \[A\]ᵀ\[A\]{α, β} = \[A\]ᵀb. Graph: the α term falls as 1/ω, the β term rises linearly, their sum is a U-shaped curve through the measured points.

### Step 9: partition

```latex
\begin{bmatrix}[m_{ff}] & [m_{fc}]\\ [m_{cf}] & [m_{cc}]\end{bmatrix}\begin{Bmatrix}\ddot{\underline x}_f\\ \ddot{\underline x}_c\end{Bmatrix} + \ldots = \begin{Bmatrix}\underline f_f\\ \underline f_c + \underline R\end{Bmatrix}
```

First row: x\_c is known (often zero), so solve \[m\_ff\]ẍ\_f + \[c\_ff\]ẋ\_f + \[k\_ff\]x\_f = f\_f − (\[m\_fc\]ẍ\_c + \[c\_fc\]ẋ\_c + \[k\_fc\]x\_c). Second row: once x\_f is known, it gives the reactions R.

### Step 10: solutions

- **Modes:** eigenvalues and eigenvectors of \[m\_ff\]⁻¹\[k\_ff\].
- **Forced response:** X₀ = \[G(iΩ)\]F₀ with \[G\] = (−Ω²\[m\_ff\] + iΩ\[c\_ff\] + \[k\_ff\])⁻¹.
- **Imposed motion of constraints** (e.g. ground or support motion):

```latex
\underline X_0 = -\left(-\Omega^2[m_{ff}] + i\Omega[c_{ff}] + [k_{ff}]\right)^{-1}\left(-\Omega^2[m_{fc}] + i\Omega[c_{fc}] + [k_{fc}]\right)\underline X_{c0} = [G_c(i\Omega)]\,\underline X_{c0}
```

### On your blackboard (L10)

- [ ] The 10 steps, in order
- [ ] Meshing rules + element length criterion and why (quasi-static elements)
- [ ] Axial (linear) and bending (Hermite cubic) shape functions, with the conditions used to find them
- [ ] Element T and V → \[m\_k\] and \[k\_k\] integrals
- [ ] The 4×4 bending stiffness matrix and 2×2 axial one
- [ ] Rotation matrix λ and \[m^G\] = Λᵀ m^L Λ
- [ ] Assembly with \[E\_k\], sketch of overlapping blocks
- [ ] Rayleigh damping fit (U-shaped curve)
- [ ] Partition ff/fc/cf/cc and the two uses (motion, reactions)
- [ ] &#91;G\_c\] for constraint motion

### Likely oral questions (L10)

1. **Why FEM? Advantages over analytical solutions?** General, automatable, libraries exist, CAD integration. Analytical methods need new \[H(γ)\] for every system.
2. **How do you choose the mesh?** Nodes at discontinuities, element length from the quasi-static criterion.
3. **Derive the shape functions of a beam element.** Linear axial, cubic bending, nodal conditions. Why these are exact statically.
4. **How are the element mass and stiffness matrices obtained?** Substitute shape functions in T and V, integrate. Consistent mass.
5. **Explain assembly.** Local → global, extraction matrix, summing blocks at shared nodes.
6. **How do you handle constraints and compute reactions?** Remove, partition, solve the ff block, then the cf block gives R.
7. **How do you model damping in an FE model?** Rayleigh, least squares on measured h\_i.
8. **How do you compute the response to a support motion?** \[G\_c\].

### Traps and follow-ups (L10)

- "Is FEM exact?" → exact for static nodal loads; in dynamics only an approximation, good if elements are short enough. The highest FE modes are inaccurate.
- "Why does the FE frequency overestimate the exact one?" → the assumed shape constrains the motion (a stiffer model). It converges from above as the mesh is refined (with consistent mass).
- "Why remove the constraints at the beginning?" → to build matrices in a general way and recover the reactions at the end.
- "Why must a node go where two beams meet at an angle?" → axial and bending of the two beams couple there; the transformation to global handles it.

## L11 — Solid finite elements

**Big idea:** when no dimension prevails, you can't reduce to beams or plates. Solid (3D) elements use only nodal **displacements** (no rotations). The recipe is the same as L10: shape functions → T and V → element matrices → assembly. The new ingredients are the full 3D stress–strain law and the **isoparametric mapping** for elements of arbitrary shape.

### 1. Element families

| Type | Examples | Nodal dofs |
| --- | --- | --- |
| 1D | Beam, truss | Displacements + rotations |
| 2D | Plates, shells | Displacements + rotations |
| 3D (solid) | Tetrahedra, hexahedra | Displacements only (u, v, w) |

### 2. The 8-node hexahedron

Master element: a cube in natural coordinates (ξ, η, ζ) ∈ \[−1, 1\]³, nodes at the corners. 8 nodes × 3 dofs = **24 dofs**: x\_k = {u₁, v₁, w₁, …, u₈, v₈, w₈}.

Trilinear shape functions, f\_i = 1 at node i and 0 at the others (f\_i(ξ\_j, η\_j, ζ\_j) = δ\_ij):

```latex
f_i(\xi,\eta,\zeta) = \tfrac{1}{8}(1 + \xi\xi_i)(1 + \eta\eta_i)(1 + \zeta\zeta_i), \qquad \underline u = \{u, v, w\}^T = [f]\,\underline x_k
```

### 3. Mass matrix

```latex
T_k = \tfrac{1}{2}\int_{Vol}\dot{\underline u}^T\rho\,\dot{\underline u}\,dVol \;\Rightarrow\; [M_k] = \int_{Vol}[f]^T\rho\,[f]\,dVol \quad (24\times24,\ \text{symmetric, constant})
```

### 4. Stiffness matrix

**Clapeyron:** V\_k = ½∫ εᵀσ dVol, with ε and σ the 6-component vectors {ε\_x, ε\_y, ε\_z, γ\_xy, γ\_yz, γ\_zx} and {σ\_x, …, τ\_zx}.

**Constitutive law:** σ = \[E\]ε. \[E\] is block-diagonal: the normal block

```latex
[E_1] = \frac{E}{(1+\nu)(1-2\nu)}\begin{bmatrix}1-\nu & \nu & \nu\\ \nu & 1-\nu & \nu\\ \nu & \nu & 1-\nu\end{bmatrix}
```

and G on the diagonal of the shear block. It is the inverse of the generalised Hooke's law of L05.

**Strain–displacement:** ε = \[D\]u, where \[D\] is the differential operator (∂/∂x on u, ∂/∂y on v, ∂/∂z on w, and the pairs for the shears). Then ε = \[D\]\[f\]x\_k = \[B\]x\_k:

```latex
V_k = \tfrac{1}{2}\underline x_k^T\left(\int_{Vol}[B]^T[E][B]\,dVol\right)\underline x_k, \qquad [K_k] = \int_{Vol}[B]^T[E][B]\,dVol
```

Assembly follows the same rules as beam elements (no local/global rotation needed: dofs are already displacements in global axes).

### 5. Real (distorted) geometry: isoparametric mapping

A real element is a distorted hexahedron. Map the master cube onto it using the node coordinates:

```latex
x(\xi,\eta,\zeta) = \sum_{i=1}^{8}N_i\,x_i, \quad y = \sum N_i\,y_i, \quad z = \sum N_i\,z_i
```

**Isoparametric** = the same functions for geometry and displacement (N\_i = f\_i).

Two issues:

1. &#91;B\] needs derivatives with respect to x, y, z, but f\_i are functions of ξ, η, ζ. Chain rule:

```latex
\begin{Bmatrix}\partial f_i/\partial\xi\\ \partial f_i/\partial\eta\\ \partial f_i/\partial\zeta\end{Bmatrix} = [J]\begin{Bmatrix}\partial f_i/\partial x\\ \partial f_i/\partial y\\ \partial f_i/\partial z\end{Bmatrix} \;\Rightarrow\; \begin{Bmatrix}\partial f_i/\partial x\\ \vdots\end{Bmatrix} = [J]^{-1}\begin{Bmatrix}\partial f_i/\partial\xi\\ \vdots\end{Bmatrix}
```

&#91;J\] is the Jacobian of the mapping (rows: derivatives of x, y, z with respect to ξ, η, ζ).

2. The volume element: dVol = det\[J\] dξ dη dζ. Integrals are then done on the master cube (numerically, Gauss quadrature).

**Excessive distortion.** If two nodes coincide (e.g. 7 and 8) the mapping is not one-to-one and \[J\] is singular. Even before that, a badly distorted element makes \[J\]⁻¹ ill-conditioned and gives large numerical errors. That is why meshers check element quality.

### On your blackboard (L11)

- [ ] Master hexahedron with 8 nodes and 24 dofs
- [ ] f\_i = ⅛(1 + ξξ\_i)(1 + ηη\_i)(1 + ζζ\_i) and the δ\_ij property
- [ ] &#91;M\_k\] = ∫\[f\]ᵀρ\[f\]dVol
- [ ] σ = \[E\]ε, ε = \[D\]u = \[B\]x\_k, \[K\_k\] = ∫\[B\]ᵀ\[E\]\[B\]dVol
- [ ] Isoparametric mapping, \[J\], dVol = det\[J\] dξ dη dζ
- [ ] Why distortion is bad

### Likely oral questions (L11)

1. **When do you need solid elements? What changes compared to beams?** No prevailing dimension; only displacements, no rotations.
2. **Write the shape functions of the 8-node hexahedron and their property.** f\_i(node j) = δ\_ij.
3. **Derive the element stiffness matrix of a solid element.** Clapeyron, \[E\], \[D\], \[B\].
4. **What is an isoparametric element? What is the Jacobian used for?** Same functions for geometry and displacements; derivatives and volume transformation.
5. **What happens with a badly distorted element?** \[J\] singular or ill-conditioned.

### Traps and follow-ups (L11)

- "How is the beam element a special case of the same procedure?" → same steps, but in 1D the kinematics of the section (rigid) reduce ε and σ to EA u' and EJ v''.
- "Why are solid elements expensive?" → 3 dofs per node and many nodes through the thickness, so huge matrices for slender parts. Use beams and shells where possible.

## L12 — Dynamics of a rigid body in space

**Big idea:** in 3D the moment of inertia becomes a 3×3 **inertia tensor**, and rotations no longer commute, so orientation needs a defined sequence of angles (Cardan). Kinetic energy is still ½mv\_G² + ½ωᵀ\[J\_G\]ω (König). The worked example, a rotor on a fixed axis, gives the two **balancing conditions**: c.o.m. on the axis, and the axis a principal axis of inertia.

### 1. Velocity of a point (Rivals' theorem in matrix form)

v\_P = v\_G + ω ∧ (P − G) holds in 3D too. In components, the cross product becomes a skew-symmetric matrix:

```latex
\underline v_P = \underline v_G + [\tilde x_{PG}]\,\underline\omega, \qquad [\tilde x_{PG}] = \begin{bmatrix}0 & z & -y\\ -z & 0 & x\\ y & -x & 0\end{bmatrix}
```

(x, y, z are the coordinates of P relative to G; check the sign arrangement against your notes, it is −(P−G)∧ written as a matrix acting on ω.)

### 2. Kinetic energy and the inertia tensor

T = ½∫ρ v\_Pᵀv\_P dVol. Substitute v\_P and expand into four terms:

1. ½v\_Gᵀ(∫ρ dVol)v\_G = ½m v\_Gᵀv\_G
2. and 3. cross terms with ∫ρ\[x̃\_PG\]dVol = first moments about G = **0** (G is the centre of mass)
3. ½ωᵀ(∫ρ\[x̃\]ᵀ\[x̃\]dVol)ω = ½ωᵀ\[J\_G\]ω

```latex
T = \tfrac{1}{2}m\,\underline v_G^T\underline v_G + \tfrac{1}{2}\underline\omega^T[J_G]\underline\omega \quad\text{(König)}, \qquad [J_G] = \begin{bmatrix}J_{xx} & J_{xy} & J_{xz}\\ J_{yx} & J_{yy} & J_{yz}\\ J_{zx} & J_{zy} & J_{zz}\end{bmatrix}
```

- Moments of inertia: J\_xx = ∫ρ(y² + z²)dVol, and similarly for yy, zz.
- Products of inertia: J\_xy = J\_yx = −∫ρ xy dVol, and similarly.
- &#91;J\_G\] is **symmetric**. Its values depend on the axes. There is always a set of **principal axes of inertia** where it is diagonal (eigenvectors of \[J\_G\]). With three orthogonal symmetry planes, the principal axes are their intersections.
- Compute \[J\_G\] in the **local** (body-fixed) frame: there it is constant in time.

### 3. Orientation: Cardan angles

Three successive rotations, in this order:

1. σ about x\_G → frame I
2. β about y\_I → frame II
3. ρ about z\_II → local frame L

The order matters because finite rotations are **not commutative**. Each step is a planar rotation matrix, so:

```latex
\underline a^L = [\Lambda_{LG}]\,\underline a^G, \qquad [\Lambda_{LG}] = [\Lambda_{II\text{-}L}][\Lambda_{I\text{-}II}][\Lambda_{G\text{-}I}], \qquad [\Lambda_{GL}] = [\Lambda_{LG}]^{-1} = [\Lambda_{LG}]^T
```

The product of orthogonal matrices is orthogonal, so the inverse is the transpose.

**Angular velocity.** ω is the sum of σ̇ along x\_G, β̇ along y\_I and ρ̇ along z\_II = z\_L. Projecting each on the global or local axes:

```latex
\underline\omega^G = [A_G]\,\dot{\underline\theta}, \qquad \underline\omega^L = [A_L]\,\dot{\underline\theta}, \qquad \underline\theta = \{\sigma, \beta, \rho\}^T
```

The derivatives of the Cardan angles are **not** the components of ω: you need \[A\]. For σ = β = 0, \[A\_G\] = \[I\].

### 4. Free rigid body: 6 coordinates and the 6×6 mass matrix

x = {x\_O^G; θ}: 3 translations of a point O + 3 Cardan angles. Write T in the most convenient frames (translation in global, rotation in local, where \[J\_G^L\] is constant):

```latex
T = \tfrac{1}{2}\underline v_G^{G\,T}[m]\underline v_G^G + \tfrac{1}{2}\underline\omega^{L\,T}[J_G^L]\underline\omega^L = \tfrac{1}{2}\dot{\underline x}^T[M(\underline x)]\dot{\underline x}
```

If O ≠ G, v\_G = ẋ\_O + \[Λ\_GL\]\[x̃\_G^L\]\[A\_L\]θ̇, which couples translations and rotations in \[M\]. The rotational block contains the **inertia tensor about O** (3D parallel-axis theorem):

```latex
[J_O^L] = [\tilde x_G^L]^T[m][\tilde x_G^L] + [J_G^L]
```

If O = G, \[M\] is block-diagonal: \[m\] and \[A\_L\]ᵀ\[J\_G^L\]\[A\_L\].

### 5. Worked example: rotor on a fixed axis (balancing)

Body with generic mass distribution, spherical hinge at A, double cart at B (blocks 2 of 3 displacements). Axis AB = z\_G = z\_L. c.o.m. G at distance e from the axis (on x\_L). 1 dof: ρ.

Trick: keep all 6 coordinates, x = {x\_c; x\_f} with x\_c = 0 (5 constrained) and x\_f = ρ. Lagrange on all 6 gives the equation of motion **and** 5 equations for the reactions. Q\_c = Lagrangian components of the reactions: the resultant force (3 components) and moments about x\_G, y\_G (the moment about z\_G is zero because the reactions cross the axis).

**Results and their physical meaning:**

- **Force equations (x, y):** m e (ρ̈ sinρ + ρ̇² cosρ) and the companion term = reactions. These are the tangential (∝ ρ̈) and centrifugal (∝ ρ̇²) inertia forces of the c.o.m. They vanish if e = 0. **Static unbalance.**
- **Moment equations (x, y):** terms like J\_Oxz(ρ̈ sinρ + ρ̇² cosρ) and J\_Oyz(…) = moments of the reactions. They exist even if e = 0, unless J\_Oxz = J\_Oyz = 0. **Dynamic (couple) unbalance.**
- **Moment about z:** J\_Ozz ρ̈ = 0 → constant speed (no external torque).

**A rotor is balanced (zero rotating reactions) if and only if:**

1. its centre of mass lies on the axis of rotation (e = 0), and
2. the axis of rotation is a principal axis of inertia (J\_xz = J\_yz = 0).

### On your blackboard (L12)

- [ ] v\_P = v\_G + \[x̃\]ω and the skew matrix
- [ ] Derivation of T in four terms, why the cross terms vanish, König's theorem
- [ ] Inertia tensor: definitions of moments and products, symmetry, principal axes
- [ ] Cardan sequence (σ, β, ρ), product of rotation matrices, orthogonality
- [ ] ω = \[A\]θ̇ and why θ̇ ≠ ω
- [ ] &#91;J\_O\] = \[x̃\]ᵀm\[x̃\] + \[J\_G\]
- [ ] Rotor sketch with A, B, e, and the two balancing conditions with the static/dynamic unbalance terms

### Likely oral questions (L12)

1. **Derive the kinetic energy of a rigid body in space.** Rivals, four terms, König.
2. **What is the inertia tensor? What are principal axes?** Definitions, symmetric, diagonal in principal axes, symmetry planes.
3. **Why can't you describe 3D orientation with three independent rotations like a vector?** Non-commutativity, Cardan sequence.
4. **How do you get the angular velocity from the Cardan angles?** Sum of three vectors along different axes, \[A\_G\], \[A\_L\].
5. **Write the mass matrix of a free rigid body. When is it block-diagonal?** O = G.
6. **When is a rotor balanced? Static vs dynamic unbalance.** The two conditions, with the inertia terms they cancel.

### Traps and follow-ups (L12)

- "A rotor with the c.o.m. on the axis: are the bearing reactions zero?" → not necessarily. If the axis is not principal, the products of inertia create a rotating couple (dynamic unbalance). It needs correction in two planes.
- "Why compute \[J\] in the body frame?" → in the global frame it changes with orientation.
- "What singularity do Cardan angles have?" → at β = ±90°, \[A\] becomes singular (gimbal lock): σ and ρ rotate about the same axis.

## L13 — Stability of mechanical systems subjected to force fields

**Big idea:** a force field is a force that depends on the system's own state (position, velocity), like friction, aerodynamic or contact forces. Linearised around equilibrium, it adds a field stiffness k\_f and a field damping c\_f, which can be **negative**. Stability is read from the eigenvalues of the linearised system and transferred to the nonlinear system with Lyapunov's theorem. You get three types of instability: **divergence** (negative stiffness), **dynamic instability** (negative damping) and **flutter** (non-conservative, non-symmetric stiffness).

### 1. Setting

```latex
m_s\ddot x + c_s\dot x + k_s x = F(x, \dot x) \qquad [m_s]\ddot{\underline x} + [c_s]\dot{\underline x} + [k_s]\underline x = \underline F(\underline x, \dot{\underline x})
```

"s" means structural (always positive). F not explicitly time-dependent = **autonomous** field (the only case in the course).

### 2. Stability definitions (Lyapunov)

With equilibrium at z = 0 (z = state vector):

- **Stable:** for every ε > 0 there is δ > 0 such that if the initial state is within δ, the motion stays within ε for all t.
- **Asymptotically stable:** stable and z(t) → 0.
- **Unstable:** not stable.

A linear system has one equilibrium and stability independent of the perturbation size. A nonlinear system can have many equilibria, and stability may depend on the perturbation size. You can't test infinitely many perturbations numerically, so you use:

**Lyapunov's theorem (linearisation method):**

| Linearised system | Nonlinear system |
| --- | --- |
| Asymptotically stable (all Re λ < 0) | Asymptotically stable |
| Unstable (some Re λ > 0) | Unstable |
| Stable, not asymptotically (Re λ = 0) | **No conclusion**: use another method |

### 3. One dof

Equilibria: k\_s x\_e = F(x\_e, 0) (nonlinear, possibly several solutions). Linearise around each:

```latex
k_f = -\left.\frac{\partial F}{\partial x}\right|_e, \quad c_f = -\left.\frac{\partial F}{\partial \dot x}\right|_e \;\Rightarrow\; m_s\ddot x + (c_s + c_f)\dot x + (k_s + k_f)x = 0
```

With c\_T = c\_s + c\_f and k\_T = k\_s + k\_f: λ = −c\_T/(2m\_s) ± √((c\_T/2m\_s)² − k\_T/m\_s).

| Case | Roots | Behaviour |
| --- | --- | --- |
| k\_T > 0, c\_T > 0 | Re λ < 0 | Asymptotically stable |
| k\_T < 0 (any c\_T) | One real positive root | **Divergence**: moves away without oscillating (e.g. inverted pendulum) |
| k\_T > 0, c\_T < 0 | Complex, Re λ > 0 | **Dynamic instability**: oscillation growing as e^{αt} |

Sketch both time histories: monotonic growth for divergence, growing oscillation for dynamic instability.

**Worked example: friction-induced self-excited vibration.** Slider (m, c, k) on a belt moving at V, pressed by load P. Dry friction T = f\_d(V\_s)N with N = P and sliding speed V\_s = V − ẋ. At low speed the friction coefficient decreases with speed: f\_d = f\_d0 − αV\_s. Then:

```latex
m\ddot x + (c - \alpha P)\dot x + kx = (f_{d0} - \alpha V)P
```

The right side is constant (it only shifts the equilibrium). The falling friction characteristic gives a **negative damping** −αP. If c < αP, the total damping is negative: dynamic instability. Examples: violin bow on a string, brake squeal.

### 4. n dof

Equilibria from \[k\_s\]x\_e = F(x\_e, 0). Linearise:

```latex
[K_F] = -\left.\frac{\partial\underline F}{\partial\underline x}\right|_e, \quad [C_F] = -\left.\frac{\partial\underline F}{\partial\dot{\underline x}}\right|_e \;\Rightarrow\; [M_s]\ddot{\underline x} + [C_T]\dot{\underline x} + [K_T]\underline x = 0
```

Stability: det(λ²\[M\_s\] + λ\[C\_T\] + \[K\_T\]) = 0, a polynomial of degree 2n. In practice, eigenvalues of the 2n×2n state matrix. Note: \[K\_F\] and \[C\_F\] are in general **not symmetric**.

### 5. Two dof with a positional field (no damping)

Point mass in the plane, F = F(x) only, \[C\_s\] = 0, so \[C\_F\] = 0. With K̃ = K\_T/m\_s:

```latex
\lambda^4 + \lambda^2(\tilde K_{xx} + \tilde K_{yy}) + (\tilde K_{xx}\tilde K_{yy} - \tilde K_{xy}\tilde K_{yx}) = 0 \;\Rightarrow\; \lambda^2 = -\frac{\tilde K_{xx} + \tilde K_{yy}}{2} \pm \sqrt{\left(\frac{\tilde K_{xx} - \tilde K_{yy}}{2}\right)^2 + \tilde K_{xy}\tilde K_{yx}}
```

**Conservative field:** the work depends only on the end points, so a potential V exists with F = −grad V. By Schwarz's theorem the test is ∂F\_x/∂y = ∂F\_y/∂x, so **\[K\_F\] is symmetric**.

| Case | λ | Conclusion |
| --- | --- | --- |
| 1a. Conservative, \[K\_T\] positive definite | Purely imaginary pairs ±iω | Linearised: stable but not asymptotically, so Lyapunov is inconclusive. Use **Dirichlet's theorem**: conservative system, V has a minimum (V = ½xᵀ\[K\_T\]x > 0), so **stable** |
| 1b. Conservative, \[K\_T\] not positive definite | At least one real positive λ | **Divergence** |
| 2. Non-conservative, K\_xy·K\_yx < 0 and K\_xy·K\_yx < −((K\_xx − K\_yy)/2)² | λ² complex, so two complex pairs, one with Re > 0 | **Flutter** |

In words, the flutter conditions (4.24) are: the cross-coupling terms have opposite signs, and their product is larger in magnitude than the square of half the difference of the diagonal terms. Then the square root is imaginary and λ² is complex.

**Physics of flutter.** It is not negative damping. The two complex modes describe the same elliptical orbit of the mass, run clockwise and counter-clockwise. A non-conservative field does non-zero work on a closed path, with a sign that depends on the direction. In one direction the field removes energy (decaying mode), in the other it injects energy (growing mode). Name from aircraft wings.

### On your blackboard (L13)

- [ ] Lyapunov definitions (stable, asymptotically stable, unstable)
- [ ] Lyapunov's linearisation theorem table, especially the inconclusive case
- [ ] k\_f, c\_f as negative gradients; the three 1-dof cases with time histories
- [ ] Friction example: f\_d = f\_d0 − αV\_s and the resulting c − αP
- [ ] Conservative field: F = −grad V, Schwarz test, symmetric \[K\_F\]
- [ ] Biquadratic λ equation and the three 2-dof cases
- [ ] Dirichlet's theorem
- [ ] Root locus sketch for flutter (four roots, one pair in the right half-plane)

### Likely oral questions (L13)

1. **What is a force field? How does it change the equations?** State-dependent force, linearisation, k\_f and c\_f added to structural terms, possibly negative.
2. **Define stability in the sense of Lyapunov. How do you check it in practice?** Definitions, linearisation theorem and its three outcomes.
3. **Divergence vs dynamic instability (1 dof): causes and time histories.** Negative k\_T vs negative c\_T.
4. **Explain friction-induced vibration.** The full derivation with the falling friction characteristic.
5. **When is a force field conservative? What does it imply for stability?** Schwarz condition, symmetric stiffness, Dirichlet.
6. **What is flutter and where does the energy come from?** Non-conservative field, non-symmetric \[K\_F\], elliptical orbits in opposite directions.
7. **Why can't Lyapunov conclude when the linearised system is only marginally stable?** Neglected nonlinear terms decide the behaviour.

### Traps and follow-ups (L13)

- "Undamped structure with a conservative field and positive definite \[K\_T\]: is it asymptotically stable?" → no, only stable (Dirichlet). Nothing dissipates.
- "Can flutter happen in a conservative system?" → no: symmetric \[K\_T\] gives real λ².
- "Why does adding structural damping help against flutter?" → it shifts roots left; flutter then appears only above a threshold of the field intensity (e.g. a critical speed).
- Link to L01: gravitational stiffness of the inverted pendulum (k\_g = −mgl) is a conservative field causing divergence.

## L14 — Stability of ground vehicles

**Big idea:** the wheel–ground contact force depends on the vehicle's motion through the **creepages** (relative slip velocities), so it is a force field (L13). For a car, the cornering forces can make an **oversteering** vehicle diverge above a critical speed (divergence). For a railway wheelset, conicity plus creep forces give a non-symmetric stiffness, so **flutter** (hunting) appears above a critical speed.

### 1. Rolling contact

**Rigid bodies (Coulomb).** Contact is a point. Without slip, v\_C = ωR and T ≤ f\_s N. With slip, there is no kinematic link and T = f\_d N.

**Deformable bodies.** There is a contact patch of length 2a. The normal pressure is roughly parabolic (Hertz) and is not affected by the tangential forces. Three new facts: v\_C ≠ ωR even without gross slip, the tangential force depends on the kinematics (a force field), and the patch has a leading **adhesion** zone and a trailing **slip** zone.

**Brush model.** Each element of the tread is a bristle with local stiffness: τ(ξ) = C u(ξ). Velocity of the bristle tip: v = v\_C − ωR + v\_C du/dξ. In adhesion v = 0:

```latex
\frac{du}{d\xi} = -\frac{v_C - \omega R}{v_C} = -\varepsilon_l, \qquad \varepsilon_l = \frac{v_C - \omega R}{v_C}\;\text{(longitudinal creepage)}, \qquad \tau(\xi) = -C\,\varepsilon_l\,\xi
```

The bristle enters undeformed (τ(0) = 0), and τ grows linearly through the patch. Adhesion holds while the magnitude of τ ≤ f\_s p(ξ): a line under a parabola. Beyond the crossing point, slip: τ = f\_d p. T is the area under the curve. As creepage grows the slip zone grows, so T(ε\_l) is linear at small creepage then saturates (and decreases if f\_d < f\_s).

**3D:** the creepage vector ε = (v\_C − ω ∧ R)/v\_C has a longitudinal part ε\_l and a transversal part ε\_t. For small values ε\_t is the **slip angle** α (angle between the wheel plane and the wheel velocity). Creep forces T\_l, T\_t = −μ(ε\_l, ε\_t, N)·N. The spin moment is neglected for trains, and gives self-alignment for steered tyres.

### 2. Road vehicle: bicycle model

Assumptions: small steer and slip angles, constant speed V, no traction or braking, no spin, no aero. a = distance from G to the front axle, b = from G to the rear, L = a + b.

**Kinematic steering (no slip):** δ = L/R, independent of speed. That contradicts driving experience.

**With slip angles:** δ = L/R + α\_f − α\_r. Linear tyres: T\_tf = C\_f α\_f and T\_tr = C\_r α\_r (C = **cornering stiffness**, in N/rad). Equilibrium with the centrifugal force mV²/R: T\_tf = mV²b/(RL) and T\_tr = mV²a/(RL). Substituting:

```latex
\delta = \frac{L}{R}\left(1 + KV^2\right), \qquad K = \frac{m}{L^2}\left(\frac{b}{C_f} - \frac{a}{C_r}\right)\;\text{(understeer coefficient)}
```

| K | Behaviour | Steer angle with speed |
| --- | --- | --- |
| > 0 | Understeer | Increases with V² |
| = 0 | Neutral | Constant |
| < 0 | Oversteer | Decreases, reaches 0 at the critical speed |

More understeer if: G moves forward (smaller a, larger b), C\_f decreases, or C\_r increases (tyres, load transfer, anti-roll bars, traction/braking).

**Stability (2 states).** State z = {β, ψ̇}: β = body sideslip angle, ψ̇ = yaw rate. Position does not matter, only velocities. Lateral acceleration a\_G = V(β̇ + ψ̇). Slip angles: α\_f = δ − β − aψ̇/V and α\_r = −β + bψ̇/V. Equations:

```latex
T_{tf} + T_{tr} = mV(\dot\beta + \dot\psi), \qquad aT_{tf} - bT_{tr} = J_G\ddot\psi \;\Rightarrow\; [A]\dot{\underline z} + [B]\underline z = \underline C\,\delta
```

Steady state z₀ = \[B\]⁻¹Cδ₀ reproduces the formula above (ψ̇ = V/R). Perturbation: det(λ\[A\] + \[B\]) = 0 gives pλ² + qλ + r = 0 with

```latex
p = mVJ_G > 0, \quad q = m(C_F a^2 + C_R b^2) + J_G(C_F + C_R) > 0, \quad r = \frac{C_F C_R L^2}{V}\left(1 + KV^2\right)
```

If K < 0, r < 0 above the **critical speed** V\_cr = √(−1/K): one real positive root, **divergence**. An understeering car (K > 0) is always stable in this model.

### 3. Railway wheelset: hunting

2 dof: lateral displacement y and yaw σ. Constant speed V on straight track. Primary suspension: k\_y, c\_y laterally and k\_x, c\_x longitudinally at lateral distance b. Conical wheels (cone angle γ) on knife-edge rails, half track gauge s, nominal radius R₀.

**Kinematics.** Rolling radii R\_l = R₀ − γy and R\_r = R₀ + γy (sign convention as in the notes). Creepages:

```latex
\varepsilon_{ll} = -\varepsilon_{lr} = -\frac{s\dot\sigma}{V} + \frac{\gamma y}{R_0}, \qquad \varepsilon_{tl} = \varepsilon_{tr} = \frac{\dot y}{V} - \sigma\;\;\text{(sign as in the notes)}
```

**Linear creep forces (Kalker):** T\_l = −f₁₁ε\_l and T\_t = −f₂₂ε\_t. Cross terms vanish around zero creepage when spin is neglected.

**Result:**

```latex
[m]\ddot{\underline x} + ([c_s] + [c_F])\dot{\underline x} + ([k_s] + [k_F])\underline x = 0, \qquad [c_F] = \frac{2}{V}\begin{bmatrix}f_{22} & 0\\ 0 & f_{11}s^2\end{bmatrix}, \qquad [k_F] = \begin{bmatrix}0 & -2f_{22}\\ 2f_{11}\dfrac{s\gamma}{R_0} & 0\end{bmatrix}
```

(Signs depend on the conventions for y and σ: what matters is that the off-diagonal terms of \[k\_F\] have **opposite signs**.)

**Interpretation:**

- &#91;k\_F\] is **non-symmetric** → the positional field is non-conservative → the flutter condition of L13 is satisfied.
- &#91;c\_F\] is positive definite but **∝ 1/V**. At low speed, contact damping plus suspension damping dissipate the energy injected by \[k\_F\]. As V grows, damping falls until it can't: flutter above the **linear critical speed**.
- Nonlinear analysis: above the **nonlinear critical speed** (lower than the linear one) a stable limit cycle exists: **hunting**. Bifurcation diagram: a subcritical Hopf bifurcation.
- Design: stiffer primary suspension (larger diagonal of \[k\_T\]) raises the critical speed. Higher conicity γ (larger off-diagonal term) lowers it.

### On your blackboard (L14)

- [ ] Brush model: bristle velocity, adhesion condition, ε\_l, τ = −Cε\_lξ
- [ ] Adhesion/slip sketch (line vs parabola) and the T(ε\_l) curve
- [ ] Creepage vector, slip angle
- [ ] Bicycle model: δ = L/R + α\_f − α\_r, axle forces, understeer coefficient K, δ(V) plot for K > 0, = 0, < 0
- [ ] State equations in β and ψ̇, the coefficients p, q, r and V\_cr = √(−1/K)
- [ ] Wheelset: conicity and rolling radii, creepages, Kalker linear coefficients
- [ ] &#91;c\_F\] ∝ 1/V and non-symmetric \[k\_F\]; why flutter appears above a critical speed
- [ ] Hopf bifurcation diagram (linear vs nonlinear critical speed)

### Likely oral questions (L14)

1. **Why is the contact force a force field? Explain creepage with the brush model.** Bristle kinematics, adhesion and slip zones, T(ε).
2. **Derive the steering angle of a car in steady cornering and define understeer and oversteer.** Bicycle model, slip angles, K.
3. **When does a car become unstable and what type of instability is it?** Oversteer, r < 0, divergence above √(−1/K).
4. **Which design changes increase understeer?** G forward, tyre cornering stiffness, load transfer.
5. **What is hunting? Derive the linear model of a wheelset and explain the mechanism.** Conicity, creepages, non-symmetric \[k\_F\], damping ∝ 1/V, flutter.
6. **What is the difference between the linear and nonlinear critical speed?** Hopf bifurcation, limit cycle below the linear critical speed.
7. **How do you raise the critical speed of a railway vehicle?** Stiffer primary suspension, lower conicity.

### Traps and follow-ups (L14)

- "Is the oversteering car's instability a flutter?" → no: one real positive root, so divergence. The wheelset is flutter (complex roots).
- "Why does wheelset damping decrease with speed?" → creepage = velocity / V, so the force per unit velocity is ∝ 1/V.
- "Why do conical wheels exist at all?" → self-centring and curving without flanges, at the price of hunting.
- Link to L13: car = divergence from negative stiffness; wheelset = flutter from a non-conservative positional field; friction slider = negative damping.

## Cross-chapter questions and final checklist

**The professor will often start with one chapter and then jump across.** These questions link topics. Practise them out loud: each answer should take 3–5 minutes and use at least one formula and one sketch.

### Cross-chapter oral questions

1. **Lumped vs continuous systems: what is the same and what changes?** n ODEs vs one PDE; eigenproblem det(−ω²\[m\] + \[k\]) = 0 vs boundary-value problem det\[H(γ)\] = 0; n modes vs infinitely many; orthogonality in both; modal approach in both (L02, L03, L06–L09).
2. **Three ways to get natural frequencies of a beam: analytical, modal (Rayleigh-type expansion), FEM. Compare them.** Exact but limited / exact for the modes you keep / general and approximate, elements must be quasi-static (L07, L09, L10).
3. **Where does symmetry of \[m\] and \[k\] come from, and what happens when \[k\] is not symmetric?** λᵀ\[·\]λ structure and conservative forces (L01) → real frequencies and orthogonal modes (L02–L03). Non-symmetric stiffness from a non-conservative field → flutter (L13–L14).
4. **Every way a stiffness can become negative or "strange".** Gravitational stiffness of an inverted pendulum (L01), second-order stiffness of preloaded springs (L01), axial preload in a beam (L07), field stiffness k\_f (L13), oversteering car (L14).
5. **Every damping model in the course.** Viscous dampers in \[c\] (L01), modal damping and proportional damping (L03), identified h\_i (L04), modal equivalent damping in continua (L09), Rayleigh fit in FEM (L10), negative damping from friction (L13), creep damping ∝ 1/V (L14).
6. **How do you go from a measured FRF to a validated model?** L04 identification → compare with L03/L10 model modes → tune parameters (model updating).
7. **What is the role of Lagrange's equations across the course?** L01 lumped systems, L03 modal coordinates, L09 continuous systems, L10–L11 FEM, L12 rigid body in 3D (including reactions).
8. **Explain the meaning of a mode of vibration in three contexts.** Vector of a 2-dof system (L02), sine function of a beam (L06–L07), FEM eigenvector (L10). Same interpretation: shape, nodes, amplitude ratios.
9. **Three kinds of instability with one example each.** Divergence (oversteering car, inverted pendulum), dynamic instability by negative damping (friction slider), flutter (wheelset hunting, wing) (L13–L14).
10. **When is the linearised model enough and when is it not?** Small motion around equilibrium (L01). Lyapunov's inconclusive case (L13). Nonlinear critical speed below the linear one (L14).

### Formulas to know cold (final blackboard check)

Try to write the whole list on the blackboard from memory in 30 minutes. Whatever you can't write is what to review next.

| Chapter | Formula |
| --- | --- |
| L01 | Lagrange's equation; m(x) = Σ(mλ² + Jλ\_θ²); k = Σkλ² + ΣkΔ₀ν + Σmgν\_h; \[m\] = λᵀm\_phλ |
| L02 | ω = √(k/m), c\_cr = 2mω, h = c/c\_cr, ω\_d = ω√(1−h²); G = 1/(k − mΩ² + icΩ); det(−ω²\[m\] + \[k\]) = 0 |
| L03 | x = \[Φ\]q; orthogonality; \[c\] = α\[m\] + β\[k\]; f̄ = \[Φ\]ᵀf |
| L04 | G\_jk = Σ x₀j x₀k / (k̄ − Ω²m̄ + iΩc̄); h = (ω₂² − ω₁²)/(4ω²); d∠G/dΩ = −1/(hω) |
| L05 | ε = ∂u/∂x, γ = ∂u/∂y + ∂v/∂x; Hooke 3D; G = E/(2(1+ν)) |
| L06 | EAu'' = mü; c = √(E/ρ); ω\_k = kπc/L (clamped–clamped) |
| L07 | M = EIw''; EIw'''' + mẅ = 0; γ⁴ = mω²/EI; ω\_k = (kπ/L)²√(EI/m) |
| L08 | M\_t = GI\_Pϑ'; c = √(G/ρ); I\_P = πD⁴/32 |
| L09 | \[m̄\] = ∫ΦmΦᵀdx; \[k̄\] = ∫Φ''EIΦ''ᵀdx; c̄ = 2hm̄ω |
| L10 | Hermite shape functions; 4×4 bending stiffness; \[m^G\] = Λᵀm^LΛ; partition ff/fc |
| L11 | f\_i = ⅛(1+ξξ\_i)(1+ηη\_i)(1+ζζ\_i); \[K\] = ∫BᵀEB dVol; dVol = det J dξ dη dζ |
| L12 | T = ½mv\_G² + ½ωᵀ\[J\_G\]ω; ω = \[A\]θ̇; balancing conditions |
| L13 | k\_f = −∂F/∂x, c\_f = −∂F/∂ẋ; Lyapunov table; biquadratic λ equation |
| L14 | ε\_l = (v\_C − ωR)/v\_C; δ = (L/R)(1 + KV²); K = (m/L²)(b/C\_f − a/C\_r); V\_cr = √(−1/K) |

### Sketches to know cold

- [ ] Bode diagram of a 1-dof system (several h) with the three ranges
- [ ] 2-dof Bode diagrams with two resonances and an anti-resonance
- [ ] Mode shapes: 2-dof snapshots, first 3 modes of a beam with nodes
- [ ] Half-power points on an FRF peak
- [ ] Element dx for axial, bending, torsion
- [ ] Brush model adhesion/slip and T(ε)
- [ ] δ(V) for under-, neutral and oversteer
- [ ] Root positions for divergence, dynamic instability and flutter
- [ ] Hopf bifurcation diagram for the wheelset

### How to use this in the last weeks

1. Each day, pick one chapter. Read its section, then close it and answer its oral questions out loud.
2. Rewrite its blackboard list from memory. Mark what you missed.
3. Every few days, do two or three cross-chapter questions.
4. Ask me for a **mock oral**: I'll play the professor, ask a question from any chapter, then push with follow-ups and tell you what was missing.
