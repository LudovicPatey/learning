---
title: Equipotence and subpotence
summary: Equipotence and subpotence of sets, defined by bijections and injections.
duration: 10
---

In his *Dialogues Concerning Two New Sciences*, Galileo observes a paradox. Every integer is the root of exactly one square, and every square has exactly one root — so there should be "as many" squares as integers. Yet the squares form a strict part of the integers, so there should be fewer of them. Galileo concluded that one cannot meaningfully compare the sizes of infinite quantities.

Cantor took the opposite view: keep the first intuition — matching elements one-to-one — as the *definition* of having the same size, and accept that the second intuition simply fails for infinite sets.

## Equipotence

Recall that a function $f : A \to B$ is *injective* if $x \neq y$ implies $f(x) \neq f(y)$, *surjective* if its image is the whole of $B$, and *bijective* if it is both.

:::definition{#def-equipotent}
Two sets $A$ and $B$ are **equipotent** if there is a bijection between them. We then write $|A| = |B|$.
:::

:::figure[Galileo's matching between the integers and the squares.]
<svg viewBox="0 0 320 150" width="320" role="img" aria-label="Arrows from 0,1,2,3 to 0,1,4,9" style="font-family: serif; font-size: 15px">
<g fill="currentColor"><text x="40" y="30">0</text><text x="40" y="60">1</text><text x="40" y="90">2</text><text x="40" y="120">3</text><text x="40" y="145">⋮</text><text x="262" y="30">0</text><text x="262" y="60">1</text><text x="262" y="90">4</text><text x="262" y="120">9</text><text x="262" y="145">⋮</text></g>
<g stroke="currentColor" stroke-width="1.3" fill="none"><path d="M58 25 H250"/><path d="M58 55 H250"/><path d="M58 85 H250"/><path d="M58 115 H250"/></g>
<g fill="currentColor"><path d="M250 21 l8 4 l-8 4z"/><path d="M250 51 l8 4 l-8 4z"/><path d="M250 81 l8 4 l-8 4z"/><path d="M250 111 l8 4 l-8 4z"/></g>
<text x="12" y="12" fill="currentColor" font-size="12">integers</text><text x="250" y="12" fill="currentColor" font-size="12">squares</text>
</svg>
:::

By this definition, $\nat$ and the set of squares $\{n^2 : n \in \nat\}$ are equipotent, via $n \mapsto n^2$. The paradox dissolves: the intuition that a strict subset has fewer elements is true for finite sets, and false for infinite ones.

:::remark
The notation $|A| = |B|$ suggests an equality between two objects $|A|$ and $|B|$, the *cardinalities* of $A$ and $B$. One can give a precise definition of $|A|$ as a mathematical object, but we will not need it: the statement $|A| = |B|$ is perfectly well defined on its own.
:::

:::quiz
Which of these functions witness that $\nat$ and the set $E = \{0, 2, 4, \dots\}$ of even numbers are equipotent?

- [x] $n \mapsto 2n$, from $\nat$ to $E$.

  Injective, and every even number $2k$ is the image of $k$.
- [ ] $n \mapsto n + 2$, from $\nat$ to $E$.

  This does not even map into $E$: $1 \mapsto 3$.
- [x] $m \mapsto m/2$, from $E$ to $\nat$.

  It is the inverse of $n \mapsto 2n$, hence also a bijection. A bijection in either direction is enough.
- [ ] $n \mapsto 4n$, from $\nat$ to $E$.

  Injective, but not surjective: $2$ is not of the form $4n$. It only shows that $\nat$ is *at most* as big as $E$ — see below.
:::

## Subpotence

Intuitively, $B$ is at least as big as $A$ if each element of $A$ can be given its own representative in $B$.

:::definition{#def-subpotent}
A set $A$ is **subpotent** to a set $B$ if there is an injection from $A$ into $B$. We then write $|A| \leq |B|$, and $|A| \nleq |B|$ otherwise.
:::

:::proposition{#prop-subpotent-transitive}
If $|A| \leq |B|$ and $|B| \leq |C|$, then $|A| \leq |C|$.
:::

:::proof{of=prop-subpotent-transitive}
Let $f : A \to B$ and $g : B \to C$ be injections. If $x \neq y$ are in $A$, then $f(x) \neq f(y)$ by injectivity of $f$, hence $g(f(x)) \neq g(f(y))$ by injectivity of $g$. So $g \circ f : A \to C$ is an injection.
:::

:::quiz
Suppose now that $f : A \to B$ is only **surjective** and $g : B \to C$ is injective. Which conclusion is justified?

- [ ] $g \circ f$ is an injection, so $|A| \leq |C|$.

  The first step of the proof breaks: from $x \neq y$ we can no longer deduce $f(x) \neq f(y)$.
- [ ] $g \circ f$ is a bijection between $A$ and $C$.

  $g$ need not be surjective, and $g \circ f$ need not be injective.
- [x] Nothing in this proof gives a relation between $|A|$ and $|C|$.

  Right: the argument uses injectivity of *both* maps. (In fact, with the axiom of choice a surjection $A \to B$ yields an injection $B \to A$, but that is a different argument.)
:::

Transitivity is easy. What is much less clear is **antisymmetry**: if $|A| \leq |B|$ and $|B| \leq |A|$, do we have $|A| = |B|$? Unrolling the definitions: given an injection from $A$ into $B$ and another from $B$ into $A$, can we build a *bijection*? The answer is yes — this is the :ref{#thm-cantor-bernstein}, proved in the next lesson.
