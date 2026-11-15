---
title: Computable Sacks forcing
summary: Sufficiently generic sets for computable Sacks forcing are computably dominated and of minimal degree; unlike 1-generic sets, they are not generalized low; traces for the functions they compute.
duration: 30
prerequisites: [forcing-with-trees, degree-structure/minimal-degrees]
---

Cohen forcing and computable Sacks forcing produce generic sets with opposite properties. A 1-generic set is generalized low, is not of minimal degree, and has hyperimmune degree; it is a typical set in the sense of category. A Sacks generic set is computably dominated and of minimal degree, and its jump cannot be computed from the set and any fixed oracle. The difference comes from what a condition can decide. A string decides the convergence of computations, which are local properties of the set; a perfect tree decides properties of all its paths at once, such as "$\Phi_e$ loses all information" or "$\Phi_e$ is total", but cannot fix the bits of the set beyond its root.

This lesson collects the properties of Sacks generic sets. The first section restates results of earlier courses as density statements; the second proves a new one, due to Monin and Patey.

## Minimal degrees and computable domination

The constructions of a computably dominated set (:ref{#thm-martin-miller-ftrees}) and of a minimal degree (:ref{#thm-minimal-degree}) both proceed by computable f-trees. In the language of forcing they prove density statements.

:::proposition{#prop-sacks-generic}
Every sufficiently generic set for computable Sacks forcing is non-computable, computably dominated, and of minimal degree.
:::

:::proof{of=prop-sacks-generic}
For each $e$, each of the following sets of conditions is dense, by the lemma indicated, applied to an arbitrary condition $T$: the subtrees $S$ such that $\Phi_e \neq X$ for every path $X$ (:ref{#lem-ftree-noncomputable}); the subtrees on all paths of which $\Phi_e$ is partial, or bounded by a common computable function (:ref{#lem-ftree-domination}); the subtrees that are $e$-splitting or avoid $e$-splits (:ref{#lem-splitting-dichotomy}). Let $G$ be generic for these sets. It is not computable, and computably dominated. If $Y = \Phi^G_e$ is total, $G$ is a path of a condition that is $e$-splitting or avoids $e$-splits, so $G \leq_T Y$ or $Y$ is computable by :ref{#lem-splitting-consequences}.
:::

The theorems of Spector and of Miller and Martin add that the generic set can be taken computable in $\emptyset''$: the three families of dense sets are uniformly $\emptyset''$-effectively dense, as their proofs show, and the root of each condition is a prefix of the generic set. Cohen generic sets behave in the opposite way: a 1-generic set is never of minimal degree, since its columns are Turing independent (:ref{#thm-generic-independent}).

::::exercise{#ex-sacks-traceable difficulty=2 objective="Extract computable traces from the domination argument for computable Sacks forcing."}
Let $G$ be sufficiently generic for computable Sacks forcing. Show that $G$ is **computably traceable** with bound $2^n$: for every total $G$-computable function $f$ there is a computable sequence $(T_n)$ of finite sets, given by canonical indices, with $|T_n| \leq 2^n$ and $f(n) \in T_n$ for every $n$.

:::solution
Let $f = \Phi^G_e$. By :ref{#lem-ftree-domination}, the set of conditions $S$ such that either $\Phi^X_e$ is partial for every path $X$, or $\Phi^{S(\rho)}_e(|\rho|)\converge$ for every $\rho$, is dense: in Case 2 of the proof, the subtree built has this property. Let $G$ be generic for these sets. Since $\Phi^G_e$ is total, $G$ is a path of a condition $S$ of the second kind. Let $T_n = \{ \Phi^{S(\rho)}_e(n) : |\rho| = n \}$, computable from $n$ since $S$ is computable, with at most $2^n$ elements. Some $\rho$ of length $n$ has $S(\rho) \prec G$, so $f(n) = \Phi^{S(\rho)}_e(n) \in T_n$. Adapted from Monin and Patey, chapter *Effective forcing*, exercise on computable traceability in the section *Forcing with trees*.
:::
::::

## Sacks generic sets are not generalized low

A 1-generic set is generalized low, $G' \leq_T G \oplus \emptyset'$ (:ref{#cor-cohen-jumps}). For Sacks generic sets the jump cannot be computed from $G$ and any fixed oracle. The idea is to choose a $\Pi^0_1$ class $[R]$ inside the current condition, so that the jump of $G$ knows whether $G \in [R]$, and to keep, above every node of $R$, a node of the condition outside $[R]$. Whatever a reduction predicts about this bit of the jump, the condition can be extended to make the prediction wrong.

:::theorem{#thm-sacks-not-gl1}
Let $X$ be any set. For every sufficiently generic set $G$ for computable Sacks forcing, $G' \not\leq_T G \oplus X$.
:::

:::proof{of=thm-sacks-not-gl1}
Fix $e$ and a condition $T$. We find $S \leq T$ such that $\Phi^{P \oplus X}_e \neq P'$ for every path $P$ of $S$; the set of such conditions is then dense, for each $e$.

For a string $\rho$, let $\hat\rho$ be the string obtained by inserting a $0$ after each bit of $\rho$, and let $R(\rho) = T(\hat \rho)$. Since $\rho \mapsto \hat\rho$ preserves comparability and incomparability, $R$ is a computable f-tree and a subtree of $T$. For each $\rho$, let $\tau_\rho = T(\hat\rho\, 0 1)$, a node of $T$ above $R(\rho)$. No path of $R$ extends $\tau_\rho$: such a path would extend $R(\rho)$, hence one of the nodes $R(\rho 0) = T(\hat\rho\, 0 0)$ and $R(\rho 1) = T(\hat\rho\, 1 0)$, which are incompatible with $T(\hat\rho\, 0 1)$.

The class $[R]$ is $\Pi^0_1$. Let $a$ be an index of a functional such that $\Phi^Y_a(x)$ searches for a $k$ such that no node $R(\rho)$ with $|\rho| = k$ is a prefix of $Y$. Then $\Phi^Y_a(a)\converge$ if and only if $Y \notin [R]$, so $Y'(a) = 1$ if and only if $Y \notin [R]$, for every set $Y$.

For a string $\nu$, the computation $\Phi^{\nu \oplus X}_e(a)$ uses the oracle $\nu \oplus X$, with the bits of $\nu$ at the even positions below $2|\nu|$, and is defined if it reads no other even position.

- If $\Phi^{\nu \oplus X}_e(a)$ diverges for every node $\nu$ of $R$, let $S = R$. For every path $P$ of $R$, $\Phi^{P \oplus X}_e(a)\diverge$, since a convergent computation would converge with a node of $R$ that is a prefix of $P$.
- Otherwise, take a node $\nu = R(\rho)$ with $\Phi^{\nu \oplus X}_e(a)\converge = i$. If $i = 1$, let $S$ be the full subtree of $R$ above $\nu$: its paths $P$ are in $[R]$, so $P'(a) = 0 \neq 1 = \Phi^{P \oplus X}_e(a)$. If $i \neq 1$, let $S$ be the full subtree of $T$ above $\tau_\rho$: its paths $P$ extend $\nu$ and are not in $[R]$, so $P'(a) = 1 \neq i = \Phi^{P \oplus X}_e(a)$.

In every case $\Phi^{P \oplus X}_e(a) \neq P'(a)$ for every path $P$ of $S$. A set generic for these dense sets, for all $e$, satisfies $G' \not\leq_T G \oplus X$.
:::

:::figure[The subtree $R$ of the proof of :ref{#thm-sacks-not-gl1}, for $T$ the identity tree, drawn to depth $4$. The nodes of $R$ are the strings with a $0$ after each bit. Above each node $R(\rho)$, the node $\tau_\rho = T(\hat\rho\, 0 1)$ of $T$ is extended by no path of $R$. Whether a path lies in $[R]$ is a bit of its jump, and the condition can always be shrunk to a subtree of $R$ or to a subtree above some $\tau_\rho$.]
<svg class="fig" viewBox="0 0 600 316" width="600" role="img" aria-label="A binary tree of depth four; the nodes of a subtree R are highlighted, and for each node of R a node of the tree whose cylinder avoids the paths of R"><line x1="300.0" y1="26" x2="165.0" y2="78" class="accent-stroke" stroke-width="2.4"/><line x1="300.0" y1="26" x2="435.0" y2="78" class="accent-stroke" stroke-width="2.4"/><line x1="165.0" y1="78" x2="97.5" y2="130" class="accent-stroke" stroke-width="2.4"/><line x1="165.0" y1="78" x2="232.5" y2="130" class="muted-stroke" stroke-width="1"/><line x1="435.0" y1="78" x2="367.5" y2="130" class="accent-stroke" stroke-width="2.4"/><line x1="435.0" y1="78" x2="502.5" y2="130" class="muted-stroke" stroke-width="1"/><line x1="97.5" y1="130" x2="63.8" y2="182" class="accent-stroke" stroke-width="2.4"/><line x1="97.5" y1="130" x2="131.2" y2="182" class="accent-stroke" stroke-width="2.4"/><line x1="232.5" y1="130" x2="198.8" y2="182" class="muted-stroke" stroke-width="1"/><line x1="232.5" y1="130" x2="266.2" y2="182" class="muted-stroke" stroke-width="1"/><line x1="367.5" y1="130" x2="333.8" y2="182" class="accent-stroke" stroke-width="2.4"/><line x1="367.5" y1="130" x2="401.2" y2="182" class="accent-stroke" stroke-width="2.4"/><line x1="502.5" y1="130" x2="468.8" y2="182" class="muted-stroke" stroke-width="1"/><line x1="502.5" y1="130" x2="536.2" y2="182" class="muted-stroke" stroke-width="1"/><line x1="63.8" y1="182" x2="46.9" y2="234" class="accent-stroke" stroke-width="2.4"/><line x1="63.8" y1="182" x2="80.6" y2="234" class="muted-stroke" stroke-width="1"/><line x1="131.2" y1="182" x2="114.4" y2="234" class="accent-stroke" stroke-width="2.4"/><line x1="131.2" y1="182" x2="148.1" y2="234" class="muted-stroke" stroke-width="1"/><line x1="198.8" y1="182" x2="181.9" y2="234" class="muted-stroke" stroke-width="1"/><line x1="198.8" y1="182" x2="215.6" y2="234" class="muted-stroke" stroke-width="1"/><line x1="266.2" y1="182" x2="249.4" y2="234" class="muted-stroke" stroke-width="1"/><line x1="266.2" y1="182" x2="283.1" y2="234" class="muted-stroke" stroke-width="1"/><line x1="333.8" y1="182" x2="316.9" y2="234" class="accent-stroke" stroke-width="2.4"/><line x1="333.8" y1="182" x2="350.6" y2="234" class="muted-stroke" stroke-width="1"/><line x1="401.2" y1="182" x2="384.4" y2="234" class="accent-stroke" stroke-width="2.4"/><line x1="401.2" y1="182" x2="418.1" y2="234" class="muted-stroke" stroke-width="1"/><line x1="468.8" y1="182" x2="451.9" y2="234" class="muted-stroke" stroke-width="1"/><line x1="468.8" y1="182" x2="485.6" y2="234" class="muted-stroke" stroke-width="1"/><line x1="536.2" y1="182" x2="519.4" y2="234" class="muted-stroke" stroke-width="1"/><line x1="536.2" y1="182" x2="553.1" y2="234" class="muted-stroke" stroke-width="1"/><circle cx="300.0" cy="26" r="5.5" class="accent-fill"/><circle cx="165.0" cy="78" r="2.5" class="muted-fill"/><circle cx="435.0" cy="78" r="2.5" class="muted-fill"/><circle cx="97.5" cy="130" r="5.5" class="accent-fill"/><rect x="227.5" y="125" width="10" height="10" class="node"/><circle cx="367.5" cy="130" r="5.5" class="accent-fill"/><circle cx="502.5" cy="130" r="2.5" class="muted-fill"/><circle cx="63.8" cy="182" r="2.5" class="muted-fill"/><circle cx="131.2" cy="182" r="2.5" class="muted-fill"/><circle cx="198.8" cy="182" r="2.5" class="muted-fill"/><circle cx="266.2" cy="182" r="2.5" class="muted-fill"/><circle cx="333.8" cy="182" r="2.5" class="muted-fill"/><circle cx="401.2" cy="182" r="2.5" class="muted-fill"/><circle cx="468.8" cy="182" r="2.5" class="muted-fill"/><circle cx="536.2" cy="182" r="2.5" class="muted-fill"/><circle cx="46.9" cy="234" r="5.5" class="accent-fill"/><rect x="75.6" y="229" width="10" height="10" class="node"/><circle cx="114.4" cy="234" r="5.5" class="accent-fill"/><circle cx="148.1" cy="234" r="2.5" class="muted-fill"/><circle cx="181.9" cy="234" r="2.5" class="muted-fill"/><circle cx="215.6" cy="234" r="2.5" class="muted-fill"/><circle cx="249.4" cy="234" r="2.5" class="muted-fill"/><circle cx="283.1" cy="234" r="2.5" class="muted-fill"/><circle cx="316.9" cy="234" r="5.5" class="accent-fill"/><rect x="345.6" y="229" width="10" height="10" class="node"/><circle cx="384.4" cy="234" r="5.5" class="accent-fill"/><circle cx="418.1" cy="234" r="2.5" class="muted-fill"/><circle cx="451.9" cy="234" r="2.5" class="muted-fill"/><circle cx="485.6" cy="234" r="2.5" class="muted-fill"/><circle cx="519.4" cy="234" r="2.5" class="muted-fill"/><circle cx="553.1" cy="234" r="2.5" class="muted-fill"/><text x="309.0" y="19" class="math" font-size="13">R<tspan class="mrm">(ε)</tspan></text><text x="106.5" y="123" class="math" font-size="13">R<tspan class="mrm">(0)</tspan></text><text x="80.6" y="256" text-anchor="middle" class="math" font-size="14">τ<tspan class="mrm" font-size="9" dy="4">₀</tspan></text><text x="232.5" y="152" text-anchor="middle" class="math" font-size="14">τ<tspan class="mrm" font-size="9" dy="4">ε</tspan></text><text x="376.5" y="123" class="math" font-size="13">R<tspan class="mrm">(1)</tspan></text><text x="350.6" y="256" text-anchor="middle" class="math" font-size="14">τ<tspan class="mrm" font-size="9" dy="4">₁</tspan></text><circle cx="40" cy="296" r="5" class="accent-fill"/><text x="52" y="300" class="label">nodes R(ρ) = T(ρ(0) 0 ρ(1) 0 …), |ρ| ≤ 2</text><rect x="335" y="291" width="10" height="10" class="node"/><text x="352" y="300" class="label">τ<tspan font-size="9" dy="3">ρ</tspan><tspan dy="-3"> = T(… 0 1): no path of R extends it</tspan></text></svg>
:::

With $X = \emptyset'$, sufficiently generic Sacks sets are not generalized low, in contrast with 1-generic sets. The theorem fails for Jockusch–Soare forcing, since a sufficiently generic set may be computable (:ref{#ex-generic-notions}); Monin and Patey discuss, in exercises, restrictions of Jockusch–Soare forcing for which an analogue holds or fails.

:::quiz[Sacks generic sets and the jump]
In the proof of :ref{#thm-sacks-not-gl1}, why is the subtree $R$ built from $T$ by inserting a $0$ after each bit, rather than taken equal to $T$?

- [x] So that above every node of $R$ some node of $T$ escapes $[R]$: the extension can then make $G'(a) = 1$ while keeping a prefix that fixed the computation.
- [ ] So that $[R]$ is a $\Pi^0_1$ class.

  $[T]$ is also a $\Pi^0_1$ class; what matters is the room left between $[R]$ and $[T]$.
- [ ] So that $R$ is computable.

  $T$ is computable as well.

---

Why does the proof not need to know which case holds?

- [x] Because it only shows that an extension with the required property exists, which is what density asks; finding it effectively would need the oracle $X$ and more.
- [ ] Because the first case never holds.

  It may hold, for instance for a functional that never converges.
- [ ] Because $X$ decides it.

  Deciding it needs to know whether some node makes a computation relative to $X$ converge, which is $\Sigma^0_1(X)$, not $X$-computable.
:::

## Notes and references

Spector (1956) built a minimal degree by function trees; Miller and Martin (1968) adapted the method to build a non-computable computably dominated set. The reformulation of both constructions in terms of Sacks forcing, and the theorem that Sacks generic sets are not generalized low, are from the chapter *Effective forcing* of Monin and Patey (section *Forcing with trees*, and the theorem on the continuity of the Turing jump); the proof here follows theirs, with the subtree $R$ made explicit. Monin and Patey also show, in an exercise, that Sacks generic sets are computably traceable; computable traceability is due to Terwijn and Zambella (2001). Soare (Chapter 12) presents Spector's construction.

- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- W. Miller and D. A. Martin, *The degrees of hyperimmune sets*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 14 (1968), 159–166.
- S. A. Terwijn and D. Zambella, *Computational randomness and lowness*, Journal of Symbolic Logic 66 (2001), 1199–1205.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Chapter 12.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Forcing with trees* and subsection *Forcing Σ⁰₁/Π⁰₁ requirements*.

:::::exercises
::::exercise{#ex-js-fails-sacks-properties difficulty=1 objective="See that the properties of Sacks generic sets fail for Jockusch–Soare forcing."}
Show that the conclusion of :ref{#thm-sacks-not-gl1} fails for Jockusch–Soare forcing, and that :ref{#prop-sacks-generic} fails for it as well.

:::solution
Let $Y$ be computable. Every filter containing the condition $\{ Y \}$ determines $Y$, and a filter generic for any countable family of dense sets can contain $\{ Y \}$, by :ref{#lem-rasiowa-sikorski}. Then $G = Y$ satisfies $G' \equiv_T \emptyset' \leq_T G \oplus \emptyset'$, and $G$ is computable, so it is not of minimal degree.
:::
::::

::::exercise{#ex-sacks-cone-avoidance difficulty=1 objective="Prove cone avoidance for computable Sacks forcing by a splitting dichotomy."}
Let $A$ be a non-computable set. Show directly that every sufficiently generic set $G$ for computable Sacks forcing satisfies $A \not\leq_T G$.

:::solution
Fix $e$ and a condition $T$. We find $S \leq T$ such that $\Phi^X_e \neq A$ for every path $X$ of $S$.

*Case 1: there are $n$ and nodes $\tau_0, \tau_1$ of $T$ with $\Phi^{\tau_0}_e(n)\converge \neq \Phi^{\tau_1}_e(n)\converge$.* One of the two values, say that of $\tau_i$, differs from $A(n)$. Let $S$ be the full subtree above $\tau_i$. Every path $X$ of $S$ extends $\tau_i$, so $\Phi^X_e(n) = \Phi^{\tau_i}_e(n) \neq A(n)$.

*Case 2: otherwise.* For each $n$, all the nodes of $T$ on which $\Phi_e(n)$ converges give the same value. Let $\psi(n)$ be the value given by the first node found on which $\Phi_e(n)$ converges, a partial computable function. Let $S = T$, and let $X$ be a path with $\Phi^X_e$ total. For each $n$, the computation $\Phi^X_e(n)$ converges with some use $u$, and a node of $T$ that is a prefix of $X$ of length at least $u$ gives the same value, so $\Phi^X_e(n) = \psi(n)$. Hence $\Phi^X_e = \psi$ is computable, and differs from $A$.

In both cases, the set of conditions all of whose paths $X$ satisfy $\Phi^X_e \neq A$ is dense. A set generic for these sets, for every $e$, does not compute $A$. Adapted from Monin and Patey, chapter *Effective forcing*, section *Forcing with trees*. The statement is also the case $n = 0$ of the general preservation result of the lesson on the forcing question.
:::
::::

::::exercise{#ex-sacks-not-low difficulty=1 objective="Draw consequences of the failure of generalized lowness for Sacks generic sets."}
Show that every sufficiently generic set $G$ for computable Sacks forcing is not low, and that a single sufficiently generic set satisfies $G' \not\leq_T G \oplus \emptyset^{(n)}$ for every $n$. Compare with a 1-generic set computable in $\emptyset'$.

:::solution
If $G$ were low, then $G' \leq_T \emptyset' \leq_T G \oplus \emptyset'$, contradicting :ref{#thm-sacks-not-gl1} with $X = \emptyset'$. For each $n$, the theorem with $X = \emptyset^{(n)}$ gives a countable family $\mathcal D_n$ of dense sets; a set generic for the countable family $\bigcup_n \mathcal D_n$ satisfies $G' \not\leq_T G \oplus \emptyset^{(n)}$ for every $n$. By contrast, a 1-generic set $G \leq_T \emptyset'$, which exists by :ref{#thm-low-generic-exists}, satisfies $G' \leq_T G \oplus \emptyset' \equiv_T \emptyset'$ (:ref{#cor-cohen-jumps}), so it is low.
:::
::::

::::exercise{#ex-sacks-not-1-generic difficulty=2 objective="Separate Sacks generic sets from Cohen generic sets with the escape nodes of the non-GL₁ proof."}
1. Let $S$ be a computable f-tree. Show that for every string $\sigma$, $[\sigma] \cap [S] = \emptyset$ if and only if $\sigma$ is not a prefix of any node $S(\rho)$ with $|\rho| = |\sigma|$. Deduce that the set $W_S$ of strings $\sigma$ with $[\sigma] \cap [S] = \emptyset$ is computable.
2. Show that every sufficiently generic set $G$ for computable Sacks forcing is not 1-generic, that is, there is a c.e. set of strings $W$ such that no prefix of $G$ belongs to $W$ and every prefix of $G$ has an extension in $W$.

:::solution
1. Recall that $|S(\rho)| \geq |\rho|$, since the nodes strictly increase along a string. If $X \in [S] \cap [\sigma]$, some node $S(\rho)$ with $|\rho| = |\sigma|$ is a prefix of $X$, as shown after :ref{#def-function-tree}; both $\sigma$ and $S(\rho)$ are prefixes of $X$ and $|S(\rho)| \geq |\sigma|$, so $\sigma \preceq S(\rho)$. Conversely, if $\sigma \preceq S(\rho)$, the set $\bigcup_j S(\rho 0^j)$ is a path of $S$ extending $\sigma$. The condition of the statement involves the $2^{|\sigma|}$ computable nodes $S(\rho)$, so $W_S$ is computable.
2. Let $T$ be a condition, and $R$ the subtree $R(\rho) = T(\hat\rho)$ of the proof of :ref{#thm-sacks-not-gl1}. Every string $\sigma$ has an extension in $W_R$. If $\sigma \in W_R$, this is $\sigma$. Otherwise, by item 1, $\sigma \preceq R(\rho)$ for some $\rho$ with $|\rho| = |\sigma|$, and the escape node $\tau_\rho = T(\hat\rho\, 0 1)$ extends $R(\rho)$; no path of $R$ extends $\tau_\rho$, as shown in that proof, so $\tau_\rho \in W_R$. Hence the set of conditions $S$ such that every string has an extension in $W_S$ is dense, since it contains $R \leq T$.

   Let $G$ be generic for this dense set, and $S$ a condition of the generic filter in it. Then $G \in [S]$, so no prefix of $G$ belongs to $W_S$; and every prefix of $G$ has an extension in $W_S$. The set $W_S$ is computable, hence c.e., so $G$ is not 1-generic.
:::
::::

::::exercise{#ex-sacks-traceable-bound difficulty=3 objective="Refine the trace construction for Sacks generic sets to an arbitrary slow-growing bound."}
Let $h$ be a computable nondecreasing unbounded function with $h(0) \geq 1$. Show that every sufficiently generic set $G$ for computable Sacks forcing is computably traceable with bound $h$: for every total $G$-computable function $f$ there is a computable sequence $(T_n)$ of finite sets, given by canonical indices, with $|T_n| \leq h(n)$ and $f(n) \in T_n$ for every $n$.

:::solution
Let $\ell(n)$ be the largest $k$ with $2^k \leq h(n)$; it exists since $h(n) \geq 1$, and $\ell$ is computable, nondecreasing and unbounded. For each $k$, the set $N_k = \{ n : \ell(n) = k \}$ is finite, and computable uniformly in $k$: compute $\ell(0), \ell(1), \dots$ until a value larger than $k$ appears.

Fix $e$ and a condition $T$.

*Case 1: some node $\sigma$ of $T$ and some $x$ have no node $\tau \succeq \sigma$ of $T$ with $\Phi^\tau_e(x)\converge$.* As in Case 1 of :ref{#lem-ftree-domination}, the full subtree above $\sigma$ is an extension on all paths of which $\Phi_e(x)$ diverges.

*Case 2: otherwise.* Then for every node $\sigma$ of $T$ and every finite set $N$, some node $\tau \succeq \sigma$ of $T$ satisfies $\Phi^\tau_e(n)\converge$ for every $n \in N$: find a node converging at the first element of $N$, then a node above it converging at the second, and so on; a computation that converges on a string still converges on its extensions. Define $S(\rho) = T(\mu_\rho)$, where $\mu_\varepsilon$ is the first string found with $\Phi^{T(\mu)}_e(n)\converge$ for all $n \in N_0$, and $\mu_{\rho i}$ is the first $\mu \succeq \mu_\rho\, i$ found with $\Phi^{T(\mu)}_e(n)\converge$ for all $n \in N_{|\rho| + 1}$. The searches terminate, since the nodes of $T$ above $T(\mu_\rho\, i)$ are the strings $T(\mu)$ with $\mu \succeq \mu_\rho\, i$. As in :ref{#lem-ftree-domination}, $S$ is a computable subtree of $T$, and $\Phi^{S(\rho)}_e(n)\converge$ whenever $\ell(n) = |\rho|$. Let
$$
T_n = \{ \Phi^{S(\rho)}_e(n) : |\rho| = \ell(n) \},
$$
computable from $n$, with $|T_n| \leq 2^{\ell(n)} \leq h(n)$. For a path $X$ of $S$ and $n \in \nat$, some $\rho$ of length $\ell(n)$ has $S(\rho) \prec X$, so $\Phi^X_e(n) = \Phi^{S(\rho)}_e(n) \in T_n$.

So for each $e$, the set of conditions $S$ such that either $\Phi^X_e$ is partial for every path $X$, or some computable sequence $(T_n)$ with $|T_n| \leq h(n)$ satisfies $\Phi^X_e(n) \in T_n$ for every path $X$ and every $n$, is dense. If $G$ is generic for these sets and $f = \Phi^G_e$ is total, $G$ is a path of a condition of the second kind, and $f$ is traced. Monin and Patey derive this from :ref{#ex-sacks-traceable} and a theorem of Terwijn and Zambella on changing the bound; the direct construction here avoids it.
:::
::::
:::::
