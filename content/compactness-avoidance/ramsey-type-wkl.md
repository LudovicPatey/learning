---
title: The Ramsey-type weak König lemma
summary: The Dzhafarov–Jockusch question is weakly merging but its reservoirs are PA; homogeneous sets for binary trees and their characterization by the paths; the Ramsey-type weak König lemma, implied by weak König's lemma and by Ramsey's theorem for pairs (Flood); homogeneous sets need not carry the complexity of the paths.
duration: 40
prerequisites: [weak-merging, pi01-classes/finitely-branching-trees, ramsey-theorem/jockusch]
---

Both proofs of Seetapun's theorem use compactness: the Dzhafarov–Jockusch step chooses a partition of the reservoir in a non-empty $\Pi^0_1$ class (:ref{#thm-dj-cone-avoidance}), and the direct proof does the same with the Seetapun question. The first section shows that the Dzhafarov–Jockusch question is weakly merging, so that :ref{#lem-disjunctive-pa} would apply to it if its reservoirs were not PA, and that the choice of a partition is exactly what makes them PA. What the construction really needs from the partition $B$ is weaker: an infinite subset of the reservoir lying on one side of $B$. The rest of the lesson isolates this weak form of compactness, the **Ramsey-type weak König lemma**, and relates it to weak König's lemma and to Ramsey's theorem for pairs. The next two lessons prove Liu's theorem that it admits PA avoidance, and the following one uses it in place of the choice of a partition to prove that Ramsey's theorem for pairs admits PA avoidance.

## The Dzhafarov–Jockusch question

:::example{#ex-dj-weakly-merging}
Let $A$ be a set, and consider the disjunctive notion of forcing of :ref{#ex-dj-disjunctive}: conditions $(\sigma_0, \sigma_1, X)$ with $\sigma_i \subseteq A^i$, where $A^0 = A$ and $A^1 = \overline A$, and $X$ an infinite set in a Scott ideal $\mathcal M$, with its question: $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ if for every set $B$, with $B^0 = B$ and $B^1 = \overline B$, there are $i < 2$ and $\tau$ compatible with $(\sigma_i, X \cap B^i)$ satisfying $\varphi_i$. This question is weakly merging with $k = 3$.

Indeed, suppose that the answer is negative for three pairs $(\varphi^s_0, \varphi^s_1)$, $s < 3$. For each $s$, the sets $B$ witnessing the negative answer form a non-empty $\Pi^0_1(X \oplus Z)$ class, so the product of the three classes has a member $(B_0, B_1, B_2) \in \mathcal M$. The three sets split $X$ into the eight sets $X \cap B_0^{a_0} \cap B_1^{a_1} \cap B_2^{a_2}$, one of which, say for $(a_0, a_1, a_2)$, is infinite; call it $Y$. Two of the three bits are equal, say $a_s = a_t = i$ with $s < t$. The condition $(\sigma_0, \sigma_1, Y)$ extends $c$, and a member of side $i$ satisfying $\varphi^s_i$ would have a prefix compatible with $(\sigma_i, X \cap B_s^i)$ satisfying it, which is excluded; the same holds for $t$. So $(\sigma_0, \sigma_1, Y) \Vdash \neg \varphi^s_i(G_i) \wedge \neg \varphi^t_i(G_i)$.
:::

Yet :ref{#lem-disjunctive-pa} does not apply: a Scott ideal containing $Z$ contains sets that are PA relative to $Z$, hence relative to every $D \leq_T Z$, and these sets cannot be excluded from $\mathcal M$, since the reservoirs $X \cap B_0^{a_0} \cap \cdots$ are computed from them. The reservoirs must be kept in the class of the sets that are not PA relative to $D$, and a non-empty $\Pi^0_1(X \oplus Z)$ class of partitions need not have such a member. What the argument really needs from a negative answer is weaker than a partition: an infinite subset of $X$ contained in $B^a$ for some member $B$ of the class and some side $a$. Liu's solution is to shrink the reservoir in this way without choosing a partition. The existence of such subsets is the Ramsey-type weak König lemma.

:::quiz[the Dzhafarov–Jockusch question]
In :ref{#ex-dj-weakly-merging}, why are three negative answers needed rather than two?

- [x] Because the infinite piece $Y$ of $X$ lies on side $a_s$ of $B_s$ for each $s$, and only with three bits are two of them guaranteed to be equal; with two bits, $Y$ could lie on side $0$ of $B_0$ and side $1$ of $B_1$.
- [ ] Because the product of two $\Pi^0_1$ classes may be empty.

  A product of non-empty classes is non-empty.
- [ ] Because $X$ must be split into eight pieces.

  The eight pieces come from three sets; the number of sets is what matters.
:::

## Homogeneous sets for trees

As in the course on Ramsey's theorem, a set $P \subseteq \nat$ is identified with its characteristic function, and for $i < 2$ we write $P^{-1}(i) = \{ x : P(x) = i \}$.

:::definition{#def-homogeneous-tree}
Let $T \subseteq \bstr$ be an infinite binary tree and $i < 2$.

1. A finite set $F$ is **homogeneous for $T$ with color $i$** if infinitely many strings $\sigma \in T$ satisfy $\sigma(x) = i$ for every $x \in F$ with $x < |\sigma|$.
2. An infinite set $H$ is **homogeneous for $T$ with color $i$** if every finite subset of $H$ is.
3. The **Ramsey-type weak König lemma** $\mathsf{RWKL}$ is the problem whose instances are the infinite binary trees, and whose solutions are the infinite sets that are homogeneous for the tree with some color.
:::

::::exercise{#ex-homogeneous-one-color difficulty=1 objective="Check that the color in the definition of homogeneous sets for trees can be taken uniform, by a finite intersection argument."}
Show that in :ref{#def-homogeneous-tree}, requiring a single color for all finite subsets of $H$ is no restriction: if every finite subset of $H$ is homogeneous for $T$ with some color, possibly depending on the subset, then $H$ is homogeneous with one color.

:::solution
For a finite $F \subseteq H$, let $c(F) \subseteq \{0, 1\}$ be the non-empty set of colors with which $F$ is homogeneous. If $F \subseteq F'$, then $c(F') \subseteq c(F)$. If the color $0$ fails for some $F_0$ and the color $1$ for some $F_1$, then $c(F_0 \cup F_1) \subseteq c(F_0) \cap c(F_1) = \emptyset$, a contradiction. So some color belongs to $c(F)$ for every $F$.
:::
::::

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

Flood's reduction explains the role of $\mathsf{RWKL}$ in Ramsey's theorem: a coloring of pairs can encode the levels of a tree, and its homogeneous sets then behave like homogeneous sets for the tree. Liu's theorem :ref{#thm-rwkl-pa-avoidance} shows that $\mathsf{RWKL}$ admits PA avoidance; by :ref{#prop-pa-avoidance-model}, $\mathsf{WKL} \not\leq_\omega \mathsf{RWKL}$, so $\mathsf{RWKL}$ is strictly weaker than $\mathsf{WKL}$.

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

::::exercise{#ex-flood-stable difficulty=2 objective="Show that Flood's coloring is stable, with the leftmost path as limit set."}
Let $T$ be an infinite binary tree, $\sigma_y$ the leftmost string of $T$ of length $y$, and $f(\{ x, y \}) = \sigma_y(x)$ for $x < y$, as in the proof of :ref{#prop-rwkl-reductions}. Show that $f$ is stable, with limit set the leftmost path $P$ of $T$. Deduce that every infinite binary tree computes a stable coloring all of whose infinite homogeneous sets are homogeneous for $T$.

:::solution
Fix $x$. Every string of $T$ of length $x + 1$ that is not the prefix of a path has no extension in $T$ beyond some length, by König's lemma; let $\ell$ be larger than all these lengths. Let $y \geq \ell$. The restriction of $\sigma_y$ to $x + 1$ is then the prefix of a path, so it is not to the left of $P \uh (x+1)$, the leftmost such string. And $P \uh y \in T$, so $\sigma_y$ is not to the right of $P \uh y$, and its restriction is not to the right of $P \uh (x+1)$. So $\sigma_y(x) = P(x)$ for $y \geq \ell$: $f$ is stable, with limit set $P$. Its infinite homogeneous sets are homogeneous for $T$ by :ref{#prop-rwkl-reductions}.
:::
::::

## Notes and references

The Ramsey-type weak König lemma was introduced by Flood (2012) under the name Ramsey-type König's lemma, together with the reduction from Ramsey's theorem for pairs, in fact from its stable version (:ref{#ex-flood-stable}), and the proof that it implies the existence of DNC functions over $\mathsf{RCA}_0$ (see :ref{to="compactness-avoidance/dnc-avoidance"}); the name $\mathsf{RWKL}$ is from Bienvenu, Patey and Shafer (2017), who studied the Ramsey-type versions of other problems. The weak merging of the Dzhafarov–Jockusch question (:ref{#ex-dj-weakly-merging}) is an exercise of the section *Weak merging* of Patey's monograph. The presentation of $\mathsf{RWKL}$ follows the chapter *Compactness avoidance* of Patey's monograph, section *Ramsey-type WKL*; the characterization of homogeneous sets by the paths (:ref{#prop-homogeneous-member}) makes explicit what the monograph's definition expresses through finite sets.

- S. Flood, *Reverse mathematics and a Ramsey-type König's lemma*, Journal of Symbolic Logic 77 (2012), 1272–1280.
- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71; arXiv:1411.5874.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, sections *Weak merging* and *Ramsey-type WKL*.

:::::exercises
::::exercise[The pigeonhole principle with $\ell$ colors]{#ex-dj-ell-colors difficulty=2 objective="Extend the weak merging of the Dzhafarov–Jockusch question to $\ell$ colors, with $k = \ell + 1$."}
Generalize :ref{#ex-dj-weakly-merging} to the pigeonhole principle with $\ell$ colors: conditions $(\sigma_0, \dots, \sigma_{\ell - 1}, X)$ with $\sigma_i \subseteq A^i$ for a partition $\nat = A^0 \sqcup \cdots \sqcup A^{\ell - 1}$, $X$ in a Scott ideal, and the question "for every partition $\nat = B^0 \sqcup \cdots \sqcup B^{\ell - 1}$ there are $i < \ell$ and $\tau$ compatible with $(\sigma_i, X \cap B^i)$ satisfying $\varphi_i$". State weak merging for $\ell$ sides, and show that this question satisfies it with $k = \ell + 1$.

:::solution
Weak merging for $\ell$ sides: for every condition there is $k$ such that if the answer is negative for $k$ tuples $(\varphi^s_0, \dots, \varphi^s_{\ell - 1})$, then some extension forces $\neg \varphi^s_i(G_i) \wedge \neg \varphi^t_i(G_i)$ for some side $i$ and some $s < t < k$. Given $\ell + 1$ negative answers, each is witnessed by a non-empty $\Pi^0_1(X \oplus Z)$ class of partitions (coded as functions $\nat \to \ell$), and the Scott ideal contains a member $(B_s)_{s \leq \ell}$ of the product. The sets $X \cap \bigcap_{s \leq \ell} B^{a_s}_s$, for $(a_s) \in \ell^{\ell + 1}$, are finitely many and cover $X$, so one of them, $Y$, is infinite. Among the $\ell + 1$ colors $a_s < \ell$, two coincide by the pigeonhole principle: $a_s = a_t = i$ with $s < t$. A member of side $i$ of $(\vec \sigma, Y)$ satisfying $\varphi^s_i$ would have a prefix compatible with $(\sigma_i, X \cap B^i_s)$ satisfying it, contradicting the choice of $B_s$; the same holds for $t$. So $(\vec \sigma, Y)$ forces both negations on side $i$.
:::
::::

::::exercise[No merging with two answers]{#ex-dj-not-merging difficulty=1 objective="Show that two negative answers of the Dzhafarov–Jockusch question cannot always be merged on one side, so that three answers are needed."}
In the notion of forcing of :ref{#ex-dj-weakly-merging}, let $c = (\varepsilon, \varepsilon, \nat)$. Find two pairs of $\Sigma^0_1$ sentences $(\varphi^s_0, \varphi^s_1)$, $s < 2$, answered negatively at $c$, such that for no extension $d$ of $c$ and no side $i$ does $d$ force $\neg \varphi^0_i(G_i) \wedge \neg \varphi^1_i(G_i)$.

:::solution
Let $\varphi^0_0$ and $\varphi^1_1$ be the sentence "$G$ contains an even number", and $\varphi^0_1$ and $\varphi^1_0$ the sentence "$G$ contains an odd number". For $s = 0$, the set $B$ of odd numbers witnesses the negative answer, as in :ref{#ex-disjunctive-one-negation}: strings compatible with $(\varepsilon, \nat \cap B^0)$ have only odd elements, and strings compatible with $(\varepsilon, \nat \cap B^1)$ only even elements. For $s = 1$, the set $B$ of even numbers witnesses it in the same way.

Let $d = (\tau_0, \tau_1, Y)$ extend $c$, $i < 2$, and $y \in Y$. The set $\tau_i \cup \{ y \}$ is a member of side $i$ of $d$, since $y \geq \min Y \geq |\tau_i|$. It contains the number $y$, which is even or odd, so it satisfies $\varphi^0_i$ or $\varphi^1_i$, which are the two sentences "contains an even number" and "contains an odd number" in some order. So $d$ does not force both negations on side $i$. Hence the constant $k = 3$ of :ref{#ex-dj-weakly-merging} cannot be replaced by $2$: the question is weakly merging but not merging.
:::
::::

::::exercise[First properties of homogeneous sets]{#ex-homogeneous-basic difficulty=1 objective="Check how homogeneity behaves under subsets and larger trees, and what a set homogeneous with both colors says about the paths."}
Let $T$ and $T'$ be infinite binary trees, and $H$ an infinite set homogeneous for $T$ with color $i$. Show that every infinite subset of $H$ is homogeneous for $T$ with color $i$; that if $[T] \subseteq [T']$, then $H$ is homogeneous for $T'$ with color $i$; and that if $H$ is also homogeneous for $T$ with color $1 - i$, then $[T]$ has at least two members.

:::solution
A finite subset of a subset of $H$ is a finite subset of $H$, so the first statement follows from the definition. By :ref{#prop-homogeneous-member}, there is $P \in [T]$ with $H \subseteq P^{-1}(i)$; then $P \in [T']$, and $H$ is homogeneous for $T'$ by the same proposition. If $H$ is homogeneous with both colors, there are $P_0, P_1 \in [T]$ with $H \subseteq P_0^{-1}(i)$ and $H \subseteq P_1^{-1}(1 - i)$. Since $H$ is non-empty, $P_0$ and $P_1$ differ on its elements, so they are two distinct members of $[T]$.
:::
::::

::::exercise[Homogeneity is co-c.e.]{#ex-homogeneous-finite-pi01 difficulty=1 objective="Compute the complexity of homogeneity for finite and infinite sets, using that the strings compatible with a finite set form a tree."}
Let $T$ be an infinite binary tree. Show that "$F$ is homogeneous for $T$ with color $i$" is a $\Pi^0_1(T)$ property of the finite set $F$ and of $i$, and that for $T$ computable, the class of the sets $H \subseteq \nat$ all of whose finite subsets are homogeneous for $T$ with color $i$ is a $\Pi^0_1$ class.

:::solution
Let $T_F$ be the set of the strings $\sigma \in T$ with $\sigma(x) = i$ for every $x \in F$ with $x < |\sigma|$. It is closed under prefixes, since $T$ is and the condition on $\sigma$ is inherited by its prefixes, and it is computable in $T$, uniformly in $F$ and $i$. A tree contains infinitely many strings if and only if it contains a string of every length: if it contains a string of length at least $\ell$, its prefix of length $\ell$ is in the tree, and a binary tree has finitely many strings of each length. So $F$ is homogeneous with color $i$ if and only if for every $\ell$, some string of length $\ell$ belongs to $T_F$; for each $\ell$ this is a finite search, so the property is $\Pi^0_1(T)$.

For $T$ computable, a set $H$ belongs to the class if and only if for every finite set $F$ and every $\ell$, either $F \not\subseteq H$ or some string of length $\ell$ belongs to $T_F$. Each clause is decided by a finite prefix of $H$ and a finite computation, so the class is $\Pi^0_1$. Its infinite members are the solutions of color $i$ to the instance $T$ of $\mathsf{RWKL}$.
:::
::::

::::exercise[Homogeneous sets for the class of DNC₂ functions]{#ex-dnc2-homogeneous difficulty=1 objective="Characterize the homogeneous sets of the class $\mathrm{DNC}_2$, and see where the class leaves the values free."}
Let $T$ be a computable tree with $[T] = \mathrm{DNC}_2$, the class of the functions $\mathrm{DNC}_2$ relative to $\emptyset$. Show that an infinite set $H$ is homogeneous for $T$ with color $i$ if and only if $J(n) \neq i$ for every $n \in H$ at which $J(n)$ is defined. Deduce that both colors have computable infinite homogeneous sets, but that a set homogeneous with color $i$ may be contained in $\{ n : J(n) = 1 - i \}$.

:::solution
By :ref{#prop-homogeneous-member}, $H$ is homogeneous with color $i$ if and only if some $f \in \mathrm{DNC}_2$ equals $i$ on $H$. If $J(n) = i$ for some $n \in H$, no $\mathrm{DNC}_2$ function takes the value $i$ at $n$. Conversely, if $J(n) \neq i$ wherever $J(n)$ is defined on $H$, the function equal to $i$ on $H$ and to $1 - J(m)$ at the other numbers $m$ where $J(m)$ is defined, $0$ elsewhere, is $\mathrm{DNC}_2$; it is well defined on $H$ since $i = 1 - J(n)$ when $n \in H$ and $J(n)$ is defined.

An infinite computable set of numbers $n$ with $J(n)$ undefined, as in :ref{#ex-rwkl}, is homogeneous with both colors. The set $\{ n : J(n) = 1 - i \}$ is infinite, since $J$ takes the value $1 - i$ at the indices of the constant function $1 - i$, and all its infinite subsets are homogeneous with color $i$. This set is c.e., so it has infinite computable subsets: homogeneity with color $i$ only excludes the numbers at which $J$ takes the value $i$, and carries none of the information that makes the members of $\mathrm{DNC}_2$ PA.
:::
::::

::::exercise[A tree whose leftmost strings are not extendible]{#ex-flood-example difficulty=1 objective="Compute Flood's coloring on an explicit tree, and see that the leftmost strings need not be prefixes of paths."}
Let $T$ be the tree of the strings of the form $1^m$ or $1^m 0$, $m \geq 0$. Compute the coloring $f$ of the proof of :ref{#prop-rwkl-reductions} for $T$, its infinite homogeneous sets, and the sets homogeneous for $T$.

:::solution
$T$ is closed under prefixes and infinite, and its only path is $1^\infty$, the set $\nat$. For $y \geq 1$, the strings of $T$ of length $y$ are $1^y$ and $1^{y-1} 0$, and the leftmost one is $\sigma_y = 1^{y-1} 0$. So for $x < y$, $f(\{ x, y \}) = 1$ if $x < y - 1$ and $f(\{ x, y \}) = 0$ if $x = y - 1$. An infinite set cannot be homogeneous with color $0$: for $x < y < z$ in it, $x = z - 1$ and $y = z - 1$ would both hold. The infinite homogeneous sets of $f$ are the infinite sets with no two consecutive elements, with color $1$.

By :ref{#prop-homogeneous-member}, the sets homogeneous for $T$ are the infinite subsets of $(1^\infty)^{-1}(1) = \nat$, with color $1$, and none has color $0$. Every infinite homogeneous set of $f$ is therefore homogeneous for $T$, as Flood's reduction requires, although no string $\sigma_y$ with $y \geq 1$ is the prefix of a path. The coloring is stable, with limit set $\nat$, the leftmost path, as in :ref{#ex-flood-stable}.
:::
::::
:::::
