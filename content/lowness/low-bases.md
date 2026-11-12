---
title: Low bases for problems
summary: A problem admits a low basis if every instance has a solution that is low relative to the instance; such problems have ω-models consisting of low sets, which separates them from the jump, from cohesiveness and from Ramsey's theorem for pairs; low solutions also control the second jump.
duration: 40
prerequisites: [avoidance/avoidance-properties, effective-forcing/mathias-forcing, reducibilities/preservation, ramsey-theorem/cohesiveness, ramsey-theorem/triples, turing-degrees/low-and-high, arithmetic-hierarchy/post-theorem]
---

The previous course studied cone avoidance and its variants. These are **genericity properties**: they hold for every sufficiently generic set of a suitable notion of forcing, and their proofs never require the construction to be effective. A cone-avoiding solution is one of uncountably many, and the proof gives no description of it. This course studies the opposite kind of property, **effectiveness properties**, which require the solution to be built by a construction of bounded complexity. The main example is lowness: a set $Y$ is low if $Y' \leq_T \emptyset'$ (:ref{#def-low}). There are only countably many low sets, so a low solution is never obtained by mere genericity; the construction itself must be carried out with the oracle $\emptyset'$.

Effectiveness properties are harder to establish than genericity properties, since the dense sets of the construction must be met by an effective procedure, and conditions must be represented by finite codes. In return they say more about a problem. A low solution is a solution whose jump is no more complex than that of a computable set; from the point of view of the arithmetic hierarchy above the first level, it is invisible. This lesson defines low bases for problems, shows how they give ω-models and separations, and explains what lowness says about the second jump. The next lessons develop the method to obtain them.

## Low bases

Recall that a problem $\mathsf P$ is a class of instances, each with a class of solutions (:ref{#def-problem}).

:::definition{#def-low-basis-problem}
A problem $\mathsf P$ **admits a low basis** if for every set $Z$ and every $Z$-computable instance $X$ of $\mathsf P$, there is a solution $Y$ to $X$ with $(Y \oplus Z)' \leq_T Z'$. Such a $Y$ is said to be **low relative to $Z$**, or **low over $Z$**.
:::

The definition is relativized, as for cone avoidance (:ref{#def-cone-avoidance-problem}). For $Z = \emptyset$, it says that every computable instance has a low solution. Dzhafarov and Mummert say that $\mathsf P$ **admits low solutions** (their Definition 3.6.2). Lowness relative to $Z$ is not the same as lowness of $Y$: the condition $(Y \oplus Z)' \leq_T Z'$ concerns the join, and implies that $Y$ is low only when $Z$ is.

:::example{#ex-low-basis-problems}
1. **$\mathsf{WKL}$** admits a low basis: this is the low basis theorem (:ref{#thm-low-basis}) relativized to $Z$, applied to the class of paths of a $Z$-computable infinite binary tree.
2. **$\mathsf{RT}^1_2$** admits a low basis: a $Z$-computable set $A$ or its complement is an infinite $Z$-computable solution $Y$, and $(Y \oplus Z)' \equiv_T Z'$.
3. **The jump $\mathsf J$** does not: the computable instance $\emptyset$ has the only solution $\emptyset'$, which is not low (:ref{#prop-low-basic}).
4. **$\mathsf{COH}$** does not: some computable sequence of sets has no low cohesive set (:ref{#prop-coh-no-low}).
5. **$\mathsf{RT}^2_2$** does not: some computable coloring of pairs has no infinite $\Delta^0_2$ homogeneous set (:ref{#thm-jockusch-no-delta2}), and low sets are $\Delta^0_2$.
6. **$\mathsf D^2_2$** (:ref{#def-d22}) does not, although every computable instance has a $\Delta^0_2$ solution: by a theorem of Downey, Hirschfeldt, Lempp and Solomon, admitted in the last lesson, some $\Delta^0_2$ set has no infinite low subset of itself or of its complement.
:::

Items 4–6 show that the property is not about growth or coding: $\mathsf{COH}$ and $\mathsf{RT}^2_2$ admit cone avoidance, and even strong cone avoidance for $\mathsf{COH}$ (:ref{to="avoidance/disjunctive-question"}). Lowness and cone avoidance are independent properties of problems. The rest of the course shows that $\mathsf{COH}$, $\mathsf D^2_2$ and $\mathsf{RT}^2_2$ nevertheless admit a weakening of low bases, with solutions whose jump is computed by any set PA relative to $\emptyset'$.

## Models of low sets

The relativized definition is what makes low bases iterate. The class of low sets is closed downward under Turing reducibility, but not under joins: there are low sets $A$ and $B$ with $A \oplus B \equiv_T \emptyset'$ (see :ref{to="turing-degrees/low-and-high"}). Adding to a low set $Z$ a solution $Y$ that is low but not low over $Z$ may thus lead out of the low sets. Lowness over $Z$ prevents this: if $(Y \oplus Z)' \leq_T Z'$ and $Z' \leq_T \emptyset'$, then $Z \oplus Y$ is low.

:::theorem{#thm-low-basis-model}
Let $\mathsf P$ be a problem that admits a low basis. For every low set $Z$, there is a Turing ideal containing $Z$, satisfying $\mathsf P$, all of whose members are low.
:::

:::proof{of=thm-low-basis-model}
Let $\mathcal W$ be the class of low sets. It is a weakness property in the sense of :ref{#def-weakness}, since it is closed downward under Turing reducibility (:ref{#prop-low-basic}). The problem $\mathsf P$ preserves $\mathcal W$: let $Z \in \mathcal W$ and let $X \leq_T Z$ be an instance. By the low basis for $\mathsf P$, $X$ has a solution $Y$ with $(Y \oplus Z)' \leq_T Z' \leq_T \emptyset'$, so $Z \oplus Y \in \mathcal W$. By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ containing $Z$ and satisfying $\mathsf P$.
:::

For $\mathsf P = \mathsf{WKL}$, this is :ref{#thm-low-scott}. When $\mathsf P$ is a $\Pi^1_2$ statement of second-order arithmetic, read as a problem, the ideal is an ω-model of $\mathsf{RCA}_0 + \mathsf P$ consisting of low sets, and in particular of $\Delta^0_2$ sets.

:::quiz[models of low sets]
In the proof of :ref{#thm-low-basis-model}, why would it not suffice that every $Z$-computable instance has a low solution $Y$?

- [x] Because the set added to the ideal is $Z \oplus Y$, and the join of two low sets need not be low; lowness of $Y$ over $Z$ is what makes $Z \oplus Y$ low.
- [ ] Because $Y$ must compute $Z$.

  $Y$ need not compute $Z$; the ideal contains $Z \oplus Y$, which computes both.
- [ ] Because the ideal must be closed under the jump.

  It is not, and cannot be, since $\emptyset'$ is not low.

---

Where is the hypothesis that $Z$ is low used?

- [x] To start the construction inside the class $\mathcal W$ of low sets; lowness of every later set then follows from $(Y \oplus Z)' \leq_T Z' \leq_T \emptyset'$.
- [ ] To ensure that the instances of $\mathsf P$ in the ideal are computable.

  They are computable in members of the ideal, not computable.
- [ ] To apply the low basis theorem.

  The low basis of $\mathsf P$ is used, relativized to members of the ideal; it holds for every $Z$.
:::

:::corollary{#cor-low-basis-separations}
Let $\mathsf P$ be a problem that admits a low basis. Then $\mathsf J$, $\mathsf{COH}$ and $\mathsf{RT}^2_2$ are not ω-reducible to $\mathsf P$. In particular, if $\mathsf P$ is a $\Pi^1_2$ statement, then $\mathsf{RCA}_0 + \mathsf P$ proves neither $\mathsf{ACA}_0$, nor $\mathsf{COH}$, nor $\mathsf{RT}^2_2$.
:::

:::proof{of=cor-low-basis-separations}
By the proof of :ref{#thm-low-basis-model}, $\mathsf P$ preserves the class $\mathcal W$ of low sets. Each of the three problems has a computable instance, hence an instance computable in $\emptyset \in \mathcal W$, with no low solution, by items 3–5 of :ref{#ex-low-basis-problems}; so none of them preserves $\mathcal W$. Apply :ref{#thm-preservation-separation}. For the second statement, the ideal of :ref{#thm-low-basis-model} with $Z = \emptyset$ is an ω-model of $\mathsf{RCA}_0 + \mathsf P$ that contains the computable instances and none of their solutions.
:::

The separation from $\mathsf{RT}^2_2$ is the reason why low bases are useful in the study of Ramsey-type theorems: a problem with a low basis is strictly weaker than $\mathsf{RT}^2_2$ in ω-models, and the same holds for any problem of which some computable instance has no $\Delta^0_2$ solution, such as the chain-antichain principle (Herrmann, 2001). Cone avoidance gives only the separation from $\mathsf{ACA}_0$.

The definition uses lowness rather than the weaker property of being $\Delta^0_2$. The reason is that $\Delta^0_2$ solutions do not iterate. The jump $\mathsf J$ has $\Delta^0_2$ solutions relative to its instances: $X'$ is $\Delta^0_2(X)$. But a Turing ideal satisfying $\mathsf J$ contains $\emptyset'$, then $\emptyset''$, and so on: all arithmetic sets. A set $\Delta^0_2$ relative to a $\Delta^0_2$ set is $\Delta^0_3$, not $\Delta^0_2$; a set low relative to a low set is low.

## Lowness and the second jump

A low set does not add anything to the arithmetic hierarchy from the second level on.

:::proposition{#prop-low-second-jump}
Let $Z$ be a set, and $Y$ a set with $(Y \oplus Z)' \leq_T Z'$. For every $n \geq 2$, every $\Sigma^0_n(Y \oplus Z)$ set is $\Sigma^0_n(Z)$. In particular, if $Y$ is low, every $\Sigma^0_n(Y)$ set is $\Sigma^0_n$ for $n \geq 2$.
:::

:::proof{of=prop-low-second-jump}
By Post's theorem relativized (:ref{#thm-post}), a set is $\Sigma^0_n(W)$ if and only if it is $\Sigma^0_{n-1}(W')$, for $n \geq 2$ and every $W$. The class $\Sigma^0_{n-1}(W')$ depends only on the Turing degree of $W'$, and is monotone in it. Since $Z' \leq_T (Y \oplus Z)' \leq_T Z'$, the sets $(Y \oplus Z)'$ and $Z'$ have the same degree, so $\Sigma^0_{n-1}((Y \oplus Z)') = \Sigma^0_{n-1}(Z')$, that is, $\Sigma^0_n(Y \oplus Z) = \Sigma^0_n(Z)$.
:::

Consequently, a problem that admits a low basis has every preservation property of the second and higher levels. For instance, for every $Z$ and every set $C$ that is not $\Sigma^0_2(Z)$, every $Z$-computable instance has a solution $Y$ such that $C$ is not $\Sigma^0_2(Y \oplus Z)$; and if $C \not\leq_T Z'$, then $C \not\leq_T (Y \oplus Z)'$. Properties of this kind, which control the jump of the solution rather than the solution itself, are the subject of the later course on jump cone avoidance; when a problem admits a low basis, they come for free. This is a second reason to prefer a low basis when one exists: controlling the second jump of a generic set directly is much harder than controlling the first one, as the highness of Mathias generic sets shows (:ref{#prop-mathias-dominant}).

:::quiz[the second jump]
In the proof of :ref{#prop-low-second-jump}, why does the conclusion fail for $n = 1$?

- [x] Because Post's theorem expresses $\Sigma^0_1(Y \oplus Z)$ through the oracle $Y \oplus Z$ itself, not through its jump; a low set $Y$ can have $\Sigma^0_1(Y)$ sets that are not $\Sigma^0_1$, for instance $Y$ itself when $Y$ is not c.e.
- [ ] Because low sets are not $\Sigma^0_1$.

  Some are, for instance the computable sets and the low c.e. sets.
- [ ] Because the jump of $Y \oplus Z$ is not computable in $Z'$.

  It is, by hypothesis; the issue is at the level of $Y \oplus Z$ itself.
:::

## Exercises

::::exercise{difficulty=1}
Let $\mathsf Q$ be the problem whose instances are all sets $X$, where the only solution to a computable $X$ is $\emptyset$, and the only solution to a non-computable $X$ is $X'$. Show that every computable instance of $\mathsf Q$ has a low solution, but that $\mathsf Q$ does not admit a low basis.

:::solution
A computable instance has the solution $\emptyset$, which is low. Let $Z$ be a non-computable low set, for instance a 1-generic set computable in $\emptyset'$ (:ref{#cor-low-exists}). The instance $Z$ is $Z$-computable, and its only solution is $Y = Z'$. Then $(Y \oplus Z)' \equiv_T Z'' \equiv_T \emptyset''$, while $Z' \equiv_T \emptyset'$, and $\emptyset'' \not\leq_T \emptyset'$. So $Z$ has no solution low over $Z$. The example shows that the unrelativized property is not enough for :ref{#thm-low-basis-model}: the ideal must contain $Z$, and then a solution to the instance $Z$.
:::
::::

::::exercise{difficulty=1}
Let $\mathsf P$ admit a low basis, let $Z$ be a set and $C$ a set with $C \not\leq_T Z'$. Show that every $Z$-computable instance of $\mathsf P$ has a solution $Y$ such that $C$ is not $\Delta^0_2(Y \oplus Z)$.

:::solution
Let $Y$ be a solution with $(Y \oplus Z)' \leq_T Z'$. If $C$ were $\Delta^0_2(Y \oplus Z)$, it would be computable in $(Y \oplus Z)'$ by Post's theorem relativized, hence in $Z'$, a contradiction.
:::
::::

::::exercise{difficulty=2}
Show that every Turing ideal containing $\emptyset$ and satisfying $\mathsf J$ contains every arithmetic set, although every $Z$-computable instance of $\mathsf J$ has a $\Delta^0_2(Z)$ solution. Why does the proof of :ref{#thm-low-basis-model} fail for the class of $\Delta^0_2$ sets?

:::solution
A Turing ideal satisfying $\mathsf J$ that contains $X$ contains $X'$, the only solution to the instance $X$. By induction it contains $\emptyset^{(n)}$ for every $n$, hence every arithmetic set, by Post's theorem. Every $Z$-computable instance $X$ has the solution $X' \leq_T Z'$, which is $\Delta^0_2(Z)$. The class of $\Delta^0_2$ sets is a weakness property, but $\mathsf J$ does not preserve it: for $Z = \emptyset'$, which is $\Delta^0_2$, the instance $\emptyset'$ has the solution $\emptyset''$, and $\emptyset' \oplus \emptyset''$ is not $\Delta^0_2$. A $\Delta^0_2(Z)$ solution of a $\Delta^0_2$ set $Z$ is only $\Delta^0_3$, while a solution low over a low set is low.
:::
::::

## Notes and references

The distinction between genericity and effectiveness properties, the definition of a low basis for problems, and the remarks on models of low sets and on the second jump follow the section *Motivation* of the chapter *Lowness* of Patey's monograph *Lowness and avoidance*. Dzhafarov and Mummert define problems that admit or omit low solutions in Definition 3.6.2; Hirschfeldt builds ω-models from basis theorems in Proposition 4.27. The low basis theorem is due to Jockusch and Soare (1972). The theorem of Downey, Hirschfeldt, Lempp and Solomon is Theorem 6.37 of Hirschfeldt. Herrmann (2001) built a computable partial order with no infinite $\Delta^0_2$ chain or antichain.

- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- R. Downey, D. R. Hirschfeldt, S. Lempp and R. Solomon, *A Δ⁰₂ set with no infinite low subset in either it or its complement*, Journal of Symbolic Logic 66 (2001), 1371–1381.
- E. Herrmann, *Infinite chains and antichains in computable partial orderings*, Journal of Symbolic Logic 66 (2001), 923–934.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 4.5 and 6.4.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 3.6.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, section *Motivation*.
