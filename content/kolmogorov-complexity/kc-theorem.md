---
title: The KC theorem
summary: Prefix-free machines can be built from c.e. sets of requests of total weight at most 1; K is the least right-c.e. function satisfying the Kraft inequality.
duration: 35
prerequisites: [prefix-free-complexity]
---

Constructing a prefix-free machine by hand requires keeping its domain prefix-free, which is often tedious. The **KC theorem**, an effective form of the converse of the Kraft inequality, removes this difficulty: to obtain descriptions of prescribed lengths, it suffices to enumerate requests whose total weight is at most $1$. Most constructions involving $K$ in the theory of algorithmic randomness are written in this form. The theorem yields a characterization of $K$ as the least function, up to a constant, that is approximable from above and satisfies the Kraft inequality; the next lesson derives the coding theorem from it.

## Bounded request sets

:::definition{#def-request-set}
A **request** is a pair $(\sigma, \ell) \in \bstr \times \nat$, asking for a description of $\sigma$ of length $\ell$. A set of requests $R$ is **bounded** if its **weight** $\sum_{(\sigma, \ell) \in R} 2^{-\ell}$ is at most $1$. A prefix-free machine $M$ **satisfies** $R$ if for every request $(\sigma, \ell) \in R$ there is a string $\tau$ of length $\ell$ with $M(\tau) = \sigma$, these strings $\tau$ being distinct for distinct requests.
:::

For example, for a computable sequence $X$, the set $\{ (X \uh n, n + 1) : n \in \nat \}$ is a bounded c.e. request set of weight $\sum_n 2^{-n-1} = 1$. The requests $(\sigma, 2|\sigma| + 1)$, for all strings $\sigma$, form a bounded request set of weight $\sum_n 2^n 2^{-2n-1} = 1$. The requests $(\sigma, |\sigma|)$ do not: their weight is $\sum_n 2^n 2^{-n} = \infty$, in accordance with :ref{#cor-k-above-length}.

The offline construction of Kraft, which places the intervals from left to right in order of decreasing size, is not available when the requests are enumerated one at a time in an unknown order. A naive online strategy fails: if the requests of lengths $3, 3, 1$ arrive in this order and the first two receive $000$ and $100$, then no free interval of length $\tfrac12$ remains, although the total weight is $\tfrac34$. The proof below keeps the unused part of $[0, 1]$ as a union of dyadic intervals of pairwise distinct lengths, like the binary expansion of the remaining weight, so that a request of weight at most the remaining weight can always be served.

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

A request is served by the smallest free interval that is large enough, which is split as needed: its left part of the requested size is assigned, and the rest becomes free intervals of the sizes in between.

:::figure[The KC construction on the requests of lengths $2, 3, 1, 3$, of total weight $1$. Each row shows $[0, 1]$ after a request: the shaded intervals are the free strings, of pairwise distinct lengths, and the others are assigned. The second request, of length $3$, is served inside $01$, the longest free string of length at most $3$, rather than inside $1$, which remains available for the third request, of length $1$.]
<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="Five rows show the unit interval before and after each of four requests of lengths 2, 3, 1 and 3; assigned intervals are filled, free intervals are shaded and have pairwise distinct lengths"><text x="10" y="30" class="label">start</text><rect x="150.0" y="14" width="430.0" height="26" class="cell head-cell"/><text x="365.0" y="31" text-anchor="middle" class="mrm" font-size="12">ε</text><text x="10" y="72" class="label">request 1: length 2</text><text x="10" y="88" class="label">ρ = ε, τ = 00</text><rect x="257.5" y="62" width="107.5" height="26" class="cell head-cell"/><text x="311.2" y="79" text-anchor="middle" class="mrm" font-size="12">01</text><rect x="365.0" y="62" width="215.0" height="26" class="cell head-cell"/><text x="472.5" y="79" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="150.0" y="62" width="107.5" height="26" class="cell"/><text x="203.8" y="79" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">0</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 00</tspan></text><text x="10" y="120" class="label">request 2: length 3</text><text x="10" y="136" class="label">ρ = 01, τ = 010</text><rect x="311.2" y="110" width="53.8" height="26" class="cell head-cell"/><text x="338.1" y="127" text-anchor="middle" class="mrm" font-size="12">011</text><rect x="365.0" y="110" width="215.0" height="26" class="cell head-cell"/><text x="472.5" y="127" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="150.0" y="110" width="107.5" height="26" class="cell"/><text x="203.8" y="127" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">0</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 00</tspan></text><rect x="257.5" y="110" width="53.8" height="26" class="cell"/><text x="284.4" y="127" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 010</tspan></text><text x="10" y="168" class="label">request 3: length 1</text><text x="10" y="184" class="label">ρ = 1, τ = 1</text><rect x="311.2" y="158" width="53.8" height="26" class="cell head-cell"/><text x="338.1" y="175" text-anchor="middle" class="mrm" font-size="12">011</text><rect x="150.0" y="158" width="107.5" height="26" class="cell"/><text x="203.8" y="175" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">0</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 00</tspan></text><rect x="257.5" y="158" width="53.8" height="26" class="cell"/><text x="284.4" y="175" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 010</tspan></text><rect x="365.0" y="158" width="215.0" height="26" class="cell"/><text x="472.5" y="175" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">2</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 1</tspan></text><text x="10" y="216" class="label">request 4: length 3</text><text x="10" y="232" class="label">ρ = 011, τ = 011</text><rect x="150.0" y="206" width="107.5" height="26" class="cell"/><text x="203.8" y="223" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">0</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 00</tspan></text><rect x="257.5" y="206" width="53.8" height="26" class="cell"/><text x="284.4" y="223" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">1</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 010</tspan></text><rect x="365.0" y="206" width="215.0" height="26" class="cell"/><text x="472.5" y="223" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">2</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 1</tspan></text><rect x="311.2" y="206" width="53.8" height="26" class="cell"/><text x="338.1" y="223" text-anchor="middle" class="math" font-size="13">τ<tspan class="mrm" font-size="9" dy="3">3</tspan><tspan class="mrm" font-size="11" dy="-3" dx="3">= 011</tspan></text><rect x="150" y="248" width="14" height="12" class="cell head-cell"/><text x="170" y="258" class="label">free string</text><rect x="270" y="248" width="14" height="12" class="cell"/><text x="290" y="258" class="label">assigned to a request</text></svg>
:::

:::quiz[the KC theorem]
In the proof of :ref{#thm-kc}, why is the **longest** free string of length at most $\ell_s$ chosen?

- [x] To preserve invariant 2: the new free strings have the lengths between $|\rho| + 1$ and $\ell_s$, and no other free string has such a length precisely because $\rho$ is the longest free string of length at most $\ell_s$.
- [ ] To make the machine prefix-free.

  Any free string of length at most $\ell_s$ would keep the domain prefix-free; the choice matters for invariant 2.
- [ ] Because shorter free strings may not exist.

  A free string of length at most $\ell_s$ exists by the weight argument; there may be several.

---

Where is the boundedness of $R$ used?

- [x] To show that at every stage some free string has length at most $\ell_s$: the remaining weight, which by invariant 3 is the weight of the free strings, is at least $2^{-\ell_s}$.
- [ ] To show that the domain of $M$ is prefix-free.

  Prefix-freeness follows from the invariants for any requests that can be served; boundedness guarantees that every request can be served.
- [ ] To show that $M$ is computable.

  The construction is effective whatever the weights; without boundedness it may get stuck.
:::

## The characterization of K

A function $f : \bstr \to \nat$ is **approximable from above**, or **right-c.e.**, if there is a computable function $(s, \sigma) \mapsto f_s(\sigma)$, non-increasing in $s$, with $\lim_s f_s(\sigma) = f(\sigma)$. As noted after :ref{#thm-optimal-prefix-free}, $K$ is right-c.e., and by :ref{#prop-k-basic} (4) it satisfies $\sum_\sigma 2^{-K(\sigma)} \leq 1$. The converse is the following theorem: every function with these two properties is an upper bound for $K$. The idea is to request a description of $\sigma$ of length $f_s(\sigma) + 1$ each time the approximation decreases; the requests about $\sigma$ have distinct lengths, so their weight is at most twice the weight of the last one.

:::theorem{#thm-k-minimal}
If $f : \bstr \to \nat$ is right-c.e. and $\sum_\sigma 2^{-f(\sigma)} \leq 1$, then $K \leq^+ f$. So $K$ is, up to an additive constant, the least right-c.e. function satisfying the Kraft inequality.
:::

:::proof{of=thm-k-minimal}
Let $(f_s)$ be an approximation from above. Enumerate the request $(\sigma, f_0(\sigma) + 1)$ for each $\sigma$, and the request $(\sigma, f_{s+1}(\sigma) + 1)$ whenever $f_{s+1}(\sigma) < f_s(\sigma)$. The requests concerning $\sigma$ have pairwise distinct lengths $v + 1$, with $v$ ranging over the values taken by $f_s(\sigma)$, which are at least $f(\sigma)$. Their weight is at most $\sum_{v \geq f(\sigma)} 2^{-v-1} = 2^{-f(\sigma)}$. The total weight is at most $\sum_\sigma 2^{-f(\sigma)} \leq 1$. By :ref{#thm-kc}, $K(\sigma) \leq^+ f(\sigma) + 1$, since the request $(\sigma, f(\sigma) + 1)$ is enumerated when the approximation reaches its limit.
:::

For example, the function $f(\sigma) = |\sigma| + K(|\sigma|)$ is right-c.e., and $\sum_\sigma 2^{-|\sigma| - K(|\sigma|)} = \sum_n 2^n\, 2^{-n - K(n)} = \sum_n 2^{-K(n)} \leq 1$. The theorem gives again $K(\sigma) \leq^+ |\sigma| + K(|\sigma|)$, without building a machine. This argument is due to Chaitin.

:::quiz[the characterization of K]
In the proof of :ref{#thm-k-minimal}, why are requests issued with length $f_s(\sigma) + 1$ rather than $f_s(\sigma)$?

- [x] Because $\sigma$ receives one request for each value of the approximation, and the factor $\tfrac12$ makes the total weight of these requests at most $2^{-f(\sigma)}$.
- [ ] Because $f_s(\sigma)$ may be $0$.

  A request of length $0$ is allowed; it has weight $1$.
- [ ] To make $f + 1$ right-c.e.

  $f + 1$ is right-c.e. whenever $f$ is.
:::

## Exercises

::::exercise{difficulty=1}
Let $f : \nat \to \nat$ be computable with $\sum_n 2^{-f(n)} < \infty$. Show that $K(n) \leq^+ f(n)$. Deduce that $K(n) \leq^+ \log n + 2 \log \log n$ for $n \geq 4$, and show that $K(n) > \log n + \log \log n$ for infinitely many $n$.

:::solution
Let $c$ be such that $\sum_n 2^{-f(n) - c} \leq 1$. The computable function $f + c$ is right-c.e. and satisfies the Kraft inequality, so $K \leq^+ f + c$ by :ref{#thm-k-minimal}. The series $\sum_{n \geq 4} 1/(n (\log n)^2)$ converges, which gives the second bound with $f(n) = \lceil \log n + 2 \log \log n \rceil$ for $n \geq 4$ (and $f(n) = 0$ for $n < 4$). If $K(n) \leq \log n + \log \log n$ for all $n \geq n_0$, then $\sum_n 2^{-K(n)} \geq \sum_{n \geq n_0} 1/(n \log n)$, which diverges, contradicting :ref{#prop-k-basic} (4).
:::
::::

::::exercise{difficulty=2}
Let $d$ be a number and $R$ a c.e. set of requests of weight at most $2^d$. Show that $K(\sigma) \leq^+ \ell + d$ for every $(\sigma, \ell) \in R$. Deduce from :ref{#thm-kc} that if $(R_d)_{d \in \nat}$ is a uniformly c.e. sequence of request sets with weights at most $2^{-d}$, then $K(\sigma) \leq^+ \ell$ for every $d$ and every $(\sigma, \ell) \in R_d$.

:::solution
The set $\{ (\sigma, \ell + d) : (\sigma, \ell) \in R \}$ has weight at most $1$, and :ref{#thm-kc} applies. For the second statement, let $R$ be the union of the sets $R_d$ for $d \geq 1$; it is c.e., and its weight is at most $\sum_{d \geq 1} 2^{-d} = 1$, so a single application of :ref{#thm-kc} gives the bound for $d \geq 1$, with one constant. The set $R_0$, of weight at most $1$, is handled by a second application.
:::
::::

## Notes and references

The KC theorem appears in Levin's dissertation (1971) and in Schnorr (1973, Lemma 1), and was given its usual form, for prefix-free complexity, by Chaitin (1975), who credits the key idea to Pippenger; the name stands for Kraft and Chaitin, or "Kraft's inequality, computable version" (Downey–Hirschfeldt, Section 3.6). Nies calls it the machine existence theorem, and his proof (Theorem 2.2.17) is the one given here. The characterization of $K$ is in Nies, Theorem 2.2.19, and in Downey and Hirschfeldt, Theorem 3.7.8, as the minimality of $K$ among Chaitin's information content measures.

- L. A. Levin, *Some theorems on the algorithmic approach to probability theory and information theory*, Dissertation, Moscow University, 1971 (in Russian).
- C. P. Schnorr, *Process complexity and effective random tests*, Journal of Computer and System Sciences 7 (1973), 376–388.
- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- L. G. Kraft, *A device for quantizing, grouping, and coding amplitude modulated pulses*, Master's thesis, MIT, 1949.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 2.2.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.6 and 3.7.
