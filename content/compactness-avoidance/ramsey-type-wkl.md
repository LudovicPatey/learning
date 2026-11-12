---
title: The Ramsey-type weak König lemma
summary: Homogeneous sets for binary trees and their characterization by the paths; the Ramsey-type weak König lemma, implied by weak König's lemma and by Ramsey's theorem for pairs (Flood); examples showing that homogeneous sets need not carry the complexity of the paths.
duration: 30
prerequisites: [weak-merging, pi01-classes/finitely-branching-trees, ramsey-theorem/jockusch]
---

Both proofs of Seetapun's theorem use compactness: the Dzhafarov–Jockusch step chooses a partition of the reservoir in a non-empty $\Pi^0_1$ class (:ref{#thm-dj-cone-avoidance}), and the direct proof does the same with the Seetapun question. The previous lesson showed that this choice is exactly what prevents the argument from avoiding PA degrees. What the construction really needs from the partition $B$ is weaker: an infinite subset of the reservoir lying on one side of $B$. This lesson isolates this weak form of compactness, the **Ramsey-type weak König lemma**, and relates it to weak König's lemma and to Ramsey's theorem for pairs. The next lesson proves Liu's theorem that it admits PA avoidance, and the lesson after uses it in place of the choice of a partition to prove that Ramsey's theorem for pairs admits PA avoidance.

## Homogeneous sets for trees

As in the course on Ramsey's theorem, a set $P \subseteq \nat$ is identified with its characteristic function, and for $i < 2$ we write $P^{-1}(i) = \{ x : P(x) = i \}$.

:::definition{#def-homogeneous-tree}
Let $T \subseteq \bstr$ be an infinite binary tree and $i < 2$.

1. A finite set $F$ is **homogeneous for $T$ with color $i$** if infinitely many strings $\sigma \in T$ satisfy $\sigma(x) = i$ for every $x \in F$ with $x < |\sigma|$.
2. An infinite set $H$ is **homogeneous for $T$ with color $i$** if every finite subset of $H$ is.
3. The **Ramsey-type weak König lemma** $\mathsf{RWKL}$ is the problem whose instances are the infinite binary trees, and whose solutions are the infinite sets that are homogeneous for the tree with some color.
:::

The definition speaks of finite subsets and of strings of the tree, and never of its paths, so that a solution does not obviously compute a path. In fact homogeneity is a property of the paths.

:::proposition{#prop-homogeneous-member}
Let $T$ be an infinite binary tree, $H$ a set and $i < 2$. Then $H$ is homogeneous for $T$ with color $i$ if and only if there is a path $P \in [T]$ with $H \subseteq P^{-1}(i)$.
:::

:::proof{of=prop-homogeneous-member}
If $P \in [T]$ and $H \subseteq P^{-1}(i)$, the prefixes of $P$ show that every finite $F \subseteq H$ is homogeneous with color $i$. Conversely, for a finite $F \subseteq H$, let $T_F$ be the set of the strings $\sigma \in T$ with $\sigma(x) = i$ for every $x \in F$ with $x < |\sigma|$. It is a tree, and it is infinite by homogeneity of $F$, so it has a path (:ref{#lem-weak-konig}), which is a path of $T$ in the closed class $\mathcal C_F = \{ P \in [T] : F \subseteq P^{-1}(i) \}$. The classes $\mathcal C_F$, for $F$ finite subset of $H$, are closed and non-empty, and $\mathcal C_{F \cup F'} \subseteq \mathcal C_F \cap \mathcal C_{F'}$. By compactness (:ref{#prop-cantor-compact}), their intersection is non-empty; a member $P$ of it satisfies $H \subseteq P^{-1}(i)$.
:::

So a solution to an instance $T$ of $\mathsf{RWKL}$ is an infinite subset of one side of some path of $T$: it is a solution to the pigeonhole principle for a member of $[T]$ that is not given. The definition through finite sets says the same thing without mentioning this member, and this is what makes the problem weak. The examples show the two extremes.

:::example{#ex-rwkl}
1. **A single path.** For a set $C$, the tree $T_C = \{ C \uh n : n \in \nat \}$ has the single path $C$, so its homogeneous sets are the infinite subsets of $C$ or of $\overline C$. On such instances, $\mathsf{RWKL}$ is the pigeonhole principle $\mathsf{RT}^1_2$ for $C$.
2. **The class $\mathrm{DNC}_2$.** Its members are all PA, but it has a computable homogeneous set. Let $H$ be an infinite computable set of numbers $n$ with $J(n)$ undefined, for instance an infinite computable set of indices of the nowhere defined function. For a finite $F \subseteq H$ and each $i < 2$, the function equal to $i$ on $F$ and to $1 - J(n)$ wherever $J(n)$ is defined is a member of $\mathrm{DNC}_2$; so $H$ is homogeneous with both colors.
:::

The second example shows that homogeneous sets can be found where the class leaves the values free, and need not carry the information that makes the members complex. Whether this is always possible, in the sense of PA degrees, is the content of Liu's theorem.

:::proposition{#prop-rwkl-reductions}
1. Every infinite binary tree $T$ has a homogeneous set computable in any of its paths. So $\mathsf{RWKL} \leq_c \mathsf{WKL}$.
2. (Flood) Every infinite binary tree $T$ computes a coloring $f : [\nat]^2 \to 2$ such that every infinite homogeneous set for $f$ is homogeneous for $T$. So $\mathsf{RWKL} \leq_c \mathsf{RT}^2_2$.
:::

:::proof{of=prop-rwkl-reductions}
1. If $P$ is a path, one of $P^{-1}(0)$ and $P^{-1}(1)$ is infinite, and it is homogeneous for $T$ by :ref{#prop-homogeneous-member}.
2. For each $y$, let $\sigma_y$ be the leftmost string of $T$ of length $y$; it exists since $T$ is infinite, and it is computable in $T$. Let $f(\{ x, y \}) = \sigma_y(x)$ for $x < y$. Let $H$ be infinite and homogeneous for $f$ with color $i$, and $F \subseteq H$ finite. For every $y \in H$ with $y > \max F$, $\sigma_y(x) = f(\{ x, y \}) = i$ for every $x \in F$. These are infinitely many strings of $T$, so $F$ is homogeneous for $T$ with color $i$.
:::

Flood's reduction explains the role of $\mathsf{RWKL}$ in Ramsey's theorem: a coloring of pairs can encode the levels of a tree, and its homogeneous sets then behave like homogeneous sets for the tree. Liu's theorem of the next lesson shows that $\mathsf{RWKL}$ admits PA avoidance; by :ref{#prop-pa-avoidance-model}, $\mathsf{WKL} \not\leq_\omega \mathsf{RWKL}$, so $\mathsf{RWKL}$ is strictly weaker than $\mathsf{WKL}$.

:::quiz[homogeneous sets for trees]
In the proof of :ref{#prop-homogeneous-member}, why is compactness needed in addition to the existence of a path in each tree $T_F$?

- [x] Because each $T_F$ gives a path that depends on $F$; a single path $P$ with all of $H$ on side $i$ is obtained as a point in the intersection of the closed classes $\mathcal C_F$.
- [ ] Because $T_F$ may be finite.

  $T_F$ is infinite by the homogeneity of $F$.
- [ ] Because $H$ is not computable.

  The argument is not effective and does not need $H$ to be computable.

---

In Flood's reduction, why is the leftmost string of each length used, rather than an arbitrary one?

- [x] To make the coloring computable in $T$; any choice of strings of $T$ of length $y$ would give the homogeneity property.
- [ ] Because the leftmost strings are extendible.

  They need not be extendible; the argument uses only that they belong to $T$.
- [ ] Because the leftmost strings form a path.

  They need not be prefixes of one another.
:::

## Exercises

::::exercise{difficulty=1}
Show that in :ref{#def-homogeneous-tree}, requiring a single color for all finite subsets of $H$ is no restriction: if every finite subset of $H$ is homogeneous for $T$ with some color, possibly depending on the subset, then $H$ is homogeneous with one color.

:::solution
For a finite $F \subseteq H$, let $c(F) \subseteq \{0, 1\}$ be the non-empty set of colors with which $F$ is homogeneous. If $F \subseteq F'$, then $c(F') \subseteq c(F)$. If the color $0$ fails for some $F_0$ and the color $1$ for some $F_1$, then $c(F_0 \cup F_1) \subseteq c(F_0) \cap c(F_1) = \emptyset$, a contradiction. So some color belongs to $c(F)$ for every $F$.
:::
::::

::::exercise{difficulty=2}
Let $T$ be an infinite binary tree, $\sigma_y$ the leftmost string of $T$ of length $y$, and $f(\{ x, y \}) = \sigma_y(x)$ for $x < y$, as in the proof of :ref{#prop-rwkl-reductions}. Show that $f$ is stable, with limit set the leftmost path $P$ of $T$. Deduce that every infinite binary tree computes a stable coloring all of whose infinite homogeneous sets are homogeneous for $T$, and that the limit set of a stable coloring need not be computable in its homogeneous sets.

:::solution
Fix $x$. Every string of $T$ of length $x + 1$ that is not the prefix of a path has no extension in $T$ beyond some length, by König's lemma; let $\ell$ be larger than all these lengths. Let $y \geq \ell$. The restriction of $\sigma_y$ to $x + 1$ is then the prefix of a path, so it is not to the left of $P \uh (x+1)$, the leftmost such string. And $P \uh y \in T$, so $\sigma_y$ is not to the right of $P \uh y$, and its restriction is not to the right of $P \uh (x+1)$. So $\sigma_y(x) = P(x)$ for $y \geq \ell$: $f$ is stable, with limit set $P$. Its infinite homogeneous sets are homogeneous for $T$ by :ref{#prop-rwkl-reductions}. If $T$ is a computable tree whose paths are all PA, the limit set $P$ is PA, while by Liu's theorem of the next lesson some infinite homogeneous set of $f$ is not PA, so it does not compute $P$.
:::
::::

## Notes and references

The Ramsey-type weak König lemma was introduced by Flood (2012) under the name Ramsey-type König's lemma, together with the reduction from Ramsey's theorem for pairs, in fact from its stable version (second exercise), and the proof that it implies the existence of DNC functions over $\mathsf{RCA}_0$ (see :ref{to="compactness-avoidance/dnc-avoidance"}); the name $\mathsf{RWKL}$ is from Bienvenu, Patey and Shafer (2017), who also proved that $\mathsf{RWKL}$ is robust and studied the Ramsey-type versions of other problems. The presentation follows the chapter *Compactness avoidance* of Patey's monograph, section *Ramsey-type WKL*; the characterization of homogeneous sets by the paths (:ref{#prop-homogeneous-member}) makes explicit what the monograph's definition expresses through finite sets.

- S. Flood, *Reverse mathematics and a Ramsey-type König's lemma*, Journal of Symbolic Logic 77 (2012), 1272–1280.
- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71; arXiv:1411.5874.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *Ramsey-type WKL*.
