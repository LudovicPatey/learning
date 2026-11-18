---
title: The Erdős–Moser theorem
summary: Tournaments and the Erdős–Moser theorem EM; RT²₂ is equivalent to EM + ADS over RCA₀, and EM + SADS implies SRT²₂; EM implies the infinite pigeonhole principle for any number of colors, hence Σ⁰₂ collection (Kreuzer); a computable tournament with no computable infinite transitive subtournament; the separations of EM from ADS and SRT²₂.
duration: 40
prerequisites: [stable-cohesive, induction-conservation/pigeonhole]
---

The two previous lessons studied consequences of $\mathsf{RT}^2_2$ that impose an order on the instance. The Erdős–Moser theorem goes the other way: it asks for an infinite set on which a coloring *becomes* an order. Together with $\mathsf{ADS}$, which solves orders, it gives back $\mathsf{RT}^2_2$. This decomposition, like that of Cholak, Jockusch and Slaman, splits Ramsey's theorem for pairs into two strictly weaker parts, but along a different line: transitivity on one side, orders on the other.

## Tournaments

:::definition{#def-tournament}
A **tournament** on a set $X \subseteq \nat$ is a relation $T \subseteq X \times X$ such that for all distinct $x, y \in X$, exactly one of $T(x, y)$ and $T(y, x)$ holds, and $T(x, x)$ holds for no $x$. It is **transitive** on $S \subseteq X$ if $T(x, y)$ and $T(y, z)$ imply $T(x, z)$ for all $x, y, z \in S$. The **Erdős–Moser theorem** $\mathsf{EM}$ states that every tournament on an infinite set is transitive on some infinite subset.
:::

Think of $T(x, y)$ as "$x$ beats $y$" in a round-robin competition. A tournament is transitive on $S$ exactly when "beats" is a strict linear order of $S$: the players of $S$ can be ranked so that each beats all those ranked below. A tournament on $\nat$ is the same thing as a coloring of pairs: for $x < y$, give $\{ x, y \}$ the color $1$ if $T(x, y)$ and $0$ if $T(y, x)$. In these terms, $T$ is transitive on $S$ if and only if the coloring is transitive on $S$ in the sense of :ref{#ex-ads-transitive} (:ref{#ex-tournament-transitive}). So $\mathsf{EM}$ asks for an infinite set on which the coloring is transitive, and $\mathsf{RT}^2_2$ for one on which it is constant: $\mathsf{RT}^2_2$ implies $\mathsf{EM}$.

:::figure[A tournament on $\{ 0, 1, 2, 3, 4 \}$: an arrow from $x$ to $y$ means $T(x, y)$. It is transitive on $\{ 0, 1, 3 \}$, which it ranks as $0, 1, 3$, and not on $\{ 0, 1, 2 \}$, where $0$ beats $1$, $1$ beats $2$ and $2$ beats $0$.]
<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="A tournament on five vertices, numbered 0 to 4, drawn on a pentagon with an arrow from each winner to each loser. The arrows among 0, 1 and 3 are highlighted: 0 beats 1, 1 beats 3 and 0 beats 3, a transitive subtournament. The vertices 0, 1 and 2 form a cycle"><defs><marker id="em-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker><marker id="em-arrow-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="312.1" y1="44.8" x2="373.7" y2="89.6" class="accent-stroke" stroke-width="2.2" marker-end="url(#em-arrow-a)"/><line x1="382.9" y1="113.9" x2="359.4" y2="186.2" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><line x1="349.5" y1="188.1" x2="305.3" y2="52.2" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><line x1="295.4" y1="50.3" x2="251.2" y2="186.2" class="accent-stroke" stroke-width="2.2" marker-end="url(#em-arrow-a)"/><line x1="375.4" y1="108.4" x2="259.7" y2="192.4" class="accent-stroke" stroke-width="2.2" marker-end="url(#em-arrow-a)"/><line x1="339.1" y1="202.4" x2="262.9" y2="202.4" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><line x1="241.3" y1="188.1" x2="217.8" y2="115.8" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><line x1="224.6" y1="90.8" x2="286.2" y2="46.0" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><line x1="227.5" y1="99.6" x2="370.5" y2="99.6" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><line x1="342.0" y1="193.6" x2="226.3" y2="109.6" class="muted-stroke" stroke-width="1.2" marker-end="url(#em-arrow)"/><circle cx="300.0" cy="36.0" r="13" class="head-cell"/><text x="300.0" y="41.0" text-anchor="middle" class="mrm" font-size="14">0</text><circle cx="387.5" cy="99.6" r="13" class="head-cell"/><text x="387.5" y="104.6" text-anchor="middle" class="mrm" font-size="14">1</text><circle cx="354.1" cy="202.4" r="13" class="node"/><text x="354.1" y="207.4" text-anchor="middle" class="mrm" font-size="14">2</text><circle cx="245.9" cy="202.4" r="13" class="head-cell"/><text x="245.9" y="207.4" text-anchor="middle" class="mrm" font-size="14">3</text><circle cx="212.5" cy="99.6" r="13" class="node"/><text x="212.5" y="104.6" text-anchor="middle" class="mrm" font-size="14">4</text><text x="30" y="60" class="label">an arrow x → y: x beats y</text><text x="30" y="80" class="label">highlighted: {0, 1, 3}, transitive</text><text x="30" y="100" class="label">0 → 1 → 2 → 0: a cycle</text></svg>
:::

The finite form of the theorem is the starting point of Erdős and Moser (1964): every tournament on $2^n$ players has a transitive subtournament of $n + 1$ players (:ref{#ex-finite-em}). The infinite form follows from $\mathsf{RT}^2_2$ as above; the question is how much of Ramsey's theorem it needs.

## Two decompositions of Ramsey's theorem for pairs

:::theorem{#thm-rt22-em-ads}
The following are provable in $\mathsf{RCA}_0$.
1. $\mathsf{RT}^2_2$ is equivalent to $\mathsf{EM} + \mathsf{ADS}$.
2. $\mathsf{EM} + \mathsf{SADS}$ implies $\mathsf{SRT}^2_2$.
:::

:::proof{of=thm-rt22-em-ads}
1. $\mathsf{RT}^2_2$ implies $\mathsf{EM}$, by the translation above, and $\mathsf{ADS}$ by :ref{#prop-rt22-cac-ads}. Conversely, let $c : [\nat]^2 \to 2$, and let $T$ be the tournament on $\nat$ with $T(x, y)$ if and only if $c(\{ x, y \}) = 1$, for $x < y$; it exists by $\Delta^0_1$ comprehension. By $\mathsf{EM}$, there is an infinite set $S$ on which $T$ is transitive. Then $x \leq_L y \iff x = y \vee T(x, y)$ is a linear order of $S$. By $\mathsf{ADS}$, it has an infinite ascending or descending sequence $H \subseteq S$. If $H$ is ascending, then for $x < y$ in $H$, $x <_L y$, that is, $T(x, y)$, and $c(\{ x, y \}) = 1$: $H$ is homogeneous of color $1$. If $H$ is descending, it is homogeneous of color $0$.
2. If $c$ is stable, the order $\leq_L$ above is stable. Let $x \in S$. If $\lim_y c(\{ x, y \}) = 1$, then $T(x, y)$ for almost every $y \in S$, so $x$ has finitely many $\leq_L$-predecessors in $S$. If the limit is $0$, then $T(y, x)$ for almost every $y \in S$, and $x$ has finitely many successors. So $\mathsf{SADS}$ suffices in the argument of part 1.
:::

The order built from a transitive set ranks the players; an ascending sequence of this ranking, read in the order of $\nat$, consists of players each of whom beats all later ones, which is exactly homogeneity of color $1$. The figure gives a finite picture: on $\{ 0, 1, 3 \}$, the ranking is $0, 1, 3$, and every earlier player beats every later one.

:::quiz[the decomposition RT²₂ = EM + ADS]
In the proof of :ref{#thm-rt22-em-ads} (1), why is $\mathsf{ADS}$ applied to the transitive set $S$ rather than to the tournament on all of $\nat$?

- [x] Because $T$ is a linear order only where it is transitive; on $\nat$, it may have cycles, and is not an instance of $\mathsf{ADS}$.
- [ ] Because $S$ is computable.

  $S$ is given by $\mathsf{EM}$ and need not be computable; it is a set of the model.
- [ ] Because ascending sequences of $\nat$ are homogeneous for every coloring.

  Ascending sequences are defined for a linear order, here $\leq_L$ on $S$; they are homogeneous for $c$ because $\leq_L$ comes from $c$.
:::

## The first-order strength of EM

The next result shows that $\mathsf{EM}$, although it says nothing about colorings of numbers, carries the pigeonhole principle for any number of colors, and thus some induction. Recall that $\mathsf{RT}^1_{<\infty}$ states that for every $k$, every $f : \nat \to k$ has an infinite homogeneous set, and that by Hirst's theorem it is equivalent to $\mathsf B\Sigma^0_2$ over $\mathsf{RCA}_0$ (:ref{#thm-hirst}).

:::theorem[Kreuzer]{#thm-em-bsigma2}
Over $\mathsf{RCA}_0$, $\mathsf{EM}$ implies $\mathsf{RT}^1_{<\infty}$, hence $\mathsf B\Sigma^0_2$.
:::

**Intuition.** Let $f$ be a coloring of numbers. Declare that $x$ beats $y$, for $x < y$, if they have the same color. On a transitive set, two players of different colors, followed by a third of a different color from the second, force the first and third to differ as well. So along a transitive set, a color that has been left is never taken again: the colors appear in consecutive blocks. There are at most $k$ blocks, and the last one is infinite.

:::proof{of=thm-em-bsigma2}
We argue in $\mathsf{RCA}_0$. Let $f : \nat \to k$. Define the tournament $T$ by $T(x, y)$ if $f(x) = f(y)$, and $T(y, x)$ otherwise, for $x < y$. By $\mathsf{EM}$, there is an infinite set $S$ on which $T$ is transitive.

*Colors form blocks along $S$.* Let $x < y < z$ in $S$ with $f(x) \neq f(y)$. If $f(z) = f(x)$, then $f(y) \neq f(z)$, so $T(y, x)$ and $T(z, y)$, and transitivity gives $T(z, x)$, that is, $f(x) \neq f(z)$: a contradiction. So once a color is left along $S$, it never reappears.

*There are finitely many blocks.* Let $W$ be the set of $x \in S$ such that $f(y) \neq f(x)$ for every $y \in S$ with $y < x$: the first element of $S$ of each color that appears. It exists by $\Delta^0_1$ comprehension, contains $\min S$, and $f$ is injective on $W$. If $W$ had $k + 1$ elements, its first $k + 1$ elements would form a finite set mapped injectively into $\{ 0, \ldots, k - 1 \}$ by $f$, contradicting the finite pigeonhole principle, which $\mathsf{RCA}_0$ proves by $\Sigma^0_0$ induction on $k$. So $W$ is bounded, and it has a largest element $x$.

*The last block is infinite.* Let $y \in S$ with $y > x$, and suppose $f(y) = j \neq f(x)$. The least $z \in S$ with $f(z) = j$ belongs to $W$, and $z \neq x$. If $z < x$, then $z < x < y$ in $S$ with $f(z) = j \neq f(x)$ and $f(y) = j$, which the first step forbids. So $z > x$, contradicting the maximality of $x$ in $W$. Hence $f$ is constant on $\{ y \in S : y \geq x \}$, an infinite set that exists by $\Delta^0_1$ comprehension.

By :ref{#thm-hirst}, $\mathsf B\Sigma^0_2$ follows.
:::

:::quiz[the proof of Kreuzer's theorem]
In the proof of :ref{#thm-em-bsigma2}, where is the transitivity of $T$ on $S$ used?

- [x] Only in the first step, for the color $0$ of the induced coloring: two consecutive changes of color force a change between the first and third element, so a color cannot reappear after it has been left.
- [ ] To show that $W$ is bounded.

  Boundedness uses only the injectivity of $f$ on $W$ and the finite pigeonhole principle.
- [ ] To show that $S$ is infinite.

  $S$ is infinite by $\mathsf{EM}$.
:::

So $\mathsf{EM}$ is not $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, unlike $\mathsf{COH}$ and $\mathsf{WKL}_0$: $\mathsf{RCA}_0$ does not prove $\mathsf B\Sigma^0_2$ (:ref{to="induction-conservation/pigeonhole"}).

## A computable tournament without computable solutions

:::proposition{#prop-em-not-computable}
There is a computable tournament on $\nat$ that is transitive on no infinite computable set. Consequently, $\mathsf{RCA}_0$ does not prove $\mathsf{EM}$.
:::

**Intuition.** To defeat a c.e. set $W_e$, wait for two of its elements $x < y$, oriented say $T(x, y)$. Every later number $z$ can then be oriented to close a cycle: $T(y, z)$ and $T(z, x)$. If $W_e$ is infinite, it contains such a $z$, and the three players $x$, $y$, $z$ form a cycle. Two requirements conflict only if they hold a common element, and then the stronger one decides the orientation of the pairs through it. A requirement is injured only when a stronger one takes one of its elements, which happens finitely often.

:::proof{of=prop-em-not-computable}
We define $T$ on $\{ 0, \ldots, s \}$ at stage $s$, orienting the pairs $\{ z, s \}$ for $z < s$. Requirement $\mathcal R_e$ may hold a pair $x_e < y_e$. At stage $s$, process $e = 0, 1, \ldots, s - 1$ in turn. If $\mathcal R_e$ holds a pair one of whose elements is held by some $\mathcal R_{e'}$ with $e' < e$, it releases its pair. Then, if $\mathcal R_e$ holds no pair and $W_{e,s}$ has two elements $x < y$ held by no $\mathcal R_{e'}$ with $e' < e$, it takes the least such pair.

Now orient each pair $\{ z, s \}$ with $z < s$. If no requirement holds $z$, set $T(z, s)$. Otherwise, let $\mathcal R_e$ be the requirement of highest priority holding $z$, with pair $x_e < y_e$, and orient $\{ z, s \}$ as in a cycle through $x_e$, $y_e$ and $s$: if $T(x_e, y_e)$, set $T(y_e, s)$ when $z = y_e$ and $T(s, x_e)$ when $z = x_e$; if $T(y_e, x_e)$, set $T(s, y_e)$ when $z = y_e$ and $T(x_e, s)$ when $z = x_e$. Each pair is oriented once, when its larger element appears, so $T$ is a computable tournament.

*Each requirement is injured finitely often.* By induction on $e$, suppose that after some stage $s_0$, the requirements $\mathcal R_{e'}$ with $e' < e$ no longer take or release pairs, so that the elements they hold are fixed, at most $2e$ of them. After $s_0$, $\mathcal R_e$ releases its pair at most once. If $W_e$ is infinite, it has two elements outside these $2e$ elements, so $\mathcal R_e$ eventually holds a pair $x_e < y_e$ disjoint from the pairs of stronger requirements, and keeps it forever; let $s_e$ be the stage at which it takes it.

*Each $\mathcal R_e$ is met.* Let $W_e$ be infinite, and say $T(x_e, y_e)$. For $z > s_e$, no stronger requirement holds $x_e$ or $y_e$, so $\mathcal R_e$ is the strongest requirement holding them, and the construction sets $T(y_e, z)$ and $T(z, x_e)$. Since $W_e$ is infinite, it has an element $z > s_e$, and $T$ is not transitive on $\{ x_e, y_e, z \} \subseteq W_e$. The case $T(y_e, x_e)$ is symmetric. So $T$ is transitive on no infinite c.e. set, in particular on no infinite computable set, and $\mathrm{REC} \not\models \mathsf{EM}$, while $\mathrm{REC} \models \mathsf{RCA}_0$.
:::

The injury here is milder than in the cut construction of :ref{#thm-tennenbaum-denisov}: an action never undoes the work of a weaker requirement on pairs already oriented, because a cycle can be closed with any new element. Kach, Lerman, Solomon and Weber proved much more: some computable tournament has no infinite transitive subtournament that is $\Sigma^0_2$, so that $\mathsf{EM}$ behaves like $\mathsf{RT}^2_2$ in the arithmetic hierarchy (:ref{#thm-jockusch-no-delta2}). We admit this.

## Separations

The decomposition of :ref{#thm-rt22-em-ads} is proper. $\mathsf{ADS}$ does not imply $\mathsf{EM}$: otherwise it would imply $\mathsf{RT}^2_2$, which it does not, since $\mathsf{ADS}$ does not imply the existence of DNC functions (Hirschfeldt and Shore; :ref{to="dnr-wwkl"}) while $\mathsf{RT}^2_2$ does (:ref{#cor-rt22-dnc}). $\mathsf{EM}$ does not imply $\mathsf{ADS}$, and not even $\mathsf{SRT}^2_2$, by a theorem of Lerman, Solomon and Towsner (2013): there is an ω-model of $\mathsf{EM}$ that is not a model of $\mathsf{SRT}^2_2$, hence by :ref{#thm-rt22-em-ads} (2) not a model of $\mathsf{SADS}$. Their proof is an iterated forcing argument; Patey later gave a proof by preservation of two hyperimmunities, presented in the course on the design of separations (:ref{#cor-sd-em-not-srt22}).

On the other side, $\mathsf{EM}$ is not weak. It implies the Ramsey-type weak König lemma (Bienvenu, Patey and Shafer; Flood and Towsner), hence the existence of DNC functions relative to every set; Wang showed that it even gives functions DNC relative to the jump of every set (Dzhafarov–Mummert, Theorem 9.5.7). We admit these results.

::::exercise{#ex-finite-em difficulty=1 objective="Prove the finite Erdős–Moser theorem by repeatedly keeping the larger half of the players beaten by, or beating, a chosen player."}
Show that every tournament on a set of $2^n$ players is transitive on some set of $n + 1$ players.

:::solution
By induction on $n$. For $n = 0$, a single player is a transitive set of size $1$. Let $X$ have $2^{n+1}$ players and pick $p \in X$. The other $2^{n+1} - 1$ players split into those beaten by $p$ and those who beat $p$, so one of the two groups, $Y$, has at least $2^n$ players. By induction, $T$ is transitive on some $Z \subseteq Y$ of size $n + 1$. Suppose that $p$ beats every player of $Y$, and let $a, b, c$ in $Z \cup \{ p \}$ with $T(a, b)$ and $T(b, c)$. If none of them is $p$, then $T(a, c)$ by the transitivity on $Z$. No player of $Z$ beats $p$, so $b \neq p$ and $c \neq p$; hence $a = p$, $c \in Z$, and $T(p, c)$. So $T$ is transitive on $Z \cup \{ p \}$, which has $n + 2$ players. If every player of $Y$ beats $p$, the argument is symmetric, with $p$ ranked last.
:::
::::

## Notes and references

The finite theorem is in Erdős and Moser (1964). In reverse mathematics, the decomposition $\mathsf{RT}^2_2 = \mathsf{EM} + \mathsf{ADS}$ was noted by several authors (Bovykin and Weiermann among them; Hirschfeldt, Exercise 9.30; Dzhafarov–Mummert, Proposition 9.5.2, call it folklore). :ref{#thm-em-bsigma2} is due to Kreuzer (2012), with the proof of Dzhafarov and Mummert, Theorem 9.5.8. The separation of $\mathsf{EM}$ from $\mathsf{SRT}^2_2$ is due to Lerman, Solomon and Towsner (2013), and the absence of $\Sigma^0_2$ solutions to Kach, Lerman, Solomon and Weber (see Lerman, Solomon and Towsner). The direct construction of :ref{#prop-em-not-computable} is a warm-up for the much stronger theorem of Kach, Lerman, Solomon and Weber.

- P. Erdős and L. Moser, *On the representation of directed graphs as unions of orderings*, Magyar Tudományos Akadémia Matematikai Kutató Intézetének Közleményei 9 (1964), 125–132.
- M. Lerman, R. Solomon and H. Towsner, *Separating principles below Ramsey's theorem for pairs*, Journal of Mathematical Logic 13 (2013), 1350007.
- A. P. Kreuzer, *Primitive recursion and the chain antichain principle*, Notre Dame Journal of Formal Logic 53 (2012), 245–265.
- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 9.2.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 9.5.

:::::exercises
::::exercise{#ex-tournament-transitive difficulty=1 objective="Translate transitivity of a tournament into transitivity of the induced coloring."}
Let $T$ be a tournament on $\nat$ and $c$ the induced coloring: $c(\{ x, y \}) = 1$ if $T(x, y)$, for $x < y$. Show that $T$ is transitive on $S$ if and only if for all $x < y < z$ in $S$ and each color $i$, $c(\{ x, y \}) = c(\{ y, z \}) = i$ implies $c(\{ x, z \}) = i$.

:::solution
Suppose $T$ transitive on $S$, and $x < y < z$ in $S$. If $c(\{ x, y \}) = c(\{ y, z \}) = 1$, then $T(x, y)$ and $T(y, z)$, so $T(x, z)$ and $c(\{ x, z \}) = 1$. If both are $0$, then $T(z, y)$ and $T(y, x)$, so $T(z, x)$ and $c(\{ x, z \}) = 0$.

Conversely, assume the condition, and let $a, b, c'$ in $S$ with $T(a, b)$ and $T(b, c')$; they are distinct, since $T$ is irreflexive and asymmetric. We show $T(a, c')$; suppose instead $T(c', a)$, so that $a, b, c'$ form a cycle. List them in increasing order as $x < y < z$. A cycle on three elements, read in increasing order, has either $T(x, y)$, $T(y, z)$, $T(z, x)$, or $T(y, x)$, $T(z, y)$, $T(x, z)$. In the first case, $c(\{ x, y \}) = c(\{ y, z \}) = 1$ and $c(\{ x, z \}) = 0$; in the second, the colors are $0$, $0$ and $1$. Both contradict the condition.
:::
::::

::::exercise{#ex-rt22-three-parts difficulty=1 objective="Combine the two decompositions of Ramsey's theorem for pairs into one with three parts."}
Show in $\mathsf{RCA}_0$ that $\mathsf{RT}^2_2$ is equivalent to $\mathsf{EM} + \mathsf{SADS} + \mathsf{COH}$.

:::solution
$\mathsf{RT}^2_2$ implies $\mathsf{EM}$ and $\mathsf{ADS}$ by :ref{#thm-rt22-em-ads}, hence $\mathsf{SADS}$ and $\mathsf{COH}$ by :ref{#prop-ads-decomposition} and :ref{#thm-ads-coh}. Conversely, $\mathsf{COH}$ implies $\mathsf{CADS}$ (:ref{#prop-ads-decomposition} (3)), so $\mathsf{SADS} + \mathsf{COH}$ implies $\mathsf{SADS} + \mathsf{CADS}$, which is $\mathsf{ADS}$ (part 1), and $\mathsf{EM} + \mathsf{ADS}$ implies $\mathsf{RT}^2_2$.
:::
::::

::::exercise{#ex-em-delta2 difficulty=2 objective="Compute a transitive set below the second jump, by the proof of Ramsey's theorem, and see that EM has the same upper bound as RT²₂."}
Show that every computable tournament on $\nat$ is transitive on an infinite set computable in $\emptyset''$. Show that for every computable stable coloring $c$, the tournament of the proof of :ref{#thm-rt22-em-ads} is transitive on an infinite $\Delta^0_2$ set.

:::solution
A set homogeneous for the induced coloring is transitive for $T$: on it, either every earlier player beats every later one, or every later player beats every earlier one, and both relations are strict linear orders. By the upper bound for Ramsey's theorem for pairs (:ref{#thm-jockusch-upper}, with $n = 2$, or :ref{#ex-rt22-via-decomposition}), the computable induced coloring has an infinite homogeneous set computable in $\emptyset''$. If $c$ is stable, it has an infinite $\Delta^0_2$ homogeneous set by :ref{#prop-srt-d22}, since its limit set and the complement are $\Delta^0_2$ and one of them is infinite; this set is transitive for $T$.
:::
::::
:::::
