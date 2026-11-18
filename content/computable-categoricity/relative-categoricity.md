---
title: Relative computable categoricity
summary: A computable structure is relatively computably categorical if and only if it has a c.e. Scott family of existential formulas over finitely many parameters (Ash, Knight, Manasse, Slaman; Chisholm), proved by a failed diagonalization against all Turing functionals; naming constants preserves relative categoricity, and invariant computable relations are relatively intrinsically computable.
duration: 35
prerequisites: [scott-families]
---

The previous lesson showed that a c.e. existential Scott family makes a structure relatively computably categorical. This lesson proves the converse, completing the characterization. The proof follows the pattern of the characterization of r.i.c.e. relations: try to build a copy that no computable procedure can match with the structure; the failure of the attempt produces the Scott family. The characterization then turns questions about all copies into questions about definability in one structure, which the next lesson applies to classical examples.

As before, $\mathcal A$ is a computable structure in a computable relational vocabulary, with domain $\nat$, and tuples consist of distinct elements.

## The theorem


:::theorem[Ash, Knight, Manasse, Slaman; Chisholm]{#thm-rcc-scott}
A computable structure $\mathcal A$ is relatively computably categorical if and only if it has a c.e. existential Scott family over some tuple.
:::

**Intuition.** Assume that every copy computes an isomorphism with $\mathcal A$, and build a copy by an enumeration of $\mathcal A$ that tries to defeat every Turing functional: at its turn, a functional $\Phi_e$ is defeated if a finite part of the enumeration makes $\Phi_e$ compute a partial map that no automorphism extends. Some functional computes an isomorphism, so the attempt fails for it, past some finite part $\bar p$ of the enumeration. What the functional computes from a finite part of the diagram then depends only on this finite diagram, and it identifies orbits; the finite diagram is described by an existential formula. The construction is that of :ref{#thm-akms-chisholm-1}, with functionals in place of c.e. operators.

:::proof{of=thm-rcc-scott}
One direction is :ref{#prop-scott-rcc}. Conversely, let $\mathcal A$ be relatively computably categorical. As in the proof of :ref{#thm-akms-chisholm-1}, for a tuple $\bar q$ of $\mathcal A$, $D_{\mathcal A}(\bar q)$ is the finite atomic diagram of $\bar q$: the string of length $|\bar q|$ recording the truth of the first $|\bar q|$ atomic formulas, in a fixed listing of the atomic formulas in which the $i$-th one mentions only variables $x_j$ with $j < i$, the variable $x_j$ naming $q_j$; if $g$ is an injective enumeration of $\mathcal A$ extending $\bar q$, then $D_{\mathcal A}(\bar q)$ is an initial segment of $D(g^{-1}(\mathcal A))$. For a string $\sigma$, $\Phi_e^\sigma(j)$ is the output, if any, of the $e$-th Turing functional on input $j$ with oracle $\sigma$ in at most $|\sigma|$ steps; its value is read as an element of $\mathcal A$. For a tuple $\bar q$, let $\pi^e_{\bar q}$ be the finite map
$$
\pi^e_{\bar q} : q_j \mapsto \Phi_e^{D_{\mathcal A}(\bar q)}(j), \qquad j < |\bar q| \text{ such that } \Phi_e^{D_{\mathcal A}(\bar q)}(j) \text{ is defined},
$$
and let $Q_e$ be the set of tuples $\bar q$ such that $\pi^e_{\bar q}$ is not the restriction of an automorphism of $\mathcal A$.

*Construction.* Let $\bar p_0$ be empty. At stage $s + 1 = 2e + 1$, append to $\bar p_s$ the $e$-th element of $\mathcal A$ if it is not already there. At stage $s + 1 = 2e$, if some tuple $\bar q \supseteq \bar p_s$ belongs to $Q_e$, let $\bar p_{s+1}$ be such a $\bar q$; otherwise $\bar p_{s+1} = \bar p_s$. Let $g = \bigcup_s \bar p_s$, a bijection from $\nat$ onto $A$, and $\mathcal B = g^{-1}(\mathcal A)$, an ω-presentation; $g$ is an isomorphism from $\mathcal B$ onto $\mathcal A$. The construction is not effective, since $Q_e$ need not be decidable; this is why the hypothesis must apply to all copies.

*Some stage fails.* By :ref{#lem-rcc-formulations}, some isomorphism from $\mathcal B$ onto $\mathcal A$ is computable in $D(\mathcal B)$: there is $e$ such that $\Phi_e^{D(\mathcal B)}$ is such an isomorphism. Then $\alpha = \Phi_e^{D(\mathcal B)} \circ g^{-1}$ is an automorphism of $\mathcal A$. If a tuple $\bar q \in Q_e$ had been chosen at stage $2e$, then $\bar q \subseteq g$, $D_{\mathcal A}(\bar q)$ is an initial segment of $D(\mathcal B)$, and for each $j$ in the domain of $\pi^e_{\bar q}$, $\alpha(q_j) = \Phi_e^{D(\mathcal B)}(j) = \pi^e_{\bar q}(q_j)$: the automorphism $\alpha$ extends $\pi^e_{\bar q}$, contradicting $\bar q \in Q_e$. So no extension of $\bar p = \bar p_{2e-1}$ belongs to $Q_e$. Let $k = |\bar p|$.

*The key claim.* Let $\bar q, \bar q' \supseteq \bar p$ with $D_{\mathcal A}(\bar q) = D_{\mathcal A}(\bar q') = \sigma$, and let $\bar j$ be a tuple of numbers below $|\bar q|$ such that $\Phi_e^\sigma$ is defined at $0, \ldots, k - 1$ and at the entries of $\bar j$. Then some automorphism of $\mathcal A$ fixing $\bar p$ maps $\bar q_{\bar j}$ to $\bar q'_{\bar j}$, where $\bar q_{\bar j} = (q_{j_1}, \ldots, q_{j_\ell})$. Indeed, the values $v_j = \Phi_e^\sigma(j)$ depend only on $\sigma$, so $\pi^e_{\bar q}(q_j) = v_j = \pi^e_{\bar q'}(q'_j)$ for each such $j$. Since $\bar q, \bar q' \notin Q_e$, there are automorphisms $\beta \supseteq \pi^e_{\bar q}$ and $\beta' \supseteq \pi^e_{\bar q'}$. Then $\beta'^{-1} \circ \beta$ maps $q_j$ to $v_j$ and then to $q'_j$; for $j < k$, $q_j = p_j = q'_j$, so it fixes $\bar p$.

*The Scott family.* For a string $\sigma$ of length $n \geq k$ and a tuple $\bar j$ of numbers below $n$ such that $\Phi_e^\sigma$ is defined at $0, \ldots, k - 1$ and at the entries of $\bar j$, let
$$
\theta_{\sigma, \bar j}(\bar p, \bar x) \equiv \exists z_k \ldots \exists z_{n-1}\, \big( \delta_\sigma(\bar p, z_k, \ldots, z_{n-1}) \wedge \bar x = (\bar p z_k \ldots z_{n-1})_{\bar j} \big),
$$
where $\delta_\sigma(y_0, \ldots, y_{n-1})$ is the conjunction of the first $n$ atomic formulas or their negations, as recorded by $\sigma$, together with $y_i \neq y_j$ for $i \neq j$. The set $\Phi$ of these formulas is computable, and they are existential. Every tuple $\bar a$ satisfies one: write $\bar a = g_{\bar j}$ for a tuple $\bar j$ of positions; since $\Phi_e^{D(\mathcal B)}$ is total, it is defined at $0, \ldots, k - 1$ and at $\bar j$ with an initial segment of $D(\mathcal B)$ as oracle, and within the allowed number of steps once this segment is long enough; this segment is $\sigma = D_{\mathcal A}(\bar q)$ for an initial segment $\bar q \supseteq \bar p$ of $g$, and $\bar a$ satisfies $\theta_{\sigma, \bar j}$ with witnesses the rest of $\bar q$. If $\bar a$ and $\bar a'$ satisfy $\theta_{\sigma, \bar j}$, with witnesses forming tuples $\bar q = \bar p \bar z$ and $\bar q' = \bar p \bar z'$, then $D_{\mathcal A}(\bar q) = D_{\mathcal A}(\bar q') = \sigma$, $\bar a = \bar q_{\bar j}$ and $\bar a' = \bar q'_{\bar j}$, and the key claim gives an automorphism fixing $\bar p$ that maps $\bar a$ to $\bar a'$. So $\Phi$ is a c.e. existential Scott family over $\bar p$.
:::

:::quiz[the characterization of relative computable categoricity]
In the key claim, why must the two tuples $\bar q$ and $\bar q'$ have the same finite diagram, rather than merely extend $\bar p$?

- [x] The functional $\Phi_e$ only sees the oracle string: with the same diagram it gives the same values $v_j$, which are the bridge between $\bar q_{\bar j}$ and $\bar q'_{\bar j}$.
- [ ] Otherwise one of them could belong to $Q_e$.

  No extension of $\bar p$ belongs to $Q_e$, whatever its diagram.
- [ ] So that the formula $\theta_{\sigma, \bar j}$ is existential.

  The formula is existential for every $\sigma$; equality of diagrams is what makes it define an orbit.

---

The functional $\Phi_e$ is an isomorphism from the copy $\mathcal B$, built in the proof, onto $\mathcal A$. Is it used that $\Phi_e$ is total?

- [x] Yes, only to show that every tuple satisfies some formula of the family: the values of $\Phi_e$ at the positions of the tuple must converge on a finite part of the diagram.
- [ ] No, the key claim gives everything.

  The key claim shows that each formula defines an orbit; without totality, some tuples might satisfy no formula.
- [ ] Yes, to show that no extension of $\bar p$ is in $Q_e$.

  That uses only that $\Phi_e^{D(\mathcal B)}$ composed with $g^{-1}$ is an automorphism; totality is part of it, but the contradiction comes from the finite map $\pi^e_{\bar q}$.
:::

The proof **relativizes**, as does that of :ref{#prop-scott-rcc}: for a structure $\mathcal A$ computable in a set $X$, every copy $\mathcal B$ is isomorphic to $\mathcal A$ by an isomorphism computable in $X \oplus D(\mathcal B)$ if and only if $\mathcal A$ has an $X$-c.e. existential Scott family over some tuple. This form is used in the lesson on relative and plain categoricity.

## First applications

The theorem turns questions about all copies into questions about definability in one structure. Two consequences show how it is used.

:::corollary{#cor-rcc-constants}
Let $\bar c$ be a tuple of $\mathcal A$. Then $\mathcal A$ is relatively computably categorical if and only if the expansion $(\mathcal A, \bar c)$, with the entries of $\bar c$ named by constants, is.
:::

:::proof{of=cor-rcc-constants}
If $\Phi$ is a c.e. existential Scott family for $(\mathcal A, \bar c)$ over $\bar p$, replace the constants by parameters: the formulas become formulas over the tuple $\bar p \bar c$, and an automorphism of $(\mathcal A, \bar c)$ is an automorphism of $\mathcal A$ fixing $\bar c$; so $\Phi$ is a Scott family for $\mathcal A$ over $\bar p \bar c$. Conversely, let $\Phi$ be a c.e. existential Scott family for $\mathcal A$ over $\bar p$. For $\varphi(\bar p, \bar y, \bar x) \in \Phi$ with $|\bar y| = |\bar c|$, let $\varphi^{\bar c}(\bar p, \bar x)$ be $\varphi(\bar p, \bar c, \bar x)$, with $\bar c$ now constants. Let $\Psi$ be the set of formulas $\varphi^{\bar c}(\bar p, \bar x') \wedge \varepsilon(\bar x)$, where $\bar x'$ is a subtuple of the variables $\bar x$ and $\varepsilon$ is a conjunction of equalities $x_i = c_j$, one for each variable $x_i$ not in $\bar x'$; it is c.e. Every tuple $\bar a$ satisfies a formula of $\Psi$: let $\bar a'$ be the subtuple of the entries of $\bar a$ that are not in $\bar c$, take the formula $\varphi \in \Phi$ satisfied by the tuple $\bar c \bar a'$, and record the other entries by equalities. If $\bar a$ and $\bar b$ satisfy the same formula of $\Psi$, then $\bar c \bar a'$ and $\bar c \bar b'$ satisfy $\varphi$, so some automorphism fixing $\bar p$ maps $\bar c \bar a'$ to $\bar c \bar b'$; it fixes $\bar c$, so it maps the remaining entries of $\bar a$, which are entries of $\bar c$, to the same entries of $\bar b$. It is an automorphism of $(\mathcal A, \bar c)$ mapping $\bar a$ to $\bar b$.
:::

For plain computable categoricity, the corresponding statement fails: Cholak, Goncharov, Khoussainov and Shore built a computably categorical structure that is no longer computably categorical once a single element is named. The relative notion is robust under such changes because it is a definability notion.

:::corollary{#cor-rcc-definable-relations}
If $\mathcal A$ is relatively computably categorical, every relation on $\mathcal A$ that is invariant under the automorphisms fixing some tuple, and computable in $\mathcal A$, is relatively intrinsically computable.
:::

:::proof{of=cor-rcc-definable-relations}
Let $R$ be computable in $\mathcal A$ and invariant under the automorphisms fixing $\bar c$. Let $\mathcal B$ be a copy and $R^{\mathcal B}$ the image of $R$ under an isomorphism $h : \mathcal A \to \mathcal B$. By :ref{#cor-rcc-constants}, $(\mathcal A, \bar c)$ is relatively computably categorical, so there is an isomorphism $f : (\mathcal A, \bar c) \to (\mathcal B, h(\bar c))$ computable in $D(\mathcal B)$ and the finite tuple $h(\bar c)$. Then $h^{-1} \circ f$ is an automorphism of $\mathcal A$ fixing $\bar c$, so it preserves $R$, and $R^{\mathcal B} = h(R) = f(R)$. Since $f$ is computable in $D(\mathcal B)$ and $R$ is computable, $R^{\mathcal B} = \{ \bar b : f^{-1}(\bar b) \in R \}$ is computable in $D(\mathcal B)$.
:::

So a structure with a computable relation that is invariant over some parameters, but not relatively intrinsically computable, is not relatively computably categorical. The next lesson uses this to settle the classical examples.

## Notes and references

:ref{#thm-rcc-scott} is due to Ash, Knight, Manasse and Slaman (1989, Theorem 4) and, independently, to Chisholm (1990); Goncharov (1975) had isolated the same syntactic condition for computable categoricity of structures with a decidable two-quantifier theory (see the lesson on relative and plain categoricity). Montalbán (Theorem VIII.4) proves the hard direction with a 2-generic enumeration, first forcing the functional to be an isomorphism; the proof given here replaces genericity by the diagonalization of :ref{#thm-akms-chisholm-1}, which only needs that no extension of $\bar p$ makes the functional err, totality being used only for the existence of formulas. Ash and Knight state the result as Theorem 10.14, for all levels of the hyperarithmetic hierarchy at once. The example of Cholak, Goncharov, Khoussainov and Shore is from their 1999 paper.

- C. J. Ash, J. F. Knight, M. Manasse and T. A. Slaman, *Generic copies of countable structures*, Annals of Pure and Applied Logic 42 (1989), 195–205.
- J. Chisholm, *Effective model theory vs. recursive model theory*, Journal of Symbolic Logic 55 (1990), 1168–1191.
- P. Cholak, S. Goncharov, B. Khoussainov and R. A. Shore, *Computably categorical structures and expansions by constants*, Journal of Symbolic Logic 64 (1999), 13–37.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Sections III.4 and VIII.2.
- C. J. Ash and J. F. Knight, *Computable Structures and the Hyperarithmetical Hierarchy*, Chapter 10.

:::::exercises
::::exercise{#ex-rcc-delta2-omega difficulty=2 objective="Use the theorem on ω and on an expansion of ω to see that the successor relation is what is missing." lessons="computable-structures/back-and-forth"}
Show that $\omega = (\nat; \leq)$ is not relatively computably categorical, but that the expansion $(\nat; \leq, S)$ by the successor relation is. Deduce that the successor relation is not relatively intrinsically computable on $\omega$.

:::solution
By :ref{#ex-omega-no-scott}, $\omega$ has no existential Scott family over any tuple, so by :ref{#thm-rcc-scott} it is not relatively computably categorical. In $(\nat; \leq, S)$, the formulas $\varphi_n(x)$ saying "$x$ is reached by $n$ steps of $S$ from an element with no $S$-predecessor" are not existential, but with the parameter $p = 0$ the formulas of :ref{#ex-scott-families} for $(\nat; S)$ are, and they form a c.e. existential Scott family over $0$: the expansion is rigid, and each element satisfies exactly one formula. So $(\nat; \leq, S)$ is relatively computably categorical. If $S$ were relatively intrinsically computable on $\omega$, a copy $\mathcal B$ of $\omega$ would compute $S^{\mathcal B}$, hence the diagram of a copy of $(\nat; \leq, S)$, hence an isomorphism with the standard copy, uniformly from the image of $0$; so $\omega$ would be relatively computably categorical, which it is not.
:::
::::

::::exercise{#ex-rcc-equivalence-structure difficulty=2 objective="Apply the characterization to equivalence structures, where the parameters name the finitely many exceptional classes."}
An equivalence structure is a set with an equivalence relation $E$. Let $\mathcal E$ be a computable equivalence structure with infinitely many classes of size $2$ and no other classes. Show that $\mathcal E$ is relatively computably categorical. Then let $\mathcal E'$ have infinitely many classes of each finite size $n \geq 1$ and no infinite class; show that $\mathcal E'$ has no existential Scott family over any tuple.

:::solution
For $\mathcal E$: describe a tuple $\bar a$ by the quantifier-free formula listing which entries are $E$-equivalent. Two tuples $\bar a$ and $\bar b$ with the same description are automorphic: a class meeting $\bar a$ in two entries is mapped to the class of the corresponding entries of $\bar b$, entry to entry; a class meeting $\bar a$ in one entry is mapped to the class of the corresponding entry of $\bar b$, the other element of the first class going to the other element of the second; and the infinitely many remaining classes of each side are matched by any bijection. So these formulas form a c.e. Scott family without parameters, made of quantifier-free formulas, and $\mathcal E$ is relatively computably categorical by :ref{#thm-rcc-scott}.

For $\mathcal E'$: let $\bar p$ be a tuple and $\exists \bar y\, \psi(\bar p, x, \bar y)$ an existential formula true of an element $a$ whose class $C$ contains no entry of $\bar p$, with witnesses $\bar m$. Let $C$ have size $n$, and let $F$ be the finite set of entries of $\bar p$, $a$ and $\bar m$. Choose a class $C'$ of size $n + 1$ disjoint from $F$, and let $h$ be the map on $F$ that fixes the elements outside $C$ and maps $F \cap C$, which has at most $n$ elements, injectively into $C'$. It is injective and preserves $E$ in both directions: elements of $C$ go to $C'$, which meets no other element of $F$ or of its image. So it preserves the quantifier-free formula $\psi$, and $h(a)$ satisfies the existential formula with witnesses $h(\bar m)$. But $h(a)$, in a class of size $n + 1$, is not automorphic to $a$. Since the classes containing entries of $\bar p$ are finitely many, there are such elements $a$, and no existential Scott family over $\bar p$ exists.
:::
::::
:::::
