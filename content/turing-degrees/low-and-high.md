---
title: Low and high sets
summary: Sets whose jump is as small or as large as possible; 1-generic sets are generalized low, so non-computable low sets exist; high sets that avoid a cone.
duration: 40
prerequisites: [limit-computability, finite-extensions]
---

For a set $A \leq_T \emptyset'$, monotonicity of the jump gives $\emptyset' \leq_T A' \leq_T \emptyset''$. The two extreme cases define two classes of sets. A set is **low** if its jump is as small as possible, $A' \equiv_T \emptyset'$: from the point of view of the jump, it cannot be distinguished from a computable set. A set is **high** if its jump is as large as possible, $A' \geq_T \emptyset''$: its jump has the power of the double jump. This lesson shows that both classes contain sets that are not trivial examples — non-computable low sets and incomplete high sets — and that the jump is therefore not injective on degrees.

## Low sets

:::definition{#def-low}
A set $A$ is **low** if $A' \leq_T \emptyset'$, equivalently $A' \equiv_T \emptyset'$.
:::

The two conditions are equivalent since $\emptyset' \leq_T A'$ for every $A$ (:ref{#cor-jump-degrees}).

:::proposition{#prop-low-basic}
1. Every computable set is low, and every low set is computable in $\emptyset'$.
2. If $B \leq_T A$ and $A$ is low, then $B$ is low.
3. No low set is Turing complete.
4. If $A$ is low, every $A$-c.e. set is computable in $\emptyset'$.
:::

:::proof{of=prop-low-basic}
1. If $A$ is computable, $A' \equiv_T \emptyset'$ by monotonicity of the jump. If $A$ is low, $A \leq_T A' \leq_T \emptyset'$.
2. $B' \leq_T A' \leq_T \emptyset'$.
3. If $\emptyset' \leq_T A$, then $\emptyset'' \leq_T A'$, and lowness would give $\emptyset'' \leq_T \emptyset'$, contradicting :ref{#thm-jump}.
4. An $A$-c.e. set is one-one reducible to $A'$ (:ref{#thm-jump}), which is computable in $\emptyset'$.
:::

Item 4 explains the name: for a low set $A$, computing relative to $A$ adds nothing at the level of the jump. Non-computable low sets are provided by genericity.

:::theorem{#thm-generic-low}
If $G$ is 1-generic, then $G' \leq_T G \oplus \emptyset'$.
:::

:::proof{of=thm-generic-low}
For each $e$, let $V_e = \{ \sigma : \Phi^\sigma_e(e)\converge \}$, a c.e. set of strings, uniformly in $e$. Consider the following procedure with oracle $G \oplus \emptyset'$. On input $e$, for $n = 0, 1, 2, \dots$, let $\sigma = G \uh n$, and

- ask $\emptyset'$ whether $\sigma \in V_e$; if so, answer $e \in G'$;
- ask $\emptyset'$ whether some extension of $\sigma$ belongs to $V_e$; if not, answer $e \notin G'$.

Both questions are c.e., uniformly in $e$ and $\sigma$, so $\emptyset'$ answers them. Since $G$ is 1-generic, some prefix of $G$ is in $V_e$ or has no extension in $V_e$, so the procedure terminates. The answers are correct: if $G \uh n \in V_e$, then $\Phi^G_e(e)\converge$ by :ref{#prop-oracle-stages}; if $G \uh n$ has no extension in $V_e$, then $\Phi^G_e(e)\diverge$, since otherwise $\Phi^{G \uh k}_e(e)\converge$ for some $k \geq n$, and $G \uh k$ is an extension of $G \uh n$ in $V_e$.
:::

Sets with $A' \equiv_T A \oplus \emptyset'$ are called **generalized low**: their jump is no more than what is required, namely $A$ itself together with $\emptyset'$. The theorem says that 1-generic sets are generalized low.

:::corollary{#cor-low-exists}
There is a non-computable low set. Consequently, the jump is not injective on degrees: there is $\abf > \obf$ with $\abf' = \obf'$.
:::

:::proof{of=cor-low-exists}
Let $G \leq_T \emptyset'$ be 1-generic (:ref{#prop-1-generic}). It is not computable, and $G' \leq_T G \oplus \emptyset' \equiv_T \emptyset'$.
:::

There are also non-computable low sets that are c.e.; their construction requires the priority method, and is given in the course on Post's problem.

:::quiz[1-generic sets are generalized low]
Why does the procedure in the proof of :ref{#thm-generic-low} need the oracle $G$, and not only $\emptyset'$?

- [x] To know the prefixes $G \uh n$ about which the questions are asked.

  $\emptyset'$ answers questions about strings, but it does not know which strings are prefixes of $G$. For $G \leq_T \emptyset'$, the oracle $G$ is redundant, which gives lowness.
- [ ] To decide whether $\Phi^G_e(e)$ converges.

  That is what the procedure computes; $G$ alone cannot decide it.
- [ ] Because $\emptyset'$ cannot answer c.e. questions about strings.

  It can: every c.e. question reduces to a membership question in $\emptyset'$.

---

Where is 1-genericity used?

- [x] To ensure that the procedure terminates: some prefix of $G$ either belongs to $V_e$ or has no extension in it.

  For an arbitrary set, it may happen that $\Phi^G_e(e)\diverge$ while every prefix has extensions in $V_e$; the procedure would then run forever.
- [ ] To ensure that the answers are correct.

  Correctness holds for every set; only termination needs genericity.
- [ ] To show that $V_e$ is c.e.

  $V_e$ is c.e. by definition.
:::

## High sets

:::definition{#def-high}
A set $A$ is **high** if $\emptyset'' \leq_T A'$.
:::

Historically, highness was defined for sets computable in $\emptyset'$, for which it means $A' \equiv_T \emptyset''$; the definition has since been extended to all sets. Every set computing $\emptyset'$ is high, by monotonicity of the jump. The interesting high sets are those that do not compute $\emptyset'$.

Highness is a strength property, and it is not obtained by diagonalization but by building a set whose jump computes $\emptyset''$. By the relativized limit lemma (:ref{#thm-limit-lemma}), $\emptyset'' \leq_T A'$ holds if $\emptyset''$ has an $A$-computable $\Delta^0_2$ approximation. The construction below builds $A$ so that its columns $A^{[x]} = \{ y : \langle x, y \rangle \in A \}$ are, from some point on, constant equal to $\emptyset''(x)$; then $\emptyset''(x) = \lim_y A(\langle x, y \rangle)$.

:::theorem{#thm-high-cone-avoidance}
For every non-computable set $C$, there is a high set $A$ with $C \not\leq_T A$.
:::

:::proof{of=thm-high-cone-avoidance}
*Conditions.* A **condition** is a pair $(\sigma, m)$ of a string and an integer. It represents the sets
$$
[\sigma, m] = \{ X \succ \sigma : X(\langle x, y \rangle) = \emptyset''(x) \text{ for every } \langle x, y \rangle \geq |\sigma| \text{ with } x < m \}:
$$
beyond $\sigma$, the columns $x < m$ are fixed to their limit value. A condition $(\tau, n)$ **extends** $(\sigma, m)$ if $n \geq m$ and $[\tau, n] \subseteq [\sigma, m]$; for $n = m$, this means that $\sigma \preceq \tau$ and $\tau(\langle x, y \rangle) = \emptyset''(x)$ for every position $\langle x, y \rangle$ with $|\sigma| \leq \langle x, y \rangle < |\tau|$ and $x < m$. Every set $[\sigma, m]$ is non-empty. For a fixed $m$, the relation "$(\tau, m)$ extends $(\sigma, m)$" is computable: it only involves the finite string $\emptyset'' \uh m$, which can be written into the algorithm.

*Requirements.* For each $e$, $\mathcal S_e : \Phi^A_e \neq C$.

*Construction.* Start with $(\sigma_0, m_0) = (\varepsilon, 0)$. At step $e$, given $(\sigma_e, m_e)$, find an extension $(\tau, m_e)$ forcing $\mathcal S_e$, that is, such that every $X \in [\tau, m_e]$ satisfies $\Phi^X_e \neq C$, as shown below. Then let $m_{e+1} = m_e + 1$ and let $\sigma_{e+1}$ extend $\tau$ by one bit, chosen so that $(\sigma_{e+1}, m_{e+1})$ extends $(\tau, m_e)$. Let $A$ be the unique set extending all $\sigma_e$.

*Forcing $\mathcal S_e$.* Write $(\sigma, m) = (\sigma_e, m_e)$. Three cases are possible.

1. There are $x$ and an extension $(\tau, m)$ of $(\sigma, m)$ with $\Phi^\tau_e(x)\converge \neq C(x)$. Then every $X \in [\tau, m]$ satisfies $\Phi^X_e(x)\converge \neq C(x)$, by the use principle.
2. There is $x$ such that no extension $(\tau, m)$ of $(\sigma, m)$ has $\Phi^\tau_e(x)\converge$. Then every $X \in [\sigma, m]$ satisfies $\Phi^X_e(x)\diverge$: otherwise $\Phi^{X \uh k}_e(x)\converge$ for some $k \geq |\sigma|$, and $(X \uh k, m)$ is an extension of $(\sigma, m)$, since $X \in [\sigma, m]$. Take $\tau = \sigma$.
3. Neither case holds. Then $C$ is computable: to compute $C(x)$, search for $\tau$ such that $(\tau, m)$ extends $(\sigma, m)$ and $\Phi^\tau_e(x)\converge$, and output the value. The search terminates since case 2 fails, and the value is $C(x)$ since case 1 fails. The search is computable, since the extension relation with second component $m$ is. This contradicts the hypothesis on $C$.

*Verification.* Each condition of the construction extends the previous ones, and $A$ belongs to every $[\sigma_e, m_e]$: a position $\langle x, y \rangle \geq |\sigma_e|$ with $x < m_e$ lies below $|\sigma_k|$ for some $k > e$, and the bit placed there respects the column constraint of every condition in force, all of which fix column $x$ to $\emptyset''(x)$. So $A \in [\tau, m_e]$ for the condition $(\tau, m_e)$ chosen at step $e$, every $\mathcal S_e$ is satisfied, and $C \not\leq_T A$. Fix $x$. For $e > x$, we have $m_e > x$, and every position $\langle x, y \rangle \geq |\sigma_{x+1}|$ is assigned the value $\emptyset''(x)$ by the construction. Hence $A(\langle x, y \rangle) = \emptyset''(x)$ for all but finitely many $y$. The sets $A_y = \{ x : A(\langle x, y \rangle) = 1 \}$ form an $A$-computable $\Delta^0_2$ approximation of $\emptyset''$, so $\emptyset'' \leq_T A'$ by :ref{#thm-limit-lemma} relativized to $A$.
:::

:::corollary{#cor-high-incomplete}
There is a high set that is not Turing complete: $\emptyset'' \leq_T A'$ and $\emptyset' \not\leq_T A$.
:::

:::proof{of=cor-high-incomplete}
Apply :ref{#thm-high-cone-avoidance} with $C = \emptyset'$.
:::

Sacks (1963) showed that there are high incomplete c.e. sets, and Friedberg (1957) that every degree $\dbf \geq \obf'$ is the jump of some degree $\abf$, with $\abf \vee \obf' = \dbf$ (the **jump inversion theorem**). We admit these results.

:::quiz[high sets avoiding a cone]
Why does case 3 restrict the search to extensions with the **same** second component $m$?

- [x] Because the extension relation with fixed $m$ only involves the finite string $\emptyset'' \uh m$, so the search is computable.

  With increasing second components, testing extensions would require more and more of $\emptyset''$.
- [ ] Because extensions with larger $m$ do not exist.

  They exist; they are used at the end of each step.
- [ ] To make the set $A$ high.

  Highness comes from increasing $m$ between steps, not from this search.

---

Why does the column $\{ y : \langle x, y \rangle \in A \}$ converge to $\emptyset''(x)$?

- [x] After the step at which $m$ exceeds $x$, all new positions in column $x$ receive the value $\emptyset''(x)$, and only finitely many positions were assigned before.
- [ ] Because $C$ is not computable.

  The hypothesis on $C$ is used for the requirements, not for highness.
- [ ] Because every extension of a condition preserves all columns.

  A condition only fixes the columns below its second component.

:::

## Exercises

::::exercise{difficulty=1}
Show that a set $A$ is low if and only if $A'$ has a computable $\Delta^0_2$ approximation.

:::solution
By :ref{#thm-limit-lemma}, $A' \leq_T \emptyset'$ if and only if $A'$ is limit computable.
:::
::::

::::exercise{difficulty=1}
Show that if $G$ is 1-generic, then $G' \equiv_T G \oplus \emptyset'$.

:::solution
One direction is :ref{#thm-generic-low}. Conversely, $G \leq_T G'$ and $\emptyset' \leq_T G'$ by :ref{#cor-jump-degrees}, so $G \oplus \emptyset' \leq_T G'$.
:::
::::

::::exercise{difficulty=2}
Let $B$ be any set and $C$ a non-computable set. Show that there is a set $A$ with $B \leq_T A'$ and $C \not\leq_T A$.

:::solution
Repeat the proof of :ref{#thm-high-cone-avoidance} with $B$ in place of $\emptyset''$: the conditions fix the columns $x < m$ to the value $B(x)$. Case 3 is still computable, since for fixed $m$ it only involves $B \uh m$. The columns of $A$ converge to $B$, so $B \leq_T A'$ by the relativized limit lemma.
:::
::::

## Notes and references

The hierarchies of low$_n$ and high$_n$ sets were introduced by Soare and by Cooper in the early 1970s; high degrees had been studied before by Martin (1966), who characterized them by dominant functions. The theorem on 1-generic sets is due to Jockusch (1980). The jump inversion theorem is due to Friedberg (1957), and the existence of high incomplete c.e. sets to Sacks (1963).

- R. M. Friedberg, *A criterion for completeness of degrees of unsolvability*, Journal of Symbolic Logic 22 (1957), 159–160.
- G. E. Sacks, *Recursive enumerability and the jump operator*, Transactions of the American Mathematical Society 108 (1963), 223–239.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- R. I. Soare, *Recursively Enumerable Sets and Degrees*, Springer, 1987.
