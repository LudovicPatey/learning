---
title: Scott families
summary: Three equivalent formulations of relative computable categoricity; Scott families of formulas defining the orbits of tuples over finitely many parameters, with examples; a c.e. Scott family of existential formulas makes a computable structure relatively computably categorical, by an effective back-and-forth argument.
duration: 30
prerequisites: [computable-structures/back-and-forth, intrinsic-definability/intrinsic-relations]
---

The rational order is computably categorical for a simple reason: the orbit of a tuple under automorphisms is described by its order type, a formula that every copy can check. The order $\omega$ is not computably categorical, and no finite description of this kind exists for it: the orbit of an element is determined by its number of predecessors, which an existential formula cannot express. This lesson and the next turn the contrast into a theorem. For the relative notion, where all copies are considered and not only the computable ones, the answer is exact: a structure is relatively computably categorical if and only if the orbits of its tuples are defined, over finitely many parameters, by a c.e. family of existential formulas. This lesson introduces these families and proves that they suffice, by a back-and-forth argument; the next one proves that they are necessary.

Throughout, $\mathcal A$ is a computable structure in a computable relational vocabulary, with domain $\nat$; a tuple of elements is a finite sequence of distinct elements, unless said otherwise.

## Three formulations

Recall from :ref{#def-computably-categorical} that $\mathcal A$ is relatively computably categorical if any two copies $\mathcal B$ and $\mathcal C$ are isomorphic by an isomorphism computable in $D(\mathcal B) \oplus D(\mathcal C)$. Since $\mathcal A$ itself is computable, it is enough to compare each copy with $\mathcal A$.

:::lemma{#lem-rcc-formulations}
For a computable structure $\mathcal A$, the following are equivalent.
1. $\mathcal A$ is relatively computably categorical.
2. For every copy $\mathcal B$, some isomorphism from $\mathcal A$ onto $\mathcal B$ is computable in $D(\mathcal B)$.
3. For every set $X$, any two copies of $\mathcal A$ computable in $X$ are isomorphic by an isomorphism computable in $X$.
:::

:::proof{of=lem-rcc-formulations}
(1) implies (2): take $\mathcal C = \mathcal A$, whose diagram is computable. (2) implies (3): if $\mathcal B$ and $\mathcal C$ are computable in $X$, there are isomorphisms $f : \mathcal A \to \mathcal B$ and $h : \mathcal A \to \mathcal C$ computable in $X$, and $h \circ f^{-1}$ is computable in $X$, since $f^{-1}(b)$ is found by searching for the $a$ with $f(a) = b$. (3) implies (1): given copies $\mathcal B$ and $\mathcal C$, apply (3) with $X = D(\mathcal B) \oplus D(\mathcal C)$.
:::

The third formulation explains the name: $\mathcal A$ is computably categorical relative to every oracle. For a structure obtained by a natural construction, a proof of computable categoricity usually relativizes, and so proves relative categoricity. The two notions nevertheless differ, as the lesson on relative and plain categoricity shows.

## Scott families

:::definition{#def-scott-family}
Let $\bar p$ be a tuple of $\mathcal A$. A **Scott family over $\bar p$** is a set $\Phi$ of first-order formulas $\varphi(\bar p, \bar x)$, with the parameters $\bar p$, such that
1. every tuple $\bar a$ of $\mathcal A$ satisfies some formula of $\Phi$;
2. if two tuples $\bar a$ and $\bar b$ satisfy the same formula of $\Phi$, some automorphism of $\mathcal A$ fixes $\bar p$ pointwise and maps $\bar a$ to $\bar b$.

It is **existential** if its formulas are existential, and **c.e.** if the set of indices of its formulas is c.e.
:::

Each formula of a Scott family that is satisfied by some tuple $\bar a$ defines the orbit of $\bar a$ under the automorphisms fixing $\bar p$: the tuples that satisfy it are in this orbit, by (2), and the orbit is contained in the set of tuples satisfying it, since automorphisms fixing $\bar p$ preserve formulas with parameters $\bar p$. Montalbán calls a structure with a c.e. existential Scott family over $\bar p$ **effectively $\exists$-atomic** over $\bar p$.

:::example{#ex-scott-families}
1. On $(\mathbb Q; <)$, the formulas describing the order type of a tuple, such as $x_1 < x_0 < x_2$, form a c.e. Scott family without parameters: two tuples of the same order type are automorphic, by the back-and-forth argument of :ref{#thm-effective-cantor}, started from the partial isomorphism between them. The formulas are quantifier-free.
2. On the successor structure $(\nat; S)$, with parameter $p = 0$, let $\varphi_n(p, x)$ say that $x$ is reached from $p$ by $n$ steps: for $n \geq 1$, $\exists z_1 \ldots z_{n-1}\, (S(p, z_1) \wedge S(z_1, z_2) \wedge \cdots \wedge S(z_{n-1}, x))$, and $x = p$ for $n = 0$. Each element satisfies exactly one $\varphi_n$, and the structure is rigid; the conjunctions of such formulas for the entries of a tuple form a c.e. existential Scott family over $0$.
3. On the order $\omega = (\nat; \leq)$, which is rigid, the orbit of $n$ is $\{n\}$, and it is defined by a first-order formula without parameters: "$x$ has exactly $n$ predecessors". This formula is not existential, and no existential formula with parameters defines $\{n\}$ once $n$ is larger than the parameters (:ref{#ex-omega-no-scott}).
:::

::::exercise{#ex-omega-no-scott difficulty=1 objective="See why existential formulas cannot pin down an element of ω, by moving witnesses upward."}
Let $\bar p$ be a tuple of $\omega = (\nat; \leq)$ and $n > \max \bar p$. Show that every existential formula $\exists \bar y\, \psi(\bar p, x, \bar y)$, with $\psi$ quantifier-free, that holds of $n$ also holds of $n + 1$. Deduce that $\omega$ has no existential Scott family over any tuple.

:::solution
Let $\bar m$ be witnesses for $n$: $\psi(\bar p, n, \bar m)$ holds. The map $h(t) = t$ for $t < n$ and $h(t) = t + 1$ for $t \geq n$ is an order-preserving injection of $\nat$ into itself, and it fixes $\bar p$, since all entries of $\bar p$ are below $n$. A quantifier-free formula in the vocabulary $\{\leq\}$ is a Boolean combination of formulas $u \leq v$ and $u = v$, which an order-preserving injection preserves in both directions. So $\psi(\bar p, n + 1, h(\bar m))$ holds, and $n + 1$ satisfies the existential formula, with witnesses $h(\bar m)$. If $\Phi$ were an existential Scott family over $\bar p$, the formula of $\Phi$ satisfied by $n$ would be satisfied by $n + 1$, and $n$, $n + 1$ would be automorphic; but $\omega$ is rigid.
:::
::::

## From Scott families to isomorphisms

:::proposition{#prop-scott-rcc}
If a computable structure $\mathcal A$ has a c.e. existential Scott family over some tuple, then it is relatively computably categorical.
:::

**Intuition.** A copy can recognize where to send each element: it searches for a formula of the family and for witnesses to it, as in Cantor's argument, with the formula playing the role of the order type. Existential formulas are exactly those whose truth a copy can confirm by a finite search.

:::proof{of=prop-scott-rcc}
Let $\Phi$ be a c.e. existential Scott family over $\bar p$, and $\mathcal B$ a copy of $\mathcal A$. Fix an isomorphism $f : \mathcal A \to \mathcal B$ and let $\bar q = f(\bar p)$, a finite piece of non-uniform information. For a formula $\varphi(\bar p, \bar x)$ of $\Phi$, write $\varphi(\bar q, \bar x)$ for the same formula over $\mathcal B$ with parameters $\bar q$.

We build finite maps $r_0 \subseteq r_1 \subseteq \cdots$ from $\mathcal A$ to $\mathcal B$, with the invariant: $r_s$ maps a tuple $\bar a$ to a tuple $\bar b$ such that some $\varphi \in \Phi$ satisfies $\mathcal A \models \varphi(\bar p, \bar a)$ and $\mathcal B \models \varphi(\bar q, \bar b)$. Let $r_0$ be empty, with the empty tuple, which satisfies a formula of $\Phi$ in both structures (any formula satisfied in $\mathcal A$ by the empty tuple is a sentence with parameters $\bar p$, true in $\mathcal B$ with $\bar q$).

The invariant implies that some isomorphism $\mathcal A \to \mathcal B$ extends $r_s$ and maps $\bar p$ to $\bar q$. Indeed, $\mathcal B \models \varphi(\bar q, \bar b)$ gives $\mathcal A \models \varphi(\bar p, f^{-1}(\bar b))$, since $f^{-1}$ maps $\bar q$ to $\bar p$; then $\bar a$ and $f^{-1}(\bar b)$ satisfy the same formula of $\Phi$, so some automorphism $\alpha$ of $\mathcal A$ fixing $\bar p$ maps $\bar a$ to $f^{-1}(\bar b)$, and $f \circ \alpha$ is the required isomorphism.

*Forth.* Given $r_s : \bar a \mapsto \bar b$ and the least element $c$ of $\mathcal A$ not in $\bar a$, search for a formula $\varphi \in \Phi$ and an element $d$ of $\mathcal B$ such that $\mathcal A \models \varphi(\bar p, \bar a c)$ and $\mathcal B \models \varphi(\bar q, \bar b d)$. Both conditions are c.e. in $D(\mathcal B)$: $\Phi$ is c.e., $\mathcal A$ is computable, and an existential formula is checked by finding witnesses. The search terminates: if $g \supseteq r_s$ is an isomorphism mapping $\bar p$ to $\bar q$, then $d = g(c)$ works with any formula of $\Phi$ satisfied by $\bar a c$, since $g$ maps $\bar p \bar a c$ to $\bar q \bar b d$. Let $r_{s+1} = r_s \cup \{ (c, d) \}$; the invariant holds.

*Back.* Symmetrically, given the least element $d$ of $\mathcal B$ not in the range, search for $\varphi$ and $c$ with the same two properties.

Alternating forth and back steps, $r = \bigcup_s r_s$ is a bijection; it preserves the atomic formulas, since each $r_s$ extends to an isomorphism; and it is computable in $D(\mathcal B)$, with $\bar q$ as finite information. By :ref{#lem-rcc-formulations}, $\mathcal A$ is relatively computably categorical.
:::

:::quiz[Scott families and isomorphisms]
In the proof that a Scott family gives isomorphisms, where is it used that the formulas of $\Phi$ are existential?

- [x] To make the search through $\mathcal B$ effective in $D(\mathcal B)$: an existential formula is verified by finding witnesses, so its truth is c.e. in the diagram.
- [ ] To guarantee that the search terminates.

  Termination comes from the existence of an isomorphism extending $r_s$; it would hold for formulas of any complexity.
- [ ] To show that tuples satisfying the same formula are automorphic.

  This is clause (2) of the definition of a Scott family, assumed of $\Phi$.

---

Why does the construction start from the image $\bar q = f(\bar p)$ of the parameters under some isomorphism, rather than from any tuple of $\mathcal B$?

- [x] The formulas of $\Phi$ define orbits over $\bar p$; they can be transferred to $\mathcal B$ only over a tuple that plays the same role as $\bar p$, that is, satisfies $(\mathcal B, \bar q) \cong (\mathcal A, \bar p)$.
- [ ] Because $\bar q$ must be computable from $D(\mathcal B)$.

  A finite tuple is always computable; the point is that it must correspond to $\bar p$ under an isomorphism.
- [ ] Because the empty map must extend to an isomorphism.

  The empty map always does; the parameters matter for the later steps.
:::

The isomorphism is obtained from $D(\mathcal B)$ and the image $\bar q$ of the parameters: the only non-uniformity is the choice of $\bar q$. When the Scott family has no parameters, the same procedure works for all copies at once; such structures are called **uniformly relatively computably categorical**. Examples are the rational order and the random graph (:ref{#ex-random-graph-scott}).

## Notes and references

The notion of a Scott family comes from Scott's isomorphism theorem for countable structures, in which the orbits are defined by infinitary formulas; its effective versions, with finitary existential formulas, are due to Goncharov (1975) and to Ash, Knight, Manasse and Slaman (1989). :ref{#prop-scott-rcc} is the easy direction of their characterization, proved in the next lesson; see Montalbán, Sections III.4 and VIII.2, and Ash–Knight, Chapter 10.

- C. J. Ash, J. F. Knight, M. Manasse and T. A. Slaman, *Generic copies of countable structures*, Annals of Pure and Applied Logic 42 (1989), 195–205.
- S. S. Goncharov, *Autostability and computable families of constructivizations*, Algebra and Logic 14 (1975), 392–408.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Sections III.4 and VIII.2.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 10.

:::::exercises
::::exercise{#ex-random-graph-scott difficulty=1 objective="Write a Scott family for a homogeneous structure and recover its categoricity from it."}
Show that the quantifier-free formulas describing which pairs of a tuple are adjacent and which entries are equal form a c.e. Scott family without parameters for the random graph, and deduce from :ref{#prop-scott-rcc} that the random graph is relatively computably categorical.

:::solution
Two tuples $\bar a$ and $\bar b$ of the same length satisfying the same such formula determine a finite partial isomorphism $a_i \mapsto b_i$. By the extension property, every finite partial isomorphism extends: the back-and-forth argument of :ref{#ex-random-graph}, started from it, gives an automorphism mapping $\bar a$ to $\bar b$. Every tuple satisfies the formula describing its own adjacencies. The formulas are quantifier-free, hence existential, and they form a computable set. By :ref{#prop-scott-rcc}, the random graph is relatively computably categorical, and since there are no parameters, uniformly so.
:::
::::

::::exercise{#ex-integers-scott difficulty=1 objective="Find an existential Scott family with one parameter for a rigid-like structure and compare with the order."}
Show that $(\mathbb Z; S)$, the integers with the successor relation, has a c.e. existential Scott family over the tuple $(0)$, and that the order $(\mathbb Z; \leq)$ has no existential Scott family over any tuple.

:::solution
For $n \in \mathbb Z$, let $\varphi_n(p, x)$ say that $x$ is reached from $p$ by $n$ steps of $S$ if $n \geq 0$, or that $p$ is reached from $x$ by $-n$ steps if $n < 0$, written with existential quantifiers over the intermediate elements as in :ref{#ex-scott-families}. Each integer $m$ satisfies exactly $\varphi_m(0, x)$, and an automorphism fixing $0$ is the identity; the conjunctions of such formulas for the entries of a tuple form a c.e. existential Scott family over $0$. For the order, let $\bar p$ be a tuple and $n > \max \bar p$. The map fixing every $t < n$ and sending $t \geq n$ to $t + 1$ is an order-preserving injection of $\mathbb Z$ into itself fixing $\bar p$, so, as in :ref{#ex-omega-no-scott}, every existential formula over $\bar p$ true of $n$ is true of $n + 1$. An automorphism of $(\mathbb Z; \leq)$ fixing $\bar p$ is a translation fixing a point, the identity; so $n$ and $n + 1$ are not automorphic over $\bar p$.
:::
::::
:::::
