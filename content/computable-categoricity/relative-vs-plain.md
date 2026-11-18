---
title: Relative and plain categoricity
summary: Computable categoricity on a cone, for all oracles above a fixed one, is equivalent to an existential Scott family over parameters, with no effectiveness condition; natural structures behave in the same way for all three notions; categoricity for decidable copies and effective atomicity; Goncharov's computably categorical structure that is not relatively computably categorical.
duration: 20
prerequisites: [classical-examples, computable-structures/computable-models]
---

Relative computable categoricity has a structural characterization; plain computable categoricity, which only considers computable copies, has none in general: its index set is $\Pi^1_1$-complete. Between the two notions there is a gap, which this lesson and the next describe from both sides. If the oracles are allowed to grow, the gap disappears: categoricity relative to all oracles above a fixed one is equivalent to the existence of an existential Scott family, with no effectiveness condition. The structures in the gap must therefore be built against the computable functions themselves, and Goncharov built one. The next lesson shows that, for structures that are effective enough, the gap disappears as well.

## Categoricity on a cone

:::definition{#def-cc-cone}
A countable structure $\mathcal A$ is **computably categorical on a cone** if there is a set $Y$ such that, for every $X \geq_T Y$, any two copies of $\mathcal A$ computable in $X$ are isomorphic by an isomorphism computable in $X$.
:::

By :ref{#lem-rcc-formulations}, a relatively computably categorical structure is computably categorical on a cone, with $Y = \emptyset$. The definition, however, applies to all countable structures, computable or not, and it ignores the properties of the structure that depend on the particular oracles below $Y$.

:::theorem[Montalbán]{#thm-cc-cone}
A countable structure is computably categorical on a cone if and only if it has an existential Scott family over some tuple.
:::

:::proof{of=thm-cc-cone}
Suppose that $\Phi$ is an existential Scott family over $\bar p$, and let $\mathcal A_0$ be a copy of the structure. A Scott family is a countable set of formulas; let $Y = D(\mathcal A_0) \oplus \Phi$, where $\Phi$ stands for the set of indices of its formulas. Then $\mathcal A_0$ is computable in $Y$ and $\Phi$ is c.e. in $Y$, so by the relativized form of :ref{#prop-scott-rcc}, every copy $\mathcal B$ is isomorphic to $\mathcal A_0$ by an isomorphism computable in $Y \oplus D(\mathcal B)$. If $X \geq_T Y$ and $\mathcal B$, $\mathcal C$ are copies computable in $X$, composing two such isomorphisms gives an isomorphism between $\mathcal B$ and $\mathcal C$ computable in $X$.

Conversely, let $Y$ witness categoricity on a cone, let $\mathcal A_0$ be a copy, and $Z = Y \oplus D(\mathcal A_0)$. For any copy $\mathcal B$, the set $X = Z \oplus D(\mathcal B)$ is above $Y$ and computes $\mathcal A_0$ and $\mathcal B$, so some isomorphism between them is computable in $Z \oplus D(\mathcal B)$. By the relativized form of :ref{#thm-rcc-scott}, $\mathcal A_0$, which is computable in $Z$, has an existential Scott family over some tuple, c.e. in $Z$.
:::

:::quiz[categoricity on a cone]
In the first half of the proof of :ref{#thm-cc-cone}, why does $Y$ include the diagram of a copy $\mathcal A_0$?

- [x] The relativized form of :ref{#prop-scott-rcc} applies to a structure computable in the oracle; the structure may have no computable copy, and $Y$ must compute one.
- [ ] To make the Scott family existential.

  The family is existential by hypothesis; $Y$ only needs to compute a copy and enumerate the family.
- [ ] Because every copy computes $Y$.

  Copies need not compute $Y$; the cone is above $Y$, and $Y$ is chosen to compute $\mathcal A_0$.

---

In the second half, why is the oracle $X = Z \oplus D(\mathcal B)$ used?

- [x] It lies in the cone above $Y$ and computes both $\mathcal A_0$ and $\mathcal B$, so categoricity relative to $X$ gives an isomorphism computable in $Z \oplus D(\mathcal B)$, the hypothesis of the relativized :ref{#thm-rcc-scott}.
- [ ] Because $\mathcal B$ is computable.

  $\mathcal B$ is an arbitrary copy; the oracle is chosen to compute it.
- [ ] To make $Z$ above $Y$.

  $Z = Y \oplus D(\mathcal A_0)$ is above $Y$ by definition.
:::


So, on a cone, computable categoricity is a property of the isomorphism type alone, and it is decided by definability: are the orbits defined by existential formulas over finitely many parameters? The condition is also equivalent to the existence of a Scott sentence of a certain low complexity (Montalbán, Theorem VIII.8; see the course on Scott analysis).

The theorem explains the classical results of the previous lesson. A proof that a natural structure is, or is not, computably categorical usually relativizes to every oracle, and then it proves the statement on a cone. For such structures, plain categoricity, relative categoricity and categoricity on a cone coincide, and the structural condition decides all three. A structure for which they differ must be built against the computable functions themselves, as in Goncharov's example below.

## Decidable copies

Recall from the course on computable structures that an ω-presentation is **decidable** if its elementary diagram, the set of first-order formulas true of its elements, is computable. Studying decidable copies is natural in effective model theory, where a structure is given by its theory.

:::definition{#def-effectively-atomic}
Let $\mathcal A$ be a structure and $\bar p$ a tuple. A formula $\varphi(\bar p, \bar x)$ **generates the type** of a tuple $\bar a$ over $\bar p$ if $\mathcal A \models \varphi(\bar p, \bar a)$ and, for every first-order formula $\theta(\bar p, \bar x)$ true of $\bar a$, $\mathcal A \models \forall \bar x\, (\varphi(\bar p, \bar x) \to \theta(\bar p, \bar x))$. The structure is **effectively atomic over $\bar p$** if there is a c.e. set $\Phi$ of formulas such that every tuple $\bar a$ satisfies some formula of $\Phi$, and every formula of $\Phi$ satisfied by $\bar a$ generates its type over $\bar p$. It is **computably categorical for decidable copies** if any two decidable copies are computably isomorphic.
:::

:::proposition{#prop-atomic-decidable-cc}
A decidable structure that is effectively atomic over some tuple is computably categorical for decidable copies.
:::

The proof is the back-and-forth argument of :ref{#prop-scott-rcc}, with complete types in place of orbits.

:::proof{of=prop-atomic-decidable-cc}
Let $\Phi$ witness effective atomicity over $\bar p$, and let $\mathcal B$ be a decidable copy; fix $\bar q$ in $\mathcal B$ with the same type as $\bar p$, the image of $\bar p$ under an isomorphism. Build finite maps $\bar a \mapsto \bar b$ with the invariant that some $\varphi \in \Phi$ satisfies $\mathcal A \models \varphi(\bar p, \bar a)$ and $\mathcal B \models \varphi(\bar q, \bar b)$. Since $(\mathcal B, \bar q)$ and $(\mathcal A, \bar p)$ satisfy the same formulas, and $\varphi$ generates the type of $\bar a$ over $\bar p$, the invariant says that $\bar p \bar a$ and $\bar q \bar b$ have the same type. To go forth with a new element $c$, find $\varphi' \in \Phi$ true of $\bar a c$, which is decidable in $\mathcal A$, and then $d$ in $\mathcal B$ with $\mathcal B \models \varphi'(\bar q, \bar b d)$, which is decidable in $\mathcal B$; such a $d$ exists because $\exists y\, \varphi'(\bar p, \bar a, y)$ belongs to the type of $\bar a$, hence holds of $\bar b$ over $\bar q$. Going back is symmetric. The union is a computable isomorphism. Two decidable copies are thus both computably isomorphic to $\mathcal A$, hence to each other.
:::

The converse is Nurtazin's theorem, the subject of the next lesson. Its proof must build a decidable copy, so the generic copy used for :ref{#thm-rcc-scott} is not available.

## When the notions differ

:::theorem[Goncharov]{#thm-goncharov-cc-not-rcc}
There is a computable structure that is computably categorical but not relatively computably categorical.
:::

We admit the theorem; Goncharov's proof codes a family of c.e. sets with special enumerations into a graph, by a finite injury construction (Montalbán, Theorem VIII.14). The structure is built by diagonalization against the computable functions; its categoricity is a property of the computable copies only, not of the isomorphism type, and its proof does not relativize. Its existence also shows that relative categoricity cannot be replaced by plain categoricity in :ref{#thm-rcc-scott}. The next lesson shows that this cannot happen for structures that are effective enough.

::::exercise{#ex-cone-omega difficulty=1 objective="Apply the characterization on a cone to a structure that is not computably categorical."}
Show that $\omega = (\nat; \leq)$ is not computably categorical on a cone, while $(\mathbb Q; <)$ is.

:::solution
By :ref{#ex-omega-no-scott}, $\omega$ has no existential Scott family over any tuple, so by :ref{#thm-cc-cone} it is not computably categorical on a cone. The order types of tuples form a Scott family of quantifier-free formulas for $(\mathbb Q; <)$ (:ref{#ex-scott-families}), so it is computably categorical on a cone; it is in fact relatively computably categorical, so $Y = \emptyset$ works.
:::
::::

## Notes and references

:ref{#thm-cc-cone} is Montalbán, Theorem VIII.8, where a third equivalent condition, on Scott sentences, is added. :ref{#thm-goncharov-cc-not-rcc} is Goncharov (1977). The Π¹₁-completeness of computable categoricity is due to Downey, Kach, Lempp, Lewis-Pye, Montalbán and Turetsky (2015).

- S. S. Goncharov, *The quantity of non-autoequivalent constructivizations*, Algebra and Logic 16 (1977), 169–185.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Sections VIII.3 and VIII.5.

:::::exercises

::::exercise{#ex-cone-linear-orders difficulty=1 objective="Read off categoricity on a cone from the proofs of the previous lesson." lessons="classical-examples"}
Show that a countable linear order, computable or not, is computably categorical on a cone if and only if it has finitely many adjacent pairs.

:::solution
By :ref{#thm-cc-cone}, the question is whether the order has an existential Scott family over some tuple. The proof of :ref{#thm-lo-rcc} answers it without using computability. With finitely many adjacent pairs, the order types over the tuple $\bar p$ listing the set $P$ of :ref{#lem-finite-adjacencies} form a Scott family of quantifier-free formulas. With infinitely many, the second part of the proof shows that for every tuple $\bar p$, some existential formula over $\bar p$ true of an adjacent pair is also true of a non-adjacent pair; so there is no existential Scott family over any tuple.
:::
::::
:::::
