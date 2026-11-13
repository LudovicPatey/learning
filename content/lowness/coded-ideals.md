---
title: Coded Scott ideals
summary: A set codes a countable family through its columns; no Turing ideal contains its own code; the codes of Scott ideals containing X, with computable indices for joins, reductions and PA sets, form a non-empty Π⁰₁(X) class, so the sets PA relative to X are exactly those that compute such codes, and low codes exist.
duration: 40
prerequisites: [forcing-the-jump, big-five/wkl0, reducibilities/wkl-reductions, pi01-classes/pa-degrees]
---

The proofs of strong cone avoidance and of Seetapun's theorem use Mathias forcing with reservoirs in a Scott ideal (:ref{#thm-dj-cone-avoidance}, :ref{to="avoidance/seetapun-forcing"}). The reservoirs must be closed under the operations of the construction: intersection with a set of the ideal, and choice of a path through a tree of the ideal. To carry out such a construction effectively, an oracle must be able to name the reservoirs by finite codes, to compute the codes of the new reservoirs, and to answer questions about them. Computable reservoirs are named by $\Delta^0_1$ indices, but the computable sets do not form a Scott ideal. This lesson provides names for the members of a Scott ideal: a single set $M$ lists them as its columns, and a member is named by its column number. The main facts are that such a list can be chosen with the operations of the ideal given by computable functions on column numbers, that every PA set computes one, and that a single application of the low basis theorem gives a low one.

## Codes of families of sets

Recall that $\langle \cdot, \cdot \rangle$ is Cantor's pairing function, a computable bijection from $\nat^2$ to $\nat$ with $\langle a, b \rangle \geq a, b$.

:::definition{#def-coded-family}
The **join** of a sequence of sets $Z_0, Z_1, \dots$ is the set $\bigoplus_n Z_n = \{ \langle n, x \rangle : x \in Z_n \}$; the set $Z_n$ is its **$n$-th column**. A set $M$ **codes** a countable family $\mathcal M$ if $M = \bigoplus_n Z_n$ and $\mathcal M = \{ Z_n : n \in \nat \}$. An **$M$-index** of a set $X \in \mathcal M$ is an $n$ with $Z_n = X$.
:::

Every column is computable in $M$, uniformly in its index: $x \in Z_n$ if and only if $\langle n, x \rangle \in M$. So every member of the coded family is computable in $M$. The converse fails: the family coded by $M$ never contains all the sets computable in $M$.

:::proposition{#prop-no-self-code}
If $M$ codes a family $\mathcal M = \{ Z_n : n \in \nat \}$, the set $D = \{ n : n \notin Z_n \}$ is computable in $M$ and does not belong to $\mathcal M$. In particular, no Turing ideal contains a set that codes it.
:::

:::proof{of=prop-no-self-code}
$D$ is computable in $M$, since $n \in D$ if and only if $\langle n, n \rangle \notin M$. If $D = Z_m$, then $m \in D \iff m \notin Z_m \iff m \notin D$, a contradiction. If $\mathcal M$ is a Turing ideal coded by $M \in \mathcal M$, then $D \leq_T M$ belongs to $\mathcal M$, which is impossible.
:::

So a code of a Turing ideal is strictly more complex than every member. For the ideal of computable sets, $\emptyset''$ computes a code, since it decides which programs compute total $\{0, 1\}$-valued functions; by the proposition, every code of this ideal computes a set that is not computable. For Scott ideals, the next theorem gives a precise answer: the sets that compute codes of Scott ideals containing $X$ are exactly the sets PA relative to $X$.

## The Scott class

:::theorem[Scott]{#thm-scott-class}
Let $X$ be a set. For $a, b, e \in \nat$, let
$$
\mathrm{join}(a, b) = 3\langle a, b \rangle + 1, \qquad \mathrm{red}(a, e) = 3 \langle a, e \rangle + 2, \qquad \mathrm{pa}(a) = 3a + 3.
$$
Let $\mathcal S_X$ be the class of sets $M = \bigoplus_n Z_n$ such that for all $a, b, e$:

1. $Z_0 = X$;
2. $Z_{\mathrm{join}(a, b)} = Z_a \oplus Z_b$;
3. for all $x$, if $\Phi^{Z_a}_e(x)\converge = v \in \{0, 1\}$, then $Z_{\mathrm{red}(a, e)}(x) = v$;
4. for all $i$, if $\Phi^{Z_a}_i(i)\converge = v$, then $Z_{\mathrm{pa}(a)}(i) \neq v$.

Then $\mathcal S_X$ is a non-empty $\Pi^0_1(X)$ class, and every member codes a Scott ideal containing $X$. Moreover:

- if $\Phi^{Z_a}_e$ is the characteristic function of a set $Y$, then $Z_{\mathrm{red}(a, e)} = Y$;
- $Z_{\mathrm{pa}(a)}$ is a $\{0, 1\}$-valued function DNC relative to $Z_a$.
:::

:::proof{of=thm-scott-class}
Every $n \geq 1$ is of exactly one of the forms $\mathrm{join}(a, b)$, $\mathrm{red}(a, e)$ or $\mathrm{pa}(a)$, according to its remainder modulo $3$, since the pairing function is a bijection. In each clause, the columns referred to have indices smaller than $n$: $\langle a, b \rangle \geq a, b$ gives $3\langle a, b \rangle + 1 > a, b$, and $3a + 3 > a$.

*Complexity.* Each clause is a universal statement whose matrix is decided by finitely many bits of $M$ and $X$: for clause 3, the computation $\Phi^{Z_a}_e(x)[s]$ at stage $s$ queries finitely many bits of the column $Z_a$, that is, of $M$, and the clause holds if and only if for all $x$ and $s$, convergence at stage $s$ with value $v \in \{0, 1\}$ implies $Z_{\mathrm{red}(a, e)}(x) = v$. Clauses 2 and 4 are similar, and clause 1 compares bits of $M$ and $X$. A conjunction of uniformly $\Pi^0_1(X)$ conditions is $\Pi^0_1(X)$, so $\mathcal S_X$ is a $\Pi^0_1(X)$ class (:ref{#prop-pi01-equivalent}, relativized).

*Non-emptiness.* Define the columns by recursion on $n$: $Z_0 = X$; for $n = \mathrm{join}(a, b)$, $Z_n = Z_a \oplus Z_b$; for $n = \mathrm{red}(a, e)$, let $Z_n(x) = \Phi^{Z_a}_e(x)$ if this converges with a value in $\{0, 1\}$, and $Z_n(x) = 0$ otherwise; for $n = \mathrm{pa}(a)$, let $Z_n(i) = 1$ if $\Phi^{Z_a}_i(i)\converge = 0$, and $Z_n(i) = 0$ otherwise. The columns used at step $n$ are already defined, and each clause holds for $n$.

*Members.* Let $M \in \mathcal S_X$ and $\mathcal M = \{ Z_n \}$. If $\Phi^{Z_a}_e$ is the characteristic function of $Y$, clause 3 gives $Z_{\mathrm{red}(a, e)}(x) = Y(x)$ for every $x$. So $\mathcal M$ is closed downward under Turing reducibility, and by clause 2 under joins: it is a Turing ideal, containing $X$ by clause 1. By clause 4, $Z_{\mathrm{pa}(a)}$ differs from $\Phi^{Z_a}_i(i)$ whenever this converges, and it is $\{0, 1\}$-valued as a set; so it is PA relative to $Z_a$. By :ref{#prop-wkl-scott}, $\mathcal M$ is a Scott ideal.
:::

:::figure[The first ten columns of a member of the Scott class $\mathcal S_X$. Column $0$ is $X$; each later column is determined, or constrained, by earlier ones: a join, a set computed from an earlier column, or a function DNC relative to an earlier column.]
<svg class="fig" viewBox="0 0 600 256" width="600" role="img" aria-label="The first ten columns of a member of the Scott class: column 0 is the parameter X; the other columns are, in turn, a join of two earlier columns, a set computed from an earlier column, and a function diagonally non-computable relative to an earlier column"><defs><marker id="lw-sc-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><rect x="34" y="40" width="46" height="120" rx="4" class="cell"/><text x="57.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">0</tspan></text><text x="57.0" y="80" text-anchor="middle" class="label">X</text><text x="57.0" y="190" text-anchor="middle" class="label muted">parameter</text><rect x="88" y="40" width="46" height="120" rx="4" class="cell"/><text x="111.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">1</tspan></text><text x="111.0" y="80" text-anchor="middle" class="label">Z₀</text><text x="111.0" y="96" text-anchor="middle" class="label">⊕</text><text x="111.0" y="112" text-anchor="middle" class="label">Z₀</text><text x="111.0" y="190" text-anchor="middle" class="label muted">join</text><rect x="142" y="40" width="46" height="120" rx="4" class="cell"/><text x="165.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">2</tspan></text><text x="165.0" y="80" text-anchor="middle" class="label">Φ₀(Z₀)</text><text x="165.0" y="190" text-anchor="middle" class="label muted">reduction</text><rect x="196" y="40" width="46" height="120" rx="4" class="cell head-cell"/><text x="219.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">3</tspan></text><text x="219.0" y="80" text-anchor="middle" class="label">DNC₂</text><text x="219.0" y="96" text-anchor="middle" class="label">over</text><text x="219.0" y="112" text-anchor="middle" class="label">Z₀</text><text x="219.0" y="190" text-anchor="middle" class="label muted">PA</text><rect x="250" y="40" width="46" height="120" rx="4" class="cell"/><text x="273.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">4</tspan></text><text x="273.0" y="80" text-anchor="middle" class="label">Z₁</text><text x="273.0" y="96" text-anchor="middle" class="label">⊕</text><text x="273.0" y="112" text-anchor="middle" class="label">Z₀</text><text x="273.0" y="190" text-anchor="middle" class="label muted">join</text><rect x="304" y="40" width="46" height="120" rx="4" class="cell"/><text x="327.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">5</tspan></text><text x="327.0" y="80" text-anchor="middle" class="label">Φ₀(Z₁)</text><text x="327.0" y="190" text-anchor="middle" class="label muted">reduction</text><rect x="358" y="40" width="46" height="120" rx="4" class="cell head-cell"/><text x="381.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">6</tspan></text><text x="381.0" y="80" text-anchor="middle" class="label">DNC₂</text><text x="381.0" y="96" text-anchor="middle" class="label">over</text><text x="381.0" y="112" text-anchor="middle" class="label">Z₁</text><text x="381.0" y="190" text-anchor="middle" class="label muted">PA</text><rect x="412" y="40" width="46" height="120" rx="4" class="cell"/><text x="435.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">7</tspan></text><text x="435.0" y="80" text-anchor="middle" class="label">Z₀</text><text x="435.0" y="96" text-anchor="middle" class="label">⊕</text><text x="435.0" y="112" text-anchor="middle" class="label">Z₁</text><text x="435.0" y="190" text-anchor="middle" class="label muted">join</text><rect x="466" y="40" width="46" height="120" rx="4" class="cell"/><text x="489.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">8</tspan></text><text x="489.0" y="80" text-anchor="middle" class="label">Φ₁(Z₀)</text><text x="489.0" y="190" text-anchor="middle" class="label muted">reduction</text><rect x="520" y="40" width="46" height="120" rx="4" class="cell head-cell"/><text x="543.0" y="30" text-anchor="middle" class="math" font-size="14">Z<tspan class="mrm" font-size="10" dy="4">9</tspan></text><text x="543.0" y="80" text-anchor="middle" class="label">DNC₂</text><text x="543.0" y="96" text-anchor="middle" class="label">over</text><text x="543.0" y="112" text-anchor="middle" class="label">Z₂</text><text x="543.0" y="190" text-anchor="middle" class="label muted">PA</text><text x="300" y="218" text-anchor="middle" class="label">column 3⟨a, b⟩ + 1: join of columns a and b;  column 3⟨a, e⟩ + 2: Φₑ applied to column a;</text><text x="300" y="236" text-anchor="middle" class="label">column 3a + 3: a {0,1}-valued function DNC relative to column a (Cantor pairing ⟨·,·⟩)</text></svg>
:::

The clauses are chosen so that each is a $\Pi^0_1$ constraint on a column in terms of earlier columns, and can be satisfied whatever the earlier columns are. Clause 3 cannot require that $Z_{\mathrm{red}(a, e)}$ equal $\Phi^{Z_a}_e$, since totality is not a $\Pi^0_1$ property; it only requires agreement where the computation converges, and this suffices when the computation is total. The same device makes the paths through trees of the ideal available by computable indices.

:::lemma{#lem-scott-paths}
There is a computable function $p$ such that for every $X$, every $M = \bigoplus_n Z_n \in \mathcal S_X$, every $a$ and every $t$: if $\Phi^{Z_a}_t$ is the characteristic function of an infinite binary tree $T$, then $Z_{p(a, t)}$ is a path of $T$.
:::

:::proof{of=lem-scott-paths}
The proof of :ref{#thm-pa-characterization} is uniform and relativizes: there is a computable $k$ such that, for every $Z$, every $\{0, 1\}$-valued function $f$ DNC relative to $Z$ and every $t$ such that $\Phi^Z_t$ is the characteristic function of an infinite binary tree, $\Phi^{Z \oplus f}_{k(t)}$ is the characteristic function of a path of this tree. Apply it with $Z = Z_a$ and $f = Z_{\mathrm{pa}(a)}$: the set $Z_a \oplus Z_{\mathrm{pa}(a)}$ is the column $\mathrm{join}(a, \mathrm{pa}(a))$, so $p(a, t) = \mathrm{red}(\mathrm{join}(a, \mathrm{pa}(a)), k(t))$ works.
:::

In words: from the $M$-index of a set $Z$ of the ideal and an index of a non-empty $\Pi^0_1(Z)$ class, one computes the $M$-index of a member of the class. This is the effective form of the closure of a Scott ideal under paths.

:::quiz[the Scott class]
Why does clause 3 of :ref{#thm-scott-class} only constrain the column where $\Phi^{Z_a}_e$ converges with a value in $\{0, 1\}$?

- [x] Because the clause must be $\Pi^0_1$ and satisfiable for every $a$ and $e$, including those for which $\Phi^{Z_a}_e$ is partial or not $\{0, 1\}$-valued; when it is a characteristic function, the clause determines the column completely.
- [ ] Because the column must be finite.

  The column may be infinite; it is the set computed by $\Phi_e$ when that set exists.
- [ ] Because the other values are already fixed by clause 2.

  Clause 2 concerns other columns.

---

Why is every column constrained only in terms of columns of smaller index?

- [x] So that the columns can be defined one after the other, which proves that the class is non-empty.
- [ ] So that the class is $\Pi^0_1$.

  Constraints referring to later columns would also be $\Pi^0_1$; the order matters for satisfiability, not for complexity.
- [ ] So that the ideal contains $X$.

  That is clause 1.
:::

:::corollary{#cor-scott-codes}
Let $X$ be a set.
1. A set computes a member of $\mathcal S_X$ if and only if it is PA relative to $X$. In particular, every set PA relative to $X$ computes a code of a Scott ideal containing $X$.
2. There is a code $M$ of a Scott ideal containing $X$ with $M' \leq_T X'$. In particular, there is a low code of a Scott ideal, and every member of the ideal it codes is low.
:::

:::proof{of=cor-scott-codes}
1. A set PA relative to $X$ computes a member of every non-empty $\Pi^0_1(X)$ class, by :ref{#thm-pa-characterization} relativized; apply it to $\mathcal S_X$. Conversely, a member $M$ of $\mathcal S_X$ computes the column $Z_{\mathrm{pa}(0)}$, a $\{0, 1\}$-valued function DNC relative to $Z_0 = X$, so $M$ is PA relative to $X$.
2. By the low basis theorem relativized to $X$, the non-empty $\Pi^0_1(X)$ class $\mathcal S_X$ has a member $M$ with $(X \oplus M)' \leq_T X'$; since $X = Z_0$ is computable in $M$, this is $M' \leq_T X'$. For $X = \emptyset$, $M$ is low, and every member of the ideal, being computable in $M$, is low.
:::

Item 1 is the coded form of :ref{#thm-scott-pa}, and item 2 is Simpson's proof of :ref{#thm-low-scott}: one application of the low basis theorem to the class of codes, instead of countably many applications to the classes of PA sets. The difference matters for what follows. The ideal of :ref{#thm-low-scott} consists of low sets, but its natural code $\bigoplus_n Z_n$ need not be low; the code of item 2 is. The next lesson, :ref{to="lowness/uniform-lowness"}, shows what $\emptyset'$ can answer about the members of an ideal with a low code.

## Exercises

::::exercise{difficulty=1}
Let $C$ be a non-computable set. Show, with a single application of the cone avoidance basis theorem, that there is a code $M$ of a Scott ideal with $C \not\leq_T M$, and deduce :ref{#lem-scott-cone} for $Z = \emptyset$.

:::solution
By :ref{#thm-cone-avoidance-basis}, the non-empty $\Pi^0_1$ class $\mathcal S_\emptyset$ has a member $M$ with $C \not\leq_T M$. Every member of the ideal coded by $M$ is computable in $M$, so it does not compute $C$. The ideal is a Scott ideal by :ref{#thm-scott-class}, and it does not contain $C$.
:::
::::

::::exercise{difficulty=1}
Let $M$ code a Turing ideal $\mathcal M$ that contains $\emptyset$ and is closed under the jump. Show that $M$ computes every arithmetic set, and that $M$ is not arithmetic.

:::solution
$\mathcal M$ contains $\emptyset^{(n)}$ for every $n$, and every member of $\mathcal M$ is computable in $M$; every arithmetic set is computable in some $\emptyset^{(n)}$ by Post's theorem. If $M$ were arithmetic, it would be computable in some $\emptyset^{(n)}$, and $\emptyset^{(n+1)}$, which is computable in $M$, would be computable in $\emptyset^{(n)}$, contradicting :ref{#thm-jump}.
:::
::::

## Notes and references

Scott (1962) showed that the countable Scott ideals are exactly the families of sets representable in complete extensions of Peano arithmetic, and that every PA degree computes one; the presentation through a $\Pi^0_1$ class of codes follows the section *Coding ideals* of the chapter *Lowness* of Patey's monograph, with explicit clauses for joins, reductions and PA sets instead of an enumeration of tree functionals, so that every column depends only on earlier ones. Simpson builds countable coded ω-models of $\mathsf{WKL}_0$ as paths of a single tree (Definition VII.2.1, Lemma VIII.2.9, Theorem VIII.2.17 and Corollary VIII.2.18). The same section of the monograph proves Spector's exact pair theorem for countable ideals, which is :ref{#thm-exact-pair} of the course on the structure of the degrees.

- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in *Recursive Function Theory*, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009, Sections VII.2 and VIII.2.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, section *Coding ideals*.
