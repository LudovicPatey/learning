---
title: Ville's theorem and the savings trick
summary: The success set of a supermartingale is null, and every null class is contained in the success set of a martingale (Ville); von Mises's selection rules and Ville's critique; the savings trick turns success into convergence of the capital to infinity.
duration: 35
prerequisites: [betting-strategies]
---

Kolmogorov's inequality says that a strategy rarely wins much. This lesson draws its two consequences. The first is Ville's theorem: the classes on which a single martingale succeeds are exactly the null classes, so that betting strategies and covers of small measure are two descriptions of the same objects; the effective versions of this dictionary, in the next lessons, give the equivalence of the martingale and measure-theoretic definitions of randomness. The second is the savings trick: success, which only requires an unbounded capital, can always be turned into a capital that tends to infinity.

## Success sets and null classes

:::proposition{#prop-success-null}
The success set of every supermartingale is null.
:::

:::proof{of=prop-success-null}
Let $d$ be a supermartingale. If $d(\varepsilon) = 0$, then $d = 0$ by :ref{#lem-martingale-basic} (1), and $S[d]$ is empty. Otherwise, for every $k$, $S[d]$ is contained in $\{ X : \exists n\ d(X \uh n) \geq 2^k d(\varepsilon) \}$, of measure at most $2^{-k}$ by :ref{#lem-kolmogorov-inequality} (2). So $\lambda(S[d]) \leq 2^{-k}$ for every $k$.
:::

The converse is the main result of this lesson. A null class is covered by open classes of measure at most $2^{-n}$; the martingale $d_{\mathcal U}$ of :ref{#ex-martingales} turns an open class $\mathcal U$ into a strategy with initial capital $\lambda(\mathcal U)$, whose capital is $1$ once the sequence is known to be in $\mathcal U$. Summing these strategies over the covers gives a capital that grows by $1$ each time the sequence is seen to enter one more cover.

:::theorem[Ville]{#thm-ville}
For a Borel class $\mathcal N \subseteq \cs$, the following are equivalent.

1. $\mathcal N$ is null.
2. $\mathcal N \subseteq S[d]$ for some martingale $d$.
3. $\mathcal N \subseteq S[d]$ for some supermartingale $d$.

Moreover, in (2) one can take $d(\varepsilon) \leq 1$ and $\lim_n d(X \uh n) = \infty$ for every $X \in \mathcal N$.
:::

:::proof{of=thm-ville}
(2) ⇒ (3) is immediate, and (3) ⇒ (1) is :ref{#prop-success-null}. For (1) ⇒ (2), let $\mathcal N$ be null. By outer regularity (:ref{#fact-lebesgue-measure}), for each $n$ there is an open class $\mathcal U_n \supseteq \mathcal N$ with $\lambda(\mathcal U_n) \leq 2^{-n-1}$. Let $d = \sum_n d_{\mathcal U_n}$. Since $\sum_n d_{\mathcal U_n}(\varepsilon) = \sum_n \lambda(\mathcal U_n) \leq 1$, $d$ is a martingale with $d(\varepsilon) \leq 1$, by :ref{#lem-martingale-basic} (2).

Let $X \in \mathcal N$. For each $n$, $X$ belongs to the open class $\mathcal U_n$, so there is $m_n$ with $[X \uh m_n] \subseteq \mathcal U_n$; then $d_{\mathcal U_n}(X \uh m) = 1$ for every $m \geq m_n$. Hence $d(X \uh m) \geq |\{ n : m_n \leq m \}|$, and the right-hand side tends to infinity with $m$.
:::

The proof is a dictionary between covers and strategies: a cover of measure $2^{-n}$ is a strategy with initial capital $2^{-n}$, and Kolmogorov's inequality turns a strategy back into covers, the classes where the capital exceeds $2^n$. The next lessons make both directions effective. The supermartingale version of the theorem is not more general, by :ref{#lem-martingale-basic} (3).

:::quiz[Ville's theorem]
In the proof of (1) ⇒ (2) in :ref{#thm-ville}, why are the covers $\mathcal U_n$ required to be open?

- [x] So that a sequence of $\mathcal U_n$ has a prefix whose whole cylinder lies in $\mathcal U_n$, after which $d_{\mathcal U_n}$ stays equal to $1$ along the sequence.
- [ ] Because $d_{\mathcal C}$ is a martingale only when $\mathcal C$ is open.

  $d_{\mathcal C}$ is a martingale for every Borel class $\mathcal C$, by additivity.
- [ ] To make the measures $\lambda(\mathcal U_n)$ summable.

  The bound $2^{-n-1}$ gives summability; openness gives the capital along the members of $\mathcal N$.

---

Why does the martingale of the proof satisfy $\lim_m d(X \uh m) = \infty$, and not only $\sup_m d(X \uh m) = \infty$?

- [x] Because each cover contributes a capital $1$ that is never lost once the sequence has entered it, so the capital is bounded below by a non-decreasing unbounded count.
- [ ] Because every martingale that succeeds on $X$ has a limit along $X$.

  The capital of a martingale may oscillate: the definition of success only asks for unboundedness. The savings trick, at the end of this lesson, removes such oscillations.
- [ ] Because $d(\varepsilon) \leq 1$.

  The initial capital plays no role in the behavior along $X$.
:::

Martingales were introduced by Ville in a critique of von Mises's definition of random sequences. Von Mises called a sequence random if the frequency of ones tends to $\frac12$ along every subsequence chosen by an admissible selection rule, a rule that decides whether to select the next bit by looking at the bits seen so far. Ville showed that for every countable family of selection rules there is a sequence that satisfies this condition for all of them and yet has, in every prefix, at least as many zeros as ones. The class of such sequences is null (the simple random walk crosses above $0$ almost surely, a classical fact admitted here), so by :ref{#thm-ville} a single martingale succeeds on all of them: betting strategies detect regularities that selection rules miss. Ville's construction is presented by Downey and Hirschfeldt (Theorem 6.5.1).

## The savings trick

Success only requires the capital to be unbounded: the gambler may come close to ruin after each of her successes. :ref{#fig-savings} shows such a strategy, whose capital reaches $2^k$ for every $k$ but falls back to $\frac14$ each time. A cautious gambler puts aside part of her gains: each time her capital passes a new power of $2$, she stops betting with part of it. The construction below runs one copy of $d$ for each threshold $2^k$; the $k$-th copy stops betting forever once the capital of $d$ has exceeded $2^k$.

:::proposition[savings trick]{#prop-savings}
For every (super)martingale $d$ there is a (super)martingale $d^+$ with $d^+(\varepsilon) = 2 d(\varepsilon)$ such that:

1. $S[d^+] = S[d]$, and $\lim_n d^+(X \uh n) = \infty$ for every $X \in S[d]$;
2. $d^+(\sigma\tau) \geq d^+(\sigma) - 2$ for all strings $\sigma$ and $\tau$ (the **savings property**).

If $d$ is computable with rational values computable from $\sigma$, so is $d^+$, uniformly in $d$.
:::

:::proof{of=prop-savings}
For each $k$ and each string $\sigma$, let $\sigma_k$ be the shortest prefix $\rho$ of $\sigma$ with $d(\rho) > 2^k$, if there is one, and $\sigma_k = \sigma$ otherwise. Let $d_k(\sigma) = d(\sigma_k)$: the $k$-th copy follows $d$ until its capital exceeds $2^k$, and stops betting from then on. Each $d_k$ is a (super)martingale with $d_k(\varepsilon) = d(\varepsilon)$: if some prefix of $\sigma$ has value above $2^k$, then $d_k(\sigma 0) = d_k(\sigma 1) = d_k(\sigma)$; otherwise $d_k(\sigma i) = d(\sigma i)$ for both $i$, and $d_k(\sigma) = d(\sigma)$. Let $d^+ = \sum_k 2^{-k} d_k$, a (super)martingale with $d^+(\varepsilon) = 2 d(\varepsilon)$ by :ref{#lem-martingale-basic} (2).

Fix $\sigma$, let $M = \max_{\rho \preceq \sigma} d(\rho)$, and let $m$ be the least $k$ with $M \leq 2^k$. For $k < m$, some prefix of $\sigma$ has value above $2^k$, so $d_k$ has stopped betting: $d_k(\sigma\tau) = d_k(\sigma)$ for every $\tau$. For $k \geq m$, $d_k(\sigma) = d(\sigma) \leq 2^m$. Hence
$$
d^+(\sigma) = \sum_{k < m} 2^{-k} d_k(\sigma) + 2^{1-m} d(\sigma) \leq \sum_{k < m} 2^{-k} d_k(\sigma\tau) + 2 \leq d^+(\sigma\tau) + 2,
$$
which is (2). If $X \in S[d]$, then for every $k$ there is $n_k$ with $d(X \uh n_k) > 2^k$, and $2^{-k} d_k(X \uh n) > 1$ for every $n \geq n_k$; so $d^+(X \uh n) \geq |\{ k : n_k \leq n \}|$, which tends to infinity. If $X \notin S[d]$, let $2^j$ bound $d$ along $X$; the formula above, applied to $\sigma = X \uh n$, shows that $d^+(X \uh n) \leq 2 \cdot 2^j + 2$, since every value $d_k(X \uh n)$ is a value of $d$ on a prefix of $X$. So $S[d^+] = S[d]$.

If the values of $d$ are rationals computable from $\sigma$, then $M$, $m$ and the values $d_k(\sigma)$ for $k < m$ are computable from $\sigma$, and so is $d^+(\sigma)$ by the displayed formula.
:::

:::figure[The savings trick along one sequence $X$. The capital of $d$ (black) doubles up to $4$, $8$, $16$ and $32$, and falls back to $\frac14$ after each peak; $d$ succeeds on $X$ without converging. The capital of $d^+$ (accent), computed exactly by the formula of the proof, never falls by more than $2$ and increases by about $2$ after each new peak.]{#fig-savings}
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Capital of a martingale along one sequence, with higher and higher peaks followed by falls to one quarter, and the capital of the savings martingale, which never falls by more than 2 and tends to infinity"><line x1="50" y1="210" x2="578" y2="210" class="axis"/><line x1="50" y1="210" x2="50" y2="14" class="axis"/><text x="42.0" y="214.0" text-anchor="end" class="mrm" font-size="11">0</text><text x="42.0" y="166.5" text-anchor="end" class="mrm" font-size="11">8</text><line x1="50" y1="162.5" x2="570" y2="162.5" class="muted-stroke" stroke-width="0.5" stroke-dasharray="2 4"/><text x="42.0" y="119.0" text-anchor="end" class="mrm" font-size="11">16</text><line x1="50" y1="115.0" x2="570" y2="115.0" class="muted-stroke" stroke-width="0.5" stroke-dasharray="2 4"/><text x="42.0" y="71.5" text-anchor="end" class="mrm" font-size="11">24</text><line x1="50" y1="67.5" x2="570" y2="67.5" class="muted-stroke" stroke-width="0.5" stroke-dasharray="2 4"/><text x="42.0" y="24.0" text-anchor="end" class="mrm" font-size="11">32</text><line x1="50" y1="20.0" x2="570" y2="20.0" class="muted-stroke" stroke-width="0.5" stroke-dasharray="2 4"/><text x="582.0" y="214.0" text-anchor="start" class="math" font-size="14">n</text><polyline points="50.0,204.1 62.4,198.1 74.8,186.2 87.1,198.1 99.5,204.1 111.9,207.0 124.3,208.5 136.7,207.0 149.0,204.1 161.4,198.1 173.8,186.2 186.2,162.5 198.6,186.2 211.0,198.1 223.3,204.1 235.7,207.0 248.1,208.5 260.5,207.0 272.9,204.1 285.2,198.1 297.6,186.2 310.0,162.5 322.4,115.0 334.8,162.5 347.1,186.2 359.5,198.1 371.9,204.1 384.3,207.0 396.7,208.5 409.0,207.0 421.4,204.1 433.8,198.1 446.2,186.2 458.6,162.5 471.0,115.0 483.3,20.0 495.7,115.0 508.1,162.5 520.5,186.2 532.9,198.1 545.2,204.1 557.6,207.0 570.0,208.5" class="ink-stroke" stroke-width="1.3"/><polyline points="50.0,198.1 62.4,186.2 74.8,174.4 87.1,180.3 99.5,183.3 111.9,184.8 124.3,185.5 136.7,184.8 149.0,183.3 161.4,180.3 173.8,174.4 186.2,162.5 198.6,168.4 211.0,171.4 223.3,172.9 235.7,173.6 248.1,174.0 260.5,173.6 272.9,172.9 285.2,171.4 297.6,168.4 310.0,162.5 322.4,150.6 334.8,156.6 347.1,159.5 359.5,161.0 371.9,161.8 384.3,162.1 396.7,162.3 409.0,162.1 421.4,161.8 433.8,161.0 446.2,159.5 458.6,156.6 471.0,150.6 483.3,138.8 495.7,144.7 508.1,147.7 520.5,149.1 532.9,149.9 545.2,150.3 557.6,150.4 570.0,150.5" class="accent-stroke" stroke-width="2"/><line x1="150" y1="236" x2="172" y2="236" class="ink-stroke" stroke-width="1.3"/><text x="178.0" y="240.0" text-anchor="start" class="math" font-size="13">d</text><text x="188" y="240" class="label">(X↾n)</text><line x1="330" y1="236" x2="352" y2="236" class="accent-stroke" stroke-width="2"/><text x="358" y="240" class="math" font-size="13">d<tspan class="mrm" font-size="10" dy="-6">+</tspan></text><text x="374" y="240" class="label">(X↾n), with savings</text></svg>
:::

:::quiz[the savings trick]
In the proof of :ref{#prop-savings}, why does the savings property hold with the constant $2$, whatever the capital of $d$?

- [x] Because the copies $d_k$ with $k < m$ have stopped betting and keep their value, and the copies still betting have weights $2^{-k}$, $k \geq m$, and capital at most $2^m$, so together they hold at most $2$.
- [ ] Because $d(\sigma\tau) \geq d(\sigma) - 2$.

  The original $d$ has no such property: in :ref{#fig-savings} it falls from $32$ to $\frac14$.
- [ ] Because $d^+(\varepsilon) = 2 d(\varepsilon)$.

  The initial capital is unrelated to the losses along a sequence.

---

Why is $S[d^+] \subseteq S[d]$?

- [x] Along a sequence where $d$ is bounded by $2^m$, every copy $d_k$ takes values of $d$ on prefixes, so $d^+$ is bounded by $2^{m+1} + 2$.
- [ ] Because $d^+ \leq d$.

  At the root, $d^+(\varepsilon) = 2 d(\varepsilon)$, and stopped copies can exceed the current value of $d$.
- [ ] Because $d^+$ is a supermartingale.

  Supermartingales can succeed on sequences on which a given $d$ does not.
:::

## Exercises

::::exercise{difficulty=1}
Let $d_0, d_1, \dots$ be martingales with $d_n(\varepsilon) > 0$. Show directly, without :ref{#thm-ville}, that there is a single martingale that succeeds on every sequence on which some $d_n$ succeeds.

:::solution
Let $d = \sum_n 2^{-n} d_n / d_n(\varepsilon)$. Its initial capital is $\sum_n 2^{-n} = 2$, so it is a martingale by :ref{#lem-martingale-basic} (2). It is above each $2^{-n} d_n / d_n(\varepsilon)$, so it succeeds wherever some $d_n$ does.
:::
::::

::::exercise{difficulty=1}
Let $d$ be a martingale with the savings property: $d(\sigma\tau) \geq d(\sigma) - 2$ for all strings $\sigma$ and $\tau$. Show that $d$ succeeds on $X$ if and only if $\lim_n d(X \uh n) = \infty$.

:::solution
If $\sup_n d(X \uh n) = \infty$ and $b$ is a real, choose $n_0$ with $d(X \uh n_0) \geq b + 2$. For every $n \geq n_0$, $d(X \uh n) \geq d(X \uh n_0) - 2 \geq b$. The converse is clear.
:::
::::


## Notes and references

Ville (1939) proved that the success sets of martingales are exactly the null classes, in his critique of von Mises (1919); Wald (1936, 1937) showed that for every countable family of selection rules there are sequences satisfying von Mises's definition, and Church (1940) proposed to use the computable rules. Downey and Hirschfeldt describe this history at the beginning of Section 6.2 and prove Ville's theorem on selection rules in Section 6.5 (Theorem 6.5.1, after Lieb, Osherson and Weinstein); they state the characterization of null classes after Definition 6.3.1. Nies proves it as Proposition 7.1.15, from which the proof of :ref{#thm-ville} is taken. The savings trick is folklore (Downey–Hirschfeldt, Proposition 6.3.8; Nies, Exercise 7.1.14); the construction given here, with one copy of $d$ for each threshold $2^k$, is the one used by Franklin and Stephan (2010) for computable martingales (Downey–Hirschfeldt, Theorem 7.1.8).

- J. Ville, *Étude critique de la notion de collectif*, Gauthier-Villars, Paris, 1939.
- R. von Mises, *Grundlagen der Wahrscheinlichkeitsrechnung*, Mathematische Zeitschrift 5 (1919), 52–99.
- A. Church, *On the concept of a random sequence*, Bulletin of the American Mathematical Society 46 (1940), 130–135.
- J. N. Y. Franklin and F. Stephan, *Schnorr trivial sets and truth-table reducibility*, Journal of Symbolic Logic 75 (2010), 501–521.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 6.2, 6.3, 6.5 and 7.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 7.1.
