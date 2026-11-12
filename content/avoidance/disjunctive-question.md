---
title: Strong cone avoidance and disjunctive questions
summary: Strong cone avoidance of cohesiveness, with reservoirs that only avoid the cone; disjunctive notions of forcing, which build one set on each side of an instance, and their forcing questions; the abstract disjunctive cone avoidance lemma and Lachlan's disjunction; the Dzhafarov–Jockusch forcing as an example.
duration: 45
prerequisites: [forcing-question-method, ramsey-theorem/cone-avoidance]
---

Strong cone avoidance quantifies over arbitrary instances, so the reservoirs of a Mathias-type construction can no longer be kept simple: intersecting a reservoir with an arbitrary set produces an arbitrary set. This lesson shows the two devices that handle arbitrary instances. The first keeps in the reservoirs only the property that is being preserved, as in the proof that cohesiveness admits strong cone avoidance. The second handles problems whose solutions lie on one of several sides: it builds one set on each side, and uses a **disjunctive forcing question**, whose answers yield progress on one side without control on which. The next lesson applies it to Ramsey's theorem for pairs.

As in the previous lesson, a set $Z$ is fixed and the sentences are built with functionals of the oracle $Z \oplus G$.

## Strong cone avoidance of cohesiveness

The first application uses the class $\mathcal M$ of :ref{#def-question-local} in an essential way: the reservoirs are only required to avoid the cone, and their complexity is otherwise arbitrary. Recall that a set $G$ is cohesive for a sequence $\vec R = (R_n)$ if it is infinite and, for each $n$, $G \subseteq^* R_n$ or $G \subseteq^* \overline{R_n}$ (:ref{#def-cohesive}).

:::theorem[Wang]{#thm-coh-strong-cone}
$\mathsf{COH}$ admits strong cone avoidance: for every set $Z$, every $C \not\leq_T Z$ and every sequence of sets $\vec R$, there is an $\vec R$-cohesive set $G$ with $C \not\leq_T Z \oplus G$.
:::

:::proof{of=thm-coh-strong-cone}
*The notion of forcing.* The conditions are the Mathias conditions $(\sigma, X)$ (:ref{#def-mathias-condition}) such that $C \not\leq_T Z \oplus X$, with the order and members of :ref{#ex-forcing-notions}, item 4. Refinement holds as for computable Mathias forcing, since removing finitely many elements from a reservoir does not change its degree. Let $\mathcal M = \{ Z \oplus X : C \not\leq_T Z \oplus X \}$.

*The question.* For a $\Sigma^0_1$ sentence $\varphi$, let $(\sigma, X) \mathrel{?{\vdash}} \varphi$ if some string $\tau$ compatible with $(\sigma, X)$ satisfies $\varphi$, that is, makes the computation converge with oracle $Z \oplus \tau$. The proof of :ref{#prop-mathias-question} shows that this is a forcing question; it does not use the computability of $X$. Compatibility with $(\sigma, X)$ is decidable in $X$, so the relation is $\Sigma^0_1(Z \oplus X)$ with $Z \oplus X \in \mathcal M$. By :ref{#thm-local-cone-avoidance}, every sufficiently generic $G$ satisfies $C \not\leq_T Z \oplus G$.

*Cohesiveness.* Fix $n$ and a condition $(\sigma, X)$. Let $p$ be the enumeration of $X$ in increasing order, and $A = \{ k : p(k) \in R_n \}$. By the Dzhafarov–Jockusch theorem (:ref{#thm-dj-cone-avoidance}) relative to $Z \oplus X$, there is an infinite set $H$, contained in $A$ or in $\overline A$, with $C \not\leq_T Z \oplus X \oplus H$. The set $Y = p[H]$ is an infinite subset of $X$, contained in $R_n$ or in $\overline{R_n}$, and computable in $X \oplus H$; so $C \not\leq_T Z \oplus Y$, and $(\sigma, Y)$ is a condition extending $(\sigma, X)$. All its members $G$ satisfy $G \subseteq^* R_n$ or $G \subseteq^* \overline{R_n}$. So the set of conditions with this property is dense, for each $n$.

*Infinity.* Given $(\sigma, X)$ and $k$, adding to $\sigma$ an element of $X$ above $k$, and removing from $X$ the numbers up to it, gives an extension all of whose members have an element above $k$.

A set generic for all these dense sets is infinite, $\vec R$-cohesive, and does not compute $C$ together with $Z$.
:::

Strong cone avoidance of cohesiveness contrasts with :ref{#thm-coh-cone-avoidance}, where the sequence is computable in $Z$ and the reservoirs can be kept computable in $Z$. Here the sets $R_n$ are arbitrary, so their intersections with a reservoir are not simple, and the reservoirs are only required to satisfy the property that is being preserved. The step that shrinks a reservoir is an instance of the pigeonhole principle, applied to an arbitrary set: strong cone avoidance of $\mathsf{COH}$ is inherited from strong cone avoidance of $\mathsf{RT}^1_2$. This is the general pattern for Mathias-type notions: the reservoirs are taken in a class defined by the weakness property, and the operations on reservoirs must preserve that class.

:::quiz[strong cone avoidance of cohesiveness]
Why can the reservoir $X \cap R_n$, or $X \setminus R_n$, not be used directly as the new reservoir in the proof of :ref{#thm-coh-strong-cone}?

- [x] Because $R_n$ is arbitrary, so these sets may compute $C$ together with $Z$, and the new condition would not be a condition.
- [ ] Because neither of them is infinite.

  One of them is infinite.
- [ ] Because the question would no longer be a forcing question.

  The question is a forcing question for every Mathias condition; the issue is the class $\mathcal M$.
:::

## Disjunctive notions of forcing

For Ramsey-type problems, a solution must be found on one of several sides, and one cannot know in advance which side will allow a weak solution. The proof of the Dzhafarov–Jockusch theorem (:ref{#thm-dj-cone-avoidance}) builds one set on each side and satisfies, for every pair of indices, a disjunction of two requirements; Lachlan's disjunction (:ref{to="ramsey-theorem/cone-avoidance"}) then says that one of the two sets satisfies all its requirements. The disjunctive notions of forcing build pairs of sets by decreasing sequences of conditions. We only need the following structure.

:::definition{#def-disjunctive-notion}
A **disjunctive notion of forcing** consists of a set of conditions with a preorder $\leq$, and, for each condition $c$ and each $i < 2$, a non-empty closed class $[c]_i \subseteq \cs$, the **members of side $i$**, such that $d \leq c$ implies $[d]_i \subseteq [c]_i$. For a sentence $\varphi$ of level $1$ about a set $G$, a condition $c$ **forces $\varphi(G_i)$**, written $c \Vdash \varphi(G_i)$, if every member of side $i$ of $c$ satisfies $\varphi$.

A **disjunctive forcing question** is a relation $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ between conditions and pairs of $\Sigma^0_1$ sentences such that:

1. if $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, there are $d \leq c$ and $i < 2$ with $d \Vdash \varphi_i(G_i)$;
2. if $c \mathrel{?{\nvdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, there are $d \leq c$ and $i < 2$ with $d \Vdash \neg \varphi_i(G_i)$.

It is **$\Sigma^0_1(\mathcal M)$-preserving** if for every condition $c$ there is $X \in \mathcal M$ such that for all $\Sigma^0_1$ formulas $\varphi_0(\vec x)$ and $\varphi_1(\vec x)$, the relation $\{ \vec m : c \mathrel{?{\vdash}} \varphi_0(\vec m)(G_0) \vee \varphi_1(\vec m)(G_1) \}$ is $\Sigma^0_1(X)$.
:::

In both properties, the side $i$ is not under control: a positive answer yields one of the two sentences on its side, a negative answer the negation of one of them, on its side. This is all that disjunctive requirements need.

:::lemma{#lem-disjunctive-cone}
Let a disjunctive notion of forcing have a $\Sigma^0_1(\mathcal M)$-preserving disjunctive forcing question, and let $C$ be computable in no member of $\mathcal M$. For every condition $c$ and all $e_0, e_1$, there are $d \leq c$, $i < 2$ and $x$ such that $d \Vdash \Phi^{Z \oplus G_i}_{e_i}(x)\converge = 1 - C(x)$ or $d \Vdash \neg (\Phi^{Z \oplus G_i}_{e_i}(x)\converge = C(x))$. In either case, every member $G$ of side $i$ of $d$ satisfies $\Phi^{Z \oplus G}_{e_i} \neq C$.
:::

:::proof{of=lem-disjunctive-cone}
Let $X \in \mathcal M$ be given for $c$, and let $U$ be the set of pairs $(x, v) \in \nat \times \{ 0, 1 \}$ such that $c \mathrel{?{\vdash}} (\Phi^{Z \oplus G}_{e_0}(x)\converge = v)(G_0) \vee (\Phi^{Z \oplus G}_{e_1}(x)\converge = v)(G_1)$. It is $\Sigma^0_1(X)$. If $(x, 1 - C(x)) \in U$ for some $x$, property 1 gives the first alternative; if $(x, C(x)) \notin U$ for some $x$, property 2 gives the second. Otherwise $U$ is the graph of $C$, and $C \leq_T X$, which is excluded.
:::

This is the three-case argument of :ref{#thm-local-cone-avoidance}, with one more unknown: the side. The lemma is used together with Lachlan's disjunction, in the following form.

:::lemma{#lem-disjunctive-construction}
Let $c_0 \geq c_1 \geq \cdots$ be a sequence of conditions of a disjunctive notion of forcing, and $G_0, G_1$ sets with $G_i \in [c_s]_i$ for all $s$ and $i$. Suppose that for every pair $(e_0, e_1)$ there are $s$ and $i$ such that every member $G$ of side $i$ of $c_s$ satisfies $\Phi^{Z \oplus G}_{e_i} \neq C$. Then $C \not\leq_T Z \oplus G_0$ or $C \not\leq_T Z \oplus G_1$.
:::

:::proof{of=lem-disjunctive-construction}
For every pair $(e_0, e_1)$, $\Phi^{Z \oplus G_0}_{e_0} \neq C$ or $\Phi^{Z \oplus G_1}_{e_1} \neq C$, since $G_i$ is a member of side $i$ of every $c_s$. If $\Phi^{Z \oplus G_0}_{e_0} = C$ for some $e_0$, then $\Phi^{Z \oplus G_1}_{e_1} \neq C$ for every $e_1$, so $C \not\leq_T Z \oplus G_1$. Otherwise $C \not\leq_T Z \oplus G_0$.
:::

:::quiz[disjunctive questions]
In property 2 of :ref{#def-disjunctive-notion}, why is the extension only required to force the negation of **one** of the two sentences?

- [x] Because a negative answer typically comes from a partition of the reservoir, and shrinking the reservoir to one side of the partition controls only the stem on that side.
- [ ] Because forcing both negations is never possible.

  It is possible in some cases, for instance when the condition itself forces both; it is just not required.
- [ ] Because the requirements of the construction are conjunctions.

  They are disjunctions: one failing side suffices.

---

In the proof of :ref{#lem-disjunctive-construction}, why is it essential that the hypothesis holds for **every pair** $(e_0, e_1)$?

- [x] Because if $\Phi_{e_0}$ computes $C$ from $Z \oplus G_0$, the pairs $(e_0, e_1)$ for all $e_1$ show that no $\Phi_{e_1}$ computes $C$ from $Z \oplus G_1$; pairs with a fixed first index would not cover all $e_1$.
- [ ] Because the side $i$ must be the same for all pairs.

  The side may depend on the pair; this is the point of Lachlan's disjunction.
- [ ] Because $C$ is not computable.

  The non-computability of $C$ is used in :ref{#lem-disjunctive-cone}, not here.
:::

The forcing of Dzhafarov and Jockusch fits this frame. Its conditions are the triples $(\sigma_0, \sigma_1, X)$ of the proof of :ref{#thm-dj-cone-avoidance}, the members of side $i$ are the members of the Mathias condition $(\sigma_i, X)$, and the relation "$c$ answers $(x, v)$" of that proof is the instance, for the sentences $\Phi^{Z \oplus G}_{e_i}(x)\converge = v$, of the disjunctive question: $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if for every partition $\nat = U^0 \sqcup U^1$ there are $i < 2$ and a string $\tau$ compatible with $(\sigma_i, X \cap U^i)$ satisfying $\varphi_i$. The three cases of that proof are the proof of :ref{#lem-disjunctive-cone}, with $\mathcal M$ a Scott ideal not containing $C$.

## Exercises

::::exercise{difficulty=2}
Let $A$ be a set. Define a disjunctive notion of forcing for the pigeonhole principle with conditions $(\sigma_0, \sigma_1, X)$, $X \in \mathcal M$ infinite, $\sigma_i \subseteq A^i$ where $A^0 = A$ and $A^1 = \overline A$, the members of side $i$ being those of the Mathias condition $(\sigma_i, X)$. Show that the question of the Dzhafarov–Jockusch proof is a $\Sigma^0_1(\mathcal M)$-preserving disjunctive forcing question, and that :ref{#lem-disjunctive-cone} and :ref{#lem-disjunctive-construction} give :ref{#thm-dj-cone-avoidance}.

:::solution
Let $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if for every set $B$, with $B^0 = B$ and $B^1 = \nat \setminus B$, there are $i < 2$ and a string $\tau$ compatible with $(\sigma_i, X \cap B^i)$ satisfying $\varphi_i$.

*Preservation.* The set of strings $\beta$ (partial partitions) for which no such $i$ and $\tau$ with $|\tau| \leq |\beta|$ and convergence in $|\beta|$ steps exist is a tree computable in $X \oplus Z$, whose paths are the sets $B$ for which the definition fails. The answer is positive if and only if this tree is finite, a $\Sigma^0_1(X \oplus Z)$ property, and $X \oplus Z \in \mathcal M$ when $\mathcal M$ is a Scott ideal containing $Z$.

*Property 1.* Apply the definition to $B = A$. The witness $\tau$ has its new elements in $X \cap A^i$, so replacing $\sigma_i$ by $\tau$ and $X$ by $X \setminus [0, |\tau|)$ gives a condition, all of whose members of side $i$ extend $\tau$ and satisfy $\varphi_i$.

*Property 2.* The tree has a path in $\mathcal M$; for some $i$, $Y = X \cap B^i$ is infinite, and $(\sigma_0, \sigma_1, Y)$ is a condition. A member of side $i$ satisfying $\varphi_i$ would have a prefix compatible with $(\sigma_i, X \cap B^i)$ satisfying $\varphi_i$, contradicting the choice of $B$.

Under the assumption that no infinite subset of $A$ or $\overline A$ lies in $\mathcal M$, both sides can be extended, as in the proof of :ref{#thm-dj-cone-avoidance}. A sequence of conditions handling infinity and all pairs $(e_0, e_1)$ through :ref{#lem-disjunctive-cone} gives, by :ref{#lem-disjunctive-construction}, an infinite subset of $A$ or of $\overline A$ that does not compute $C$ together with $Z$.
:::
::::

::::exercise{difficulty=1}
Let $C_0$ and $C_1$ be Turing incomparable sets. Find sets $G_0, G_1$ such that for every pair $(e_0, e_1)$ and every $j < 2$, $\Phi^{G_0}_{e_0} \neq C_j$ or $\Phi^{G_1}_{e_1} \neq C_j$, while neither $G_0$ nor $G_1$ avoids both cones. What does this say about disjunctive constructions with several cones?

:::solution
Let $G_0 = C_1$ and $G_1 = C_0$. For $j = 0$, $\Phi^{G_0}_{e_0} \neq C_0$ for every $e_0$, since $C_1$ does not compute $C_0$; for $j = 1$, $\Phi^{G_1}_{e_1} \neq C_1$ for every $e_1$. But $G_0$ computes $C_1$ and $G_1$ computes $C_0$. Lachlan's disjunction, applied separately to each cone, gives a side avoiding $C_0$ and a side avoiding $C_1$, possibly different. A disjunctive construction therefore avoids one cone at a time. That cone avoidance for one set implies cone avoidance for countably many sets at once is a theorem of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky, whose proof uses a different argument.
:::
::::

## Notes and references

Strong cone avoidance of $\mathsf{COH}$ is due to Wang (2014); the proof through Mathias conditions whose reservoirs avoid the cone, using strong cone avoidance of the pigeonhole principle for the density of cohesiveness, follows an exercise of the chapter *Cone avoidance* of Patey's monograph (section *Seetapun's theorem*), which also defines disjunctive forcing questions. Lachlan's disjunction is Lemma 8.3.7 of Dzhafarov and Mummert, and 2-fold Mathias forcing is their Definition 8.3.5. The theorem that avoidance of one cone implies avoidance of countably many cones is Corollary 2.4 of Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022).

- W. Wang, *Some logically weak Ramseyan theorems*, Advances in Mathematics 261 (2014), 1–25.
- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 8.3.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, section *Seetapun's theorem*.
