---
title: Weak merging and Liu's lemma
summary: Forcing questions that can only merge two of several negative answers; finite valuations and Liu's combinatorial lemma, which makes the third case of the PA avoidance argument non-trivial; the abstract theorem for weakly merging questions, and its disjunctive version for problems with two sides.
duration: 45
prerequisites: [pa-avoidance, avoidance/disjunctive-question]
---

The merging property of the previous lesson fails for the forcing questions that matter most for Ramsey-type problems. A disjunctive question (:ref{#def-disjunctive-notion}) builds one set on each side, and a negative answer yields an extension that forces a negation on **one** side, chosen by the construction, not by us. Given two negative answers, the two negations may be forced on different sides, and neither side is then forced to be partial. With three negative answers, however, two of them must be forced on the same side, by the pigeonhole principle. Tree-like notions of forcing, where the number of sides grows along the construction, need more answers, but a fixed finite number for each condition.

This lesson shows that this weaker property suffices for PA avoidance. The price is paid in the third case of the argument: it is no longer enough that a $\Sigma^0_1$ set of pairs $(x, v)$ cannot be the graph of a $\mathrm{DNC}_2$ function. One needs that a $\Sigma^0_1$ set of **finite valuations** that contains no correct valuation leaves out arbitrarily many pairwise incompatible ones. This is Liu's combinatorial lemma.

## Finite valuations

:::definition{#def-valuation}
Let $D$ be a set.

1. A **finite valuation** is a function $h : F \to \{0, 1\}$ with $F \subseteq \nat$ finite, its domain $\mathrm{dom}\, h$. Finite valuations are coded by numbers.
2. A finite valuation $h$ is **correct** relative to $D$ if for every $n \in \mathrm{dom}\, h$, $J^D(n)$ is defined and $h(n) \neq J^D(n)$, that is, $h(n) = 1 - J^D(n)$.
3. Two finite valuations are **compatible** if they agree on the intersection of their domains.
4. A partial function $\psi$ is **incompatible** with $h$ if $\psi(n)\converge \neq h(n)$ for some $n \in \mathrm{dom}\, h$, and **compatible** with $h$ otherwise.
:::

A correct valuation is a piece of information shared by all $\mathrm{DNC}_2$ functions relative to $D$: on its domain, they all take the values of $h$. So a function $f : \nat \to \{0, 1\}$ incompatible with a correct valuation is not $\mathrm{DNC}_2$ relative to $D$: if $f(n) \neq h(n)$ with $h$ correct, then $f(n) = J^D(n)$. A correct valuation only exists on the domain of $J^D$; on numbers where $J^D$ is undefined, both values are allowed, and no correct valuation has them in its domain.

:::example{#ex-valuations}
Take $D = \emptyset$. If $J(3) = 0$ and $J(5) = 1$, the valuation $\{ 3 \mapsto 1, 5 \mapsto 0 \}$ is correct, and $\{ 3 \mapsto 1 \}$ is compatible with it; $\{ 3 \mapsto 0 \}$ is incompatible with both. If $J(7)$ is undefined, no valuation with $7$ in its domain is correct. The two valuations with domain $\{ 7 \}$ are incompatible with each other, and a partial function compatible with both is undefined at $7$.
:::

The last remark is the use of valuations in the proofs: a functional that is forced to be compatible with two incompatible valuations is forced to be partial. In the previous lesson, the two valuations were $\{ x \mapsto 0 \}$ and $\{ x \mapsto 1 \}$. Valuations with larger domains provide more pairwise incompatible valuations: there are $2^m$ of them with a given domain of size $m$.

## Liu's lemma

:::lemma[Liu]{#lem-liu-valuations}
Let $D \leq_T W$ be sets such that $W$ is not PA relative to $D$, and let $U$ be a $\Sigma^0_1(W)$ set of finite valuations. Either $U$ contains a valuation correct relative to $D$, or for every $m$ there is a set $F$ with $m$ elements such that no valuation with domain $F$ belongs to $U$. In the second case, the $2^m$ valuations with domain $F$ are pairwise incompatible and lie outside $U$.
:::

The idea of the proof is to build the set $F$ one element at a time, keeping the property that the valuations of $U$ whose domain contains $F$ are all wrong somewhere outside $F$. If the next element could not be found, the valuations of $U$ would give a method to avoid $J^D$, computable in $W$.

:::proof{of=lem-liu-valuations}
Suppose that $U$ contains no correct valuation. For a finite set $F$, say that $F$ is **safe** if no $h \in U$ with $F \subseteq \mathrm{dom}\, h$ is correct on $\mathrm{dom}\, h \setminus F$, that is, satisfies $J^D(n)\converge = 1 - h(n)$ for every $n \in \mathrm{dom}\, h \setminus F$. The empty set is safe, since $U$ contains no correct valuation.

*Claim.* If $F$ is safe, there is $w \notin F$ such that $F \cup \{ w \}$ is safe.

Suppose not. Then for every $n \notin F$, some $h \in U$ with $F \cup \{ n \} \subseteq \mathrm{dom}\, h$ is correct on $\mathrm{dom}\, h \setminus (F \cup \{ n \})$. Define $f : \nat \to \{0, 1\}$ as follows. On the finite set $F$, let $f(n) = 1 - J^D(n)$ if $J^D(n)$ is defined and $f(n) = 0$ otherwise; these finitely many values are fixed in advance. For $n \notin F$, search for an $h \in U$ as above, and let $f(n) = 1 - h(n)$ for the first one found. The search terminates by assumption, and is computable in $W$, since $U$ is $\Sigma^0_1(W)$ and $J^D$ is partial computable in $D \leq_T W$; so $f \leq_T W$.

We show that $f(n) \neq J^D(n)$ whenever $J^D(n)$ is defined. This is clear for $n \in F$. Let $n \notin F$ with $J^D(n)$ defined, and let $h$ be the valuation found. If $h(n) \neq J^D(n)$, then $h(n) = 1 - J^D(n)$, and $h$ is correct on $\mathrm{dom}\, h \setminus F$, with $F \subseteq \mathrm{dom}\, h$: this contradicts the safety of $F$. So $h(n) = J^D(n)$, and $f(n) = 1 - h(n) \neq J^D(n)$. Thus $f$ is $\mathrm{DNC}_2$ relative to $D$ and computable in $W$, contradicting the hypothesis on $W$. This proves the claim.

Starting from the empty set and applying the claim $m$ times gives a safe set $F$ with $m$ elements. A valuation $h \in U$ with domain exactly $F$ would be vacuously correct on $\mathrm{dom}\, h \setminus F = \emptyset$, contradicting safety. So no valuation with domain $F$ belongs to $U$.
:::

:::figure[The proof of :ref{#lem-liu-valuations}. Starting from the empty set, the claim adds one number at a time while keeping the set safe. Once $F$ has $m$ elements, the $2^m$ valuations with domain $F$ are pairwise incompatible, and none of them belongs to $U$.]
<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="The safe sets F0, F1, F2, F3 obtained by adding w0, w1, w2 one at a time, and the eight pairwise incompatible valuations with domain F3, none of which is in U"><text x="20" y="28" class="label">safe sets</text><text x="20" y="60" class="label">F₀ = ∅</text><text x="20" y="110" class="label">F₁ = {w₀}</text><text x="20" y="160" class="label">F₂ = {w₀, w₁}</text><text x="20" y="210" class="label">F₃ = {w₀, w₁, w₂}</text><line x1="60" y1="68" x2="60" y2="94" class="muted-stroke" stroke-width="1.2"/><line x1="60" y1="118" x2="60" y2="144" class="muted-stroke" stroke-width="1.2"/><line x1="60" y1="168" x2="60" y2="194" class="muted-stroke" stroke-width="1.2"/><text x="20" y="250" class="label">each step: the claim of the proof</text><line x1="420.0" y1="44" x2="335.0" y2="94" class="ink-stroke" stroke-width="1.1"/><text x="367.5" y="74.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="420.0" y1="44" x2="505.0" y2="94" class="ink-stroke" stroke-width="1.1"/><text x="472.5" y="74.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="242" y="74.0" text-anchor="end" class="math" font-size="13">w₀</text><line x1="335.0" y1="104" x2="292.5" y2="154" class="ink-stroke" stroke-width="1.1"/><text x="303.8" y="134.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="335.0" y1="104" x2="377.5" y2="154" class="ink-stroke" stroke-width="1.1"/><text x="366.2" y="134.0" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="505.0" y1="104" x2="462.5" y2="154" class="ink-stroke" stroke-width="1.1"/><text x="473.8" y="134.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="505.0" y1="104" x2="547.5" y2="154" class="ink-stroke" stroke-width="1.1"/><text x="536.2" y="134.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="242" y="134.0" text-anchor="end" class="math" font-size="13">w₁</text><line x1="292.5" y1="164" x2="271.2" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="271.9" y="194.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="292.5" y1="164" x2="313.8" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="313.1" y="194.0" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="377.5" y1="164" x2="356.2" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="356.9" y="194.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="377.5" y1="164" x2="398.8" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="398.1" y="194.0" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="462.5" y1="164" x2="441.2" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="441.9" y="194.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="462.5" y1="164" x2="483.8" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="483.1" y="194.0" text-anchor="middle" class="mrm" font-size="12">1</text><line x1="547.5" y1="164" x2="526.2" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="526.9" y="194.0" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="547.5" y1="164" x2="568.8" y2="214" class="ink-stroke" stroke-width="1.1"/><text x="568.1" y="194.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="242" y="194.0" text-anchor="end" class="math" font-size="13">w₂</text><circle cx="420.0" cy="40" r="4" class="muted-fill"/><circle cx="335.0" cy="100" r="4" class="muted-fill"/><circle cx="292.5" cy="160" r="4" class="muted-fill"/><rect x="262.2" y="214" width="18" height="16" class="cell head-cell"/><rect x="304.8" y="214" width="18" height="16" class="cell head-cell"/><circle cx="377.5" cy="160" r="4" class="muted-fill"/><rect x="347.2" y="214" width="18" height="16" class="cell head-cell"/><rect x="389.8" y="214" width="18" height="16" class="cell head-cell"/><circle cx="505.0" cy="100" r="4" class="muted-fill"/><circle cx="462.5" cy="160" r="4" class="muted-fill"/><rect x="432.2" y="214" width="18" height="16" class="cell head-cell"/><rect x="474.8" y="214" width="18" height="16" class="cell head-cell"/><circle cx="547.5" cy="160" r="4" class="muted-fill"/><rect x="517.2" y="214" width="18" height="16" class="cell head-cell"/><rect x="559.8" y="214" width="18" height="16" class="cell head-cell"/><text x="420.0" y="246" text-anchor="middle" class="label">the 2³ valuations with domain F₃:</text><text x="420.0" y="262" text-anchor="middle" class="label">pairwise incompatible, none in U</text></svg>
:::

The proof does not find the set $F$ effectively: safety is a $\Pi^0_1(W)$ property of $F$, and the element $w$ is only known to exist. This is enough, since the lemma is used in the third case of a density argument, which is a proof by contradiction. In the first exercise below, the elements of $F$ can be taken among the numbers on which $J$ is undefined, which shows where the incompatible valuations come from in a typical case.

:::quiz[Liu's lemma]
In the proof of the claim, where is the safety of $F$ used?

- [x] To show that a valuation $h$ found in the search gives the wrong value at $n$ when $J^D(n)$ is defined: otherwise $h$ would be correct outside $F$.
- [ ] To show that the search terminates.

  Termination comes from the assumption that no $w$ works, which is what is refuted.
- [ ] To define $f$ on $F$.

  On $F$, the values of $f$ are fixed in advance, using finitely many bits of information.

---

Why are the values of $f$ on $F$ fixed in advance rather than computed?

- [x] Because the valuations of $U$ give no information on $F$: they may be wrong on $F$; finitely many values can be built into the algorithm.
- [ ] Because $J^D$ is total on $F$.

  $J^D$ may be undefined on $F$; then the value $0$ is chosen.
- [ ] Because $F$ is infinite.

  $F$ is finite.
:::

## Weakly merging questions

:::definition{#def-weakly-merging}
A forcing question is **weakly merging** (at level $1$) if for every condition $c$ there is $k \geq 2$ such that for all $\Sigma^0_1$ sentences $\varphi_0, \dots, \varphi_{k-1}$ with $c \mathrel{?{\nvdash}} \varphi_s$ for every $s < k$, there are $d \leq c$ and $s < t < k$ with $d \Vdash \neg \varphi_s \wedge \neg \varphi_t$.
:::

A merging question is weakly merging with $k = 2$ for every condition. The number $k$ may depend on the condition: in the next lesson, $k$ is the number of sides of the condition plus one.

:::theorem{#thm-weak-merging-pa}
Let $D$ be a set, and $\mathcal M$ a class of sets computing $D$, none of which is PA relative to $D$. Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving weakly merging forcing question. For every sufficiently generic set $G$, $Z \oplus G$ is not PA relative to $D$.
:::

:::proof{of=thm-weak-merging-pa}
For a finite valuation $h$, write $\Phi^{Z \oplus G}_e \perp h$ for the $\Sigma^0_1$ sentence "$\Phi^{Z \oplus G}_e$ is incompatible with $h$"; it is $\Sigma^0_1$ uniformly in the code of $h$. For each $e$, let $E_e$ be the set of conditions all of whose members $G$ are such that $\Phi^{Z \oplus G}_e$ is not $\mathrm{DNC}_2$ relative to $D$. Let $c$ be a condition, $k$ as in :ref{#def-weakly-merging}, and $X \in \mathcal M$ as in :ref{#def-question-local}. The set
$$
U = \{ h \text{ finite valuation} : c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e \perp h \}
$$
is $\Sigma^0_1(X)$.

1. If $U$ contains a correct valuation $h$, property 1 of the question gives $d \leq c$ forcing $\Phi^{Z \oplus G}_e \perp h$. For every member $G$ of $d$, $\Phi^{Z \oplus G}_e$ is incompatible with a correct valuation, so it is not $\mathrm{DNC}_2$ relative to $D$: $d \in E_e$.
2. If there are pairwise incompatible valuations $h_0, \dots, h_{k-1}$ outside $U$, then $c \mathrel{?{\nvdash}} \Phi^{Z \oplus G}_e \perp h_s$ for every $s < k$, and the question is weakly merging: some $d \leq c$ and $s < t$ satisfy $d \Vdash \neg (\Phi^{Z \oplus G}_e \perp h_s) \wedge \neg (\Phi^{Z \oplus G}_e \perp h_t)$. On every member $G$ of $d$, $\Phi^{Z \oplus G}_e$ is compatible with $h_s$ and with $h_t$; at a number $n$ where $h_s$ and $h_t$ differ, $\Phi^{Z \oplus G}_e(n)$ is undefined. So $d \in E_e$.
3. Otherwise, $U$ contains no correct valuation and no $k$ pairwise incompatible valuations lie outside $U$. Since $X$ computes $D$ and is not PA relative to $D$, this contradicts :ref{#lem-liu-valuations} with $W = X$ and $m$ such that $2^m \geq k$.

So $E_e$ is dense, and a set generic for the sets $E_e$ satisfies the theorem.
:::

When the question is merging, case 2 already applies with the two valuations $\{ x \mapsto 0 \}$ and $\{ x \mapsto 1 \}$ for a single $x$, and case 3 reduces to the selection argument of :ref{#thm-local-pa-avoidance}. Weak merging trades a stronger property of the question for a deeper third case. This is the general shape of preservation proofs: the less the question can do, the more combinatorics is needed to show that some case applies.

:::quiz[weakly merging questions]
In case 2 of the proof of :ref{#thm-weak-merging-pa}, why must the valuations $h_0, \dots, h_{k-1}$ be pairwise incompatible, rather than only distinct?

- [x] Because weak merging gives two of them, $h_s$ and $h_t$, chosen by the question and not by us; the conclusion that $\Phi^{Z \oplus G}_e$ is partial needs these two to be incompatible.
- [ ] Because :ref{#lem-liu-valuations} only gives pairwise incompatible valuations.

  The lemma gives them because the proof needs them, not conversely.
- [ ] Because otherwise $U$ would not be $\Sigma^0_1(X)$.

  The complexity of $U$ does not depend on the valuations chosen in case 2.
:::

## Disjunctive questions

The application to the pigeonhole principle uses the disjunctive framework of :ref{to="avoidance/disjunctive-question"}, with sides $G_0$ and $G_1$.

:::definition{#def-disjunctive-weakly-merging}
A disjunctive forcing question (:ref{#def-disjunctive-notion}) is **weakly merging** if for every condition $c$ there is $k \geq 2$ such that for all pairs of $\Sigma^0_1$ sentences $(\varphi^s_0, \varphi^s_1)$, $s < k$, with $c \mathrel{?{\nvdash}} \varphi^s_0(G_0) \vee \varphi^s_1(G_1)$ for every $s < k$, there are $d \leq c$, a side $i < 2$ and $s < t < k$ with $d \Vdash \neg \varphi^s_i(G_i) \wedge \neg \varphi^t_i(G_i)$.
:::

:::lemma{#lem-disjunctive-pa}
Let $D$ be a set and $\mathcal M$ a class of sets computing $D$, none of which is PA relative to $D$. Let a disjunctive notion of forcing have a $\Sigma^0_1(\mathcal M)$-preserving weakly merging disjunctive question.

1. For every condition $c$ and all $e_0, e_1$, there are $d \leq c$ and $i < 2$ such that for every member $G$ of side $i$ of $d$, $\Phi^{Z \oplus G}_{e_i}$ is not $\mathrm{DNC}_2$ relative to $D$.
2. Let $c_0 \geq c_1 \geq \cdots$ be conditions and $G_0, G_1$ sets with $G_i \in [c_s]_i$ for all $s$ and $i$. If for every pair $(e_0, e_1)$ some $c_s$ satisfies the conclusion of item 1, then $Z \oplus G_0$ or $Z \oplus G_1$ is not PA relative to $D$.
:::

:::proof{of=lem-disjunctive-pa}
1. Let $k$ be given for $c$ by :ref{#def-disjunctive-weakly-merging}, $X \in \mathcal M$ by $\Sigma^0_1(\mathcal M)$-preservation, and
$$
U = \{ h : c \mathrel{?{\vdash}} (\Phi^{Z \oplus G}_{e_0} \perp h)(G_0) \vee (\Phi^{Z \oplus G}_{e_1} \perp h)(G_1) \},
$$
a $\Sigma^0_1(X)$ set. If $U$ contains a correct valuation, property 1 of the disjunctive question gives $d \leq c$ and $i$ with $d \Vdash (\Phi^{Z \oplus G}_{e_i} \perp h)(G_i)$, and every member of side $i$ is as required. If $k$ pairwise incompatible valuations lie outside $U$, weak merging gives $d$, $i$ and $s < t$ such that every member $G$ of side $i$ makes $\Phi^{Z \oplus G}_{e_i}$ compatible with $h_s$ and $h_t$, hence partial. One of the two cases holds, by :ref{#lem-liu-valuations}.
2. This is Lachlan's disjunction, as in :ref{#lem-disjunctive-construction}: for every pair $(e_0, e_1)$, $\Phi^{Z \oplus G_0}_{e_0}$ or $\Phi^{Z \oplus G_1}_{e_1}$ is not $\mathrm{DNC}_2$ relative to $D$. If some $\Phi^{Z \oplus G_0}_{e_0}$ is $\mathrm{DNC}_2$ relative to $D$, then no $\Phi^{Z \oplus G_1}_{e_1}$ is, and $Z \oplus G_1$ is not PA relative to $D$; otherwise $Z \oplus G_0$ is not PA relative to $D$.
:::

The Dzhafarov–Jockusch question has the combinatorial property, but not the definability that the lemma needs.

:::example{#ex-dj-weakly-merging}
Let $A$ be a set, and consider the disjunctive notion of forcing of the first exercise of :ref{to="avoidance/disjunctive-question"}: conditions $(\sigma_0, \sigma_1, X)$ with $\sigma_i \subseteq A^i$, where $A^0 = A$ and $A^1 = \overline A$, and $X$ an infinite set in a Scott ideal $\mathcal M$, with its question: $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if for every set $B$, with $B^0 = B$ and $B^1 = \overline B$, there are $i < 2$ and $\tau$ compatible with $(\sigma_i, X \cap B^i)$ satisfying $\varphi_i$. This question is weakly merging with $k = 3$.

Indeed, suppose that the answer is negative for three pairs $(\varphi^s_0, \varphi^s_1)$, $s < 3$. For each $s$, the sets $B$ witnessing the negative answer form a non-empty $\Pi^0_1(X \oplus Z)$ class, so the product of the three classes has a member $(B_0, B_1, B_2) \in \mathcal M$. The three sets split $X$ into the eight sets $X \cap B_0^{a_0} \cap B_1^{a_1} \cap B_2^{a_2}$, one of which, say for $(a_0, a_1, a_2)$, is infinite; call it $Y$. Two of the three bits are equal, say $a_s = a_t = i$ with $s < t$. The condition $(\sigma_0, \sigma_1, Y)$ extends $c$, and a member of side $i$ satisfying $\varphi^s_i$ would have a prefix compatible with $(\sigma_i, X \cap B_s^i)$ satisfying it, which is excluded; the same holds for $t$. So $(\sigma_0, \sigma_1, Y) \Vdash \neg \varphi^s_i(G_i) \wedge \neg \varphi^t_i(G_i)$.
:::

Yet :ref{#lem-disjunctive-pa} does not apply: a Scott ideal containing $Z$ contains sets that are PA relative to $Z$, hence relative to every $D \leq_T Z$, and these sets cannot be excluded from $\mathcal M$, since the reservoirs $X \cap B_0^{a_0} \cap \cdots$ are computed from them. The reservoirs must be kept in the class of the sets that are not PA relative to $D$, and a non-empty $\Pi^0_1(X \oplus Z)$ class of partitions need not have such a member. Liu's solution, in :ref{to="compactness-avoidance/liu-theorem"}, is to shrink the reservoir without choosing a partition: it suffices to find an infinite subset of $X$ contained, for some member $B$ of the class and some side $a$, in $B^a$. This is the Ramsey-type weak König lemma of the next lesson.

:::quiz[the Dzhafarov–Jockusch question]
In :ref{#ex-dj-weakly-merging}, why are three negative answers needed rather than two?

- [x] Because the infinite piece $Y$ of $X$ lies on side $a_s$ of $B_s$ for each $s$, and only with three bits are two of them guaranteed to be equal; with two bits, $Y$ could lie on side $0$ of $B_0$ and side $1$ of $B_1$.
- [ ] Because the product of two $\Pi^0_1$ classes may be empty.

  A product of non-empty classes is non-empty.
- [ ] Because $X$ must be split into eight pieces.

  The eight pieces come from three sets; the number of sets is what matters.
:::

## Exercises

::::exercise{difficulty=1}
Let $U$ be the c.e. set of the finite valuations $h$ such that $J(n)\converge = h(n)$ for some $n \in \mathrm{dom}\, h$. Show that $U$ contains no correct valuation, and give, for every $m$, a set $F$ of size $m$ as in :ref{#lem-liu-valuations}.

:::solution
A correct valuation satisfies $J(n)\converge = 1 - h(n) \neq h(n)$ on its whole domain, so it is not in $U$. Let $F$ be a set of $m$ numbers $n$ with $J(n)$ undefined; there are infinitely many, for instance the indices of the nowhere defined function, which form an infinite set by the padding lemma. A valuation with domain $F$ never satisfies $J(n)\converge = h(n)$ for $n \in F$, so it is not in $U$. Here $U$ leaves out valuations because $J$ is partial, which is the typical situation.
:::
::::

::::exercise{difficulty=2}
Generalize :ref{#ex-dj-weakly-merging} to the pigeonhole principle with $\ell$ colors: conditions $(\sigma_0, \dots, \sigma_{\ell - 1}, X)$ with $\sigma_i \subseteq A^i$ for a partition $\nat = A^0 \sqcup \cdots \sqcup A^{\ell - 1}$, $X$ in a Scott ideal, and the question "for every partition $\nat = B^0 \sqcup \cdots \sqcup B^{\ell - 1}$ there are $i < \ell$ and $\tau$ compatible with $(\sigma_i, X \cap B^i)$ satisfying $\varphi_i$". State weak merging for $\ell$ sides, and show that this question satisfies it with $k = \ell + 1$.

:::solution
Weak merging for $\ell$ sides: for every condition there is $k$ such that if the answer is negative for $k$ tuples $(\varphi^s_0, \dots, \varphi^s_{\ell - 1})$, then some extension forces $\neg \varphi^s_i(G_i) \wedge \neg \varphi^t_i(G_i)$ for some side $i$ and some $s < t < k$. Given $\ell + 1$ negative answers, each is witnessed by a non-empty $\Pi^0_1(X \oplus Z)$ class of partitions (coded as functions $\nat \to \ell$), and the Scott ideal contains a member $(B_s)_{s \leq \ell}$ of the product. The sets $X \cap \bigcap_{s \leq \ell} B^{a_s}_s$, for $(a_s) \in \ell^{\ell + 1}$, are finitely many and cover $X$, so one of them, $Y$, is infinite. Among the $\ell + 1$ colors $a_s < \ell$, two coincide by the pigeonhole principle: $a_s = a_t = i$ with $s < t$. A member of side $i$ of $(\vec \sigma, Y)$ satisfying $\varphi^s_i$ would have a prefix compatible with $(\sigma_i, X \cap B^i_s)$ satisfying it, contradicting the choice of $B_s$; the same holds for $t$. So $(\vec \sigma, Y)$ forces both negations on side $i$.
:::
::::

## Notes and references

Weakly merging questions and the abstract theorem are in the chapter *Compactness avoidance* of Patey's monograph, section *Weak merging*, where they are called weakly $\Pi^0_1$-merging; the monograph proves the combinatorial lemma there, with the explicit attribution to Liu. Valuations, their correctness and the lemma are from Liu's paper (2012), where they appear in the proof that the pigeonhole principle admits strong PA avoidance. The proof given here is a reorganization of the monograph's proof around the notion of a safe set. The example of the Dzhafarov–Jockusch question is an exercise of the same section.

- J. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *Weak merging*.
