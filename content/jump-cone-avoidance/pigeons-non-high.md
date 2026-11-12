---
title: Pigeons do not jump high
summary: Second-jump control for the pigeonhole principle; Π⁰₂ sentences forced through the question on stems, true on valid sides; a disjunctive question for Σ⁰₂ sentences when both sides stay valid, and a question on one side, with a witness of invalidity, when one side is lost; every set has an infinite subset, of itself or of its complement, whose jump avoids a given cone, and which is not high.
duration: 45
prerequisites: [pigeonhole-forcing]
---

This lesson completes the proof of :ref{#thm-pigeons-non-high}. The setting of the previous lesson is fixed: the ideals $\mathcal M \subseteq \mathcal N$, the $\mathcal M$-cohesive class $\mathcal U_S$ with $S \in \mathcal N$, its core $\mathcal U$, the set $A$ with $A_0 = A$ and $A_1 = \overline A$, the conditions $(\sigma_0, \sigma_1, X)$, and the question $\sigma \mathrel{?{\vdash}} \varphi$ for $\Sigma^0_1$ sentences. The construction is a decreasing sequence of conditions, as in :ref{#thm-seetapun-direct}. Three ingredients are added: a syntactic forcing relation for $\Pi^0_2$ sentences, which becomes truth on the sides that stay valid; a disjunctive question for $\Sigma^0_2$ sentences, used when both sides stay valid; and a question on one side, used when the other side has become invalid.

## Forcing Π⁰₂ sentences

A $\Pi^0_2$ sentence has the form $\forall y\ \theta(y)$ with $\theta$ a $\Sigma^0_1$ formula (:ref{#def-forcing-formula}).

:::definition{#def-pigeon-pi2}
A condition $(\sigma_0, \sigma_1, X)$ **promises** $\forall y\ \theta(y)$ on side $i$ if $\tau \mathrel{?{\vdash}} \theta(m)$ for every $m$ and every string $\tau$ compatible with $(\sigma_i, X)$.
:::

The promise says that whatever stem on side $i$ the future of the construction chooses, the question about each instance $\theta(m)$ answers positively. It is preserved by extensions: if $(\tau_0, \tau_1, Y)$ extends $(\sigma_0, \sigma_1, X)$, a string compatible with $(\tau_i, Y)$ is compatible with $(\sigma_i, X)$, since $\tau_i$ is compatible with $(\sigma_i, X)$ and $Y \subseteq X$.

:::lemma{#lem-pigeon-promise}
Let $p$ be a condition promising $\forall y\ \theta(y)$ on side $i$, with side $i$ valid, and let $m \in \nat$. There is an extension of $p$, with the same valid sides, that forces $\theta(m)$ on side $i$.
:::

:::proof{of=lem-pigeon-promise}
The stem $\sigma_i$ is compatible with $(\sigma_i, X)$, so $\sigma_i \mathrel{?{\vdash}} \theta(m)$. Apply item 1 of :ref{#lem-pigeon-sigma1}.
:::

The promise is the density form of forcing a $\Pi^0_2$ sentence (:ref{to="jump-cone-avoidance/sigma2-questions"}), stated through the question rather than through the forcing relation, and it is useful only as long as side $i$ is valid. In a construction where side $i$ stays valid forever, a promise made at some step is kept: each instance $\theta(m)$ is handled at a later step by the lemma.

## The disjunctive question

For a condition $p = (\sigma_0, \sigma_1, X)$ and a set $B$, write $B^0 = X \cap B$ and $B^1 = X \setminus B$: every set $B$ gives a $2$-partition of the reservoir.

:::definition{#def-pigeon-disjunctive}
Let $p = (\sigma_0, \sigma_1, X)$ be a condition, and $\varphi_0 = \exists y\ \psi_0(y)$, $\varphi_1 = \exists y\ \psi_1(y)$ two $\Sigma^0_2$ sentences, with $\psi_0, \psi_1$ $\Pi^0_1$ formulas. Let $p \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if for every set $B$ there are $i < 2$, $m \in \nat$ and a string $\tau$ compatible with $(\sigma_i, B^i)$ with $\tau \mathrel{?{\nvdash}} \neg\psi_i(m)$.
:::

As in the Seetapun forcing (:ref{#lem-seetapun-question}), the question is asked for every partition of the reservoir, so that it does not depend on $A$.

:::lemma{#lem-pigeon-disjunctive}
Let $p = (\sigma_0, \sigma_1, X)$ be a condition and $\varphi_0, \varphi_1$ as above.

1. If $p \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, there are $i < 2$ and an extension of $p$ all of whose members of side $i$ satisfy $\varphi_i$.
2. If $p \mathrel{?{\nvdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, there are $i < 2$ and an extension of $p$, with the same stems, that promises $\neg\varphi_i = \forall y\ \neg\psi_i(y)$ on side $i$.
3. The relation $\{ \vec n : p \mathrel{?{\vdash}} \varphi_0(\vec n)(G_0) \vee \varphi_1(\vec n)(G_1) \}$ is $\Sigma^0_1(X \oplus S \oplus M')$, and $X \oplus S \oplus M' \in \mathcal N$.
:::

:::proof{of=lem-pigeon-disjunctive}
1. Take $B = A$, so that $B^i = X \cap A_i$. There are $i$, $m$ and $\tau$ compatible with $(\sigma_i, X \cap A_i)$ with $\tau \mathrel{?{\nvdash}} \neg\psi_i(m)$. The new elements of $\tau$ are in $A_i$, so $q = (\tau_0, \tau_1, X \setminus \{0, \dots, |\tau| - 1\})$, with $\tau_i = \tau$ and $\tau_{1-i} = \sigma_{1-i}$, is a condition extending $p$. By item 2 of :ref{#lem-pigeon-sigma1}, applied to $q$, side $i$ and the $\Sigma^0_1$ sentence $\neg\psi_i(m)$, some extension of $q$ forces $\neg\neg\psi_i(m) = \psi_i(m)$ on side $i$. Its members of side $i$ satisfy $\psi_i(m)$, hence $\varphi_i$.
2. Let $\mathcal C$ be the class of sets $B$ such that for all $i < 2$, $m$ and $\tau$ compatible with $(\sigma_i, B^i)$, $\tau \mathrel{?{\vdash}} \neg\psi_i(m)$. Compatibility of $\tau$ with $(\sigma_i, B^i)$ depends on $X$ and on $B \uh |\tau|$, and the relation $\tau \mathrel{?{\vdash}} \neg\psi_i(m)$ is $\Pi^0_1(S \oplus M')$; so $\mathcal C$ is a $\Pi^0_1(X \oplus S \oplus M')$ class. It is non-empty by hypothesis. Since $\mathcal N$ is a Scott ideal containing $X \oplus S \oplus M'$, $\mathcal C$ has a member $B \in \mathcal N$. The sets $B^0$ and $B^1$ cover $X \in \mathcal U$, so some $B^i$ is in $\mathcal U$; it is in $\mathcal N$ and contained in $X$. The condition $(\sigma_0, \sigma_1, B^i)$ extends $p$, and promises $\forall y\ \neg\psi_i(y)$ on side $i$, by definition of $\mathcal C$.
3. The question holds if and only if $\mathcal C$ is empty, which is a $\Sigma^0_1(X \oplus S \oplus M')$ property, uniformly in the parameters of the sentences, by :ref{#prop-pi01-emptiness} relativized.
:::

Item 1 gives a property of all members, and needs no validity. Item 2 gives only a promise, on a side $i$ that is not under control: it is useful only if side $i$ stays valid. When both sides stay valid forever, the disjunctive question is a disjunctive forcing question in the sense of :ref{#def-disjunctive-notion}, one level up.

:::quiz[the disjunctive question]
In item 2 of :ref{#lem-pigeon-disjunctive}, why is the partition $B$ taken in $\mathcal N$?

- [x] Because the new reservoir $B^i = X \cap B$ or $X \setminus B$ must belong to $\mathcal N$; the Scott property of $\mathcal N$, applied to the $\Pi^0_1(X \oplus S \oplus M')$ class $\mathcal C$, provides such a $B$.
- [ ] Because $B$ must be in $\mathcal M$ to apply cohesiveness.

  Cohesiveness is not used here; the side is chosen by the partition regularity of $\mathcal U$.
- [ ] Because $A \in \mathcal N$.

  $A$ is arbitrary and need not belong to $\mathcal N$.

---

Why does item 3 need $M'$ and not only $M$?

- [x] Because the inner question $\tau \mathrel{?{\vdash}} \neg\psi_i(m)$ is a largeness property of a class $\mathcal U_S \cap \mathcal V$, which is $\Pi^0_1(S \oplus M')$ by :ref{#prop-largeness-complexity}.
- [ ] Because $X$ is computable in $M'$.

  $X$ is a member of $\mathcal N$, not necessarily computable in $M'$.
- [ ] Because compactness requires the jump.

  Compactness, the emptiness of a $\Pi^0_1$ class, is $\Sigma^0_1$ relative to the class's oracle.
:::

## The question on one side

When side $1 - i$ of a condition is invalid, the disjunctive question may answer with a promise on the wrong side. The following question avoids it, using a witness that side $1 - i$ is invalid.

:::definition{#def-invalidity-witness}
A **witness of invalidity** of side $j$ of a condition $(\sigma_0, \sigma_1, X)$ is a $\Sigma^0_1(\mathcal M)$ class $\mathcal V$ with $\mathcal U \subseteq \mathcal V$ and $X \cap A_j \notin \mathcal V$.
:::

If side $j$ is invalid, then $X \cap A_j \notin \mathcal U$, and item 3 of :ref{#prop-cohesive-core} gives a witness. A witness for $p$ is a witness for every extension of $p$, since the sets $Y \cap A_j$ decrease and $\mathcal V$ is upward closed.

:::definition{#def-pigeon-one-side}
Let $p = (\sigma_0, \sigma_1, X)$ be a condition, $\mathcal V$ a witness of invalidity of side $1 - i$, and $\varphi = \exists y\ \psi(y)$ a $\Sigma^0_2$ sentence. Let $p \mathrel{?{\vdash}}_{\mathcal V} \varphi(G_i)$ if for every set $B$ with $B^{1-i} \notin \mathcal V$ there are $m$ and a string $\tau$ compatible with $(\sigma_i, B^i)$ with $\tau \mathrel{?{\nvdash}} \neg\psi(m)$.
:::

:::lemma{#lem-pigeon-one-side}
Let $p$, $\mathcal V$ and $\varphi$ be as in the definition.

1. If $p \mathrel{?{\vdash}}_{\mathcal V} \varphi(G_i)$, there is an extension of $p$ all of whose members of side $i$ satisfy $\varphi$.
2. If $p \mathrel{?{\nvdash}}_{\mathcal V} \varphi(G_i)$, there is an extension of $p$, with the same stems, that promises $\neg\varphi$ on side $i$.
3. The relation $\{ \vec n : p \mathrel{?{\vdash}}_{\mathcal V} \varphi(\vec n)(G_i) \}$ is $\Sigma^0_1(Y)$ for some $Y \in \mathcal N$.
:::

:::proof{of=lem-pigeon-one-side}
Let $\mathcal V$ be $\Sigma^0_1(W)$ with $W \in \mathcal M$.

1. Take $B = A_0$, so that $B^{1-i} = X \cap A_{1-i}$, which is not in $\mathcal V$. There are $m$ and $\tau$ compatible with $(\sigma_i, X \cap A_i)$ with $\tau \mathrel{?{\nvdash}} \neg\psi(m)$, and the proof of item 1 of :ref{#lem-pigeon-disjunctive} applies.
2. Let $\mathcal C$ be the class of sets $B$ with $B^{1-i} \notin \mathcal V$ such that $\tau \mathrel{?{\vdash}} \neg\psi(m)$ for all $m$ and all $\tau$ compatible with $(\sigma_i, B^i)$. The condition $B^{1-i} \notin \mathcal V$ is $\Pi^0_1(X \oplus W)$, so $\mathcal C$ is a $\Pi^0_1(X \oplus W \oplus S \oplus M')$ class, non-empty by hypothesis, with a member $B \in \mathcal N$. Now $B^{1-i} \notin \mathcal V \supseteq \mathcal U$, so $B^{1-i} \notin \mathcal U$; as $B^0, B^1$ cover $X \in \mathcal U$, $B^i \in \mathcal U$. The condition $(\sigma_0, \sigma_1, B^i)$ extends $p$ and promises $\neg\varphi$ on side $i$.
3. The question holds if and only if $\mathcal C$ is empty, a $\Sigma^0_1(Y)$ property for $Y = X \oplus W \oplus S \oplus M' \in \mathcal N$.
:::

The witness forces the partition to put its large part on side $i$: this is how a question on one side can be answered by a partition, although the partition does not know $A$.

## The proof of the theorem

We first show how the questions give the requirements. Let $h$ be the computable function such that "$\Phi^{G'}_e(x)\converge = v$" is equivalent to the $\Sigma^0_2$ sentence $\chi_{e,x,v} = \exists y\ \Phi^G_{h(e,x,v)}(y)\diverge$, for every set $G$ (:ref{to="jump-cone-avoidance/sigma2-questions"}). Its negation is the $\Pi^0_2$ sentence $\forall y\ \Phi^G_{h(e,x,v)}(y)\converge$.

:::lemma{#lem-pigeon-requirements}
Let $p$ be a condition.

1. For all $e_0, e_1$, there are an extension $q$ of $p$, a side $i$ and a number $x$ such that every member of side $i$ of $q$ satisfies $\chi_{e_i, x, 1 - C(x)}$, or $q$ promises $\neg\chi_{e_i, x, C(x)}$ on side $i$.
2. If side $1 - i$ of $p$ is invalid, then for every $e$ there are an extension $q$ of $p$ and a number $x$ such that every member of side $i$ of $q$ satisfies $\chi_{e, x, 1 - C(x)}$, or $q$ promises $\neg\chi_{e, x, C(x)}$ on side $i$.
:::

:::proof{of=lem-pigeon-requirements}
1. By item 3 of :ref{#lem-pigeon-disjunctive}, the set $U$ of pairs $(x, v) \in \nat \times \{0, 1\}$ with $p \mathrel{?{\vdash}} \chi_{e_0, x, v}(G_0) \vee \chi_{e_1, x, v}(G_1)$ is $\Sigma^0_1(Y)$ for some $Y \in \mathcal N$. If $(x, 1 - C(x)) \in U$ for some $x$, item 1 of :ref{#lem-pigeon-disjunctive} gives the first alternative. If $(x, C(x)) \notin U$ for some $x$, item 2 gives the second. Otherwise $U$ is the graph of $C$, and $C \leq_T Y \in \mathcal N$, which contradicts $C \notin \mathcal N$.
2. The same, with a witness $\mathcal V$ of invalidity of side $1 - i$ and :ref{#lem-pigeon-one-side}.
:::

This is the three-case argument of :ref{#thm-local-jump-cone}, with the sides of :ref{#lem-disjunctive-cone}. We now build the sets.

:::proof{of=thm-pigeons-non-high}
We first treat $Z = \emptyset$, with the setting of :ref{#lem-pigeon-setting}. There are two cases.

*Case A: some condition $p_0$ has an invalid side, say side $1 - i$.* By item 2 of :ref{#lem-valid-part}, side $1 - i$ is invalid in every extension of $p_0$, and so side $i$ is valid in every extension, by item 1. Build a sequence $p_0 \geq p_1 \geq \cdots$ of conditions, handling in turn, infinitely often each, the following tasks:

- extend the stem on side $i$, by item 4 of :ref{#lem-valid-part};
- for an index $e$, pass to an extension given by item 2 of :ref{#lem-pigeon-requirements};
- for a $\Pi^0_2$ sentence $\forall y\ \theta(y)$ and a number $m$: if the current condition promises $\forall y\ \theta(y)$ on side $i$, pass to an extension forcing $\theta(m)$ on side $i$, by :ref{#lem-pigeon-promise}; otherwise do nothing.

Let $G_i$ be the union of the stems on side $i$. It is infinite by the first task, contained in $A_i$, and a member of side $i$ of every $p_s$, as in the proof of :ref{#thm-seetapun-direct}. If $p_s$ promises $\forall y\ \theta(y)$ on side $i$, so does every later condition, and the third task, handled at a later step for each $m$, gives a condition forcing $\theta(m)$ on side $i$; so $G_i$ satisfies $\forall y\ \theta(y)$. For each $e$, the second task gives $s$ and $x$ such that $G_i$ satisfies $\chi_{e, x, 1 - C(x)}$, or $p_s$ promises $\neg\chi_{e, x, C(x)}$, and then $G_i$ satisfies $\neg\chi_{e, x, C(x)}$. In both cases $\Phi^{G_i'}_e(x) \neq C(x)$, as a divergence or as a wrong value. So $C \not\leq_T G_i'$, and $H = G_i$ works.

*Case B: every condition has both sides valid.* Start with $p_0 = (\varepsilon, \varepsilon, \nat)$, and handle in turn, infinitely often each: extending the stem on side $0$, and on side $1$; for a pair $(e_0, e_1)$, passing to an extension given by item 1 of :ref{#lem-pigeon-requirements}; for a side $j$, a $\Pi^0_2$ sentence and a number $m$, keeping promises on side $j$ as in case A. Both sides are valid throughout, so all tasks can be carried out. Let $G_0$ and $G_1$ be the unions of the stems. Both are infinite, $G_j \subseteq A_j$, and promises on either side are kept, as in case A. For every pair $(e_0, e_1)$, there is $j$ with $\Phi^{G_j'}_{e_j} \neq C$. This is Lachlan's disjunction, as in :ref{#lem-disjunctive-construction}: if $\Phi^{G_0'}_{e_0} = C$ for some $e_0$, then $\Phi^{G_1'}_{e_1} \neq C$ for every $e_1$, and $C \not\leq_T G_1'$; otherwise $C \not\leq_T G_0'$. Let $H$ be the corresponding $G_j$.

*The general case.* For a set $Z$ and $C \not\leq_T Z'$, take a Scott ideal $\mathcal M$ containing $Z$ with a code $M$ satisfying $M' \leq_T Z'$ (:ref{#cor-scott-codes}), and a Scott ideal $\mathcal N$ containing $Z'$ and not $C$ (:ref{#lem-scott-cone}). Then $M, M' \in \mathcal N$, and $\mathcal N$ contains a set PA relative to $Z' \geq_T M'$, which computes $S$. Use sentences about $Z \oplus G$ instead of $G$: the classes $\mathcal V_{\sigma, \varphi}$ become $\Sigma^0_1(Z)$ classes, and $Z \in \mathcal M$, so they are $\Sigma^0_1(\mathcal M)$ classes, and all the lemmas hold with the same proofs. The result is an infinite $H \subseteq A_0$ or $H \subseteq A_1$ with $C \not\leq_T (Z \oplus H)'$.
:::

:::figure[The structure of the proof of :ref{#thm-pigeons-non-high}. If some condition has an invalid side, every extension has the same invalid side, and the construction below it works on the other side alone, with the question of :ref{#def-pigeon-one-side}. Otherwise both sides stay valid, and the disjunctive question of :ref{#def-pigeon-disjunctive} satisfies the requirements on one side or the other; Lachlan's disjunction gives a side on which all of them hold.]
<svg class="fig" viewBox="0 0 600 262" width="600" role="img" aria-label="The case split of the proof: if some condition has an invalid side, work on the other side with the question on one side; otherwise use the disjunctive question and Lachlan disjunction"><defs><marker id="jc-cs-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="170" y="8" width="260" height="40" rx="6" class="state"/><text x="300.0" y="24.0" text-anchor="middle" class="label">does some condition p₀</text><text x="300.0" y="40.0" text-anchor="middle" class="label">have an invalid side 1 − i?</text><rect x="20" y="92" width="260" height="54" rx="6" class="node"/><text x="150.0" y="107.0" text-anchor="middle" class="label">case A: work below p₀</text><text x="150.0" y="123.0" text-anchor="middle" class="label">side i valid in every extension</text><text x="150.0" y="139.0" text-anchor="middle" class="label">question on side i with a witness 𝒱</text><rect x="320" y="92" width="260" height="54" rx="6" class="node"/><text x="450.0" y="107.0" text-anchor="middle" class="label">case B: both sides always valid</text><text x="450.0" y="123.0" text-anchor="middle" class="label">disjunctive question</text><text x="450.0" y="139.0" text-anchor="middle" class="label">requirements on side 0 or side 1</text><rect x="20" y="196" width="260" height="48" rx="6" class="state"/><text x="150.0" y="216.0" text-anchor="middle" class="label">the stems on side i give an infinite</text><text x="150.0" y="232.0" text-anchor="middle" class="label">subset G of Aᵢ with C ≰ G′</text><rect x="320" y="196" width="260" height="48" rx="6" class="state"/><text x="450.0" y="216.0" text-anchor="middle" class="label">Lachlan’s disjunction: G₀ ⊆ A₀ with C ≰ G₀′</text><text x="450.0" y="232.0" text-anchor="middle" class="label">or G₁ ⊆ A₁ with C ≰ G₁′</text><line x1="260" y1="50" x2="160" y2="88" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><line x1="340" y1="50" x2="440" y2="88" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><line x1="150" y1="148" x2="150" y2="192" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><line x1="450" y1="148" x2="450" y2="192" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-cs-arr)"/><text x="200" y="74" text-anchor="end" class="label">yes</text><text x="400" y="74" class="label">no</text></svg>
:::

:::quiz[the construction]
In case A, why is it essential that side $i$ is valid in every extension of $p_0$?

- [x] Because promises turn into truth only through :ref{#lem-pigeon-promise}, which requires the side to be valid when the instance is handled; validity throughout makes every promise on side $i$ kept.
- [ ] Because the question of :ref{#def-pigeon-one-side} requires side $i$ to be valid.

  It requires a witness of invalidity of side $1 - i$; validity of side $i$ follows.
- [ ] Because otherwise $G_i$ would not be contained in $A_i$.

  The stems on side $i$ are always subsets of $A_i$.

---

Why can case B not use :ref{#lem-pigeon-one-side}?

- [x] Because in case B no side of any condition is invalid, so there is no witness of invalidity; the requirements must be disjunctive, and the side is chosen by the disjunctive question.
- [ ] Because :ref{#lem-pigeon-one-side} only applies to side $0$.

  It applies to either side, given a witness for the other.
- [ ] Because in case B the sets $G_0$ and $G_1$ are finite.

  Both are infinite in case B.

---

Where is the hypothesis $C \not\leq_T \emptyset'$ used?

- [x] Only in the choice of $\mathcal N$, a Scott ideal containing $\emptyset'$ and not $C$; the third case of :ref{#lem-pigeon-requirements} contradicts $C \notin \mathcal N$.
- [ ] In the choice of the low code $M$.

  $M$ exists for every $C$.
- [ ] In the construction of $S$.

  $S$ is computed by a set PA relative to $\emptyset'$, whatever $C$ is.
:::

:::corollary{#cor-pigeons-non-high}
Every set $A$ has an infinite subset $H$, of $A$ or of $\overline A$, that is not high. More generally, for every $Z$, $H$ can be chosen not high relative to $Z$.
:::

:::proof{of=cor-pigeons-non-high}
Apply :ref{#thm-pigeons-non-high} with $C = Z''$, which is not computable in $Z'$.
:::

By :ref{#ex-no-low2-subset}, "not high" cannot be improved to "low₂" for arbitrary sets $A$, and by :ref{#thm-dhls} not to "low" for $\Delta^0_2$ sets. For $\Delta^0_3$ sets, Monin and Patey proved that low₃ solutions exist, the analogue one level up of the theorem of Cholak, Jockusch and Slaman for $\Delta^0_2$ sets; the proof is beyond this course.

## Exercises

::::exercise{difficulty=2}
Deduce from :ref{#thm-pigeons-non-high} and :ref{#thm-coh-weakly-low} that $\mathsf{RT}^2_2$ admits jump cone avoidance, without using :ref{#thm-rt22-weakly-low}.

:::solution
Let $Z$ be a set, $C \not\leq_T Z'$, and $f$ a $Z$-computable coloring of pairs. The sequence $R_x = \{ y : f(\{x, y\}) = 1 \}$ is $Z$-computable. By :ref{#thm-coh-weakly-low} and item 3 of :ref{#prop-weakly-low-properties}, it has a cohesive set $G$ with $C \not\leq_T (Z \oplus G)'$. Let $p$ enumerate $G$ in increasing order, and $g(\{a, b\}) = f(\{p(a), p(b)\})$; it is stable by :ref{#thm-rt22-decomposition}, and computable in $Z \oplus G$. By :ref{#thm-pigeons-non-high} with $Z \oplus G$ in place of $Z$, applied to the limit set $A_g$, there is an infinite $K$ contained in $A_g$ or in its complement with $C \not\leq_T (Z \oplus G \oplus K)'$. By item 2 of :ref{#prop-srt-d22}, $g \oplus K$ computes an infinite homogeneous set $L$ for $g$, and $H = p[L]$ is homogeneous for $f$ and computable in $Z \oplus G \oplus K$. So $(Z \oplus H)' \leq_T (Z \oplus G \oplus K)'$, and $C \not\leq_T (Z \oplus H)'$.
:::
::::

::::exercise{difficulty=3}
Let $f$ be a function hyperimmune relative to $\emptyset'$. Show that every set $A$ has an infinite subset $H$, of $A$ or of $\overline A$, such that $f$ is hyperimmune relative to $H'$.

:::solution
Follow the proof of :ref{#thm-pigeons-non-high}, with the requirements "$\Phi^{G'}_e$ does not dominate $f$" in place of "$\Phi^{G'}_e \neq C$". The questions of :ref{#def-pigeon-disjunctive} and :ref{#def-pigeon-one-side} are compact in the sense of the second exercise of :ref{to="jump-cone-avoidance/sigma2-questions"}: writing "$\Phi^{G'}_e(m)\converge$" as $\exists \langle k, y \rangle\ \psi_{m,k}(y)$, where $\exists y\ \psi_{m,k}(y)$ expresses "$\Phi^{G'}_e(m)\converge < k$", the witness $\langle k, y \rangle$ found for a partition $B$ gives a positive answer for the sentence with bound $k$ on that partition, and, the class $\mathcal C$ being empty, compactness of Cantor space shows that finitely many witnesses serve for all partitions; their maximum $k$ gives a positive answer for "$\Phi^{G'}_e(m)\converge < k$". In case A, given a condition, let $g(m)$ be the first bound $k$ found with a positive answer for "$\Phi^{G'}_e(m)\converge < k$"; $g$ is partial computable in a member $Y$ of $\mathcal N$. Choose $\mathcal N$ such that $f$ is hyperimmune relative to every member of $\mathcal N$: build it as in the proof of :ref{#lem-scott-cone}, from $Z_0 = \emptyset'$, with $Z_{n+1} = Z_n \oplus P_n$ for a set $P_n$ PA relative to $Z_n$ such that every $Z_{n+1}$-computable function is dominated by a $Z_n$-computable one, by the computably dominated basis theorem (:ref{#thm-dominated-basis}) relativized to $Z_n$; by induction every member of $\mathcal N$ computes only functions dominated by $\emptyset'$-computable functions, which do not dominate $f$. If $g$ is total, $f(m) > g(m)$ for some $m$, and an extension makes $\Phi^{G'}_e(m) < f(m)$ on side $i$; if $g(m)$ is undefined, the question for "$\Phi^{G'}_e(m)\converge$" is negative, and an extension promises its negation. In case B, the same with pairs $(e_0, e_1)$ and the disjunctive question, the function $g(m)$ bounding both sides, followed by Lachlan's disjunction.
:::
::::

## Notes and references

:ref{#thm-pigeons-non-high} and :ref{#cor-pigeons-non-high} are due to Monin and Patey (2019); the same paper proves low₃ solutions for $\Delta^0_3$ sets and gives a simpler proof of Liu's theorem that every set has an infinite subset, of itself or of its complement, of non-PA degree. The proof given here follows the section *Pigeonhole principle* of the chapter *Jump cone avoidance* of Patey's monograph, with the cohesive classes of Le Houérou, Levy Patey and Mimouni (2024): the syntactic relation called a promise here is the monograph's syntactic forcing relation for $\Pi^0_2$ formulas, and the question on one side is its degenerate forcing question. The construction by sequences of conditions with tasks, instead of sufficiently generic filters, and the explicit case distinction are written here. The exercise on hyperimmunity is stated in the monograph, after Monin and Patey (2019).

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- B. Monin and L. Patey, *The weakness of the pigeonhole principle under hyperarithmetical reductions*, arXiv:1905.08425 (2019).
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Pigeonhole principle*.
