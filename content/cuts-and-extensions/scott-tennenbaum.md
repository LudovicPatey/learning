---
title: Scott sets as standard systems, and Tennenbaum's theorem
summary: Every countable Scott set is the standard system of a model of Peano arithmetic, built from a chain of completions inside the Scott set (Scott); the Scott set problem; the standard system of a non-standard model contains non-computable sets, and no non-standard model of IΔ₀ + exp has a computable addition (Tennenbaum).
duration: 45
prerequisites: [weak-konig-cuts, pi01-classes/pa-degrees, truth-and-provability/truth-definitions]
---

The two previous lessons showed that the standard system of a non-standard model of $\mathrm I\Delta_0 + \mathrm{exp}$ is a Scott set (:ref{#cor-ssy-scott-set}). This lesson proves the converse for countable Scott sets, following Scott: the closure under computations and under weak König's lemma is all that a countable standard system must satisfy, even for models of Peano arithmetic. The model is built from a chain of complete theories inside the Scott set, each one deciding which standard numbers belong to a new constant. The lesson ends with a consequence of the separation lemma (:ref{#lem-cut-separation}) in the opposite direction: since the standard system contains non-computable sets, a non-standard model of arithmetic cannot be computable (Tennenbaum).

## Countable Scott sets are standard systems

Since the complete consistent extensions of Peano arithmetic are the paths of a computable binary tree (proof of :ref{#thm-pa-completions}), the standard system of every non-standard model of $\mathrm I\Delta_0 + \mathrm{exp}$ contains one of them, by :ref{#cor-ssy-scott-set}. Scott's theorem shows that nothing more can be said about a countable standard system.

:::theorem[Scott]{#thm-scott-converse}
Let $\mathcal X$ be a countable Scott set. There is a countable model $M$ of $\mathrm{PA}$ with $\mathrm{SSy}(M) = \mathcal X$. Moreover, for every complete consistent extension $T \in \mathcal X$ of $\mathrm{PA}$, $M$ can be chosen to be a model of $T$.
:::

:::proof{of=thm-scott-converse}
*A completion in $\mathcal X$.* We use the following fact, for a theory $S$ in a language with a computable coding of sentences: if $S$ is consistent and computable in some $Z \in \mathcal X$, then $\mathcal X$ contains a complete consistent extension of $S$. Indeed, the proof of :ref{#thm-pa-completions}, relativized to $Z$, shows that the complete consistent extensions of $S$ are the members of a non-empty $\Pi^0_1(Z)$ class, hence the infinite paths of an infinite binary tree computable in $Z$; this tree belongs to $\mathcal X$, and so does one of its paths. In particular, since $\mathrm{PA}$ is computable and $\mathcal X$ contains the computable sets, $\mathcal X$ contains a complete consistent extension of $\mathrm{PA}$. Fix one, $T$; it may be any given complete consistent extension of $\mathrm{PA}$ in $\mathcal X$.

*A chain of theories.* Enumerate $\mathcal X = \{ X_0, X_1, \dots \}$, and let $c_0, c_1, \dots$ be new constants, $\mathcal L_i = \mathcal L_A \cup \{ c_j : j < i \}$. We build complete consistent $\mathcal L_i$-theories $T_0 = T \subseteq T_1 \subseteq \cdots$ in $\mathcal X$. Given $T_i$, let
$$
S_i = T_i \cup \{ \bar k \in c_i : k \in X_i \} \cup \{ \neg\, \bar k \in c_i : k \notin X_i \},
$$
with the bounded formula $x \in y$ of :ref{#def-ack-membership}. A finite part of $S_i$ mentions numbers $k < m$ only; let $p = \sum_{k \in X_i,\, k < m} 2^k$. Each sentence $\bar k \in \bar p$ or $\neg\, \bar k \in \bar p$ that is true in $\nat$ is a true bounded sentence, provable in $\mathrm{PA}^-$ by :ref{#thm-sigma1-complete}, hence in $T_i$; so any model of $T_i$ in which $c_i$ is interpreted as $p$ satisfies the finite part. By compactness $S_i$ is consistent. It is computable in $T_i \oplus X_i \in \mathcal X$, so $\mathcal X$ contains a complete consistent extension $T_{i+1}$ of $S_i$ in $\mathcal L_{i+1}$.

*The model.* The union $T_\omega = \bigcup_i T_i$ is a complete consistent theory in $\mathcal L_\omega = \bigcup_i \mathcal L_i$, consistent by compactness. Let $N \models T_\omega$, and let $M$ be the set of elements of $N$ definable without parameters in the language $\mathcal L_\omega$. If $N \models \exists x\ \varphi(x, \bar d)$, with $\bar d$ definable, then the least such $x$, which exists since the reduct of $N$ to $\mathcal L_A$ satisfies the least number principle of $\mathrm{PA}$ for formulas with parameters, is definable. So $M$ contains the interpretations of the constants and, by the Tarski–Vaught test, is an elementary substructure of $N$; its reduct to $\mathcal L_A$ is a model of $T$.

*Its standard system.* For each $i$, the element $c_i^N \in M$ satisfies $\mathrm{Ack}(c_i^N) \cap \nat = X_i$, by the sentences of $S_i$. Conversely, let $d \in M$ be defined by $\varphi(x)$, an $\mathcal L_j$-formula. For $k \in \nat$, $k \in \mathrm{Ack}(d)$ if and only if $N \models \exists x\, (\varphi(x) \wedge \bar k \in x)$, if and only if this $\mathcal L_j$-sentence belongs to $T_j$, by the completeness of $T_j$. So $\mathrm{Ack}(d) \cap \nat$ is computable in $T_j \in \mathcal X$, and belongs to $\mathcal X$. So the sets $\mathrm{Ack}(d) \cap \nat$, for $d \in M$, are exactly the members of $\mathcal X$. Since $\mathcal X$ contains the infinite set $\nat$, some element of $M$ has infinitely many standard numbers as Ackermann members, so it is not a standard number (:ref{#lem-ack-basic}): $M$ is non-standard, and $\mathrm{SSy}(M) = \mathcal X$.
:::

:::quiz[Scott's theorem]
In the last step of the proof of :ref{#thm-scott-converse}, why is the set coded by $d$ in $\mathcal X$, rather than only arithmetic in $\mathcal X$?

- [x] Because $d$ is definable from finitely many constants, and the complete theory $T_j$ of these constants, which belongs to $\mathcal X$, decides every sentence $\exists x\, (\varphi(x) \wedge \bar k \in x)$; membership is read off $T_j$ by a computation.
- [ ] Because $M$ is countable.

  Countability is used to enumerate $\mathcal X$; it does not bound the complexity of the coded sets.
- [ ] Because $\mathrm{SSy}(M)$ is a Scott set.

  This gives closure properties of $\mathrm{SSy}(M)$, not its inclusion in $\mathcal X$.
:::

The theorem is the first answer to the **Scott set problem**: is every Scott set the standard system of a model of $\mathrm{PA}$? Knight and Nadel (1982) proved it for Scott sets of cardinality $\aleph_1$, so the answer is positive under the continuum hypothesis. Without it the problem is open; Gitman (2008) obtained a positive answer, under the proper forcing axiom, for the Scott sets she calls proper: those that are arithmetically closed and whose quotient by the ideal of finite sets is a proper partial order.

## Tennenbaum's theorem

The separation lemma also produces non-computable sets in the standard system. By :ref{#thm-dnc2-no-computable}, the disjoint c.e. sets
$$
A_0 = \{ e : \Phi_e(e)\converge = 0 \}, \qquad A_1 = \{ e : \Phi_e(e)\converge = 1 \}
$$
cannot be separated by a computable set. Both are defined in $\nat$ by $\Sigma_1$ formulas (:ref{#cor-sigma1-ce}), so :ref{#lem-cut-separation}, applied to the standard cut without set parameters, gives a set in $\mathrm{SSy}(M)$ that separates them. Such a set is not computable. If the model were computable, every set in its standard system would be.

:::theorem[Tennenbaum]{#thm-tennenbaum}
Let $M$ be a non-standard model of $\mathrm I\Delta_0 + \mathrm{exp}$ whose domain is $\nat$. Then the addition of $M$ is not a computable function.
:::

Every countable model is isomorphic to one whose domain is $\nat$; the theorem says that none of these copies has a computable addition, so in particular that no non-standard model of Peano arithmetic is computable.

:::proof{of=thm-tennenbaum}
Suppose that $+^M$ is computable. Let $C = \mathrm{Ack}(d) \cap \nat \in \mathrm{SSy}(M)$ separate $A_0$ from $A_1$, as above. We show that $C$ is computable, which contradicts :ref{#thm-dnc2-no-computable}: the set $C$ contains $A_0$ and is disjoint from $A_1$, so its characteristic function differs from $\Phi_e(e)$ whenever this converges.

The elements $0^M$ and $1^M$ are fixed numbers, and the value $\bar m^M$ of each numeral is computed by adding $1^M$ to $0^M$, $m$ times. For an element $u$ and $m \in \nat$, the element $\bar m^M \cdot u$ is $u + \cdots + u$, with $m$ terms, also computable from $u$ and $m$. Given $n \in \nat$, let $p = 2^n$. By :ref{#def-ack-membership}, and since the power $2^n$ computed in $M$ is the standard number $\bar p^M$ (:ref{#lem-delta0-absolute}, applied to the bounded formula $\varepsilon$ of :ref{#fact-exp}), $n \in d$ holds in $M$ if and only if the remainder of $d$ in the division by $2p$ is at least $p$. By :ref{#prop-idelta0-basic}, $d = \overline{2p}^M \cdot u + \bar r^M$ for a unique pair $(u, r)$ with $u \in M$ and $r < 2p$; the remainder is a standard number $r$, since it is below a standard number (:ref{#prop-standard-part}). To decide whether $n \in C$, search through all pairs $(u, r)$, with $u$ an element of the domain $\nat$ of $M$ and $r < 2p$ a natural number, until $d = \overline{2p}^M \cdot u + \bar r^M$, which can be checked with $+^M$; the search terminates, and $n \in C$ if and only if $r \geq p$. So $C$ is computable.
:::

:::quiz[Tennenbaum's theorem]
Where does the proof use that $M$ is non-standard?

- [x] In :ref{#lem-cut-separation}, applied to the standard cut, which must be a proper cut of $M$ for overspill to apply.
- [ ] To have codes for bounded sets.

  Bounded comprehension holds in every model of $\mathrm I\Delta_0 + \mathrm{exp}$, including $\nat$.
- [ ] To make the search for $(u, r)$ terminate.

  The search terminates in every model, by division with remainder; in $\nat$ the addition is computable and the theorem fails for the other reason.
:::

Tennenbaum (1959) proved that in a non-standard model of Peano arithmetic neither addition nor multiplication is computable; the case of multiplication codes sets by divisibility by primes instead of binary digits. The proof given here, through the standard system, shows more: if $M \models \mathrm I\Delta_0 + \mathrm{exp}$ is non-standard with domain $\nat$, every set in $\mathrm{SSy}(M)$ is computable in $+^M$, and $\mathrm{SSy}(M)$ contains a set that is not computable.

Some induction is necessary. The model $\mathbb Z[X]^+$ of $\mathrm{PA}^-$ (:ref{#ex-zx-plus}) is non-standard, and it is computable: a polynomial is a finite list of integers, and its sum, product and sign are computed from the lists. Shepherdson (1964) built computable non-standard models even of open induction, in which induction holds for quantifier-free formulas. The proof above uses bounded induction in $M$ twice: for overspill in the separation lemma, and for the codes of bounded sets given by $\mathrm{exp}$.

## Exercises

::::exercise{#ex-ssy-truth difficulty=2}
Let $n \geq 1$ and $M$ a non-standard model of $\mathrm I\Sigma_n$. Show that the set of codes of $\Sigma^*_n$ sentences (:ref{#def-delta0-star}) true in $M$ belongs to $\mathrm{SSy}(M)$. Deduce that if $M$ is a non-standard model of the theory of $\nat$, then $\mathrm{SSy}(M)$ contains every arithmetic set.

:::solution
By :ref{#prop-isigma1-exp}, $M \models \mathrm I\Delta_0 + \mathrm{exp}$. The formula $\mathrm{Sat}_{\Sigma_n}(z, 0)$ is $\Sigma_n$ in $M$ (:ref{#thm-sat-n}), so for a non-standard $a$, the set $\{ z < a : \mathrm{Sat}_{\Sigma_n}(z, 0) \}$ is coded in $M$ by :ref{#thm-friedman-coded}, by some $c$. For a standard $\Sigma^*_n$ sentence $\sigma$, $\ulcorner \sigma \urcorner < a$ and $M \models \sigma \leftrightarrow \mathrm{Sat}_{\Sigma_n}(\ulcorner \sigma \urcorner, 0)$ by :ref{#cor-snowing}. So $\mathrm{Ack}(c) \cap \nat$ agrees with the set $S$ of codes of true $\Sigma^*_n$ sentences on the computable set of codes of $\Sigma^*_n$ sentences, and $S$ is the intersection of a member of $\mathrm{SSy}(M)$ with a computable set, hence computable in a member of $\mathrm{SSy}(M)$, and in $\mathrm{SSy}(M)$ by :ref{#thm-ssy-turing-ideal}.

If $M$ satisfies the theory of $\nat$, then $M \models \mathrm{PA}$, and a $\Sigma^*_n$ sentence holds in $M$ if and only if it holds in $\nat$. Let $X$ be $\Sigma^0_n$. By :ref{#thm-definable-arithmetic}, it is defined in $\nat$ by a $\Sigma_n$ formula, which :ref{#lem-variable-bounds} turns into a $\Sigma^*_n$ formula $\varphi(v_0)$ equivalent to it in $\nat$. Then $m \in X$ if and only if the $\Sigma^*_n$ sentence $\exists v_0\, (v_0 = \bar m \wedge \varphi(v_0))$ is true, and its code is computable from $m$. So $X$ is computable in a member of $\mathrm{SSy}(M)$. Every arithmetic set is $\Sigma^0_n$ for some $n$.
:::
::::

::::exercise{#ex-scott-separation difficulty=2}
Give a second proof that $\mathrm{SSy}(M)$ is a Scott set, for $M$ non-standard, using :ref{#lem-cut-separation} instead of :ref{#thm-scott-wkl-cut}. (Use the relativization of :ref{#thm-dnc2-no-computable} and of :ref{#thm-pa-characterization}: a $\{0, 1\}$-valued function that differs from $\Phi^X_e(e)$ whenever this converges computes an infinite path of every infinite binary tree computable in $X$.)

:::solution
Let $T \in \mathrm{SSy}(M)$ be an infinite binary tree. The sets $A_0 = \{ e : \Phi^T_e(e)\converge = 0 \}$ and $A_1 = \{ e : \Phi^T_e(e)\converge = 1 \}$ are disjoint and c.e. in $T$, so they are defined in $(\nat, \mathrm{SSy}(M))$ by $\Sigma^0_1$ formulas with the parameter $T$. By :ref{#lem-cut-separation}, some $C \in \mathrm{SSy}(M)$ contains $A_0$ and is disjoint from $A_1$. Its characteristic function is $\{0, 1\}$-valued and differs from $\Phi^T_e(e)$ whenever this converges; by the relativized characterization of PA degrees, $C$ computes an infinite path of $T$, which belongs to $\mathrm{SSy}(M)$ by :ref{#thm-ssy-turing-ideal}.
:::
::::

## Notes and references

Scott (1962) proved :ref{#thm-scott-converse} for the sets representable in complete extensions of arithmetic; Hájek and Pudlák (bibliographical remarks to Chapter IV) recount that Friedman (1973) introduced the standard system $\mathrm{SSy}(M)$, and that the countable standard systems are exactly the countable Scott sets (Scott algebras, in their terminology); Scott himself studied the sets binumerable in a complete extension of $\mathrm{PA}$, the traces on $\nat$ of the sets definable without parameters. Wong's Lecture 4 proves a related theorem for countable models of $\mathsf{WKL}_0$ by the arithmetized completeness theorem (Scott; Tanaka), which belongs to the next course of the track. Tennenbaum's theorem was announced in an abstract (1959), for models of $\mathrm{PA}$; Kaye's book gives a proof for both addition and multiplication. Shepherdson's computable non-standard model of open induction (1964) is an integer part of a real closed field.

- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in Recursive Function Theory, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, bibliographical remarks to Chapter IV.
- J. Knight and M. Nadel, *Models of arithmetic and closed ideals*, Journal of Symbolic Logic 47 (1982), 833–840.
- V. Gitman, *Scott's problem for proper Scott sets*, Journal of Symbolic Logic 73 (2008), 845–860.
- S. Tennenbaum, *Non-archimedean models for arithmetic*, Notices of the American Mathematical Society 6 (1959), 270.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
- J. C. Shepherdson, *A non-standard model for a free variable fragment of number theory*, Bulletin de l'Académie Polonaise des Sciences, Série des Sciences Mathématiques, Astronomiques et Physiques 12 (1964), 79–86.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 4.
