---
title: The Cantor–Bernstein theorem
summary: Two sets each injecting into the other are equipotent; explicit form of the bijection; the role of the axiom of choice.
duration: 35
prerequisites: [equipotence]
---

Subpotence is reflexive and transitive (:ref{#prop-subpotent-transitive}). This lesson proves that it is also antisymmetric: from an injection of $A$ into $B$ and an injection of $B$ into $A$, one can build a bijection between $A$ and $B$. The proof is constructive in the sense that it defines the bijection explicitly from the two injections, without any use of the axiom of choice. It is also a useful tool in practice: exhibiting two injections is often much easier than exhibiting a bijection.

## The key lemma

The proof reduces to the case where one set is a subset of the other.

:::lemma{#lem-injection-subset}
Let $B \subseteq A$ be sets, and let $f : A \to B$ be injective. Then there is a bijection $h : A \to B$.
:::

The elements of $A \setminus B$ must be sent into $B$, so they are moved by $f$. Their images may in turn be needed as images of other elements, so they are moved as well, and so on. Every other element can stay in place.

:::figure[The sets $C_n$ of the proof. The elements of $A \setminus B$ and all their iterated images form the shaded set $C$; the bijection $h$ applies $f$ on $C$ and is the identity elsewhere.]
<svg class="fig" viewBox="0 0 540 272" width="540" role="img" aria-label="The set A cut into bands C0, C1, C2, C3 and the rest; f maps each band onto the next"><defs><marker id="ah-cb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="80" y="16" width="250" height="50" class="soft-fill"/><rect x="80" y="66" width="250" height="44" class="soft-fill"/><rect x="80" y="110" width="250" height="40" class="soft-fill"/><rect x="80" y="150" width="250" height="36" class="soft-fill"/><rect x="80" y="186" width="250" height="70" class="cell"/><rect x="80" y="16" width="250" height="240" class="track-outline"/><line x1="80" y1="66" x2="330" y2="66" class="axis"/><line x1="80" y1="110" x2="330" y2="110" class="axis"/><line x1="80" y1="150" x2="330" y2="150" class="axis"/><line x1="80" y1="186" x2="330" y2="186" class="ink-stroke" stroke-width="1.2"/><text x="205.0" y="46" text-anchor="middle" class="math" font-size="17">C<tspan class="mrm" font-size="11" dy="4">0</tspan><tspan class="mrm" dy="-4"> = </tspan>A<tspan class="mrm"> ∖ </tspan>B</text><text x="205.0" y="92.0" text-anchor="middle" class="math" font-size="17">C<tspan class="mrm" font-size="11" dy="4">1</tspan></text><text x="205.0" y="134.0" text-anchor="middle" class="math" font-size="17">C<tspan class="mrm" font-size="11" dy="4">2</tspan></text><text x="205.0" y="172.0" text-anchor="middle" class="math" font-size="17">C<tspan class="mrm" font-size="11" dy="4">3</tspan></text><text x="205.0" y="200" text-anchor="middle" class="mrm muted" font-size="13">⋮</text><text x="205.0" y="226" text-anchor="middle" class="label">elements of B never reached from A ∖ B</text><text x="205.0" y="242" text-anchor="middle" class="label">by iterating f: here h is the identity</text><path d="M334,41.0 C370,47.0 370,82.0 336,88.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cb)"/><text x="368" y="69.5" class="math" font-size="15">f</text><path d="M334,88.0 C370,94.0 370,124.0 336,130.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cb)"/><text x="368" y="114.0" class="math" font-size="15">f</text><path d="M334,130.0 C370,136.0 370,162.0 336,168.0" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cb)"/><text x="368" y="154.0" class="math" font-size="15">f</text><path d="M334,168.0 C370,174.0 370,192 336,198" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-cb)"/><text x="368" y="188.0" class="math" font-size="15">f</text><text x="400" y="96" class="label">shaded: C = ⋃ Cₙ,</text><text x="400" y="112" class="label">where h = f</text><path d="M72,66 L66,66 L66,256 L72,256" class="ink-stroke" stroke-width="1.2"/><text x="58" y="166" text-anchor="end" class="math" font-size="17">B</text><path d="M42,16 L36,16 L36,256 L42,256" class="ink-stroke" stroke-width="1.2"/><text x="28" y="142" text-anchor="end" class="math" font-size="17">A</text></svg>
:::

:::proof{of=lem-injection-subset}
Define sets $C_n \subseteq A$ by induction:
$$
C_0 = A \setminus B, \qquad C_{n+1} = f(C_n),
$$
let $C = \bigcup_{n \in \nat} C_n$, and define $h : A \to A$ by
$$
h(x) = \begin{cases} f(x) & \text{if } x \in C,\\ x & \text{if } x \notin C. \end{cases}
$$

*$h$ maps $A$ into $B$.* If $x \in C$, then $h(x) = f(x) \in B$. If $x \notin C$, then in particular $x \notin C_0 = A \setminus B$, so $h(x) = x \in B$.

*$h$ is injective.* Its restriction to $C$ is $f$, which is injective, and its restriction to $A \setminus C$ is the identity. The image of $C$ is $\bigcup_n f(C_n) = \bigcup_n C_{n+1} \subseteq C$, and the image of $A \setminus C$ is $A \setminus C$. These images are disjoint, so two elements with the same image lie in the same piece, and are then equal.

*$h$ is surjective onto $B$.* Let $y \in B$. If $y \notin C$, then $h(y) = y$. If $y \in C$, then $y \in C_n$ for some $n$, and $n \neq 0$ since $y \in B$. So $y \in C_{m+1} = f(C_m)$ with $m = n - 1$: there is $x \in C_m \subseteq C$ with $h(x) = f(x) = y$.
:::

:::quiz[the proof of the lemma]
Why is $h(x) \in B$ for every $x \in A$?

- [x] If $x \in C$, then $h(x) = f(x) \in B$; if $x \notin C$, then $x \notin C_0 = A \setminus B$, so $h(x) = x \in B$.

  The elements of $A$ outside $B$ all lie in $C_0 \subseteq C$, so they are never left in place.
- [ ] Because $B \subseteq A$.

  This inclusion goes the wrong way: it shows $h(x) \in A$ only.
- [ ] Because $C \subseteq B$.

  This is false: $C_0 = A \setminus B$ is part of $C$ and disjoint from $B$.
- [ ] Because $f$ is injective.

  Injectivity of $f$ is used for injectivity of $h$, not to locate its values.

---

Which facts does the proof use to show that $h$ is injective?

- [x] $f$ is injective.
- [x] $h$ sends $C$ into $C$ and $A \setminus C$ onto $A \setminus C$.

  This makes the images of the two pieces disjoint.
- [ ] The sets $C_0, C_1, C_2, \dots$ are pairwise disjoint.

  This is true (see the exercises), but the proof does not use it.
- [ ] $A$ is infinite.

  No case distinction is needed. If $A$ is finite, $f$ injective forces $B = A$ (by :ref{#cor-finite-cardinality}), so $C = \emptyset$ and $h$ is the identity.

---

In the surjectivity part, why is $y \in C$ in some $C_{m+1}$ rather than in $C_0$?

- [x] Because $y \in B$ and $C_0 = A \setminus B$.
- [ ] Because $f$ is surjective onto $C$.

  No surjectivity of $f$ is assumed.
- [ ] Because the sets $C_n$ are increasing.

  They are not increasing; they are pairwise disjoint.
:::

:::example{#ex-cb-interval}
Let $A = [0, 1]$, $B = [0, 1) \subseteq A$ and $f(x) = x/2$, an injection of $A$ into $[0, \tfrac12] \subseteq B$. Then $C_0 = \{1\}$ and $C_n = \{2^{-n}\}$, so $C = \{1, \tfrac12, \tfrac14, \dots\}$. The bijection of the lemma is
$$
h(x) = \begin{cases} x / 2 & \text{if } x = 2^{-n} \text{ for some } n \in \nat,\\ x & \text{otherwise.} \end{cases}
$$
It shifts the sequence $1, \tfrac12, \tfrac14, \dots$ by one step, which frees the point $1$, and fixes every other point. This is the device of the first exercise of the previous lesson, applied to a copy of $\nat$ inside $[0, 1]$.
:::

## The theorem

:::theorem[Cantor–Bernstein]{#thm-cantor-bernstein}
If $f : A \to B$ and $g : B \to A$ are injections, then there is a bijection between $A$ and $B$.
:::

:::proof{of=thm-cantor-bernstein}
Let $A' = g(B) \subseteq A$. The map $g \circ f$ is an injection from $A$ into $A'$, so by :ref{#lem-injection-subset} there is a bijection $h : A \to A'$. The map $g$, seen as a function from $B$ to $A'$, is a bijection; so $g^{-1} \circ h : A \to B$ is a bijection.
:::

:::quiz[the proof of the theorem]
To which pair "$B \subseteq A$, injection of $A$ into $B$" is the lemma applied?

- [x] The subset $g(B) \subseteq A$, with the injection $g \circ f : A \to g(B)$.

  Composing with $g$ brings everything back inside $A$, where the lemma applies.
- [ ] The set $B$ itself, with $f : A \to B$.

  The lemma requires $B \subseteq A$, which need not hold: $A$ and $B$ may be unrelated sets.
- [ ] The subset $f(A) \subseteq B$, with $g : B \to f(A)$.

  The map $g$ takes values in $A$, not in $f(A)$.
:::

:::corollary{#cor-mutually-subpotent}
If $|A| \leq |B|$ and $|B| \leq |A|$, then $|A| = |B|$. Consequently, if $A \subseteq B \subseteq C$ and $|A| = |C|$, then $|A| = |B| = |C|$.
:::

:::proof{of=cor-mutually-subpotent}
The first statement is a reformulation of :ref{#thm-cantor-bernstein}. For the second, the inclusion gives $|B| \leq |C|$, and $|C| = |A| \leq |B|$ gives $|C| \leq |B|$.
:::

The second statement is often used in the following form: to show that a set $B$ has the same cardinality as a set $C$, find a subset of $B$ equipotent to $C$, and an injection of $B$ into $C$.

## The bijection, explicitly

Unfolding the two proofs gives a direct description of the bijection.

:::proposition{#prop-cb-explicit}
Let $f : A \to B$ and $g : B \to A$ be injections, and let
$$
C = \bigcup_{n \in \nat} (g \circ f)^n\big(A \setminus g(B)\big).
$$
Then the function $\varphi : A \to B$ defined by $\varphi(x) = f(x)$ for $x \in C$, and $\varphi(x) = g^{-1}(x)$ for $x \notin C$, is a bijection.
:::

:::proof{of=prop-cb-explicit}
In the proof of :ref{#thm-cantor-bernstein}, the lemma is applied to $A' = g(B)$ and to the injection $g \circ f$. Its sets are $C_0 = A \setminus g(B)$ and $C_{n+1} = (g \circ f)(C_n)$, so their union is the set $C$ of the statement, and the bijection is $g^{-1} \circ h$, where $h(x) = g(f(x))$ for $x \in C$ and $h(x) = x$ otherwise. For $x \in C$, this gives $g^{-1}(g(f(x))) = f(x)$. For $x \notin C$, it gives $g^{-1}(x)$, which is defined since $x \notin C_0$ means $x \in g(B)$.
:::

The set $C$ has a simple description. Assume for this paragraph that $A$ and $B$ are disjoint (otherwise, replace them by disjoint copies). Starting from $x \in A$, one can try to go backwards: if $x \in g(B)$, its **parent** is the unique $y \in B$ with $g(y) = x$; if $y \in f(A)$, the parent of $y$ is the unique $x' \in A$ with $f(x') = y$; and so on. Every element thus has a unique sequence of ancestors, which either stops at an element of $A \setminus g(B)$, or stops at an element of $B \setminus f(A)$, or never stops. An element $x \in A$ lies in $C$ exactly when its ancestry stops in $A \setminus g(B)$: indeed, $x \in (g \circ f)^n(A \setminus g(B))$ means that the $2n$-th ancestor of $x$ exists and lies in $A \setminus g(B)$.

So the elements of $A \cup B$ split into **chains** under $f$ and $g$, and the bijection pairs elements within each chain. On a chain starting in $A$, it must use $f$, since the first element has no preimage under $g$. On a chain starting in $B$, it must use $g^{-1}$, since the first element is not in the image of $f$. On a chain without a first element, which is either infinite in both directions or a finite cycle, both choices work, and the proof makes the choice $g^{-1}$.

:::figure[The three kinds of chains, with elements of $A$ in the top row and elements of $B$ in the bottom row. The thick arrows are the pairs $(x, \varphi(x))$ of the bijection.]
<svg class="fig" viewBox="0 0 580 250" width="580" role="img" aria-label="Three kinds of chains of f and g and how the bijection pairs their elements"><defs><marker id="ah-ch" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker><marker id="ah-chm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><text x="196" y="14" text-anchor="end" class="label">A</text><text x="196" y="54" text-anchor="end" class="label">B</text><text x="0" y="14" class="label">starts in A ∖ g(B):</text><text x="0" y="30" class="label">every element of A</text><text x="0" y="46" class="label">goes to its image by f</text><line x1="214.8" y1="13.7" x2="255.7" y2="45.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="245.0" y="34.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="266.8" y1="46.3" x2="307.7" y2="14.9" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="279.0" y="34.0" text-anchor="middle" class="math muted" font-size="12">g</text><line x1="318.8" y1="13.7" x2="359.7" y2="45.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="349.0" y="34.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="370.8" y1="46.3" x2="411.7" y2="14.9" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="383.0" y="34.0" text-anchor="middle" class="math muted" font-size="12">g</text><line x1="422.8" y1="13.7" x2="463.7" y2="45.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="453.0" y="34.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="474.8" y1="46.3" x2="515.7" y2="14.9" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="487.0" y="34.0" text-anchor="middle" class="math muted" font-size="12">g</text><circle cx="210" cy="10" r="4.5" class="ink-fill"/><circle cx="262" cy="50" r="4.5" class="node"/><circle cx="314" cy="10" r="4.5" class="ink-fill"/><circle cx="366" cy="50" r="4.5" class="node"/><circle cx="418" cy="10" r="4.5" class="ink-fill"/><circle cx="470" cy="50" r="4.5" class="node"/><circle cx="522" cy="10" r="4.5" class="ink-fill"/><text x="540" y="34" class="mrm muted" font-size="15">⋯</text><circle cx="210" cy="10" r="9" class="accent-stroke" stroke-width="1.2"/><text x="0" y="96" class="label">starts in B ∖ f(A):</text><text x="0" y="112" class="label">every element of A</text><text x="0" y="128" class="label">goes to its preimage by g</text><line x1="257.2" y1="95.7" x2="216.3" y2="127.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="227.0" y="116.0" text-anchor="middle" class="math muted" font-size="12">g⁻¹</text><line x1="266.8" y1="95.7" x2="307.7" y2="127.1" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="297.0" y="116.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="361.2" y1="95.7" x2="320.3" y2="127.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="331.0" y="116.0" text-anchor="middle" class="math muted" font-size="12">g⁻¹</text><line x1="370.8" y1="95.7" x2="411.7" y2="127.1" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="401.0" y="116.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="465.2" y1="95.7" x2="424.3" y2="127.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="435.0" y="116.0" text-anchor="middle" class="math muted" font-size="12">g⁻¹</text><line x1="474.8" y1="95.7" x2="515.7" y2="127.1" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="505.0" y="116.0" text-anchor="middle" class="math muted" font-size="12">f</text><circle cx="210" cy="132" r="4.5" class="node"/><circle cx="262" cy="92" r="4.5" class="ink-fill"/><circle cx="314" cy="132" r="4.5" class="node"/><circle cx="366" cy="92" r="4.5" class="ink-fill"/><circle cx="418" cy="132" r="4.5" class="node"/><circle cx="470" cy="92" r="4.5" class="ink-fill"/><circle cx="522" cy="132" r="4.5" class="node"/><text x="540" y="116" class="mrm muted" font-size="15">⋯</text><circle cx="210" cy="132" r="9" class="accent-stroke" stroke-width="1.2"/><text x="0" y="178" class="label">has no first element:</text><text x="0" y="194" class="label">preimage by g</text><text x="0" y="210" class="label">(the choice of the proof)</text><line x1="214.8" y1="177.7" x2="255.7" y2="209.1" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="245.0" y="198.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="309.2" y1="177.7" x2="268.3" y2="209.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="279.0" y="198.0" text-anchor="middle" class="math muted" font-size="12">g⁻¹</text><line x1="318.8" y1="177.7" x2="359.7" y2="209.1" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="349.0" y="198.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="413.2" y1="177.7" x2="372.3" y2="209.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="383.0" y="198.0" text-anchor="middle" class="math muted" font-size="12">g⁻¹</text><line x1="422.8" y1="177.7" x2="463.7" y2="209.1" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#ah-chm)"/><text x="453.0" y="198.0" text-anchor="middle" class="math muted" font-size="12">f</text><line x1="517.2" y1="177.7" x2="476.3" y2="209.1" class="accent-stroke" stroke-width="2" marker-end="url(#ah-ch)"/><text x="487.0" y="198.0" text-anchor="middle" class="math muted" font-size="12">g⁻¹</text><circle cx="210" cy="174" r="4.5" class="ink-fill"/><circle cx="262" cy="214" r="4.5" class="node"/><circle cx="314" cy="174" r="4.5" class="ink-fill"/><circle cx="366" cy="214" r="4.5" class="node"/><circle cx="418" cy="174" r="4.5" class="ink-fill"/><circle cx="470" cy="214" r="4.5" class="node"/><circle cx="522" cy="174" r="4.5" class="ink-fill"/><text x="540" y="198" class="mrm muted" font-size="15">⋯</text><text x="180" y="198" class="mrm muted" font-size="15">⋯</text></svg>
:::

This is the proof of Cantor–Bernstein usually attributed to Julius König (1906). The proof above, by iteration of a single injection, is essentially Dedekind's.

:::quiz[the explicit bijection]
Let $x \in A \setminus C$. Why is $g^{-1}(x)$ defined?

- [x] Because $A \setminus g(B) = C_0 \subseteq C$, so $x \notin C$ implies $x \in g(B)$.
- [ ] Because $g$ is a bijection from $B$ to $A$.

  It is a bijection from $B$ onto $g(B)$ only; $g(B)$ may be a proper subset of $A$.
- [ ] Because the ancestry of $x$ never stops.

  The ancestry of $x$ may also stop in $B \setminus f(A)$. In both cases $x$ has a parent in $B$, which is what is needed.

---

Let $A = B = \nat$, $f(n) = n + 1$ and $g(n) = n + 1$. What is $\varphi$?

- [x] $\varphi(n) = n + 1$ for even $n$ and $\varphi(n) = n - 1$ for odd $n$.

  Here $A \setminus g(B) = \{0\}$ and $g \circ f(n) = n + 2$, so $C$ is the set of even numbers. On $C$, $\varphi = f$; elsewhere, $\varphi = g^{-1}$, that is, $n \mapsto n - 1$.
- [ ] $\varphi(n) = n + 1$ for every $n$.

  This is not surjective: $0$ is not reached.
- [ ] $\varphi(n) = n - 1$ for every $n \geq 1$, and $\varphi(0) = 0$.

  This is not injective: $0$ and $1$ are both sent to $0$.
:::

## The role of the axiom of choice

The proof of Cantor–Bernstein uses only definitions by induction and set formation: it is a theorem of ZF, set theory without the axiom of choice. Two related statements behave differently.

- *Surjections in both directions.* If there are surjections $A \to B$ and $B \to A$, are $A$ and $B$ equipotent? With the axiom of choice, yes: each surjection has a right inverse, which is an injection in the opposite direction (:ref{#rem-right-inverse-choice}), and Cantor–Bernstein applies. Without choice, this is not provable in ZF.
- *Comparability.* For any two sets $A$ and $B$, is $|A| \leq |B|$ or $|B| \leq |A|$? Zermelo's well-ordering theorem shows that this follows from the axiom of choice, and Hartogs showed in 1915 that, conversely, comparability implies the axiom of choice. We admit both results.

In this course, the sets compared are mostly sets of integers, finite objects, sequences and real numbers, for which explicit injections are available, and no use of choice is needed except where stated.

## Exercises

::::exercise{difficulty=1}
Use the Cantor–Bernstein theorem to show that $\nat$ and $\nat \times \nat$ are equipotent, without writing down an explicit bijection.

:::solution
The map $n \mapsto (n, 0)$ is an injection $\nat \to \nat \times \nat$. Conversely, $(a, b) \mapsto 2^a 3^b$ is an injection $\nat \times \nat \to \nat$, by uniqueness of prime factorization. By :ref{#thm-cantor-bernstein}, the two sets are equipotent.
:::
::::

::::exercise{difficulty=1}
Show that $[0, 1]$, $[0, 1)$, $(0, 1)$ and $\mathbb R$ are pairwise equipotent.

:::solution
We have $(0, 1) \subseteq [0, 1) \subseteq [0, 1] \subseteq \mathbb R$, and $|(0, 1)| = |\mathbb R|$ by the example of the previous lesson. By the second part of :ref{#cor-mutually-subpotent}, applied twice, all four sets are equipotent.
:::
::::

::::exercise{difficulty=2}
Let $E$ be the set of even numbers, $f : \nat \to E$ given by $f(n) = 4n$, and $g : E \to \nat$ the inclusion. Compute the bijection $\varphi$ of :ref{#prop-cb-explicit}.

:::solution
Write $v(x)$ for the exponent of $2$ in $x \geq 1$. Here $\nat \setminus g(E)$ is the set of odd numbers and $g \circ f(n) = 4n$, so $C$ is the set of numbers $4^k m$ with $m$ odd, that is, the $x \geq 1$ with $v(x)$ even. Hence $\varphi(x) = 4x$ if $x \geq 1$ and $v(x)$ is even, and $\varphi(x) = x$ otherwise, that is, for $x = 0$ and for $v(x)$ odd. One checks directly that $\varphi$ is a bijection onto $E$: the even numbers $x \geq 2$ with $v(x)$ odd are fixed, together with $0$, and those with $v(x) \geq 2$ even are the images $4y$ of the $y$ with $v(y)$ even.
:::
::::

::::exercise{difficulty=2}
In the proof of :ref{#lem-injection-subset}, show that the sets $C_n$ are pairwise disjoint.

:::solution
For $n \geq 1$, $C_n \subseteq f(A) \subseteq B$, so $C_n$ is disjoint from $C_0 = A \setminus B$. Suppose $C_m \cap C_n \neq \emptyset$ with $m < n$, and choose such a pair with $m$ minimal. Then $m \geq 1$ by the first remark. Let $y \in C_m \cap C_n$: there are $x \in C_{m-1}$ and $x' \in C_{n-1}$ with $f(x) = f(x') = y$, hence $x = x'$ by injectivity, and $C_{m-1} \cap C_{n-1} \neq \emptyset$, contradicting the minimality of $m$.
:::
::::

## Notes and references

The theorem was stated by Cantor, who could prove it only using the comparability of cardinals. Dedekind found a proof in 1887 but did not publish it. Schröder published a proof in 1898 that turned out to contain a gap, and the first published correct proof, by Felix Bernstein, appeared in Borel's *Leçons sur la théorie des fonctions* (1898). The proof by chains is due to Julius König. Hartogs' theorem on comparability is proved in Jech's monograph.

- E. Borel, *Leçons sur la théorie des fonctions*, Gauthier-Villars, Paris, 1898, Note I.
- J. König, *Sur la théorie des ensembles*, Comptes rendus de l'Académie des sciences 143 (1906), 110–112.
- F. Hartogs, *Über das Problem der Wohlordnung*, Mathematische Annalen 76 (1915), 438–443.
- T. Jech, *The Axiom of Choice*, North-Holland, 1973.
