---
title: Avoidance properties of problems
summary: Cone avoidance and strong cone avoidance as properties of problems; their relation to preservation and to ω-models; examples and counterexamples among WKL, COH, the pigeonhole principle and Ramsey's theorem; why the definitions are relativized.
duration: 45
prerequisites: [reducibilities/preservation, ramsey-theorem/seetapun, pi01-classes/basis-theorems]
---

The computability-theoretic study of a problem $\mathsf P$ (:ref{#def-problem}) asks how complex the solutions of its computable instances must be. Lower bounds are instances all of whose solutions are complex: every infinite path of some computable binary tree is PA, every infinite homogeneous set of some computable coloring of triples computes $\emptyset'$ (:ref{#prop-rt32-jump}). Upper bounds say that every computable instance has a weak solution. The weakest form of strength a problem can have is the ability to **encode** a set: to have a computable instance all of whose solutions compute a fixed non-computable set $C$. A problem that cannot do this for any $C$ admits **cone avoidance**.

This course studies cone avoidance and the related **avoidance properties** systematically. This first lesson fixes the definitions, relates them to preservation of weakness properties, and collects the examples proved in earlier courses. The next lessons develop the method that proves such properties, the **forcing question**, and apply it to Ramsey's theorem for pairs, to the preservation of non-$\Sigma^0_1$ definitions and to the preservation of hyperimmunities.

## Cone avoidance

For a set $C$, the **cone above $C$** is the class of sets that compute $C$. A set **avoids** the cone above $C$ if it does not compute $C$.

:::definition{#def-cone-avoidance-problem}
Let $\mathsf P$ be a problem.

1. $\mathsf P$ admits **cone avoidance** if for every set $Z$, every set $C$ with $C \not\leq_T Z$, and every instance $X \leq_T Z$ of $\mathsf P$, there is a solution $Y$ to $X$ with $C \not\leq_T Z \oplus Y$.
2. $\mathsf P$ admits **strong cone avoidance** if for every set $Z$, every set $C$ with $C \not\leq_T Z$, and **every** instance $X$ of $\mathsf P$, there is a solution $Y$ to $X$ with $C \not\leq_T Z \oplus Y$.
:::

The set $Z$ plays two roles. It bounds the instances: in cone avoidance, the instance must be computable in $Z$, while in strong cone avoidance it is arbitrary and $Z$ is only the oracle relative to which $C$ is non-computable. And the solution is required to avoid the cone together with $Z$: the condition is $C \not\leq_T Z \oplus Y$, not $C \not\leq_T Y$. For $Z = \emptyset$, cone avoidance says that a computable instance never forces all its solutions to compute a non-computable set. The general case is the same statement relative to $Z$; we return below to why it is needed.

The name "strong" refers to the instances, not to the solutions: strong cone avoidance asks for the same conclusion about more instances. Since every instance computable in $Z$ is an instance, strong cone avoidance implies cone avoidance. The difference measures how much of the strength of a problem comes from the complexity of its instances, its **computational** strength, and how much from its combinatorics, its **combinatorial** strength.

Cone avoidance is a preservation property in the sense of :ref{#def-weakness}. For a set $C$, the class $\mathcal W_C = \{ Z : C \not\leq_T Z \}$ is closed downwards under Turing reducibility, so it is a weakness property, and by definition:

:::proposition{#prop-cone-avoidance-preservation}
A problem $\mathsf P$ admits cone avoidance if and only if $\mathsf P$ preserves $\mathcal W_C$ for every set $C$.
:::

:::proof{of=prop-cone-avoidance-preservation}
Both statements say: for all $C$, all $Z$ with $C \not\leq_T Z$, that is $Z \in \mathcal W_C$, and every instance $X \leq_T Z$, there is a solution $Y$ with $Z \oplus Y \in \mathcal W_C$.
:::

The method of :ref{to="reducibilities/preservation"} then turns cone avoidance into ω-models and separations.

:::corollary{#cor-cone-avoidance-model}
Let $\mathsf P$ be a problem admitting cone avoidance.

1. For every non-computable set $C$, there is a Turing ideal satisfying $\mathsf P$ and not containing $C$.
2. If a problem $\mathsf Q$ has a computable instance all of whose solutions compute a fixed non-computable set, then $\mathsf Q \not\leq_\omega \mathsf P$.
:::

:::proof{of=cor-cone-avoidance-model}
1. Apply :ref{#lem-preservation-ideal} to the weakness property $\mathcal W_C$ and the set $\emptyset \in \mathcal W_C$.
2. Let $X$ be the instance and $C$ the set. Then $\emptyset \in \mathcal W_C$ and $X \leq_T \emptyset$, but $\emptyset \oplus Y \notin \mathcal W_C$ for every solution $Y$, so $\mathsf Q$ does not preserve $\mathcal W_C$, while $\mathsf P$ does. Apply :ref{#thm-preservation-separation}.
:::

For a problem coming from a $\Pi^1_2$ theorem, the first item gives an ω-model of $\mathsf{RCA}_0 + \mathsf P$ that is not a model of $\mathsf{ACA}_0$, by taking $C = \emptyset'$ (:ref{#cor-rt22-not-aca} is the case of Ramsey's theorem for pairs). Cone avoidance is the property behind most separations from $\mathsf{ACA}_0$ in reverse mathematics.

## Examples

:::example{#ex-cone-avoidance-problems}
The following table collects what earlier courses prove. The problems are those of :ref{to="reducibilities/omega-reducibility"}: $\mathsf{WKL}$ (infinite binary trees, paths), $\mathsf{COH}$ (sequences of sets, cohesive sets), $\mathsf{RT}^n_2$ (colorings of $[\nat]^n$ with two colors, infinite homogeneous sets), and $\mathsf J$ (sets, their jumps).

| problem | cone avoidance | strong cone avoidance |
| --- | --- | --- |
| $\mathsf{RT}^1_2$ | yes (trivial) | yes, Dzhafarov–Jockusch (:ref{#thm-dj-cone-avoidance}) |
| $\mathsf{WKL}$ | yes, Jockusch–Soare (:ref{#thm-cone-avoidance-basis}) | no |
| $\mathsf{COH}$ | yes (:ref{#thm-coh-cone-avoidance}) | yes, Wang (:ref{to="avoidance/strong-cone-avoidance"}) |
| $\mathsf{RT}^2_2$ | yes, Seetapun (:ref{#thm-seetapun}) | no |
| $\mathsf{RT}^3_2$ | no (:ref{#prop-rt32-jump}) | no |
| $\mathsf J$ | no | no |

The other entries are justified as follows.

1. **$\mathsf{RT}^1_2$.** A $Z$-computable set $A$ has a $Z$-computable solution, $A$ or $\overline A$, whichever is infinite; and $C \not\leq_T Z \oplus Y$ when $Y \leq_T Z$.
2. **$\mathsf{WKL}$.** The cone avoidance basis theorem relativized to $Z$ gives, for every infinite $Z$-computable binary tree, a path $Y$ with $C \not\leq_T Z \oplus Y$. Strong cone avoidance fails: for a non-computable set $C$, the tree $\{ C \uh n : n \in \nat \}$ is an infinite binary tree whose only path is $C$; take $Z = \emptyset$.
3. **$\mathsf{RT}^2_2$.** Strong cone avoidance fails: the coloring $h$ of the proof of :ref{#prop-rt32-jump} is a coloring of pairs, computable in $\emptyset'$, all of whose infinite homogeneous sets compute $\emptyset'$; take $Z = \emptyset$ and $C = \emptyset'$.
4. **$\mathsf J$.** The instance $\emptyset$ has the single solution $\emptyset'$.
:::

The two failures of strong cone avoidance are of different natures. For $\mathsf{WKL}$, the instance encodes $C$ in the simplest way: the tree is computable in $C$, and its only path is $C$. For $\mathsf{RT}^2_2$, the instance $h$ is computable in $\emptyset'$, and its homogeneous sets compute $\emptyset'$ by growth rather than by reading it: they must be sparse enough to dominate a modulus of $\emptyset'$. The second mechanism reappears in the last lesson, where avoiding a cone is compared with preserving the hyperimmunity of a function.

:::quiz[the table of examples]
Why does the tree $\{ C \uh n : n \in \nat \}$ not contradict cone avoidance for $\mathsf{WKL}$?

- [x] Because it is computable in $C$ but not in any $Z$ with $C \not\leq_T Z$, so cone avoidance says nothing about it; only strong cone avoidance quantifies over all instances.
- [ ] Because the tree is finite.

  It contains a string of every length, so it is infinite.
- [ ] Because $C$ is not a path through it.

  $C$ is its only path.

---

Why does the coloring $h$ of :ref{#prop-rt32-jump} not contradict Seetapun's theorem?

- [x] Because $h$ is not computable: the function $m$ of that proof is computable in $h$, so every $Z$ computing $h$ computes $\emptyset'$, and Seetapun's theorem says nothing about $h$ and the cone above $\emptyset'$.
- [ ] Because $h$ is a coloring of triples.

  $h$ is a coloring of pairs; the coloring of triples of :ref{#prop-rt32-jump} is built from it.
- [ ] Because $h$ has no infinite homogeneous set.

  Every coloring of pairs has infinite homogeneous sets, by Ramsey's theorem.
:::

## Why the definitions are relativized

Cone avoidance is applied repeatedly in the construction of an ω-model: at each step, the instance is computable in the sets $Z_n$ already built, and the new solution must avoid the cone together with $Z_n$. A property stated only for computable instances and for $Z = \emptyset$ cannot be iterated. The relativized form also gives closure properties. For two problems $\mathsf P_0$ and $\mathsf P_1$, let $\mathsf P_0 \times \mathsf P_1$ be the problem whose instances are the pairs $X_0 \oplus X_1$ of an instance of each, with solutions the pairs $Y_0 \oplus Y_1$ of solutions.

:::proposition{#prop-cone-avoidance-product}
If $\mathsf P_0$ and $\mathsf P_1$ admit cone avoidance, so does $\mathsf P_0 \times \mathsf P_1$. If $\mathsf P \leq_\omega \mathsf Q$ and $\mathsf Q$ admits cone avoidance, so does $\mathsf P$.
:::

:::proof{of=prop-cone-avoidance-product}
Let $C \not\leq_T Z$ and $X_0 \oplus X_1 \leq_T Z$. Cone avoidance of $\mathsf P_0$ gives a solution $Y_0$ to $X_0$ with $C \not\leq_T Z \oplus Y_0$. The instance $X_1$ is computable in $Z \oplus Y_0$, so cone avoidance of $\mathsf P_1$ **relative to $Z \oplus Y_0$** gives a solution $Y_1$ to $X_1$ with $C \not\leq_T Z \oplus Y_0 \oplus Y_1$. The second statement is the third exercise of :ref{to="reducibilities/preservation"}, applied to each weakness property $\mathcal W_C$, with :ref{#prop-cone-avoidance-preservation}.
:::

The first part of the proof uses cone avoidance of $\mathsf P_1$ with the oracle $Z \oplus Y_0$, which is not computable in general. The unrelativized definition does not support such arguments: in the first exercise, no Turing ideal satisfying both its problem and $\mathsf{WKL}$ avoids the cone above $\emptyset'$. Every natural problem known to satisfy an unrelativized preservation property satisfies the relativized one, with the same proof; in this course the definitions are always relativized.

:::quiz[relativization]
In the proof of :ref{#prop-cone-avoidance-product}, why is cone avoidance of $\mathsf P_1$ applied relative to $Z \oplus Y_0$ rather than relative to $Z$?

- [x] Because the final requirement is $C \not\leq_T Z \oplus Y_0 \oplus Y_1$; a solution $Y_1$ with $C \not\leq_T Z \oplus Y_1$ could still compute $C$ together with $Y_0$.
- [ ] Because $X_1$ is not computable in $Z$.

  $X_1$ is computable in $Z$; the issue is the join with $Y_0$.
- [ ] Because $C$ may be computable in $Z \oplus Y_0$.

  $Y_0$ was chosen so that it is not.
:::

## Exercises

::::exercise{#exr-unrelativized-cone difficulty=2}
Let $\mathsf P$ be the problem whose instances are all sets, where the only solution to a computable set is $\emptyset$, and the only solution to a non-computable set $X$ is $X'$. Show that every computable instance of $\mathsf P$ has a solution that computes no non-computable set, that $\mathsf P$ does not admit cone avoidance, and that every Turing ideal satisfying both $\mathsf P$ and $\mathsf{WKL}$ contains $\emptyset'$.

:::solution
A computable instance has the solution $\emptyset$, which computes only computable sets. For cone avoidance, take a non-computable $Z$, the instance $X = Z$ and $C = Z'$: then $C \not\leq_T Z$, and the only solution $Z'$ computes $C$. Let $\mathcal I$ be a Turing ideal satisfying $\mathsf P$ and $\mathsf{WKL}$. Some infinite computable binary tree has no computable path (:ref{#thm-dnc2-no-computable}), so $\mathcal I$ contains a non-computable set $X$, and then $X' \in \mathcal I$. Since $\emptyset' \leq_T X'$, $\emptyset' \in \mathcal I$. Both problems avoid cones on computable instances, but no ω-model of both does: $\mathsf{WKL}$ produces a non-computable set, to which $\mathsf P$ is then applied.
:::
::::

::::exercise{difficulty=1}
For $k \geq 2$, show that $\mathsf{RT}^2_k$ admits cone avoidance, by induction on $k$, using Seetapun's theorem.

:::solution
The case $k = 2$ is :ref{#thm-seetapun}. Let $f : [\nat]^2 \to k + 1$ be computable in $Z$, and $C \not\leq_T Z$. Let $g$ be the $k$-coloring that merges the colors $k - 1$ and $k$. By induction, $g$ has an infinite homogeneous set $H$ with $C \not\leq_T Z \oplus H$. If the color of $H$ is less than $k - 1$, $H$ is homogeneous for $f$. Otherwise $f$ takes only the colors $k - 1$ and $k$ on $[H]^2$; transported to $[\nat]^2$ through the enumeration of $H$, it is a coloring with two colors computable in $Z \oplus H$. By Seetapun's theorem relative to $Z \oplus H$, it has an infinite homogeneous set $L$ with $C \not\leq_T Z \oplus H \oplus L$, and the image of $L$ under the enumeration of $H$ is homogeneous for $f$, computable in $H \oplus L$.
:::
::::

::::exercise{difficulty=1}
Show that neither $\mathsf{WKL}$ nor $\mathsf{COH}$ is ω-reducible to $\mathsf{RT}^1_2$. Explain why :ref{#cor-cone-avoidance-model} cannot prove it, and which weakness property does.

:::solution
The Turing ideal $\mathrm{REC}$ of the computable sets satisfies $\mathsf{RT}^1_2$, by the first entry of the table. It does not satisfy $\mathsf{WKL}$, since some infinite computable binary tree has no computable path (:ref{#thm-dnc2-no-computable}), nor $\mathsf{COH}$, since some computable sequence of sets has no computable cohesive set (:ref{#ex-cohesive}). The three problems admit cone avoidance, so no class $\mathcal W_C$ separates them. The weakness property used here is the class of computable sets: $\mathsf{RT}^1_2$ preserves it, while $\mathsf{WKL}$ and $\mathsf{COH}$ do not.
:::
::::

## Notes and references

The definitions of cone avoidance and strong cone avoidance follow the chapter *Cone avoidance* of Patey's monograph *Lowness and avoidance*, and Dzhafarov and Mummert (Definition 3.6.11 for preservation; Section 8.3 for the cone avoidance of Ramsey's theorem). Strong cone avoidance of the pigeonhole principle is due to Dzhafarov and Jockusch (2009). The cone avoidance basis theorem is due to Jockusch and Soare (1972), cone avoidance for $\mathsf{COH}$ to Jockusch and Stephan (1993) and Cholak, Jockusch and Slaman (2001), and Seetapun's theorem to Seetapun and Slaman (1995). Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022) compare the relativized and unrelativized versions of the preservation properties; they show that the relativized versions of several of them coincide (lessons :ref{to="avoidance/non-sigma1-definitions"} and :ref{to="avoidance/moduli"}), and that the unrelativized versions do not.

- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- P. A. Cholak, C. G. Jockusch, Jr. and T. A. Slaman, *On the strength of Ramsey's theorem for pairs*, Journal of Symbolic Logic 66 (2001), 1–55.
- D. Seetapun and T. A. Slaman, *On the strength of Ramsey's theorem*, Notre Dame Journal of Formal Logic 36 (1995), 570–582.
- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71; arXiv:1903.04273.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 3.6, 4.6 and 8.3.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, sections *Context and motivation* and *First examples*.
