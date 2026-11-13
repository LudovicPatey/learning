---
title: Avoiding closed classes
summary: Constant-bound traces of closed classes and constant-bound trace avoidance, which implies PA avoidance; Liu's lemma for blocks and the abstract theorem for finitely merging questions; weak weak König's lemma does not admit constant-bound trace avoidance, while Ramsey's theorem for pairs does (Liu), so that Ramsey's theorem for pairs does not imply weak weak König's lemma.
duration: 45
prerequisites: [measure-and-closed-classes, liu-theorem, martin-lof-randomness/levin-schnorr]
---

Weak weak König's lemma admits PA avoidance (:ref{#thm-wwkl-strong-pa}), so PA avoidance cannot separate it from Ramsey's theorem for pairs. The class to be avoided is now a $\Pi^0_1$ class of random sequences, which every Turing ideal satisfying $\mathsf{WWKL}$ meets (:ref{#cor-mlr-structure}). For $\mathrm{DNC}_2$, the third case of the density argument produced a member from the answers of the question; for an arbitrary closed class, it can only produce finite approximations of members, constant-bound traces. This lesson defines the corresponding avoidance property, proves its abstract theorem with a version of Liu's lemma for blocks, and shows that $\mathsf{WWKL}$ lacks it while $\mathsf{RT}^2_2$ has it.

## Traces of closed classes

PA avoidance avoids one closed class, $\mathrm{DNC}_2$, which is $\Pi^0_1$ and homogeneous: a string extends to a member if and only if it differs from $J$ wherever $J$ is defined below its length. For an arbitrary closed class, one avoids finite approximations of members.

:::definition{#def-cb-trace}
Let $\mathcal C \subseteq \cs$ be a closed class and $k \geq 1$. A **$k$-trace** of $\mathcal C$ is a sequence $(F_n)_{n \in \nat}$ of finite sets of strings, given by canonical codes, such that for every $n$, $F_n$ contains at most $k$ strings, all of length $n$, and at least one of them is the prefix of a member of $\mathcal C$. A **constant-bound trace**, or c.b. trace, is a $k$-trace for some $k$.

A problem $\mathsf P$ admits **constant-bound trace avoidance** if for every set $Z$ and every closed class $\mathcal C$ with no $Z$-computable c.b. trace, every instance $X \leq_T Z$ has a solution $Y$ such that $\mathcal C$ has no $(Z \oplus Y)$-computable c.b. trace.
:::

A member $P$ of $\mathcal C$ computes the $1$-trace $(\{ P \uh n \})_n$, so c.b. trace avoidance is a strong form of the avoidance of members. For $\mathrm{DNC}_2^D$, the two coincide.

:::lemma{#lem-trace-reduction}
Let $D \leq_T W$, and let $\mathcal C$ be a $\Pi^0_1(D)$ class. Every $W$-computable c.b. trace of $\mathcal C$ yields a $W$-computable $1$-trace of $\mathcal C$. If moreover $\mathcal C = \mathrm{DNC}_2^D$, every $W$-computable c.b. trace of $\mathcal C$ yields a $W$-computable member of $\mathcal C$, and $W$ is PA relative to $D$.
:::

:::proof{of=lem-trace-reduction}
Call a string **dead** if it is not the prefix of a member of $\mathcal C$; this is a $\Sigma^0_1(D)$ property, hence $\Sigma^0_1(W)$. We prove by induction on $k$ that a $W$-computable $k$-trace $(F_n)$ yields a $W$-computable $1$-trace. For $k = 1$ there is nothing to prove. Let $k \geq 2$; there are two cases, and the construction is not uniform.

- *Infinitely many $F_m$ contain a dead string.* For each $n$, search for $m \geq n$ and a string of $F_m$ that is seen dead, and let $F'_n$ be the set of the restrictions to $n$ of the strings of $F_m$ not yet seen dead. The search terminates. The strings of $F_m$ that are not dead are never seen dead, and one of them is the prefix of a member, as is its restriction to $n$. So $(F'_n)$ is a $W$-computable $(k-1)$-trace; apply the induction hypothesis.
- *For some $n_0$, no $F_m$ with $m \geq n_0$ contains a dead string.* For $n \geq n_0$, let $E_n$ consist of the first string of $F_n$, and for $n < n_0$, of the restriction to $n$ of the first string of $F_{n_0}$. Then $(E_n)$ is a $W$-computable $1$-trace.

If $\mathcal C = \mathrm{DNC}_2^D$ and $(\{ \rho_n \})$ is a $1$-trace, let $f(x) = \rho_{x+1}(x)$. The string $\rho_{x+1}$ is the prefix of a function that is $\mathrm{DNC}_2$ relative to $D$, so $f(x) \neq J^D(x)$ when $J^D(x)$ is defined: $f$ is a member of $\mathcal C$, computable in $W$.
:::

The last step uses homogeneity: the strings of a $1$-trace may be prefixes of different members, but each is correct below its length.

:::proposition{#prop-cb-trace-pa}
If a problem admits constant-bound trace avoidance, it admits PA avoidance.
:::

:::proof{of=prop-cb-trace-pa}
Let $D \leq_T Z$ with $Z$ not PA relative to $D$, and $X \leq_T Z$ an instance. By :ref{#lem-trace-reduction} with $W = Z$, the class $\mathcal C = \mathrm{DNC}_2^D$ has no $Z$-computable c.b. trace. So some solution $Y$ is such that $\mathcal C$ has no $(Z \oplus Y)$-computable c.b. trace. If $Z \oplus Y$ were PA relative to $D$, it would compute a member of $\mathcal C$, hence a $1$-trace.
:::

## Liu's lemma for blocks

The proofs of c.b. trace avoidance follow those of PA avoidance, with finite sets of strings of one length in place of valuations. A **block** of length $n$ is a finite set of strings of length $n$, coded together with $n$; let $\mathcal B_n$ be the finite set of blocks of length $n$. For a closed class $\mathcal C$, the block $F \in \mathcal B_n$ is **$\mathcal C$-correct** if it is the set of the strings of length $n$ that are prefixes of members of $\mathcal C$.

:::definition{#def-disperse}
Let $k \geq 1$. A set $V \subseteq \mathcal B_n$ of blocks is **$k$-disperse** if for every partition of $V$ into $k$ parts $V_0, \dots, V_{k-1}$, some part $V_s$ has $\bigcap_{F \in V_s} F = \emptyset$, with the convention that the intersection over the empty family is the set of all strings of length $n$.
:::

If $V$ is $k$-disperse, a set $E$ of strings of length $n$ that meets every block of $V$ has more than $k$ elements. Indeed, if $E = \{ \rho_0, \dots, \rho_{j-1} \}$ with $j \leq k$, put each $F \in V$ in the part $V_s$ for the least $s$ with $\rho_s \in F$; then $\rho_s \in \bigcap_{F \in V_s} F$ for every non-empty part, and the parts $V_s$ with $j \leq s < k$ are empty. So a functional whose outputs are sets of at most $k$ strings, forced to meet every block of a $k$-disperse set, is forced to diverge. For example, the set of the $2^n$ singletons of $\mathcal B_n$ is $k$-disperse for every $k < 2^n$.

:::lemma[Liu]{#lem-liu-blocks}
Let $W$ be a set, $\mathcal C$ a closed class with no $W$-computable c.b. trace, and $U$ a $\Sigma^0_1(W)$ set of blocks. Either $U$ contains a $\mathcal C$-correct block, or for every $k$ there is $n$ such that $\mathcal B_n \setminus U$ is $k$-disperse.
:::

:::proof{of=lem-liu-blocks}
Suppose that $U$ contains no $\mathcal C$-correct block, and that for some $k$ and every $n$, $V_n = \mathcal B_n \setminus U$ is not $k$-disperse. Let $V_{n,t} = \mathcal B_n \setminus U_t$, where $U_t$ is the part of $U$ enumerated at stage $t$; these finite sets decrease to $V_n$ and are computable in $W$, uniformly. For each $n$, search for $t$ and a partition of $V_{n,t}$ into $k$ parts with non-empty intersections. The search terminates, since $V_{n,t} = V_n$ for $t$ large. Let $V_{n,0}, \dots, V_{n,k-1}$ be the partition found, and $E_n$ a set containing one string of each intersection $\bigcap_{F \in V_{n,s}} F$; it has at most $k$ strings of length $n$. The $\mathcal C$-correct block of $\mathcal B_n$ is not in $U$, so it belongs to $V_n \subseteq V_{n,t}$, and to some part $V_{n,s}$. The string chosen in $\bigcap_{F \in V_{n,s}} F$ belongs to the correct block, so it is the prefix of a member of $\mathcal C$. Thus $(E_n)$ is a $W$-computable $k$-trace of $\mathcal C$, a contradiction.
:::

A forcing question is **finitely merging** if for every condition $c$, every $\Sigma^0_1$ formula $\varphi(y)$ and every finite set $R$ such that $c \mathrel{?{\nvdash}} \varphi(m)$ for every $m \in R$, some extension of $c$ forces $\neg \varphi(m)$ for every $m \in R$. The questions of Cohen forcing and of computable Mathias forcing are finitely merging, for the reason given in :ref{#thm-coh-pa-avoidance}: if no compatible string satisfies any of the sentences, the condition itself forces all the negations.

:::theorem{#thm-finitely-merging-trace}
Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving finitely merging forcing question, and $\mathcal C$ a closed class with no c.b. trace computable in a member of $\mathcal M$. For every sufficiently generic set $G$, $\mathcal C$ has no $(Z \oplus G)$-computable c.b. trace.
:::

:::proof{of=thm-finitely-merging-trace}
Fix $e$ and $k$. We may assume that whenever $\Phi^{Z \oplus G}_e(n)$ converges, its value codes a set of at most $k$ strings of length $n$: modify the functional to diverge otherwise, which does not change the $k$-traces it computes. Let $\varphi(F)$ be the $\Sigma^0_1$ formula "$\Phi^{Z \oplus G}_e(n)$ converges and is disjoint from $F$", where $n$ is the length of the strings of the block $F$. Given a condition $c$ and $X \in \mathcal M$ for $c$, the set $U = \{ F : c \mathrel{?{\vdash}} \varphi(F) \}$ is $\Sigma^0_1(X)$.

1. If $U$ contains a $\mathcal C$-correct block $F$, an extension forces $\varphi(F)$: on its members, $\Phi^{Z \oplus G}_e(n)$ contains no prefix of a member of $\mathcal C$, so it is not a trace.
2. If $\mathcal B_n \setminus U$ is $k$-disperse, the question is finitely merging, so an extension forces $\neg \varphi(F)$ for every $F \in \mathcal B_n \setminus U$. On its members, if $\Phi^{Z \oplus G}_e(n)$ converged, its value would meet every block of a $k$-disperse set while having at most $k$ elements. So $\Phi^{Z \oplus G}_e(n)$ diverges.
3. One of the two cases holds, by :ref{#lem-liu-blocks} with $W = X$.

So the conditions forcing that $\Phi^{Z \oplus G}_e$ is not a $k$-trace of $\mathcal C$ are dense, for all $e$ and $k$.
:::

With computable Mathias forcing, this shows that $\mathsf{COH}$ admits c.b. trace avoidance, as in :ref{#thm-coh-pa-avoidance}. The case of Ramsey's theorem for pairs follows the plan of :ref{to="compactness-avoidance/partition-forcing"} and :ref{to="compactness-avoidance/liu-theorem"}, with blocks in place of valuations and disperse sets in place of pairwise incompatible valuations (a condition with $d$ parts needs a $kd$-disperse set). We admit it.

:::theorem[Liu]{#thm-liu-closed-classes}
$\mathsf{RT}^2_2$ admits constant-bound trace avoidance.
:::

## Weak weak König's lemma does not avoid traces

The converse of :ref{#prop-cb-trace-pa} fails, and $\mathsf{WWKL}$ shows it.

:::proposition{#prop-random-no-trace}
For $c$ large enough, the class $\mathcal R_c = \{ X : K(X \uh n) \geq n - c \text{ for every } n \}$ is a $\Pi^0_1$ class of positive measure with no computable c.b. trace. Consequently $\mathsf{WWKL}$ admits PA avoidance but not constant-bound trace avoidance.
:::

:::proof{of=prop-random-no-trace}
The class is $\Pi^0_1$, since $K$ is approximable from above: $K(\sigma) < m$ is a $\Sigma^0_1$ property of $\sigma$ and $m$. Its complement is the class $\mathcal V_c$ of the proof of :ref{#thm-levin-schnorr}, of measure at most $2^{-c}$, so $\lambda(\mathcal R_c) > 0$ for $c \geq 1$. Suppose that $(F_n)$ is a computable $k$-trace of $\mathcal R_c$. There is a prefix-free machine that, on a shortest description of the pair $(n, j)$ with $j < k$, outputs the $j$-th string of $F_n$. So for every $n$ there is a string $\rho_n \in F_n$, the prefix of a member of $\mathcal R_c$, with
$$
n - c \leq K(\rho_n) \leq K(n) + O(1) \leq 2 \log n + O(1),
$$
where the constant depends on $k$ but not on $n$; this fails for $n$ large. For the last statement, the tree of $\mathcal R_c$ is a computable instance of $\mathsf{WWKL}$, every path of which computes a $1$-trace of $\mathcal R_c$, while PA avoidance is :ref{#thm-wwkl-strong-pa}.
:::

:::corollary[Liu]{#cor-rt22-not-wwkl}
There is an ω-model of $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ that is not a model of $\mathsf{WWKL}_0$. In particular $\mathsf{RT}^2_2$ does not imply $\mathsf{WWKL}_0$ over $\mathsf{RCA}_0$.
:::

:::proof{of=cor-rt22-not-wwkl}
Let $\mathcal W$ be the class of the sets $Z$ such that $\mathcal R_c$ has no $Z$-computable c.b. trace. It is a weakness property containing $\emptyset$, by :ref{#prop-random-no-trace}, and $\mathsf{RT}^2_2$ preserves it, by :ref{#thm-liu-closed-classes}. By :ref{#lem-preservation-ideal}, some Turing ideal satisfying $\mathsf{RT}^2_2$ is contained in $\mathcal W$, so it contains no member of $\mathcal R_c$, a non-empty $\Pi^0_1$ class of positive measure.
:::

:::quiz[traces and randomness]
In the proof of :ref{#prop-random-no-trace}, why is a single constant $c$ used for all members, rather than the class of all random sequences?

- [x] Because the argument bounds below the complexity of every prefix of a member of the class by $n - c$ with the same $c$; for the class of all random sequences, the constant depends on the member, and the class is not closed.
- [ ] Because $\mathcal R_c$ is computable.

  It is $\Pi^0_1$, not computable.
- [ ] Because the trace must have exactly $k$ strings.

  The bound $k$ enters the constant in the complexity of $\rho_n$, not the choice of $c$.

---

In the first case of the proof of :ref{#lem-trace-reduction}, why does the restriction to $n$ of the strings of $F_m$ give a trace at level $n$?

- [x] Because $F_m$ contains the prefix of a member of $\mathcal C$, which is never seen dead, and its restriction to $n$ is again the prefix of that member.
- [ ] Because $m = n$.

  $m \geq n$ is found by a search, and is usually larger.
- [ ] Because dead strings have dead restrictions.

  The restriction of a dead string may be alive; only the live strings matter.
:::

## Exercises

::::exercise{difficulty=1}
Let $C$ be a set with $C \not\leq_T Z$. Show that $\{ C \}$ has no $Z$-computable c.b. trace. Deduce that constant-bound trace avoidance implies cone avoidance.

:::solution
Let $(F_n)$ be a $Z$-computable $k$-trace of $\{ C \}$, and $T$ the set of strings $\tau$ with $\tau \uh m \in F_m$ for every $m \leq |\tau|$. It is a $Z$-computable tree with at most $k$ strings of each length, and $C$ is a path of $T$, since $C \uh m \in F_m$ for every $m$. A tree with at most $k$ strings of each length has at most $k$ paths. So $C$ is an isolated path of $T$, and is $Z$-computable by :ref{#prop-isolated-computable} relativized, a contradiction. If $\mathsf P$ admits c.b. trace avoidance, $C \not\leq_T Z$ and $X \leq_T Z$, a solution $Y$ such that $\{ C \}$ has no $(Z \oplus Y)$-computable c.b. trace satisfies $C \not\leq_T Z \oplus Y$.
:::
::::


## Notes and references

Constant-bound traces, the lemma on disperse sets and the abstract theorem are from the section *Avoiding closed classes* of the chapter *Compactness avoidance* of Patey's monograph, where the lemma is attributed to Liu (2015); Liu calls the traces constant-bound enumerations. Liu proved in this paper that Ramsey's theorem for pairs admits the avoidance of closed classes with no computable constant-bound enumeration, and deduced that $\mathsf{RT}^2_2$ does not imply $\mathsf{WWKL}_0$ (Hirschfeldt, *Slicing the Truth*, Theorem 6.72). :ref{#lem-trace-reduction} solves two exercises of the monograph; the induction on $k$ given here is not uniform. The bound $K(n) \leq 2 \log n + O(1)$ is given by the prefix-free code that writes the length of the binary expansion of $n$ in unary before the expansion itself.

- L. Liu, *Cone avoiding closed sets*, Transactions of the American Mathematical Society 367 (2015), 1609–1630; arXiv:1602.03777.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Section 6.7.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *Avoiding closed classes*.
