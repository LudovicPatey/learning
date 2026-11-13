---
title: Questions for Σ⁰₂ sentences on two sides
summary: For the forcing with a cohesive class, Π⁰₂ sentences are promised through the question on stems and become true on sides that stay valid; a disjunctive question for Σ⁰₂ sentences ranges over all partitions of the reservoir; a question on one side uses a witness that the other side is invalid; both have answers Σ⁰₁ relative to a member of the ideal.
duration: 35
prerequisites: [pigeonhole-forcing]
---

This lesson continues the proof of :ref{#thm-pigeons-non-high}. The setting of :ref{to="jump-cone-avoidance/pigeonhole-forcing"} is fixed: the ideals $\mathcal M \subseteq \mathcal N$, the $\mathcal M$-cohesive class $\mathcal U_S$ with $S \in \mathcal N$, its core $\mathcal U$, the set $A$ with $A_0 = A$ and $A_1 = \overline A$, the conditions $(\sigma_0, \sigma_1, X)$, and the question $\sigma \mathrel{?{\vdash}} \varphi$ for $\Sigma^0_1$ sentences. Three tools for second-jump control are added: a syntactic relation for $\Pi^0_2$ sentences, the **promise**, which becomes truth on the sides that stay valid; a **disjunctive question** for $\Sigma^0_2$ sentences, for use when both sides stay valid; and a **question on one side**, for use when the other side has become invalid. Both questions have answers $\Sigma^0_1$ relative to a member of $\mathcal N$, which is what the three-case argument of :ref{#thm-local-jump-cone} needs. The next lesson assembles them.

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

Item 1 gives a property of all members, and needs no validity. Item 2 gives only a promise, on a side $i$ that is not under control: it is useful only if side $i$ stays valid. When both sides stay valid forever, the disjunctive question plays the role, one level up, of a disjunctive forcing question (:ref{#def-disjunctive-notion}), with promises in place of forcing on all members.

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

1. Take $B = A$, so that $B^{1-i} = X \cap A_{1-i}$, which is not in $\mathcal V$. There are $m$ and $\tau$ compatible with $(\sigma_i, X \cap A_i)$ with $\tau \mathrel{?{\nvdash}} \neg\psi(m)$, and the proof of item 1 of :ref{#lem-pigeon-disjunctive} applies.
2. Let $\mathcal C$ be the class of sets $B$ with $B^{1-i} \notin \mathcal V$ such that $\tau \mathrel{?{\vdash}} \neg\psi(m)$ for all $m$ and all $\tau$ compatible with $(\sigma_i, B^i)$. The condition $B^{1-i} \notin \mathcal V$ is $\Pi^0_1(X \oplus W)$, so $\mathcal C$ is a $\Pi^0_1(X \oplus W \oplus S \oplus M')$ class, non-empty by hypothesis, with a member $B \in \mathcal N$. Now $B^{1-i} \notin \mathcal V \supseteq \mathcal U$, so $B^{1-i} \notin \mathcal U$; as $B^0, B^1$ cover $X \in \mathcal U$, $B^i \in \mathcal U$. The condition $(\sigma_0, \sigma_1, B^i)$ extends $p$ and promises $\neg\varphi$ on side $i$.
3. The question holds if and only if $\mathcal C$ is empty, a $\Sigma^0_1(Y)$ property for $Y = X \oplus W \oplus S \oplus M' \in \mathcal N$.
:::

The witness forces the partition to put its large part on side $i$: this is how a question on one side can be answered by a partition, although the partition does not know $A$.

## Notes and references

The syntactic relation called a promise here is the syntactic forcing relation for $\Pi^0_2$ formulas of the section *Pigeonhole principle* of the chapter *Jump cone avoidance* of Patey's monograph, and the question on one side is its degenerate forcing question. The monograph states the disjunctive question for conditions with both sides valid; the positive case needs no validity, as noted after :ref{#lem-pigeon-disjunctive}. The strings compatible with $(\sigma_i, B^i)$ replace the finite sets $\rho \subseteq B^i$ of the monograph, so that the use principle applies to the members.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Pigeonhole principle*.
