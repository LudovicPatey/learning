---
title: Problems and ω-reducibility
summary: Theorems of the form "every instance has a solution" seen as problems; Turing ideals satisfying a problem and ω-reducibility; ω-reducibility ignores induction; König's lemma and the jump; the game characterization of ω-reducibility.
duration: 40
prerequisites: [big-five/wkl0, pi01-classes/finitely-branching-trees, ramsey-theorem/cohesiveness, induction-conservation/pigeonhole]
---

Most theorems studied in reverse mathematics have the form $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$ with $F$ and $G$ arithmetic: every infinite binary tree has a path, every coloring of pairs has an infinite homogeneous set. Such a theorem can be seen as a **problem**: its **instances** are the sets $X$ with $F(X)$, and the **solutions** to $X$ are the sets $Y$ with $G(X, Y)$. Comparing theorems over $\mathsf{RCA}_0$ in ω-models amounts to comparing the computational power of their solutions.

This course studies three reducibilities between problems. In each of them, $\mathsf P$ reduces to $\mathsf Q$ if solutions to $\mathsf P$ can be computed from solutions to $\mathsf Q$; they differ in how $\mathsf Q$ may be used. **ω-reducibility** allows any finite number of applications of $\mathsf Q$, each chosen after seeing the solutions to the previous ones. **Computable reducibility** allows a single application. **Weihrauch reducibility** allows a single application, carried out by algorithms fixed in advance for all instances. Each is finer than the previous one, and each separation result says more than the previous one: a problem that is not ω-reducible to another is not reducible to it in any of the three senses. This lesson and the next treat ω-reducibility, the next two computable reducibility, and the last two Weihrauch reducibility.

## Problems

:::definition{#def-problem}
A **problem** $\mathsf P$ consists of a class $\mathrm{dom}\, \mathsf P \subseteq \mathcal P(\nat)$ of **instances**, and, for every instance $X$, a non-empty class $\mathsf P(X) \subseteq \mathcal P(\nat)$ of **solutions** to $X$.
:::

Numbers, finite sequences, functions, trees and sequences of sets are coded by sets of numbers in the usual way, so that a problem may have instances and solutions of any of these kinds. Some examples, used throughout the course:

- $\mathsf{Id}$: every set is an instance, and its only solution is itself.
- $\mathsf J$: every set $X$ is an instance, and its only solution is $X'$.
- $\mathsf{WKL}$: the instances are the infinite binary trees, the solutions their infinite paths.
- $\mathsf{KL}$: the instances are the infinite finitely branching trees $T \subseteq \nat^{<\nat}$, the solutions their infinite paths.
- $\mathsf{RT}^n_k$: the instances are the colorings $f : [\nat]^n \to k$, the solutions their infinite homogeneous sets.
- $\mathsf{RT}^1_{<\infty}$: the instances are the pairs $(k, f)$ with $k \geq 1$ and $f : \nat \to k$, the solutions the infinite homogeneous sets for $f$.
- $\mathsf{COH}$: the instances are the sequences of sets $\vec R$, the solutions the $\vec R$-cohesive sets (:ref{#def-cohesive}).

A problem is more than a theorem: it also fixes how instances and solutions are presented. $\mathsf{RT}^1_{<\infty}$ and the problems $\mathsf{RT}^1_k$ come from the same combinatorial fact, but the number of colors is part of an instance of the first and fixed in advance for the others. The difference matters for the finer reducibilities of the next lessons.

:::definition{#def-satisfies-problem}
A Turing ideal $\mathcal I$ **satisfies** a problem $\mathsf P$, written $\mathcal I \models \mathsf P$, if every instance of $\mathsf P$ in $\mathcal I$ has a solution in $\mathcal I$.
:::

For example, the Turing ideal $\mathrm{REC}$ of the computable sets satisfies $\mathsf{RT}^1_2$: a computable coloring $f : \nat \to 2$ computes its two color classes, and one of them is infinite. It does not satisfy $\mathsf{WKL}$, since some infinite computable binary tree has no computable path (:ref{#thm-dnc2-no-computable}).

When $\mathsf P$ comes from a theorem $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$ with $F, G$ arithmetic, $\mathcal I \models \mathsf P$ exactly when the ω-model $\mathcal I$ satisfies the theorem, by absoluteness of arithmetic formulas (:ref{#prop-omega-absolute}). For instance, the Turing ideals satisfying $\mathsf J$ are the jump ideals, and those satisfying $\mathsf{WKL}$ are the Scott ideals (:ref{#def-scott-ideal}).

## ω-reducibility

:::definition{#def-omega-reducible}
A problem $\mathsf P$ is **ω-reducible** to a problem $\mathsf Q$, written $\mathsf P \leq_\omega \mathsf Q$, if every Turing ideal satisfying $\mathsf Q$ satisfies $\mathsf P$.
:::

The relation $\leq_\omega$ is reflexive and transitive, since it is defined by inclusion between classes of Turing ideals. We write $\mathsf P \equiv_\omega \mathsf Q$ if $\mathsf P \leq_\omega \mathsf Q$ and $\mathsf Q \leq_\omega \mathsf P$. A Turing ideal can be thought of as the collection of sets that a mathematician with given computational resources can construct; $\mathsf P \leq_\omega \mathsf Q$ says that whoever can always solve $\mathsf Q$ can always solve $\mathsf P$.

For problems coming from theorems as above, $\mathsf P \leq_\omega \mathsf Q$ means that every ω-model of $\mathsf{RCA}_0 + \mathsf Q$ is a model of $\mathsf P$. In particular, if $\mathsf{RCA}_0 + \mathsf Q$ proves $\mathsf P$, then $\mathsf P \leq_\omega \mathsf Q$; so a proof of $\mathsf P \not\leq_\omega \mathsf Q$ shows that $\mathsf{RCA}_0 + \mathsf Q$ does not prove $\mathsf P$. The converse fails, since implications over $\mathsf{RCA}_0$ must also hold in non-standard models. For example, every Turing ideal satisfies $\mathsf{RT}^1_{<\infty}$, since an instance $(k, f)$ computes the $k$ color classes of $f$, one of which is infinite; so $\mathsf{RT}^1_{<\infty} \leq_\omega \mathsf{Id}$. But $\mathsf{RCA}_0$ does not prove $\mathsf{RT}^1_{<\infty}$, which is equivalent to $\Sigma^0_2$ collection (:ref{#thm-hirst} and the discussion that follows it). ω-reducibility does not see induction.

The following proposition compares König's lemma with the jump. Its proof shows why the jump must be used twice for finitely branching trees. For a binary tree $T$, a node is extendible if it has extensions of every length, a $\Pi^0_1(T)$ property; so $T'$ knows the extendible nodes, and can follow them to build a path. For a finitely branching tree, the successors of a node are not bounded by a $T$-computable function, and "having an extension of length $n$" is only $\Sigma^0_1(T)$. A first jump computes the list of successors of each node; relative to this list the tree becomes bounded, and a second jump finds the extendible nodes.

:::proposition{#prop-kl-j}
$\mathsf{KL} \equiv_\omega \mathsf J$, and $\mathsf{WKL} \leq_\omega \mathsf J$.
:::

:::proof{of=prop-kl-j}
($\mathsf{KL} \leq_\omega \mathsf J$) Let $\mathcal I$ be a jump ideal and $T \in \mathcal I$ an infinite finitely branching tree. Then $T'' \in \mathcal I$. The set $T''$ is PA relative to $T'$, since $T''$ computes the leftmost path of every non-empty $\Pi^0_1(T')$ class (:ref{#prop-leftmost-path}, relativized). By :ref{#thm-konig-strength} relativized to $T$, it computes a path through $T$, which belongs to $\mathcal I$.

($\mathsf J \leq_\omega \mathsf{KL}$) Let $\mathcal I \models \mathsf{KL}$ and $X \in \mathcal I$. By :ref{#thm-finitely-branching-jump} relativized to $X$, there is an $X$-computable finitely branching tree with a unique path, which computes $X'$. The tree belongs to $\mathcal I$, so does its path, and so does $X'$.

($\mathsf{WKL} \leq_\omega \mathsf J$) Let $\mathcal I$ be a jump ideal and $T \in \mathcal I$ an infinite binary tree. Its leftmost path is computable in $T'$ (:ref{#prop-leftmost-path}, relativized), so it belongs to $\mathcal I$.
:::

In the first reduction, two instances of $\mathsf J$ were used, one after the other, to solve one instance of $\mathsf{KL}$; ω-reducibility does not see this. Computable reducibility, two lessons ahead, counts the instances.

## Reduction games

Hirschfeldt and Jockusch characterized ω-reducibility by a game between two players. In the game $G(\mathsf Q \rightarrow \mathsf P)$, Player 1 tries to show that $\mathsf Q$ does not help to solve $\mathsf P$, and Player 2 tries to solve $\mathsf P$ using $\mathsf Q$. Player 1 chooses the instance of $\mathsf P$ and the solutions to the instances of $\mathsf Q$: Player 2 must succeed whatever solutions she receives.

:::definition{#def-reduction-game}
The game $G(\mathsf Q \rightarrow \mathsf P)$ is played as follows. First, Player 1 plays an instance $X_0$ of $\mathsf P$. At each round $n \geq 1$, let $Z_{n-1} = X_0 \oplus Y_1 \oplus \cdots \oplus Y_{n-1}$, where $Y_1, \dots, Y_{n-1}$ were played before. Player 2 either plays a solution to $X_0$ computable in $Z_{n-1}$, and then wins, or plays an instance $V_n$ of $\mathsf Q$ computable in $Z_{n-1}$; then Player 1 plays a solution $Y_n$ to $V_n$. If Player 2 can play neither, or if the game never ends, Player 1 wins.
:::

:::figure[A play of $G(\mathsf J \rightarrow \mathsf{KL})$ following the proof of :ref{#prop-kl-j}. Player 2 asks for the jump of $T$, then for the jump of $T'$, and wins at round 3 with a path computable in $T''$. The game for $\mathsf J \rightarrow \mathsf{WKL}$ would end at round 2.]
<svg class="fig" viewBox="0 0 600 282" width="600" role="img" aria-label="The moves of the game G(J to KL): Player 1 plays a tree T, Player 2 plays T and T prime as instances of the jump, Player 1 answers with T prime and T double prime, and Player 2 wins with a path computable in T double prime"><defs><marker id="ah-game" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker><marker id="ah-game-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><text x="210" y="18" text-anchor="middle" class="label">Player 1</text><text x="390" y="18" text-anchor="middle" class="label">Player 2</text><rect x="184" y="31" width="52" height="28" rx="6" class="cell"/><text x="210" y="50" text-anchor="middle" class="math" font-size="17">T</text><text x="174" y="49" text-anchor="end" class="label">instance of KL</text><line x1="236" y1="45" x2="362" y2="83" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-game)"/><rect x="364" y="71" width="52" height="28" rx="6" class="cell"/><text x="390" y="90" text-anchor="middle" class="math" font-size="17">T</text><text x="426" y="89" text-anchor="start" class="label">instance of J</text><line x1="364" y1="85" x2="238" y2="123" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-game)"/><rect x="184" y="111" width="52" height="28" rx="6" class="cell"/><text x="210" y="130" text-anchor="middle" class="math" font-size="17">T′</text><text x="174" y="129" text-anchor="end" class="label">solution</text><line x1="236" y1="125" x2="362" y2="163" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-game)"/><rect x="364" y="151" width="52" height="28" rx="6" class="cell"/><text x="390" y="170" text-anchor="middle" class="math" font-size="17">T′</text><text x="426" y="169" text-anchor="start" class="label">instance of J</text><line x1="364" y1="165" x2="238" y2="203" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-game)"/><rect x="184" y="191" width="52" height="28" rx="6" class="cell"/><text x="210" y="210" text-anchor="middle" class="math" font-size="17">T″</text><text x="174" y="209" text-anchor="end" class="label">solution</text><line x1="236" y1="205" x2="362" y2="243" class="accent-stroke" stroke-width="1.2" marker-end="url(#ah-game-a)"/><rect x="364" y="231" width="52" height="28" rx="6" class="head-cell"/><text x="390" y="250" text-anchor="middle" class="math" font-size="17">P</text><text x="426" y="249" text-anchor="start" class="label">path through T</text><line x1="40" y1="32" x2="40" y2="58" class="axis"/><text x="48" y="49.0" text-anchor="start" class="label">start</text><line x1="40" y1="72" x2="40" y2="138" class="axis"/><text x="48" y="109.0" text-anchor="start" class="label">round 1</text><line x1="40" y1="152" x2="40" y2="218" class="axis"/><text x="48" y="189.0" text-anchor="start" class="label">round 2</text><line x1="40" y1="232" x2="40" y2="258" class="axis"/><text x="48" y="249.0" text-anchor="start" class="label">round 3</text><text x="426" y="104" text-anchor="start" class="label">computable in T</text><text x="426" y="184" text-anchor="start" class="label">computable in T ⊕ T′</text><text x="426" y="264" text-anchor="start" class="label">computable in T ⊕ T′ ⊕ T″</text></svg>
:::

:::theorem[Hirschfeldt, Jockusch]{#thm-game-omega}
$\mathsf P \leq_\omega \mathsf Q$ if and only if Player 2 has a winning strategy in $G(\mathsf Q \rightarrow \mathsf P)$.
:::

The idea of the proof: if Player 2 plays every instance of $\mathsf Q$ that she can compute, each at some later round, the sets computable from the moves of an infinite play form a Turing ideal satisfying $\mathsf Q$. Conversely, a Turing ideal satisfying $\mathsf Q$ but not $\mathsf P$ tells Player 1 how to play.

:::proof{of=thm-game-omega}
($\Rightarrow$) Suppose $\mathsf P \leq_\omega \mathsf Q$. Fix a bijection $n \mapsto (n_0, n_1)$ from $\{ 1, 2, \dots \}$ to $\nat^2$ with $n_0 < n$. At round $n$, Player 2 wins if possible. Otherwise, if $\Phi^{Z_{n_0}}_{n_1}$ is total and an instance of $\mathsf Q$, she plays it; it is computable in $Z_{n-1}$. Otherwise she plays any instance of $\mathsf Q$ computable in $X_0$. Such an instance exists if she has not won at round $1$: otherwise the ideal $\{ Y : Y \leq_T X_0 \}$ would satisfy $\mathsf Q$ vacuously, hence $\mathsf P$, and $X_0$ would compute a solution to itself.

Suppose that the game never ends, and let $\mathcal I = \{ Y : \exists n\ Y \leq_T Z_n \}$, a Turing ideal containing $X_0$. Every instance of $\mathsf Q$ in $\mathcal I$ is $\Phi^{Z_m}_e$ for some $m$ and $e$, was played at the round $n$ with $(n_0, n_1) = (m, e)$, and received a solution in $\mathcal I$. So $\mathcal I \models \mathsf Q$, hence $\mathcal I \models \mathsf P$, and $X_0$ has a solution computable in some $Z_n$; Player 2 would have played it at round $n + 1$. So the strategy wins.

($\Leftarrow$) Suppose $\mathsf P \not\leq_\omega \mathsf Q$: some Turing ideal $\mathcal I$ satisfies $\mathsf Q$ and contains an instance $X_0$ of $\mathsf P$ without solution in $\mathcal I$. Player 1 plays $X_0$, and answers every instance $V_n$ with a solution in $\mathcal I$. By induction, every $Z_n$ belongs to $\mathcal I$, so the instances played by Player 2 belong to $\mathcal I$, and she never finds a solution to $X_0$. Player 1 wins against every strategy.
:::

A winning strategy of Player 2 need not bound the number of rounds: it wins every play after finitely many rounds, but the number may depend on the instance and on the solutions received. The game makes this number visible: in the reduction of $\mathsf{KL}$ to $\mathsf J$, Player 2 wins in three rounds, playing $T$ and then $T'$. Bounding the number of rounds leads to the reducibilities of the lesson after next; the next lesson develops the main method for proving that $\mathsf P \not\leq_\omega \mathsf Q$.

:::quiz[the reduction game]
In the proof of ($\Leftarrow$) in :ref{#thm-game-omega}, why does Player 2 never find a solution to $X_0$?

- [x] Because all the sets played stay in the Turing ideal $\mathcal I$, which contains no solution to $X_0$, and everything Player 2 may play is computable from them.
- [ ] Because Player 1 plays solutions that do not compute anything.

  Player 1 plays solutions in $\mathcal I$; they may compute many sets, but only sets of $\mathcal I$.
- [ ] Because $\mathsf Q$ does not preserve any weakness property.

  The argument uses no property of $\mathsf Q$ beyond the existence of a Turing ideal witnessing $\mathsf P \not\leq_\omega \mathsf Q$.
:::


## Exercises

::::exercise{difficulty=1}
Show that Player 2 has a strategy in $G(\mathsf{KL} \rightarrow \mathsf J)$ that wins at round $2$, after a single instance of $\mathsf{KL}$.

:::solution
Let $X$ be the instance of $\mathsf J$ played by Player 1. At round $1$, Player 2 plays the $X$-computable finitely branching tree of :ref{#thm-finitely-branching-jump}, relativized to $X$. It has a unique path, so Player 1 must play it, and this path computes $X'$. At round $2$, Player 2 plays $X'$, which is computable in $X \oplus Y_1$.
:::
::::

::::exercise{difficulty=1}
Show that $\mathsf{RT}^n_k \leq_\omega \mathsf J$ for all $n, k \geq 1$.

:::solution
Let $\mathcal I$ be a jump ideal and $f \in \mathcal I$ a coloring of $[\nat]^n$ with $k$ colors. Then $f^{(n)} \in \mathcal I$. It is PA relative to $f^{(n-1)}$, since it computes the leftmost member of every non-empty $\Pi^0_1(f^{(n-1)})$ class (:ref{#prop-leftmost-path}, relativized). By :ref{#thm-jockusch-upper}, $f^{(n)}$ computes an infinite homogeneous set for $f$, which belongs to $\mathcal I$.
:::
::::

## Notes and references

The view of theorems as problems goes back to the computable analysis of Weihrauch and to the work of Jockusch on Ramsey's theorem. ω-reducibility and the reduction games are studied by Hirschfeldt and Jockusch, whose paper compares all the reducibilities of this course. Dzhafarov and Mummert give a systematic treatment: problems in Section 3.1, ω-model reducibility in Section 4.6, and the games in Section 4.7 (Theorem 4.7.5). Hirschfeldt, *Slicing the Truth*, Section 2.2, introduces problems and their reductions, and Section 4.5 treats ω-models.

- D. R. Hirschfeldt and C. G. Jockusch, *On notions of computability-theoretic reduction between Π¹₂ principles*, Journal of Mathematical Logic 16 (2016), 1650002.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 3.1, 4.6 and 4.7.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Sections 2.2 and 4.5.
