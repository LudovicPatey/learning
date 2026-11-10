---
title: Lowness for randomness
summary: Sets that are low for K, low for Martin-Löf randomness, and bases for randomness; the three notions coincide by the hungry sets theorem; they also coincide with K-triviality, by a theorem of Nies and Hirschfeldt, admitted here; consequences for the K-trivial sets.
duration: 45
prerequisites: [cost-functions, martin-lof-randomness/randomness-and-degrees]
---

An oracle $A$ can be used to compress strings and to test sequences for randomness. A set is **low** for a relativizable notion if, used as an oracle, it does not change the notion. For prefix-free complexity and Martin-Löf randomness, the low sets are exactly the K-trivial sets. This lesson proves the equivalence of three lowness notions, by the hungry sets argument of Hirschfeldt, Nies and Stephan, and states the theorem of Nies and Hirschfeldt that connects them to K-triviality.

## Relativized complexity and randomness

An **oracle prefix-free machine** is an oracle machine $M$ such that, for every oracle $X$, the domain of $M^X$ is prefix-free. The constructions of :ref{to="kolmogorov-complexity/prefix-free-complexity"} relativize uniformly: there is an oracle prefix-free machine $U$ such that, for every oracle prefix-free machine $M$, there is $c$ with $K_{U^X} \leq K_{M^X} + c$ for every oracle $X$. We write $K^A = K_{U^A}$, and $\mathrm{MLR}^A$ for the class of sequences passing every Martin-Löf test relative to $A$, the tests whose components are uniformly $\Sigma^0_1(A)$. The results of the course on Martin-Löf randomness relativize, by the same proofs; in particular $Z \in \mathrm{MLR}^A$ if and only if $K^A(Z \uh n) \geq n - O(1)$, and $\sum_{\tau \in \dom U^A} 2^{-|\tau|} \leq 1$.

If $B \leq_T A$, then $K^A \leq^+ K^B$, since a machine with oracle $A$ can simulate $U^B$; in particular $K^A \leq^+ K$. So oracles can only make complexity smaller and randomness harder.

For a string $\rho$, we write $U^\rho(\tau)\converge = x$ when the computation of $U$ on input $\tau$ with oracle $\rho$ halts with output $x$ and its use is exactly $|\rho|$, in the sense of :ref{#def-use}. The set of triples $(\rho, \tau, x)$ with $U^\rho(\tau)\converge = x$ is c.e., and for every oracle $X$ and every $\tau \in \dom U^X$, there is exactly one $\rho \prec X$ with $U^\rho(\tau)\converge$, namely $X \uh u$ for the use $u$ of the computation.

## Three lowness notions

:::definition{#def-lowness-randomness}
Let $A$ be a set.

1. $A$ is **low for K** if $K(\sigma) \leq^+ K^A(\sigma)$ for every string $\sigma$.
2. $A$ is **low for Martin-Löf randomness** if $\mathrm{MLR}^A = \mathrm{MLR}$.
3. $A$ is a **base for randomness** if $A \leq_T Z$ for some $Z \in \mathrm{MLR}^A$.
:::

Every computable set has the three properties. For a non-computable set $A$, the sequences computing $A$ form a null class (:ref{#thm-sacks}); a base for randomness is a set computed by some sequence that is nevertheless random relative to $A$.

:::proposition{#prop-lowness-implications}
1. If $A$ is low for K, then $A$ is K-trivial.
2. If $A$ is low for K, then $A$ is low for Martin-Löf randomness.
3. If $A$ is low for Martin-Löf randomness, then $A$ is a base for randomness.
4. The sets that are low for K are closed downward under $\leq_T$.
:::

:::proof{of=prop-lowness-implications}
1. With oracle $A$, the string $A \uh n$ is computed from $n$, so $K^A(A \uh n) \leq^+ K^A(n) \leq^+ K(n)$. If $A$ is low for K, then $K(A \uh n) \leq^+ K^A(A \uh n) \leq^+ K(n)$.
2. $\mathrm{MLR}^A \subseteq \mathrm{MLR}$ for every $A$, since a test without oracle is a test relative to $A$. Conversely, let $Z \in \mathrm{MLR}$, so that $K(Z \uh n) \geq n - c$. If $A$ is low for K, then $K^A(Z \uh n) \geq K(Z \uh n) - d \geq n - c - d$, and $Z \in \mathrm{MLR}^A$ by the relativized Levin–Schnorr theorem.
3. By the Kučera–Gács theorem (:ref{#thm-kucera-gacs}), some $Z \in \mathrm{MLR}$ computes $A$, and $\mathrm{MLR} = \mathrm{MLR}^A$.
4. If $B \leq_T A$ and $A$ is low for K, then $K \leq^+ K^A \leq^+ K^B$.
:::

## The hungry sets theorem

:::theorem[Hirschfeldt, Nies, Stephan]{#thm-hungry-sets}
Every base for randomness is low for K.
:::

:::proof{of=thm-hungry-sets}
Let $Z \in \mathrm{MLR}^A$ and $\Phi$ a Turing functional with $\Phi^Z = A$. For a string $\eta$ and a string $\rho$, write $\Phi^\eta[s] \succeq \rho$ if $\Phi^\eta(i)[s]\converge = \rho(i)$ for every $i < |\rho|$.

*The construction.* Fix a parameter $d \in \nat$. For each triple $(\rho, \tau, x)$ with $U^\rho(\tau)\converge = x$ we enumerate a finite or infinite set of strings $C = C^\rho_{\tau, x}$, the **hungry set** of the triple, which aims at a measure $2^{-|\tau| - d}$. Each triple is first considered at the stage $s_0$ at which the computation $U^\rho(\tau)\converge = x$ is found. At each stage $s \geq s_0$, the triples considered so far are processed in turn. For the triple $(\rho, \tau, x)$, each string $\eta$ of length $s$ such that
1. $\Phi^\eta[s] \succeq \rho$,
2. $[\eta]$ is disjoint from the classes $[C']^{\prec}$ of all hungry sets $C'$, in their current state, and
3. $\lambda([C]^{\prec}) + 2^{-s} \leq 2^{-|\tau| - d}$,

is added to $C$, the strings being examined in lexicographic order. At the end of the processing of the triple, if $\lambda([C]^{\prec}) \geq 2^{-|\tau| - d - 1}$ and no request has yet been made for this triple, the request $(x, |\tau| + d + 1)$ is enumerated into a set $R_d$.

At stage $s$, every string in a hungry set has length at most $s$, so for $|\eta| = s$ the cylinder $[\eta]$ is either contained in or disjoint from each class $[C']^{\prec}$; condition 2 is decidable. By condition 2, the classes $[C]^{\prec}$ of distinct hungry sets are pairwise disjoint, and by condition 3, $\lambda([C^\rho_{\tau, x}]^{\prec}) \leq 2^{-|\tau| - d}$.

*$R_d$ is a bounded request set.* A request $(x, |\tau| + d + 1)$ is made for a triple only when its hungry set has measure at least $2^{-|\tau| - d - 1}$, the weight of the request. Since the hungry sets are disjoint, the total weight of $R_d$ is at most $\lambda\big(\bigcup [C^\rho_{\tau, x}]^{\prec}\big) \leq 1$.

*A test relative to $A$.* Let $\mathcal V_d$ be the union of the classes $[C^\rho_{\tau, x}]^{\prec}$ over the triples with $\rho \prec A$, for the construction with parameter $d$. It is $\Sigma^0_1(A)$, uniformly in $d$. For each $\tau \in \dom U^A$ there is exactly one triple $(\rho, \tau, x)$ with $\rho \prec A$, so
$$
\lambda(\mathcal V_d) \leq \sum_{\tau \in \dom U^A} 2^{-|\tau| - d} \leq 2^{-d}.
$$
So $(\mathcal V_d)$ is a Martin-Löf test relative to $A$, and since $Z \in \mathrm{MLR}^A$, there is $d$ with $Z \notin \mathcal V_d$. Fix this $d$.

*Every hungry set of a true computation becomes half full.* Let $\rho \prec A$ with $U^\rho(\tau)\converge = x$, and suppose that the hungry set $C = C^\rho_{\tau, x}$ never reaches measure $2^{-|\tau| - d - 1}$. Since $\Phi^Z = A \succ \rho$, there is a stage $s$, after the triple is first considered, with $\Phi^{Z \uh s}[s] \succeq \rho$ and $2^{-s} \leq 2^{-|\tau| - d - 1}$. Let $\eta = Z \uh s$, and consider the processing of the triple at stage $s$. Condition 1 holds for $\eta$. If $[\eta]$ were contained in a hungry set $C' = C^{\rho'}_{\tau', x'}$, then some $\eta' \preceq \eta$ was added to $C'$, so $\Phi^{\eta'} \succeq \rho'$ and, since $\eta' \prec Z$, $\rho' \prec \Phi^Z = A$; then $Z \in [C']^{\prec} \subseteq \mathcal V_d$, a contradiction. So condition 2 holds. Condition 3 holds since $\lambda([C]^{\prec}) + 2^{-s} < 2^{-|\tau| - d - 1} + 2^{-|\tau| - d - 1}$. So $\eta$ is added to $C$, and $Z \in [C]^{\prec} \subseteq \mathcal V_d$, again a contradiction.

*Conclusion.* For every $\tau \in \dom U^A$ with $U^A(\tau) = x$, the triple with $\rho \prec A$ has its hungry set half full, and the request $(x, |\tau| + d + 1)$ belongs to $R_d$. By the KC theorem applied to the c.e. bounded request set $R_d$, $K(x) \leq |\tau| + d + O(1)$. Taking $\tau$ a shortest description of $x$ relative to $A$ gives $K(x) \leq^+ K^A(x)$.
:::

The hungry sets convert descriptions relative to $A$ into descriptions without oracle. A description $\tau$ of $x$ with oracle prefix $\rho$ is paid for by measure: the hungry set eats the oracles $\eta$ that compute $\rho$ through $\Phi$, until it has eaten $2^{-|\tau| - d - 1}$. If it starves, $Z$ is in a hungry set of a true computation, which is impossible when $d$ is chosen so that $Z$ avoids the $d$-th component of a test relative to $A$. The parameter $d$ is not known effectively, but this is harmless: for each $d$, $R_d$ is a c.e. bounded request set, and only the existence of a good $d$ is needed.

:::quiz[the hungry sets theorem]
In the proof of :ref{#thm-hungry-sets}, why must the hungry sets be pairwise disjoint?

- [x] So that the total weight of the requests, each bounded by the measure of a hungry set, is at most the measure of their union, hence at most $1$.
- [ ] So that the test $(\mathcal V_d)$ is uniformly $\Sigma^0_1(A)$.

  Uniformity comes from the effectiveness of the construction; disjointness is needed for the weight bound.
- [ ] So that $Z$ belongs to exactly one hungry set.

  The argument shows that $Z$ belongs to no hungry set of a true computation.

---

Where is it used that $Z$ is random relative to $A$, and not merely random?

- [x] The classes $\mathcal V_d$ collect the hungry sets of the triples with $\rho \prec A$: they form a test relative to $A$, not a test without oracle.
- [ ] To ensure that $\Phi^Z = A$.

  This is the hypothesis that $A$ is computed by $Z$; it is independent of randomness.
- [ ] To bound the weight of $R_d$.

  The weight bound uses only disjointness.

---

Why does a hungry set of a true computation that never becomes half full lead to a contradiction?

- [x] Because a long enough prefix $\eta$ of $Z$ computes $\rho$ through $\Phi$, and is either already in some hungry set of a true computation or is eaten by this one; in both cases $Z \in \mathcal V_d$.
- [ ] Because the measure of the hungry set is then less than $2^{-d}$.

  Small measure is not contradictory in itself; the contradiction is that $Z$ ends up in $\mathcal V_d$.
- [ ] Because $U^\rho(\tau)$ diverges.

  The triple is considered precisely because the computation converges.
:::

:::corollary{#cor-lowness-equivalent}
For every set $A$, the following are equivalent: $A$ is low for K; $A$ is low for Martin-Löf randomness; $A$ is a base for randomness.
:::

:::proof{of=cor-lowness-equivalent}
By :ref{#prop-lowness-implications} (2) and (3), and :ref{#thm-hungry-sets}.
:::

In particular, by :ref{#prop-lowness-implications} (1), all these sets are K-trivial, hence $\Delta^0_2$.

## K-triviality and lowness

The converse of :ref{#prop-lowness-implications} (1) is the central theorem on K-triviality.

:::theorem[Nies; Hirschfeldt, Nies]{#thm-ktrivial-lowk}
Every K-trivial set is low for K.
:::

The proof, known as the **golden run** construction, is a priority argument of considerable length, and is admitted here; see Nies (2005), or Nies, *Computability and Randomness*, Section 5.4, and Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, Chapter 11. A later proof, through the characterization of the K-trivial sets as the sets computable from some incomplete random sequence, is due to Bienvenu, Day, Greenberg, Kučera, Miller, Nies and Turetsky (2014). Granting the theorem, the following consequences are immediate.

:::corollary{#cor-ktrivial-equivalent}
For a set $A$, the following are equivalent:

1. $A$ is K-trivial;
2. $A$ is low for K;
3. $A$ is low for Martin-Löf randomness;
4. $A$ is a base for randomness.

The K-trivial sets form an ideal of the Turing degrees: they are closed downward under $\leq_T$, and under $\oplus$.
:::

:::proof{of=cor-ktrivial-equivalent}
(1 ⇔ 2) by :ref{#thm-ktrivial-lowk} and :ref{#prop-lowness-implications} (1); the other equivalences by :ref{#cor-lowness-equivalent}. Closure downward holds for low for K sets by :ref{#prop-lowness-implications} (4), and closure under join for K-trivial sets by :ref{#prop-k-trivial-join}.
:::

Downward closure is not apparent from the definition of K-triviality, and closure under join is not apparent from the definition of lowness for K; the equivalence yields both.

## Exercises

::::exercise{difficulty=2}
Show that every set that is low for K is low, that is, $A' \leq_T \emptyset'$. Deduce, using :ref{#thm-ktrivial-lowk}, that no K-trivial set is Turing complete.

:::hint
For $e \in A'$, the use of the computation $\Phi^A_e(e)$ gives a prefix of $A$ with a short description relative to $A$.
:::

:::solution
Let $A$ be low for K; it is K-trivial, hence $\Delta^0_2$. Let $g$ be the partial $A$-computable function with $g(e) = A \uh u$ when $\Phi^A_e(e)\converge$ with use $u$. Then $K^A(g(e)) \leq^+ K(e) \leq^+ 2 \log e$, and since $A$ is low for K, there is $c$ with $K(g(e)) \leq 2 \log e + c$ for every $e \in A'$, for $e \geq 2$.

With oracle $\emptyset'$, decide $e \in A'$ as follows: for each string $\sigma$ of length at most $2 \log e + c$, decide whether $U(\sigma)$ converges; if it does, with output $\rho$, decide whether $\rho \prec A$, which is possible since $A \leq_T \emptyset'$, and whether $\Phi^\rho_e(e)\converge$, a $\Sigma^0_1$ question. Answer yes if some $\sigma$ passes all three tests. If $e \in A'$, then a shortest description of $g(e)$ passes them. Conversely, if $\rho \prec A$ and $\Phi^\rho_e(e)\converge$, then $\Phi^A_e(e)\converge$ by the use principle. So $A' \leq_T \emptyset'$.

A complete set $A$ has $A' \equiv_T \emptyset''$, which is not computable in $\emptyset'$; so a K-trivial set, which is low for K by :ref{#thm-ktrivial-lowk}, is not complete.
:::
::::

::::exercise{difficulty=2}
Show without :ref{#thm-ktrivial-lowk} that a base for randomness $A$ is not Turing complete.

:::solution
By :ref{#thm-hungry-sets}, $A$ is low for K, and by the first exercise it is low, hence not complete.
:::
::::

## Notes and references

Lowness for Martin-Löf randomness was introduced by Zambella (1990) and Kučera and Terwijn (1999), who built a non-computable c.e. set low for randomness. Lowness for K is due to Muchnik, who built a non-computable c.e. set low for K. Nies (2005) proved that low for K and low for randomness coincide, and, with Hirschfeldt, that both coincide with K-triviality. The notion of base for randomness and the hungry sets argument are due to Kučera (1993) and to Hirschfeldt, Nies and Stephan (2007).

- A. Nies, *Lowness properties and randomness*, Advances in Mathematics 197 (2005), 274–305.
- D. R. Hirschfeldt, A. Nies and F. Stephan, *Using random sets as oracles*, Journal of the London Mathematical Society 75 (2007), 610–622.
- A. Kučera and S. A. Terwijn, *Lowness for the class of random sets*, Journal of Symbolic Logic 64 (1999), 1396–1402.
- L. Bienvenu, A. R. Day, N. Greenberg, A. Kučera, J. S. Miller, A. Nies and D. Turetsky, *Computing K-trivial sets by incomplete random sets*, Bulletin of Symbolic Logic 20 (2014), 80–90.
