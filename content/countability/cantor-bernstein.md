---
title: The Cantor–Bernstein theorem
summary: Mutually subpotent sets are equipotent.
duration: 15
prerequisites: [equipotence]
---

The heart of the proof lies in the following lemma, which handles the special case where one set is included in the other.

:::lemma{#lem-injection-subset}
Let $B \subseteq A$ be sets, and let $f : A \to B$ be an injective function. Then there is a bijection $h : A \to B$.
:::

:::figure[The sets $C_n$: start from the elements of $A$ outside $B$, and push them forward by $f$.]
<svg viewBox="0 0 360 250" width="360" role="img" aria-label="Rectangle A with horizontal bands C0, C1, C2, C3 and arrows f between them" style="font-family: serif; font-size: 15px">
<g fill="none" stroke="currentColor" stroke-width="1.2"><rect x="60" y="10" width="220" height="230"/><line x1="60" y1="60" x2="280" y2="60"/><line x1="60" y1="95" x2="280" y2="95"/><line x1="60" y1="130" x2="280" y2="130"/><line x1="60" y1="165" x2="280" y2="165"/><line x1="60" y1="190" x2="280" y2="190" stroke-width="2"/></g>
<g fill="currentColor"><text x="120" y="40">C₀ = A ∖ B</text><text x="160" y="83">C₁</text><text x="160" y="118">C₂</text><text x="160" y="153">C₃</text><text x="160" y="182">⋮</text><text x="72" y="215" font-size="12">elements of B never reached</text><text x="72" y="230" font-size="12">from A ∖ B by iterating f</text><text x="20" y="130">A</text><text x="20" y="160" font-size="13">(B = all</text><text x="20" y="175" font-size="13">but C₀)</text></g>
<g fill="none" stroke="currentColor" stroke-width="1.2"><path d="M285 35 C 320 45, 320 70, 288 78"/><path d="M285 78 C 315 85, 315 105, 288 112"/><path d="M285 112 C 315 120, 315 140, 288 147"/></g>
<g fill="currentColor"><path d="M288 74 l-8 5 l9 3z"/><path d="M288 108 l-8 5 l9 3z"/><path d="M288 143 l-8 5 l9 3z"/><text x="322" y="60" font-style="italic">f</text><text x="318" y="100" font-style="italic">f</text><text x="318" y="134" font-style="italic">f</text></g>
</svg>
:::

:::proof{of=lem-injection-subset}
Define a sequence of sets by induction:
$$
C_0 = A \setminus B \quad\text{and}\quad C_{n+1} = f(C_n),
$$
and let $C = \bigcup_n C_n$. Define $h : A \to B$ by
$$
h(x) = \begin{cases} f(x) & \text{if } x \in C,\\ x & \text{if } x \notin C. \end{cases}
$$

*$h$ is injective.* The function $f$ is injective, so $h$ restricted to $C$ is injective. On $A \setminus C$, $h$ is the identity, hence injective. Moreover, the image of $C$ by $h$ is $\bigcup_n f(C_n) = \bigcup_n C_{n+1} \subseteq C$, while the image of $A \setminus C$ is $A \setminus C$. So $h$ is the union of two injective functions with disjoint images, hence injective.

*$h$ is surjective.* Let $y \in B$. If $y \notin C$, then $h(y) = y$. If $y \in C$, then since $y \notin C_0$, there is some $n$ with $y \in C_{n+1} = f(C_n)$: there is an $x \in C_n$ with $h(x) = f(x) = y$.
:::

:::quiz
The lemma claims $h$ maps $A$ into $B$, not just into $A$. Why is $h(x) \in B$ for every $x \in A$?

- [x] If $x \in C$ then $f(x) \in B$ because $f$ maps into $B$; if $x \notin C$ then in particular $x \notin C_0 = A \setminus B$, so $h(x) = x \in B$.

  Exactly: the elements of $A$ outside $B$ all lie in $C_0 \subseteq C$, so they are never left fixed.
- [ ] Because $B \subseteq A$.

  This inclusion goes the wrong way to conclude $h(x) \in B$.
- [ ] Because $C \subseteq B$.

  False: $C_0 = A \setminus B$ is part of $C$ and is disjoint from $B$.
- [ ] Because $f$ is injective.

  Injectivity is used for injectivity of $h$, not to locate its values.

---

Which facts does the proof use to show that $h$ is **injective**?

- [x] $f$ is injective.
- [x] $h$ sends $C$ into $C$, and $A \setminus C$ onto $A \setminus C$.

  This is what makes the images of the two pieces disjoint.
- [ ] The sets $C_0, C_1, C_2, \dots$ are pairwise disjoint.

  True (by induction, using injectivity of $f$), but the proof does not need it — the book points this out explicitly.
- [ ] $A$ is infinite.

  If $A$ is finite, $f$ injective forces $B = A$; then $C = \emptyset$ and $h$ is the identity. No case distinction is needed.

---

In the surjectivity part, why does $y \in C$ imply $y \in C_{n+1}$ for some $n$, rather than possibly $y \in C_0$?

- [x] Because $y \in B$ and $C_0 = A \setminus B$.
- [ ] Because $f$ is surjective onto $C$.

  $f$ is not assumed surjective onto anything.
- [ ] Because the $C_n$ are increasing.

  They are not increasing — in fact they are pairwise disjoint.
:::

We can now prove the theorem.

:::theorem[Cantor–Bernstein]{#thm-cantor-bernstein}
If $A$ and $B$ are sets, and $f : A \to B$ and $g : B \to A$ are injective functions, then there is a bijection between $A$ and $B$.
:::

:::proof{of=thm-cantor-bernstein}
Let $A' = g(B) \subseteq A$. The map $g \circ f$ is an injection of $A$ into $A'$. By :ref{#lem-injection-subset}, there is a bijection $h : A \to A'$. Since $g$ is a bijection between $B$ and $A'$, the function $g^{-1} \circ h : A \to B$ is a bijection.
:::

:::quiz
To which pair "$B \subseteq A$, injection $A \to B$" is the lemma applied?

- [x] The subset $g(B) \subseteq A$, with the injection $g \circ f : A \to g(B)$.

  Composing with $g$ brings everything back inside $A$, where the lemma applies.
- [ ] The set $B$ itself, with $f : A \to B$.

  The lemma requires $B \subseteq A$, which need not hold — $A$ and $B$ may be unrelated sets.
- [ ] The subset $f(A) \subseteq B$, with $g : B \to f(A)$.

  $g$ maps into $A$, not into $f(A)$.
:::

:::corollary{#cor-mutually-subpotent}
Two mutually subpotent sets are equipotent: if $|A| \leq |B|$ and $|B| \leq |A|$, then $|A| = |B|$.
:::

So the question of whether there are infinities of different sizes comes down to finding sets $A, B$ with $|A| \leq |B|$ but $|B| \nleq |A|$. Cantor's diagonal argument will provide such a pair.

::::exercise{difficulty=1}
Use the Cantor–Bernstein theorem to show that $\nat$ and $\nat \times \nat$ are equipotent, without writing down an explicit bijection.

:::solution
The map $n \mapsto (n, 0)$ is an injection $\nat \to \nat \times \nat$. Conversely, $(a, b) \mapsto 2^a 3^b$ is an injection $\nat \times \nat \to \nat$, by uniqueness of the prime factorization. By :ref{#thm-cantor-bernstein}, the two sets are equipotent.
:::
::::
