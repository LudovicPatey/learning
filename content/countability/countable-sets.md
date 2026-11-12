---
title: Countable sets
summary: Characterizations of countable sets by injections into ℕ and by listings with repetitions; subsets of ℕ; every infinite set has a countably infinite subset.
duration: 35
prerequisites: [cantor-bernstein]
---

A set is countable when its elements can be listed in a sequence indexed by integers. Countable sets are the natural setting of computation: inputs, outputs and programs are finite objects, and there are countably many of them. This lesson characterizes countable sets in several equivalent ways, all of which reduce to one fact: every set of integers can be listed in increasing order. It then shows that $\nat$ is the smallest infinite set, a statement which, unlike the others, uses a form of the axiom of choice. The next lesson applies the characterizations to the sets built from integers by finite means.

## Definition and characterizations

:::definition{#def-countable}
A set $A$ is **countably infinite** if $|A| = |\nat|$. It is **countable** if it is finite or countably infinite, and **uncountable** otherwise.
:::

A bijection $e : \nat \to A$ is an **enumeration without repetition** of $A$, and is often written as a sequence $a_0, a_1, a_2, \dots$ with $a_n = e(n)$.

:::example{#ex-countable-sets}
1. The sets $\nat$, $\nat \setminus \{0\}$, the even numbers and the squares are countably infinite, by :ref{#ex-equipotent-sets}.
2. Every finite set is countable, and so is $\emptyset$.
3. The set $\mathbb Z$ is countably infinite: the sequence $0, -1, 1, -2, 2, -3, 3, \dots$ lists each integer exactly once. In formulas, $z \mapsto 2z$ for $z \geq 0$ and $z \mapsto -2z - 1$ for $z < 0$ is a bijection $\mathbb Z \to \nat$.
4. The set $\cs$ of infinite binary sequences, and the set $\mathbb R$, are uncountable. This is the diagonal argument of the lesson after next.
:::

The definition asks for a bijection, which is often inconvenient to write down. The characterizations below show that an injection into $\nat$, or a listing with repetitions, suffices. The basic fact behind all of them is that the subsets of $\nat$ are countable: an infinite set of integers can be listed in increasing order, by taking at each step the least element not yet listed.

:::lemma{#lem-subsets-of-n}
Every infinite set $S \subseteq \nat$ is countably infinite. More precisely, the **principal function** $p_S : \nat \to S$ defined by
$$
p_S(0) = \min S, \qquad p_S(n+1) = \min \{ s \in S : s > p_S(n) \}
$$
is a strictly increasing bijection, which enumerates $S$ in increasing order.
:::

:::proof{of=lem-subsets-of-n}
The minima exist. Indeed $S \neq \emptyset$; and if $S$ had no element greater than $p_S(n)$, then $S \subseteq \underline{p_S(n) + 1}$ would be finite, as a subset of a finite set (:ref{#ex-subset-finite}). By construction $p_S$ is strictly increasing, hence injective, and by induction $p_S(n) \geq n$ for all $n$.

For surjectivity, let $s \in S$. The values $p_S(0) < p_S(1) < \dots$ are unbounded since $p_S(n) \geq n$, so there is a least $n$ with $p_S(n) \geq s$. If $n = 0$, then $s \geq \min S = p_S(0)$ gives $s = p_S(0)$. If $n > 0$, then $p_S(n-1) < s \leq p_S(n)$, and $p_S(n)$ is by definition the least element of $S$ above $p_S(n-1)$, so $p_S(n) \leq s$, hence $s = p_S(n)$.
:::

:::proposition{#prop-countable-characterizations}
For every set $A$, the following are equivalent.

1. $A$ is countable.
2. $|A| \leq |\nat|$: there is an injection from $A$ into $\nat$.
3. $A = \emptyset$, or there is a surjection from $\nat$ onto $A$.
:::

:::proof{of=prop-countable-characterizations}
(1 ⇒ 2) A bijection with $\underline n \subseteq \nat$ or with $\nat$ is an injection into $\nat$.

(2 ⇒ 3) Suppose $A \neq \emptyset$, fix $a_0 \in A$, and let $i : A \to \nat$ be an injection. Define $s : \nat \to A$ by $s(n) = a$ if $n = i(a)$, which determines $a$ uniquely, and $s(n) = a_0$ if $n \notin i(A)$. Then $s(i(a)) = a$ for every $a$, so $s$ is surjective.

(3 ⇒ 2) The empty set injects into $\nat$. If $s : \nat \to A$ is surjective, then $|A| \leq |\nat|$ by :ref{#prop-surjection-subpotent}: the injection sends $a$ to the least $n$ with $s(n) = a$.

(2 ⇒ 1) If $i : A \to \nat$ is injective, then $A$ is equipotent to $S = i(A) \subseteq \nat$. If $S$ is finite, so is $A$. Otherwise $S$ is countably infinite by :ref{#lem-subsets-of-n}, and so is $A$.
:::

Characterization 3 is the one used most often: a non-empty set is countable when it can be listed as $a_0, a_1, a_2, \dots$, **repetitions allowed**. Removing the repetitions is done by the proof, by keeping only the first occurrence of each element.

:::figure[A listing $s$ of a set $A$, with repetitions. Each element is sent to the position of its first occurrence, shaded; this is the injection $a \mapsto \min s^{-1}(\{a\})$ of the proof of (3 ⇒ 2).]
<svg class="fig" viewBox="0 0 520 200" width="520" role="img" aria-label="A listing with repetitions; the first occurrence of each element is shaded and each element points to it"><defs><marker id="ah-fo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="66" y="28" text-anchor="end" class="math" font-size="16">n</text><text x="66" y="66" text-anchor="end" class="math" font-size="16">s<tspan class="mrm">(</tspan>n<tspan class="mrm">)</tspan></text><text x="100.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">0</text><rect x="80" y="40" width="40" height="40" class="cell head-cell"/><text x="100.0" y="66" text-anchor="middle" class="math" font-size="17">a</text><text x="140.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">1</text><rect x="120" y="40" width="40" height="40" class="cell head-cell"/><text x="140.0" y="66" text-anchor="middle" class="math" font-size="17">b</text><text x="180.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">2</text><rect x="160" y="40" width="40" height="40" class="cell"/><text x="180.0" y="66" text-anchor="middle" class="math muted" font-size="17">a</text><text x="220.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">3</text><rect x="200" y="40" width="40" height="40" class="cell head-cell"/><text x="220.0" y="66" text-anchor="middle" class="math" font-size="17">c</text><text x="260.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">4</text><rect x="240" y="40" width="40" height="40" class="cell"/><text x="260.0" y="66" text-anchor="middle" class="math muted" font-size="17">b</text><text x="300.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">5</text><rect x="280" y="40" width="40" height="40" class="cell head-cell"/><text x="300.0" y="66" text-anchor="middle" class="math" font-size="17">d</text><text x="340.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">6</text><rect x="320" y="40" width="40" height="40" class="cell"/><text x="340.0" y="66" text-anchor="middle" class="math muted" font-size="17">a</text><text x="380.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">7</text><rect x="360" y="40" width="40" height="40" class="cell head-cell"/><text x="380.0" y="66" text-anchor="middle" class="math" font-size="17">e</text><text x="420.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">8</text><rect x="400" y="40" width="40" height="40" class="cell"/><text x="420.0" y="66" text-anchor="middle" class="math muted" font-size="17">c</text><text x="460.0" y="28" text-anchor="middle" class="mrm muted" font-size="12">9</text><rect x="440" y="40" width="40" height="40" class="cell head-cell"/><text x="460.0" y="66" text-anchor="middle" class="math" font-size="17">f</text><text x="488" y="66" class="mrm muted" font-size="16">⋯</text><text x="66" y="166" text-anchor="end" class="math" font-size="16">A</text><circle cx="100" cy="160" r="14" class="node"/><text x="100" y="166" text-anchor="middle" class="math" font-size="17">a</text><line x1="100.0" y1="145.0" x2="100.0" y2="83.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/><circle cx="172" cy="160" r="14" class="node"/><text x="172" y="166" text-anchor="middle" class="math" font-size="17">b</text><line x1="166.4" y1="146.1" x2="141.1" y2="82.8" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/><circle cx="244" cy="160" r="14" class="node"/><text x="244" y="166" text-anchor="middle" class="math" font-size="17">c</text><line x1="239.7" y1="145.6" x2="220.9" y2="82.9" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/><circle cx="316" cy="160" r="14" class="node"/><text x="316" y="166" text-anchor="middle" class="math" font-size="17">d</text><line x1="313.1" y1="145.3" x2="300.6" y2="82.9" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/><circle cx="388" cy="160" r="14" class="node"/><text x="388" y="166" text-anchor="middle" class="math" font-size="17">e</text><line x1="386.5" y1="145.1" x2="380.3" y2="83.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/><circle cx="460" cy="160" r="14" class="node"/><text x="460" y="166" text-anchor="middle" class="math" font-size="17">f</text><line x1="460.0" y1="145.0" x2="460.0" y2="83.0" class="accent-stroke" stroke-width="1.3" marker-end="url(#ah-fo)"/><text x="486" y="166" class="mrm muted" font-size="16">⋯</text></svg>
:::

:::corollary{#cor-subset-countable}
1. Every subset of a countable set is countable.
2. The image of a countable set under any function is countable.
:::

:::proof{of=cor-subset-countable}
1. If $B \subseteq A$ and $i : A \to \nat$ is injective, the restriction of $i$ to $B$ is injective.
2. Let $f$ be a function defined on a countable set $A$. If $A = \emptyset$, then $f(A) = \emptyset$. Otherwise, if $s : \nat \to A$ is surjective, then $f \circ s$ is a surjection from $\nat$ onto $f(A)$.
:::

:::quiz[the principal function of a set of integers]
In the proof of :ref{#lem-subsets-of-n}, where is the hypothesis "$S$ is infinite" used?

- [x] To guarantee that $S$ has elements above $p_S(n)$, so that $p_S(n+1)$ is defined.

  For a finite set, the construction stops after $|S|$ steps, and produces a bijection with $\underline{|S|}$ instead.
- [ ] To prove that $p_S$ is injective.

  Injectivity comes from $p_S$ being strictly increasing, which holds as long as it is defined.
- [ ] To prove that $p_S(n) \geq n$.

  This follows by induction from strict increase alone.

---

In the step (3 ⇒ 2) of :ref{#prop-countable-characterizations}, why is no axiom of choice needed to invert the surjection $s$?

- [x] The preimages $s^{-1}(\{a\})$ are non-empty sets of integers, which have least elements.

  The least element is a definite choice, made uniformly for all $a$.
- [ ] Because $A$ is countable.

  That is what is being proved.
- [ ] Because every surjection has a right inverse.

  For arbitrary sets, this statement is the axiom of choice itself.
:::

## The smallest infinity

The finite sets are those that can be exhausted in finitely many steps. An infinite set can therefore never be exhausted: whatever finitely many elements have been taken from it, an element remains. Taking elements one at a time, forever, gives a copy of $\nat$ inside the set.

:::proposition{#prop-n-smallest}
Every infinite set $A$ satisfies $|\nat| \leq |A|$.
:::

:::proof{of=prop-n-smallest}
We define an injection $a : \nat \to A$ by induction. Pick $a_0 \in A$, which exists since $\emptyset$ is finite. Having chosen pairwise distinct $a_0, \dots, a_n$, the set $\{a_0, \dots, a_n\}$ is finite, so it is not $A$; pick $a_{n+1} \in A \setminus \{a_0, \dots, a_n\}$. The elements $a_n$ are pairwise distinct by construction.
:::

This proof makes infinitely many arbitrary choices, one at each step, each depending on the previous ones. It uses the **axiom of dependent choice**, a weak form of the axiom of choice, and cannot be carried out in ZF alone: it is consistent with ZF that some infinite set of real numbers has no countably infinite subset (we admit this result of Cohen; a proof is in Jech's monograph on the axiom of choice). When $A$ comes with an injection into $\nat$ or with a linear order in which every non-empty subset has a least element, one can take $a_{n+1}$ to be the least element of $A \setminus \{a_0, \dots, a_n\}$, and no choice is needed; this is what :ref{#lem-subsets-of-n} does.

:::corollary{#cor-countably-infinite-minimal}
An infinite set is countable if and only if it is equipotent to each of its infinite subsets.
:::

:::proof{of=cor-countably-infinite-minimal}
If $A$ is countably infinite and $B \subseteq A$ is infinite, then $B$ is countable by :ref{#cor-subset-countable}, and infinite, so $|B| = |\nat| = |A|$. Conversely, if $A$ is infinite and equipotent to each of its infinite subsets, then by :ref{#prop-n-smallest} it has a subset $a(\nat)$ equipotent to $\nat$, and $|A| = |a(\nat)| = |\nat|$.
:::

## Exercises

::::exercise{difficulty=1}
Let $s : \nat \to A$ be a surjection onto an infinite set $A$. Construct an explicit bijection between $\nat$ and $A$, without appealing to :ref{#prop-n-smallest}.

:::solution
Let $S = \{ n : s(n) \neq s(m) \text{ for all } m < n \}$ be the set of positions of first occurrences. The restriction of $s$ to $S$ is a bijection from $S$ onto $A$: it is surjective, since each $a \in A$ has a least $n$ with $s(n) = a$, and this $n$ is in $S$; it is injective, since two first occurrences of the same element would be equal. $S$ is infinite since $A$ is. So $s \circ p_S : \nat \to A$ is a bijection, where $p_S$ is the principal function of :ref{#lem-subsets-of-n}.
:::
::::

::::exercise{#ex-dedekind-infinite difficulty=2}
Show that a set $A$ is infinite if and only if it is equipotent to a proper subset of itself. Which direction uses the axiom of choice?

:::solution
If $A$ is finite, it is not equipotent to a proper subset, by :ref{#cor-finite-cardinality}. Conversely, if $A$ is infinite, let $a : \nat \to A$ be an injection, given by :ref{#prop-n-smallest}. The map $h$ defined by $h(a_n) = a_{n+1}$ and $h(x) = x$ for $x \notin a(\nat)$ is a bijection from $A$ onto $A \setminus \{a_0\}$. Only the second direction uses choice, through :ref{#prop-n-smallest}.
:::
::::

::::exercise{difficulty=1}
Let $A$ be countably infinite and $F \subseteq A$ finite. Show that $A \setminus F$ is countably infinite.

:::solution
By :ref{#cor-subset-countable}, $A \setminus F$ is countable. It is infinite: otherwise $A = (A \setminus F) \cup F$ would be a union of two finite sets, hence finite (if $\beta : A \setminus F \to \underline m$ and $\gamma : F \to \underline k$ are bijections, then $x \mapsto \beta(x)$ on $A \setminus F$ and $x \mapsto m + \gamma(x)$ on $F$ is a bijection onto $\underline{m + k}$, the two pieces being disjoint).
:::
::::

::::exercise{difficulty=2}
Let $A$ be infinite and $B$ countable. Show that $|A \cup B| = |A|$. Where is the axiom of choice used?

:::solution
Replacing $B$ by $B \setminus A$, which is countable by :ref{#cor-subset-countable}, we may assume $A \cap B = \emptyset$. Let $a : \nat \to A$ be an injection, given by :ref{#prop-n-smallest}, and write $a_n = a(n)$. If $B$ is countably infinite, let $b_0, b_1, \dots$ enumerate it without repetition, and define $h : A \cup B \to A$ by $h(b_k) = a_{2k}$, $h(a_n) = a_{2n+1}$, and $h(x) = x$ for $x \in A \setminus a(\nat)$. If $B = \{b_0, \dots, b_{m-1}\}$ is finite, with distinct $b_k$, let instead $h(b_k) = a_k$ for $k < m$ and $h(a_n) = a_{n+m}$. In both cases $h$ is injective on each of the three pieces $B$, $a(\nat)$ and $A \setminus a(\nat)$, and their images are disjoint and cover $A$; so $h$ is a bijection. Choice is used only through :ref{#prop-n-smallest}. This generalizes :ref{#ex-add-point}, where $B$ is a singleton and the injection $a$ is given.
:::
::::

## Notes and references

Characterizations of countable sets by injections and surjections are standard; Monin and Patey (chapter *Cantor's infinity*, section *Countable sets*) and Hrbacek and Jech give them with the same proofs. That every infinite set is Dedekind-infinite cannot be proved in ZF: in Cohen's basic model of ZF, there is an infinite set of real numbers without a countably infinite subset. Jech's monograph on the axiom of choice proves this, and studies the weak forms of choice used in this lesson (countable choice, dependent choice).

- R. Dedekind, *Was sind und was sollen die Zahlen?*, Vieweg, Braunschweig, 1888.
- T. Jech, *The Axiom of Choice*, North-Holland, 1973.
- K. Hrbacek and T. Jech, *Introduction to Set Theory*, 3rd edition, Marcel Dekker, 1999.
- B. Monin and L. Patey, *Computability theory*, chapter *Cantor's infinity*.
