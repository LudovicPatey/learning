---
title: Perfect forcing and a minimal hyperdegree
summary: Forcing with hyperarithmetic perfect classes over the ramified analytic hierarchy; the fusion lemma; generic sets satisfy Δ¹₁ comprehension and have minimal hyperdegree (Gandy, Sacks).
duration: 45
prerequisites: [cohen-forcing, effective-forcing/sacks-forcing]
---

Spector built a minimal Turing degree by forcing with perfect trees: a sequence of perfect trees, each refining the previous one, decides for every Turing functional whether it is constant or injective on the paths. Gandy and Sacks lifted the construction to hyperdegrees. The conditions are perfect classes with a hyperarithmetic code, the statements to decide are the sentences of the ramified analytic hierarchy, and the main tool is a **fusion lemma**: infinitely many requirements, given by a hyperarithmetic list of existential sentences, can be met by a single hyperarithmetic perfect class. The fusion lemma is the reason why the generic set preserves $\omega_1^{\mathrm{CK}}$, and why every set hyperarithmetic in it is either hyperarithmetic or computes it, up to a hyperarithmetic set.

The lesson follows Sacks (Sections IV.4 and IV.5), with the notion of genericity of Chong and Yu (Section 5.3), defined by dense sets arithmetic in $\mathcal O$.

## Conditions and forcing

A **condition** is a perfect class $P \subseteq \cs$, the class of paths of a perfect tree, whose tree is hyperarithmetic. A condition is given by an **index** $(b, e)$, with $b \in \mathcal O$ and $\Phi^{H_b}_e$ the characteristic function of the tree; the set of indices is $\Pi^1_1$. A condition $Q$ **extends** $P$ if $Q \subseteq P$. For a node $\sigma$ of the tree of $P$, the class $P \cap [\sigma]$ is again a condition.

:::definition[Gandy, Sacks]{#def-perfect-forcing-hyp}
The relation $P \Vdash \varphi$, for conditions $P$ and sentences $\varphi$ of $\mathcal L(\omega_1^{\mathrm{CK}}, \mathcal T)$, is defined by:

1. if $\varphi$ is ranked, $P \Vdash \varphi$ if $\mathcal M(\omega_1^{\mathrm{CK}}, X) \models \varphi$ for every $X \in P$;
2. if $\varphi(Y^\alpha)$ is unranked, $P \Vdash (\exists Y^\alpha)\varphi(Y^\alpha)$ if $P \Vdash \varphi(x_\theta)$ for some $\theta$ of rank at most $\alpha$;
3. $P \Vdash (\exists Y)\varphi(Y)$ if $P \Vdash (\exists Y^\alpha)\varphi(Y^\alpha)$ for some $\alpha < \omega_1^{\mathrm{CK}}$;
4. if $\varphi(x)$ is unranked, $P \Vdash (\exists x)\varphi(x)$ if $P \Vdash \varphi(n)$ for some $n$;
5. if $\varphi \wedge \psi$ is unranked, $P \Vdash \varphi \wedge \psi$ if $P$ forces both;
6. if $\varphi$ is unranked, $P \Vdash \neg\varphi$ if no $Q \subseteq P$ forces $\varphi$.
:::

Clause 1 treats every ranked sentence at once, by truth along the whole class; the other clauses handle unranked sentences as in Cohen forcing. By clause 1 and :ref{#lem-ramified-truth}, the relation "$P \Vdash \varphi$", restricted to existential sentences, is $\Pi^1_1$: for a ranked $\varphi$, it reads $(\forall X)(X \notin P \vee \varphi \text{ is true in } \mathcal M(\omega_1^{\mathrm{CK}}, X))$. By induction on the clauses, if $P \Vdash \varphi$ and $Q \subseteq P$, then $Q \Vdash \varphi$.

## The fusion lemma

:::lemma[Fusion; Gandy, Sacks]{#lem-hyp-fusion}
Let $(\varphi_i)_{i \in \nat}$ be a hyperarithmetic sequence of existential sentences, and $P$ a condition such that for every $i$ and every condition $Q \subseteq P$, some condition $R \subseteq Q$ forces $\varphi_i$. Then some condition $Q \subseteq P$ forces every $\varphi_i$.
:::

:::proof{of=lem-hyp-fusion}
*A hyperarithmetic selection.* The relation between $(Q, i)$ and $R$ expressed by "$R \subseteq Q$ and $R \Vdash \varphi_i$", on indices of conditions, is $\Pi^1_1$: inclusion between hyperarithmetic perfect classes is a $\Delta^1_1$ condition on their indices, and forcing is $\Pi^1_1$. By Kreisel's uniformization (:ref{#thm-kreisel-uniformization}), it is uniformized by a $\Pi^1_1$ partial function $F(Q, i)$, defined whenever $Q \subseteq P$.

*A fusion sequence.* Define conditions $Q_{i,j}$, for $i \in \nat$ and $j < 2^i$, by recursion on $i$: $Q_{0,0} = P$; given $Q_{i,j}$, choose the first two incompatible nodes $\sigma_0, \sigma_1$ of the tree of $Q_{i,j}$ of length at least $i$, and let $Q_{i+1, 2j + k} = F(Q_{i,j} \cap [\sigma_k], i)$ for $k < 2$. So $Q_{i+1, 2j}$ and $Q_{i+1, 2j+1}$ are disjoint subclasses of $Q_{i,j}$, the first $i$ bits of their members are fixed, and they force $\varphi_i$. The sequence of indices is defined by iterating a $\Pi^1_1$ partial function; since it is total, its graph is $\Pi^1_1$ (a value is correct if there is a finite sequence of correct steps leading to it), and a total function with a $\Pi^1_1$ graph is hyperarithmetic.

*The limit.* Let $Q = \bigcap_i \bigcup_{j < 2^i} Q_{i,j}$. It is a perfect class: each of its members lies in a unique $Q_{i,j}$ for each $i$, and the splitting at each level gives continuum many members, with a hyperarithmetic tree, computable from the hyperarithmetic sequence. So $Q$ is a condition, $Q \subseteq P$. Fix $i$ and write $\varphi_i$ as $(\exists Y_1) \cdots (\exists Y_k)\psi$ with $\psi$ ranked, or as a ranked sentence. Each $Q_{i+1, j}$ forces $\varphi_i$, so by clauses 2 and 3 and clause 1, every member $X$ of $Q_{i+1, j}$ satisfies, in $\mathcal M(\omega_1^{\mathrm{CK}}, X)$, a ranked instance of $\varphi_i$ with ranks at most some $\alpha_j < \omega_1^{\mathrm{CK}}$. With $\alpha = \max_{j < 2^{i+1}} \alpha_j$, every member $X$ of $Q$, which lies in some $Q_{i+1, j}$, satisfies the ranked sentence $(\exists Y_1^\alpha)\cdots(\exists Y_k^\alpha)\psi$. By clause 1, $Q$ forces it, and by clause 3, $Q \Vdash \varphi_i$.
:::

:::lemma{#lem-perfect-decide}
For every sentence $\varphi$ and condition $P$, some condition $Q \subseteq P$ forces $\varphi$ or forces $\neg\varphi$.
:::

:::proof{of=lem-perfect-decide}
For an unranked $\varphi$, this follows from clause 6. For a ranked $\varphi$, we show by induction on full ordinal rank and logical complexity that some $Q \subseteq P$ has all its members satisfying $\varphi$ in $\mathcal M(\omega_1^{\mathrm{CK}}, X)$, or all satisfying $\neg\varphi$. For an atomic $t \in \mathcal T$, take $Q = P \cap [\sigma]$ for a node $\sigma$ of the tree of $P$ longer than the value of $t$. Negation is immediate, and conjunction follows by applying the induction hypothesis twice. For $(\exists Y^\alpha)\psi(Y^\alpha)$: let $\theta_0, \theta_1, \dots$ be a hyperarithmetic list of the formulas of rank at most $\alpha$ with one free number variable. If some $Q \subseteq P$ and $i$ have all members of $Q$ satisfying $\psi(x_{\theta_i})$, then all satisfy $(\exists Y^\alpha)\psi$. Otherwise, by the induction hypothesis applied to the sentences $\psi(x_{\theta_i})$, of smaller full rank, every $Q \subseteq P$ has an extension all of whose members satisfy $\neg\psi(x_{\theta_i})$, that is, which forces this ranked sentence; by :ref{#lem-hyp-fusion}, some $Q \subseteq P$ forces all of them, and all its members satisfy $\neg(\exists Y^\alpha)\psi$. Number quantifiers are treated in the same way, with the sentences $\psi(n)$. (Sacks, Lemma IV.4.4.)
:::

## Generic sets

A set $D$ of conditions is **dense** if every condition has an extension in $D$. A set $T$ is **generic** if for every dense set $D$ of conditions whose set of indices is arithmetic in $\mathcal O$, there is $P \in D$ with $T \in P$.

For each sentence $\varphi$, the set $D_\varphi$ of conditions that force $\varphi$ or $\neg\varphi$ is dense by :ref{#lem-perfect-decide}, and arithmetic in $\mathcal O$: for ranked or existential sentences, forcing is $\Pi^1_1$, and each unranked negation or quantifier adds a number quantifier over indices of conditions or over notations. There are countably many dense sets arithmetic in $\mathcal O$; meeting them one after the other along a decreasing sequence of conditions, whose intersection is non-empty by compactness, gives a generic set inside every condition.

:::lemma[Forcing equals truth]{#lem-perfect-truth}
Let $T$ be generic. For every sentence $\varphi$, $\mathcal M(\omega_1^{\mathrm{CK}}, T) \models \varphi$ if and only if $T \in P$ for some condition $P \Vdash \varphi$.
:::

:::proof{of=lem-perfect-truth}
For a ranked $\varphi$: if $T \in P \Vdash \varphi$, then $\varphi$ holds in $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ by clause 1. Conversely, $T$ meets $D_\varphi$, and a condition containing $T$ that forced $\neg\varphi$ would make $\neg\varphi$ true; so it forces $\varphi$.

A preliminary fact: if $T \in P \cap Q$ for conditions $P$ and $Q$, then $T \in R \subseteq P \cap Q$ for some condition $R$. Indeed, membership in the hyperarithmetic classes $P$ and $Q$ is expressed by a ranked sentence $\chi$, using :ref{#lem-h-ranked} to define their trees; $\chi$ is true of $T$, so some condition $R \ni T$ forces $\chi$, and all members of $R$ belong to $P \cap Q$.

For unranked sentences, proceed by induction on logical complexity. The existential clauses follow from the induction hypothesis and the definitions. For a conjunction, if $T \in P \Vdash \varphi$ and $T \in Q \Vdash \psi$, the preliminary fact gives $R \ni T$ inside both, which forces both. For a negation: if $T \in P \Vdash \neg\varphi$ and $\varphi$ were true, some $Q \ni T$ would force $\varphi$, and a condition $R \ni T$ inside $P \cap Q$ would force $\varphi$, contradicting $P \Vdash \neg\varphi$. If $\neg\varphi$ is true, $T$ meets $D_\varphi$ in a condition that cannot force $\varphi$ by the induction hypothesis, so it forces $\neg\varphi$. (Sacks, Proposition IV.4.6 and Lemma IV.4.8.)
:::

:::theorem[Gandy, Sacks]{#thm-perfect-comprehension}
If $T$ is generic, then $\mathcal M(\omega_1^{\mathrm{CK}}, T)$ satisfies $\Delta^1_1$ comprehension. Consequently $\omega_1^T = \omega_1^{\mathrm{CK}}$ and $\mathcal M(\omega_1^{\mathrm{CK}}, T) = \mathrm{HYP}(T)$.
:::

:::proof{of=thm-perfect-comprehension}
As in the proof of :ref{#thm-feferman}, it suffices to show: if $\mathcal M(\omega_1^{\mathrm{CK}}, T) \models (\forall x)(\exists Y) C(x, Y)$ for an arithmetic $C$ with parameters, then $\mathcal M(\omega_1^{\mathrm{CK}}, T) \models (\forall x)(\exists Y^\gamma) C(x, Y^\gamma)$ for some $\gamma < \omega_1^{\mathrm{CK}}$. Let $D$ be the set of conditions that force $\neg(\forall x)(\exists Y) C(x, Y)$, or force $(\forall x)(\exists Y^\gamma) C(x, Y^\gamma)$ for some $\gamma < \omega_1^{\mathrm{CK}}$. It is arithmetic in $\mathcal O$.

*$D$ is dense.* Let $P$ be a condition. By :ref{#lem-perfect-decide}, some $Q \subseteq P$ forces $(\forall x)(\exists Y) C(x, Y)$ or its negation; in the second case $Q \in D$. In the first case, unfolding clause 6 as in the proof of :ref{#thm-feferman}, every $R \subseteq Q$ has, for each $n$, an extension forcing $(\exists Y) C(n, Y)$. By :ref{#lem-hyp-fusion}, some $S \subseteq Q$ forces all these sentences. The relation "$a \in \mathcal O_1$ and $S \Vdash (\exists Y^{|a|}) C(n, Y^{|a|})$" between $n$ and $a$ is $\Pi^1_1$ and total in $n$; Kreisel's uniformization gives a hyperarithmetic choice of $a(n)$, and Spector's boundedness theorem a bound $\gamma$ on $|a(n)|$. Every member $X$ of $S$ then satisfies the ranked sentence $(\forall x)(\exists Y^\gamma) C(x, Y^\gamma)$, so $S$ forces it by clause 1, and $S \in D$.

Since $T$ is generic, $T \in S$ for some $S \in D$. By :ref{#lem-perfect-truth}, $S$ cannot force $\neg(\forall x)(\exists Y) C(x, Y)$, which is false; so $\mathcal M(\omega_1^{\mathrm{CK}}, T) \models (\forall x)(\exists Y^\gamma) C(x, Y^\gamma)$. The consequences follow from :ref{#thm-ramified-comprehension}.
:::

## Minimality

For a ranked formula $\theta(x)$ and a set $X$, write $\theta^X = \{ n : \mathcal M(\omega_1^{\mathrm{CK}}, X) \models \theta(n) \}$. For a generic $T$, the sets $\theta^T$ are exactly the sets hyperarithmetic in $T$, by :ref{#thm-perfect-comprehension}. The next lemma is the hyperarithmetic version of Spector's dichotomy: on a smaller condition, the map $X \mapsto \theta^X$ is either constant or invertible.

:::lemma[Gandy, Sacks]{#lem-constant-or-injective}
For every condition $P$ and ranked formula $\theta(x)$, there are a condition $Q \subseteq P$ and a hyperarithmetic set $H$ such that either $\theta^X = H$ for every $X \in Q$, or $X \leq_T \theta^X \oplus H$ for every $X \in Q$, by a fixed reduction.
:::

:::proof{of=lem-constant-or-injective}
*Case I: there is $R \subseteq P$ such that no two conditions $Q_0, Q_1 \subseteq R$ force $\theta(n)$ and $\neg\theta(n)$ respectively, for any $n$.* Let $H = \{ n : \text{some } Q \subseteq R \text{ forces } \theta(n) \}$. By :ref{#lem-perfect-decide}, every $n$ has some $Q \subseteq R$ forcing $\theta(n)$ or $\neg\theta(n)$, and by the case hypothesis, $n \notin H$ if and only if some $Q \subseteq R$ forces $\neg\theta(n)$. Both definitions are $\Pi^1_1$, so $H$ is hyperarithmetic. The sentences "$\theta(n)$ if $n \in H$, $\neg\theta(n)$ if $n \notin H$" form a hyperarithmetic sequence, and every condition below $R$ has an extension forcing each of them; by :ref{#lem-hyp-fusion}, some $Q \subseteq R$ forces all of them, and $\theta^X = H$ for every $X \in Q$.

*Case II: otherwise.* Every $R \subseteq P$ has conditions $Q_0, Q_1 \subseteq R$ and $n$ with $Q_0 \Vdash \theta(n)$ and $Q_1 \Vdash \neg\theta(n)$; such $Q_0$ and $Q_1$ are disjoint. As in the proof of :ref{#lem-hyp-fusion}, a hyperarithmetic choice of $Q_0$, $Q_1$ and $n$ gives a hyperarithmetic family of conditions $Q_{i,j}$, $j < 2^i$, and numbers $f(i, j)$, with $Q_{i+1, 2j} \Vdash \theta(f(i, j))$, $Q_{i+1, 2j+1} \Vdash \neg\theta(f(i, j))$, both inside $Q_{i,j}$, the first $i$ bits of members of $Q_{i,j}$ being fixed. Let $Q = \bigcap_i \bigcup_j Q_{i,j}$ and $H$ a hyperarithmetic set coding the family and $f$. For $X \in Q$, let $t(i)$ be the $j$ with $X \in Q_{i,j}$; then $t(0) = 0$ and $t(i+1) = 2t(i)$ if $f(i, t(i)) \in \theta^X$, and $2t(i) + 1$ otherwise. So $t$ is computable in $\theta^X \oplus H$, and so is $X$, whose first $i$ bits are fixed by $Q_{i, t(i)}$.
:::

:::theorem[Gandy, Sacks]{#thm-minimal-hyperdegree}
Every generic set $T$ has minimal hyperdegree: $T$ is not hyperarithmetic, and every set $Y \leq_h T$ is hyperarithmetic or satisfies $T \leq_h Y$.
:::

:::proof{of=thm-minimal-hyperdegree}
$T$ is not hyperarithmetic (:ref{#ex-perfect-generic-not-hyp}). Let $Y \leq_h T$. By :ref{#thm-perfect-comprehension}, $Y = \theta^T$ for some ranked formula $\theta$. Let $D_\theta$ be the set of conditions $Q$ for which, for some hyperarithmetic $H$ and index $e$, either $\theta^X = H$ for all $X \in Q$, or $\Phi^{\theta^X \oplus H}_e = X$ for all $X \in Q$. It is dense by :ref{#lem-constant-or-injective}, and arithmetic in $\mathcal O$: the conditions on $Q$, $H$ and $e$ are $\Pi^1_1$, and the existential quantifiers range over indices. Since $T$ is generic, $T \in Q$ for some $Q \in D_\theta$. In the first case $Y = \theta^T = H$ is hyperarithmetic; in the second, $T \leq_T Y \oplus H$, so $T \leq_h Y$.
:::

:::quiz[the minimal hyperdegree]
In the proof of :ref{#lem-constant-or-injective}, where is the fusion lemma used?

- [x] In both cases: to find a single condition that forces $\theta(n)$ or its negation correctly for all $n$ at once in case I, and to build the splitting family in case II, whose limit must be a hyperarithmetic perfect class.
- [ ] Only to show that $H$ is hyperarithmetic.

  $H$ is hyperarithmetic because it and its complement are $\Pi^1_1$; fusion is used for the conditions.
- [ ] To show that generic sets exist.

  Existence only uses countably many dense sets and compactness.

---

Why is genericity defined with dense sets arithmetic in $\mathcal O$, rather than with all dense sets?

- [x] Because there are uncountably many sets of conditions but only countably many arithmetic in $\mathcal O$; meeting all dense sets would be impossible, while the dense sets needed in the proofs, such as $D_\varphi$ and $D_\theta$, are arithmetic in $\mathcal O$.
- [ ] Because conditions are hyperarithmetic.

  Conditions being hyperarithmetic makes the sets of indices definable, but does not bound the number of dense sets.
- [ ] To make the generic set computable in $\mathcal O$.

  A generic set is not computable in $\mathcal O$ in general; it is computable in a set arithmetic in $\mathcal O$, a different statement.
:::

::::exercise[Generic sets are not hyperarithmetic]{#ex-perfect-generic-not-hyp difficulty=1 objective="Show with a dense set that perfect generic sets avoid the hyperarithmetic sets."}
Show that no generic set, in the sense of perfect forcing, is hyperarithmetic.

:::solution
For a hyperarithmetic set $H$, let $D_H$ be the set of conditions that do not contain $H$. It is dense: a condition $P$ is perfect, so its tree has a node $\sigma$ that $H$ does not extend, and $P \cap [\sigma] \in D_H$. It is arithmetic in $\mathcal O$, since membership of $H$ in a condition is a $\Delta^1_1$ condition on the index of the condition, given an index of $H$. A generic $T$ meets $D_H$: $T \in Q$ for a condition $Q$ with $H \notin Q$, so $T \neq H$. This holds for every hyperarithmetic $H$.
:::
::::

## Notes and references

Gandy and Sacks (1967) constructed a set of minimal hyperdegree by perfect forcing over the hyperarithmetic hierarchy; Sacks (Sections IV.4 and IV.5: subsection 4.1, Lemmas 4.2–4.4, Proposition 4.6, Lemma 4.8, Theorems 5.3–5.6) is followed here, except that genericity is defined by dense sets arithmetic in $\mathcal O$, as in Chong and Yu (Section 5.3), which Sacks proves equivalent to his definition (Theorem IV.5.3). Simpson (1975) showed that there is an uncountable $\Sigma^1_1$ class of sets of minimal hyperdegree (Chong–Yu, Theorem 5.3.12).

- R. O. Gandy and G. E. Sacks, *A minimal hyperdegree*, Fundamenta Mathematicae 61 (1967), 215–223.
- C. Spector, *On degrees of recursive unsolvability*, Annals of Mathematics 64 (1956), 581–592.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Sections IV.4 and IV.5.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Section 5.3.

:::::exercises
::::exercise{#ex-generic-closed-hyp difficulty=2 objective="Compare the generic sets with the sets of the same hyperdegree."}
Let $T$ be generic for perfect forcing and $S \equiv_h T$. Show that $S$ has minimal hyperdegree, and that $\omega_1^S = \omega_1^{\mathrm{CK}}$.

:::solution
Minimality is a property of the hyperdegree: if $Y \leq_h S$, then $Y \leq_h T$, so $Y$ is hyperarithmetic or $T \leq_h Y$, and then $S \leq_h T \leq_h Y$. And $S$ is not hyperarithmetic, since $T \leq_h S$ and $T$ is not. By :ref{#cor-h-omega1}, $\omega_1^S = \omega_1^T$, which is $\omega_1^{\mathrm{CK}}$ by :ref{#thm-perfect-comprehension}. (Sacks, Exercise IV.4.12, shows that $S$ is itself generic.)
:::
::::
:::::
