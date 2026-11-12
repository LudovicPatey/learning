---
title: Weak König's lemma
summary: The system WKL₀; its ω-models are the Scott ideals; there is a Scott ideal of low sets, so WKL₀ does not prove ACA₀; REC is the intersection of all ω-models of WKL₀; WKL₀ is Π¹₁-conservative over RCA₀.
duration: 40
prerequisites: [aca0-reversals, pi01-classes/pa-degrees]
---

Weak König's lemma, the statement that every infinite binary tree has an infinite path, is the set-existence principle behind compactness arguments. A path through an infinite binary tree cannot in general be computed from the tree, but it can be chosen far below the jump: by the low basis theorem, some path is low. The system $\mathsf{WKL}_0$ therefore lies strictly between $\mathsf{RCA}_0$ and $\mathsf{ACA}_0$, and its computability-theoretic counterpart is the notion of PA degree. This lesson studies the system and its ω-models; the next one proves that it is equivalent to theorems of analysis such as the Heine–Borel theorem.

## The system and its ω-models

:::definition{#def-wkl0}
**Weak König's lemma** ($\mathsf{WKL}$) is the statement: every infinite tree $T \subseteq 2^{<\nat}$ has an infinite path. $\mathsf{WKL}_0$ is $\mathsf{RCA}_0 + \mathsf{WKL}$.
:::

Being infinite and being a path are arithmetic properties, so $\mathsf{WKL}$ is a $\Pi^1_2$ statement: for every tree, if it is infinite, there exists a path.

**Examples.** Each instance below is computable, and none of them has a computable path; so each is a statement of $\mathsf{WKL}_0$ that $\mathsf{RCA}_0$ does not prove, by considering the ω-model $\mathrm{REC}$.

- The tree of strings $\sigma \in 2^{<\nat}$ such that $\sigma(e) \neq \Phi_{e, |\sigma|}(e)$ for every $e < |\sigma|$ with $\Phi_{e,|\sigma|}(e)\converge$: its paths are the $\{0,1\}$-valued DNC functions (:ref{#thm-dnc2-no-computable}).
- For disjoint c.e. sets $A$ and $B$ that are computably inseparable, the tree of strings that put the elements of $A$ enumerated by stage $|\sigma|$ into the set and those of $B$ out of it: its paths are the separating sets.

**Why binary.** The restriction to binary trees is essential: the tree of the reversal of :ref{#thm-konig-aca} has at most two successors at each node and yields $\mathsf{ACA}_0$. What matters is not the number of successors but the fact that their values are known in advance. For trees $T \subseteq \nat^{<\nat}$ with a bound $g$ on the values, $\tau(m) < g(m)$ for $\tau \in T$, the strength is that of $\mathsf{WKL}$ (last exercise; compare :ref{#prop-finitely-branching-coding}).

:::definition{#def-scott-ideal}
A **Scott ideal** is a Turing ideal $\mathcal I$ such that every infinite binary tree $T \in \mathcal I$ has an infinite path in $\mathcal I$.
:::

:::proposition{#prop-wkl-scott}
1. An ω-model satisfies $\mathsf{WKL}_0$ if and only if it is a Scott ideal.
2. A Turing ideal $\mathcal I$ is a Scott ideal if and only if for every $X \in \mathcal I$ there is $Y \in \mathcal I$ that is PA relative to $X$.
:::

:::proof{of=prop-wkl-scott}
1. By :ref{#thm-rca-turing-ideal} and absoluteness: a tree in the model is infinite in the model if and only if it is infinite, and a set of the model is a path in the model if and only if it is a path.
2. ($\Rightarrow$) Given $X \in \mathcal I$, the $X$-computable tree whose paths are the $\{0, 1\}$-valued functions DNC relative to $X$ belongs to $\mathcal I$ and is infinite, so it has a path $Y \in \mathcal I$, which is PA relative to $X$. ($\Leftarrow$) Let $T \in \mathcal I$ be an infinite binary tree, and $Y \in \mathcal I$ PA relative to $T$. By the relativization of :ref{#thm-pa-characterization}, $Y$ computes a path of $T$, which belongs to $\mathcal I$.
:::

Part 2 reduces the closure condition, which concerns every tree of the ideal, to a single tree for each set: the tree of DNC functions is a **universal instance**, whose solutions compute solutions of all other instances. This is the reason why the study of ω-models of $\mathsf{WKL}_0$ is the study of PA degrees.

$\mathrm{REC}$ is not a Scott ideal (:ref{#cor-rca-not-wkl}), so $\mathsf{RCA}_0$ does not prove $\mathsf{WKL}_0$. $\mathsf{ACA}_0$ proves $\mathsf{WKL}_0$, since $\mathsf{WKL}$ is a special case of König's lemma (:ref{#thm-konig-aca}). Correspondingly, a jump ideal is a Scott ideal, since $X'$ computes a path through every infinite $X$-computable binary tree, the leftmost one. The converse fails.

**Intuition for the separation.** To build a Scott ideal that is not a jump ideal, one adds, step by step, a set that is PA relative to everything built so far; by part 2 of :ref{#prop-wkl-scott}, the union of the resulting chain is a Scott ideal. The low basis theorem chooses each new set so that the jump does not grow: the jump of every member of the chain stays computable in $\emptyset'$. Then $\emptyset'$ itself never enters.

:::theorem{#thm-low-scott}
There is a Scott ideal all of whose members are low. Consequently $\mathsf{WKL}_0$ does not prove $\mathsf{ACA}_0$.
:::

:::proof{of=thm-low-scott}
Define sets $Z_0 = \emptyset$ and $Z_{n+1} = Z_n \oplus P_n$, where $P_n$ is PA relative to $Z_n$ and satisfies $(Z_n \oplus P_n)' \leq_T Z_n'$. Such a $P_n$ exists by the low basis theorem (:ref{#thm-low-basis}) relativized to $Z_n$, applied to the non-empty $\Pi^0_1(Z_n)$ class of $\{0,1\}$-valued functions DNC relative to $Z_n$. By induction, $Z_n' \leq_T \emptyset'$ for every $n$.

Let $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$. It is a Turing ideal, since the sequence $Z_n$ is increasing. It is a Scott ideal: if $X \leq_T Z_n$, then $P_n \leq_T Z_{n+1}$ is in $\mathcal I$ and PA relative to $Z_n$, hence relative to $X$, and :ref{#prop-wkl-scott} (2) applies. Every $X \in \mathcal I$ satisfies $X' \leq_T Z_n' \leq_T \emptyset'$, so $X$ is low. In particular $\emptyset' \notin \mathcal I$, and $\mathcal I$ is not a jump ideal: it is an ω-model of $\mathsf{WKL}_0$ in which $\mathsf{ACA}_0$ fails.
:::

The proof is typical of separations in reverse mathematics: one closes a model under the solutions of a problem while preserving a computability-theoretic weakness, here lowness, that excludes the stronger principle. The same scheme, with other preservation properties, separates Ramsey's theorem for pairs from $\mathsf{ACA}_0$ in the next course. Simpson proves the theorem differently (Theorem VIII.2.17, Corollary VIII.2.18): a whole countable coded ω-model of $\mathsf{WKL}_0$ is a path through a single tree computable in the parameter, and one application of the low basis theorem gives a low code, all of whose members are low.

:::quiz[models of WKL₀]
In the proof of :ref{#thm-low-scott}, why is $(Z_n \oplus P_n)' \leq_T Z_n'$ required rather than $P_n$ low?

- [x] Because the join of two low sets need not be low: $Z_{n+1}$ is the join of $Z_n$ and $P_n$, and it is the jump of this join that must stay below $\emptyset'$.
- [ ] Because $P_n$ cannot be low.

  It is low: $P_n' \leq_T (Z_n \oplus P_n)' \leq_T Z_n' \leq_T \emptyset'$. The lowness of $P_n$ alone would not suffice, since the join of two low sets need not be low.
- [ ] Because $Z_n$ is not low.

  Every $Z_n$ is low, by the inductive use of this condition.

---

Why does $\mathcal I$ not satisfy $\mathsf{ACA}_0$?

- [x] Because $\mathsf{ACA}_0$ would put $\emptyset'$ into the model, and every member of $\mathcal I$ is low, while $\emptyset'$ is not.
- [ ] Because $\mathcal I$ is countable.

  $\mathrm{ARITH}$ is countable and satisfies $\mathsf{ACA}_0$.
- [ ] Because some infinite tree in $\mathcal I$ has no path in $\mathcal I$.

  $\mathcal I$ is a Scott ideal: every infinite binary tree in it has a path in it.

---

Why is $\mathcal I$ closed under join?

- [x] Because the sequence $(Z_n)$ is increasing for $\leq_T$: if $X \leq_T Z_m$ and $Y \leq_T Z_n$, both are computable from $Z_{\max(m, n)}$, and so is $X \oplus Y$.
- [ ] Because every member of $\mathcal I$ is low.

  Lowness is not preserved by joins; closure under join comes from the chain.
- [ ] Because each $P_n$ is PA relative to $Z_n$.

  This gives the closure under paths of trees, not under joins.
:::

## Conservation

$\mathsf{WKL}_0$ proves no new arithmetic sentence: by a theorem of Harrington, every $\Pi^1_1$ sentence provable in $\mathsf{WKL}_0$ is provable in $\mathsf{RCA}_0$. The proof uses a forcing argument with trees over non-standard models, which can be seen as the low basis theorem carried out inside a countable model; it is given in the course on induction and conservation (:ref{to="induction-conservation/harrington"}). So compactness arguments, though non-constructive, do not increase the arithmetic consequences of the base theory. Combined with a theorem of Parsons on $\Sigma^0_1$ induction, it shows that $\mathsf{WKL}_0$ is $\Pi^0_2$-conservative over primitive recursive arithmetic, a partial realization of Hilbert's program (Simpson, Theorem IX.3.16).

## Exercises

::::exercise{difficulty=1}
Show that there is no least ω-model of $\mathsf{WKL}_0$, but that the intersection of all ω-models of $\mathsf{WKL}_0$ is $\mathrm{REC}$.

:::solution
For every non-computable set $C$ there is a Scott ideal not containing $C$: build the sequence $Z_n$ of :ref{#thm-low-scott} with $P_n$ PA relative to $Z_n$ and $C \not\leq_T Z_n \oplus P_n$, using the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $Z_n$; by induction $C \not\leq_T Z_n$ for every $n$. So every non-computable set is missing from some ω-model of $\mathsf{WKL}_0$, and the intersection of all of them is $\mathrm{REC}$, which is not a model. A least ω-model would be contained in this intersection, hence equal to $\mathrm{REC}$, a contradiction.
:::
::::

::::exercise{difficulty=1}
Show that a Scott ideal is never of the form $\{ X : X \leq_T A \}$, and that every Scott ideal contains a member of every non-empty $\Pi^0_1$ class.

:::solution
If $\mathcal I = \{ X : X \leq_T A \}$ were a Scott ideal, then $A \in \mathcal I$, and by :ref{#prop-wkl-scott} (2) some $Y \in \mathcal I$ would be PA relative to $A$, so $Y \leq_T A$. But no set computable in $A$ is PA relative to $A$: a $\{0, 1\}$-valued function computable in $A$ is not DNC relative to $A$, by the relativization of :ref{#thm-dnc2-no-computable}. For the second part, a non-empty $\Pi^0_1$ class is the set of paths of a computable binary tree $T$, which is infinite since it has a path. Since $\mathcal I$ is a Turing ideal, $T \in \mathcal I$, and $T$ has a path in $\mathcal I$, which is a member of the class.
:::
::::

::::exercise{difficulty=2}
A tree $T \subseteq \nat^{<\nat}$ is **bounded** by $g : \nat \to \nat$ if $\tau(m) < g(m)$ for every $\tau \in T$ and $m < |\tau|$. Show in $\mathsf{WKL}_0$ that every infinite tree bounded by some function $g$ has a path.

:::solution
Since $T$ is infinite, $g(m) \geq 1$ for every $m$. Code a string $\tau$ bounded by $g$ by the binary string $\tau^*$ obtained by concatenating, for $j < |\tau|$, the blocks $0^{\tau(j)} 1^{g(j) - \tau(j)}$; it has length $\sum_{j < |\tau|} g(j) \geq |\tau|$. Let $T^*$ be the set of binary strings $\rho$ that are prefixes of $\tau^*$ for some $\tau \in T$ with $|\tau| \leq |\rho|$. The quantifier over $\tau$ is bounded, since $\tau(j) < g(j)$ and $|\tau| \leq |\rho|$, so $T^*$ exists by $\Delta^0_1$ comprehension. It is a tree: if $\rho' \preceq \rho$ and $\rho$ is a prefix of $\tau^*$, then $\rho'$ is a prefix of $(\tau \uh l)^*$ with $l = \min(|\tau|, |\rho'|)$, and $\tau \uh l \in T$. It is infinite since $\tau^* \in T^*$ for every $\tau \in T$. Let $Y$ be a path, by $\mathsf{WKL}$. Each block of $Y$, of length $g(j)$, is a block of some $\tau^*$ with $\tau \in T$ and $|\tau| > j$, since the prefix of $Y$ ending with this block belongs to $T^*$; hence it is of the form $0^k 1^{g(j) - k}$ with $k < g(j)$; let $P(j) = k$, which exists by $\Delta^0_1$ comprehension. For every $n$, the prefix of $Y$ made of the first $n$ blocks is a prefix of some $\tau^*$ with $\tau \in T$; since the blocks determine the values, $\tau \uh n = P \uh n$, so $P \uh n \in T$. Hence $P$ is a path through $T$.
:::
::::

## Notes and references

Friedman (1976) identified $\mathsf{WKL}_0$. The characterization of its countable ω-models goes back to Scott (1962), who showed that they are exactly the classes of sets representable in complete extensions of Peano arithmetic, hence the name Scott systems (Simpson, notes to Section VIII.2). The ω-models of $\mathsf{WKL}_0$, the low model and the fact that $\mathrm{REC}$ is the intersection of all of them are in Simpson, Section VIII.2 (Corollaries VIII.2.18 and VIII.2.27); the basis theorems are due to Jockusch and Soare (1972). Bounded König's lemma, the last exercise, is Simpson, Lemma IV.1.4. Harrington's conservation theorem (1977) is unpublished; Simpson, Section IX.2, presents it. The $\Pi^0_2$ conservation over primitive recursive arithmetic is due to Friedman (1976, unpublished); Sieg (1985) gave a proof-theoretic proof (Simpson, notes to Section IX.3). Hirschfeldt, Sections 4.4–4.5, and Dzhafarov and Mummert, Section 5.6.2, present the same material from the computability-theoretic side.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections IV.1, VIII.2, IX.2 and IX.3.
- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in *Recursive Function Theory*, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- W. Sieg, *Fragments of arithmetic*, Annals of Pure and Applied Logic 28 (1985), 33–71.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 4.4–4.5.
