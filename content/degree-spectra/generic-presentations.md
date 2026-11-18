---
title: Generic presentations
summary: The degree spectrum of a structure; 1-generic enumerations and presentations, which decide every relatively intrinsically c.e. set of tuples; a set c.e. in a sufficiently generic presentation is c.e. in every copy; Richter's theorem that a structure whose existential types are c.e. has copies forming a c.e.-minimal pair with any given set, so that such a structure has no Turing degree unless it is computable; linear orders as the main example.
duration: 40
prerequisites: [intrinsic-definability/intrinsic-relations, cohen-genericity/one-genericity]
---

Knight's theorem (:ref{#thm-knight-coding}) shows that the Turing degrees of the copies of a non-trivial structure form a set closed upward. This set, the degree spectrum, is the standard measure of the computational complexity of a structure. This lesson introduces the main tool for studying it. A copy built from a sufficiently generic enumeration has no computational property without a structural reason. If such a copy enumerates a set of numbers, then every copy does. The first application is Richter's theorem: many structures, linear orders among them, cannot have a Turing degree unless they have a computable copy.

## Degree spectra

:::definition{#def-degree-spectrum}
The **degree spectrum** of a structure $\mathcal A$ is the set
$$
\mathrm{DgSp}(\mathcal A) = \{ X \subseteq \nat : X \text{ computes a copy of } \mathcal A \}.
$$
:::

The degree spectrum is closed upward under Turing reducibility, so it is a set of Turing degrees. By Knight's theorem, if $\mathcal A$ is not trivial, it is exactly the set of degrees of the copies of $\mathcal A$. The structure has a computable copy if and only if its spectrum contains $\mathbf 0$, in which case the spectrum is the set of all degrees. Two shapes of spectra have names. A structure has **Turing degree** $Y$ if $\mathrm{DgSp}(\mathcal A) = \{ X : Y \leq_T X \}$, an upper cone. It has **enumeration degree** $Y$ if $\mathrm{DgSp}(\mathcal A) = \{ X : Y \text{ is c.e. in } X \}$, an **enumeration cone**. The enumeration cone of $Y \oplus \overline Y$ is the upper cone of $Y$, so a structure with a Turing degree has an enumeration degree. Both shapes occur, as the next lesson shows. The central question is which sets of degrees are degree spectra.

## Generic enumerations

Throughout, $\mathcal A$ is an ω-presentation of a structure in a relational vocabulary. We use the pull-backs of enumerations of the course on computable structures. For an injective enumeration $g : \nat \to A$, the pull-back $g^{-1}(\mathcal A)$ is an ω-presentation isomorphic to $\mathcal A$, and its atomic diagram is the union of the finite diagrams $D_{\mathcal A}(g \uh k)$ of the initial segments of $g$. Let $A^\star$ be the set of finite tuples of elements of $A$ without repetitions. For $\bar p, \bar q \in A^\star$, write $\bar p \subseteq \bar q$ if $\bar p$ is an initial segment of $\bar q$.

A tuple $\bar p \in A^\star$ **decides** a set $R \subseteq A^\star$ if either some initial segment of $\bar p$ is in $R$, or no extension of $\bar p$ is in $R$. Given a set $X \subseteq \nat$, a relation $R$ on $\mathcal A$ is **$X$-r.i.c.e.** if its image $R^{\mathcal B}$ is c.e. in $D(\mathcal B) \oplus X$ for every copy $(\mathcal B, R^{\mathcal B})$ of $(\mathcal A, R)$. For $X = \emptyset$, this is the definition of r.i.c.e. relations (:ref{#def-rice}).

:::definition{#def-generic-enumeration}
Let $X \subseteq \nat$. An injective function $g : \nat \to A$ is an **$X$-generic enumeration** of $\mathcal A$ if every $X$-r.i.c.e. set $R \subseteq A^\star$ is decided by some initial segment $g \uh k$ of $g$. A **$X$-generic presentation** of $\mathcal A$ is the pull-back $g^{-1}(\mathcal A)$ of an $X$-generic enumeration $g$ that is onto $A$. For $X = \emptyset$, we say **generic**; Montalbán says *1-generic*.
:::

This is the analogue, for structures, of 1-genericity relative to $X$ for sets (:ref{#def-relative-genericity}). The difference is in the sets to be decided. For sets, these are the $X$-c.e. sets of strings. For structures, they are the sets of tuples that every copy can enumerate with the help of $X$. The definition depends only on the isomorphism type of $\mathcal A$, which is what makes generic presentations useful.

:::lemma{#lem-generic-exists}
For every $X$, the structure $\mathcal A$ has an $X$-generic enumeration onto $A$, computable in $(D(\mathcal A) \oplus X)'$.
:::

:::proof{of=lem-generic-exists}
Every $X$-r.i.c.e. set $R \subseteq A^\star$ is c.e. in $D(\mathcal A) \oplus X$, since $\mathcal A$ is one of its copies. So it suffices to decide every set $V_e = W_e^{D(\mathcal A) \oplus X} \cap A^\star$. We build $g = \bigcup_s \bar p_s$ with $\bar p_s \in A^\star$, starting from the empty tuple. At stage $2e + 1$, ask whether some $\bar q \in A^\star$ extending $\bar p_{2e}$ belongs to $V_e$. This is a $\Sigma^0_1$ question relative to $D(\mathcal A) \oplus X$, so $(D(\mathcal A) \oplus X)'$ answers it. If the answer is yes, let $\bar p_{2e+1}$ be the first such $\bar q$ found; otherwise $\bar p_{2e+1} = \bar p_{2e}$. Either way $\bar p_{2e+1}$ decides $V_e$. At stage $2e + 2$, append to $\bar p_{2e+1}$ the least element of $A$ not already in it. The function $g$ is injective, onto, and decides every $V_e$.
:::

Being onto is in fact automatic (:ref{#ex-generic-onto}). The pull-back $\mathcal B = g^{-1}(\mathcal A)$ satisfies $D(\mathcal B) \leq_T g \oplus D(\mathcal A)$. So a structure with a copy computable in $Z$ has an $X$-generic presentation computable in $(Z \oplus X)'$.

::::exercise{#ex-generic-onto difficulty=1 objective="Use a dense r.i.c.e. set of tuples to show that a generic enumeration meets every element."}
Let $g$ be an injective function that decides every r.i.c.e. subset of $A^\star$. Show that $g$ is onto $A$.

:::solution
Fix $a \in A$, and let $R_a$ be the set of tuples in $A^\star$ that contain $a$. It is r.i.c.e., with parameter $a$: in a copy, a tuple is in the image of $R_a$ if one of its entries is the image of $a$, which is decidable once that image is known. It is also dense: every $\bar q \in A^\star$ has an extension in $R_a$, namely $\bar q$ itself if $a$ occurs in it, and $\bar q a$ otherwise. So no initial segment of $g$ avoids $R_a$, and some initial segment of $g$ belongs to $R_a$. Then $a$ is in the range of $g$.
:::
::::

## Sets enumerated by generic presentations

Recall that a set $Y \subseteq \nat$ is **c.e.-coded** by $\mathcal A$ if it is c.e. in every copy of $\mathcal A$. By Knight's corollary (:ref{#cor-knight-ce-coded}), these are the sets enumeration reducible to the existential type of some tuple. The next lemma shows that one sufficiently generic copy suffices to detect them.

:::lemma{#lem-generic-ce}
Let $g$ be a $Y$-generic enumeration of $\mathcal A$ onto $A$, and $\mathcal B = g^{-1}(\mathcal A)$. If $Y$ is c.e. in $D(\mathcal B)$, then $Y$ is c.e.-coded by $\mathcal A$.
:::

**Intuition.** As in the proof of the theorem of Ash, Knight, Manasse, Slaman and Chisholm (:ref{#thm-akms-chisholm-1}), consider the tuples along which the enumeration of $Y$ goes wrong. Genericity says that $g$ either takes such a tuple or reaches a point beyond which no wrong tuple exists. The first case cannot happen, and in the second case, the extensions of that point enumerate exactly $Y$, in every copy.

:::proof{of=lem-generic-ce}
Let $Y = W_e^{D(\mathcal B)}$. For a tuple $\bar q \in A^\star$, write $W_e^{D_{\mathcal A}(\bar q)}$ for the finite set enumerated by $W_e$ in $|\bar q|$ steps with the finite oracle $D_{\mathcal A}(\bar q)$. Let
$$
Q = \{ \bar q \in A^\star : \text{some } n \in W_e^{D_{\mathcal A}(\bar q)} \text{ satisfies } n \notin Y \}.
$$
The set $Q$ is $Y$-r.i.c.e.: in a copy $\mathcal C$, the image of $Q$ is the set of tuples $\bar q'$ of $\mathcal C$ without repetitions such that some $n \in W_e^{D_{\mathcal C}(\bar q')}$ is not in $Y$. This is c.e. in $D(\mathcal C) \oplus Y$, since $D_{\mathcal C}(\bar q')$ is computable from $D(\mathcal C)$ and $Y$ decides whether $n \in Y$. Here we use that an isomorphism maps a tuple to a tuple with the same finite atomic diagram.

So some initial segment of $g$ decides $Q$. No initial segment $g \uh k$ belongs to $Q$. Indeed, $D_{\mathcal A}(g \uh k)$ is an initial part of $D(\mathcal B)$, so $W_e^{D_{\mathcal A}(g \uh k)} \subseteq W_e^{D(\mathcal B)} = Y$. Hence some $\bar p = g \uh k$ has no extension in $Q$. We claim that
$$
Y = \{ n : \text{some } \bar q \in A^\star \text{ extending } \bar p \text{ satisfies } n \in W_e^{D_{\mathcal A}(\bar q)} \}.
$$
If $n \in Y = W_e^{D(\mathcal B)}$, the enumeration uses a finite part of $D(\mathcal B)$. So $n \in W_e^{D_{\mathcal A}(g \uh m)}$ for some $m \geq k$, and $g \uh m$ extends $\bar p$. Conversely, if $n \in W_e^{D_{\mathcal A}(\bar q)}$ with $\bar q$ extending $\bar p$ and $n \notin Y$, then $\bar q \in Q$, which is excluded.

The right-hand side is c.e. in every copy $\mathcal C$. Let $\bar p'$ be the image of $\bar p$ in $\mathcal C$, a finite piece of information. Then $n$ belongs to the set if and only if some tuple $\bar q'$ of $\mathcal C$ without repetitions, extending $\bar p'$, satisfies $n \in W_e^{D_{\mathcal C}(\bar q')}$. This search is effective in $D(\mathcal C)$. So $Y$ is c.e.-coded.
:::

The genericity must be relative to $Y$, because the set $Q$ to be decided refers to $Y$. In practice the lemma is applied to a presentation that is generic relative to a set computing $Y$. If $Y \leq_T Z$, every $Y$-r.i.c.e. set is $Z$-r.i.c.e., so a $Z$-generic enumeration is $Y$-generic.

:::quiz[sets enumerated by generic presentations]
In the proof of :ref{#lem-generic-ce}, why can no initial segment of $g$ belong to $Q$?

- [x] Along $g$, the finite diagrams $D_{\mathcal A}(g \uh k)$ are parts of the diagram of $\mathcal B$, and $W_e$ enumerates only elements of $Y$ from $D(\mathcal B)$; a tuple in $Q$ makes $W_e$ enumerate an element outside $Y$.
- [ ] Because $Q$ is empty.

  $Q$ need not be empty: tuples off $g$ may give wrong enumerations. The point is that $g$ avoids them from some point on.
- [ ] Because $g$ is onto.

  Surjectivity plays no role here. What matters is that $g$ is the enumeration from which $\mathcal B$ is built.

---

Why must the enumeration be generic relative to $Y$, and not merely generic?

- [x] The set $Q$ of tuples that make $W_e$ err mentions $Y$, through the condition $n \notin Y$, so it is in general only $Y$-r.i.c.e.
- [ ] To make $\mathcal B$ computable in $Y$.

  Genericity does not make $\mathcal B$ computable in anything; the generic enumeration is built with a jump.
- [ ] Because $Y$ is c.e.

  $Y$ is not assumed c.e.; that is what the lemma concludes, in the relativized form "c.e. in every copy".
:::

## Richter's theorem

A structure has **c.e. existential types** if the existential type $\exists\text{-}\mathrm{tp}_{\mathcal A}(\bar p)$ of every tuple is c.e. By :ref{#cor-knight-ce-coded}, this holds if and only if every set c.e.-coded by $\mathcal A$ is c.e. Indeed, a set enumeration reducible to a c.e. set is c.e., and each existential type is c.e.-coded. Richter called the corresponding property, with computable types, the *computable embeddability condition*; Montalbán uses the *c.e. embeddability condition*.

:::theorem[Richter]{#thm-richter}
Let $\mathcal A$ have c.e. existential types, and let $X \subseteq \nat$. There is a copy $\mathcal B$ of $\mathcal A$ such that every set c.e. in both $X$ and $D(\mathcal B)$ is c.e.
:::

:::proof{of=thm-richter}
Let $\mathcal B$ be an $X'$-generic presentation of $\mathcal A$ (:ref{#lem-generic-exists}). Let $Y$ be c.e. in $X$ and in $D(\mathcal B)$. Then $Y \leq_T X'$, so the enumeration defining $\mathcal B$ is $Y$-generic. By :ref{#lem-generic-ce}, $Y$ is c.e.-coded by $\mathcal A$, hence c.e.
:::

:::corollary[Richter]{#cor-richter-no-degree}
Let $\mathcal A$ have c.e. existential types. If $\mathcal A$ has an enumeration degree, or a Turing degree, then $\mathcal A$ has a computable copy.
:::

:::proof{of=cor-richter-no-degree}
Suppose that $\mathrm{DgSp}(\mathcal A) = \{ Z : Y \text{ is c.e. in } Z \}$. Every copy of $\mathcal A$ is in the spectrum, so $Y$ is c.e. in every copy, that is, c.e.-coded. Hence $Y$ is c.e. Then every set, the empty set included, is in the spectrum, and $\mathcal A$ has a computable copy. A Turing degree is a particular enumeration degree.
:::

The proof of the corollary does not need the full strength of the theorem, only :ref{#cor-knight-ce-coded}. The theorem says more: the copies of $\mathcal A$ cannot all share any non-computable information, even a set that is merely c.e. in some degree.

:::example[Richter]{#ex-linear-orders-ce-types}
Linear orders have computable existential types. Let $a_1 < \cdots < a_k$ be a tuple of a linear order $\mathcal L$, listed in increasing order. Record the number of elements of each of the $k + 1$ intervals $(-\infty, a_1)$, $(a_1, a_2)$, …, $(a_k, +\infty)$; each number is finite or infinite. An existential formula $\exists \bar y\, \varphi(\bar x, \bar y)$, with $\varphi$ quantifier-free, holds of $\bar a$ if and only if some arrangement of $\bar y$ satisfies $\varphi$. An arrangement says how the $y_j$ are ordered among themselves and, for each $y_j$, either which $a_i$ it equals or in which interval it lies. It is realized if and only if no interval receives more new elements than it has. There are finitely many arrangements, and checking one is a finite computation from the recorded numbers. So the existential type of $\bar a$ is computable from finitely many numbers and the order of $\bar a$, hence computable.
:::

So a linear order with a Turing degree, or an enumeration degree, has a computable copy. In particular no linear order has the degree spectrum $\{ Z : Y \leq_T Z \}$ for a non-computable $Y$. Richter proved the same for trees, viewed as partial orders. Boolean algebras, vector spaces, algebraically closed fields and equivalence structures also have c.e. existential types (Montalbán, Section V.1).

## Notes and references

Degree spectra were introduced by Richter in her thesis. :ref{#thm-richter}, :ref{#cor-richter-no-degree} and :ref{#ex-linear-orders-ce-types} are from Richter (1981). The proof through generic presentations is Montalbán's, from *Within the Arithmetic*, Chapter IV (Definition IV.13, Lemma IV.14, Theorem IV.20, Corollary IV.21) and Section V.1 (Theorem V.7, Theorem V.10). Generic presentations go back to the forcing arguments of Knight (1986) and of Manasse and Slaman, published in Ash, Knight, Manasse and Slaman (1989). Here the existence lemma uses the jump of $D(\mathcal A) \oplus X$. Montalbán builds a generic enumeration computably in the complete r.i.c.e. relation of the structure, which can be strictly weaker.

- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Cambridge University Press, 2021, Chapters IV and V.
- L. J. Richter, *Degrees of structures*, Journal of Symbolic Logic 46 (1981), 723–731.
- C. J. Ash, J. F. Knight, M. Manasse and T. A. Slaman, *Generic copies of countable structures*, Annals of Pure and Applied Logic 42 (1989), 195–205.

:::::exercises
::::exercise{#ex-enumeration-degree-ce-types difficulty=1 objective="Apply Knight's corollary to the base of an enumeration cone."}
Suppose that $\mathcal A$ has enumeration degree $Y$. Show that $Y$ is enumeration reducible to the existential type of some tuple of $\mathcal A$, and that $Y$ is c.e. in every copy of $\mathcal A$.

:::solution
Every copy of $\mathcal A$ is computable in itself, so its diagram belongs to the spectrum $\{ Z : Y \text{ is c.e. in } Z \}$. So $Y$ is c.e. in the diagram of every copy: $Y$ is c.e.-coded by $\mathcal A$. By :ref{#cor-knight-ce-coded}, $Y \leq_e \exists\text{-}\mathrm{tp}_{\mathcal A}(\bar p)$ for some tuple $\bar p$.
:::
::::

::::exercise{#ex-exact-pair-copies difficulty=2 objective="Relativize the construction of generic presentations to find two copies whose common c.e. information is exactly the c.e.-coded sets."}
Let $\mathcal B$ be a copy of $\mathcal A$. Show that there is a copy $\mathcal C$ such that a set is c.e. in both $D(\mathcal B)$ and $D(\mathcal C)$ if and only if it is c.e.-coded by $\mathcal A$.

:::solution
Let $\mathcal C$ be a $D(\mathcal B)'$-generic presentation of $\mathcal A$ (:ref{#lem-generic-exists}). A set c.e.-coded by $\mathcal A$ is c.e. in the diagram of every copy, in particular of $\mathcal B$ and $\mathcal C$. Conversely, let $Y$ be c.e. in $D(\mathcal B)$ and in $D(\mathcal C)$. Then $Y \leq_T D(\mathcal B)'$, so every $Y$-r.i.c.e. set is $D(\mathcal B)'$-r.i.c.e., and the enumeration defining $\mathcal C$ is $Y$-generic. By :ref{#lem-generic-ce}, $Y$ is c.e.-coded.
:::
::::

::::exercise{#ex-dense-order-generic difficulty=1 objective="See what genericity means for a structure whose existential types are trivial."}
Let $\mathcal Q = (\mathbb Q; <)$. Show that every r.i.c.e. subset $R$ of $Q^\star$ that is closed under extensions and dense (every tuple has an extension in $R$) contains an initial segment of every generic enumeration. Give an example of such a set $R$ that says that the enumeration has, among its first elements, three elements in increasing order of their positions.

:::solution
The first statement is the definition: a generic enumeration $g$ has an initial segment that decides $R$, and since every tuple has an extension in $R$, the initial segment cannot avoid $R$; so some initial segment of $g$ is in $R$. For the example, let $R$ be the set of tuples $\bar q \in Q^\star$ containing indices $i < j < k$ with $q_i < q_j < q_k$. It is closed under extensions, and r.i.c.e. without parameters, since in a copy the condition is decided by the diagram of the tuple. It is dense: given $\bar q$, append three new rationals in increasing order, which exist because $\mathbb Q$ is infinite.
:::
::::
:::::
