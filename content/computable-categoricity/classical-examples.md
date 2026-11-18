---
title: Linear orders, vector spaces, Boolean algebras
summary: A computable linear order is relatively computably categorical if and only if it has finitely many adjacent pairs; an infinite-dimensional computable vector space is not computably categorical; a Boolean algebra with finitely many atoms is relatively computably categorical, and one with infinitely many is not; the known characterizations of computable categoricity in classical classes, and the Π¹₁-completeness of the general notion.
duration: 40
prerequisites: [relative-categoricity, intrinsic-definability/intrinsic-vs-relative]
---

The theorem of the previous lesson reduces relative computable categoricity to a question of definability: are the orbits of tuples described by existential formulas over finitely many parameters? For classical structures, this question has a concrete answer, given by a single invariant of the structure: the number of adjacent pairs of a linear order, the dimension of a vector space, the number of atoms of a Boolean algebra. In each case, a finite invariant allows the parameters to name everything that is not homogeneous, and an infinite one leaves an existential formula unable to tell an element from a less special one. The proofs of the negative direction share one technique: move the witnesses of an existential formula by an embedding that preserves the quantifier-free facts but destroys the property.

## Linear orders

Two elements $a < b$ of a linear order are **adjacent** if no element lies strictly between them. Adjacency is not preserved by embeddings: an element may be inserted between $a$ and $b$ in a larger order. This is why it escapes existential formulas.

:::lemma{#lem-finite-adjacencies}
Let $\mathcal L$ be a linear order with finitely many adjacent pairs, and let $P$ be the finite set of elements belonging to an adjacent pair, together with the least and the greatest elements of $\mathcal L$, if they exist. Then every non-empty interval of $\mathcal L$ between two consecutive elements of $P$, below the least element of $P$ or above the greatest, is a dense order without endpoints.
:::

:::proof{of=lem-finite-adjacencies}
Let $I$ be such an interval, non-empty; it contains no element of $P$. It is dense: if $x < y$ in $I$ were adjacent, $x$ would belong to $P$. It has no least element: if $c$ were least in $I$, then either $I$ is an initial segment of $\mathcal L$ and $c$ is the least element of $\mathcal L$, or $I$ lies just above some $u \in P$, and then $u$ and $c$ are adjacent, since an element between them would belong to $I$ and lie below $c$; in both cases $c \in P$, a contradiction. Symmetrically, $I$ has no greatest element.
:::

:::figure[A linear order with finitely many adjacencies, as in :ref{#lem-finite-adjacencies}. The set $P$ consists of the two adjacent pairs $p_0, p_1$ and $p_2, p_3$, and of the greatest element $p_4$; the remaining intervals are dense without endpoints. The order type is $\eta + 2 + \eta + 2 + \eta + 1$.]
<svg class="fig" viewBox="0 0 680 170" width="680" role="img" aria-label="A linear order drawn on a line. Five marked elements p0 to p4 belong to the finite set P: p0 and p1 are adjacent, and so are p2 and p3; p4 is the greatest element. To the left of p0, between p1 and p2, and between p3 and p4 lie intervals drawn as shaded bands, each a dense order without endpoints"><rect x="40" y="71" width="130" height="18" rx="9" class="soft-fill"/><line x1="46" y1="80" x2="164" y2="80" class="muted-stroke" stroke-width="1.2" stroke-dasharray="2 3"/><text x="105.0" y="114" text-anchor="middle" class="math">η</text><rect x="270" y="71" width="110" height="18" rx="9" class="soft-fill"/><line x1="276" y1="80" x2="374" y2="80" class="muted-stroke" stroke-width="1.2" stroke-dasharray="2 3"/><text x="325.0" y="114" text-anchor="middle" class="math">η</text><rect x="480" y="71" width="120" height="18" rx="9" class="soft-fill"/><line x1="486" y1="80" x2="594" y2="80" class="muted-stroke" stroke-width="1.2" stroke-dasharray="2 3"/><text x="540.0" y="114" text-anchor="middle" class="math">η</text><path d="M200,68 Q220.0,46 240,68" fill="none" class="accent-stroke" stroke-width="1.6"/><path d="M410,68 Q430.0,46 450,68" fill="none" class="accent-stroke" stroke-width="1.6"/><circle cx="200" cy="80" r="6" class="head-cell"/><text x="200" y="110" text-anchor="middle" class="math">p₀</text><circle cx="240" cy="80" r="6" class="head-cell"/><text x="240" y="110" text-anchor="middle" class="math">p₁</text><circle cx="410" cy="80" r="6" class="head-cell"/><text x="410" y="110" text-anchor="middle" class="math">p₂</text><circle cx="450" cy="80" r="6" class="head-cell"/><text x="450" y="110" text-anchor="middle" class="math">p₃</text><circle cx="630" cy="80" r="6" class="head-cell"/><text x="630" y="110" text-anchor="middle" class="math">p₄</text><text x="8" y="160" class="label">shaded: dense intervals without endpoints</text><text x="672" y="160" text-anchor="end" class="label">arcs: the adjacent pairs</text></svg>
:::

:::theorem[Dzgoev, Goncharov; Remmel]{#thm-lo-rcc}
A computable linear order is relatively computably categorical if and only if it has finitely many adjacent pairs.
:::

**Intuition.** With finitely many adjacencies, the order is a finite sum of points and copies of $\mathbb Q$, by :ref{#lem-finite-adjacencies}; naming the points, the orbit of a tuple is given by its order type, as in $\mathbb Q$. With infinitely many adjacencies, some adjacent pair lies in an infinite interval determined by the parameters; any existential formula true of the pair has finitely many witnesses, and spreading these witnesses apart inside the interval keeps the formula true while separating the pair.

:::proof{of=thm-lo-rcc}
Let $\mathcal L$ be a computable linear order.

*Finitely many adjacencies.* Let $\bar p$ list the set $P$ of :ref{#lem-finite-adjacencies}. For a tuple $\bar a$, let $\varphi_{\bar a}(\bar p, \bar x)$ be the quantifier-free formula giving the order type of $\bar p \bar a$: the order between any two entries. Let $\bar a$ and $\bar b$ satisfy the same $\varphi_{\bar a}$. Then, in each interval $I$ of :ref{#lem-finite-adjacencies}, the entries of $\bar a$ and of $\bar b$ that lie in $I$ are in the same number and the same order. Since $I$ is a dense order without endpoints, the order-preserving map between them extends to an automorphism of $I$, by the back-and-forth argument of :ref{#thm-effective-cantor} started from this finite map. These automorphisms, together with the identity on $P$, form an automorphism of $\mathcal L$ fixing $\bar p$ and mapping $\bar a$ to $\bar b$. The formulas $\varphi_{\bar a}$ form a computable Scott family of quantifier-free formulas over $\bar p$, and $\mathcal L$ is relatively computably categorical by :ref{#thm-rcc-scott}.

*Infinitely many adjacencies.* By :ref{#thm-rcc-scott}, it suffices to show that $\mathcal L$ has no existential Scott family over any tuple $\bar p$. The entries of $\bar p$ cut $\mathcal L$ into finitely many intervals. An adjacent pair disjoint from $\bar p$ lies in one of them, since no entry of $\bar p$ lies between its elements; at most $2|\bar p|$ adjacent pairs meet $\bar p$. So some interval $I$ contains infinitely many adjacent pairs, and $I$ is infinite. Let $a < b$ be an adjacent pair in $I$, and suppose that an existential formula $\exists \bar y\, \psi(\bar p, x_1, x_2, \bar y)$, with $\psi$ quantifier-free, holds of $(a, b)$ with witnesses $\bar m$. List the elements of $I$ among $a$, $b$ and the entries of $\bar m$ as $f_1 < \cdots < f_N$; since $a$ and $b$ are adjacent, they are consecutive: $a = f_r$ and $b = f_{r+1}$. As $I$ is infinite, it contains elements $w_1 < \cdots < w_{N+1}$. Let $h$ map $f_i$ to $w_i$ for $i \leq r$ and to $w_{i+1}$ for $i > r$, and fix the entries of $\bar p$ and of $\bar m$ outside $I$. Since $I$ is an interval of $\bar p$, this finite map preserves the order in both directions, hence every quantifier-free formula, and $\psi(\bar p, w_r, w_{r+2}, h(\bar m))$ holds. So the pair $(w_r, w_{r+2})$ satisfies the existential formula, but it is not adjacent, since $w_{r+1}$ lies between: it is not automorphic to $(a, b)$, as automorphisms preserve adjacency. Hence the formula satisfied by $(a, b)$ in a Scott family over $\bar p$ would define more than the orbit of $(a, b)$, which is impossible.
:::

:::quiz[relative categoricity of linear orders]
In the case of infinitely many adjacencies, why is the adjacent pair chosen in an interval of $\bar p$ that contains infinitely many adjacent pairs, rather than in any interval?

- [x] Such an interval is infinite, so it has room for the $N + 1$ elements $w_i$, one more than the elements of the configuration in it.
- [ ] Because adjacent pairs in a finite interval are automorphic to non-adjacent ones.

  Automorphisms preserve adjacency in every interval; the problem with a finite interval is that the witnesses cannot be spread apart inside it.
- [ ] Because the formula must have infinitely many witnesses.

  An existential formula has finitely many witnesses; what is needed is an infinite interval to move them in.

---

Where does the proof use that the formula is existential?

- [x] Existential formulas are preserved by the embedding $h$, which maps witnesses to witnesses; a universal formula, such as "nothing lies between $x_1$ and $x_2$", is not preserved by maps that insert elements.
- [ ] To bound the number of parameters.

  The parameters $\bar p$ are fixed in advance; the form of the formula concerns its quantifiers.
- [ ] To show that $I$ is infinite.

  That comes from the infinitely many adjacent pairs.
:::

The theorem is due, for plain computable categoricity, to Dzgoev and Goncharov (1980) and, independently, Remmel (1981): a computable linear order with infinitely many adjacent pairs has a computable copy with no computable isomorphism to it. That proof is a finite injury construction of the copy, guessing adjacencies from the c.e. complement of the adjacency relation, and is not given here (Ash–Knight, Theorem 12.11). For linear orders, as for all the classes listed at the end of this lesson, plain and relative computable categoricity coincide.

## Vector spaces

A finite-dimensional $\mathbb Q$-vector space is relatively computably categorical, with a basis as parameters (:ref{#ex-computably-categorical}). In infinite dimension, the span of a vector is the obstruction: it is computable in a well-chosen copy and not in others.

:::proposition{#prop-vector-not-cc}
A computable $\mathbb Q$-vector space of infinite dimension is not computably categorical.
:::

:::proof{of=prop-vector-not-cc}
Let $\mathcal V_0$ be the standard presentation of the space $\mathbb Q^{(\omega)}$ of finitely supported sequences of rationals, in which a vector is given by its finite list of coordinates. In $\mathcal V_0$, the set $\mathbb Q u$ of multiples of any vector $u$ is computable, by comparing coordinates. Every computable $\mathbb Q$-vector space of countably infinite dimension is a copy of $\mathcal V_0$.

Suppose that $\mathcal V_0$ is computably categorical. Fix $v \neq 0$. By :ref{#ex-multiples-vector}, the relation $\mathbb Q v$ is not intrinsically computable: there is a computable copy $(\mathcal W, R)$ of $(\mathcal V_0, \mathbb Q v)$ with $R$ not computable. If $g : (\mathcal V_0, \mathbb Q v) \to (\mathcal W, R)$ is an isomorphism, then $R = g(\mathbb Q v) = \mathbb Q w$ with $w = g(v)$. By assumption, there is a computable isomorphism $f : \mathcal V_0 \to \mathcal W$. Let $u = f^{-1}(w)$. Then $f(\mathbb Q u) = \mathbb Q w = R$, since $f$ is linear. So $x \in R$ if and only if $f^{-1}(x) \in \mathbb Q u$, which is computable, as $f^{-1}$ is computed from $f$ by search. This contradicts the choice of $\mathcal W$.
:::

The proof is an instance of a general remark: if $\mathcal A$ is computably categorical and $R$ is a relation definable with parameters, computable in $\mathcal A$, then $R$ is computable in every computable copy, provided the parameters are moved with the isomorphism. The relation $\mathbb Q v$ is not invariant, but its images under isomorphisms are the relations $\mathbb Q w$, all of which can be transported by a computable isomorphism. Algebraically closed fields behave in the same way: those of infinite transcendence degree are not computably categorical (Ershov 1977), and their intrinsically computable unary relations are the finite and cofinite ones (Ash–Knight, Section 11.3.2).

## Boolean algebras

In a Boolean algebra, an **atom** is a minimal non-zero element. Atoms play the role of adjacencies: "$x$ is an atom" is a universal property, and an embedding may map an atom to an element that splits.

:::proposition{#prop-ba-finitely-many-atoms}
A computable Boolean algebra with finitely many atoms is relatively computably categorical.
:::

:::proof{of=prop-ba-finitely-many-atoms}
Let $\mathcal B$ have atoms $a_1, \ldots, a_n$, and let $c$ be the complement of $a_1 \vee \cdots \vee a_n$. The elements below $c$ form a Boolean algebra $\mathcal C$, with $c$ as top, and $\mathcal C$ has no atom, since an atom of $\mathcal C$ would be an atom of $\mathcal B$ distinct from the $a_i$. Every element $x$ of $\mathcal B$ is the join of $x \wedge c$ and of the atoms below $x$, so $\mathcal B$ is the product of the finite algebra generated by the atoms and of $\mathcal C$.

For a tuple $\bar b$, let $\varphi_{\bar b}(\bar a, \bar x)$ be the quantifier-free formula recording, for every Boolean term $t(\bar a, \bar x)$ built from the parameters $\bar a$ and the variables $\bar x$, whether $t = 0$; finitely many terms suffice, those that are meets of the $a_i$, the $x_j$ and their complements, since every term is a join of such meets. If $\bar b$ and $\bar b'$ satisfy $\varphi_{\bar b}$, the finite subalgebras generated by $\bar a \bar b$ and by $\bar a \bar b'$ are isomorphic by a map fixing $\bar a$ and sending $\bar b$ to $\bar b'$, since a finite Boolean algebra is determined by which meets of generators are zero. Its restriction to the elements below $c$ is an isomorphism between finite subalgebras of the atomless algebra $\mathcal C$, which extends to an automorphism of $\mathcal C$ by the back-and-forth argument of :ref{#ex-atomless-ba}. Together with the identity on the finite part, it gives an automorphism of $\mathcal B$ fixing $\bar a$ and mapping $\bar b$ to $\bar b'$. So the formulas $\varphi_{\bar b}$ form a computable Scott family of quantifier-free formulas over $\bar a$.
:::

::::exercise{#ex-ba-infinitely-many-atoms difficulty=2 objective="Move the witnesses of an existential formula by an embedding of finite Boolean algebras to show that infinitely many atoms prevent relative categoricity."}
Let $\mathcal B$ be a computable Boolean algebra with infinitely many atoms. Show that $\mathcal B$ is not relatively computably categorical. *Hint:* given a tuple $\bar p$, choose an atom of the subalgebra generated by $\bar p$ that bounds infinitely many atoms of $\mathcal B$, and an atom $a$ of $\mathcal B$ below it; then replace $a$ by an element that is not an atom without changing the quantifier-free type of a finite configuration.

:::solution
By :ref{#thm-rcc-scott}, we show that there is no existential Scott family over a tuple $\bar p$. The subalgebra $\langle \bar p \rangle$ generated by $\bar p$ is finite, and its atoms partition $1$; since $\mathcal B$ has infinitely many atoms, some atom $t$ of $\langle \bar p \rangle$ bounds infinitely many atoms of $\mathcal B$. Let $a \leq t$ be an atom of $\mathcal B$. Suppose an existential formula $\exists \bar y\, \psi(\bar p, x, \bar y)$, with $\psi$ quantifier-free, holds of $a$ with witnesses $\bar m$, and let $F = \langle \bar p, a, \bar m \rangle$, a finite subalgebra. Since $a$ is an atom of $\mathcal B$ belonging to $F$, it is an atom of $F$, and the atoms of $F$ below $t$ are $s_1 = a, s_2, \ldots, s_r$, which partition $t$. Choose distinct atoms $e_2, \ldots, e_r$ of $\mathcal B$ below $t$, and let $s'_1 = t \wedge \neg(e_2 \vee \cdots \vee e_r)$, which bounds infinitely many atoms, so it is not zero and not an atom; let $s'_i = e_i$ for $i \geq 2$. The map sending each $s_i$ to $s'_i$ and fixing the other atoms of $F$ extends to an embedding $h$ of $F$ into $\mathcal B$: a map from the atoms of a finite Boolean algebra to pairwise disjoint non-zero elements with the same joins over each atom of $\langle \bar p \rangle$ extends to an embedding, and $h$ fixes $\langle \bar p \rangle$, since $s'_1 \vee \cdots \vee s'_r = t$. An embedding preserves quantifier-free formulas, so $\psi(\bar p, h(a), h(\bar m))$ holds and $s'_1 = h(a)$ satisfies the existential formula. But $s'_1$ is not an atom, so it is not automorphic to $a$.
:::
::::

The converse of :ref{#prop-ba-finitely-many-atoms} for plain categoricity is due to Goncharov (1975) and La Roche (1978): a computable Boolean algebra with infinitely many atoms is not computably categorical (Ash–Knight, Theorem 12.13).

## The classical classes

For many classes of algebraic structures, computable categoricity has been characterized by a structural invariant, and in each case plain and relative categoricity agree. The following table collects the main results, as listed by Montalbán (Table 1 of Chapter VIII).

| Class | Computably categorical if and only if | Reference |
| --- | --- | --- |
| Linear orders | finitely many adjacent pairs | Dzgoev, Goncharov 1980; Remmel 1981 |
| Boolean algebras | finitely many atoms | Goncharov 1975; La Roche 1978 |
| $\mathbb Q$-vector spaces | finite dimension | — |
| Algebraically closed fields | finite transcendence degree | Ershov 1977 |
| Torsion-free abelian groups | finite rank | Nurtazin 1974 |
| Ordered abelian groups | finite rank | Goncharov, Lempp, Solomon 2003 |
| Trees of finite height | finite type | Lempp, McCoy, Miller, Solomon 2005 |

Each characterization requires its own priority construction for the negative direction. No such characterization exists in general: Downey, Kach, Lempp, Lewis-Pye, Montalbán and Turetsky (2015) showed that the set of indices of computable structures that are computably categorical is $\Pi^1_1$-complete, so computable categoricity is as complicated as a property of computable structures can be, and no arithmetic or hyperarithmetic description of it is possible. Relative computable categoricity, by contrast, is a $\Sigma^0_3$ property: by :ref{#thm-rcc-scott}, it amounts to the existence of parameters and of a c.e. existential Scott family, and Downey, Kach, Lempp and Turetsky (2013, Theorem 1.6) showed that the index set of the computable structures with such a family is $\Sigma^0_3$-complete (Montalbán, Exercise III.23). The next lesson compares the two notions.

## Notes and references

:ref{#thm-lo-rcc} for plain categoricity is due to Dzgoev and Goncharov (1980) and to Remmel (1981); the proof of the relative version through :ref{#thm-rcc-scott} is standard (Montalbán, Chapter VIII). The decomposition of :ref{#lem-finite-adjacencies} is Ash–Knight, proof of Theorem 12.11. :ref{#prop-vector-not-cc} is folklore; the argument through the Ash–Nerode theorem follows Ash–Knight, Section 12.1, where the same reasoning shows that $\omega$ is not computably categorical. :ref{#prop-ba-finitely-many-atoms} and its converse are due to Goncharov (1975) and La Roche (1978); Ash–Knight, Theorem 12.13.

- V. D. Dzgoev and S. S. Goncharov, *Autostable models*, Algebra and Logic 19 (1980), 28–37.
- J. B. Remmel, *Recursively categorical linear orderings*, Proceedings of the American Mathematical Society 83 (1981), 387–391.
- R. Downey, A. Kach, S. Lempp, A. Lewis-Pye, A. Montalbán and D. Turetsky, *The complexity of computable categoricity*, Advances in Mathematics 268 (2015), 423–466.
- R. Downey, A. Kach, S. Lempp and D. Turetsky, *Computable categoricity versus relative computable categoricity*, Fundamenta Mathematicae 221 (2013), 129–159.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 12.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Chapter VIII.

:::::exercises
::::exercise{#ex-lo-examples difficulty=1 objective="Apply the characterization of relatively categorical linear orders to standard order types."}
Which of the following orders are relatively computably categorical: $1 + \eta$, $\eta + 2 + \eta$, $\omega + \omega^*$, $\zeta \cdot \eta$ (a copy of the integers for each rational), $\eta \cdot 2$, and $2 \cdot \eta$ (a pair of adjacent elements for each rational)?

:::solution
By :ref{#thm-lo-rcc}, count the adjacent pairs. $1 + \eta$: the least element has no successor, since $\eta$ has no least element, and $\eta$ is dense; no adjacent pair, relatively categorical. $\eta + 2 + \eta$: one adjacent pair, relatively categorical. $\omega + \omega^*$: infinitely many (every element of $\omega$ and its successor), not. $\zeta \cdot \eta$: infinitely many, not. $\eta \cdot 2 = \eta + \eta$: dense without endpoints, isomorphic to $\eta$, no adjacent pair, relatively categorical. $2 \cdot \eta$: one adjacent pair for each rational, infinitely many, not.
:::
::::

::::exercise{#ex-lo-parameters-needed difficulty=1 objective="See that parameters cannot be avoided in the characterization, by an order whose adjacent pair must be named."}
Show that $\eta + 2 + \eta$ has no Scott family of existential formulas without parameters, and give one with parameters.

:::solution
Let $a < b$ be the adjacent pair. Without parameters, an existential formula $\exists \bar y\, \psi(x_1, x_2, \bar y)$ true of $(a, b)$ with witnesses $\bar m$ remains true when the finite configuration $a, b, \bar m$ is moved by an order-preserving injection into $\eta + 2 + \eta$ that sends $a$ and $b$ into the second copy of $\eta$: such an injection exists, since every finite linear order embeds into $\eta$, and any finite part of $\eta + 2 + \eta$ embeds into $\eta$ preserving the order. The images of $a$ and $b$ are not adjacent, so the formula does not define the orbit of $(a, b)$. With the parameters $a, b$, the order types over $(a, b)$ form a Scott family, by the proof of :ref{#thm-lo-rcc}.
:::
::::

::::exercise{#ex-ba-examples difficulty=1 objective="Apply the results on Boolean algebras to the interval algebras of standard orders."}
The interval algebra of a linear order $\mathcal L$ with a least element is the Boolean algebra of finite unions of half-open intervals $[a, b)$ of $\mathcal L$, with $b$ possibly $+\infty$. Show that the interval algebra of $\eta$ with a least element added, $1 + \eta$, is atomless, and that the interval algebra of $\omega$ has infinitely many atoms. Which of the two is relatively computably categorical?

:::solution
In the interval algebra of $1 + \eta$, every non-zero element contains an interval $[a, b)$ with $a < b$, and density gives $c$ with $a < c < b$, so $[a, c)$ is a non-zero element strictly below it: there are no atoms. The algebra is relatively computably categorical by :ref{#prop-ba-finitely-many-atoms}, with no atoms to name. In the interval algebra of $\omega$, each $[n, n + 1) = \{n\}$ is an atom, so there are infinitely many atoms, and the algebra is not relatively computably categorical, by :ref{#ex-ba-infinitely-many-atoms}.
:::
::::

::::exercise{#ex-vector-not-rcc difficulty=2 objective="Prove the relative version for vector spaces from the characterization, by a linear map that is not injective but keeps finitely many vectors non-zero."}
Let $\mathcal V$ be a computable $\mathbb Q$-vector space of infinite dimension, in the vocabulary of addition, the constant $0$ and the scalar multiplications as unary functions. Show directly that $\mathcal V$ has no existential Scott family over any tuple $\bar p$, and deduce again that it is not relatively computably categorical. *Hint:* consider a pair $(v_1, v_2)$ linearly independent over the span of $\bar p$, and send $v_2$ to a multiple of $v_1$.

:::solution
Let $S$ be the span of $\bar p$, $v_1 \notin S$ and $v_2 \notin S + \mathbb Q v_1$. An automorphism fixing $\bar p$ is linear and fixes $S$, so it maps $(v_1, v_2)$ to a pair that is linearly independent over $S$. Suppose an existential formula $\exists \bar y\, \psi(\bar p, x_1, x_2, \bar y)$, with $\psi$ quantifier-free, holds of $(v_1, v_2)$ with witnesses $\bar m$. Atomic formulas are equalities between terms, and terms denote rational linear combinations; so $\psi$ is a Boolean combination of statements $w = 0$, where $w$ ranges over finitely many linear combinations of $\bar p$, $v_1$, $v_2$, $\bar m$. Let $w_1, \ldots, w_r$ be those that are non-zero.

Let $U$ be the span of $\bar p$, $v_1$, $v_2$ and $\bar m$, with a basis consisting of a basis $\bar s$ of $S$, then $v_1$, $v_2$, and vectors $\bar u$. Choose vectors $\bar u'$ of $\mathcal V$ linearly independent over $S + \mathbb Q v_1$, which is possible in infinite dimension, and a rational $q$, and let $h$ be the linear map on $U$ fixing $\bar s$ and $v_1$, sending $v_2$ to $q v_1$ and $\bar u$ to $\bar u'$. A linear map preserves the true equations $w = 0$. Write $w_k = \sigma_k + \alpha_k v_1 + \beta_k v_2 + \sum_l \gamma_{kl} u_l$ with $\sigma_k \in S$; then $h(w_k) = \sigma_k + (\alpha_k + \beta_k q) v_1 + \sum_l \gamma_{kl} u'_l$. If some $\gamma_{kl} \neq 0$, this is non-zero by the independence of $\bar u'$. Otherwise it is zero only if $\sigma_k = 0$ and $\alpha_k + \beta_k q = 0$; if $\beta_k = 0$, this would make $w_k = \alpha_k v_1 = 0$, which is not the case; if $\beta_k \neq 0$, it happens for the single value $q = -\alpha_k / \beta_k$. Choosing $q$ outside these finitely many values, $h$ keeps every $w_k$ non-zero, so $\psi(\bar p, v_1, q v_1, h(\bar m))$ holds, and the dependent pair $(v_1, q v_1)$ satisfies the existential formula. It is not in the orbit of $(v_1, v_2)$. So no existential Scott family over $\bar p$ exists, and by :ref{#thm-rcc-scott} the space is not relatively computably categorical, in accordance with :ref{#prop-vector-not-cc}.
:::
::::
:::::
