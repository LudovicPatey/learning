---
title: Weak König's lemma
summary: The system WKL₀; its ω-models are the Scott ideals; there is a Scott ideal of low sets, so WKL₀ does not prove ACA₀; REC is the intersection of all ω-models of WKL₀; WKL₀ is Π¹₁-conservative over RCA₀.
duration: 25
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

**Why binary.** The restriction to binary trees is essential: the tree of the reversal of :ref{#thm-konig-aca} has at most two successors at each node and yields $\mathsf{ACA}_0$. What matters is not the number of successors but the fact that their values are known in advance. For trees $T \subseteq \nat^{<\nat}$ with a bound $g$ on the values, $\tau(m) < g(m)$ for $\tau \in T$, the strength is that of $\mathsf{WKL}$ (:ref{#ex-bounded-konig-wkl}; compare :ref{#prop-finitely-branching-coding}).

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

::::exercise{#ex-rec-intersection-wkl difficulty=1 objective="Vary the construction of the low Scott ideal with the cone avoidance basis theorem, to show that $\mathsf{WKL}_0$ has no least ω-model."}
Show that there is no least ω-model of $\mathsf{WKL}_0$, but that the intersection of all ω-models of $\mathsf{WKL}_0$ is $\mathrm{REC}$.

:::solution
For every non-computable set $C$ there is a Scott ideal not containing $C$: build the sequence $Z_n$ of :ref{#thm-low-scott} with $P_n$ PA relative to $Z_n$ and $C \not\leq_T Z_n \oplus P_n$, using the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $Z_n$; by induction $C \not\leq_T Z_n$ for every $n$. So every non-computable set is missing from some ω-model of $\mathsf{WKL}_0$, and the intersection of all of them is $\mathrm{REC}$, which is not a model. A least ω-model would be contained in this intersection, hence equal to $\mathrm{REC}$, a contradiction.
:::
::::

::::exercise{#ex-bounded-konig-wkl difficulty=2 objective="Code a tree with a known bound on its values into a binary tree, to prove bounded König's lemma in $\mathsf{WKL}_0$."}
A tree $T \subseteq \nat^{<\nat}$ is **bounded** by $g : \nat \to \nat$ if $\tau(m) < g(m)$ for every $\tau \in T$ and $m < |\tau|$. Show in $\mathsf{WKL}_0$ that every infinite tree bounded by some function $g$ has a path.

:::solution
Since $T$ is infinite, $g(m) \geq 1$ for every $m$. Code a string $\tau$ bounded by $g$ by the binary string $\tau^*$ obtained by concatenating, for $j < |\tau|$, the blocks $0^{\tau(j)} 1^{g(j) - \tau(j)}$; it has length $\sum_{j < |\tau|} g(j) \geq |\tau|$. Let $T^*$ be the set of binary strings $\rho$ that are prefixes of $\tau^*$ for some $\tau \in T$ with $|\tau| \leq |\rho|$. The quantifier over $\tau$ is bounded, since $\tau(j) < g(j)$ and $|\tau| \leq |\rho|$, so $T^*$ exists by $\Delta^0_1$ comprehension. It is a tree: if $\rho' \preceq \rho$ and $\rho$ is a prefix of $\tau^*$, then $\rho'$ is a prefix of $(\tau \uh l)^*$ with $l = \min(|\tau|, |\rho'|)$, and $\tau \uh l \in T$. It is infinite since $\tau^* \in T^*$ for every $\tau \in T$. Let $Y$ be a path, by $\mathsf{WKL}$. Each block of $Y$, of length $g(j)$, is a block of some $\tau^*$ with $\tau \in T$ and $|\tau| > j$, since the prefix of $Y$ ending with this block belongs to $T^*$; hence it is of the form $0^k 1^{g(j) - k}$ with $k < g(j)$; let $P(j) = k$, which exists by $\Delta^0_1$ comprehension. For every $n$, the prefix of $Y$ made of the first $n$ blocks is a prefix of some $\tau^*$ with $\tau \in T$; since the blocks determine the values, $\tau \uh n = P \uh n$, so $P \uh n \in T$. Hence $P$ is a path through $T$.
:::
::::

## Conservation

$\mathsf{WKL}_0$ proves no new arithmetic sentence: by a theorem of Harrington, every $\Pi^1_1$ sentence provable in $\mathsf{WKL}_0$ is provable in $\mathsf{RCA}_0$. The proof uses a forcing argument with trees over non-standard models, which can be seen as the low basis theorem carried out inside a countable model; it is given in the course on induction and conservation (:ref{to="induction-conservation/harrington"}). So compactness arguments, though non-constructive, do not increase the arithmetic consequences of the base theory. Combined with a theorem of Parsons on $\Sigma^0_1$ induction, it shows that $\mathsf{WKL}_0$ is $\Pi^0_2$-conservative over primitive recursive arithmetic, a partial realization of Hilbert's program (Simpson, Theorem IX.3.16).

## Notes and references

Liu's theorem, that Ramsey's theorem for pairs does not imply WKL₀, is proved in the course on compactness avoidance (:ref{to="compactness-avoidance/liu-theorem"}). In the track on models of arithmetic, the weak König lemma holds in the coded sets of every proper exponential cut (:ref{to="cuts-and-extensions/weak-konig-cuts"}), and semiregular cuts are characterized by it (:ref{to="cuts-and-extensions/semiregular-cuts"}).

Friedman (1976) identified $\mathsf{WKL}_0$. The characterization of its countable ω-models goes back to Scott (1962), who showed that they are exactly the classes of sets representable in complete extensions of Peano arithmetic, hence the name Scott systems (Simpson, notes to Section VIII.2). The ω-models of $\mathsf{WKL}_0$, the low model and the fact that $\mathrm{REC}$ is the intersection of all of them are in Simpson, Section VIII.2 (Corollaries VIII.2.18 and VIII.2.27); the basis theorems are due to Jockusch and Soare (1972). Bounded König's lemma, :ref{#ex-bounded-konig-wkl}, is Simpson, Lemma IV.1.4. Harrington's conservation theorem (1977) is unpublished; Simpson, Section IX.2, presents it. The $\Pi^0_2$ conservation over primitive recursive arithmetic is due to Friedman (1976, unpublished); Sieg (1985) gave a proof-theoretic proof (Simpson, notes to Section IX.3). Hirschfeldt, Sections 4.4–4.5, and Dzhafarov and Mummert, Section 5.6.2, present the same material from the computability-theoretic side.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections IV.1, VIII.2, IX.2 and IX.3.
- H. Friedman, *Systems of second order arithmetic with restricted induction, I, II*, abstracts, Journal of Symbolic Logic 41 (1976), 557–559.
- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in *Recursive Function Theory*, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- W. Sieg, *Fragments of arithmetic*, Annals of Pure and Applied Logic 28 (1985), 33–71.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 4.4–4.5.

:::::exercises
::::exercise{#ex-scott-not-principal difficulty=1 objective="Use the characterization of Scott ideals by PA sets to show that a Scott ideal is never generated by a single set, and that it meets every non-empty $\Pi^0_1$ class."}
Show that a Scott ideal is never of the form $\{ X : X \leq_T A \}$, and that every Scott ideal contains a member of every non-empty $\Pi^0_1$ class.

:::solution
If $\mathcal I = \{ X : X \leq_T A \}$ were a Scott ideal, then $A \in \mathcal I$, and by :ref{#prop-wkl-scott} (2) some $Y \in \mathcal I$ would be PA relative to $A$, so $Y \leq_T A$. But no set computable in $A$ is PA relative to $A$: a $\{0, 1\}$-valued function computable in $A$ is not DNC relative to $A$, by the relativization of :ref{#thm-dnc2-no-computable}. For the second part, a non-empty $\Pi^0_1$ class is the set of paths of a computable binary tree $T$, which is infinite since it has a path. Since $\mathcal I$ is a Turing ideal, $T \in \mathcal I$, and $T$ has a path in $\mathcal I$, which is a member of the class.
:::
::::

::::exercise{#ex-scott-chain difficulty=1 objective="Check that Scott ideals are closed under unions of chains but not under intersections."}
Show that the union of an increasing sequence $\mathcal I_0 \subseteq \mathcal I_1 \subseteq \cdots$ of Scott ideals is a Scott ideal, and that the intersection of a family of Scott ideals need not be a Scott ideal.

:::solution
The union $\mathcal I$ is a Turing ideal by :ref{#ex-union-ideals}. Let $T \in \mathcal I$ be an infinite binary tree. Then $T \in \mathcal I_n$ for some $n$, and $T$ has a path in $\mathcal I_n \subseteq \mathcal I$. So $\mathcal I$ is a Scott ideal.

By :ref{#prop-wkl-scott} (1), the Scott ideals are the ω-models of $\mathsf{WKL}_0$, and by :ref{#ex-rec-intersection-wkl} their intersection is $\mathrm{REC}$. It is not a Scott ideal (:ref{#cor-rca-not-wkl}). An intersection of only two Scott ideals can already be $\mathrm{REC}$: see :ref{#ex-dominated-scott}.
:::
::::

::::exercise{#ex-scott-extension difficulty=1 objective="Apply the chain construction of the low Scott ideal to extend an arbitrary countable Turing ideal to a Scott ideal."}
Show that every countable Turing ideal is contained in a countable Scott ideal.

:::solution
Let $\mathcal J$ be a countable Turing ideal, listed as $X_0, X_1, \dots$, possibly with repetitions. Let $Z_0 = \emptyset$ and $Z_{n+1} = Z_n \oplus X_n \oplus P_n$, where $P_n$ is PA relative to $Z_n \oplus X_n$; for instance $P_n = (Z_n \oplus X_n)'$, which computes a $\{0, 1\}$-valued function DNC relative to $Z_n \oplus X_n$, as $\emptyset'$ does in the unrelativized case. Let $\mathcal I = \{ Y : \exists n\ Y \leq_T Z_n \}$.

It is a Turing ideal, since $Z_n \leq_T Z_{n+1}$ (:ref{#ex-union-ideals}), and it is countable, as a countable union of countable classes. It contains each $X_n \leq_T Z_{n+1}$, so $\mathcal J \subseteq \mathcal I$. If $Y \leq_T Z_n$, then $P_n \leq_T Z_{n+1}$ belongs to $\mathcal I$ and is PA relative to $Z_n \oplus X_n$, hence relative to $Y$, since a $\{0,1\}$-valued function DNC relative to a set is DNC relative to every set computable in it. By :ref{#prop-wkl-scott} (2), $\mathcal I$ is a Scott ideal.
:::
::::

::::exercise{#ex-wkl-sequences difficulty=2 objective="Interleave a sequence of binary trees into a single binary tree, to solve infinitely many instances of $\mathsf{WKL}$ at once in $\mathsf{WKL}_0$."}
A sequence of trees $(T_n)$ is coded by a set whose $n$-th column is $T_n$. Show in $\mathsf{WKL}_0$: for every sequence $(T_n)$ of infinite binary trees, there is a set $P$ such that, for every $n$, the column $P^{[n]} = \{ k : \langle n, k \rangle \in P \}$ is a path through $T_n$.

:::solution
For a string $\sigma \in 2^{<\nat}$ and a number $n$, let $\sigma^{[n]}$ be the string $k \mapsto \sigma(\langle n, k \rangle)$, defined for the $k$ with $\langle n, k \rangle < |\sigma|$; since $\langle n, k \rangle$ is increasing in $k$, these $k$ form an initial segment, and $\sigma^{[n]}$ is a string. Since $\langle n, k \rangle \geq n$, the string $\sigma^{[n]}$ is empty for $n \geq |\sigma|$. Let
$$
T = \{ \sigma \in 2^{<\nat} : \forall n < |\sigma|\ \sigma^{[n]} \in T_n \},
$$
which exists by $\Delta^0_1$ comprehension. If $\tau \preceq \sigma$, then $\tau^{[n]} \preceq \sigma^{[n]}$ for every $n$, so $T$ is a tree, the $T_n$ being trees.

$T$ is infinite. Let $\ell \in \nat$. Each $T_n$ is infinite and has finitely many strings of length less than $\ell$, so it contains a string of length at least $\ell$, and its prefix $\rho_n$ of length $\ell$; take $\rho_n$ to be the first string of length $\ell$ in $T_n$, a bounded search, so that the finite sequence $(\rho_n)_{n < \ell}$ exists. Let $\sigma$ be the string of length $\ell$ with $\sigma(\langle n, k \rangle) = \rho_n(k)$; every position $p < \ell$ is of the form $\langle n, k \rangle$ with $n, k \leq p < \ell$. Then each $\sigma^{[n]}$ with $n < \ell$ is a prefix of $\rho_n$, so it belongs to $T_n$, and $\sigma \in T$.

By $\mathsf{WKL}$, $T$ has a path $P$. For each $n$ and $j$, choose $\ell > \max(n, \langle n, j \rangle)$; then $P^{[n]} \uh (j+1)$ is a prefix of $(P \uh \ell)^{[n]}$, which belongs to $T_n$. So each $P^{[n]}$ is a path through $T_n$.
:::
::::

::::exercise{#ex-leftmost-path-aca difficulty=2 objective="Show that asking for the leftmost path of a binary tree raises the strength of weak König's lemma to $\mathsf{ACA}_0$." lessons="aca0"}
For $X \neq Y$ in $2^\nat$, write $X <_{\mathrm{lex}} Y$ if $X(k) < Y(k)$ at the least $k$ with $X(k) \neq Y(k)$. A path $P$ of a tree $T$ is **leftmost** if $P <_{\mathrm{lex}} Q$ for every path $Q \neq P$ of $T$. Show that $\mathsf{ACA}_0$ is equivalent over $\mathsf{RCA}_0$ to the statement: every infinite tree $T \subseteq 2^{<\nat}$ has a leftmost path.

:::solution
($\Rightarrow$) Call $\sigma$ **extendible** if for every $\ell$ there is $\tau \in T$ with $\sigma \preceq \tau$ and $|\tau| = \ell$; this is a $\Pi^0_1$ property, and the set $E$ of extendible strings exists by arithmetic comprehension. The empty string is extendible: $T$ has finitely many strings of length less than $\ell$, so being infinite it has one of length at least $\ell$, whose prefix of length $\ell$ is in $T$. If $\sigma$ is extendible, so is $\sigma 0$ or $\sigma 1$: otherwise there are $\ell_0, \ell_1$ such that $\sigma i$ has no extension in $T$ of length $\ell_i$, and $\sigma$ has none of length $\max(\ell_0, \ell_1)$. Define $P$ by $P \uh (k+1) = (P \uh k) 0$ if $(P \uh k) 0 \in E$, and $(P \uh k) 1$ otherwise; it exists by $\Delta^0_1$ comprehension relative to $E$. By induction on $k$, $P \uh k \in E$, so $P$ is a path. Let $Q \neq P$ be a path, and $k$ the least position where they differ. If $Q(k) = 0$, then $(P \uh k) 0 = Q \uh (k+1)$ is extendible, since $Q$ is a path; so $P(k) = 0 = Q(k)$, a contradiction. So $Q(k) = 1$, $P(k) = 0$, and $P <_{\mathrm{lex}} Q$.

($\Leftarrow$) We prove (4) of :ref{#thm-aca-equivalents}. Let $f$ be injective, and let $T$ be the set of strings $\sigma$ such that, for every $m < |\sigma|$ with $\sigma(m) = 0$, $f(i) \neq m$ for all $i < |\sigma|$. It is a tree defined by a bounded formula. It is infinite: the string of length $\ell$ with $\sigma(m) = 1$ if and only if $f(i) = m$ for some $i < \ell$ belongs to $T$. If $X$ is a path and $X(m) = 0$, then $m$ is not in the range of $f$, by considering prefixes longer than any $i$. Let $P$ be the leftmost path. If $m$ is in the range of $f$, then $P(m) = 1$. If $m$ is not in the range of $f$ and $P(m) = 1$, let $Q$ agree with $P$ except that $Q(m) = 0$; $Q$ exists by $\Delta^0_1$ comprehension, it is a path, since its only $0$ outside those of $P$ is at a position outside the range of $f$, and $Q <_{\mathrm{lex}} P$, a contradiction. So the range of $f$ is $\{ m : P(m) = 1 \}$, which exists by $\Delta^0_1$ comprehension.

The paths of $T$ are the sets containing the range of $f$, and the leftmost one is the range itself; this is the formal version of the fact that the leftmost member of a $\Pi^0_1$ class may compute $\emptyset'$. Compare Dzhafarov and Mummert, Exercise 5.13.23 (1).
:::
::::

::::exercise{#ex-dominated-scott difficulty=2 objective="Build a Scott ideal of computably dominated sets by the chain method, and intersect it with the low Scott ideal."}
1. Show that there is a Scott ideal all of whose members are computably dominated (:ref{#def-computably-dominated}).
2. Deduce that there are two Scott ideals whose intersection is $\mathrm{REC}$, so that the intersection of two ω-models of $\mathsf{WKL}_0$ need not be one.

You may use the relativization of :ref{#thm-dominated-basis}: for every set $Z$, every non-empty $\Pi^0_1(Z)$ class has a member $P$ such that every total $(Z \oplus P)$-computable function is dominated by a total $Z$-computable function.

:::solution
1. Let $Z_0 = \emptyset$ and $Z_{n+1} = Z_n \oplus P_n$, where $P_n$ is a member of the non-empty $\Pi^0_1(Z_n)$ class of $\{0, 1\}$-valued functions DNC relative to $Z_n$, chosen by the relativized basis theorem. By induction on $n$, every total $Z_n$-computable function is dominated by a computable function: this is clear for $Z_0$, and a total $Z_{n+1}$-computable function $g$ is dominated by a total $Z_n$-computable $h$, which is dominated by a computable function by the induction hypothesis, and then $g$ is dominated by the same computable function. Let $\mathcal I = \{ X : \exists n\ X \leq_T Z_n \}$. As in the proof of :ref{#thm-low-scott}, $\mathcal I$ is a Scott ideal: if $X \leq_T Z_n$, then $P_n \in \mathcal I$ is PA relative to $Z_n$, hence relative to $X$. Every total $X$-computable function, for $X \leq_T Z_n$, is $Z_n$-computable, hence dominated by a computable function: $X$ is computably dominated.
2. Let $\mathcal J$ be the Scott ideal of low sets of :ref{#thm-low-scott}. Both $\mathcal I$ and $\mathcal J$ contain $\mathrm{REC}$. A set $X \in \mathcal I \cap \mathcal J$ is low, hence $X \leq_T X' \leq_T \emptyset'$ and $X$ is $\Delta^0_2$; and it is computably dominated. A non-computable $\Delta^0_2$ set is never computably dominated (remark after :ref{#def-computably-dominated}), so $X$ is computable. Hence $\mathcal I \cap \mathcal J = \mathrm{REC}$, which is not a Scott ideal (:ref{#cor-rca-not-wkl}).

Part 1 is Dzhafarov and Mummert, Exercise 4.8.13; the computably dominated basis theorem is due to Jockusch and Soare (1972).
:::
::::
:::::
