---
title: Problems and ω-reducibility
summary: Theorems of the form "every instance has a solution" seen as problems; Turing ideals satisfying a problem and ω-reducibility; König's lemma and the jump; weakness properties and their preservation, the standard method for separations; the game characterization of ω-reducibility.
duration: 40
prerequisites: [big-five/wkl0, pi01-classes/finitely-branching-trees, ramsey-theorem/seetapun]
---

Most theorems studied in reverse mathematics have the form $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$ with $F$ and $G$ arithmetic: every infinite binary tree has a path, every coloring of pairs has an infinite homogeneous set. Such a theorem can be seen as a **problem**: its **instances** are the sets $X$ with $F(X)$, and the **solutions** to $X$ are the sets $Y$ with $G(X, Y)$. Comparing theorems over $\mathsf{RCA}_0$ in ω-models amounts to comparing the computational power of their solutions. This course studies three reducibilities between problems, of increasing precision: ω-reducibility, computable reducibility and Weihrauch reducibility.

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

:::definition{#def-satisfies-problem}
A Turing ideal $\mathcal I$ **satisfies** a problem $\mathsf P$, written $\mathcal I \models \mathsf P$, if every instance of $\mathsf P$ in $\mathcal I$ has a solution in $\mathcal I$.
:::

When $\mathsf P$ comes from a theorem $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$ with $F, G$ arithmetic, $\mathcal I \models \mathsf P$ exactly when the ω-model $\mathcal I$ satisfies the theorem, by absoluteness of arithmetic formulas (:ref{#prop-omega-absolute}). For instance, the Turing ideals satisfying $\mathsf J$ are the jump ideals, and those satisfying $\mathsf{WKL}$ are the Scott ideals (:ref{#def-scott-ideal}).

:::definition{#def-omega-reducible}
A problem $\mathsf P$ is **ω-reducible** to a problem $\mathsf Q$, written $\mathsf P \leq_\omega \mathsf Q$, if every Turing ideal satisfying $\mathsf Q$ satisfies $\mathsf P$.
:::

For problems coming from theorems as above, $\mathsf P \leq_\omega \mathsf Q$ means that every ω-model of $\mathsf{RCA}_0 + \mathsf Q$ is a model of $\mathsf P$. In particular, if $\mathsf{RCA}_0 + \mathsf Q$ proves $\mathsf P$, then $\mathsf P \leq_\omega \mathsf Q$; so a proof of $\mathsf P \not\leq_\omega \mathsf Q$ shows that $\mathsf{RCA}_0 + \mathsf Q$ does not prove $\mathsf P$. The converse fails in general, since implications over $\mathsf{RCA}_0$ must also hold in non-standard models.

:::proposition{#prop-kl-j}
$\mathsf{KL} \equiv_\omega \mathsf J$, and $\mathsf{WKL} \leq_\omega \mathsf J$.
:::

:::proof{of=prop-kl-j}
($\mathsf{KL} \leq_\omega \mathsf J$) Let $\mathcal I$ be a jump ideal and $T \in \mathcal I$ an infinite finitely branching tree. Then $T'' \in \mathcal I$. The set $T''$ is PA relative to $T'$, since $T''$ computes the leftmost path of every non-empty $\Pi^0_1(T')$ class (:ref{#prop-leftmost-path}, relativized). By :ref{#thm-konig-strength} relativized to $T$, it computes a path through $T$, which belongs to $\mathcal I$.

($\mathsf J \leq_\omega \mathsf{KL}$) Let $\mathcal I \models \mathsf{KL}$ and $X \in \mathcal I$. By :ref{#thm-finitely-branching-jump} relativized to $X$, there is an $X$-computable finitely branching tree with a unique path, which computes $X'$. The tree belongs to $\mathcal I$, so does its path, and so does $X'$.

($\mathsf{WKL} \leq_\omega \mathsf J$) Let $\mathcal I$ be a jump ideal and $T \in \mathcal I$ an infinite binary tree. Its leftmost path is computable in $T'$ (:ref{#prop-leftmost-path}, relativized), so it belongs to $\mathcal I$.
:::

In the first reduction, two instances of $\mathsf J$ were used, one after the other, to solve one instance of $\mathsf{KL}$; ω-reducibility does not see this. The next lesson introduces a reducibility that counts the instances.

## Weakness properties and preservation

To show $\mathsf P \not\leq_\omega \mathsf Q$, one builds a Turing ideal that satisfies $\mathsf Q$ and contains an instance of $\mathsf P$ without solution. The construction of :ref{#thm-low-scott} is typical: one closes an ideal under solutions to instances of $\mathsf Q$, while keeping all its members in a class of "weak" sets. The method can be stated once and for all.

:::definition{#def-weakness}
A **weakness property** is a class $\mathcal W \subseteq \mathcal P(\nat)$ closed downwards under Turing reducibility: if $X \in \mathcal W$ and $Y \leq_T X$, then $Y \in \mathcal W$. A problem $\mathsf Q$ **preserves** $\mathcal W$ if for every $Z \in \mathcal W$ and every instance $X \leq_T Z$ of $\mathsf Q$, there is a solution $Y$ to $X$ with $Z \oplus Y \in \mathcal W$.
:::

Examples of weakness properties are the low sets, the computably dominated sets, the sets that do not compute a given set $C$, and the class of sets computable in a given set. By the low basis theorem (:ref{#thm-low-basis}) relativized to a low set $Z$, every infinite $Z$-computable binary tree has a path $Y$ with $(Z \oplus Y)' \leq_T Z' \leq_T \emptyset'$, so $\mathsf{WKL}$ preserves the class of low sets, as in the proof of :ref{#thm-low-scott}; by the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}), it preserves $\{ Z : C \not\leq_T Z \}$ for every $C$.

:::lemma{#lem-preservation-ideal}
If $\mathsf Q$ preserves $\mathcal W$, then for every $X \in \mathcal W$ there is a Turing ideal $\mathcal I \subseteq \mathcal W$ containing $X$ and satisfying $\mathsf Q$.
:::

:::proof{of=lem-preservation-ideal}
Fix a bijection $n \mapsto (n_0, n_1)$ from $\nat$ to $\nat^2$ with $n_0 \leq n$. We build $Z_0 \leq_T Z_1 \leq_T \cdots$ in $\mathcal W$, with $Z_0 = X$. Given $Z_n$, let $(p, e) = (n_0, n_1)$. If $\Phi^{Z_p}_e$ is total and is an instance of $\mathsf Q$, it is computable in $Z_n$, and by preservation there is a solution $Y$ with $Z_n \oplus Y \in \mathcal W$; let $Z_{n+1} = Z_n \oplus Y$. Otherwise let $Z_{n+1} = Z_n$.

Let $\mathcal I = \{ Y : \exists n\ Y \leq_T Z_n \}$. It is a Turing ideal, since the sequence is increasing, it contains $X$, and $\mathcal I \subseteq \mathcal W$ by downward closure. If $V \in \mathcal I$ is an instance of $\mathsf Q$, then $V = \Phi^{Z_p}_e$ for some $p$ and $e$; at the step $n$ with $(n_0, n_1) = (p, e)$, a solution to $V$ was added, and it belongs to $\mathcal I$.
:::

:::theorem{#thm-preservation-separation}
If $\mathsf Q$ preserves a weakness property $\mathcal W$ and $\mathsf P$ does not, then $\mathsf P \not\leq_\omega \mathsf Q$.
:::

:::proof{of=thm-preservation-separation}
Since $\mathsf P$ does not preserve $\mathcal W$, there are $Z \in \mathcal W$ and an instance $X \leq_T Z$ of $\mathsf P$ such that $Z \oplus Y \notin \mathcal W$ for every solution $Y$ to $X$. By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ containing $Z$ and satisfying $\mathsf Q$. Then $X \in \mathcal I$. If a solution $Y$ belonged to $\mathcal I$, so would $Z \oplus Y$, which is not in $\mathcal W \supseteq \mathcal I$. So $\mathcal I$ does not satisfy $\mathsf P$.
:::

:::corollary{#cor-wkl-not-j}
$\mathsf J \not\leq_\omega \mathsf{WKL}$, $\mathsf{KL} \not\leq_\omega \mathsf{WKL}$, and $\mathsf J \not\leq_\omega \mathsf{RT}^2_2$.
:::

:::proof{of=cor-wkl-not-j}
Let $\mathcal W = \{ Z : \emptyset' \not\leq_T Z \}$. The problem $\mathsf{WKL}$ preserves $\mathcal W$ by the cone avoidance basis theorem, relativized to $Z$. The problem $\mathsf J$ does not: $\emptyset \in \mathcal W$ is an instance whose only solution is $\emptyset'$, and $\emptyset \oplus \emptyset' \notin \mathcal W$. So $\mathsf J \not\leq_\omega \mathsf{WKL}$ by :ref{#thm-preservation-separation}. By :ref{#prop-kl-j}, $\mathsf{KL} \equiv_\omega \mathsf J$, so $\mathsf{KL} \not\leq_\omega \mathsf{WKL}$ too. The problem $\mathsf{RT}^2_2$ preserves $\mathcal W$ by Seetapun's theorem (:ref{#thm-seetapun}) with $C = \emptyset'$: for every $Z \in \mathcal W$, every $Z$-computable coloring of pairs has an infinite homogeneous set $H$ with $\emptyset' \not\leq_T Z \oplus H$. So $\mathsf J \not\leq_\omega \mathsf{RT}^2_2$, again by :ref{#thm-preservation-separation}.
:::

The property used here is **cone avoidance**: a problem $\mathsf Q$ avoids cones if, for every $Z$ and every $C \not\leq_T Z$, every $Z$-computable instance has a solution $Y$ with $C \not\leq_T Z \oplus Y$. Downey, Greenberg, Harrison-Trainor, Patey and Turetsky (2022) showed that a problem that avoids one cone at a time also avoids countably many cones simultaneously; we admit this result.

:::quiz[preservation]
In the proof of :ref{#lem-preservation-ideal}, why is each instance $\Phi^{Z_p}_e$ handled at a step $n \geq p$?

- [x] Because the solution is added to $Z_n$, which must compute the instance for preservation to apply; $Z_p \leq_T Z_n$ holds when $p \leq n$, since the sequence is increasing.
- [ ] Because the instances must be handled in increasing order.

  The order is a bookkeeping device; what matters is that each pair $(p, e)$ is handled at some step $n \geq p$.
- [ ] Because $\Phi^{Z_p}_e$ may be partial.

  Partial functions are skipped; the condition $p \leq n$ concerns the total ones.

---

Why does a weakness property need to be closed downwards?

- [x] So that the Turing ideal generated by the sequence $Z_n$, which contains every set computable in some $Z_n$, stays inside $\mathcal W$.
- [ ] So that $\mathcal W$ is a Turing ideal.

  A weakness property need not be closed under join: the low sets are not.
- [ ] So that $\mathsf Q$ has solutions in $\mathcal W$.

  This is the preservation hypothesis.
:::

## Reduction games

Hirschfeldt and Jockusch characterized ω-reducibility by a game between two players. In the game $G(\mathsf Q \rightarrow \mathsf P)$, Player 1 tries to show that $\mathsf Q$ does not help to solve $\mathsf P$, and Player 2 tries to solve $\mathsf P$ using $\mathsf Q$.

:::definition{#def-reduction-game}
The game $G(\mathsf Q \rightarrow \mathsf P)$ is played as follows. First, Player 1 plays an instance $X_0$ of $\mathsf P$. At each round $n \geq 1$, let $Z_{n-1} = X_0 \oplus Y_1 \oplus \cdots \oplus Y_{n-1}$, where $Y_1, \dots, Y_{n-1}$ were played before. Player 2 either plays a solution to $X_0$ computable in $Z_{n-1}$, and then wins, or plays an instance $V_n$ of $\mathsf Q$ computable in $Z_{n-1}$; then Player 1 plays a solution $Y_n$ to $V_n$. If Player 2 can play neither, or if the game never ends, Player 1 wins.
:::

:::theorem[Hirschfeldt, Jockusch]{#thm-game-omega}
$\mathsf P \leq_\omega \mathsf Q$ if and only if Player 2 has a winning strategy in $G(\mathsf Q \rightarrow \mathsf P)$.
:::

:::proof{of=thm-game-omega}
($\Rightarrow$) Suppose $\mathsf P \leq_\omega \mathsf Q$. Fix a bijection $n \mapsto (n_0, n_1)$ from $\{ 1, 2, \dots \}$ to $\nat^2$ with $n_0 < n$. At round $n$, Player 2 wins if possible. Otherwise, if $\Phi^{Z_{n_0}}_{n_1}$ is total and an instance of $\mathsf Q$, she plays it; it is computable in $Z_{n-1}$. Otherwise she plays any instance of $\mathsf Q$ computable in $X_0$. Such an instance exists if she has not won at round $1$: otherwise the ideal $\{ Y : Y \leq_T X_0 \}$ would satisfy $\mathsf Q$ vacuously, hence $\mathsf P$, and $X_0$ would compute a solution to itself.

Suppose that the game never ends, and let $\mathcal I = \{ Y : \exists n\ Y \leq_T Z_n \}$, a Turing ideal containing $X_0$. Every instance of $\mathsf Q$ in $\mathcal I$ is $\Phi^{Z_m}_e$ for some $m$ and $e$, was played at the round $n$ with $(n_0, n_1) = (m, e)$, and received a solution in $\mathcal I$. So $\mathcal I \models \mathsf Q$, hence $\mathcal I \models \mathsf P$, and $X_0$ has a solution computable in some $Z_n$; Player 2 would have played it at round $n + 1$. So the strategy wins.

($\Leftarrow$) Suppose $\mathsf P \not\leq_\omega \mathsf Q$: some Turing ideal $\mathcal I$ satisfies $\mathsf Q$ and contains an instance $X_0$ of $\mathsf P$ without solution in $\mathcal I$. Player 1 plays $X_0$, and answers every instance $V_n$ with a solution in $\mathcal I$. By induction, every $Z_n$ belongs to $\mathcal I$, so the instances played by Player 2 belong to $\mathcal I$, and she never finds a solution to $X_0$. Player 1 wins against every strategy.
:::

The game makes the number of applications of $\mathsf Q$ visible: in the reduction of $\mathsf{KL}$ to $\mathsf J$, Player 2 wins in three rounds, playing $T$ and then $T'$. Counting rounds leads to the reducibilities of the next lesson.

## Exercises

::::exercise{#ex-wkl-kl-rt22 difficulty=1}
Show that $\mathsf{WKL} \leq_\omega \mathsf{KL}$ but $\mathsf{KL} \not\leq_\omega \mathsf{WKL}$, and that $\mathsf{RT}^2_2 \not\leq_\omega \mathsf{WKL}$.

:::solution
A Turing ideal satisfying $\mathsf{KL}$ is a jump ideal by :ref{#prop-kl-j}, since $\mathsf J \leq_\omega \mathsf{KL}$, so it satisfies $\mathsf{WKL}$, since $\mathsf{WKL} \leq_\omega \mathsf J$. The second statement is :ref{#cor-wkl-not-j}. For the third, $\mathsf{WKL}$ preserves the class of low sets; by :ref{#thm-jockusch-no-delta2}, there is a computable instance of $\mathsf{RT}^2_2$ without $\Delta^0_2$ solution, in particular without low solution; taking $Z = \emptyset$, which is low, $\mathsf{RT}^2_2$ does not preserve lowness. Apply :ref{#thm-preservation-separation}.
:::
::::

::::exercise{difficulty=2}
Show that if $\mathsf P \leq_\omega \mathsf Q$ and $\mathsf Q$ preserves a weakness property $\mathcal W$, then $\mathsf P$ preserves $\mathcal W$. Deduce :ref{#thm-preservation-separation} again.

:::solution
Let $Z \in \mathcal W$ and $X \leq_T Z$ an instance of $\mathsf P$. By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ containing $Z$ and satisfying $\mathsf Q$. It satisfies $\mathsf P$, and contains $X$, so it contains a solution $Y$ to $X$, and $Z \oplus Y \in \mathcal I \subseteq \mathcal W$. So $\mathsf P$ preserves $\mathcal W$. Contrapositively, if $\mathsf Q$ preserves $\mathcal W$ and $\mathsf P$ does not, then $\mathsf P \not\leq_\omega \mathsf Q$.
:::
::::

## Notes and references

The view of theorems as problems goes back to the computable analysis of Weihrauch and to the work of Jockusch on Ramsey's theorem. ω-reducibility and the reduction games are studied by Hirschfeldt and Jockusch, whose paper compares all the reducibilities of this course; Dzhafarov and Mummert's book is a systematic treatment.

- D. R. Hirschfeldt and C. G. Jockusch, *On notions of computability-theoretic reduction between Π¹₂ principles*, Journal of Mathematical Logic 16 (2016), 1650002.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Chapters 3 and 4.
- R. Downey, N. Greenberg, M. Harrison-Trainor, L. Patey and D. Turetsky, *Relationships between computability-theoretic properties of problems*, Journal of Symbolic Logic 87 (2022), 47–71.
