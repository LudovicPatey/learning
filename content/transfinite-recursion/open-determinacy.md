---
title: Open determinacy
summary: Infinite games of perfect information in second-order arithmetic; ATR₀ proves the determinacy of open games, by ranking the winning positions of the first player along a well-ordering, or else by a pseudohierarchy that guides the second player; the determinacy of clopen games implies ATR₀ (Steel), through games in which each player builds a descending sequence; a survey of stronger forms of determinacy.
duration: 40
prerequisites: [pseudohierarchies, sigma11-separation]
---

In an infinite game of perfect information, two players alternately choose natural numbers, and the resulting infinite sequence decides the winner. Gale and Stewart proved in 1953 that if the set of plays won by the first player is open, one of the players has a winning strategy. The classical proof ranks the positions from which the first player can force a win, by transfinite recursion. This lesson shows that this proof is exactly $\mathsf{ATR}_0$: open determinacy is provable in $\mathsf{ATR}_0$, with a pseudohierarchy for the case where the ranking does not end, and conversely the determinacy of clopen games implies $\mathsf{ATR}_0$.

## Games and strategies

A **play** is a function $f : \nat \to \nat$; player 0 chooses $f(0), f(2), \ldots$ and player 1 chooses $f(1), f(3), \ldots$. A **position** is a finite sequence. A **strategy** for player 0 is a function $S_0$ from the positions of even length to $\nat$, and a strategy for player 1 a function $S_1$ from the positions of odd length to $\nat$. The play $S_0 \otimes S_1$ is defined by $f(2k) = S_0(f \uh 2k)$ and $f(2k+1) = S_1(f \uh (2k + 1))$.

A game is given by its set of plays won by player 0. It is **open** (or $\Sigma^0_1$) if this set is $\{ f : \exists k\ f \uh 2k \in W \}$ for a set $W$ of positions of even length: player 0 wins as soon as a position of $W$ is reached. Every $\Sigma^0_1$ property of $f$ with parameters, $\exists n\, \theta(f \uh n)$ with $\theta$ bounded, has this form, with $W$ the set of positions $\sigma$ of even length such that $\theta(\sigma \uh n)$ for some $n \leq |\sigma|$. A game is **clopen** (or $\Delta^0_1$) if its set of plays won by player 0 is defined both by a $\Sigma^0_1$ and by a $\Pi^0_1$ formula.

:::definition{#def-determinacy}
A game is **determined** if player 0 has a strategy $S_0$ with which every play $S_0 \otimes S_1$ is won by 0, or player 1 has a strategy $S_1$ with which no play $S_0 \otimes S_1$ is won by 0. **$\Sigma^0_1$ determinacy** is the statement that every open game is determined, and **$\Delta^0_1$ determinacy** the scheme that every clopen game is determined.
:::

The two cases exclude each other: playing the two strategies against each other would give a play both won and not won by 0. In a clopen game, every play is decided at a finite stage, in the sense that the $\Sigma^0_1$ definition or the $\Pi^0_1$ definition of its complement is witnessed by a finite part of the play. Open games need not be: a play that never reaches $W$ is lost by player 0, but at no finite stage is this visible.

## ATR₀ proves open determinacy

Fix an open game with set $W$. The positions from which player 0 can force a win in one round, or in a bounded number of rounds, are defined by recursion. Along a linear order $X$, consider the equations
$$
W_j = \big\{ \sigma : \sigma \in W \ \text{ or } \ \exists m\, \forall n\, \exists i <_X j\ \ \sigma \langle m, n \rangle \in W_i \big\}, \qquad j \in F_X,
$$
for positions $\sigma$ of even length. A position is in $W_j$ if it is winning already, or if player 0 has a move $m$ after which every answer $n$ of player 1 leads to a position of some earlier level. They define a $\theta$-hierarchy for an arithmetic $\theta$, which exists along every well-ordering in $\mathsf{ATR}_0$; and $W_i \subseteq W_j$ for $i <_X j$.

:::theorem{#thm-open-determinacy-atr}
$\mathsf{ATR}_0$ proves $\Sigma^0_1$ determinacy.
:::

**Intuition.** If, along some well-ordering, the empty position enters a level, player 0 wins by always moving to a position of a lower level: the levels form a descending sequence, which must end in $W$. If the empty position enters no level along any well-ordering, the method of pseudohierarchies gives levels along an ill-founded order that never contain the empty position. Player 1 then follows a descending sequence $g(0) >_X g(1) >_X \cdots$, keeping the position outside $W_{g(k)}$ after $k$ rounds; the definition of the levels says he can.

:::proof{of=thm-open-determinacy-atr}
We argue in $\mathsf{ATR}_0$.

*Case 1: for some well-ordering $X$ and some hierarchy $(W_j)$ along $X$, the empty position belongs to some $W_l$.* For $\sigma \in W_l$, let $r(\sigma)$ be the $\leq_X$-least $j$ with $\sigma \in W_j$. Let $S_0(\sigma)$ be, for $\sigma \in W_l \setminus W$, the least $m$ such that every $n$ has some $i <_X r(\sigma)$ with $\sigma \langle m, n \rangle \in W_i$; such an $m$ exists since $\sigma \in W_{r(\sigma)}$ and $\sigma \notin W$. Let $S_0(\sigma) = 0$ for the other positions. $S_0$ exists by arithmetic comprehension. Let $S_1$ be any strategy and $f = S_0 \otimes S_1$. By induction on $k$, as long as $f \uh 2k \notin W$, the position $f \uh 2k$ is in $W_l$, and $r(f \uh (2k+2)) <_X r(f \uh 2k)$. If $f \uh 2k \notin W$ for every $k$, the values $r(f \uh 2k)$ would form a descending sequence of $X$. So some $f \uh 2k$ is in $W$, and $S_0$ is winning.

*Case 2: otherwise.* Let $\varphi(X)$ be the $\Sigma^1_1$ formula: $X$ is a linear order, and some hierarchy $(W_j)$ along $X$ has $\langle\rangle \notin W_j$ for every $j$. By arithmetic transfinite recursion and the case hypothesis, $\varphi(X)$ holds for every well-ordering. By :ref{#lem-pseudohierarchies}, it holds for some linear order $X$ that is not a well-ordering. Fix such an $X$, its hierarchy $(W_j)$, and a descending sequence $g$ of $X$.

Define $S_1$ on a position $\sigma \langle m \rangle$ with $|\sigma| = 2k$: let $S_1(\sigma \langle m \rangle)$ be the least $n$ with $\sigma \langle m, n \rangle \notin W_{g(k+1)}$, if there is one, and $0$ otherwise. Let $S_0$ be any strategy and $f = S_0 \otimes S_1$. We show by induction on $k$ that $f \uh 2k \notin W_{g(k)}$. For $k = 0$, $\langle\rangle \notin W_{g(0)}$. If $f \uh 2k \notin W_{g(k)}$, then by the equations, for $m = f(2k)$ there is $n$ such that $f \uh 2k \, \langle m, n \rangle \notin W_i$ for every $i <_X g(k)$, in particular for $i = g(k+1)$. So $S_1$ finds such an $n$, and $f \uh (2k + 2) \notin W_{g(k+1)}$. Since $W \subseteq W_j$ for every $j$, no $f \uh 2k$ is in $W$, and $S_1$ is winning.
:::

:::quiz[open determinacy]
In Case 2, why does player 1 need a descending sequence of $X$, rather than a single level $W_j$?

- [x] Because staying outside one level $W_j$ is not preserved by a round of the game: the equations only say that from outside $W_j$, player 1 can stay outside every level below $j$. To keep this up forever he must go down infinitely often.
- [ ] Because the levels are increasing, so the last one is the largest.

  An ill-founded order may have no last element, and the issue is preservation, not size.
- [ ] Because a descending sequence makes $S_1$ computable.

  $S_1$ is arithmetic in the hierarchy and the sequence; computability plays no role here.

---

In Case 1, why does the strategy $S_0$ win?

- [x] Because each move of player 0 strictly lowers the level of the position, and a well-ordering has no infinite descending sequence, so after finitely many rounds the position is in $W$.
- [ ] Because $S_0$ reaches $W$ in one move.

  It reaches a lower level; $W$ may be reached only after many rounds, as many as the rank of the empty position.
- [ ] Because player 1 cannot leave $W_l$.

  He cannot leave the levels below the current one by the choice of $m$; this is the reason why the level decreases.
:::

## Clopen determinacy implies ATR₀

The reversal uses games in which each player builds a descending sequence, and the one whose sequence lasts longer wins.

For linear orders $X$ and $Y$, at least one of which is a well-ordering, let $G(X, Y)$ be the game in which player 0 plays $f(0) >_X f(2) >_X \cdots$ and player 1 plays $f(1) >_Y f(3) >_Y \cdots$; the first player who cannot or does not continue his sequence loses, player 0 being checked first in each round. Formally, player 0 wins if for some $j$, his sequence is descending up to $f(2j + 2)$ while $f(2j+3) <_Y f(2j+1)$ fails; and he loses if for some $j$, $f(2j + 2) <_X f(2j)$ fails while player 1's sequence is descending up to $f(2j + 1)$. Both conditions are $\Sigma^0_1$. Since one of the orders is a well-ordering, one of the sequences eventually fails, so exactly one of the two conditions holds: the set of plays won by 0 is $\Sigma^0_1$, and its complement too, and $G(X, Y)$ is clopen.

:::lemma{#lem-descent-games}
The following is provable in $\mathsf{RCA}_0$, for linear orders $X$ and $Y$ one of which is a well-ordering.
1. If $X$ is not a well-ordering, player 0 has a winning strategy in $G(X, Y)$.
2. If player 0 has a winning strategy in $G(X, Y)$, then player 1 has one in $G(Y, X)$.
:::

:::proof{of=lem-descent-games}
1. Player 0 plays a descending sequence $x_0 >_X x_1 >_X \cdots$ of $X$, ignoring the moves of player 1: $S_0(\sigma) = x_j$ for $|\sigma| = 2j$. His sequence never fails. Since $X$ is not a well-ordering, $Y$ is one, so player 1's sequence fails at some round, and at the first such round the winning condition of player 0 holds.
2. Let $S_0$ win $G(X, Y)$. Define a strategy $S'_1$ for player 1 in $G(Y, X)$ by $S'_1(\sigma) = S_0(\langle \sigma(1), \ldots, \sigma(2j) \rangle)$ for $|\sigma| = 2j + 1$: player 1 ignores the first move of player 0 and answers as $S_0$ would, treating the later moves of player 0 as the moves of player 1 in $G(X, Y)$. Let $S'_0$ be a strategy for player 0 in $G(Y, X)$, $k = S'_0(\langle\rangle)$, and $S_1(\sigma) = S'_0(\langle k \rangle \sigma)$. For $f = S_0 \otimes S_1$ and $f' = S'_0 \otimes S'_1$, induction on $j$ gives $f'(2j + 1) = f(2j)$ and $f'(2j + 2) = f(2j + 1)$. Since $S_0$ wins, some $j$ has $f(2i+2) <_X f(2i)$ for all $i \leq j$ and $f(2j + 3) \not<_Y f(2j+1)$. In $f'$, this reads: $f'(2i + 3) <_X f'(2i + 1)$ for all $i \leq j$, and $f'(2j + 4) \not<_Y f'(2j + 2)$. So in $G(Y, X)$, player 0, who plays in $Y$, fails at $f'(2(j+1) + 2)$ while player 1's sequence is descending up to $f'(2(j+1) + 1)$: player 0 loses $f'$. So $S'_1$ wins $G(Y, X)$.
:::

:::theorem[Steel]{#thm-clopen-determinacy-atr}
Over $\mathsf{RCA}_0$, $\mathsf{ATR}_0$, $\Sigma^0_1$ determinacy and $\Delta^0_1$ determinacy are equivalent.
:::

**Intuition.** Given disjoint $\Sigma^1_1$ properties $\neg\mathrm{WO}(X_k)$ and $\neg\mathrm{WO}(Y_k)$, consider the clopen game in which player 0 chooses $k$, player 1 chooses one of $G(X_k, Y_k)$ and $G(Y_k, X_k)$, and they play it. Player 0 cannot have a winning strategy: player 1 picks a game he wins, which exists by determinacy of the descent games and :ref{#lem-descent-games}. So player 1 has a winning strategy, and its choices separate: if $X_k$ is ill-founded, player 0 wins $G(X_k, Y_k)$, so player 1 must choose the other game.

:::proof{of=thm-clopen-determinacy-atr}
$\mathsf{ATR}_0$ implies $\Sigma^0_1$ determinacy by :ref{#thm-open-determinacy-atr}, which implies $\Delta^0_1$ determinacy. Assume $\Delta^0_1$ determinacy. It implies $\mathsf{ACA}_0$ (:ref{#ex-clopen-aca}). We prove $\Sigma^1_1$ separation and apply :ref{#thm-atr-sigma11-separation}. Let $\varphi_1(k) \iff \neg\mathrm{WO}(X_k)$ and $\varphi_0(k) \iff \neg\mathrm{WO}(Y_k)$ be disjoint, with sequences of linear orders given by the normal form and :ref{#prop-kb-aca}. For every $k$, one of $X_k$ and $Y_k$ is a well-ordering, so $G(X_k, Y_k)$ and $G(Y_k, X_k)$ are clopen.

Let $G'$ be the game in which player 0 first plays $k$, player 1 plays $i$, and then they play $G(X_k, Y_k)$ if $i = 0$ and $G(Y_k, X_k)$ if $i = 1$ (any other $i$ loses for player 1). Its winning condition is clopen, uniformly, so $G'$ is determined.

Player 0 has no winning strategy in $G'$. Let $S_0$ be a strategy, and $k$ its first move. By $\Delta^0_1$ determinacy, $G(X_k, Y_k)$ is determined. If player 1 has a winning strategy in it, he plays $i = 0$ and follows it. Otherwise player 0 has one in $G(X_k, Y_k)$, and by :ref{#lem-descent-games} (2) player 1 has one in $G(Y_k, X_k)$; he plays $i = 1$ and follows it. In both cases, the play against $S_0$ is lost by player 0.

So player 1 has a winning strategy $S_1$. Let $Z = \{ k : S_1(\langle k \rangle) = 1 \}$, which exists by $\Delta^0_1$ comprehension. If $X_k$ is not a well-ordering, player 0 has a winning strategy in $G(X_k, Y_k)$ by :ref{#lem-descent-games} (1); if $S_1$ answered $k$ with $0$, player 0 could open with $k$ and then follow that strategy, and win against $S_1$. So $S_1(\langle k \rangle) = 1$ and $k \in Z$. If $Y_k$ is not a well-ordering, player 0 wins $G(Y_k, X_k)$, and in the same way $S_1(\langle k \rangle) = 0$ and $k \notin Z$. So $Z$ separates $\varphi_1$ from $\varphi_0$.
:::

:::quiz[clopen determinacy and separation]
Why does the reversal use the clopen game $G'$, rather than the games $G(X_k, Y_k)$ one at a time?

- [x] Because a separating set must decide all $k$ at once, and one winning strategy for $G'$ contains, in its answers to the first moves, a choice for every $k$; determinacy of each game separately gives one strategy per $k$, with no way to collect them.
- [ ] Because the games $G(X_k, Y_k)$ are not clopen.

  Each of them is clopen, since one of $X_k$ and $Y_k$ is a well-ordering.
- [ ] Because player 0 always wins $G(X_k, Y_k)$.

  He wins it when $X_k$ is ill-founded; when $Y_k$ is ill-founded, player 1 wins it.
:::

The same pattern, one strategy for a game that begins with the choice of an instance, turns determinacy of a class of games into a comprehension principle. Stronger determinacy statements give stronger systems: the determinacy of games whose winning set is the intersection of an open and a closed set is equivalent to $\Pi^1_1\text{-}\mathsf{CA}_0$ (Tanaka; Simpson, Section VI.5), and Friedman showed that Borel determinacy, which Martin proved in set theory, is not provable in second-order arithmetic.

::::exercise{#ex-clopen-aca difficulty=1 objective="Show that clopen determinacy implies arithmetic comprehension, with a game of three moves."}
Show in $\mathsf{RCA}_0$ that $\Delta^0_1$ determinacy implies $\mathsf{ACA}_0$. Use the game in which player 0 plays $k$, player 1 plays $n$, player 0 plays $m$, and player 0 wins if $g(n) \neq k$ and $g(m) = k$, for a given function $g$.

:::solution
The winning condition depends only on the first three moves, so it is clopen. Player 0 has no winning strategy: after his first move $k$, player 1 answers $n$ with $g(n) = k$ if there is one, and then player 0 cannot win; and if there is none, player 0 cannot find $m$ with $g(m) = k$. So player 1 has a winning strategy $S_1$. If $g(m) = k$ for some $m$, then $g(S_1(\langle k \rangle)) = k$: otherwise player 0 would win by playing $k$ and then $m$. Hence $k$ is in the range of $g$ if and only if $g(S_1(\langle k \rangle)) = k$, and the range exists by $\Delta^0_1$ comprehension. By :ref{#thm-aca-equivalents}, $\mathsf{ACA}_0$ follows.
:::
::::

## Notes and references

Open determinacy is due to Gale and Stewart (1953). The equivalence of $\mathsf{ATR}_0$ with open and clopen determinacy is due to Steel (1976), one of the earliest results of reverse mathematics. The proofs follow Simpson, Section V.8: :ref{#thm-open-determinacy-atr} is his Theorem V.8.2, :ref{#lem-descent-games} Lemma V.8.6, :ref{#ex-clopen-aca} Lemma V.8.5 and :ref{#thm-clopen-determinacy-atr} Theorem V.8.7, whose proof through $\Sigma^1_1$ separation is Simpson's. Dzhafarov and Mummert treat determinacy in Section 12.3. Tanaka (1990) proved the equivalence of $\Sigma^0_1 \wedge \Pi^0_1$ determinacy with $\Pi^1_1\text{-}\mathsf{CA}_0$, and Friedman (1971) the unprovability of Borel determinacy in second-order arithmetic.

- D. Gale and F. M. Stewart, *Infinite games with perfect information*, in *Contributions to the Theory of Games II*, Annals of Mathematics Studies 28, Princeton University Press, 1953, 245–266.
- J. R. Steel, *Determinateness and Subsystems of Analysis*, PhD thesis, University of California, Berkeley, 1976.
- K. Tanaka, *Weak axioms of determinacy and subsystems of analysis I: Δ⁰₂ games*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 36 (1990), 481–491.
- H. Friedman, *Higher set theory and mathematical practice*, Annals of Mathematical Logic 2 (1971), 325–357.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.8 and VI.5.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 12.3.

:::::exercises
::::exercise{#ex-descent-game-comparison difficulty=2 objective="Relate the descent games to comparisons of well-orderings."}
Let $X$ and $Y$ be well-orderings. Show in $\mathsf{ATR}_0$ that if $|X| \leq |Y|$, then player 1 has a winning strategy in $G(X, Y)$.

:::solution
Let $h$ be an isomorphism of $X$ onto an initial segment of $Y$. Player 1 answers each move $x$ of player 0 with $h(x)$. As long as player 0 plays a descending sequence $x_0 >_X x_1 >_X \cdots$, player 1 plays $h(x_0) >_Y h(x_1) >_Y \cdots$, which is descending. Player 0's sequence fails at some point, since $X$ is a well-ordering; at the round where it fails, player 0 is checked first, and loses. Formally, if $f(2j + 2) <_X f(2j)$ fails at the least such $j$, then player 1's sequence is descending up to $f(2j + 1) = h(f(2j))$, and player 0 loses. (Simpson, Exercise V.8.8, asks for the converse as well.)
:::
::::

::::exercise{#ex-finite-game difficulty=1 objective="Compute the levels of the hierarchy of winning positions on a game that player 0 wins in two rounds, and read off the strategy of Case 1."}
Consider the open game in which player 0 wins as soon as a position $\sigma$ of length $4$ with $\sigma(2) > \sigma(1)$ is reached: $W$ is the set of positions of even length at least $4$ with $\sigma(2) > \sigma(1)$. Compute, along $X = \{ 0 < 1 < 2 \}$, which positions of length $0$ and $2$ belong to $W_0$, $W_1$ and $W_2$, and give the strategy $S_0$ of Case 1.

:::solution
$W_0 = W$, since there is no $i <_X 0$; it contains no position of length $0$ or $2$. A position $\langle a, b \rangle$ is in $W_1$: the move $m = b + 1$ gives $\langle a, b, m, n \rangle \in W = W_0$ for every $n$. The empty position is not in $W_1$, since no position of length $2$ is in $W_0$; it is in $W_2$, since for any first move $a$ and every answer $b$, $\langle a, b \rangle \in W_1$. So $r(\langle\rangle) = 2$ and $r(\langle a, b \rangle) = 1$. The strategy of Case 1 plays the least $m$ that works: $S_0(\langle\rangle) = 0$ and $S_0(\langle a, b \rangle) = b + 1$; after two rounds, the position is in $W$.
:::
::::
:::::
