---
title: The hungry sets theorem
summary: Every base for randomness is low for K, by the hungry sets construction of Hirschfeldt, Nies and Stephan; hence being low for K, low for Martin-Löf randomness and a base for randomness are equivalent.
duration: 35
prerequisites: [lowness]
---

A base for randomness $A$ is computed by a sequence $Z$ that is random relative to $A$. This lesson proves that such a set is low for K: every description of a string with oracle $A$ can be replaced by a description without oracle that is longer by a constant. With the implications of the previous lesson, the three lowness notions coincide. The proof introduces a technique used throughout the study of lowness: requests to the KC theorem are paid for by the measure of disjoint open sets, and randomness relative to $A$ guarantees that the measure is available where it is needed.

## The theorem

:::theorem[Hirschfeldt, Nies, Stephan]{#thm-hungry-sets}
Every base for randomness is low for K.
:::

Let $Z \in \mathrm{MLR}^A$ compute $A$ through a functional $\Phi$. We must turn each description $\tau$ of a string $x$ relative to $A$ into a description of $x$ without oracle, of length $|\tau| + O(1)$, with the KC theorem. The difficulty is that $A$ is unknown: a computation $U^\rho(\tau) = x$ is found for many strings $\rho$, most of which are not prefixes of $A$, and requesting a description for all of them would exceed the weight bound. The solution is to make each request pay for itself in measure. To the computation, we attach a **hungry set** of oracles: we feed it the cylinders $[\eta]$ of the oracles $\eta$ that compute $\rho$ through $\Phi$, until it has eaten measure $2^{-|\tau| - d - 1}$, and only then do we request a description of $x$ of length $|\tau| + d + 1$. The hungry sets are kept disjoint, so the total weight of the requests is at most the measure of their union, at most $1$. This **accounting** of the weight of requests against the measure of disjoint open sets is the technique of the proof.

It remains to see why the hungry set of a true computation, one with $\rho \prec A$, is fed enough. The prefixes of $Z$ compute longer and longer prefixes of $A$, so they are candidates for every such hungry set. The hungry sets of true computations form a test relative to $A$, since $A$ can recognize the true computations; $Z$ is random relative to $A$, so for a suitable $d$ it avoids this test. Then every hungry set of a true computation reaches half its target: otherwise it would eventually eat a prefix of $Z$, unless a prefix of $Z$ already belongs to another hungry set of a true computation, and in both cases $Z$ would belong to the test.

:::figure[Hungry sets for a fixed parameter $d$, drawn in Cantor space. Each is a union of cylinders, pairwise disjoint across hungry sets, with a target measure $2^{-|\tau| - d}$; a request is made when half the target is reached. The bottom row is the class $\mathcal V_d$, the union of the hungry sets of the computations whose oracle is a prefix of $A$. When $Z$ avoids $\mathcal V_d$, every such hungry set reaches half its target, as the proof shows.]
<svg class="fig" viewBox="0 0 600 260" width="600" role="img" aria-label="Cantor space as an interval; four hungry sets made of disjoint cylinders of length 5, three of them attached to computations with an oracle prefix of A and one not; the union of the first three is the class V_d, which does not contain the sequence Z"><text x="150.0" y="16.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="520.0" y="16.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="10" y="41" class="label">true, target 2⁻³</text><rect x="150" y="26" width="370" height="22" class="cell"/><rect x="151.0" y="27" width="9.6" height="20" class="head-cell"/><rect x="162.6" y="27" width="9.6" height="20" class="head-cell"/><rect x="174.1" y="27" width="9.6" height="20" class="head-cell"/><rect x="185.7" y="27" width="9.6" height="20" class="head-cell"/><text x="526" y="41" class="label">full</text><text x="10" y="75" class="label">true, target 2⁻³</text><rect x="150" y="60" width="370" height="22" class="cell"/><rect x="243.5" y="61" width="9.6" height="20" class="head-cell"/><rect x="255.1" y="61" width="9.6" height="20" class="head-cell"/><text x="526" y="75" class="label">half full</text><text x="10" y="109" class="label">true, target 2⁻⁴</text><rect x="150" y="94" width="370" height="22" class="cell"/><rect x="382.2" y="95" width="9.6" height="20" class="head-cell"/><rect x="393.8" y="95" width="9.6" height="20" class="head-cell"/><text x="526" y="109" class="label">full</text><text x="10" y="143" class="label">false, target 2⁻³</text><rect x="150" y="128" width="370" height="22" class="cell"/><rect x="428.5" y="129" width="9.6" height="20" class="soft-fill"/><rect x="440.1" y="129" width="9.6" height="20" class="soft-fill"/><rect x="451.6" y="129" width="9.6" height="20" class="soft-fill"/><text x="526" y="143" class="label">3/4 full</text><text x="10.0" y="188.0" text-anchor="start" class="math" font-size="15">V<tspan class="mrm" font-size="10" dy="4">d</tspan></text><rect x="150" y="172" width="370" height="22" class="cell"/><rect x="151.0" y="173" width="9.6" height="20" class="head-cell"/><rect x="162.6" y="173" width="9.6" height="20" class="head-cell"/><rect x="174.1" y="173" width="9.6" height="20" class="head-cell"/><rect x="185.7" y="173" width="9.6" height="20" class="head-cell"/><rect x="243.5" y="173" width="9.6" height="20" class="head-cell"/><rect x="255.1" y="173" width="9.6" height="20" class="head-cell"/><rect x="382.2" y="173" width="9.6" height="20" class="head-cell"/><rect x="393.8" y="173" width="9.6" height="20" class="head-cell"/><line x1="316.9" y1="168" x2="316.9" y2="202" class="accent-stroke" stroke-width="2"/><text x="316.9" y="218.0" text-anchor="middle" class="math" font-size="15">Z</text><text x="150" y="238" class="label">bottom row: the union of the hungry sets of true computations; Z avoids it</text></svg>
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

The parameter $d$ is not known effectively, but this is harmless: for each $d$, $R_d$ is a c.e. bounded request set, and only the existence of a good $d$ is needed.

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

The converse of :ref{#prop-lowness-implications} (1), that every K-trivial set is low for K, is the central theorem on K-triviality; it is discussed in the last lesson.

## Exercises

::::exercise{difficulty=2}
Show that a base for randomness is not Turing complete.

:::solution
By :ref{#thm-hungry-sets}, a base for randomness $A$ is low for K, and by the exercise of the previous lesson it is low. A complete set $A$ has $A' \equiv_T \emptyset''$, which is not computable in $\emptyset'$; so $A$ is not complete.
:::
::::

::::exercise{difficulty=2}
Let $Z_0$ and $Z_1$ be sequences such that $Z_1$ is random relative to $Z_0$. Show that every set $X$ with $X \leq_T Z_0$ and $X \leq_T Z_1$ is low for K.

:::solution
A Martin-Löf test relative to $X$ is a test relative to $Z_0$, since $X \leq_T Z_0$: the components, uniformly $\Sigma^0_1(X)$, are uniformly $\Sigma^0_1(Z_0)$. So $\mathrm{MLR}^{Z_0} \subseteq \mathrm{MLR}^X$, and $Z_1 \in \mathrm{MLR}^X$. Since $X \leq_T Z_1$, $X$ is a base for randomness, hence low for K by :ref{#thm-hungry-sets}. By van Lambalgen's theorem, the hypothesis holds when $Z_0 \oplus Z_1$ is random; so a set computed by both halves of a random sequence is low for K.
:::
::::

## Notes and references

The hungry sets theorem is due to Hirschfeldt, Nies and Stephan (2007). The proof given here, with the conclusion "low for K", follows Nies; Downey and Hirschfeldt present the argument with the conclusion "K-trivial", which suffices with the main theorem of the last lesson. Nies (2005) had proved earlier, by a different argument, that lowness for K and lowness for Martin-Löf randomness coincide. The second exercise is a corollary of Hirschfeldt, Nies and Stephan.

The theorem is Theorem 5.1.22 of Nies, *Computability and Randomness*, with the accounting method as Remark 5.1.21, and Theorem 11.7.2 of Downey and Hirschfeldt, *Algorithmic Randomness and Complexity*, with the second exercise as Corollary 11.7.3.

- A. Nies, *Lowness properties and randomness*, Advances in Mathematics 197 (2005), 274–305.
- D. R. Hirschfeldt, A. Nies and F. Stephan, *Using random sets as oracles*, Journal of the London Mathematical Society 75 (2007), 610–622.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 5.1.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 11.7.
