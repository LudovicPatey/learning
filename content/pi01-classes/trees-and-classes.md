---
title: Trees and Π⁰₁ classes
summary: Binary trees and their paths, weak König's lemma, open and closed classes of Cantor space, compactness, and the Π⁰₁ classes as sets of paths through computable trees.
duration: 40
prerequisites: [turing-degrees/oracle-computation, arithmetic-hierarchy/post-theorem]
---

Many problems of mathematics ask for an infinite object satisfying conditions that can each be refuted in finite time: a coloring of an infinite graph in which no two adjacent vertices share a color, a completion of a consistent theory, a separating set for two disjoint c.e. sets. The set of solutions of such a problem is a $\Pi^0_1$ class: the set of infinite paths through a computable binary tree. This lesson defines trees, the topology of Cantor space, and the $\Pi^0_1$ classes, and proves weak König's lemma, which guarantees that an infinite binary tree has a path. The rest of the course studies how complex these paths must be.

## Binary trees

We use the notation for strings of :ref{to="turing-degrees/oracle-computation"}: $\sigma \preceq \tau$ is the prefix relation, $|\sigma|$ the length, $[\sigma]$ the cylinder of the sequences extending $\sigma$, and $2^n$ the set of strings of length $n$.

:::definition{#def-binary-tree}
A **binary tree** is a set $T \subseteq \bstr$ closed under prefixes: if $\tau \in T$ and $\sigma \preceq \tau$, then $\sigma \in T$. Its elements are **nodes**. A **path** through $T$ is a sequence $X \in \cs$ all of whose prefixes belong to $T$; the class of paths is written $[T]$. A node $\sigma \in T$ is **extendible** if $[\sigma] \cap [T] \neq \emptyset$, that is, if some path goes through it.
:::

:::figure[A binary tree. The dashed branches are finite: their nodes are in the tree but are not extendible. Every other node lies on an infinite path, one of which is highlighted.]
<svg class="fig" viewBox="0 0 600 306" width="600" role="img" aria-label="A binary tree: some branches die out, the others extend to infinite paths; one path is highlighted"><line x1="300.0" y1="22" x2="440.0" y2="68" class="ink-stroke" stroke-width="1.2"/><line x1="300.0" y1="22" x2="160.0" y2="68" class="accent-stroke" stroke-width="2.2"/><line x1="160.0" y1="68" x2="230.0" y2="114" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="160.0" y1="68" x2="90.0" y2="114" class="accent-stroke" stroke-width="2.2"/><line x1="440.0" y1="68" x2="370.0" y2="114" class="ink-stroke" stroke-width="1.2"/><line x1="440.0" y1="68" x2="510.0" y2="114" class="ink-stroke" stroke-width="1.2"/><line x1="370.0" y1="114" x2="335.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="90.0" y1="114" x2="125.0" y2="160" class="accent-stroke" stroke-width="2.2"/><line x1="370.0" y1="114" x2="405.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="510.0" y1="114" x2="545.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="230.0" y1="114" x2="195.0" y2="160" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="90.0" y1="114" x2="55.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="510.0" y1="114" x2="475.0" y2="160" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="335.0" y1="160" x2="352.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="405.0" y1="160" x2="422.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="125.0" y1="160" x2="107.5" y2="206" class="accent-stroke" stroke-width="2.2"/><line x1="335.0" y1="160" x2="317.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="545.0" y1="160" x2="562.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="405.0" y1="160" x2="387.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="195.0" y1="160" x2="212.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="55.0" y1="160" x2="72.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="545.0" y1="160" x2="527.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="475.0" y1="160" x2="492.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="475.0" y1="160" x2="457.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="55.0" y1="160" x2="37.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="125.0" y1="160" x2="142.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="107.5" y1="206" x2="98.8" y2="252" class="ink-stroke" stroke-width="1.2"/><line x1="107.5" y1="206" x2="116.2" y2="252" class="accent-stroke" stroke-width="2.2"/><circle cx="300.0" cy="22" r="4" class="accent-fill"/><circle cx="440.0" cy="68" r="4" class="ink-fill"/><circle cx="352.5" cy="206" r="4" class="ink-fill"/><circle cx="422.5" cy="206" r="4" class="ink-fill"/><circle cx="107.5" cy="206" r="4" class="accent-fill"/><circle cx="317.5" cy="206" r="4" class="ink-fill"/><circle cx="562.5" cy="206" r="3.5" class="muted-fill"/><circle cx="230.0" cy="114" r="3.5" class="muted-fill"/><circle cx="387.5" cy="206" r="4" class="ink-fill"/><circle cx="90.0" cy="114" r="4" class="accent-fill"/><circle cx="335.0" cy="160" r="4" class="ink-fill"/><circle cx="212.5" cy="206" r="3.5" class="muted-fill"/><circle cx="125.0" cy="160" r="4" class="accent-fill"/><circle cx="405.0" cy="160" r="4" class="ink-fill"/><circle cx="72.5" cy="206" r="4" class="ink-fill"/><circle cx="545.0" cy="160" r="4" class="ink-fill"/><circle cx="98.8" cy="252" r="4" class="ink-fill"/><circle cx="527.5" cy="206" r="4" class="ink-fill"/><circle cx="160.0" cy="68" r="4" class="accent-fill"/><circle cx="370.0" cy="114" r="4" class="ink-fill"/><circle cx="492.5" cy="206" r="3.5" class="muted-fill"/><circle cx="457.5" cy="206" r="3.5" class="muted-fill"/><circle cx="195.0" cy="160" r="3.5" class="muted-fill"/><circle cx="55.0" cy="160" r="4" class="ink-fill"/><circle cx="37.5" cy="206" r="4" class="ink-fill"/><circle cx="116.2" cy="252" r="4" class="accent-fill"/><circle cx="475.0" cy="160" r="3.5" class="muted-fill"/><circle cx="142.5" cy="206" r="4" class="ink-fill"/><circle cx="510.0" cy="114" r="4" class="ink-fill"/><text x="352.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="422.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="317.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="387.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="72.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="527.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="37.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="142.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="116.2" y="272" text-anchor="middle" class="mrm" font-size="12">⋮</text><text x="130.2" y="274" class="label">a path X</text><text x="310.0" y="18" class="mrm" font-size="13">ε</text><line x1="24" y1="296" x2="44" y2="296" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="300" class="label">a finite branch: no infinite extension</text><line x1="300" y1="296" x2="320" y2="296" class="accent-stroke" stroke-width="2.2"/><text x="326" y="300" class="label">initial segments of an infinite path</text></svg>
:::

:::lemma[Weak König's lemma]{#lem-weak-konig}
Every infinite binary tree has a path.
:::

:::proof{of=lem-weak-konig}
Let $T$ be an infinite binary tree. Say that a node $\sigma \in T$ is **large** if infinitely many nodes of $T$ extend it. The root $\varepsilon$ is large, since $T$ is infinite. If $\sigma$ is large, then one of $\sigma 0$ and $\sigma 1$ is large: every node extending $\sigma$ other than $\sigma$ itself extends one of them, and they cannot both have finitely many extensions in $T$. Define $X$ by induction: $X(n)$ is $0$ if $(X \uh n)\, 0$ is large, and $1$ otherwise. By induction, every $X \uh n$ is large, hence in $T$, so $X \in [T]$.
:::

The proof chooses, at each step, a branch with infinitely many nodes above it, a question that cannot be decided by an algorithm in general. The course measures exactly how much computational power this choice requires.

:::quiz[weak König's lemma]
Why is one of $\sigma 0$ and $\sigma 1$ large when $\sigma$ is large?

- [x] Because the infinitely many nodes extending $\sigma$, other than $\sigma$ itself, extend $\sigma 0$ or $\sigma 1$; if both had finitely many extensions, there would be finitely many nodes above $\sigma$.
- [ ] Because $T$ is computable.

  Computability plays no role in the lemma.
- [ ] Because both $\sigma 0$ and $\sigma 1$ belong to $T$.

  One of them may be missing from $T$; then the other carries all the extensions.

---

Does the lemma hold for trees in which a node may have infinitely many immediate successors?

- [ ] Yes, by the same proof.

  The proof uses that a node has two possible successors: the pigeonhole step fails with infinitely many.
- [x] No: the tree of strings $\sigma$ of natural numbers with $\sigma(i) \geq |\sigma|$ for all $i$ is infinite and has no path.

  The tree contains strings of every length, for instance the string of length $n$ all of whose entries are $n$; but a path $P$ would need $P(0) \geq n$ for every $n$. The case of finitely many successors is treated in the last lesson.
:::

## The topology of Cantor space

:::definition{#def-open-closed}
A class $\mathcal U \subseteq \cs$ is **open** if it is a union of cylinders: $\mathcal U = \bigcup_{\sigma \in W} [\sigma]$ for some set of strings $W$, written $\mathcal U = [W]^{\prec}$. A class is **closed** if its complement is open.
:::

These are the open and closed sets of the product topology on $\cs = \{0, 1\}^\nat$. The cylinders $[\sigma]$ are both open and closed: the complement of $[\sigma]$ is the union of the cylinders $[\tau]$ with $|\tau| = |\sigma|$, $\tau \neq \sigma$.

:::proposition{#prop-closed-tree}
A class $\mathcal P \subseteq \cs$ is closed if and only if $\mathcal P = [T]$ for some binary tree $T$. One can take $T = \{ X \uh n : X \in \mathcal P, n \in \nat \}$, whose nodes are all extendible.
:::

:::proof{of=prop-closed-tree}
If $\mathcal P = [T]$, its complement is the union of the cylinders $[\sigma]$ with $\sigma \notin T$: a sequence is not a path exactly when one of its prefixes is not in $T$. So $\mathcal P$ is closed. Conversely, let $\mathcal P$ be closed, with complement $[W]^{\prec}$, and let $T = \{ X \uh n : X \in \mathcal P \}$, a tree. Clearly $\mathcal P \subseteq [T]$. If $Y \in [T] \setminus \mathcal P$, then $Y \in [\sigma]$ for some $\sigma \in W$; but $\sigma \prec Y$ is in $T$, so $\sigma = X \uh n$ for some $X \in \mathcal P$, and $X \in [\sigma] \subseteq [W]^{\prec}$, a contradiction.
:::

:::proposition[Compactness]{#prop-cantor-compact}
Cantor space is compact: if $\cs = \bigcup_{\sigma \in W} [\sigma]$, then already $\cs = \bigcup_{\sigma \in F} [\sigma]$ for a finite $F \subseteq W$. More generally, every closed class is compact, and a decreasing sequence $\mathcal P_0 \supseteq \mathcal P_1 \supseteq \cdots$ of non-empty closed classes has a non-empty intersection.
:::

:::proof{of=prop-cantor-compact}
Let $T$ be the set of strings having no prefix in $W$, a tree. Its paths are the sequences not covered by $[W]^{\prec}$, so $[T] = \emptyset$, and $T$ is finite by :ref{#lem-weak-konig}. Let $n$ exceed the lengths of its nodes. Every string of length $n$ is then outside $T$, so it has a prefix in $W$, of length at most $n$; the finitely many such prefixes form $F$. The same argument applies to a cover of a closed class $[S]$, using the tree $S \cap T$. For the last statement, if $\bigcap_n \mathcal P_n = \emptyset$, the complements of the $\mathcal P_n$ form an open cover of $\mathcal P_0$, so finitely many of them cover it, and since they increase, one of them does; then $\mathcal P_n = \emptyset$ for some $n$.
:::

## Π⁰₁ classes

:::definition{#def-pi01-class}
A class $\mathcal P \subseteq \cs$ is a **$\Pi^0_1$ class** if $\mathcal P = [T]$ for some computable binary tree $T$. A **$\Sigma^0_1$ class** is a class $[W]^{\prec}$ with $W$ a c.e. set of strings. An **index** of a $\Pi^0_1$ class is an index of the characteristic function of such a tree $T$.
:::

:::proposition{#prop-pi01-equivalent}
For $\mathcal P \subseteq \cs$, the following are equivalent:

1. $\mathcal P$ is a $\Pi^0_1$ class;
2. $\mathcal P = [T]$ for some co-c.e. tree $T$;
3. $\mathcal P = \{ X : \forall n\ R(X \uh n) \}$ for some computable relation $R$ on strings;
4. $\mathcal P = \{ X : \Phi^X_e(0)\diverge \}$ for some $e$;
5. the complement of $\mathcal P$ is a $\Sigma^0_1$ class.

Moreover, the passages between these descriptions are uniform in indices.
:::

:::proof{of=prop-pi01-equivalent}
(1 ⇒ 2) A computable tree is co-c.e.

(2 ⇒ 5) The complement of $[T]$ is $[\bstr \setminus T]^{\prec}$, and $\bstr \setminus T$ is c.e.

(5 ⇒ 4) If the complement is $[W]^{\prec}$ with $W$ c.e., let $\Phi_e$ be the functional which, with oracle $X$, enumerates $W$ and halts as soon as it finds a string $\sigma \in W$ with $\sigma \prec X$. Then $\Phi^X_e(0)\converge$ if and only if $X \in [W]^{\prec}$.

(4 ⇒ 3) Let $R(\sigma)$ be "$\Phi^\sigma_e(0)[|\sigma|]\diverge$". It is computable, and by :ref{#prop-oracle-stages}, $\Phi^X_e(0)\diverge$ if and only if $R(X \uh n)$ for every $n$.

(3 ⇒ 1) Let $T = \{ \sigma : \forall \tau \preceq \sigma\ R(\tau) \}$. It is a computable tree, and $X \in [T]$ if and only if $R(X \uh n)$ for every $n$.

All steps transform indices by computable functions.
:::

:::example{#ex-pi01-classes}
1. Let $A$ and $B$ be disjoint c.e. sets. The class $\mathcal S(A, B) = \{ X : A \subseteq X \text{ and } X \cap B = \emptyset \}$ of **separating sets** is $\Pi^0_1$: $X \notin \mathcal S(A, B)$ if and only if some $n \in A$ has $X(n) = 0$ or some $n \in B$ has $X(n) = 1$, a $\Sigma^0_1$ condition on prefixes of $X$.
2. The class $\mathrm{DNC}_2 = \{ X : X(e) \neq \Phi_e(e) \text{ for every } e \text{ with } \Phi_e(e)\converge \}$ is $\Pi^0_1$, by the same argument; its elements are the **diagonally non-computable** $\{0, 1\}$-valued functions.
3. A singleton $\{ Y \}$ with $Y$ computable is a $\Pi^0_1$ class, with tree $\{ Y \uh n : n \in \nat \}$.
:::

:::proposition{#prop-pi01-emptiness}
Given an index of a computable tree $T$, the property $[T] = \emptyset$ is $\Sigma^0_1$: $[T] = \emptyset$ if and only if $T$ has no node of some length $n$. Consequently, the set of indices of empty $\Pi^0_1$ classes is c.e., and the extendible nodes of a computable tree form a co-c.e. set.
:::

:::proof{of=prop-pi01-emptiness}
By :ref{#lem-weak-konig}, $[T] = \emptyset$ if and only if $T$ is finite, if and only if some length $n$ has no node in $T$, since $T$ is closed under prefixes. For a given $n$, this is decided by testing the $2^n$ strings of length $n$. A node $\sigma$ is not extendible if and only if the computable tree $\{ \tau \in T : \tau \preceq \sigma \text{ or } \sigma \preceq \tau \}$ has no path, which is a $\Sigma^0_1$ condition, uniformly in $\sigma$.
:::

This is a remarkable consequence of compactness: emptiness of a $\Pi^0_1$ class, a priori a $\Pi^0_2$ property, is in fact $\Sigma^0_1$. The non-emptiness of a $\Pi^0_1$ class, which asks for an infinite path, is witnessed by finite information only negatively: one learns that a class is empty, never that it is non-empty.

:::quiz[Π⁰₁ classes]
Why is the emptiness of $[T]$, for a computable tree $T$, a $\Sigma^0_1$ property?

- [x] By weak König's lemma, $[T]$ is empty if and only if $T$ is finite, which is witnessed by a length $n$ at which $T$ has no node, a decidable condition for each $n$.
- [ ] Because $T$ is computable.

  Computability of $T$ makes each test decidable; the reduction from "no path" to "finite" is compactness.
- [ ] Because $[T]$ is a closed class.

  Closedness is needed for compactness, but the statement concerns the complexity of a property of indices.

---

Which of these classes are $\Pi^0_1$?

- [ ] $\{ X : X \subseteq \emptyset' \}$.

  The class is closed, but not $\Pi^0_1$: a string $0^n 1$ has a cylinder disjoint from the class if and only if $n \notin \emptyset'$, and by the second exercise the set of such $n$, the complement of $\emptyset'$, would then be c.e.
- [x] $\{ X : X \cap \emptyset' = \emptyset \}$.

  $X \cap \emptyset' \neq \emptyset$ is the $\Sigma^0_1$ condition "some $n$ enters $\emptyset'$ with $X(n) = 1$".
- [ ] $\{ X : X \text{ is finite} \}$.

  It is not closed: the sequences $1^n 0 0 \cdots$ are finite sets converging to the infinite set $\nat$.
:::

## Exercises

::::exercise{difficulty=1}
Show that the intersection of two $\Pi^0_1$ classes, and the union of two $\Pi^0_1$ classes, are $\Pi^0_1$ classes, uniformly in indices.

:::solution
If $\mathcal P = [S]$ and $\mathcal Q = [T]$ with $S$ and $T$ computable trees, then $\mathcal P \cap \mathcal Q = [S \cap T]$ and $\mathcal P \cup \mathcal Q = [S \cup T]$. The first equality is immediate. For the second, a path of $S \cup T$ that is not a path of $S$ has a prefix $\sigma \notin S$; all its longer prefixes are then outside $S$, hence in $T$, and its shorter prefixes are prefixes of nodes of $T$, hence in $T$; so it is a path of $T$.
:::
::::

::::exercise{difficulty=2}
Show that a class $\mathcal P \subseteq \cs$ is $\Pi^0_1$ if and only if the set of strings $\sigma$ with $[\sigma] \cap \mathcal P = \emptyset$ is c.e., and $\mathcal P$ is closed.

:::solution
If $\mathcal P = [T]$ with $T$ computable, then $[\sigma] \cap \mathcal P = \emptyset$ is the $\Sigma^0_1$ property of :ref{#prop-pi01-emptiness}, uniformly in $\sigma$. Conversely, if $\mathcal P$ is closed and $W = \{ \sigma : [\sigma] \cap \mathcal P = \emptyset \}$ is c.e., then the complement of $\mathcal P$ is $[W]^{\prec}$: a sequence outside the closed class $\mathcal P$ has a cylinder neighborhood disjoint from $\mathcal P$. So the complement is a $\Sigma^0_1$ class, and $\mathcal P$ is $\Pi^0_1$ by :ref{#prop-pi01-equivalent}.
:::
::::

## Notes and references

König's lemma is due to Dénes Kőnig (1927). $\Pi^0_1$ classes were studied systematically from the 1950s, notably by Kleene, Kreisel and Shoenfield, and the theory of their members by Jockusch and Soare (1972). Cenzer and Remmel's survey gives a broad account.

- D. Kőnig, *Über eine Schlussweise aus dem Endlichen ins Unendliche*, Acta Scientiarum Mathematicarum (Szeged) 3 (1927), 121–130.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. Cenzer and J. B. Remmel, *Π⁰₁ classes in mathematics*, in *Handbook of Recursive Mathematics*, Volume 2, Studies in Logic 139, North-Holland, 1998, 623–821.
