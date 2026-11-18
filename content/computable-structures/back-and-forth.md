---
title: The effective back-and-forth method
summary: Computable isomorphisms between copies; Cantor's back-and-forth argument made effective, so that any two copies of the rational order are isomorphic by a map computable from their diagrams; computably categorical structures (the rationals, the random graph, finite-dimensional vector spaces, the successor structure) and structures that are not (the order ω, which is Δ⁰₂-categorical); what makes the method effective.
duration: 25
prerequisites: [presentations]
---

Two computable copies of the same structure may fail to be computably isomorphic, as the two copies of $\omega$ of the first lesson show. The second basic question of the subject is therefore: for which structures are all computable copies computably isomorphic? This lesson answers it for the first examples, with the tool that proves most isomorphism theorems for countable structures, Cantor's back-and-forth argument. When the argument only needs finite, decidable information at each step, it is computable, and the structure is computably categorical. The course on computable categoricity turns this observation into a general theory.

## Computable categoricity

:::definition{#def-computably-categorical}
A computable structure $\mathcal A$ is **computably categorical** if any two computable copies of $\mathcal A$ are isomorphic by a computable isomorphism. It is **relatively computably categorical** if any two copies $\mathcal B$ and $\mathcal C$, not necessarily computable, are isomorphic by an isomorphism computable in $D(\mathcal B) \oplus D(\mathcal C)$. More generally, $\mathcal A$ is **$\Delta^0_n$-categorical** if any two computable copies are isomorphic by an isomorphism computable in $\emptyset^{(n-1)}$.
:::

Since composing isomorphisms preserves computability, $\mathcal A$ is computably categorical if and only if every computable copy is computably isomorphic to one fixed computable copy. By :ref{#prop-two-copies-omega}, the order $\omega = (\nat; \leq)$ is not computably categorical.

## Cantor's argument, effectively

A **finite partial isomorphism** from $\mathcal B$ to $\mathcal C$ is a finite map $p$ from elements of $\mathcal B$ to elements of $\mathcal C$ that preserves the atomic formulas: for every atomic formula $\varphi$ and tuple $\bar b$ in the domain of $p$, $\mathcal B \models \varphi(\bar b) \iff \mathcal C \models \varphi(p(\bar b))$. For linear orders, this means that $p$ preserves the order.

:::theorem[Cantor]{#thm-effective-cantor}
Let $\mathcal B$ and $\mathcal C$ be two copies of $(\mathbb Q; <)$, that is, countable dense linear orders without endpoints. There is an isomorphism between them computable in $D(\mathcal B) \oplus D(\mathcal C)$. In particular, $(\mathbb Q; <)$ is relatively computably categorical.
:::

**Intuition.** Build the isomorphism as a union of finite partial isomorphisms, alternating two kinds of steps: going forth, put the least unmatched element of $\mathcal B$ in the domain; going back, put the least unmatched element of $\mathcal C$ in the range. To match a new element, one only needs its position relative to the finitely many elements already matched, and some element of the other copy in the corresponding position; density and the absence of endpoints guarantee that one exists, and the diagrams let us recognize it.

:::figure[A step forth in the proof of :ref{#thm-effective-cantor}. The finite partial isomorphism $p$ matches $a_1 < a_2 < a_3$ with $b_1 < b_2 < b_3$. The new element $a$ lies between $a_2$ and $a_3$; the search through $\mathcal B$ finds an element $b$ between $b_2$ and $b_3$, which exists by density, and $p$ is extended by $a \mapsto b$.]
<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="Two copies of the rationals drawn as horizontal lines. A finite partial isomorphism matches a1, a2, a3 with b1, b2, b3. A new element a of the first copy lies between a2 and a3; the search finds an element b of the second copy between b2 and b3, and a is matched with b"><defs><marker id="bf-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="66" y1="70" x2="560" y2="70" class="muted-stroke" stroke-width="1.2"/><text x="8" y="74" class="label">copy 𝒜</text><line x1="66" y1="190" x2="560" y2="190" class="muted-stroke" stroke-width="1.2"/><text x="8" y="194" class="label">copy ℬ</text><line x1="90" y1="78" x2="130" y2="182" class="muted-stroke" stroke-width="1.1" stroke-dasharray="4 3"/><circle cx="90" cy="70" r="6" class="node"/><text x="90" y="56" text-anchor="middle" class="math">a₁</text><circle cx="130" cy="190" r="6" class="node"/><text x="130" y="214" text-anchor="middle" class="math">b₁</text><line x1="230" y1="78" x2="300" y2="182" class="muted-stroke" stroke-width="1.1" stroke-dasharray="4 3"/><circle cx="230" cy="70" r="6" class="node"/><text x="230" y="56" text-anchor="middle" class="math">a₂</text><circle cx="300" cy="190" r="6" class="node"/><text x="300" y="214" text-anchor="middle" class="math">b₂</text><line x1="420" y1="78" x2="470" y2="182" class="muted-stroke" stroke-width="1.1" stroke-dasharray="4 3"/><circle cx="420" cy="70" r="6" class="node"/><text x="420" y="56" text-anchor="middle" class="math">a₃</text><circle cx="470" cy="190" r="6" class="node"/><text x="470" y="214" text-anchor="middle" class="math">b₃</text><circle cx="330" cy="70" r="7" class="head-cell"/><text x="330" y="56" text-anchor="middle" class="math">a</text><rect x="306" y="178" width="158" height="24" rx="5" class="soft-fill"/><circle cx="360" cy="190" r="5" class="node"/><circle cx="390" cy="190" r="7" class="head-cell"/><text x="390" y="214" text-anchor="middle" class="math">b</text><circle cx="430" cy="190" r="5" class="node"/><line x1="330" y1="79" x2="388" y2="179" class="accent-stroke" stroke-width="1.8" marker-end="url(#bf-arrow)"/><text x="592" y="252" text-anchor="end" class="label">search ℬ for an element between b₂ and b₃</text><text x="8" y="252" class="label">dashed: the partial isomorphism p</text></svg>
:::

:::proof{of=thm-effective-cantor}
We define finite partial isomorphisms $p_0 \subseteq p_1 \subseteq \cdots$, starting from the empty map. At step $2s$, let $b$ be the least element of $\mathcal B$ not in the domain of $p_{2s}$. Using $D(\mathcal B)$, find the position of $b$ relative to the domain $b_1 < \cdots < b_k$ of $p_{2s}$: below $b_1$, between $b_i$ and $b_{i+1}$, or above $b_k$. Search through $\mathcal C$, using $D(\mathcal C)$, for an element $c$ in the corresponding position relative to $p_{2s}(b_1) < \cdots < p_{2s}(b_k)$. It exists: if the position is between $b_i$ and $b_{i+1}$, by density of $\mathcal C$, and if it is below or above all, since $\mathcal C$ has no endpoints. Let $p_{2s+1} = p_{2s} \cup \{ (b, c) \}$, which is again a partial isomorphism. Step $2s + 1$ is symmetric, with the least element of $\mathcal C$ not in the range. The union $f = \bigcup_s p_s$ is an order-preserving bijection, since every element of $\mathcal B$ enters the domain and every element of $\mathcal C$ the range, and it is computable in $D(\mathcal B) \oplus D(\mathcal C)$, since each step is a search that terminates.
:::

:::quiz[the effective back-and-forth argument]
Why does the construction alternate between steps forth and back, rather than only going forth?

- [x] Going forth alone defines a map on all of $\mathcal B$ that preserves the order, but its range may miss elements of $\mathcal C$; the steps back make it onto.
- [ ] Because going forth alone would not be computable.

  Each forth step is computable; what fails is surjectivity.
- [ ] Because the search might not terminate otherwise.

  The search terminates at every step, by density and the absence of endpoints.

---

Where is it used that the order of $\mathcal C$ is decidable from $D(\mathcal C)$?

- [x] To recognize, during the search, an element in the required position relative to the finitely many elements already matched: this position is described by finitely many atomic facts.
- [ ] To know that $\mathcal C$ is dense.

  Density is a property of the isomorphism type, known in advance; the diagram is used to locate elements.
- [ ] To find the least unmatched element of $\mathcal C$.

  The least unmatched element is found from the finite map, without the diagram.
:::

The same method applies whenever the following holds: given a finite partial isomorphism that extends to an isomorphism, and a new element, the elements of the other copy that can be matched with it are recognizable by a search using the diagrams. Three examples:

:::example{#ex-computably-categorical}
1. **The random graph**, the countable graph in which, for all disjoint finite sets $U$ and $V$ of vertices, some vertex is adjacent to every vertex of $U$ and to none of $V$. Every finite partial isomorphism extends, by this extension property, and a matching vertex is found by search. So the random graph is relatively computably categorical (:ref{#ex-random-graph}).
2. **Finite-dimensional vector spaces.** Let $\mathcal V$ and $\mathcal W$ be copies of $\mathbb Q^n$, and fix bases $\bar v$ and $\bar w$, finitely many parameters. Every element of $\mathcal V$ is a rational combination of $\bar v$, found by search; send it to the same combination of $\bar w$. This isomorphism is computable from the diagrams and the two bases.
3. **The successor structure** $(\nat; S)$, in which $S$ is the graph of $n \mapsto n + 1$. Given a copy, name as a parameter its first element, the only one with no predecessor; then the element corresponding to $n$ is reached by $n$ steps of $S$, which the diagram computes. So $(\nat; S)$ is relatively computably categorical, while $(\nat; \leq)$, which has the same isomorphisms, is not computably categorical: the successor relation is computable in one presentation and not in the others.
:::

The second and third examples use parameters, a finite amount of non-uniform information: the bases, the first element. The definition of computable categoricity allows this.

## A structure that is Δ⁰₂-categorical

The order $\omega$ is not computably categorical, but its isomorphisms are not far from computable.

:::proposition{#prop-omega-delta2}
Any two copies $\mathcal B$ and $\mathcal C$ of $(\nat; \leq)$ are isomorphic by an isomorphism computable in $(D(\mathcal B) \oplus D(\mathcal C))'$. In particular, $\omega$ is $\Delta^0_2$-categorical.
:::

:::proof{of=prop-omega-delta2}
The unique isomorphism sends the element of $\mathcal B$ with exactly $n$ predecessors to the element of $\mathcal C$ with exactly $n$ predecessors. "$b$ has at least $n$ predecessors" is a $\Sigma^0_1$ property relative to $D(\mathcal B)$, and "$b$ has at most $n$ predecessors" a $\Pi^0_1$ one, so "$b$ has exactly $n$ predecessors" is decided by $D(\mathcal B)'$, and the element with exactly $n$ predecessors is found by search. So the isomorphism is computable in $(D(\mathcal B) \oplus D(\mathcal C))'$.
:::

Here the information needed to match an element, the number of its predecessors, is not finite information decidable from the diagram: it is a $\Delta^0_2$ property. In the copy of :ref{#prop-two-copies-omega}, this information codes $\emptyset'$, and the jump is necessary. This contrast between $\omega$ and $\mathbb Q$ is the starting point of the general theory: a structure is relatively computably categorical exactly when the orbits of its tuples are described by existential formulas, uniformly enough (the theorem of Goncharov, Ash, Knight, Manasse, Slaman and Chisholm, in the course on computable categoricity). For $\mathbb Q$, the orbit of a tuple is given by its order type, a quantifier-free formula; for $\omega$, by the number of predecessors of each element, which no existential formula can express.

::::exercise{#ex-random-graph difficulty=1 objective="Run the effective back-and-forth argument on the random graph."}
Show that any two copies $\mathcal B$ and $\mathcal C$ of the random graph are isomorphic by an isomorphism computable in $D(\mathcal B) \oplus D(\mathcal C)$.

:::solution
Build finite partial isomorphisms $p_s$ as in :ref{#thm-effective-cantor}. To go forth with a new vertex $b$, let $U$ be the set of vertices of the domain of $p_s$ adjacent to $b$, and $V$ the others. By the extension property of $\mathcal C$, there are infinitely many vertices adjacent to every vertex of $p_s(U)$ and to none of $p_s(V)$: applying the property again with the vertices already found added to the second set gives a new one each time. So one of them, $c$, lies outside the range of $p_s$. Such a $c$ is found by a search using $D(\mathcal C)$, which decides adjacency, and $p_s \cup \{ (b, c) \}$ preserves adjacency and equality. Going back is symmetric. The union is an isomorphism computable in $D(\mathcal B) \oplus D(\mathcal C)$.
:::
::::

## Notes and references

The back-and-forth argument is Cantor's (1895) for the rationals; its effective content was noticed early, and computable categoricity (called autostability in the Russian literature) was introduced by Mal'cev in the 1960s. The examples are standard (Ash–Knight, Chapter 12, Sections 12.1 and 12.3; Montalbán, *Within the Arithmetic*, Sections III.3 and VIII.1). That an infinite-dimensional $\mathbb Q$-vector space is not computably categorical, and that a linear order is relatively computably categorical if and only if it has finitely many adjacencies, are proved in the course on computable categoricity, which also states the theorem of Dzgoev, Goncharov and Remmel for plain categoricity.

- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 12.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Chapters III and VIII.
- E. B. Fokina, V. Harizanov and A. Melnikov, *Computable model theory*, in *Turing's Legacy*, Lecture Notes in Logic 42, Cambridge University Press, 2014, 124–194.

:::::exercises
::::exercise{#ex-integers-delta2 difficulty=2 objective="Show that the order of the integers is Δ⁰₂-categorical but not computably categorical."}
Let $\zeta = (\mathbb Z; \leq)$. Show that any two copies of $\zeta$ are isomorphic by an isomorphism computable in the jump of the join of their diagrams, and that $\zeta$ has two computable copies that are not computably isomorphic.

:::solution
Fix an element $b_0$ of $\mathcal B$ and an element $c_0$ of $\mathcal C$, as parameters. The isomorphisms of $\zeta$ are the translations, and there is a unique isomorphism sending $b_0$ to $c_0$; it sends the element of $\mathcal B$ with exactly $n$ elements between it and $b_0$, above $b_0$, to the element of $\mathcal C$ in the same position relative to $c_0$, and similarly below. "Exactly $n$ elements between" is decided by the jump, as in :ref{#prop-omega-delta2}.

For the second part, modify the copy of :ref{#prop-two-copies-omega}. Fix a computable copy of $\zeta$ on the even numbers, and let $e_k$ be its element representing the integer $k$. Let $k_0, k_1, \ldots$ be a computable injective enumeration of $\emptyset'$, and insert the odd number $2s + 1$ between $e_{k_s}$ and $e_{k_s + 1}$, ordering two odd numbers as their $k$'s. Each interval receives at most one new element, so the result is still a copy of $\zeta$, and it is computable. In it, $e_{k+1}$ is the successor of $e_k$ if and only if $k \notin \emptyset'$. In the standard copy the successor function is computable, and a computable isomorphism would make the successor function of the other copy computable.
:::
::::

::::exercise{#ex-atomless-ba difficulty=2 objective="Adapt the back-and-forth argument to Boolean algebras, where partial isomorphisms are between finite subalgebras."}
Show that the countable atomless Boolean algebra is relatively computably categorical. (Work with isomorphisms between finite subalgebras: a finite subalgebra is determined by its atoms, and an isomorphism by a bijection between the atoms.)

:::solution
Let $\mathcal B$ and $\mathcal C$ be copies, and keep at each step an isomorphism $p$ between finite subalgebras $B_0 \subseteq \mathcal B$ and $C_0 \subseteq \mathcal C$, given by a bijection between their atoms. Going forth with a new element $b$, the subalgebra generated by $B_0$ and $b$ has as atoms the non-zero elements among $a \wedge b$ and $a \wedge \neg b$, for the atoms $a$ of $B_0$. For each atom $a$ of $B_0$ split by $b$ (both parts non-zero), the atom $p(a)$ of $C_0$ is non-zero, and since $\mathcal C$ is atomless, there is $d \leq p(a)$ with $d \neq 0$ and $d \neq p(a)$; search for one, using $D(\mathcal C)$ to compute the operations. Map $a \wedge b$ to $d$ and $a \wedge \neg b$ to $p(a) \wedge \neg d$; if $a \wedge b = 0$ or $a \wedge \neg b = 0$, map the atom $a$ to $p(a)$ unchanged. This defines an isomorphism of the generated subalgebras, extending $p$, and $b$ is in its domain. Going back is symmetric. The union is an isomorphism computable in $D(\mathcal B) \oplus D(\mathcal C)$, since every step is a terminating search and the atoms of finite subalgebras are computed from the operations.
:::
::::
:::::
