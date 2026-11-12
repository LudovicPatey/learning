---
title: The coding theorem and Chaitin's Ω
summary: The coding theorem identifies K with minus the logarithm of the probability that the optimal machine outputs a string; counting strings of small complexity; Chaitin's halting probability Ω is Turing complete and has incompressible prefixes.
duration: 45
prerequisites: [kc-theorem]
---

A string may have many descriptions, and its complexity only counts the shortest one. The **coding theorem** says that the other descriptions do not matter, up to a multiplicative constant: the probability that the optimal prefix-free machine outputs $\sigma$ when its input is produced by tossing a coin is $2^{-K(\sigma)}$, up to a constant factor. A string that is produced with large probability, by whatever mixture of long descriptions, has a short description. The proof is an application of the KC theorem. Its main consequence here is a counting theorem for $K$, which determines the maximal complexity of strings of each length. The lesson ends with Chaitin's halting probability $\Omega$, the measure of the domain of the optimal machine: a real number whose first $n$ bits solve the halting problem for all descriptions of length at most $n$, and which is nevertheless incompressible.

## The coding theorem

For a prefix-free machine $M$, the **output probability** of $\sigma$ is
$$
P_M(\sigma) = \sum_{\tau : M(\tau) = \sigma} 2^{-|\tau|}.
$$
It is the probability that $M$ outputs $\sigma$ when its input is produced by tossing a fair coin, the machine reading bits as needed. By :ref{#prop-kraft}, $\sum_\sigma P_M(\sigma) \leq 1$. Clearly $P_U(\sigma) \geq 2^{-K(\sigma)}$, the contribution of a shortest description. For example, the machine $M$ with $M(1^n 0^{k+1} 1) = 0^n$ for all $n$ and $k$ is prefix-free, and $P_M(0^n) = \sum_k 2^{-n-k-2} = 2^{-n-1}$, while $K_M(0^n) = n + 2$: the output probability of $0^n$ is carried by infinitely many descriptions, the shortest of which accounts for half of it. The coding theorem compares the two quantities in general.

The proof uses the KC theorem to turn probability into short descriptions: each time the approximation of $P_M(\sigma)$ from below exceeds a new power $2^{-k}$, a description of $\sigma$ of length $k + 1$ is requested. The total weight of these requests for $\sigma$ is less than $P_M(\sigma)$, so the request set is bounded because the output probabilities sum to at most $1$.

:::theorem[Coding theorem; Levin, Chaitin]{#thm-coding}
For every prefix-free machine $M$, $K(\sigma) \leq^+ -\log P_M(\sigma)$ for every $\sigma$ with $P_M(\sigma) > 0$. In particular $K(\sigma) =^+ -\log P_U(\sigma)$.
:::

:::proof{of=thm-coding}
Let $P_{M,s}(\sigma)$ be the sum over the descriptions $\tau$ of $\sigma$ such that $|\tau| \leq s$ and $M(\tau)[s]\converge$; it is computable, non-decreasing in $s$, with limit $P_M(\sigma)$. For each $k \geq 1$ and $\sigma$, enumerate the request $(\sigma, k + 1)$ when $P_{M,s}(\sigma) > 2^{-k}$ for the first time. Fix $\sigma$ with $P_M(\sigma) > 0$, and let $k_0$ be the least $k$ with $P_M(\sigma) > 2^{-k}$; then $k_0 \geq 1$, since $P_M(\sigma) \leq 1$. The requests about $\sigma$ are those with $k \geq k_0$, of total weight $\sum_{k \geq k_0} 2^{-k-1} = 2^{-k_0} < P_M(\sigma)$. So the request set is bounded by $\sum_\sigma P_M(\sigma) \leq 1$. By :ref{#thm-kc}, $K(\sigma) \leq^+ k_0 + 1$. By minimality of $k_0$, $P_M(\sigma) \leq 2^{-(k_0 - 1)}$, so $k_0 \leq 1 - \log P_M(\sigma)$, and $K(\sigma) \leq^+ -\log P_M(\sigma)$.
:::

The theorem says that a string that is produced with large probability has a short description. Equivalently, up to a multiplicative constant, the shortest description accounts for the whole output probability of a string: $P_U(\sigma) \leq 2^{c - K(\sigma)}$. In the example above, $K(0^n) \leq^+ n$ is a weak bound; the strength of the theorem appears when the descriptions of a string are not visible individually, as in the next proof, where all descriptions of strings of length $n$ are gathered into descriptions of $n$.

:::quiz[the coding theorem]
In the proof of :ref{#thm-coding}, why is the weight of the requests about $\sigma$ less than $P_M(\sigma)$?

- [x] Because a request $(\sigma, k + 1)$ is issued only when $P_M(\sigma) > 2^{-k}$, once for each such $k$, and the weights $2^{-k-1}$ for $k \geq k_0$ add up to $2^{-k_0} < P_M(\sigma)$.
- [ ] Because $K(\sigma) \leq -\log P_M(\sigma)$.

  This is the conclusion of the theorem, not an ingredient of the weight computation.
- [ ] Because $M$ is prefix-free, so each $\sigma$ has a single description.

  A string may have infinitely many $M$-descriptions; prefix-freeness only bounds the sum of all output probabilities by $1$.
:::

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

$\Omega$ is the probability that $U$ halts when its input is produced by tossing a coin. Its value depends on $U$, as the halting set $\emptyset'$ depends on the enumeration of the machines. By :ref{#prop-kraft}, $\Omega \leq 1$, and $\Omega > 0$ since $U$ has a non-empty domain. The theorem below shows that $\Omega$ is irrational, so $0 < \Omega < 1$ and $\Omega$ has a unique binary expansion $\omega = \omega_0 \omega_1 \cdots$, with $\Omega = \sum_i \omega_i 2^{-i-1}$; we identify $\Omega$ with the sequence $\omega$. The rationals $\Omega_s = \sum \{ 2^{-|\tau|} : |\tau| \leq s,\ U(\tau)[s]\converge \}$ form a computable non-decreasing sequence with limit $\Omega$: $\Omega$ is **left-c.e.**

The binary expansion of $\Omega$ is a compressed form of the domain of $U$. If the first $n$ bits of $\Omega$ are known, wait for a stage $s$ at which $\Omega_s$ exceeds the dyadic rational they define. A description of length at most $n$ that converges after stage $s$ would add at least $2^{-n}$ to $\Omega_s$ and push the sum beyond the dyadic interval of length $2^{-n}$ that contains $\Omega$. So the first $n$ bits of $\Omega$ determine which descriptions of length at most $n$ converge, and this information is enough to produce a string of complexity larger than $n$.

:::figure[Why $n$ bits of $\Omega$ settle the halting of all descriptions of length at most $n$. A description of length at most $n$ converging after the stage $s$ would move the approximation by at least $2^{-n}$, beyond $q + 2^{-n}$, while the limit $\Omega$ lies below $q + 2^{-n}$.]
<svg class="fig" viewBox="0 0 600 190" width="600" role="img" aria-label="On the real line, the dyadic interval from q to q plus 2 to the minus n contains Omega; once Omega_s exceeds q, a program of length at most n converging later would add at least 2 to the minus n and push the sum beyond q plus 2 to the minus n"><defs><marker id="kc-omega-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker><marker id="kc-omega-arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="40" y1="92" x2="560" y2="92" class="axis"/><rect x="150" y="82" width="260" height="20" class="soft-fill"/><line x1="150" y1="78" x2="150" y2="106" class="ink-stroke" stroke-width="1.2"/><text x="150" y="124" text-anchor="middle" class="math" font-size="14">q</text><line x1="410" y1="78" x2="410" y2="106" class="ink-stroke" stroke-width="1.2"/><text x="410" y="124" text-anchor="middle" class="math" font-size="14">q + 2⁻ⁿ</text><circle cx="230" cy="92" r="4" class="ink-fill"/><text x="230" y="72" text-anchor="middle" class="math" font-size="15">Ω<tspan class="mrm" font-size="10" dy="4">s</tspan></text><circle cx="330" cy="92" r="4" class="accent-fill"/><text x="330" y="72" text-anchor="middle" class="math" font-size="15">Ω</text><path d="M230,138 L520,138" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#kc-omega-arrow)"/><text x="375.0" y="156" text-anchor="middle" class="label">adding a new program of length ≤ n: at least 2⁻ⁿ, beyond q + 2⁻ⁿ</text><text x="40" y="24" class="label">q = 0.ω<tspan font-size="9" dy="3">0</tspan><tspan dy="-3">⋯ω</tspan><tspan font-size="9" dy="3">n−1</tspan><tspan dy="-3" dx="4">is read off the first n bits of Ω; the interval [q, q + 2⁻ⁿ) contains Ω.</tspan></text><text x="40" y="42" class="label">At the first stage s with Ω<tspan font-size="9" dy="3">s</tspan><tspan dy="-3"> &gt; q, every program of length ≤ n in the domain has converged.</tspan></text></svg>
:::

:::theorem[Chaitin]{#thm-omega}
1. $\Omega \equiv_T \emptyset'$.
2. $\Omega$ is irrational, and for every $n$, the prefix $\omega \uh n$ determines, uniformly in $n$, the set of strings of length at most $n$ in the domain of $U$.
3. There is a constant $c$ with $K(\omega \uh n) \geq n - c$ for every $n$.
:::

:::proof{of=thm-omega}
*Settled stages.* If $\Omega - \Omega_s < 2^{-n}$ and $s \geq n$, then every string $\tau$ of length at most $n$ in the domain of $U$ satisfies $U(\tau)[s]\converge$: otherwise $\tau$ is not counted in $\Omega_s$, and $\Omega \geq \Omega_s + 2^{-|\tau|} \geq \Omega_s + 2^{-n}$. So the strings of length at most $n$ in the domain of $U$ are those that converge by stage $s$.

*The domain of $U$ computes $\emptyset'$.* The argument is that of :ref{#ex-domain-complete}, adapted to prefix-free machines. Let $M$ be the prefix-free machine with $M(1^e 0) = 0^s$, where $s$ is the least stage with $\Phi_e(e)[s]\converge$, and $M$ undefined elsewhere. Let $d$ be such that $K \leq K_M + d$. If $\Phi_e(e)$ converges at stage $s$, then $K(0^s) \leq e + 1 + d$. With the domain of $U$ as an oracle, compute the outputs of the strings of length at most $e + 1 + d$ in the domain, and let $t$ be the largest number with $0^t$ among them ($t = 0$ if there is none). Then $\Phi_e(e)\converge$ if and only if $\Phi_e(e)[t]\converge$.

*$\Omega$ is irrational.* If $\Omega$ were rational, then, given $n$, the search for a stage $s \geq n$ with $\Omega - \Omega_s < 2^{-n}$ would be effective, since $\Omega$ and $\Omega_s$ are rationals, and it terminates since $\Omega_s$ tends to $\Omega$. By the first paragraph, the domain of $U$ would be computable, and so would be $\emptyset'$, which is not the case.

*Prefixes of $\omega$.* Let $q = 0.\omega_0 \cdots \omega_{n-1}$. Since $\Omega$ is irrational, $q < \Omega < q + 2^{-n}$. Search for $s \geq n$ with $\Omega_s > q$; it exists, and then $\Omega - \Omega_s < 2^{-n}$, so $s$ is settled for $n$. This procedure only uses $\omega \uh n$, which proves 2. In particular $\omega$ computes the domain of $U$, hence $\emptyset'$.

*$\omega \leq_T \emptyset'$.* For a dyadic rational $q$, $q < \Omega$ holds if and only if $\Omega_s > q$ for some $s$, a c.e. condition, so $\emptyset'$ decides it; and $q \neq \Omega$, since $\Omega$ is irrational. The prefix $\omega \uh k$ is the binary expansion of the largest $q = j 2^{-k}$ with $q < \Omega$, so $\emptyset'$ computes $\omega$. This proves 1.

*Incompressibility.* Let $N$ be the machine that, on input $\tau$, computes $\rho = U(\tau)$ and $n = |\rho|$, runs the procedure of 2 as if $\rho$ were $\omega \uh n$, obtaining a stage $s$ if the search terminates, lists the outputs of the strings of length at most $n$ that converge by stage $s$, and outputs the first string, in the length-lexicographic order, that is not in this list. The domain of $N$ is contained in that of $U$, so $N$ is prefix-free. If $U(\tau) = \omega \uh n$, the list contains every string $\sigma$ with $K(\sigma) \leq n$, by 2, so $N(\tau)$ has complexity larger than $n$. Let $c$ be such that $K \leq K_N + c$, and let $\tau$ be a shortest description of $\omega \uh n$. Then $n < K(N(\tau)) \leq |\tau| + c = K(\omega \uh n) + c$.
:::

Statement 3 says that $\omega$ is random in the sense announced in the lesson on prefix-free complexity, and hence, by the next course, Martin-Löf random. The first $n$ bits of $\Omega$ solve the halting problem for all programs of length at most $n$, and yet they cannot be compressed: up to a constant, no prefix-free description of them is shorter than $n$.

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
Show that there is a constant $c$ such that, for all $n$ and $b$, fewer than $2^{b + c}$ strings $\sigma$ of length $n$ satisfy $K(\sigma) < K(n) + b$. Compare with :ref{#lem-few-segments}.

:::solution
Apply :ref{#thm-k-counting} with $k = n - b$: fewer than $2^{n - (n - b) + c} = 2^{b + c}$ strings of length $n$ satisfy $K(\sigma) < n + K(n) - (n - b) = K(n) + b$. (If $k$ is negative, the statement of the counting theorem still holds, with the same proof.) The bound is exponential in $b$, like the bound $(d + 1)^2 2^{d + c}$ of :ref{#lem-few-segments} for plain complexity, and it is used to show that the sets with $K(X \uh n) \leq^+ K(n)$ are computable in $\emptyset'$.
:::
::::

## Notes and references

The coding theorem is due to Levin (1974) and Chaitin (1975), and in a sense to Solomonoff; Downey and Hirschfeldt (Section 3.9) state it with Levin's maximal c.e. discrete semimeasure, and Nies (Theorem 2.2.25) derives it from the characterization of $K$; the proof given here applies the KC theorem directly. The counting theorem is due to Chaitin (1975) (Downey–Hirschfeldt, Theorem 3.7.6; Nies, Theorem 2.2.26). Chaitin (1975) introduced $\Omega$ and proved its randomness (Downey–Hirschfeldt, Theorem 6.1.3). Calude, Hertling, Khoussainov and Wang (1998), after Solovay, and Kučera and Slaman (2001) showed that the left-c.e. reals that are random in the sense of the next course are exactly the halting probabilities of optimal prefix-free machines (Downey–Hirschfeldt, Section 9.2).

- L. A. Levin, *Laws of information conservation (nongrowth) and aspects of the foundation of probability theory*, Problems of Information Transmission 10 (1974), 206–210.
- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- C. P. Schnorr, *Process complexity and effective random tests*, Journal of Computer and System Sciences 7 (1973), 376–388.
- C. S. Calude, P. H. Hertling, B. Khoussainov and Y. Wang, *Recursively enumerable reals and Chaitin Ω numbers*, STACS 98, Lecture Notes in Computer Science 1373, Springer, 1998, 596–606.
- A. Kučera and T. A. Slaman, *Randomness and recursive enumerability*, SIAM Journal on Computing 31 (2001), 199–211.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.7, 3.9, 3.13 and 6.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 2.2.
