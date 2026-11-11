---
title: The KC theorem and the coding theorem
summary: Building prefix-free machines from bounded request sets; K is the least right-c.e. function satisfying the Kraft inequality; the coding theorem identifies K with the logarithm of the halting probability of a string; counting strings of small complexity; Chaitin's number Ω.
duration: 45
prerequisites: [prefix-free-complexity]
---

Constructing a prefix-free machine by hand requires keeping its domain prefix-free, which is often tedious. The **KC theorem**, an effective form of the Kraft inequality, removes this difficulty: to obtain descriptions of prescribed lengths, it suffices to enumerate requests whose total weight is at most $1$. It yields a characterization of $K$ as the least function, up to a constant, that is approximable from above and satisfies the Kraft inequality, and the **coding theorem**, which identifies $2^{-K(\sigma)}$ with the probability that the optimal machine outputs $\sigma$ on a random input. The lesson ends with Chaitin's halting probability $\Omega$.

## Bounded request sets

:::definition{#def-request-set}
A **request** is a pair $(\sigma, \ell) \in \bstr \times \nat$, asking for a description of $\sigma$ of length $\ell$. A set of requests $R$ is **bounded** if its **weight** $\sum_{(\sigma, \ell) \in R} 2^{-\ell}$ is at most $1$. A prefix-free machine $M$ **satisfies** $R$ if for every request $(\sigma, \ell) \in R$ there is a string $\tau$ of length $\ell$ with $M(\tau) = \sigma$, these strings $\tau$ being distinct for distinct requests.
:::

:::theorem[KC theorem; Levin, Schnorr, Chaitin]{#thm-kc}
For every c.e. bounded request set $R$, there is a prefix-free machine $M$ that satisfies $R$. In particular $K(\sigma) \leq^+ \ell$ for every $(\sigma, \ell) \in R$. Moreover, an index of $M$ is computable from an index of $R$.
:::

:::proof{of=thm-kc}
Enumerate $R$ as $(\sigma_0, \ell_0), (\sigma_1, \ell_1), \dots$, one request per stage (if $R$ is finite, the construction stops). We assign to the request $(\sigma_s, \ell_s)$ a string $\tau_s$ of length $\ell_s$, and set $M(\tau_s) = \sigma_s$. Along the construction we maintain a finite set $F_s$ of **free** strings, with the following invariants:

1. the strings $\tau_0, \dots, \tau_{s-1}$ and the elements of $F_s$ form a prefix-free set, the $\tau_i$ being pairwise distinct;
2. the elements of $F_s$ have pairwise distinct lengths;
3. $\sum_{\rho \in F_s} 2^{-|\rho|} = 1 - \sum_{i < s} 2^{-\ell_i}$.

Initially $F_0 = \{ \varepsilon \}$ and no string is assigned; the invariants hold.

At stage $s$, the weight of $R$ gives $2^{-\ell_s} \leq 1 - \sum_{i < s} 2^{-\ell_i} = \sum_{\rho \in F_s} 2^{-|\rho|}$. Some free string has length at most $\ell_s$: otherwise, by invariant 2, the free strings have distinct lengths larger than $\ell_s$, and their weight is less than $\sum_{j > \ell_s} 2^{-j} = 2^{-\ell_s}$. Let $\rho$ be the **longest** free string with $|\rho| \leq \ell_s$, and $k = \ell_s - |\rho|$. Let $\tau_s = \rho\, 0^{k}$, and
$$
F_{s+1} = (F_s \setminus \{ \rho \}) \cup \{ \rho\, 0^j 1 : 0 \leq j < k \}.
$$
The new free strings have the lengths $|\rho| + 1, \dots, \ell_s$; no element of $F_s$ had one of these lengths, by the choice of $\rho$, so invariant 2 is preserved. The strings $\tau_s$ and $\rho\, 0^j 1$, $j < k$, are pairwise incomparable extensions of $\rho$, and $\rho$ was incomparable with the other strings of invariant 1; so invariant 1 is preserved. Finally $2^{-|\rho|} = 2^{-\ell_s} + \sum_{j < k} 2^{-(|\rho| + j + 1)}$, so invariant 3 is preserved.

The construction is effective, so $M$ is a machine; its domain $\{ \tau_s \}$ is prefix-free by invariant 1, and it satisfies $R$. The construction is uniform in an index of $R$. The bound on $K$ follows from optimality: $K \leq K_M + c_M$.
:::

The free strings record the unused part of Cantor space as a union of disjoint cylinders of distinct sizes, like the binary expansion of the remaining weight. A request is served by the smallest free cylinder that is large enough, which is split as needed.

:::figure[A stage of the KC construction. The longest free string of length at most $4$ is $\rho$, of length $2$. A request of length $4$ receives $\rho 00$, and $\rho 1$, $\rho 01$ replace $\rho$ among the free strings.]
<svg class="fig" viewBox="0 0 460 210" role="img" aria-label="KC construction stage"><line class="ink-stroke" x1="230" y1="20" x2="170" y2="58"/><line class="ink-stroke" x1="230" y1="20" x2="290" y2="58"/><line class="ink-stroke" x1="170" y1="58" x2="120" y2="96"/><line class="ink-stroke" x1="120" y1="96" x2="80" y2="134"/><line class="ink-stroke" x1="120" y1="96" x2="160" y2="134"/><line class="ink-stroke" x1="80" y1="134" x2="50" y2="172"/><line class="ink-stroke" x1="80" y1="134" x2="110" y2="172"/><circle class="node" cx="230" cy="20" r="8"/><circle class="node" cx="170" cy="58" r="8"/><circle class="muted-fill" cx="290" cy="58" r="8"/><circle class="node" cx="80" cy="134" r="8"/><circle class="node" cx="120" cy="96" r="8"/><circle class="soft-fill" cx="160" cy="134" r="8"/><circle class="accent-stroke" cx="160" cy="134" r="8"/><circle class="soft-fill" cx="110" cy="172" r="8"/><circle class="accent-stroke" cx="110" cy="172" r="8"/><circle class="accent-fill" cx="50" cy="172" r="8"/><text class="math" x="92" y="100">ρ</text><text class="label" x="304" y="62">other strings</text><text class="label" x="174" y="138">ρ1: free</text><text class="label" x="124" y="176">ρ01: free</text><text class="label" x="0" y="200">ρ00: assigned</text><circle class="soft-fill" cx="300" cy="120" r="7"/><circle class="accent-stroke" cx="300" cy="120" r="7"/><text class="label" x="314" y="124">free string</text><circle class="accent-fill" cx="300" cy="146" r="7"/><text class="label" x="314" y="150">assigned at this stage</text><circle class="muted-fill" cx="300" cy="172" r="7"/><text class="label" x="314" y="176">unaffected</text></svg>
:::

## The characterization of K

A function $f : \bstr \to \nat$ is **approximable from above**, or **right-c.e.**, if there is a computable function $(s, \sigma) \mapsto f_s(\sigma)$, non-increasing in $s$, with $\lim_s f_s(\sigma) = f(\sigma)$. As noted after :ref{#thm-optimal-prefix-free}, $K$ is right-c.e., and by :ref{#prop-k-basic} (4) it satisfies $\sum_\sigma 2^{-K(\sigma)} \leq 1$.

:::theorem{#thm-k-minimal}
If $f : \bstr \to \nat$ is right-c.e. and $\sum_\sigma 2^{-f(\sigma)} \leq 1$, then $K \leq^+ f$. So $K$ is, up to an additive constant, the least right-c.e. function satisfying the Kraft inequality.
:::

:::proof{of=thm-k-minimal}
Let $(f_s)$ be an approximation from above. Enumerate the request $(\sigma, f_0(\sigma) + 1)$ for each $\sigma$, and the request $(\sigma, f_{s+1}(\sigma) + 1)$ whenever $f_{s+1}(\sigma) < f_s(\sigma)$. The requests concerning $\sigma$ have pairwise distinct lengths $v + 1$, with $v$ ranging over the values taken by $f_s(\sigma)$, which are at least $f(\sigma)$. Their weight is at most $\sum_{v \geq f(\sigma)} 2^{-v-1} = 2^{-f(\sigma)}$. The total weight is at most $\sum_\sigma 2^{-f(\sigma)} \leq 1$. By :ref{#thm-kc}, $K(\sigma) \leq^+ f(\sigma) + 1$, since the request $(\sigma, f(\sigma) + 1)$ is enumerated when the approximation reaches its limit.
:::

:::quiz[the KC theorem]
In the proof of :ref{#thm-kc}, why is the **longest** free string of length at most $\ell_s$ chosen?

- [x] To preserve invariant 2: the new free strings have the lengths between $|\rho| + 1$ and $\ell_s$, and no other free string has such a length precisely because $\rho$ is the longest free string of length at most $\ell_s$.
- [ ] To make the machine prefix-free.

  Any free string of length at most $\ell_s$ would keep the domain prefix-free; the choice matters for invariant 2.
- [ ] Because shorter free strings may not exist.

  A free string of length at most $\ell_s$ exists by the weight argument; there may be several.

---

In the proof of :ref{#thm-k-minimal}, why are requests issued with length $f_s(\sigma) + 1$ rather than $f_s(\sigma)$?

- [x] Because $\sigma$ receives one request for each value of the approximation, and the factor $\tfrac12$ makes the total weight of these requests at most $2^{-f(\sigma)}$.
- [ ] Because $f_s(\sigma)$ may be $0$.

  A request of length $0$ is allowed; it has weight $1$.
- [ ] To make $f + 1$ right-c.e.

  $f + 1$ is right-c.e. whenever $f$ is.
:::

## The coding theorem

For a prefix-free machine $M$, the **output probability** of $\sigma$ is
$$
P_M(\sigma) = \sum_{\tau : M(\tau) = \sigma} 2^{-|\tau|}.
$$
It is the probability that $M$ outputs $\sigma$ when its input is produced by tossing a fair coin, the machine reading bits as needed. By :ref{#prop-kraft}, $\sum_\sigma P_M(\sigma) \leq 1$. Clearly $P_U(\sigma) \geq 2^{-K(\sigma)}$, the contribution of a shortest description.

:::theorem[Coding theorem; Levin, Chaitin]{#thm-coding}
For every prefix-free machine $M$, $K(\sigma) \leq^+ -\log P_M(\sigma)$ for every $\sigma$ with $P_M(\sigma) > 0$. In particular $K(\sigma) =^+ -\log P_U(\sigma)$.
:::

:::proof{of=thm-coding}
Let $P_{M,s}(\sigma)$ be the sum over the descriptions $\tau$ of $\sigma$ such that $|\tau| \leq s$ and $M(\tau)[s]\converge$; it is computable, non-decreasing in $s$, with limit $P_M(\sigma)$. For each $k \geq 1$ and $\sigma$, enumerate the request $(\sigma, k + 1)$ when $P_{M,s}(\sigma) > 2^{-k}$ for the first time. Fix $\sigma$ with $P_M(\sigma) > 0$, and let $k_0$ be the least $k$ with $P_M(\sigma) > 2^{-k}$; then $k_0 \geq 1$, since $P_M(\sigma) \leq 1$. The requests about $\sigma$ are those with $k \geq k_0$, of total weight $\sum_{k \geq k_0} 2^{-k-1} = 2^{-k_0} < P_M(\sigma)$. So the request set is bounded by $\sum_\sigma P_M(\sigma) \leq 1$. By :ref{#thm-kc}, $K(\sigma) \leq^+ k_0 + 1$. By minimality of $k_0$, $P_M(\sigma) \leq 2^{-(k_0 - 1)}$, so $k_0 \leq 1 - \log P_M(\sigma)$, and $K(\sigma) \leq^+ -\log P_M(\sigma)$.
:::

The theorem says that a string that is produced with large probability has a short description. Equivalently, up to a multiplicative constant, the shortest description accounts for the whole output probability of a string: $P_U(\sigma) \leq 2^{c - K(\sigma)}$.

:::theorem[Counting theorem; Chaitin]{#thm-k-counting}
There is a constant $c$ such that for all $n$ and $k$, fewer than $2^{n - k + c}$ strings $\sigma$ of length $n$ satisfy $K(\sigma) < n + K(n) - k$.
:::

:::proof{of=thm-k-counting}
Let $M$ be the prefix-free machine $\tau \mapsto |U(\tau)|$, with the domain of $U$. Then $P_M(n) = \sum_{|\sigma| = n} P_U(\sigma) \geq \sum_{|\sigma| = n} 2^{-K(\sigma)}$. By the coding theorem, $2^{-K(n)} \geq 2^{-c} P_M(n)$ for a constant $c$. Let $N$ be the number of strings $\sigma$ of length $n$ with $K(\sigma) < n + K(n) - k$. Each contributes more than $2^{-n - K(n) + k}$ to $P_M(n)$, so $N\, 2^{-n - K(n) + k} < P_M(n) \leq 2^{c - K(n)}$, and $N < 2^{n - k + c}$.
:::

With $k = c + 1$, fewer than half of the strings of length $n$ have $K(\sigma) < n + K(n) - c - 1$. This proves the second part of :ref{#cor-k-above-length}: most strings of length $n$ have complexity $n + K(n) - O(1)$, the maximal value.

## Chaitin's halting probability

:::definition{#def-omega}
The **halting probability** of $U$ is
$$
\Omega = \sum_{\tau : U(\tau)\converge} 2^{-|\tau|} = \sum_\sigma P_U(\sigma).
$$
:::

By :ref{#prop-kraft}, $\Omega \leq 1$, and $\Omega > 0$ since $U$ has a non-empty domain. The theorem below shows that $\Omega$ is irrational, so $0 < \Omega < 1$ and $\Omega$ has a unique binary expansion $\omega = \omega_0 \omega_1 \cdots$, with $\Omega = \sum_i \omega_i 2^{-i-1}$; we identify $\Omega$ with the sequence $\omega$. The rationals $\Omega_s = \sum \{ 2^{-|\tau|} : |\tau| \leq s,\ U(\tau)[s]\converge \}$ form a computable non-decreasing sequence with limit $\Omega$: $\Omega$ is **left-c.e.**

:::theorem[Chaitin]{#thm-omega}
1. $\Omega \equiv_T \emptyset'$.
2. $\Omega$ is irrational, and for every $n$, the prefix $\omega \uh n$ determines, uniformly in $n$, the set of strings of length at most $n$ in the domain of $U$.
3. There is a constant $c$ with $K(\omega \uh n) \geq n - c$ for every $n$.
:::

:::proof{of=thm-omega}
*Settled stages.* If $\Omega - \Omega_s < 2^{-n}$ and $s \geq n$, then every string $\tau$ of length at most $n$ in the domain of $U$ satisfies $U(\tau)[s]\converge$: otherwise $\tau$ is not counted in $\Omega_s$, and $\Omega \geq \Omega_s + 2^{-|\tau|} \geq \Omega_s + 2^{-n}$. So the strings of length at most $n$ in the domain of $U$ are those that converge by stage $s$.

*The domain of $U$ computes $\emptyset'$.* Let $M$ be the prefix-free machine with $M(1^e 0) = 0^s$, where $s$ is the least stage with $\Phi_e(e)[s]\converge$, and $M$ undefined elsewhere. Let $d$ be such that $K \leq K_M + d$. If $\Phi_e(e)$ converges at stage $s$, then $K(0^s) \leq e + 1 + d$. With the domain of $U$ as an oracle, compute the outputs of the strings of length at most $e + 1 + d$ in the domain, and let $t$ be the largest number with $0^t$ among them ($t = 0$ if there is none). Then $\Phi_e(e)\converge$ if and only if $\Phi_e(e)[t]\converge$.

*$\Omega$ is irrational.* If $\Omega$ were rational, then, given $n$, the search for a stage $s \geq n$ with $\Omega - \Omega_s < 2^{-n}$ would be effective, since $\Omega$ and $\Omega_s$ are rationals, and it terminates since $\Omega_s$ tends to $\Omega$. By the first paragraph, the domain of $U$ would be computable, and so would be $\emptyset'$, which is not the case.

*Prefixes of $\omega$.* Let $q = 0.\omega_0 \cdots \omega_{n-1}$. Since $\Omega$ is irrational, $q < \Omega < q + 2^{-n}$. Search for $s \geq n$ with $\Omega_s > q$; it exists, and then $\Omega - \Omega_s < 2^{-n}$, so $s$ is settled for $n$. This procedure only uses $\omega \uh n$, which proves 2. In particular $\omega$ computes the domain of $U$, hence $\emptyset'$.

*$\omega \leq_T \emptyset'$.* For a dyadic rational $q$, $q < \Omega$ holds if and only if $\Omega_s > q$ for some $s$, a c.e. condition, so $\emptyset'$ decides it; and $q \neq \Omega$, since $\Omega$ is irrational. The prefix $\omega \uh k$ is the binary expansion of the largest $q = j 2^{-k}$ with $q < \Omega$, so $\emptyset'$ computes $\omega$. This proves 1.

*Incompressibility.* Let $N$ be the machine that, on input $\tau$, computes $\rho = U(\tau)$ and $n = |\rho|$, runs the procedure of 2 as if $\rho$ were $\omega \uh n$, obtaining a stage $s$ if the search terminates, lists the outputs of the strings of length at most $n$ that converge by stage $s$, and outputs the first string, in the length-lexicographic order, that is not in this list. The domain of $N$ is contained in that of $U$, so $N$ is prefix-free. If $U(\tau) = \omega \uh n$, the list contains every string $\sigma$ with $K(\sigma) \leq n$, by 2, so $N(\tau)$ has complexity larger than $n$. Let $c$ be such that $K \leq K_N + c$, and let $\tau$ be a shortest description of $\omega \uh n$. Then $n < K(N(\tau)) \leq |\tau| + c = K(\omega \uh n) + c$.
:::

Statement 3 says that $\omega$ is random in the sense announced in the previous lesson. The first $n$ bits of $\Omega$ solve the halting problem for all programs of length at most $n$, and yet they cannot be compressed: up to a constant, no prefix-free description of them is shorter than $n$.

:::quiz[Chaitin's Ω]
Why does a stage $s$ with $\Omega - \Omega_s < 2^{-n}$ settle the halting of all programs of length at most $n$?

- [x] Because a program of length at most $n$ halting after stage $s$ would add at least $2^{-n}$ to the sum, beyond $\Omega_s$, so that $\Omega - \Omega_s \geq 2^{-n}$.
- [ ] Because $U$ halts on every program of length at most $n$ before stage $n$.

  Halting times are not computably bounded; this is the point of the halting problem.
- [ ] Because $\Omega_s$ is a dyadic rational.

  This plays no role; the argument compares weights.

---

In the incompressibility proof, why is the machine $N$ prefix-free?

- [x] Because it first computes $U(\tau)$, so its domain is contained in the domain of $U$, which is prefix-free.
- [ ] Because its outputs are pairwise distinct.

  Prefix-freeness concerns the inputs, not the outputs.
- [ ] Because the search for $s$ always terminates.

  It may not terminate when $U(\tau)$ is not a prefix of $\omega$; this only makes the domain smaller.
:::

## Exercises

::::exercise{difficulty=1}
Show that there is a constant $c$ such that every string $\sigma$ has at most $2^{c+d}$ descriptions $\tau$ with $|\tau| \leq K(\sigma) + d$, for every $d$.

:::solution
By the coding theorem, $P_U(\sigma) \leq 2^{c - K(\sigma)}$. Each description $\tau$ with $|\tau| \leq K(\sigma) + d$ contributes at least $2^{-K(\sigma) - d}$ to $P_U(\sigma)$. So there are at most $2^{c - K(\sigma)} / 2^{-K(\sigma) - d} = 2^{c + d}$ of them.
:::
::::

::::exercise{difficulty=1}
Let $f : \nat \to \nat$ be computable with $\sum_n 2^{-f(n)} < \infty$. Show that $K(n) \leq^+ f(n)$. Deduce that $K(n) \leq^+ \log n + 2 \log \log n$ for $n \geq 4$, and show that $K(n) > \log n + \log \log n$ for infinitely many $n$.

:::solution
Let $c$ be such that $\sum_n 2^{-f(n) - c} \leq 1$. The computable function $f + c$ is right-c.e. and satisfies the Kraft inequality, so $K \leq^+ f + c$ by :ref{#thm-k-minimal}. The series $\sum_{n \geq 4} 1/(n (\log n)^2)$ converges, which gives the second bound with $f(n) = \lceil \log n + 2 \log \log n \rceil$ for $n \geq 4$. If $K(n) \leq \log n + \log \log n$ for all $n \geq n_0$, then $\sum_n 2^{-K(n)} \geq \sum_{n \geq n_0} 1/(n \log n)$, which diverges, contradicting :ref{#prop-k-basic} (4).
:::
::::

## Notes and references

The KC theorem was proved by Levin (1971) and Schnorr (1973), and by Chaitin (1975), who gave it its usual form; the name stands for Kraft and Chaitin. The coding theorem is due to Levin (1974) and Chaitin (1975). Chaitin (1975) introduced $\Omega$; Solovay, Calude, Hertling, Khoussainov, Wang, Kučera and Slaman showed that the left-c.e. reals that are random in the sense of the next course are exactly the halting probabilities of optimal prefix-free machines.

- L. A. Levin, *Laws of information conservation (nongrowth) and aspects of the foundation of probability theory*, Problems of Information Transmission 10 (1974), 206–210.
- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- C. P. Schnorr, *Process complexity and effective random tests*, Journal of Computer and System Sciences 7 (1973), 376–388.
- A. Kučera and T. A. Slaman, *Randomness and recursive enumerability*, SIAM Journal on Computing 31 (2001), 199–211.
