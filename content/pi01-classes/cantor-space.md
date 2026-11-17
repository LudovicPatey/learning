---
title: Trees and Cantor space
summary: Binary trees and their paths, weak König's lemma, open and closed classes of Cantor space, and compactness.
duration: 30
prerequisites: [turing-degrees/oracle-computation]
---

Many problems of mathematics ask for an infinite object satisfying conditions that can each be refuted in finite time: a coloring of an infinite graph in which no two adjacent vertices share a color, a completion of a consistent theory, a separating set for two disjoint c.e. sets. The solutions of such a problem are the infinite paths through a binary tree, and when the conditions are checked by an algorithm, the tree is computable; the set of solutions is then a $\Pi^0_1$ class, the subject of the next lesson. This lesson sets up the combinatorics and the topology: binary trees, weak König's lemma, which guarantees that an infinite binary tree has a path, and the open and closed classes of Cantor space, whose compactness is the main tool of the course.

## Binary trees

We use the notation for strings of :ref{to="turing-degrees/oracle-computation"}: $\sigma \preceq \tau$ is the prefix relation, $|\sigma|$ the length, and $[\sigma]$ the cylinder of the sequences extending $\sigma$. We also write $2^n$ for the set of strings of length $n$, and $2^{\leq n}$ for the set of strings of length at most $n$.

:::definition{#def-binary-tree}
A **binary tree** is a set $T \subseteq \bstr$ closed under prefixes: if $\tau \in T$ and $\sigma \preceq \tau$, then $\sigma \in T$. Its elements are **nodes**. A **path** through $T$ is a sequence $X \in \cs$ all of whose prefixes belong to $T$; the class of paths is written $[T]$. A node $\sigma \in T$ is **extendible** if $[\sigma] \cap [T] \neq \emptyset$, that is, if some path goes through it.
:::

:::example{#ex-binary-trees}
Write $0^\infty$ for the constant sequence $00\cdots$.

1. The full binary tree $\bstr$ has every sequence as a path: $[\bstr] = \cs$.
2. For every sequence $Y$, the tree $\{ Y \uh n : n \in \nat \}$ has exactly one path, $Y$.
3. The tree $\{ 0^n : n \in \nat \} \cup \{ 0^n 1 : n \in \nat \}$ is infinite and has exactly one path, $0^\infty$. Its nodes $0^n 1$ are not extendible: a tree may have infinitely many nodes that lie on no path.
4. A finite tree has no path. Weak König's lemma, below, gives the converse for binary trees.
:::

:::figure[A binary tree. The dashed branches are finite: their nodes are in the tree but are not extendible. Every other node lies on an infinite path, one of which is highlighted.]
<svg class="fig" viewBox="0 0 600 306" width="600" role="img" aria-label="A binary tree: some branches die out, the others extend to infinite paths; one path is highlighted"><line x1="300.0" y1="22" x2="160.0" y2="68" class="accent-stroke" stroke-width="2.2"/><line x1="300.0" y1="22" x2="440.0" y2="68" class="ink-stroke" stroke-width="1.2"/><line x1="160.0" y1="68" x2="90.0" y2="114" class="accent-stroke" stroke-width="2.2"/><line x1="160.0" y1="68" x2="230.0" y2="114" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="440.0" y1="68" x2="370.0" y2="114" class="ink-stroke" stroke-width="1.2"/><line x1="440.0" y1="68" x2="510.0" y2="114" class="ink-stroke" stroke-width="1.2"/><line x1="90.0" y1="114" x2="55.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="90.0" y1="114" x2="125.0" y2="160" class="accent-stroke" stroke-width="2.2"/><line x1="230.0" y1="114" x2="195.0" y2="160" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="370.0" y1="114" x2="335.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="370.0" y1="114" x2="405.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="510.0" y1="114" x2="475.0" y2="160" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="510.0" y1="114" x2="545.0" y2="160" class="ink-stroke" stroke-width="1.2"/><line x1="55.0" y1="160" x2="37.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="55.0" y1="160" x2="72.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="125.0" y1="160" x2="107.5" y2="206" class="accent-stroke" stroke-width="2.2"/><line x1="125.0" y1="160" x2="142.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="195.0" y1="160" x2="212.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="335.0" y1="160" x2="317.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="335.0" y1="160" x2="352.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="405.0" y1="160" x2="387.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="405.0" y1="160" x2="422.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="475.0" y1="160" x2="457.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="475.0" y1="160" x2="492.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="545.0" y1="160" x2="527.5" y2="206" class="ink-stroke" stroke-width="1.2"/><line x1="545.0" y1="160" x2="562.5" y2="206" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="107.5" y1="206" x2="98.8" y2="252" class="ink-stroke" stroke-width="1.2"/><line x1="107.5" y1="206" x2="116.2" y2="252" class="accent-stroke" stroke-width="2.2"/><circle cx="300.0" cy="22" r="4" class="accent-fill"/><circle cx="160.0" cy="68" r="4" class="accent-fill"/><circle cx="440.0" cy="68" r="4" class="ink-fill"/><circle cx="90.0" cy="114" r="4" class="accent-fill"/><circle cx="230.0" cy="114" r="3.5" class="muted-fill"/><circle cx="370.0" cy="114" r="4" class="ink-fill"/><circle cx="510.0" cy="114" r="4" class="ink-fill"/><circle cx="55.0" cy="160" r="4" class="ink-fill"/><circle cx="125.0" cy="160" r="4" class="accent-fill"/><circle cx="195.0" cy="160" r="3.5" class="muted-fill"/><circle cx="335.0" cy="160" r="4" class="ink-fill"/><circle cx="405.0" cy="160" r="4" class="ink-fill"/><circle cx="475.0" cy="160" r="3.5" class="muted-fill"/><circle cx="545.0" cy="160" r="4" class="ink-fill"/><circle cx="37.5" cy="206" r="4" class="ink-fill"/><circle cx="72.5" cy="206" r="4" class="ink-fill"/><circle cx="107.5" cy="206" r="4" class="accent-fill"/><circle cx="142.5" cy="206" r="4" class="ink-fill"/><circle cx="212.5" cy="206" r="3.5" class="muted-fill"/><circle cx="317.5" cy="206" r="4" class="ink-fill"/><circle cx="352.5" cy="206" r="4" class="ink-fill"/><circle cx="387.5" cy="206" r="4" class="ink-fill"/><circle cx="422.5" cy="206" r="4" class="ink-fill"/><circle cx="457.5" cy="206" r="3.5" class="muted-fill"/><circle cx="492.5" cy="206" r="3.5" class="muted-fill"/><circle cx="527.5" cy="206" r="4" class="ink-fill"/><circle cx="562.5" cy="206" r="3.5" class="muted-fill"/><circle cx="98.8" cy="252" r="4" class="ink-fill"/><circle cx="116.2" cy="252" r="4" class="accent-fill"/><text x="37.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="72.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="142.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="317.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="352.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="387.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="422.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="527.5" y="226" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><text x="116.2" y="272" text-anchor="middle" class="mrm" font-size="12">⋮</text><text x="130.2" y="274" class="label">a path X</text><text x="310.0" y="18" class="mrm" font-size="13">ε</text><line x1="24" y1="296" x2="44" y2="296" class="muted-stroke" stroke-dasharray="3 3" stroke-width="1.2"/><text x="50" y="300" class="label">a finite branch: no infinite extension</text><line x1="300" y1="296" x2="320" y2="296" class="accent-stroke" stroke-width="2.2"/><text x="326" y="300" class="label">initial segments of an infinite path</text></svg>
:::

:::lemma[Weak König's lemma]{#lem-weak-konig}
Every infinite binary tree has a path.
:::

The path is built one bit at a time. A node can lead to a path only if infinitely many nodes lie above it, and the proof keeps this property as an invariant: since a node has only two successors, the infinitely many nodes above it cannot all be distributed over successors with finitely many nodes each. This is a pigeonhole argument, and it is the only place where the binary branching is used.

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

These are the open and closed sets of the product topology on $\cs = \{0, 1\}^\nat$. The cylinders $[\sigma]$ are both open and closed: the complement of $[\sigma]$ is the union of the cylinders $[\tau]$ with $|\tau| = |\sigma|$, $\tau \neq \sigma$. A class is open when membership in it is witnessed by a finite prefix, and closed when non-membership is.

For example, the class $\{ X : X(n) = 1 \text{ for some } n \} = \bigcup_n [0^n 1]$ is open. It is not closed, since its complement $\{ 0^\infty \}$ contains no cylinder and so is not open. Every singleton $\{ Y \}$ is closed, its complement being the union of the cylinders $[\tau]$ with $\tau \not\prec Y$. The class of finite sets is neither open nor closed: every cylinder contains infinite sets, so it is not open; and every cylinder $[1^n]$ around the infinite set $\nat$ contains the finite set $1^n 0^\infty$, so its complement is not open.

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

:::figure[The proof of :ref{#prop-cantor-compact} on the cover $W = \{1, 00, 011, 0100, 0101\}$. The strings with no prefix in $W$ form a tree without path, hence finite; beyond its height, every string has a prefix in $W$, and finitely many cylinders already cover Cantor space.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The strings without prefix in W form a finite tree; the cylinders of the strings of W cover Cantor space"><line x1="300.0" y1="24" x2="160.0" y2="64" class="ink-stroke" stroke-width="1.4"/><line x1="160.0" y1="64" x2="230.0" y2="104" class="ink-stroke" stroke-width="1.4"/><line x1="230.0" y1="104" x2="195.0" y2="144" class="ink-stroke" stroke-width="1.4"/><line x1="300.0" y1="24" x2="440.0" y2="64" class="accent-stroke" stroke-width="1.4"/><line x1="160.0" y1="64" x2="90.0" y2="104" class="accent-stroke" stroke-width="1.4"/><line x1="230.0" y1="104" x2="265.0" y2="144" class="accent-stroke" stroke-width="1.4"/><line x1="195.0" y1="144" x2="177.5" y2="184" class="accent-stroke" stroke-width="1.4"/><line x1="195.0" y1="144" x2="212.5" y2="184" class="accent-stroke" stroke-width="1.4"/><line x1="440.0" y1="70" x2="440.0" y2="208" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/><line x1="90.0" y1="110" x2="90.0" y2="208" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/><line x1="265.0" y1="150" x2="265.0" y2="208" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/><line x1="177.5" y1="190" x2="177.5" y2="208" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/><line x1="212.5" y1="190" x2="212.5" y2="208" class="muted-stroke" stroke-width="1" stroke-dasharray="2 3"/><circle cx="300.0" cy="24" r="4" class="ink-fill"/><circle cx="160.0" cy="64" r="4" class="ink-fill"/><circle cx="230.0" cy="104" r="4" class="ink-fill"/><circle cx="195.0" cy="144" r="4" class="ink-fill"/><circle cx="440.0" cy="64" r="5" class="node"/><text x="449.0" y="59" class="mrm" font-size="12">1</text><circle cx="90.0" cy="104" r="5" class="node"/><text x="81.0" y="99" text-anchor="end" class="mrm" font-size="12">00</text><circle cx="265.0" cy="144" r="5" class="node"/><text x="274.0" y="139" class="mrm" font-size="12">011</text><circle cx="177.5" cy="184" r="5" class="node"/><text x="168.5" y="179" text-anchor="end" class="mrm" font-size="12">0100</text><circle cx="212.5" cy="184" r="5" class="node"/><text x="221.5" y="179" class="mrm" font-size="12">0101</text><text x="309.0" y="18" class="mrm" font-size="13">ε</text><rect x="21.0" y="210" width="138.0" height="22" class="cell head-cell"/><text x="90.0" y="225" text-anchor="middle" class="mrm" font-size="11">[00]</text><rect x="161.0" y="210" width="33.0" height="22" class="cell head-cell"/><text x="177.5" y="225" text-anchor="middle" class="mrm" font-size="11">[0100]</text><rect x="196.0" y="210" width="33.0" height="22" class="cell head-cell"/><text x="212.5" y="225" text-anchor="middle" class="mrm" font-size="11">[0101]</text><rect x="231.0" y="210" width="68.0" height="22" class="cell head-cell"/><text x="265.0" y="225" text-anchor="middle" class="mrm" font-size="11">[011]</text><rect x="301.0" y="210" width="278.0" height="22" class="cell head-cell"/><text x="440.0" y="225" text-anchor="middle" class="mrm" font-size="11">[1]</text><text x="20" y="256" class="label">Cantor space, ordered from left (0) to right (1): the cylinders [σ], σ ∈ W, cover it</text><circle cx="24" cy="276" r="4" class="ink-fill"/><text x="34" y="280" class="label">strings with no prefix in W: the finite tree T</text><circle cx="344" cy="276" r="5" class="node"/><text x="354" y="280" class="label">strings of W</text></svg>
:::

Compactness is the main tool of the course. It converts a statement about all sequences, such as "no sequence is a path through $T$", into a statement about finitely many strings, such as "no string of length $n$ is in $T$". The next lesson shows that this conversion is effective, and the basis theorems of :ref{to="pi01-classes/basis-theorems"} rest on it.

## Exercises

::::exercise{#ex-clopen difficulty=1 objective="Use compactness to characterize the classes that are both open and closed."}
Show that a class is both open and closed if and only if it is a finite union of cylinders.

:::solution
A finite union of cylinders is open, and it is closed as a finite union of closed classes: if $\mathcal U = [\sigma_1] \cup \dots \cup [\sigma_k]$, with $n$ the largest length of the $\sigma_i$, then the complement of $\mathcal U$ is the union of the cylinders $[\tau]$ with $|\tau| = n$ and $\tau$ extending no $\sigma_i$. Conversely, let $\mathcal U = [W]^{\prec}$ be open and closed. Then $\mathcal U$ is closed, hence compact by :ref{#prop-cantor-compact}, and it is covered by the cylinders $[\sigma]$, $\sigma \in W$; finitely many of them cover it, and their union is $\mathcal U$.
:::
::::

::::exercise{#ex-uniform-continuity difficulty=2 objective="Derive a uniform bound on the use of a functional that is total on Cantor space from weak König's lemma."}
Let $\Phi$ be a Turing functional such that $\Phi^X$ is total for every $X \in \cs$. Show that there is a function $u$ such that, for every $X$ and every $n$, the computation $\Phi^X(n)$ converges with use at most $u(n)$. Deduce that $\Phi^X(n)$ is computed from the $u(n)$ first bits of $X$, uniformly in $X$.

:::solution
Fix $n$, and let $T_n$ be the set of strings $\sigma$ such that $\Phi^\sigma(n)[|\sigma|]\diverge$. It is a tree, by monotonicity of the computations of :ref{#prop-oracle-stages}. A path $X$ through $T_n$ would satisfy $\Phi^{X \uh s}(n)[s]\diverge$ for every $s$, hence $\Phi^X(n)\diverge$, contrary to the hypothesis. So $T_n$ is finite by :ref{#lem-weak-konig}; let $u(n)$ exceed the lengths of its nodes. For every $X$, the string $X \uh u(n)$ is not in $T_n$, so $\Phi^{X \uh u(n)}(n)[u(n)]\converge$, and the use is at most $u(n)$. The function $u$ is even computable: $u(n)$ can be found by testing, for $\ell = 0, 1, \dots$, whether every string of length $\ell$ satisfies $\Phi^\sigma(n)[\ell]\converge$. This is a form of uniform continuity, and the next lessons use the same argument relative to a $\Pi^0_1$ class.
:::
::::

## Notes and references

König's lemma is due to Dénes Kőnig (1927). Its restriction to binary trees, weak König's lemma, is the axiom of the system $\mathsf{WKL}_0$ of reverse mathematics (Simpson, Chapter IV). The topology of Cantor space is standard; Soare's *Turing Computability* treats open and closed classes and the compactness theorem in Sections 8.1–8.3, and Nies in Section 1.8, where :ref{#prop-closed-tree} and its dual form are Facts 1.8.3 and 1.8.4, and :ref{#ex-clopen} is Proposition 1.8.6. The derivation of compactness from weak König's lemma has a converse in reverse mathematics: over $\mathsf{RCA}_0$, weak König's lemma is equivalent to the Heine–Borel covering lemma for the unit interval (Simpson, Theorem IV.1.2).

- D. Kőnig, *Über eine Schlussweise aus dem Endlichen ins Unendliche*, Acta Scientiarum Mathematicarum (Szeged) 3 (1927), 121–130.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 8.1–8.3.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.8.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section IV.1.

:::::exercises
::::exercise{#ex-classify-open-closed difficulty=1 objective="Decide on examples whether a class of Cantor space is open, closed, both or neither."}
Identify sequences with sets of integers. For each of the following classes, decide whether it is open, closed, both or neither:

1. the class of sets with at most two elements;
2. the class of sets $X$ such that $X(n) = X(n+1) = 1$ for some $n$;
3. the class of sets all of whose elements are even;
4. the class of sets $X$ with $X(0) = 1$ or $X(5) = 0$;
5. the class of cofinite sets.

:::solution
A class is open if and only if each of its members has a prefix whose cylinder is contained in the class; so a class is not open as soon as some member has no such prefix, and not closed as soon as some non-member has every cylinder around it meeting the class.

1. *Closed, not open.* The complement is the union of the cylinders $[\sigma]$ with $\sigma$ containing three ones, so it is open. The class is not open: it contains $0^\infty$, and every cylinder $[0^n]$ contains the set $0^n 1 1 1 0^\infty$, which has three elements.
2. *Open, not closed.* It is the union of the cylinders $[\sigma]$ with $\sigma$ containing two consecutive ones. Its complement contains $0^\infty$, and every cylinder $[0^n]$ contains $0^n 1 1 0^\infty$, which is in the class; so the complement is not open.
3. *Closed, not open.* The complement is the union of the cylinders $[\sigma]$ such that $\sigma(n) = 1$ for some odd $n < |\sigma|$. The class contains $0^\infty$, and every cylinder $[0^n]$ contains the set $\{2n + 1\}$, which has an odd element.
4. *Both.* Membership depends only on the first six bits: the class is the union of the cylinders $[\sigma]$ with $|\sigma| = 6$ and $\sigma(0) = 1$ or $\sigma(5) = 0$, and its complement is the union of the other cylinders of strings of length $6$.
5. *Neither.* Every cylinder $[\sigma]$ contains the finite set $\sigma 0^\infty$, which is not cofinite, so the class contains no cylinder at all, and it is not empty: it is not open. Its complement contains $0^\infty$, and every cylinder $[0^n]$ contains the cofinite set $0^n 1^\infty$: the complement is not open.
:::
::::

::::exercise{#ex-wkl-from-compactness difficulty=1 objective="Derive weak König's lemma from the compactness of Cantor space, the converse of the proof given in the lesson."}
Assume only that every cover of $\cs$ by cylinders has a finite subcover. Deduce weak König's lemma, without using :ref{#lem-weak-konig}.

:::solution
Let $T$ be a binary tree without path; we show that $T$ is finite. Every sequence $X$ has a prefix outside $T$, since otherwise $X$ would be a path. So the cylinders $[\sigma]$ with $\sigma \notin T$ cover $\cs$, and finitely many of them, say $[\sigma_1], \dots, [\sigma_k]$ with each $\sigma_i \notin T$, already cover it; $k \geq 1$ since $\cs$ is not empty. Let $n$ be the largest length of the $\sigma_i$. Let $\tau$ be a string of length $n$, and $X$ a sequence extending $\tau$. Then $X \in [\sigma_i]$ for some $i$; the strings $\sigma_i$ and $\tau$ are both prefixes of $X$ and $|\sigma_i| \leq |\tau|$, so $\sigma_i \preceq \tau$. Since $\sigma_i \notin T$ and $T$ is closed under prefixes, $\tau \notin T$. So $T$ has no node of length $n$, hence none of length at least $n$, and $T \subseteq 2^{\leq n}$ is finite. By contraposition, an infinite binary tree has a path.
:::
::::

::::exercise{#ex-continuous-finite-range difficulty=1 objective="Apply compactness to show that a locally constant function on Cantor space depends on a bounded prefix."}
Let $f : \cs \to \nat$ be **locally constant**: every $X$ has a prefix $\sigma$ such that $f$ is constant on $[\sigma]$. Show that there is $n$ such that $f(X)$ depends only on $X \uh n$, and that $f$ takes finitely many values.

:::solution
Let $W$ be the set of strings $\sigma$ such that $f$ is constant on $[\sigma]$. By hypothesis $\cs = [W]^{\prec}$, so by :ref{#prop-cantor-compact} there are $\sigma_1, \dots, \sigma_k \in W$ with $\cs = [\sigma_1] \cup \dots \cup [\sigma_k]$. Let $n$ be the largest length of the $\sigma_i$. If $X \uh n = Y \uh n$, choose $i$ with $X \in [\sigma_i]$; then $\sigma_i \preceq X \uh n = Y \uh n$, so $Y \in [\sigma_i]$, and $f(X) = f(Y)$ since $f$ is constant on $[\sigma_i]$. The values of $f$ are its values on the $k$ cylinders $[\sigma_i]$, one on each, so there are at most $k$ of them.
:::
::::

::::exercise{#ex-closed-sequential difficulty=1 objective="Characterize the closed classes of Cantor space by limits of sequences."}
Say that a sequence $(X_k)_{k \in \nat}$ of elements of $\cs$ **converges** to $X$ if for every $n$, $X_k \uh n = X \uh n$ for all sufficiently large $k$. Show that a class $\mathcal P$ is closed if and only if the limit of every convergent sequence of members of $\mathcal P$ belongs to $\mathcal P$.

:::solution
Let $\mathcal P$ be closed, $X_k \in \mathcal P$ converging to $X$, and suppose $X \notin \mathcal P$. The complement of $\mathcal P$ is open, so it contains a cylinder $[\sigma]$ with $\sigma \prec X$. For $k$ large enough, $X_k \uh |\sigma| = X \uh |\sigma| = \sigma$, so $X_k \in [\sigma]$ is not in $\mathcal P$, a contradiction.

Conversely, suppose that $\mathcal P$ contains the limits of its convergent sequences, and let $Y \notin \mathcal P$. Some cylinder $[Y \uh n]$ is disjoint from $\mathcal P$: otherwise, choose $X_n \in [Y \uh n] \cap \mathcal P$ for every $n$; for every $m$ and every $k \geq m$, $X_k \uh m = Y \uh m$, so $(X_n)$ converges to $Y$, and $Y \in \mathcal P$, a contradiction. So the complement of $\mathcal P$ is the union of the cylinders disjoint from $\mathcal P$, which is open, and $\mathcal P$ is closed.
:::
::::

::::exercise{#ex-extendible-subtree difficulty=1 objective="Show that the extendible nodes of a tree form the least tree with the same paths."}
Let $T$ be a binary tree and $E$ the set of its extendible nodes. Show that $E$ is a tree with $[E] = [T]$, that every node of $E$ has an immediate successor in $E$, and that $E \subseteq S$ for every binary tree $S$ with $[S] = [T]$.

:::solution
If $\sigma \in E$ and $\tau \preceq \sigma$, a path through $\sigma$ also goes through $\tau$, so $\tau \in E$: $E$ is a tree. Since $E \subseteq T$, $[E] \subseteq [T]$. If $X \in [T]$, every prefix of $X$ is extendible, witnessed by $X$ itself, so $X \in [E]$. If $\sigma \in E$ and $X$ is a path through $\sigma$, then $X \uh (|\sigma| + 1)$ is an immediate successor of $\sigma$, extendible by $X$. Finally, let $S$ be a tree with $[S] = [T]$ and $\sigma \in E$; a path $X \in [T]$ through $\sigma$ belongs to $[S]$, so its prefix $\sigma$ belongs to $S$. In other words, $E$ is the tree $\{ X \uh n : X \in [T], n \in \nat \}$ of :ref{#prop-closed-tree}, and it is the least tree whose class of paths is $[T]$. Adapted from Soare 2016, Exercise 3.7.3(a).
:::
::::

::::exercise{#ex-cantor-metric difficulty=1 objective="Describe the topology of Cantor space by an ultrametric whose balls are the cylinders."}
For $X \neq Y$ in $\cs$, let $d(X, Y) = 2^{-n}$, where $n$ is the least position with $X(n) \neq Y(n)$, and let $d(X, X) = 0$. Show that $d$ is a metric satisfying $d(X, Z) \leq \max(d(X, Y), d(Y, Z))$, that the ball $\{ Y : d(X, Y) < 2^{-n} \}$ is the cylinder $[X \uh (n+1)]$, and that the open classes of :ref{#def-open-closed} are exactly the open sets of the metric $d$.

:::solution
Symmetry and $d(X, Y) = 0 \iff X = Y$ are immediate. Let $X, Y, Z$ be given, and suppose that $X$ and $Y$ agree below $n$ and $Y$ and $Z$ agree below $m$. Then $X$ and $Z$ agree below $\min(n, m)$, so $d(X, Z) \leq 2^{-\min(n, m)}$. Applying this with $n$ and $m$ the first positions of difference (or arbitrarily large if the sequences are equal) gives $d(X, Z) \leq \max(d(X, Y), d(Y, Z))$, which implies the triangle inequality.

For $Y \neq X$, $d(X, Y) < 2^{-n}$ if and only if the first difference between $X$ and $Y$ is at a position greater than $n$, that is, $X \uh (n+1) = Y \uh (n+1)$; and $Y = X$ belongs to both sets. So the ball is $[X \uh (n+1)]$.

If $\mathcal U = [W]^{\prec}$ and $X \in \mathcal U$, then $X \in [\sigma] \subseteq \mathcal U$ for some $\sigma \in W$, and the ball $[X \uh (|\sigma| + 1)]$ is contained in $[\sigma]$; so $\mathcal U$ is open for $d$. Conversely, if every $X \in \mathcal U$ has a ball $[X \uh (n_X + 1)]$ contained in $\mathcal U$, then $\mathcal U$ is the union of these cylinders.
:::
::::
:::::
