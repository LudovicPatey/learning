---
title: Designing a notion of forcing
summary: How a notion of forcing for a Ramsey-type problem is designed, on the example of the Erdős–Moser theorem; extendibility and block extendibility of the stems; the forcing question over all partitions of the reservoir.
duration: 45
prerequisites: [custom-properties, avoidance/seetapun-forcing]
---

The notions of forcing of the previous courses were given ready-made, with clauses whose role appeared only in the proofs. This lesson explains how such a notion is designed, on the Erdős–Moser theorem, in three steps. **Extendibility**: the reservoir guarantees that the stem extends to an infinite solution. **Block extendibility**: the invariant survives the addition of finite blocks, as forcing questions require. **Computational properties**: the reservoirs are weak, in a class closed under the operations performed on them; this step is in the next lesson.

## Tournaments and the Erdős–Moser theorem

:::definition{#def-sd-tournament}
A **tournament** on a set $D \subseteq \nat$ is a relation $T \subseteq D^2$ such that for all $a \neq b$ in $D$, exactly one of $T(a, b)$ and $T(b, a)$ holds, and $T(a, a)$ never holds. A set $F \subseteq D$ is **$T$-transitive** if $T(a, b)$ and $T(b, c)$ imply $T(a, c)$ for all $a, b, c \in F$. The **Erdős–Moser theorem** $\mathsf{EM}$ is the problem whose instances are the tournaments on $\nat$, and whose solutions are the infinite $T$-transitive sets.
:::

Read $T(a, b)$ as "$a$ beats $b$". A **3-cycle** is a set $\{ a, b, c \}$ with $T(a, b)$, $T(b, c)$ and $T(c, a)$. A set is $T$-transitive if and only if it contains no 3-cycle: if $T(a, b)$ and $T(b, c)$ but not $T(a, c)$, then $a \neq c$ and $T(c, a)$. On a transitive set, $T$ is a strict linear order, and subsets of transitive sets are transitive.

:::proposition{#prop-sd-em-rt22}
$\mathsf{EM} \leq_{sc} \mathsf{RT}^2_2$: every tournament $T$ computes a coloring $f : [\nat]^2 \to 2$ all of whose infinite homogeneous sets are $T$-transitive.
:::

:::proof{of=prop-sd-em-rt22}
For $a < b$, let $f(\{ a, b \}) = 1$ if $T(a, b)$ and $0$ otherwise. On a set homogeneous for color $1$, $T$ coincides with the order $<$ of $\nat$; on a set homogeneous for color $0$, with its reverse. Both are transitive.
:::

The classical proofs of $\mathsf{EM}$ go through this reduction. The notion of forcing below builds transitive sets directly; it shows that the reduction cannot be reversed (:ref{to="separation-design/erdos-moser-separation"}).

Fix a $Z$-computable tournament $T$ and a class $\mathcal M$ of possible reservoirs. As in the previous courses, a string $\sigma$ is identified with the finite set $\{ n < |\sigma| : \sigma(n) = 1 \}$, and a string $\tau$ is **compatible** with a pair $(\sigma, X)$ if $\sigma \preceq \tau$ and the new elements of $\tau$ belong to $X$. Sentences are built with functionals of the oracle $Z \oplus G$, and $\tau$ **satisfies** $\Phi^{Z \oplus G}_a\converge$ if $\Phi^{Z \oplus \tau}_a\converge$.

## Step 1: extendibility

Start from Mathias conditions $(\sigma, X)$ with a transitive stem. The set built may be finite: if $\{ a, b, z \}$ is a 3-cycle for some $a, b \in \sigma$ and almost every $z \in X$, no element can be added. The criterion for the right invariant is the classical theorem itself: $\mathsf{EM}$ inside $X$ gives an infinite transitive $Y \subseteq X$; what prevents $\sigma \cup Y$ from being transitive? A 3-cycle in $\sigma \cup Y$ cannot lie inside $\sigma$ or inside $Y$; two cases remain.

- **One element in $\sigma$, two in $Y$.** It is avoided if every $a \in \sigma$ beats every reservoir element, or is beaten by every one. This is obtained for free, by restricting the reservoir for each $a \in \sigma$ in turn to whichever of $\{ y \in X : T(a, y) \}$ and $\{ y \in X : T(y, a) \}$ is infinite: an **optional** property.
- **Two elements in $\sigma$, one in $Y$.** No restriction helps if almost every $z \in X$ closes a 3-cycle with two elements of $\sigma$. It must be **required**: every reservoir element is a one-point extension of the stem.

:::definition{#def-sd-em-condition}
An **$\mathsf{EM}$ condition** for $T$ with reservoirs in $\mathcal M$ is a pair $(\sigma, X)$ with $X \in \mathcal M$ infinite, $\min X \geq |\sigma|$, such that:

(a) every $a \in \sigma$ satisfies $T(a, y)$ for all $y \in X$, or $T(y, a)$ for all $y \in X$;

(b) $\sigma \cup \{ y \}$ is $T$-transitive for every $y \in X$.

The condition $(\tau, Y)$ **extends** $(\sigma, X)$ if $\tau$ is compatible with $(\sigma, X)$ and $Y \subseteq X$. The **members** of $(\sigma, X)$ are the $T$-transitive sets $G$ with $\sigma \preceq G$ whose elements beyond $|\sigma|$ belong to $X$.
:::

By (b), $\sigma$ is transitive. Both properties pass to subsets of the reservoir. If $d$ extends $c$, the members of $d$ are members of $c$.

:::figure[An $\mathsf{EM}$ condition. Arcs: the order of $T$ on the transitive stem ($a_1$ beats $a_2$, and so on). Each stem element beats every reservoir element (arrow down) or is beaten by every one (arrow up): property (a). Property (b) then requires the elements beating the reservoir to come first in the stem; with the pattern down, up, down, $a_2$, $a_3$ and any $y \in X$ would form a 3-cycle.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="An Erdős–Moser condition: four stem elements above a reservoir; the first two stem elements beat every reservoir element, the last two are beaten by every reservoir element"><defs><marker id="sd-em-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="40" y="64" class="label">stem σ</text><circle cx="120" cy="60" r="14" class="state"/><text x="120" y="65" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="3">1</tspan></text><circle cx="220" cy="60" r="14" class="state"/><text x="220" y="65" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="3">2</tspan></text><circle cx="320" cy="60" r="14" class="state"/><text x="320" y="65" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="3">3</tspan></text><circle cx="420" cy="60" r="14" class="state"/><text x="420" y="65" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="3">4</tspan></text><path d="M130,46 Q170.0,18 210,46" fill="none" class="muted-stroke" stroke-width="1.1" marker-end="url(#sd-em-arr)"/><path d="M230,46 Q270.0,18 310,46" fill="none" class="muted-stroke" stroke-width="1.1" marker-end="url(#sd-em-arr)"/><path d="M330,46 Q370.0,18 410,46" fill="none" class="muted-stroke" stroke-width="1.1" marker-end="url(#sd-em-arr)"/><rect x="80" y="150" width="400" height="56" rx="10" class="cell"/><text x="40" y="184" class="label">X</text><circle cx="100" cy="178" r="3.5" class="accent-fill"/><circle cx="124" cy="178" r="3.5" class="accent-fill"/><circle cx="148" cy="178" r="3.5" class="accent-fill"/><circle cx="172" cy="178" r="3.5" class="accent-fill"/><circle cx="196" cy="178" r="3.5" class="accent-fill"/><circle cx="220" cy="178" r="3.5" class="accent-fill"/><circle cx="244" cy="178" r="3.5" class="accent-fill"/><circle cx="268" cy="178" r="3.5" class="accent-fill"/><circle cx="292" cy="178" r="3.5" class="accent-fill"/><circle cx="316" cy="178" r="3.5" class="accent-fill"/><circle cx="340" cy="178" r="3.5" class="accent-fill"/><circle cx="364" cy="178" r="3.5" class="accent-fill"/><circle cx="388" cy="178" r="3.5" class="accent-fill"/><circle cx="412" cy="178" r="3.5" class="accent-fill"/><circle cx="436" cy="178" r="3.5" class="accent-fill"/><circle cx="460" cy="178" r="3.5" class="accent-fill"/><line x1="120" y1="76" x2="120" y2="146" class="ink-stroke" stroke-width="1.4" marker-end="url(#sd-em-arr)"/><line x1="220" y1="76" x2="220" y2="146" class="ink-stroke" stroke-width="1.4" marker-end="url(#sd-em-arr)"/><line x1="320" y1="148" x2="320" y2="78" class="ink-stroke" stroke-width="1.4" marker-end="url(#sd-em-arr)"/><line x1="420" y1="148" x2="420" y2="78" class="ink-stroke" stroke-width="1.4" marker-end="url(#sd-em-arr)"/><text x="500" y="110" class="label">arrow down:</text><text x="500" y="126" class="label">beats all of X</text><text x="500" y="150" class="label">arrow up:</text><text x="500" y="166" class="label">beaten by all</text><text x="80" y="234" class="label">(b): for every y ∈ X, the set σ ∪ {y} contains no 3-cycle</text></svg>
:::

The optional property is what makes the required one survive the addition of an element.

:::lemma{#lem-sd-em-extension}
Let $(\sigma, X)$ be an $\mathsf{EM}$ condition and $x \in X$. Let $\tau = \sigma \cup \{ x \}$, a string of length $x + 1$, and let $Y$ be the set of $y \in X$ with $y > x$ and $T(x, y)$ if this set is infinite, and the set of $y \in X$ with $y > x$ and $T(y, x)$ otherwise. If $Y \in \mathcal M$, then $(\tau, Y)$ is an $\mathsf{EM}$ condition extending $(\sigma, X)$.
:::

:::proof{of=lem-sd-em-extension}
The set $Y$ is infinite and $\min Y > x$. Property (a) holds for the elements of $\sigma$ since $Y \subseteq X$, and for $x$ by the choice of $Y$. For (b), let $y \in Y$ and suppose that $\sigma \cup \{ x, y \}$ contains a 3-cycle. By (b) for $(\sigma, X)$, the sets $\sigma \cup \{ x \}$ and $\sigma \cup \{ y \}$ are transitive, so the cycle contains $x$, $y$ and some $a \in \sigma$. In a 3-cycle, $a$ beats one of the two other elements and is beaten by the other; since $x, y \in X$, this contradicts (a) for $(\sigma, X)$.
:::

If $\mathcal M$ is closed under computability in $X \oplus Z$, the stems grow forever and their union is an infinite transitive set: a proof of $\mathsf{EM}$, without first-jump control.

## Step 2: block extendibility

The Mathias question asks whether some compatible string satisfies a $\Sigma^0_1$ sentence: it adds a block of reservoir elements at once. A transitive block does not suffice.

:::example{#ex-sd-em-block}
Let $(\sigma, X)$ be a condition and $x < y$ in $X$ with $T(x, y)$, such that for almost every $z \in X$, $T(y, z)$ and $T(z, x)$. The block $\{ x, y \}$ and the set $\sigma \cup \{ x, y \}$ are transitive, the latter as in the proof of :ref{#lem-sd-em-extension}. But $\{ x, y, z \}$ is a 3-cycle for almost every $z \in X$, so no infinite $Y \subseteq X$ makes $(\sigma \cup \{ x, y \}, Y)$ satisfy (b).
:::

The obstruction relates the block to the future. Suppose that $T$ is **stable**: every $x$ beats almost every $z$, in which case let $L(x) = 1$, or is beaten by almost every $z$, and let $L(x) = 0$. In the example, $L(x) = 0$ and $L(y) = 1$. If a block $\rho$ is **homogeneous for $L$**, then, after removing finitely many reservoir elements, no future element closes a cycle with two elements of $\rho$. A question asking for such a block would be $\Sigma^0_1(X \oplus Z')$, since $L$ is only $\Delta^0_2(Z)$. The remedy is the **over-approximation** of :ref{to="avoidance/forcing-question-method"}: ask for such a block for every possible limit function, that is, for every partition of the reservoir. For unstable tournaments, compactness leaves finitely many elements to stabilize, by restricting the reservoir.

:::lemma{#lem-sd-em-question}
Let $\mathcal M$ be a Scott ideal containing $Z$. For an $\mathsf{EM}$ condition $c = (\sigma, X)$ and a $\Sigma^0_1$ sentence $\varphi$, let $c \mathrel{?{\vdash}} \varphi$ hold if for every set $B$, writing $B^0 = B$ and $B^1 = \nat \setminus B$, there are $i < 2$ and a string $\tau$ compatible with $(\sigma, X \cap B^i)$, whose new elements form a $T$-transitive set, such that $\tau$ satisfies $\varphi$. Then:

1. if $c \mathrel{?{\vdash}} \varphi$, some extension of $c$ forces $\varphi$, that is, all its members satisfy $\varphi$;
2. if $c \mathrel{?{\nvdash}} \varphi$, some extension of $c$ forces $\neg \varphi$;
3. the relation $c \mathrel{?{\vdash}} \varphi(\vec m)$ is $\Sigma^0_1(X \oplus Z)$, uniformly in $\vec m$.
:::

:::proof{of=lem-sd-em-question}
Write $\varphi = \Phi^{Z \oplus G}_a\converge$. For a string $\beta$, let $\beta^0 = \{ n < |\beta| : \beta(n) = 1 \}$ and $\beta^1 = \{ n < |\beta| : \beta(n) = 0 \}$. Let $S$ be the set of strings $\beta$ for which there are no $i < 2$ and $\tau$ with $|\tau| \leq |\beta|$, compatible with $(\sigma, X \cap \beta^i)$, with transitive new elements and $\Phi^{Z \oplus \tau}_a[|\beta|]\converge$. As for :ref{#lem-seetapun-question}, $S$ is a tree computable in $X \oplus Z$ whose paths are the sets $B$ for which the definition fails, so the answer is positive if and only if $S$ is finite. This is 3.

*Property 2.* If $S$ has a path, it has one, $B$, in the Scott ideal $\mathcal M$. Some $X \cap B^i$ is infinite, and $d = (\sigma, X \cap B^i)$ is a condition extending $c$, since (a) and (b) pass to subsets. If a member $G$ of $d$ satisfied $\varphi$ with use $u$, the string $G \uh \max(u, |\sigma|)$ would be a witness for $B$, contradicting $B \in [S]$.

*Property 1.* Let $\ell \geq |\sigma|$ be such that no string of length $\ell$ belongs to $S$, and $F = X \cap [0, \ell)$. By finitely many restrictions as in step 1, there is $Y \subseteq X \setminus [0, \ell)$, computable in $X \oplus Z$, such that each $a \in F$ has a color $\gamma(a)$: $a$ beats every $y \in Y$ if $\gamma(a) = 1$, and is beaten by every $y \in Y$ if $\gamma(a) = 0$. Apply the definition of $S$ to the string $\beta$ of length $\ell$ with $X \cap \beta^i = \{ a \in F : \gamma(a) = i \}$: there are $i$ and $\tau$ compatible with $(\sigma, X)$, whose set $\rho$ of new elements is transitive and contained in $\{ a \in F : \gamma(a) = i \}$, satisfying $\varphi$. Then $d = (\tau, Y)$ is a condition extending $c$, whose members extend $\tau$, hence satisfy $\varphi$:

Property (a) holds for $\sigma$ since $Y \subseteq X$, and for $\rho$ by the choice of $\gamma$. For (b), let $y \in Y$ and consider a triple of $\sigma \cup \rho \cup \{ y \}$. With at least two elements in $\sigma$, it lies in some $\sigma \cup \{ z \}$ with $z \in X$, transitive by (b) for $c$. With exactly one element $a \in \sigma$, the two others lie in $X$, and $a$ beats both or is beaten by both, by (a) for $c$. Otherwise it lies in $\rho \cup \{ y \}$: $\rho$ is transitive, and two elements of $\rho$ are both beaten by $y$ or both beat $y$, since $\gamma$ is constant on $\rho$. In no case is it a 3-cycle. Finally $\min Y \geq \ell \geq |\tau|$.
:::

:::quiz[the Erdős–Moser question]
In the proof of property 1, why is the new block taken among the elements $a \in F$ with $\gamma(a) = i$, for a single $i$?

- [x] So that each $y$ in the new reservoir beats all its elements or is beaten by all of them, which excludes the obstruction of :ref{#ex-sd-em-block}.
- [ ] To make the block transitive.

  Transitivity is part of the answer to the question.
- [ ] So that property (a) holds for the new stem.

  Property (a) for the block comes from the thinning, which gives every $a \in F$ a color.

---

Where is it used that $\mathcal M$ is a Scott ideal, and not only a Turing ideal containing $Z$?

- [x] In property 2, to find a partition $B \in \mathcal M$ witnessing the negative answer, so that $X \cap B^i \in \mathcal M$.
- [ ] In property 1, for the thinned reservoir $Y$.

  $Y$ is computable in $X \oplus Z$.
- [ ] In property 3.

  It only uses that $S$ is computable in $X \oplus Z$.
:::

## Exercises

::::exercise{#exr-em-l-compatible difficulty=2}
Suppose $T$ is stable, with limit function $L$ as above. Say that a finite set $\rho$ is **$L$-compatible** if $T(a, b)$ implies $L(a) \geq L(b)$ for all $a, b \in \rho$. Show that if $(\sigma, X)$ is an $\mathsf{EM}$ condition and $\rho \subseteq X$ is a transitive $L$-compatible set, there is an infinite set $Y \subseteq X$, cofinite in $X$, such that $(\sigma \cup \rho, Y)$ satisfies (a) and (b). Show that every set homogeneous for $L$ is $L$-compatible, and that the block of :ref{#ex-sd-em-block} is not.

:::solution
Let $Y$ be the set of $y \in X$ with $y > \max \rho$ such that every $a \in \rho$ beats $y$ if $L(a) = 1$ and is beaten by $y$ if $L(a) = 0$. Each $a \in \rho$ excludes finitely many $y$, by stability, so $Y$ is cofinite in $X$. Property (a) holds by the choice of $Y$; for (b), triples with an element of $\sigma$ are handled as in :ref{#lem-sd-em-question}. A 3-cycle $\{ a, b, y \}$ with $a, b \in \rho$ and $y \in Y$, say with $T(a, b)$, must have $T(b, y)$ and $T(y, a)$, that is, $L(b) = 1$ and $L(a) = 0$, contradicting compatibility. Homogeneous sets are trivially compatible; the block of the example has $T(x, y)$ and $L(x) < L(y)$.
:::
::::

## Notes and references

The three steps and their application to the Erdős–Moser theorem follow the chapter *Forcing design* of Patey's monograph (sections *Core concepts* and *Erdős–Moser theorem*); $\mathsf{EM}$ conditions are those of Patey (2017), where (a) reads "$X$ is in a minimal interval of $\sigma$". The monograph's question uses colorings $g : \nat \to 2$ and $g$-compatible blocks; the variant with partitions and homogeneous blocks, mentioned there, is used here for its similarity with the Seetapun question. The Erdős–Moser theorem was introduced in reverse mathematics by Bovykin and Weiermann (2017).

- L. Patey, *Lowness and avoidance*, chapter *Forcing design*.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- A. Bovykin and A. Weiermann, *The strength of infinitary Ramseyan principles can be accessed by their densities*, Annals of Pure and Applied Logic 168 (2017), 1700–1709.
