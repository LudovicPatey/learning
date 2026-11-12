---
title: The halting problem
summary: Undecidability of the halting problem; many-one reductions; undecidability of totality and of halting on a fixed input.
duration: 40
prerequisites: [universal-program-smn, countability/diagonalization-and-computation]
---

This lesson proves that the halting problem is not computable, and introduces the main tool for transferring undecidability from one problem to another: many-one reductions. With them, the undecidability of the halting problem propagates to many other questions about programs — halting on a fixed input, totality, emptiness of the domain — and, outside computability theory, to problems of number theory, group theory and logic.

## The halting set

:::definition{#def-halting}
The **halting set**, or **halting problem**, is
$$
\emptyset' = \{ e \in \nat : \Phi_e(e)\converge \}.
$$
The set $H = \{ \langle e, x \rangle : \Phi_e(x)\converge \}$ is the **general halting set**.
:::

The notation $\emptyset'$, read "zero jump", comes from the theory of the Turing jump: $\emptyset'$ is the jump of the empty set. The restriction to the diagonal $x = e$ makes the diagonal argument direct; the general halting set has the same degree of difficulty, as shown below.

:::theorem{#thm-halting}
The set $\emptyset'$ is not computable.
:::

:::proof{of=thm-halting}
Suppose $\emptyset'$ is computable. Consider the following algorithm $D$: on input $x$, decide whether $x \in \emptyset'$; if so, enter an infinite loop; otherwise, halt with output $0$. By :ref{#prop-computable-closure}, $D$ computes a partial computable function, so it has an index $d$, and for every $x$,
$$
\Phi_d(x)\converge \iff x \notin \emptyset' \iff \Phi_x(x)\diverge.
$$
For $x = d$, this gives $\Phi_d(d)\converge \iff \Phi_d(d)\diverge$, a contradiction.
:::

This is Cantor's diagonal argument applied to the table whose rows are the partial functions $\Phi_e$: the algorithm $D$ differs from row $x$ at column $x$, by converging where it diverges and diverging where it converges.

:::figure[Row $e$ records, for each input $x$, whether $\Phi_e(x)$ converges ($\downarrow$) or diverges ($\uparrow$). The row $D$ reverses the diagonal, so it differs from every row. Since $D$ would be computable if $\emptyset'$ were, it would be a row $d$, and its diagonal entry would differ from itself.]
<svg class="fig" viewBox="0 0 440 330" width="440" role="img" aria-label="A table whose row e lists whether Phi_e converges or diverges on each input; the diagonal is marked; the row D reverses each diagonal entry"><text x="199.0" y="12" text-anchor="middle" class="label">input x</text><text x="97.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">0</text><text x="131.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">1</text><text x="165.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">2</text><text x="199.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">3</text><text x="233.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">4</text><text x="267.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">5</text><text x="301.0" y="26" text-anchor="middle" class="mrm muted" font-size="12">6</text><text x="40" y="56" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="80" y="34" width="34" height="34" class="cell head-cell"/><text x="97.0" y="57" text-anchor="middle" class="mrm" font-size="17">↓</text><rect x="114" y="34" width="34" height="34" class="cell"/><text x="131.0" y="57" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="148" y="34" width="34" height="34" class="cell"/><text x="165.0" y="57" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="182" y="34" width="34" height="34" class="cell"/><text x="199.0" y="57" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="216" y="34" width="34" height="34" class="cell"/><text x="233.0" y="57" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="250" y="34" width="34" height="34" class="cell"/><text x="267.0" y="57" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="284" y="34" width="34" height="34" class="cell"/><text x="301.0" y="57" text-anchor="middle" class="mrm muted" font-size="17">↑</text><text x="330" y="56" class="mrm muted" font-size="15">⋯</text><text x="40" y="90" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="80" y="68" width="34" height="34" class="cell"/><text x="97.0" y="91" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="114" y="68" width="34" height="34" class="cell head-cell"/><text x="131.0" y="91" text-anchor="middle" class="mrm" font-size="17">↑</text><rect x="148" y="68" width="34" height="34" class="cell"/><text x="165.0" y="91" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="182" y="68" width="34" height="34" class="cell"/><text x="199.0" y="91" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="216" y="68" width="34" height="34" class="cell"/><text x="233.0" y="91" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="250" y="68" width="34" height="34" class="cell"/><text x="267.0" y="91" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="284" y="68" width="34" height="34" class="cell"/><text x="301.0" y="91" text-anchor="middle" class="mrm muted" font-size="17">↓</text><text x="330" y="90" class="mrm muted" font-size="15">⋯</text><text x="40" y="124" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="80" y="102" width="34" height="34" class="cell"/><text x="97.0" y="125" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="114" y="102" width="34" height="34" class="cell"/><text x="131.0" y="125" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="148" y="102" width="34" height="34" class="cell head-cell"/><text x="165.0" y="125" text-anchor="middle" class="mrm" font-size="17">↓</text><rect x="182" y="102" width="34" height="34" class="cell"/><text x="199.0" y="125" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="216" y="102" width="34" height="34" class="cell"/><text x="233.0" y="125" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="250" y="102" width="34" height="34" class="cell"/><text x="267.0" y="125" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="284" y="102" width="34" height="34" class="cell"/><text x="301.0" y="125" text-anchor="middle" class="mrm muted" font-size="17">↑</text><text x="330" y="124" class="mrm muted" font-size="15">⋯</text><text x="40" y="158" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="80" y="136" width="34" height="34" class="cell"/><text x="97.0" y="159" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="114" y="136" width="34" height="34" class="cell"/><text x="131.0" y="159" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="148" y="136" width="34" height="34" class="cell"/><text x="165.0" y="159" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="182" y="136" width="34" height="34" class="cell head-cell"/><text x="199.0" y="159" text-anchor="middle" class="mrm" font-size="17">↑</text><rect x="216" y="136" width="34" height="34" class="cell"/><text x="233.0" y="159" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="250" y="136" width="34" height="34" class="cell"/><text x="267.0" y="159" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="284" y="136" width="34" height="34" class="cell"/><text x="301.0" y="159" text-anchor="middle" class="mrm muted" font-size="17">↓</text><text x="330" y="158" class="mrm muted" font-size="15">⋯</text><text x="40" y="192" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">4</tspan></text><rect x="80" y="170" width="34" height="34" class="cell"/><text x="97.0" y="193" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="114" y="170" width="34" height="34" class="cell"/><text x="131.0" y="193" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="148" y="170" width="34" height="34" class="cell"/><text x="165.0" y="193" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="182" y="170" width="34" height="34" class="cell"/><text x="199.0" y="193" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="216" y="170" width="34" height="34" class="cell head-cell"/><text x="233.0" y="193" text-anchor="middle" class="mrm" font-size="17">↓</text><rect x="250" y="170" width="34" height="34" class="cell"/><text x="267.0" y="193" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="284" y="170" width="34" height="34" class="cell"/><text x="301.0" y="193" text-anchor="middle" class="mrm muted" font-size="17">↑</text><text x="330" y="192" class="mrm muted" font-size="15">⋯</text><text x="40" y="226" text-anchor="middle" class="mrm" font-size="16">Φ<tspan class="mrm" font-size="10" dy="4">5</tspan></text><rect x="80" y="204" width="34" height="34" class="cell"/><text x="97.0" y="227" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="114" y="204" width="34" height="34" class="cell"/><text x="131.0" y="227" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="148" y="204" width="34" height="34" class="cell"/><text x="165.0" y="227" text-anchor="middle" class="mrm muted" font-size="17">↑</text><rect x="182" y="204" width="34" height="34" class="cell"/><text x="199.0" y="227" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="216" y="204" width="34" height="34" class="cell"/><text x="233.0" y="227" text-anchor="middle" class="mrm muted" font-size="17">↓</text><rect x="250" y="204" width="34" height="34" class="cell head-cell"/><text x="267.0" y="227" text-anchor="middle" class="mrm" font-size="17">↑</text><rect x="284" y="204" width="34" height="34" class="cell"/><text x="301.0" y="227" text-anchor="middle" class="mrm muted" font-size="17">↓</text><text x="330" y="226" class="mrm muted" font-size="15">⋯</text><text x="199.0" y="254" text-anchor="middle" class="mrm muted" font-size="15">⋮</text><line x1="80" y1="264" x2="318" y2="264" class="axis"/><text x="40" y="294" text-anchor="middle" class="math" font-size="16">D</text><rect x="80" y="272" width="34" height="34" class="cell head-cell"/><text x="97.0" y="295" text-anchor="middle" class="mrm" font-size="17" font-weight="600">↑</text><rect x="114" y="272" width="34" height="34" class="cell head-cell"/><text x="131.0" y="295" text-anchor="middle" class="mrm" font-size="17" font-weight="600">↓</text><rect x="148" y="272" width="34" height="34" class="cell head-cell"/><text x="165.0" y="295" text-anchor="middle" class="mrm" font-size="17" font-weight="600">↑</text><rect x="182" y="272" width="34" height="34" class="cell head-cell"/><text x="199.0" y="295" text-anchor="middle" class="mrm" font-size="17" font-weight="600">↓</text><rect x="216" y="272" width="34" height="34" class="cell head-cell"/><text x="233.0" y="295" text-anchor="middle" class="mrm" font-size="17" font-weight="600">↑</text><rect x="250" y="272" width="34" height="34" class="cell head-cell"/><text x="267.0" y="295" text-anchor="middle" class="mrm" font-size="17" font-weight="600">↓</text><rect x="284" y="272" width="34" height="34" class="cell"/><text x="301.0" y="295" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="330" y="288" class="label">D(x)↓ if and only if</text><text x="330" y="304" class="label">Φₓ(x)↑</text></svg>
:::

The technique is **diagonalization**, introduced in the course on countability (:ref{#thm-cantor-diagonal}). Its effective form requires the diagonal row to be computable from the table, here through the decision procedure for $\emptyset'$ that the proof assumes. The same argument is presented in the course on countability in a slightly different form, through partial functions without total extensions (:ref{#cor-halting-diagonal}).

:::quiz[the proof of the theorem]
Where is the hypothesis "$\emptyset'$ is computable" used?

- [x] To make the test "$x \in \emptyset'$" in $D$ always terminate, so that $D$ halts whenever $\Phi_x(x)\diverge$.

  If the test could diverge, $D$ would diverge on such $x$ as well, and the equivalence $\Phi_d(x)\converge \iff \Phi_x(x)\diverge$ would fail.
- [ ] To show that $D$ has an index.

  Every partial computable function has an index. The issue is whether $D$ is partial computable with the required behavior.
- [ ] It is not used.

  It is used: without it, the test in $D$ could diverge, and $D$ would not halt on the inputs $x$ with $\Phi_x(x)\diverge$.

---

Why is the equivalence $\Phi_d(x)\converge \iff \Phi_x(x)\diverge$ applied with $x = d$?

- [x] So that the two sides concern the same computation, $\Phi_d(d)$: the row $d$ disagrees with the diagonal at its own column.
- [ ] Because $d$ is the least index of $D$.

  Any index of $D$ works.
- [ ] Any $x$ would give a contradiction.

  For $x \neq d$ the equivalence relates two different computations and is consistent.

---

Which step corresponds to "flipping the diagonal bit" in Cantor's argument?

- [x] $D$ loops on $x$ exactly when $\Phi_x(x)$ halts, and halts exactly when it loops.
- [ ] Deciding whether $x \in \emptyset'$.

  This only reads the diagonal entry.
- [ ] Choosing an index $d$ for $D$.

  This corresponds to the step "$Y$ would be one of the rows".
:::

## Many-one reductions

:::definition{#def-many-one}
Let $A, B \subseteq \nat$. A **many-one reduction** of $A$ to $B$ is a total computable function $f$ such that for all $x$,
$$
x \in A \iff f(x) \in B.
$$
We write $A \leq_m B$ if such an $f$ exists, and $A \equiv_m B$ if $A \leq_m B$ and $B \leq_m A$.
:::

The reduction transforms each question "$x \in A$?" into a question "$f(x) \in B$?" with the same answer. When $f$ is moreover injective, one speaks of a **one-one reduction**, written $A \leq_1 B$.

:::figure[A many-one reduction $f$ of $A$ to $B$. Elements of $A$ go into $B$, elements outside $A$ go outside $B$. The function $f$ need be neither injective nor surjective.]
<svg class="fig" viewBox="0 0 470 250" width="470" role="img" aria-label="Two copies of the integers, each split into a set and its complement; the reduction f sends the elements of A into B and the other elements outside B"><defs><marker id="ah-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><rect x="60" y="30" width="110" height="200" rx="6" class="track-outline"/><rect x="60" y="30" width="110" height="90" rx="6" class="soft-fill"/><line x1="60" y1="120" x2="170" y2="120" class="ink-stroke" stroke-width="1.2"/><text x="115.0" y="20" text-anchor="middle" class="math" font-size="16">ℕ</text><text x="74" y="54" class="math" font-size="16">A</text><text x="74" y="218" class="mrm" font-size="15">ℕ ∖ <tspan class="math">A</tspan></text><rect x="300" y="30" width="110" height="200" rx="6" class="track-outline"/><rect x="300" y="30" width="110" height="90" rx="6" class="soft-fill"/><line x1="300" y1="120" x2="410" y2="120" class="ink-stroke" stroke-width="1.2"/><text x="355.0" y="20" text-anchor="middle" class="math" font-size="16">ℕ</text><text x="314" y="54" class="math" font-size="16">B</text><text x="314" y="218" class="mrm" font-size="15">ℕ ∖ <tspan class="math">B</tspan></text><line x1="121.0" y1="62.2" x2="347.0" y2="69.7" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-red)"/><line x1="101.0" y1="99.3" x2="347.1" y2="70.9" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-red)"/><line x1="136.0" y1="140.5" x2="362.0" y2="159.3" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-red)"/><line x1="106.0" y1="178.2" x2="332.0" y2="184.8" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-red)"/><line x1="140.9" y1="194.1" x2="362.1" y2="161.2" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-red)"/><circle cx="115" cy="62" r="4.5" class="ink-fill"/><circle cx="95" cy="100" r="4.5" class="ink-fill"/><circle cx="130" cy="140" r="4.5" class="ink-fill"/><circle cx="100" cy="178" r="4.5" class="ink-fill"/><circle cx="135" cy="195" r="4.5" class="ink-fill"/><circle cx="340" cy="185" r="4.5" class="ink-fill"/><circle cx="355" cy="70" r="4.5" class="ink-fill"/><circle cx="370" cy="160" r="4.5" class="ink-fill"/><circle cx="385" cy="100" r="4.5" class="muted-fill"/><circle cx="330" cy="104" r="4.5" class="muted-fill"/><circle cx="395" cy="205" r="4.5" class="muted-fill"/><text x="235" y="118" text-anchor="middle" class="math" font-size="16">f</text><text x="300" y="248" class="label">grey points: not values of f</text></svg>
:::

:::example{#ex-many-one}
Let $A \subseteq \nat$ and $2A = \{ 2x : x \in A \}$. The function $x \mapsto 2x$ reduces $A$ to $2A$. Conversely, if $A \neq \nat$, fix $b \notin A$; the function $g(y) = y/2$ for $y$ even and $g(y) = b$ for $y$ odd reduces $2A$ to $A$, so $A \equiv_m 2A$. The hypothesis $A \neq \nat$ is needed: the set $2\nat$ of even numbers does not reduce to $\nat$, since every value of a reduction to $\nat$ lies in $\nat$, which would force every $y$ to be even. So $\leq_m$ is sensitive to the trivial sets $\emptyset$ and $\nat$; the first exercise shows that this is the only anomaly among computable sets.
:::

:::proposition{#prop-many-one}
1. The relation $\leq_m$ is reflexive and transitive.
2. $A \leq_m B$ if and only if $\nat \setminus A \leq_m \nat \setminus B$.
3. If $A \leq_m B$ and $B$ is computable, then $A$ is computable. Equivalently, if $A \leq_m B$ and $A$ is not computable, then $B$ is not computable.
:::

:::proof{of=prop-many-one}
1. The identity reduces $A$ to $A$. If $f$ reduces $A$ to $B$ and $g$ reduces $B$ to $C$, then $g \circ f$ is total computable and $x \in A \iff f(x) \in B \iff g(f(x)) \in C$.
2. The same $f$ works: $x \notin A \iff f(x) \notin B$.
3. $\chi_A = \chi_B \circ f$ is total computable.
:::

To show that a set $B$ is not computable, it therefore suffices to reduce a non-computable set, typically $\emptyset'$, to $B$. Most reductions from $\emptyset'$ are built with the SMN theorem: from $e$, one computes the index of a program whose behavior depends on whether $\Phi_e(e)$ converges.

:::proposition{#prop-halting-variants}
1. $\emptyset' \equiv_m H$.
2. $\emptyset' \leq_m \{ e : \Phi_e(0)\converge \}$, and $\emptyset' \leq_m \{ e : \mathrm{dom}(\Phi_e) \neq \emptyset \}$.
3. $\emptyset' \leq_m \mathrm{Tot}$ and $\nat \setminus \emptyset' \leq_m \mathrm{Tot}$, where $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$.

In particular, none of these sets is computable.
:::

:::proof{of=prop-halting-variants}
1. $e \mapsto \langle e, e \rangle$ reduces $\emptyset'$ to $H$. Conversely, let $z$ be the function of :ref{#ex-smn-uses}, with $\Phi_{z(e, x)}(y) \simeq \Phi_e(x)$ for all $y$. Then $\langle e, x \rangle \in H \iff \Phi_e(x)\converge \iff \Phi_{z(e, x)}(z(e, x))\converge \iff z(e, x) \in \emptyset'$, so $\langle e, x \rangle \mapsto z(e, x)$ reduces $H$ to $\emptyset'$. (The function $n \mapsto z(\pi_0(n), \pi_1(n))$ is total computable, since the inverses $\pi_0, \pi_1$ of the pairing function are.)
2. With the same $z$, the function $\Phi_{z(e, e)}$ is total if $e \in \emptyset'$ and nowhere defined otherwise. So $e \mapsto z(e, e)$ reduces $\emptyset'$ to both sets, and also to $\mathrm{Tot}$, which proves the first half of item 3.
3. For the second half, let $g$ be total computable, given by :ref{#cor-smn-parameters}, such that
$$
\Phi_{g(e)}(x) \simeq \begin{cases} 0 & \text{if } \Phi_e(e)[x]\diverge,\\ \text{undefined} & \text{if } \Phi_e(e)[x]\converge. \end{cases}
$$
This is a definition by cases with a computable condition (:ref{#prop-stage-properties}). If $e \notin \emptyset'$, then $\Phi_e(e)[x]\diverge$ for every $x$, and $\Phi_{g(e)}$ is total. If $e \in \emptyset'$, then $\Phi_e(e)[x]\converge$ for all large $x$, and $\Phi_{g(e)}$ is not total. So $g$ reduces $\nat \setminus \emptyset'$ to $\mathrm{Tot}$.
:::

The second half of item 3 is stronger than it looks. The lesson on computably enumerable sets shows that $\nat \setminus \emptyset'$ is not computably enumerable, and that sets reducible to a computably enumerable set are computably enumerable. Hence $\mathrm{Tot}$ is not computably enumerable; and by item 2 of :ref{#prop-many-one}, its complement is not either. Totality is strictly harder than halting, a fact made precise by the arithmetic hierarchy.

:::quiz[reductions from the halting set]
In the reduction of $\emptyset'$ to $\{ e : \Phi_e(0)\converge \}$, what does the program $z(e, e)$ do on input $0$?

- [x] It ignores its input and runs $\Phi_e(e)$, so it halts on $0$ if and only if $e \in \emptyset'$.
- [ ] It runs $\Phi_e(0)$.

  That would reduce the wrong set: it relates $\Phi_e(0)$, not $\Phi_e(e)$.
- [ ] It decides whether $e \in \emptyset'$.

  No program does that. The reduction only computes an index; the hard question is transferred to the target set.

---

In the reduction $g$ of $\nat \setminus \emptyset'$ to $\mathrm{Tot}$, why does $\Phi_{g(e)}(x)$ test convergence at stage $x$ instead of running $\Phi_e(e)$ to completion?

- [x] Because the test must be decidable, so that $\Phi_{g(e)}(x)$ converges when $e \notin \emptyset'$; running $\Phi_e(e)$ would diverge exactly in that case.

  The stage test is a bounded simulation, which always terminates.
- [ ] To make $g$ total.

  $g$ is total by the parameter form of SMN, whatever the program it describes.
- [ ] Because $\Phi_e(e)$ converges at stage $x$ for every $x$.

  It converges at all large stages if $e \in \emptyset'$, and at none otherwise.

---

Which statements are correct?

- [x] For each single $e$, some program outputs the correct answer to "$e \in \emptyset'$?".

  One of the two constant programs does. Undecidability concerns a single program answering for all $e$.
- [x] If $A \leq_m B$ and $B$ is computable, then $A$ is computable.
- [ ] If $A \leq_m B$ and $A$ is computable, then $B$ is computable.

  Every computable set reduces to $\emptyset'$, as to any set other than $\emptyset$ and $\nat$ (see the exercises).
:::

## Undecidable problems in mathematics

Reductions from the halting problem show that many natural mathematical problems are undecidable. The following results are admitted; each is proved by coding computations into the problem considered.

- **The Entscheidungsproblem.** The set of (codes of) valid formulas of first-order logic is not computable (Church, Turing, 1936). Since Kalmár reduced the decision problem to formulas whose only non-logical symbol is a single binary relation symbol (1937), it remains undecidable for these formulas.
- **The word problem for groups.** There is a finitely presented group for which the set of words equal to the identity is not computable (Novikov, 1955; Boone, 1959).
- **Hilbert's tenth problem.** The set of polynomial equations with integer coefficients having a solution in integers is not computable (Matiyasevich, 1970, completing work of Davis, Putnam and Robinson). More precisely, every computably enumerable set (in the sense of the next lesson) is Diophantine, and therefore $\emptyset'$ reduces to the solvability of Diophantine equations.

## Exercises

::::exercise{difficulty=1}
Show that if $A$ is computable and $B \neq \emptyset$, $B \neq \nat$, then $A \leq_m B$. What happens if $B = \emptyset$ or $B = \nat$?

:::solution
Fix $b_1 \in B$ and $b_0 \notin B$, and let $f(x) = b_1$ if $x \in A$ and $f(x) = b_0$ otherwise; $f$ is total computable and reduces $A$ to $B$. If $B = \emptyset$, then $A \leq_m B$ forces $A = \emptyset$, since no $f(x)$ lies in $B$; similarly, $A \leq_m \nat$ forces $A = \nat$.
:::
::::

::::exercise{difficulty=1}
Show that $\{ e : \Phi_e(e)\converge = 0 \}$ is not computable.

:::solution
Let $g$ be total computable with $\Phi_{g(e)}(y) \simeq 0$ if $\Phi_e(e)\converge$, and undefined otherwise; it exists by :ref{#cor-smn-parameters}, since the right-hand side is a partial computable function of $(e, y)$. Then $e \in \emptyset' \iff \Phi_{g(e)}(g(e))\converge = 0$, so $g$ reduces $\emptyset'$ to the set.
:::
::::

::::exercise{difficulty=2 #ex-inf-reductions}
Let $\mathrm{Inf} = \{ e : \mathrm{dom}(\Phi_e) \text{ is infinite} \}$. Show that $\emptyset' \leq_m \mathrm{Inf}$ and $\nat \setminus \emptyset' \leq_m \mathrm{Inf}$.

:::solution
The reduction $e \mapsto z(e, e)$ of :ref{#prop-halting-variants} sends $e \in \emptyset'$ to an index of a total function, whose domain is infinite, and $e \notin \emptyset'$ to an index of the nowhere defined function. The reduction $g$ of item 3 sends $e \notin \emptyset'$ to an index of a total function, and $e \in \emptyset'$ to an index of a function whose domain is $\{ x : \Phi_e(e)[x]\diverge \}$, a finite initial segment of $\nat$.
:::
::::

## Notes and references

Turing proved in 1936 that no machine decides whether a given machine is circle-free, and deduced the unsolvability of the Entscheidungsproblem; Church obtained the latter independently with the λ-calculus. Many-one reducibility was introduced by Post in 1944, in the paper that founded the study of computably enumerable sets and their degrees. Soare's textbook treats the halting set, many-one reducibility and the reductions to $\mathrm{Tot}$ in Sections 1.6.2–1.6.3. Davis' survey and Matiyasevich's book on Hilbert's tenth problem, and Lyndon and Schupp's book on combinatorial group theory, present the undecidability results listed above.

- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society (2) 42 (1936), 230–265.
- A. Church, *A note on the Entscheidungsproblem*, Journal of Symbolic Logic 1 (1936), 40–41.
- L. Kalmár, *Zurückführung des Entscheidungsproblems auf den Fall von Formeln mit einer einzigen, binären, Funktionsvariablen*, Compositio Mathematica 4 (1937), 137–144.
- E. L. Post, *Recursively enumerable sets of positive integers and their decision problems*, Bulletin of the American Mathematical Society 50 (1944), 284–316.
- M. Davis, *Hilbert's tenth problem is unsolvable*, American Mathematical Monthly 80 (1973), 233–269.
- Y. V. Matiyasevich, *Hilbert's Tenth Problem*, MIT Press, 1993.
- R. C. Lyndon and P. E. Schupp, *Combinatorial Group Theory*, Springer, 1977.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Section 1.6.
- B. Monin and L. Patey, *Computability theory*, chapter *Foundations of computability*, section *Computably enumerable sets*.
