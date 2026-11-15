---
title: Limit computability
summary: Shoenfield's limit lemma; Δ⁰₂ approximations, their moduli and computation functions; domination properties of the sets computable in ∅′.
duration: 45
prerequisites: [turing-jump]
---

A set computable in $\emptyset'$ can be computed by an algorithm that is allowed to **change its mind** finitely many times on each input: it produces guesses $A_0(x), A_1(x), A_2(x), \dots$ which are eventually correct, but without ever knowing that the last change has occurred. This is Shoenfield's limit lemma. It gives the sets below $\obf'$ a concrete description by computable approximations, and it is the basis of most constructions of sets below $\emptyset'$, notably by the priority method. This lesson proves the lemma and studies how fast an approximation settles.

## Limit computable sets

:::definition{#def-delta2-approximation}
A **$\Delta^0_2$ approximation** of a set $A$ is a uniformly computable sequence of sets $A_0, A_1, A_2, \dots$ such that for every $x$, $A_s(x) = A(x)$ for all sufficiently large $s$. A set is **limit computable** if it has a $\Delta^0_2$ approximation.
:::

Equivalently, $A$ is limit computable if there is a total computable function $g : \nat^2 \to \{0, 1\}$ with $A(x) = \lim_s g(x, s)$ for every $x$, where the limit of a sequence of integers is the value it eventually takes. A c.e. approximation (:ref{#def-ce-approx}) is a $\Delta^0_2$ approximation in which elements may enter but never leave; so c.e. sets are limit computable. In a general $\Delta^0_2$ approximation, $A_s(x)$ may change any finite number of times.

:::example{#ex-delta2-approximations}
1. The complement of $\emptyset'$ has the approximation $\nat \setminus \emptyset'_s$, where $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$: elements are present at the start and may leave once, but never come back. So co-c.e. sets are limit computable, although they need not be c.e.
2. Approximations are not unique. If $(A_s)$ is a $\Delta^0_2$ approximation of $A$ and $g$ is computable, increasing and unbounded, then $(A_{g(s)})$ is another one; and a computable set $A$ has, besides the constant approximation $A_s = A$, approximations that change their minds, such as $A_s = A \symdiff \{ x : x \geq s \}$, in which each bit is wrong until stage $x + 1$.
3. The set $\mathrm{Tot}$ has no $\Delta^0_2$ approximation, since it is not computable in $\emptyset'$ (lesson on the jump).
:::

:::figure[A $\Delta^0_2$ approximation. Each column $x$ changes finitely many times; the shaded cells are the changes, and the bits shown in full have reached their final value.]
<svg class="fig" viewBox="0 0 420 330" width="420" role="img" aria-label="A table of approximations A_s; each column eventually stops changing"><text x="105.0" y="28" text-anchor="middle" class="math muted" font-size="13">0</text><text x="135.0" y="28" text-anchor="middle" class="math muted" font-size="13">1</text><text x="165.0" y="28" text-anchor="middle" class="math muted" font-size="13">2</text><text x="195.0" y="28" text-anchor="middle" class="math muted" font-size="13">3</text><text x="225.0" y="28" text-anchor="middle" class="math muted" font-size="13">4</text><text x="255.0" y="28" text-anchor="middle" class="math muted" font-size="13">5</text><text x="285.0" y="28" text-anchor="middle" class="math muted" font-size="13">6</text><text x="40" y="28" class="label">stage</text><text x="60" y="60" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="90" y="40" width="30" height="30" class="cell"/><text x="105.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="120" y="40" width="30" height="30" class="cell"/><text x="135.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="150" y="40" width="30" height="30" class="cell"/><text x="165.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="180" y="40" width="30" height="30" class="cell"/><text x="195.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="210" y="40" width="30" height="30" class="cell"/><text x="225.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="240" y="40" width="30" height="30" class="cell"/><text x="255.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="270" y="40" width="30" height="30" class="cell"/><text x="285.0" y="60" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="60" y="90" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="90" y="70" width="30" height="30" class="cell"/><text x="105.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="120" y="70" width="30" height="30" class="cell head-cell"/><text x="135.0" y="90" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="70" width="30" height="30" class="cell"/><text x="165.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="180" y="70" width="30" height="30" class="cell"/><text x="195.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="210" y="70" width="30" height="30" class="cell head-cell"/><text x="225.0" y="90" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="70" width="30" height="30" class="cell"/><text x="255.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="270" y="70" width="30" height="30" class="cell"/><text x="285.0" y="90" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="60" y="120" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="90" y="100" width="30" height="30" class="cell"/><text x="105.0" y="120" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="120" y="100" width="30" height="30" class="cell"/><text x="135.0" y="120" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="100" width="30" height="30" class="cell"/><text x="165.0" y="120" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="180" y="100" width="30" height="30" class="cell"/><text x="195.0" y="120" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="210" y="100" width="30" height="30" class="cell"/><text x="225.0" y="120" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="100" width="30" height="30" class="cell head-cell"/><text x="255.0" y="120" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="270" y="100" width="30" height="30" class="cell"/><text x="285.0" y="120" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="60" y="150" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="90" y="130" width="30" height="30" class="cell head-cell"/><text x="105.0" y="150" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="120" y="130" width="30" height="30" class="cell"/><text x="135.0" y="150" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="130" width="30" height="30" class="cell"/><text x="165.0" y="150" text-anchor="middle" class="mrm muted" font-size="15">0</text><rect x="180" y="130" width="30" height="30" class="cell"/><text x="195.0" y="150" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="210" y="130" width="30" height="30" class="cell"/><text x="225.0" y="150" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="130" width="30" height="30" class="cell"/><text x="255.0" y="150" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="270" y="130" width="30" height="30" class="cell"/><text x="285.0" y="150" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="60" y="180" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">4</tspan></text><rect x="90" y="160" width="30" height="30" class="cell"/><text x="105.0" y="180" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="120" y="160" width="30" height="30" class="cell"/><text x="135.0" y="180" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="160" width="30" height="30" class="cell head-cell"/><text x="165.0" y="180" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="180" y="160" width="30" height="30" class="cell"/><text x="195.0" y="180" text-anchor="middle" class="mrm muted" font-size="15">1</text><rect x="210" y="160" width="30" height="30" class="cell"/><text x="225.0" y="180" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="160" width="30" height="30" class="cell"/><text x="255.0" y="180" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="270" y="160" width="30" height="30" class="cell"/><text x="285.0" y="180" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="60" y="210" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">5</tspan></text><rect x="90" y="190" width="30" height="30" class="cell"/><text x="105.0" y="210" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="120" y="190" width="30" height="30" class="cell"/><text x="135.0" y="210" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="190" width="30" height="30" class="cell"/><text x="165.0" y="210" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="180" y="190" width="30" height="30" class="cell head-cell"/><text x="195.0" y="210" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="210" y="190" width="30" height="30" class="cell"/><text x="225.0" y="210" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="190" width="30" height="30" class="cell"/><text x="255.0" y="210" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="270" y="190" width="30" height="30" class="cell"/><text x="285.0" y="210" text-anchor="middle" class="mrm muted" font-size="15">0</text><text x="60" y="240" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">6</tspan></text><rect x="90" y="220" width="30" height="30" class="cell"/><text x="105.0" y="240" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="120" y="220" width="30" height="30" class="cell"/><text x="135.0" y="240" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="220" width="30" height="30" class="cell"/><text x="165.0" y="240" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="180" y="220" width="30" height="30" class="cell"/><text x="195.0" y="240" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="210" y="220" width="30" height="30" class="cell"/><text x="225.0" y="240" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="220" width="30" height="30" class="cell"/><text x="255.0" y="240" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="270" y="220" width="30" height="30" class="cell head-cell"/><text x="285.0" y="240" text-anchor="middle" class="mrm" font-size="15">1</text><text x="60" y="270" text-anchor="middle" class="math" font-size="15">A<tspan class="mrm" font-size="10" dy="4">7</tspan></text><rect x="90" y="250" width="30" height="30" class="cell"/><text x="105.0" y="270" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="120" y="250" width="30" height="30" class="cell"/><text x="135.0" y="270" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="150" y="250" width="30" height="30" class="cell"/><text x="165.0" y="270" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="180" y="250" width="30" height="30" class="cell"/><text x="195.0" y="270" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="210" y="250" width="30" height="30" class="cell"/><text x="225.0" y="270" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="240" y="250" width="30" height="30" class="cell"/><text x="255.0" y="270" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="270" y="250" width="30" height="30" class="cell"/><text x="285.0" y="270" text-anchor="middle" class="mrm" font-size="15">1</text><text x="195.0" y="296" text-anchor="middle" class="mrm muted" font-size="15">⋮</text><line x1="90" y1="304" x2="300" y2="304" class="axis"/><text x="60" y="328" text-anchor="middle" class="math" font-size="15">A</text><text x="105.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">0</text><text x="135.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><text x="165.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><text x="195.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">0</text><text x="225.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">0</text><text x="255.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><text x="285.0" y="328" text-anchor="middle" class="mrm" font-size="15" font-weight="600">1</text><text x="312" y="100" class="label">shaded: a bit that</text><text x="312" y="116" class="label">changes at this stage</text></svg>
:::

:::theorem[Shoenfield's limit lemma]{#thm-limit-lemma}
A set $A$ is computable in $\emptyset'$ if and only if it is limit computable. More generally, for every $X$, a set is computable in $X'$ if and only if it has an $X$-computable $\Delta^0_2$ approximation.
:::

:::proof{of=thm-limit-lemma}
We prove the unrelativized statement; the proof relativizes. Fix a c.e. approximation $(\emptyset'_s)$ of $\emptyset'$, for instance $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$.

($\Rightarrow$) Let $A = \Phi^{\emptyset'}_e$. Define $A_s(x) = \Phi^{\emptyset'_s}_e(x)[s]$ if this computation converges with a value in $\{0, 1\}$, and $A_s(x) = 0$ otherwise. The sequence $(A_s)$ is uniformly computable, by :ref{#prop-oracle-stages}. Fix $x$, and let $u$ be the use of the computation $\Phi^{\emptyset'}_e(x)$ and $t$ a stage at which it converges. Since only finitely many elements below $u$ enter $\emptyset'$, there is $s_0$ with $\emptyset'_s \uh u = \emptyset' \uh u$ for all $s \geq s_0$. For $s \geq \max(s_0, t)$, the computation with oracle $\emptyset'_s$ agrees with the computation with oracle $\emptyset'$ on all the cells it reads, so by monotonicity and the use principle $\Phi^{\emptyset'_s}_e(x)[s]\converge = A(x)$, and $A_s(x) = A(x)$.

($\Leftarrow$) Let $(A_s)$ be a $\Delta^0_2$ approximation of $A$. The relation
$$
C(x, y) \iff \exists s \geq y\ \ A_s(x) \neq A_y(x)
$$
is c.e., hence computable in $\emptyset'$ (:ref{#prop-ce-below-jump}). To compute $A(x)$ with oracle $\emptyset'$, search for the least $y$ with $\neg C(x, y)$, that is, such that the approximation of $x$ does not change after stage $y$, and output $A_y(x)$. Such a $y$ exists since the approximation of $x$ eventually stabilizes, and then $A_y(x) = \lim_s A_s(x) = A(x)$.
:::

The two directions use $\emptyset'$ differently. In the first, the oracle $\emptyset'$ is replaced by its approximations, and the use principle guarantees that the computation eventually sees a correct prefix of the oracle. In the second, the oracle is asked a single question for each $y$: "will $x$ change again after stage $y$?", a c.e. question.

:::quiz[the limit lemma]
In the direction ($\Rightarrow$), why does $A_s(x)$ eventually stabilize, although $\emptyset'_s$ never equals $\emptyset'$ at any finite stage?

- [x] The computation $\Phi^{\emptyset'}_e(x)$ only reads the oracle below its use $u$, and $\emptyset'_s \uh u$ is eventually correct.

  This is the use principle, combined with the fact that a c.e. approximation of a finite segment stabilizes.
- [ ] Because $\emptyset'_s$ is increasing.

  Monotonicity of the approximation helps to stabilize $\emptyset'_s \uh u$, but the key point is that only a finite part of the oracle matters.
- [ ] Because $A$ is c.e.

  $A$ is only assumed computable in $\emptyset'$.

---

In the direction ($\Leftarrow$), what is asked of the oracle?

- [x] For each $y$, whether the approximation of $x$ changes after stage $y$: a c.e. question, which $\emptyset'$ answers.
- [ ] Whether $x \in A$.

  $\emptyset'$ does not know $A$ directly; it only answers c.e. questions.
- [ ] The final value of the approximation.

  The final value is read from the approximation, once a stage without later changes is found.
:::

:::corollary{#cor-limit-lemma}
1. If $Y$ is $X$-c.e., then $Y \leq_T X'$.
2. The relation "is c.e. relative to" is not transitive: $\emptyset''$ is $\emptyset'$-c.e., $\emptyset'$ is c.e., and $\emptyset''$ is not c.e.
:::

:::proof{of=cor-limit-lemma}
1. An $X$-c.e. approximation of $Y$ is an $X$-computable $\Delta^0_2$ approximation; apply the relativized limit lemma.
2. If $\emptyset''$ were c.e., it would be computable in $\emptyset'$ by item 1, contradicting $\emptyset' <_T \emptyset''$.
:::

::::exercise{#ex-dce-limit difficulty=1 objective="Approximate a difference of c.e. sets with at most two mind changes."}
A set $A$ is **d.c.e.** if $A = B \setminus C$ for c.e. sets $B$ and $C$. Show that every d.c.e. set has a $\Delta^0_2$ approximation in which each $x$ changes at most twice, and is therefore computable in $\emptyset'$.

:::solution
Let $(B_s)$ and $(C_s)$ be c.e. approximations, and $A_s = B_s \setminus C_s$. The value $A_s(x)$ starts at $0$, may become $1$ when $x$ enters $B$, and may become $0$ again when $x$ enters $C$; once $x \in C_s$ it stays $0$. So it changes at most twice, and converges to $(B \setminus C)(x)$. Apply :ref{#thm-limit-lemma}.
:::
::::

::::exercise{#ex-bounded-changes-use difficulty=2 objective="Turn an approximation with computably bounded mind changes into a computation from $\emptyset'$ with computably bounded use."}
Let $(A_s)$ be a $\Delta^0_2$ approximation of $A$ such that, for every $x$, the number of $s$ with $A_{s+1}(x) \neq A_s(x)$ is at most $h(x)$, for a computable function $h$. Show that there are an index $e$ and a computable function $b$ such that $\Phi^{\emptyset'}_e = A$ and $\use^{\emptyset'}_e(x) \leq b(x)$ for every $x$.

:::solution
For each $x$ and $k$, let $q(x, k)$ be an index, computable from $(x, k)$, of the machine which halts on its own index if and only if the approximation of $x$ changes at least $k$ times; then $q(x, k) \in \emptyset'$ if and only if $x$ changes at least $k$ times. To compute $A(x)$, query $\emptyset'$ at the positions $q(x, 1), \dots, q(x, h(x))$, let $k$ be the number of changes found, and run the approximation until $k$ changes of $x$ have been observed; the value reached is $A(x)$. Only the positions $q(x, k)$, $k \leq h(x)$, are queried, so the use is bounded by $b(x) = 1 + \max_{k \leq h(x)} q(x, k)$, up to the cells the oracle head crosses to reach them, which are below this bound.
:::
::::

## Moduli and computation functions

A $\Delta^0_2$ approximation does not tell when it has settled. How long one must wait is measured by the following functions.

:::definition{#def-modulus}
Let $(A_s)$ be a $\Delta^0_2$ approximation of $A$.

1. Its **modulus** is the function $m(x) = $ the least $s$ such that $A_t \uh x = A_s \uh x$ for every $t \geq s$.
2. Its **computation function** is $c(x) = $ the least $s \geq x$ such that $A_s \uh x = A \uh x$.
:::

Both are total, since each of the finitely many bits below $x$ eventually settles. Clearly $c(x) \leq \max(x, m(x))$. The computation function may be much smaller than the modulus: $A_s \uh x$ may be correct at some stage and change later. A function $f$ **dominates** $g$ if $f(x) \geq g(x)$ for every $x$.

:::example{#ex-modulus-computation}
Let $A = \emptyset$ and $A_s = \{ n \}$ if $s = 2^n$ for some $n$, and $A_s = \emptyset$ otherwise. Each bit $n$ changes twice, at stages $2^n$ and $2^n + 1$, so this is a $\Delta^0_2$ approximation of $\emptyset$. Below $x$ the last change happens at stage $2^{x-1} + 1$, so $m(x) = 2^{x-1} + 1$ for $x \geq 1$; but $A_s \uh x = \emptyset \uh x$ already for $s = x + 1$ (a stage $s$ has $A_s \uh x \neq \emptyset$ only if $s = 2^n$ with $n < x$, and $x$ and $x + 1$ are not both powers of $2$ when $x \geq 2$; the case $x = 1$ is checked directly), so $c(x) \leq x + 1$. The computation function sees a correct stage early; the modulus waits for the last mistake.
:::

:::proposition{#prop-modulus-computes}
Let $(A_s)$ be a $\Delta^0_2$ approximation of $A$ with modulus $m$.

1. Every function $f$ dominating $m$ computes $A$.
2. If $(A_s)$ is a c.e. approximation, then $m$ is computable in $A$, so that $A \equiv_T m$.
:::

:::proof{of=prop-modulus-computes}
1. $A(x) = A_{f(x+1)}(x)$, since $f(x+1) \geq m(x+1)$ and the bits below $x + 1$ do not change after stage $m(x+1)$.
2. For a c.e. approximation, once $A_s \uh x = A \uh x$, no element below $x$ enters later, since all elements of $A$ below $x$ are already in $A_s$ and elements never leave. So $m(x)$ is the least $s$ with $A_s \uh x = A \uh x$, which is found with oracle $A$ by testing $s = 0, 1, \dots$. Conversely $A \leq_T m$ by item 1.
:::

:::corollary{#cor-complete-domination}
Let $m$ be the modulus of the approximation $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$. A set $X$ computes $\emptyset'$ if and only if $X$ computes a function dominating $m$.
:::

:::proof{of=cor-complete-domination}
If $X \geq_T \emptyset'$, then $X$ computes $m$ by :ref{#prop-modulus-computes}. Conversely, a function dominating $m$ computes $\emptyset'$ by the same proposition, and if $X$ computes it, so does $X$.
:::

So the sets that compute $\emptyset'$ are exactly the sets that compute sufficiently fast-growing functions, as already observed in :ref{#ex-oracle-domination}. For general $\Delta^0_2$ approximations, the modulus is usually not computable in $A$, but the computation function is, and the following result shows that it carries the same information.

:::theorem[Domination of the computation function]{#thm-computation-function}
Let $(A_s)$ be a $\Delta^0_2$ approximation of $A$ with computation function $c$. Then $c \leq_T A$, and every function $f$ dominating $c$ computes $A$.
:::

:::proof{of=thm-computation-function}
To compute $c(x)$ from $A$, read $A \uh x$ and search for the least $s \geq x$ with $A_s \uh x = A \uh x$.

Let $f$ dominate $c$. The idea is that $f$ does not tell which stage is correct, but it tells that the **frame** of stages $[x, f(x)]$ contains a correct stage, $c(x)$. If all the stages of a frame agree on an initial segment, they agree with the correct one there. For each $x$, let $M(x)$ be the largest $y \leq x$ such that $A_t \uh y = A_x \uh y$ for every $t$ with $x \leq t \leq f(x)$. The function $M$ is $f$-computable: it only involves the finitely many sets $A_t$, $x \leq t \leq f(x)$.

*Claim 1: $A_x \uh M(x) = A \uh M(x)$.* Since $x \leq c(x) \leq f(x)$, the stage $t = c(x)$ is among those considered, and $A_{c(x)} \uh x = A \uh x$. With $y = M(x) \leq x$, we get $A_x \uh y = A_{c(x)} \uh y = A \uh y$.

*Claim 2: $M(x) \to \infty$.* Fix $n$, and let $s_n$ be such that $A_t \uh n = A \uh n$ for all $t \geq s_n$. For $x \geq \max(n, s_n)$, all $A_t$ with $t \geq x$ agree with $A$ below $n$, so $M(x) \geq n$.

To decide whether $n \in A$ with oracle $f$, search for $x$ with $M(x) > n$, which exists by Claim 2, and answer $A_x(n)$, which is correct by Claim 1.
:::

:::figure[Frames in the proof of :ref{#thm-computation-function}. For each $x$, the stages $t$ with $x \leq t \leq f(x)$ include the stage $c(x)$ at which the approximation is correct below $x$. Agreement of all the stages of the frame below some length $M(x)$ therefore implies correctness below $M(x)$.]
<svg class="fig" viewBox="0 0 560 250" width="560" role="img" aria-label="For each x, the frame of stages from x to f(x) contains the stage c(x), at which the approximation is correct below x"><text x="80" y="24" text-anchor="middle" class="mrm muted" font-size="11">0</text><line x1="80" y1="32" x2="80" y2="186" class="axis" stroke-dasharray="2 4"/><text x="106" y="24" text-anchor="middle" class="mrm muted" font-size="11">1</text><line x1="106" y1="32" x2="106" y2="186" class="axis" stroke-dasharray="2 4"/><text x="132" y="24" text-anchor="middle" class="mrm muted" font-size="11">2</text><line x1="132" y1="32" x2="132" y2="186" class="axis" stroke-dasharray="2 4"/><text x="158" y="24" text-anchor="middle" class="mrm muted" font-size="11">3</text><line x1="158" y1="32" x2="158" y2="186" class="axis" stroke-dasharray="2 4"/><text x="184" y="24" text-anchor="middle" class="mrm muted" font-size="11">4</text><line x1="184" y1="32" x2="184" y2="186" class="axis" stroke-dasharray="2 4"/><text x="210" y="24" text-anchor="middle" class="mrm muted" font-size="11">5</text><line x1="210" y1="32" x2="210" y2="186" class="axis" stroke-dasharray="2 4"/><text x="236" y="24" text-anchor="middle" class="mrm muted" font-size="11">6</text><line x1="236" y1="32" x2="236" y2="186" class="axis" stroke-dasharray="2 4"/><text x="262" y="24" text-anchor="middle" class="mrm muted" font-size="11">7</text><line x1="262" y1="32" x2="262" y2="186" class="axis" stroke-dasharray="2 4"/><text x="288" y="24" text-anchor="middle" class="mrm muted" font-size="11">8</text><line x1="288" y1="32" x2="288" y2="186" class="axis" stroke-dasharray="2 4"/><text x="314" y="24" text-anchor="middle" class="mrm muted" font-size="11">9</text><line x1="314" y1="32" x2="314" y2="186" class="axis" stroke-dasharray="2 4"/><text x="340" y="24" text-anchor="middle" class="mrm muted" font-size="11">10</text><line x1="340" y1="32" x2="340" y2="186" class="axis" stroke-dasharray="2 4"/><text x="366" y="24" text-anchor="middle" class="mrm muted" font-size="11">11</text><line x1="366" y1="32" x2="366" y2="186" class="axis" stroke-dasharray="2 4"/><text x="392" y="24" text-anchor="middle" class="mrm muted" font-size="11">12</text><line x1="392" y1="32" x2="392" y2="186" class="axis" stroke-dasharray="2 4"/><text x="418" y="24" text-anchor="middle" class="mrm muted" font-size="11">13</text><line x1="418" y1="32" x2="418" y2="186" class="axis" stroke-dasharray="2 4"/><text x="444" y="24" text-anchor="middle" class="mrm muted" font-size="11">14</text><line x1="444" y1="32" x2="444" y2="186" class="axis" stroke-dasharray="2 4"/><text x="470" y="24" text-anchor="middle" class="mrm muted" font-size="11">15</text><line x1="470" y1="32" x2="470" y2="186" class="axis" stroke-dasharray="2 4"/><text x="496" y="24" text-anchor="middle" class="mrm muted" font-size="11">16</text><line x1="496" y1="32" x2="496" y2="186" class="axis" stroke-dasharray="2 4"/><text x="510" y="24" class="label">stage</text><text x="28" y="45" class="math" font-size="15">x</text><text x="40" y="45" class="mrm" font-size="15">= 3</text><rect x="154" y="33" width="138" height="14" rx="7" class="soft-fill"/><line x1="158" y1="40" x2="288" y2="40" class="accent-stroke" stroke-width="2"/><circle cx="210" cy="40" r="5" class="accent-fill"/><text x="28" y="79" class="math" font-size="15">x</text><text x="40" y="79" class="mrm" font-size="15">= 4</text><rect x="180" y="67" width="138" height="14" rx="7" class="soft-fill"/><line x1="184" y1="74" x2="314" y2="74" class="accent-stroke" stroke-width="2"/><circle cx="236" cy="74" r="5" class="accent-fill"/><text x="28" y="113" class="math" font-size="15">x</text><text x="40" y="113" class="mrm" font-size="15">= 5</text><rect x="206" y="101" width="190" height="14" rx="7" class="soft-fill"/><line x1="210" y1="108" x2="392" y2="108" class="accent-stroke" stroke-width="2"/><circle cx="314" cy="108" r="5" class="accent-fill"/><text x="28" y="147" class="math" font-size="15">x</text><text x="40" y="147" class="mrm" font-size="15">= 6</text><rect x="232" y="135" width="190" height="14" rx="7" class="soft-fill"/><line x1="236" y1="142" x2="418" y2="142" class="accent-stroke" stroke-width="2"/><circle cx="314" cy="142" r="5" class="accent-fill"/><text x="28" y="181" class="math" font-size="15">x</text><text x="40" y="181" class="mrm" font-size="15">= 7</text><rect x="258" y="169" width="216" height="14" rx="7" class="soft-fill"/><line x1="262" y1="176" x2="470" y2="176" class="accent-stroke" stroke-width="2"/><circle cx="392" cy="176" r="5" class="accent-fill"/><rect x="80" y="207" width="40" height="14" rx="7" class="soft-fill"/><line x1="84" y1="214" x2="116" y2="214" class="accent-stroke" stroke-width="2"/><text x="128" y="218" class="label">the frame of stages t with x ≤ t ≤ f(x)</text><circle cx="380" cy="214" r="5" class="accent-fill"/><text x="392" y="218" class="label">the stage c(x)</text></svg>
:::

The condition $c(x) \geq x$ in the definition of the computation function is used in Claim 1: it guarantees that the stages $x \leq t \leq f(x)$ include a correct stage. Without it, the frame could start after the correct stage and contain only incorrect stages.

The theorem is due to Miller and Martin (1968), who used it to show that every non-computable set $A \leq_T \emptyset'$ computes a function not dominated by any computable function: by the theorem, a computable function dominating $c$ would compute $A$. Their degrees are called **hyperimmune**, and they are studied in the course on immunity and growth.

:::quiz[domination of the computation function]
In Claim 1, where is the hypothesis that $f$ dominates $c$ used?

- [x] To guarantee that the correct stage $c(x)$ lies in the interval $[x, f(x)]$ examined by $M$.

  Then the stages of the interval agree with a correct stage on the segment of length $M(x)$, hence with $A$.
- [ ] To show that $M$ is $f$-computable.

  Computability of $M$ from $f$ holds for any $f$.
- [ ] To show that $M(x) \to \infty$.

  Claim 2 only uses the convergence of the approximation.

---

Why does $M(x)$ consider all stages between $x$ and $f(x)$, rather than only the stage $f(x)$?

- [x] Because the correct stage $c(x)$ is unknown; requiring agreement over the whole interval ensures agreement with it.

  The stage $f(x)$ alone may be incorrect on $A \uh x$, since the approximation may have changed again after $c(x)$.
- [ ] To make $M$ increasing.

  $M$ need not be increasing.
- [ ] Because $f(x)$ may be smaller than $x$.

  $f(x) \geq c(x) \geq x$.
:::

## Notes and references

The limit lemma is due to Shoenfield (1959), and was also observed by Gold and by Putnam (1965), in connection with learning in the limit and trial-and-error predicates. The theorem on computation functions is due to Miller and Martin (1968); it is Theorem 5.6.6 of Soare (2016), and Proposition "Martin and Miller" of the section on limit computability of Monin and Patey, whose proof is followed here. The name "Martin–Miller theorem" used in earlier versions of this lesson is not standard. Soare defines the computation function with $\mu s > x$ and $A \uh x$ the restriction to the elements $y \leq x$, which makes no difference to the argument. The limit lemma is Lemma 3.6.2 of Soare (2016), Theorem 2.6.1 of Downey and Hirschfeldt (2010) and Lemma 1.4.2 of Nies (2009); moduli are treated in Soare (2016, §3.5). The d.c.e. sets and the hierarchy of $n$-c.e. sets were introduced by Putnam and by Ershov.

- J. R. Shoenfield, *On degrees of unsolvability*, Annals of Mathematics 69 (1959), 644–653.
- H. Putnam, *Trial and error predicates and the solution to a problem of Mostowski*, Journal of Symbolic Logic 30 (1965), 49–57.
- E. M. Gold, *Limiting recursion*, Journal of Symbolic Logic 30 (1965), 28–48.
- W. Miller and D. A. Martin, *The degrees of hyperimmune sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 159–166.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §§3.5–3.6 and §5.6.

:::::exercises
::::exercise{#ex-modulus-not-dominated difficulty=1 objective="Deduce from the properties of the modulus that the settling time of the halting problem escapes every computable function."}
Let $m$ be the modulus of the approximation $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$. Show that no computable function dominates $m$, and that for every computable $f$ there are infinitely many $x$ with $f(x) < m(x)$.

:::solution
A computable function dominating $m$ would compute $\emptyset'$ by :ref{#prop-modulus-computes}, so $\emptyset'$ would be computable. If $f(x) \geq m(x)$ for all but finitely many $x$, modify $f$ at these finitely many points to obtain a computable function dominating $m$, which is impossible.
:::
::::

::::exercise{#ex-delta2-closure difficulty=1 objective="Manipulate $\Delta^0_2$ approximations to show closure properties of the sets computable in $\emptyset'$."}
Let $(A_s)$ and $(B_s)$ be $\Delta^0_2$ approximations of $A$ and $B$, and $f$ a total computable function. Give $\Delta^0_2$ approximations of $\nat \setminus A$, $A \cup B$, $A \cap B$, $A \oplus B$ and $f^{-1}(A) = \{ x : f(x) \in A \}$.

:::solution
Take $\nat \setminus A_s$, $A_s \cup B_s$, $A_s \cap B_s$, $A_s \oplus B_s$ and $f^{-1}(A_s) = \{ x : f(x) \in A_s \}$. Each sequence is uniformly computable, since membership of $x$ in its $s$-th term is computed from finitely many values $A_s(y)$, $B_s(y)$, with $y \in \{ x, f(x), \lfloor x/2 \rfloor \}$. For a fixed $x$, these finitely many values are constant from some stage on, and then equal to the values $A(y)$, $B(y)$; so the $s$-th term agrees with the target set at $x$ for all large $s$. For instance, if $A_s(f(x)) = A(f(x))$ for $s \geq s_0$, then $x \in f^{-1}(A_s) \iff x \in f^{-1}(A)$ for $s \geq s_0$. By :ref{#thm-limit-lemma}, this confirms that the sets computable in $\emptyset'$ are closed under these operations, which can also be checked directly with oracle machines.
:::
::::

::::exercise{#ex-limit-lemma-functions difficulty=2 objective="Extend the limit lemma from sets to functions."}
Show that a total function $f : \nat \to \nat$ is computable in $\emptyset'$ if and only if there is a total computable function $g : \nat^2 \to \nat$ with $f(x) = \lim_s g(x, s)$ for every $x$.

:::solution
Let $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$.

($\Rightarrow$) Let $f = \Phi^{\emptyset'}_e$, and let $g(x, s) = \Phi^{\emptyset'_s}_e(x)[s]$ if this computation converges, and $g(x, s) = 0$ otherwise. It is computable by :ref{#prop-oracle-stages}. Fix $x$, let $u$ be the use of $\Phi^{\emptyset'}_e(x)$ and $t$ a stage with $\Phi^{\emptyset'}_e(x)[t]\converge$. Only finitely many elements below $u$ enter $\emptyset'$, so there is $s_0$ with $\emptyset'_s \uh u = \emptyset' \uh u$ for $s \geq s_0$. For $s \geq \max(s_0, t, u)$, the computation $\Phi^{\emptyset'}_e(x)[s]$ converges by monotonicity and reads only cells below $u$, where $\emptyset'_s$ and $\emptyset'$ agree; so $\Phi^{\emptyset'_s}_e(x)[s]\converge = f(x)$, and $g(x, s) = f(x)$.

($\Leftarrow$) The relation $C(x, y) \iff \exists s \geq y\ \ g(x, s) \neq g(x, y)$ is c.e., hence computable in $\emptyset'$ (:ref{#prop-ce-below-jump}). With oracle $\emptyset'$, search for the least $y$ with $\neg C(x, y)$, which exists since $g(x, s)$ is eventually constant, and output $g(x, y)$. Since $g(x, s) = g(x, y)$ for all $s \geq y$, this is $\lim_s g(x, s) = f(x)$.

The proof is that of :ref{#thm-limit-lemma}, with values in $\nat$ instead of $\{0, 1\}$. Adapted from Nies 2009, Exercise 1.4.7(i).
:::
::::

::::exercise{#ex-bounded-use-changes difficulty=2 objective="Prove the converse of the exercise on bounded mind changes: a computation from $\emptyset'$ with computably bounded use gives an approximation with computably bounded mind changes."}
Let $A = \Phi^{\emptyset'}_e$ with $\use^{\emptyset'}_e(x) \leq b(x)$ for every $x$, for a computable function $b$. Show that $A$ has a $\Delta^0_2$ approximation $(A_s)$ such that, for every $x$, the number of $s$ with $A_{s+1}(x) \neq A_s(x)$ is at most $b(x) + 1$.

:::solution
Let $\emptyset'_s = \{ e : \Phi_e(e)[s]\converge \}$, and $\sigma_{x, s} = \emptyset'_s \uh b(x)$, a string of length $b(x)$. Define $A_0(x) = 0$ and
$$
A_{s+1}(x) = \begin{cases} v & \text{if } \Phi^{\sigma_{x, s+1}}_e(x)[s+1]\converge = v \text{ with } v \in \{0, 1\},\\ A_s(x) & \text{otherwise.} \end{cases}
$$
The sequence is uniformly computable by :ref{#prop-oracle-stages}.

*Mind changes.* The approximation $(\emptyset'_s)$ is increasing, so the string $\sigma_{x, s}$ changes only when an element below $b(x)$ enters, which happens at most $b(x)$ times. The stages therefore split into at most $b(x) + 1$ intervals on which $\sigma_{x, s}$ is a constant string $\sigma$. On such an interval, once $\Phi^\sigma_e(x)[s]\converge = v$ holds, it holds at all later stages of the interval with the same $v$ (monotonicity in $s$), so $A_s(x)$ changes at most once in the interval: when this computation first converges. In total, $x$ changes at most $b(x) + 1$ times.

*Convergence.* From some stage $s_0$ on, $\sigma_{x, s} = \emptyset' \uh b(x)$. The computation $\Phi^{\emptyset'}_e(x)$ has use $u \leq b(x)$, so by :ref{#thm-use-principle} and monotonicity, $\Phi^{\emptyset' \uh b(x)}_e(x)\converge = A(x)$, and $\Phi^{\emptyset' \uh b(x)}_e(x)[s]\converge = A(x)$ for all large $s$. From then on $A_s(x) = A(x)$.

The sets with an approximation of this kind are the **$\omega$-c.e.** sets. With :ref{#ex-bounded-changes-use}, the exercise shows that they are exactly the sets computable from $\emptyset'$ with a computably bounded use (Soare 2016, Theorem 3.8.8; Downey and Hirschfeldt 2010, Corollary 2.6.2).
:::
::::

::::exercise{#ex-modulus-not-in-set difficulty=2 objective="See that the modulus of a $\Delta^0_2$ approximation need not be computable in the set approximated."}
Give a $\Delta^0_2$ approximation of the empty set whose modulus computes $\emptyset'$. Compare with item 2 of :ref{#prop-modulus-computes}.

:::solution
For $e \in \emptyset'$, let $s_e$ be the least $s$ with $\Phi_e(e)[s]\converge$. Let $A_s = \{ e : s = s_e \}$; that is, $e \in A_s$ if and only if $\Phi_e(e)[s]\converge$ and, for $s \geq 1$, not $\Phi_e(e)[s-1]\converge$ (for $s = 0$ no computation has converged, since convergence at stage $s$ requires $e < s$). This sequence is uniformly computable. Each $e$ belongs to $A_s$ for at most one $s$, so $\lim_s A_s(e) = 0$, and $(A_s)$ is a $\Delta^0_2$ approximation of $\emptyset$.

Let $m$ be its modulus. If $e \in \emptyset'$, the bit $e$ equals $1$ at stage $s_e$ and $0$ at stage $s_e + 1$, so the bits below $e + 1$ change after every stage $s < s_e + 1$: hence $m(e + 1) > s_e$. Therefore $e \in \emptyset'$ if and only if $\Phi_e(e)[m(e + 1)]\converge$: if $e \in \emptyset'$, the computation converges at stage $s_e < m(e+1)$, hence at stage $m(e+1)$ by monotonicity; the converse is clear. So $\emptyset' \leq_T m$, while the set approximated is computable. For a c.e. approximation this cannot happen, since then $m \leq_T A$.
:::
::::

::::exercise{#ex-co-dce difficulty=1 objective="Diagonalize against all differences of c.e. sets to show that the class of d.c.e. sets is not closed under complement."}
Show that there is a set $A$ whose complement is d.c.e. but which is not d.c.e. Deduce that $A$ is computable in $\emptyset'$ and has an approximation in which each $x$ changes at most twice, starting from the value $1$.

:::solution
Write $e = \langle a, b \rangle$, and let $B = \{ \langle a, b \rangle : \langle a, b \rangle \in W_a \}$ and $C = \{ \langle a, b \rangle : \langle a, b \rangle \in W_b \}$. Both are c.e., so $D = B \setminus C$ is d.c.e. Let $A = \nat \setminus D$. If $A = W_a \setminus W_b$ for some $a$ and $b$, let $e = \langle a, b \rangle$. Then
$$
e \in A \iff e \in W_a \setminus W_b \iff e \in B \setminus C = D \iff e \notin A,
$$
a contradiction. So $A$ is not d.c.e.

By :ref{#ex-dce-limit}, $D$ has an approximation $(D_s)$ in which each $x$ starts at $0$ and changes at most twice. Then $A_s = \nat \setminus D_s$ is an approximation of $A$ which starts at $1$ and changes at most twice, and $A$ is computable in $\emptyset'$. This is the first step of the **Ershov hierarchy** of $n$-c.e. sets (Soare 2016, Exercise 3.8.16, gives the general step: an $(n+1)$-c.e. set that is not $n$-c.e.).
:::
::::

::::exercise{#ex-ce-computation-function difficulty=1 objective="Compare the modulus and the computation function of a c.e. approximation."}
Let $(A_s)$ be a c.e. approximation of $A$, with modulus $m$ and computation function $c$. Show that $c(x) = \max(x, m(x))$ for every $x$, and that $A$, $m$ and $c$ are Turing equivalent.

:::solution
As in the proof of :ref{#prop-modulus-computes}, for a c.e. approximation, $A_s \uh x = A \uh x$ implies $A_t \uh x = A \uh x$ for every $t \geq s$: the elements of $A$ below $x$ are already in $A_s$, elements never leave, and no other element enters, since $A_t \subseteq A$. Conversely, if $A_s \uh x \neq A \uh x$, a change below $x$ occurs after stage $s$. So the stages $s$ with $A_s \uh x = A \uh x$ form the final segment $[m(x), \infty)$, and the least such $s \geq x$ is $\max(x, m(x))$.

By :ref{#prop-modulus-computes}, $A \equiv_T m$; $c$ is computed from $m$ by the formula above. Conversely, $m$ is computed from $c$: if $c(x) > x$, then $m(x) = c(x)$; if $c(x) = x$, then $m(x) \leq x$, the string $A_x \uh x$ is correct, and $m(x)$ is the least $s \leq x$ with $A_s \uh x = A_x \uh x$, which is computed from the approximation. So $A \equiv_T m \equiv_T c$, in agreement with :ref{#thm-computation-function}.
:::
::::
:::::
