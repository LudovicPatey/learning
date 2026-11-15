---
title: Weihrauch reducibility
summary: Uniform computable reductions; problems that uniformly admit computable solutions, and the pigeonhole principle as a problem that admits computable solutions but not uniformly; continuity arguments; the omniscience principles LPO and LLPO.
duration: 40
prerequisites: [wkl-reductions]
---

A computable reduction may depend on the instance in a non-uniform way: the proof that $\mathsf{RT}^1_2$ admits computable solutions chooses a color class that is infinite, a choice that cannot be made by an algorithm reading the coloring. **Weihrauch reducibility** requires the reduction to be given by two fixed Turing functionals, one transforming the instance and one transforming the solution back. It was introduced by Weihrauch in computable analysis at the end of the 1980s, and first appeared in two technical reports of 1992. Gherardi and Marcone (2009), and independently Dorais, Dzhafarov, Hirst, Mileti and Shafer (2016), brought it to reverse mathematics, where it measures the uniform content of proofs.

## Definitions

:::definition{#def-weihrauch}
Let $\mathsf P$ and $\mathsf Q$ be problems.

1. $\mathsf P$ is **Weihrauch reducible** to $\mathsf Q$, written $\mathsf P \leq_W \mathsf Q$, if there are Turing functionals $\Phi$ and $\Psi$ such that, for every instance $X$ of $\mathsf P$, $\Phi^X$ is an instance of $\mathsf Q$, and for every solution $\widetilde Y$ to $\Phi^X$, $\Psi^{X \oplus \widetilde Y}$ is a solution to $X$.
2. $\mathsf P$ is **strongly Weihrauch reducible** to $\mathsf Q$, written $\mathsf P \leq_{sW} \mathsf Q$, if moreover $\Psi$ only uses $\widetilde Y$: $\Psi^{\widetilde Y}$ is a solution to $X$.
3. $\mathsf P$ **uniformly admits computable solutions** if there is a Turing functional $\Phi$ such that $\Phi^X$ is a solution to $X$ for every instance $X$.
:::

In item 1, $\Phi^X$ and $\Psi^{X \oplus \widetilde Y}$ are required to be total, as characteristic functions of sets. The functional $\Phi$ is the **forward** functional and $\Psi$ the **backward** functional. We write $\mathsf P \equiv_W \mathsf Q$ if $\mathsf P \leq_W \mathsf Q$ and $\mathsf Q \leq_W \mathsf P$; the equivalence classes are the **Weihrauch degrees**.

:::figure[Weihrauch and strong Weihrauch reductions of $\mathsf P$ to $\mathsf Q$. They have the shape of the computable reductions of the previous lesson, with the two computations given by functionals $\Phi$ and $\Psi$ that do not depend on $X$.]
<svg class="fig" viewBox="0 0 660 262" width="660" role="img" aria-label="Diagrams of a Weihrauch reduction and of a strong Weihrauch reduction of P to Q, with forward functional Phi and backward functional Psi"><defs><marker id="ah-wred" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker><marker id="ah-wreda" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><text x="90" y="34" text-anchor="middle" class="math" font-size="18">P</text><text x="250" y="34" text-anchor="middle" class="math" font-size="18">Q</text><text x="170.0" y="250" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" dx="5">≤</tspan><tspan class="mrm" font-size="11" dy="4">W</tspan><tspan dx="5" dy="-4">Q</tspan></text><rect x="68" y="50" width="44" height="30" rx="6" class="cell"/><text x="90" y="71" text-anchor="middle" class="math" font-size="17">X</text><rect x="228" y="50" width="44" height="30" rx="6" class="cell"/><text x="250" y="71" text-anchor="middle" class="math" font-size="17">X̃</text><rect x="228" y="180" width="44" height="30" rx="6" class="cell"/><text x="250" y="201" text-anchor="middle" class="math" font-size="17">Ỹ</text><rect x="68" y="180" width="44" height="30" rx="6" class="head-cell"/><text x="90" y="201" text-anchor="middle" class="math" font-size="17">Y</text><line x1="114" y1="65" x2="224" y2="65" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-wred)"/><text x="170.0" y="57" text-anchor="middle" class="label">X̃ = Φ(X)</text><line x1="250" y1="82" x2="250" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-wred)"/><line x1="90" y1="82" x2="90" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-wred)"/><text x="258" y="133.0" text-anchor="start" class="label">any solution</text><text x="82" y="133.0" text-anchor="end" class="label">a solution</text><line x1="226" y1="195" x2="116" y2="195" class="accent-stroke" stroke-width="1.6" marker-end="url(#ah-wred)"/><text x="170.0" y="224" text-anchor="middle" class="label">Y = Ψ(X ⊕ Ỹ)</text><path d="M108,82 C160,120 170,160 150,191" class="accent-stroke" stroke-width="1.2" stroke-dasharray="2 3" marker-end="url(#ah-wreda)"/><text x="170" y="132" text-anchor="start" class="label">X is used</text><text x="410" y="34" text-anchor="middle" class="math" font-size="18">P</text><text x="570" y="34" text-anchor="middle" class="math" font-size="18">Q</text><text x="490.0" y="250" text-anchor="middle" class="math" font-size="16">P<tspan class="mrm" dx="5">≤</tspan><tspan class="mrm" font-size="11" dy="4">sW</tspan><tspan dx="5" dy="-4">Q</tspan></text><rect x="388" y="50" width="44" height="30" rx="6" class="cell"/><text x="410" y="71" text-anchor="middle" class="math" font-size="17">X</text><rect x="548" y="50" width="44" height="30" rx="6" class="cell"/><text x="570" y="71" text-anchor="middle" class="math" font-size="17">X̃</text><rect x="548" y="180" width="44" height="30" rx="6" class="cell"/><text x="570" y="201" text-anchor="middle" class="math" font-size="17">Ỹ</text><rect x="388" y="180" width="44" height="30" rx="6" class="head-cell"/><text x="410" y="201" text-anchor="middle" class="math" font-size="17">Y</text><line x1="434" y1="65" x2="544" y2="65" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-wred)"/><text x="490.0" y="57" text-anchor="middle" class="label">X̃ = Φ(X)</text><line x1="570" y1="82" x2="570" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-wred)"/><line x1="410" y1="82" x2="410" y2="177" class="muted-stroke" stroke-width="1.3" stroke-dasharray="5 4" marker-end="url(#ah-wred)"/><text x="578" y="133.0" text-anchor="start" class="label">any solution</text><text x="402" y="133.0" text-anchor="end" class="label">a solution</text><line x1="546" y1="195" x2="436" y2="195" class="accent-stroke" stroke-width="1.6" marker-end="url(#ah-wred)"/><text x="490.0" y="224" text-anchor="middle" class="label">Y = Ψ(Ỹ)</text></svg>
:::

Weihrauch reducibility implies computable reducibility, and strong Weihrauch reducibility implies strong computable reducibility. Together with the previous lessons, we have the following implications. Dzhafarov and Mummert show that no other implication holds in general (their Figure 4.6).

:::figure[Implications between the reducibilities of the course. An arrow from one reducibility to another means that if $\mathsf P$ is reducible to $\mathsf Q$ in the first sense, it is reducible in the second.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="Implications between the reducibilities: strong Weihrauch implies Weihrauch and strong computable; each of these implies computable reducibility, which implies omega-reducibility"><defs><marker id="ah-impl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="38" y="67" width="64" height="32" rx="6" class="head-cell"/><text x="70" y="89" text-anchor="middle" class="mrm" font-size="17">≤<tspan font-size="12" dy="4">sW</tspan></text><rect x="198" y="17" width="64" height="32" rx="6" class="cell"/><text x="230" y="39" text-anchor="middle" class="mrm" font-size="17">≤<tspan font-size="12" dy="4">W</tspan></text><rect x="198" y="117" width="64" height="32" rx="6" class="cell"/><text x="230" y="139" text-anchor="middle" class="mrm" font-size="17">≤<tspan font-size="12" dy="4">sc</tspan></text><rect x="358" y="67" width="64" height="32" rx="6" class="cell"/><text x="390" y="89" text-anchor="middle" class="mrm" font-size="17">≤<tspan font-size="12" dy="4">c</tspan></text><rect x="498" y="67" width="64" height="32" rx="6" class="cell"/><text x="530" y="89" text-anchor="middle" class="mrm" font-size="17">≤<tspan font-size="12" dy="4">ω</tspan></text><line x1="104.4" y1="79.0" x2="193.7" y2="41.6" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-impl)"/><line x1="104.4" y1="91.0" x2="193.7" y2="128.4" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-impl)"/><line x1="264.4" y1="41.0" x2="353.7" y2="78.4" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-impl)"/><line x1="264.4" y1="129.0" x2="353.7" y2="91.6" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-impl)"/><line x1="426.0" y1="85.0" x2="492.0" y2="85.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-impl)"/><text x="230" y="12" text-anchor="middle" class="label">uniform</text><text x="230" y="168" text-anchor="middle" class="label">strong: the backward step does not use the instance</text></svg>
:::

As for computable reducibility, $\mathsf P$ uniformly admits computable solutions if and only if $\mathsf P \leq_W \mathsf{Id}$: given $\Phi$, take the identity as forward functional and $\Psi^{X \oplus Y} = \Phi^X$; given $\Phi$ and $\Psi$, the functional $X \mapsto \Psi^{X \oplus \Phi^X}$ solves $\mathsf P$. Some examples:

- $\mathsf{WKL} \leq_{sW} \mathsf{KL}$, with both functionals the identity.
- $\mathsf{Id} \leq_W \mathsf{RT}^1_2$: the forward functional outputs the constant coloring $0$, whatever the instance, and the backward functional outputs $X$, read from $X \oplus \widetilde Y$. But $\mathsf{Id} \not\leq_{sc} \mathsf{RT}^1_2$ (previous lesson), so $\mathsf{Id} \not\leq_{sW} \mathsf{RT}^1_2$.
- $\mathsf J \times \mathsf J \leq_W \mathsf J$: the forward functional is the identity, and the jump $(X_0 \oplus X_1)'$ computes $X_0' \oplus X_1'$, uniformly. Two instances of the jump given at the same time cost a single application.

## Uniformity and continuity

:::proposition{#prop-rt12-not-uniform}
$\mathsf{RT}^1_2$ admits computable solutions, but not uniformly. Consequently, $\mathsf{RT}^1_2 \leq_c \mathsf{RT}^1_1$ but $\mathsf{RT}^1_2 \not\leq_W \mathsf{RT}^1_1$.
:::

The idea of the proof: to output an element $x$, a functional reads only finitely many values of the coloring. Whatever it outputs, the coloring can be changed beyond what was read, so that the color of $x$ becomes the color used finitely often.

:::proof{of=prop-rt12-not-uniform}
A coloring $f : \nat \to 2$ computes both color classes, and one of them is infinite. Suppose that $\Phi^f$ is an infinite homogeneous set for every $f$. Let $f_0$ be the constant coloring $0$. The set $\Phi^{f_0}$ is infinite; take $x \in \Phi^{f_0}$, and let $u$ be the use of the computation $\Phi^{f_0}(x) = 1$. Let $v = \max(u, x + 1)$ and $f_1$ the coloring with $f_1(n) = 0$ for $n < v$ and $f_1(n) = 1$ for $n \geq v$. Since $f_1$ agrees with $f_0$ below $u$, we have $x \in \Phi^{f_1}$, and $f_1(x) = 0$. A homogeneous set for $f_1$ containing $x$ has color $0$, so it is included in $\{ 0, \dots, v - 1 \}$ and is finite: a contradiction. The problem $\mathsf{RT}^1_1$ uniformly admits computable solutions, with $\Phi^f = \nat$, and a problem Weihrauch reducible to such a problem uniformly admits computable solutions; this gives the consequence.
:::

:::figure[The two colorings of the proof of :ref{#prop-rt12-not-uniform}, with $u = 5$ and $x = 7$, so that $v = 8$. The computation that puts $x$ into $\Phi^{f_0}$ reads only $f_0 \uh u$, which $f_1$ shares.]
<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="The colorings f0 and f1 of the proof: they agree below the use u, so the functional puts x in both outputs, but x has color 0 for f1, which is 1 from v on"><defs><marker id="ah-cont" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><text x="86" y="61" text-anchor="middle" class="math" font-size="17">f₀</text><rect x="110" y="40" width="30" height="30" class="cell"/><text x="125.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="140" y="40" width="30" height="30" class="cell"/><text x="155.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="170" y="40" width="30" height="30" class="cell"/><text x="185.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="200" y="40" width="30" height="30" class="cell"/><text x="215.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="230" y="40" width="30" height="30" class="cell"/><text x="245.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="260" y="40" width="30" height="30" class="cell"/><text x="275.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="290" y="40" width="30" height="30" class="cell"/><text x="305.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="320" y="40" width="30" height="30" class="cell"/><text x="335.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="350" y="40" width="30" height="30" class="cell"/><text x="365.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="380" y="40" width="30" height="30" class="cell"/><text x="395.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="410" y="40" width="30" height="30" class="cell"/><text x="425.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="440" y="40" width="30" height="30" class="cell"/><text x="455.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="470" y="40" width="30" height="30" class="cell"/><text x="485.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="500" y="40" width="30" height="30" class="cell"/><text x="515.0" y="61" text-anchor="middle" class="mrm" font-size="15">0</text><text x="538" y="61" class="mrm muted" font-size="16">⋯</text><text x="86" y="125" text-anchor="middle" class="math" font-size="17">f₁</text><rect x="110" y="104" width="30" height="30" class="cell"/><text x="125.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="140" y="104" width="30" height="30" class="cell"/><text x="155.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="170" y="104" width="30" height="30" class="cell"/><text x="185.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="200" y="104" width="30" height="30" class="cell"/><text x="215.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="230" y="104" width="30" height="30" class="cell"/><text x="245.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="260" y="104" width="30" height="30" class="cell"/><text x="275.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="290" y="104" width="30" height="30" class="cell"/><text x="305.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="320" y="104" width="30" height="30" class="cell"/><text x="335.0" y="125" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="350" y="104" width="30" height="30" class="cell head-cell"/><text x="365.0" y="125" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="380" y="104" width="30" height="30" class="cell head-cell"/><text x="395.0" y="125" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="410" y="104" width="30" height="30" class="cell head-cell"/><text x="425.0" y="125" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="440" y="104" width="30" height="30" class="cell head-cell"/><text x="455.0" y="125" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="470" y="104" width="30" height="30" class="cell head-cell"/><text x="485.0" y="125" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="500" y="104" width="30" height="30" class="cell head-cell"/><text x="515.0" y="125" text-anchor="middle" class="mrm" font-size="15">1</text><text x="538" y="125" class="mrm muted" font-size="16">⋯</text><text x="125.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="155.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="185.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="215.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="245.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="275.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">5</text><text x="305.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">6</text><text x="335.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">7</text><text x="365.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">8</text><text x="395.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">9</text><text x="425.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">10</text><text x="455.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">11</text><text x="485.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">12</text><text x="515.0" y="34" text-anchor="middle" class="mrm muted" font-size="11">13</text><path d="M112,78 L112,86 L258,86 L258,78" class="accent-stroke" stroke-width="1.4"/><text x="110" y="99" dx="0" text-anchor="start" class="label">use u: read by the computation Φ(x) = 1</text><circle cx="335.0" cy="55" r="13" class="accent-stroke" stroke-width="1.6"/><circle cx="335.0" cy="119" r="13" class="accent-stroke" stroke-width="1.6"/><text x="335.0" y="14" text-anchor="middle" class="label">x</text><line x1="350" y1="96" x2="350" y2="146" class="ink-stroke" stroke-width="1.4"/><text x="350" y="160" text-anchor="middle" class="label">v</text><text x="300" y="184" text-anchor="middle" class="label">f₀ is constant 0, and x ∈ Φ(f₀); f₁ agrees with f₀ below v ≥ u, so x ∈ Φ(f₁),</text><text x="300" y="202" text-anchor="middle" class="label">but the only color with infinitely many elements is 1, while f₁(x) = 0</text></svg>
:::

The argument is a **continuity argument**: a functional decides each bit of its output from a finite part of its input, so it cannot wait for information that is only available in the limit. In topological terms, a functional induces a continuous map on Cantor space, and the proof exhibits a discontinuity that every solution map must have. Most proofs of non-reducibility in the Weihrauch degrees have this form, often combined with a diagonalization against all pairs of functionals; it replaces the computability-theoretic arguments of the previous lessons, which cannot separate problems that admit computable solutions.

Dorais, Dzhafarov, Hirst, Mileti and Shafer, Hirschfeldt and Jockusch, and Brattka and Rakotoniaina showed more generally that $\mathsf{RT}^1_{k+1} \not\leq_W \mathsf{RT}^1_k$ for every $k \geq 1$; we admit this result. Likewise, the intermediate value theorem does not uniformly admit computable solutions, although every computable instance has a computable solution (:ref{#thm-ivt-rca}): a proof must decide, from finite approximations of the function, whether it vanishes at a rational point, and near which root to look.

:::quiz[uniformity]
In the proof of :ref{#prop-rt12-not-uniform}, why can $\Phi^{f_1}$ not avoid the element $x$?

- [x] Because the computation $\Phi^{f_0}(x) = 1$ reads only $f_0 \uh u$, which is also an initial segment of $f_1$; so $\Phi^{f_1}(x) = 1$ by the use principle.
- [ ] Because $x$ has color $0$ for $f_1$.

  The color of $x$ is what makes its presence harmful; its presence comes from the use principle.
- [ ] Because $\Phi^{f_1}$ is infinite.

  Infinity is required of the output; it does not force $x$ into it.

---

Why does the computable reduction of $\mathsf{RT}^1_2$ to $\mathsf{RT}^1_1$ not yield a Weihrauch reduction?

- [x] Because the backward computation must decide which color class is infinite, a $\Pi^0_2$ property of the instance; a computable reduction may choose a different algorithm for each instance, a Weihrauch reduction may not.
- [ ] Because $\mathsf{RT}^1_1$ has no computable instance.

  Every constant coloring is a computable instance.
- [ ] Because the color classes are not computable from the coloring.

  They are computable, uniformly; what is not computable is which one is infinite.
:::

## The omniscience principles

The following problems come from constructive mathematics, where the corresponding statements are not provable: they assert that certain questions about an infinite sequence can be decided. They have instances in $\{0, 1\}^\nat$ and solutions in $\{ 0, 1 \}$, coded as sets: $0$ by $\emptyset$ and $1$ by $\{ 0 \}$, so that a solution is read from the first bit of its code.

:::definition{#def-lpo-llpo}
1. The **limited principle of omniscience** $\mathsf{LPO}$: an instance is a sequence $p \in \{0, 1\}^\nat$; its solution is $1$ if $p(n) = 1$ for some $n$, and $0$ otherwise.
2. The **lesser limited principle of omniscience** $\mathsf{LLPO}$: an instance is a sequence $p \in \{0, 1\}^\nat$ with $p(n) = 1$ for at most one $n$; its solutions are the $i \in \{ 0, 1 \}$ such that $p(2m + i) = 0$ for every $m$.
:::

$\mathsf{LPO}$ decides a $\Sigma^0_1$ question about its instance. $\mathsf{LLPO}$ answers a weaker question: given two $\Pi^0_1$ statements, "no $1$ at an even position" and "no $1$ at an odd position", at least one of which is true, it names a true one. For example, the sequence with a single $1$ at position $5$ has the unique solution $0$, and the sequence $0^\infty$ has the two solutions $0$ and $1$. In general, an instance of $\mathsf{LLPO}$ has one solution if it contains a $1$, at a position of parity opposite to the solution, and two solutions otherwise. Both problems admit computable solutions, since their solutions are numbers; their content is entirely about uniformity.

:::proposition{#prop-llpo-lpo}
$\mathsf{LLPO} \leq_W \mathsf{LPO}$, and $\mathsf{LLPO}$ does not uniformly admit computable solutions.
:::

:::proof{of=prop-llpo-lpo}
Let $\Phi^p = p$, and let $\Psi^{p \oplus i}$ output $0$ if $i = 0$; if $i = 1$, it searches for $n$ with $p(n) = 1$ and outputs $1$ if $n$ is even and $0$ if $n$ is odd. If $p$ has no $1$, both values are solutions; if $p(n) = 1$, the search terminates, and the output has the parity opposite to $n$, as required.

Suppose that $\Phi^p$ is a solution for every instance $p$. Let $i = \Phi^{0^\infty}(0)$, the bit that determines the solution, and $u$ the use of this computation. Let $p_0$ and $p_1$ be the sequences with a single $1$, at positions $2u$ and $2u + 1$ respectively. Both agree with $0^\infty$ below $u$, so $\Phi^{p_0}(0) = \Phi^{p_1}(0) = i$, and $\Phi^{p_0}$ and $\Phi^{p_1}$ both code the solution $i$. But the only solution to $p_0$ is $1$, and the only solution to $p_1$ is $0$.
:::

The backward functional of the first part uses the instance: it searches $p$ for its $1$. A strong reduction is given in :ref{#ex-llpo-sw-lpo}. The converse reduction fails, $\mathsf{LPO} \not\leq_W \mathsf{LLPO}$; a continuity argument proves it in :ref{#ex-lpo-not-w-llpo}, and the next lesson derives it from the separation of the jump from weak König's lemma.

## Exercises

::::exercise{#ex-llpo-sw-lpo difficulty=1 objective="Build a strong Weihrauch reduction by moving the search into the forward functional."}
Show that $\mathsf{LLPO} \leq_{sW} \mathsf{LPO}$.

:::solution
Let $\Phi^p$ be the sequence $q$ with $q(n) = 1$ if $p(2m) = 1$ for some $2m \leq n$, and $0$ otherwise; and $\Psi^i = i$. The solution to $q$ is $1$ exactly when $p$ has a $1$ at an even position. In that case, $1$ is the only solution to $p$. Otherwise, $p$ has no $1$ at an even position, so $0$ is a solution to $p$. The backward functional does not use $p$.
:::
::::

::::exercise{#ex-lpo-not-w-llpo difficulty=2 objective="Separate the omniscience principles by a continuity argument against an arbitrary pair of functionals."}
Show directly that $\mathsf{LPO} \not\leq_W \mathsf{LLPO}$. Suppose that $\Phi$ and $\Psi$ witness the reduction, and let $q = \Phi^{0^\infty}$. Consider separately the case where $q$ has no $1$ and the case where it has one.

:::solution
For every solution $i$ to $q$, $\Psi^{0^\infty \oplus i}$ codes $0$, the solution to $0^\infty$; let $u$ be larger than the uses of the computations $\Psi^{0^\infty \oplus i}(0)$ for these $i$. If $q$ has no $1$, let $p$ have a single $1$, at position $u$. The instance $\Phi^p$ of $\mathsf{LLPO}$ has at most one $1$, so one of $0$ and $1$ is a solution to it, say $i$; it is also a solution to $q$. Since $p \oplus i$ agrees with $0^\infty \oplus i$ below $u$, $\Psi^{p \oplus i}(0) = 0$, while the solution to $p$ is $1$. If $q(n) = 1$, let $m \geq u$ be such that $\Phi^{0^\infty}(n) = 1$ with use at most $m$, and let $p$ have a single $1$, at position $m$. Then $\Phi^p(n) = 1$, so $\Phi^p$ has its only $1$ at position $n$, and has the same unique solution $i$ as $q$. Again $\Psi^{p \oplus i}(0) = 0$, while the solution to $p$ is $1$.
:::
::::

## Notes and references

The Weihrauch degrees of theorems of analysis — the intermediate value theorem, the maximum of a continuous function, monotone convergence — are determined in the course on computable analysis (:ref{#thm-ivt-llpo-wkl}, :ref{to="computable-analysis/maximum-and-limits"}).

Weihrauch reducibility was introduced by Weihrauch in the late 1980s, in two technical reports of 1992, and studied by his students; Brattka, Gherardi and Pauly survey its history and the theory of the Weihrauch degrees. Gherardi and Marcone (2009) defined it for arbitrary problems and proposed it as a uniform version of reverse mathematics; Dorais, Dzhafarov, Hirst, Mileti and Shafer (2016) and Hirschfeldt and Jockusch (2016) developed it for combinatorial principles. Hirschfeldt, *Slicing the Truth*, Section 2.2, calls it uniform reducibility. Dzhafarov and Mummert treat uniformity in Section 3.7, with the intermediate value theorem (Proposition 3.7.4), and Weihrauch reducibility and its strong form in Sections 4.3 and 4.4; the non-reductions between the $\mathsf{RT}^1_k$ are their Proposition 4.3.7. That $\mathsf{LLPO} <_W \mathsf{LPO}$ is due to Weihrauch (1992); see Brattka, Gherardi and Pauly, Proposition 7.17.

- K. Weihrauch, *The TTE-interpretation of three hierarchies of omniscience principles*, Informatik Berichte 130, FernUniversität Hagen, 1992.
- V. Brattka, G. Gherardi and A. Pauly, *Weihrauch complexity in computable analysis*, in Handbook of Computability and Complexity in Analysis, Springer, 2021, 367–417.
- G. Gherardi and A. Marcone, *How incomputable is the separable Hahn–Banach theorem?*, Notre Dame Journal of Formal Logic 50 (2009), 393–425.
- F. G. Dorais, D. D. Dzhafarov, J. L. Hirst, J. R. Mileti and P. Shafer, *On uniform relationships between combinatorial problems*, Transactions of the American Mathematical Society 368 (2016), 1321–1359.
- V. Brattka and T. Rakotoniaina, *On the uniform computational content of Ramsey's theorem*, Journal of Symbolic Logic 82 (2017), 1278–1316.
- D. R. Hirschfeldt and C. G. Jockusch, *On notions of computability-theoretic reduction between Π¹₂ principles*, Journal of Mathematical Logic 16 (2016), 1650002.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 3.7, 4.3 and 4.4.

:::::exercises
::::exercise{#ex-klb-w-j difficulty=1 objective="Check that the computable reduction of bounded König's lemma to the jump is uniform."}
Let $\mathsf{KL}_b$ be the bounded version of König's lemma of :ref{#ex-kl-bounded}, whose instances are pairs $(T, h)$ of an infinite finitely branching tree and a bound on its successors. Show that $\mathsf{KL}_b \leq_W \mathsf J$.

:::solution
Let $\Phi^{T \oplus h} = T \oplus h$. Whether a node $\sigma$ has an extension in $T$ of length $|\sigma| + n$ is decided by inspecting the finitely many strings of that length extending $\sigma$ whose values are bounded by $h$; so the set of extendible nodes is $\Pi^0_1(T \oplus h)$, with an index independent of $T$ and $h$, and it is computable in $(T \oplus h)'$, uniformly. Let $\Psi$ compute from $(T \oplus h)'$ the path that starts at the root, which is extendible, and always moves to the least extendible successor. The search for that successor terminates, since an extendible node has an extendible successor.
:::
::::

::::exercise{#ex-w-transitive difficulty=1 objective="Compose Weihrauch reductions by composing their functionals."}
Show that $\leq_W$ and $\leq_{sW}$ are transitive, by writing the forward and backward functionals of the composed reduction.

:::solution
Let $\mathsf P \leq_W \mathsf Q$ via $\Phi_1, \Psi_1$ and $\mathsf Q \leq_W \mathsf R$ via $\Phi_2, \Psi_2$. Let $\Phi^X = \Phi_2^{\Phi_1^X}$ and $\Psi^{X \oplus \widehat Y} = \Psi_1^{X \oplus \Psi_2^{\Phi_1^X \oplus \widehat Y}}$; both are Turing functionals, since the oracle of each inner computation is computed uniformly from the given oracle. For an instance $X$ of $\mathsf P$, $\Phi_1^X$ is an instance of $\mathsf Q$, and $\Phi^X$ an instance of $\mathsf R$. If $\widehat Y$ is a solution to $\Phi^X$, then $\Psi_2^{\Phi_1^X \oplus \widehat Y}$ is a solution to $\Phi_1^X$, and $\Psi^{X \oplus \widehat Y}$ a solution to $X$. For strong reductions, take $\Psi^{\widehat Y} = \Psi_1^{\Psi_2^{\widehat Y}}$, with the same verification.
:::
::::

::::exercise{#ex-llpo-two-sequences difficulty=1 objective="Check that LLPO can be presented as a choice between two sequences, by strong Weihrauch reductions in both directions."}
Let $\mathsf{LLPO}'$ be the problem whose instances are the pairs $p_0 \oplus p_1$ of sequences in $\{0, 1\}^\nat$, at most one of which contains a $1$, the solutions being the $i < 2$ such that $p_i = 0^\infty$. Show that $\mathsf{LLPO}' \equiv_{sW} \mathsf{LLPO}$.

:::solution
($\mathsf{LLPO} \leq_{sW} \mathsf{LLPO}'$) Given $p$, let $p_i(m) = p(2m + i)$. Since $p$ has at most one $1$, at most one of $p_0, p_1$ contains a $1$. The solutions to $p_0 \oplus p_1$ are the $i$ with $p(2m + i) = 0$ for all $m$, which are the solutions to $p$. The backward functional is the identity.

($\mathsf{LLPO}' \leq_{sW} \mathsf{LLPO}$) Given $p_0 \oplus p_1$, let $p(2m + i) = 1$ if $p_i(m) = 1$ and $p_i(m') = 0$ for all $m' < m$, and $p(2m + i) = 0$ otherwise. At most one $p_i$ contains a $1$, and $p$ records only its first $1$, so $p$ has at most one $1$ and is an instance of $\mathsf{LLPO}$. If $p_i = 0^\infty$, then $p(2m + i) = 0$ for all $m$. If $p_i$ contains a $1$, at a least position $m$, then $p(2m + i) = 1$. So the solutions to $p$ are those to $p_0 \oplus p_1$, and the backward functional is again the identity.
:::
::::

::::exercise{#ex-rt12-sw-rt22 difficulty=1 objective="Reduce the pigeonhole principle to Ramsey's theorem for pairs uniformly, coding a coloring of points as a coloring of pairs." lessons="computable-reducibility"}
Show that $\mathsf{RT}^1_2 \leq_{sW} \mathsf{RT}^2_2$, hence $\mathsf{RT}^1_2 \leq_{sc} \mathsf{RT}^2_2$.

:::solution
Given $f : \nat \to 2$, let $\Phi^f$ be the coloring $g(\{ x, y \}) = f(x)$ for $x < y$. Let $H$ be an infinite homogeneous set for $g$, with color $c$. For every $x \in H$, there is $y \in H$ with $y > x$, since $H$ is infinite, and $f(x) = g(\{ x, y \}) = c$. So $H$ is homogeneous for $f$, and $\Psi^H = H$ works, without access to $f$. A strong Weihrauch reduction is a strong computable reduction.
:::
::::

::::exercise{#ex-rt1-unbounded-w difficulty=1 objective="See how the presentation of the number of colors affects Weihrauch reducibility but not computable reducibility."}
Show that $\mathsf{RT}^1_k \leq_{sW} \mathsf{RT}^1_{<\infty}$ and $\mathsf{RT}^1_{<\infty} \leq_c \mathsf{RT}^1_k$ for every $k \geq 1$. Admitting that $\mathsf{RT}^1_{k+1} \not\leq_W \mathsf{RT}^1_k$, show that $\mathsf{RT}^1_{<\infty} \not\leq_W \mathsf{RT}^1_k$ for every $k$.

:::solution
Given $f : \nat \to k$, the forward functional outputs the pair $(k, f)$, and the backward functional is the identity: the solutions to both instances are the infinite homogeneous sets for $f$.

$\mathsf{RT}^1_{<\infty}$ admits computable solutions, so $\mathsf{RT}^1_{<\infty} \leq_c \mathsf{Id}$ (:ref{#prop-c-omega}). $\mathsf{RT}^1_k$ has a computable instance, the constant coloring $0$, so $\mathsf{Id} \leq_c \mathsf{RT}^1_k$, and $\mathsf{RT}^1_{<\infty} \leq_c \mathsf{RT}^1_k$ by transitivity (:ref{#ex-c-transitive}).

If $\mathsf{RT}^1_{<\infty} \leq_W \mathsf{RT}^1_k$, then $\mathsf{RT}^1_{k+1} \leq_{sW} \mathsf{RT}^1_{<\infty} \leq_W \mathsf{RT}^1_k$, and $\mathsf{RT}^1_{k+1} \leq_W \mathsf{RT}^1_k$ by :ref{#ex-w-transitive}, a contradiction.
:::
::::

::::exercise{#ex-bound-not-uniform difficulty=1 objective="Apply a continuity argument to the problem of finding a bound for a function with finite range."}
Let $\mathsf B$ be the problem whose instances are the functions $f : \nat \to \nat$ with finite range, the solutions to $f$ being the numbers $k$ with $f(x) < k$ for every $x$. Show that $\mathsf B$ admits computable solutions, but not uniformly.

:::solution
Every $k$ above the maximum of the finite range is a solution, and a number is computable. Suppose that $\Phi^f$ codes a solution for every instance $f$. Let $f_0$ be the constant function $0$, $k_0$ the solution coded by $\Phi^{f_0}$, and $u$ the use of the computation of the code of $k_0$ from $f_0$ (finitely many bits of the output suffice to determine it). Let $f_1(x) = 0$ for $x < u$ and $f_1(x) = k_0$ for $x \geq u$. It has finite range, and agrees with $f_0$ below $u$, so $\Phi^{f_1}$ codes $k_0$. But $f_1(u) = k_0$, so $k_0$ is not a solution to $f_1$.

Adapted from Dzhafarov and Mummert, Exercise 3.9.2.
:::
::::

::::exercise[Two questions to LPO]{#ex-lpo-product difficulty=2 objective="Show by a continuity argument that two parallel questions to LPO cannot be answered by one."}
Show that $\mathsf{LPO} \times \mathsf{LPO} \not\leq_W \mathsf{LPO}$, where the product has as instances the pairs $p_0 \oplus p_1$ of sequences and as solution the pair of the solutions to $p_0$ and $p_1$. Compare with $\mathsf J \times \mathsf J \leq_W \mathsf J$.

:::solution
Suppose $\Phi$ and $\Psi$ witness the reduction. For an instance $x$, let $b(x)$ be the solution to the instance $\Phi^x$ of $\mathsf{LPO}$; $\Psi^{x \oplus b(x)}$ must code the pair of solutions to $x$, and only finitely many bits of it determine this pair. Let $z = 0^\infty \oplus 0^\infty$, with solution $(0, 0)$, and $u$ a number such that the computation of these bits by $\Psi^{z \oplus b(z)}$ reads only $z \uh u$ and $b(z)$. For $m \in \nat$, let $e_m$ be the sequence with a single $1$, at position $m$.

Case $b(z) = 1$. Then $\Phi^z(n) = 1$ for some $n$; let $v$ be such that this computation reads only $z \uh v$, and $m \geq \max(u, v)$. The instance $x = e_m \oplus 0^\infty$ agrees with $z$ below $2m \geq \max(u, v)$, so $\Phi^x(n) = 1$, $b(x) = 1$, and $\Psi^{x \oplus 1}$ codes $(0, 0)$, as $\Psi^{z \oplus 1}$ does. But the solution to $x$ is $(1, 0)$.

Case $b(z) = 0$. Let $m \geq u$ and $x_1 = e_m \oplus 0^\infty$, with solution $(1, 0)$. If $b(x_1) = 0$, then $\Psi^{x_1 \oplus 0}$ codes $(0, 0)$, as $\Psi^{z \oplus 0}$ does, since $x_1$ agrees with $z$ below $2m \geq u$: a contradiction. So $b(x_1) = 1$: $\Phi^{x_1}(n) = 1$ for some $n$, by a computation reading only $x_1 \uh v$, and $\Psi^{x_1 \oplus 1}$ codes $(1, 0)$, by computations reading only $x_1 \uh w$ and the bit $1$. Let $m' \geq \max(m + 1, v, w)$ and $x_2 = e_m \oplus e_{m'}$, with solution $(1, 1)$. It agrees with $x_1$ below $2m' + 1 > \max(v, w)$, so $b(x_2) = 1$, and $\Psi^{x_2 \oplus 1}$ codes $(1, 0)$: a contradiction.

For the jump, $(X_0 \oplus X_1)'$ computes $X_0' \oplus X_1'$ uniformly. The difference is that a solution to $\mathsf{LPO}$ carries one bit, and the argument shows that one bit, read after a finite part of the instance, cannot answer two independent questions.
:::
::::

::::exercise[Joins and meets]{#ex-w-join-meet difficulty=1 objective="Construct the least upper bound and the greatest lower bound of two problems under Weihrauch reducibility."}
For problems $\mathsf P$ and $\mathsf Q$, let $\mathsf P \sqcup \mathsf Q$ have as instances the pairs $(0, X)$ with $X$ an instance of $\mathsf P$ and $(1, V)$ with $V$ an instance of $\mathsf Q$, the solutions being the solutions to $X$, respectively $V$. Let $\mathsf P \sqcap \mathsf Q$ have as instances the sets $X \oplus V$ with $X$ an instance of $\mathsf P$ and $V$ an instance of $\mathsf Q$, the solutions being the pairs $(0, Y)$ with $Y$ a solution to $X$ and $(1, W)$ with $W$ a solution to $V$. Show that $\mathsf P \sqcup \mathsf Q$ is a least upper bound of $\mathsf P$ and $\mathsf Q$ for $\leq_W$, and $\mathsf P \sqcap \mathsf Q$ a greatest lower bound.

:::solution
($\sqcup$) $\mathsf P \leq_W \mathsf P \sqcup \mathsf Q$ via $X \mapsto (0, X)$ and the identity on solutions; similarly for $\mathsf Q$. If $\mathsf P \leq_W \mathsf R$ via $\Phi_0, \Psi_0$ and $\mathsf Q \leq_W \mathsf R$ via $\Phi_1, \Psi_1$, let $\Phi^{(i, X)} = \Phi_i^X$ and $\Psi^{(i, X) \oplus \widetilde Y} = \Psi_i^{X \oplus \widetilde Y}$; the functionals read $i$ from the instance. Then $\mathsf P \sqcup \mathsf Q \leq_W \mathsf R$.

($\sqcap$) $\mathsf P \sqcap \mathsf Q \leq_W \mathsf P$ via $X \oplus V \mapsto X$ and $Y \mapsto (0, Y)$; similarly for $\mathsf Q$. If $\mathsf R \leq_W \mathsf P$ via $\Phi_0, \Psi_0$ and $\mathsf R \leq_W \mathsf Q$ via $\Phi_1, \Psi_1$, let $\Phi^Z = \Phi_0^Z \oplus \Phi_1^Z$, an instance of $\mathsf P \sqcap \mathsf Q$, and $\Psi^{Z \oplus (i, Y)} = \Psi_i^{Z \oplus Y}$. A solution $(i, Y)$ is a solution $Y$ to $\Phi_i^Z$, so the output is a solution to $Z$. Then $\mathsf R \leq_W \mathsf P \sqcap \mathsf Q$.

Adapted from Dzhafarov and Mummert, Exercise 4.8.11, which also treats computable reducibility; the operations are due to Pauly and to Brattka and Gherardi.
:::
::::
:::::
