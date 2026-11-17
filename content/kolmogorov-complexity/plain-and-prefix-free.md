---
title: Plain and prefix-free complexity compared
summary: Levin's theorem that plain complexity is prefix-free complexity given the length of the description; Solovay's theorem that strongly K-random strings are C-random; Solovay's bound on the number of descriptions of each length and the estimate of C in terms of K.
duration: 30
prerequisites: [prefix-free-symmetry]
---

The two complexities of the course differ by at most a logarithmic term: $C \leq^+ K \leq^+ C + K(C)$ (:ref{#prop-k-basic}). This lesson makes the relation precise in three ways. Levin's theorem identifies the difference exactly: plain complexity is prefix-free complexity **given the length of the description**, $C(\sigma) =^+ K(\sigma \mid C(\sigma))$. A plain description does not need to say where it ends, because its length is known to the machine; giving this length as a condition to a prefix-free machine closes the gap. Solovay's theorem compares the two notions of randomness for strings: a string of maximal prefix-free complexity, $K(\sigma) \geq |\sigma| + K(|\sigma|) - d$, is also of maximal plain complexity. Finally, a counting lemma of Solovay on the domain of the optimal prefix-free machine, proved with the KC theorem, bounds $C$ from above by $K - K(K) + K(K(K))$.

Throughout, $U$ is the optimal prefix-free machine, $V$ an optimal plain machine defining $C$, and $U_{\mathrm c}$ the optimal conditional prefix-free machine defining $K(\sigma \mid \tau)$. We write $K^{(2)}(\sigma) = K(K(\sigma))$ and $K^{(3)}(\sigma) = K(K(K(\sigma)))$.

## Levin's theorem

:::theorem[Levin]{#thm-levin-c-k}
$C(\sigma) =^+ K(\sigma \mid C(\sigma))$.
:::

The inequality $K(\sigma \mid C(\sigma)) \leq^+ C(\sigma)$ holds because, once the length $n$ of the description is known, the descriptions of length $n$ form a prefix-free set. For the converse, a description of $\sigma$ given $n = C(\sigma)$ of length $k$ becomes a plain description of $\sigma$ if $n$ can be recovered; it suffices to add the difference $n - k$, at a logarithmic cost. If $k$ were much smaller than $n$, this would give a plain description shorter than $C(\sigma)$.

:::proof{of=thm-levin-c-k}
Let $n = C(\sigma)$.

*Upper bound.* Let $M$ be the conditional machine with $M(\tau, m) = V(\tau)$ when $|\tau| = m$, and undefined otherwise. For each condition $m$, its domain is a set of strings of length $m$, which is prefix-free. A shortest $V$-description of $\sigma$ is an $M$-description of $\sigma$ given $n$, of length $n$. So $K(\sigma \mid n) \leq n + c$ for a constant $c$.

*Lower bound.* Let $k = K(\sigma \mid n)$ and $j = n - k$; if $j \leq 0$, there is nothing to prove. Otherwise, let $N$ be the plain machine that, on an input $\bar\alpha\, 01\, \mu$, where $\alpha$ is the string of a number $j$ and $\bar\alpha$ is $\alpha$ with its bits doubled, computes $m = |\mu| + j$ and outputs $U_{\mathrm c}(\mu, m)$. With $\mu$ a shortest description of $\sigma$ given $n$, of length $k$, we get $m = n$ and $N(\bar\alpha\, 01\, \mu) = \sigma$. So
$$
n = C(\sigma) \leq k + 2 \log(j + 1) + 2 + c',
$$
that is, $j \leq 2 \log(j + 1) + c' + 2$. This bounds $j$ by a constant $d$ independent of $\sigma$, and $C(\sigma) \leq K(\sigma \mid C(\sigma)) + d$.
:::

:::quiz[Levin's theorem]
In the upper bound of :ref{#thm-levin-c-k}, why is the machine $M$ prefix-free for each condition $m$, although $V$ is not prefix-free?

- [x] $M(\cdot, m)$ only accepts inputs of length exactly $m$, and distinct strings of the same length are incomparable.
- [ ] Because $V$ is optimal.

  Optimality says nothing about the shape of the domain; the domain of $V$ contains comparable strings.
- [ ] Because the condition $m$ is a shortest description.

  The condition is a number, the length of the input; no shortest description is involved.

---

In the lower bound, why does the description $\bar\alpha\, 01\, \mu$ contain $j = n - k$ rather than $n$?

- [x] Coding $n$ would cost about $2 \log n$ bits, which is not bounded; the number $j$ is shown to be bounded, and its code costs $2 \log(j + 1) + 2$ bits.
- [ ] Because $n$ cannot be computed from $\sigma$.

  The machine never computes from $\sigma$; it computes $\sigma$. The point is the length of the description.
- [ ] Because $j$ is always positive.

  The case $j \leq 0$ is treated separately; positivity is not what makes the code short.
:::

## Strongly K-random strings are C-random

A string $\sigma$ of length $n$ is **C-random with constant $d$** if $C(\sigma) \geq n - d$, and **strongly K-random with constant $d$** if $K(\sigma) \geq n + K(n) - d$. Both say that the complexity is within $d$ of its maximal value, by :ref{#prop-c-basic} and :ref{#prop-k-basic}. The next theorem says that the second notion is at least as strong as the first.

:::theorem[Solovay]{#thm-solovay-strong-k}
For every $d$ there is $d'$ such that every strongly K-random string with constant $d$ is C-random with constant $d'$.
:::

:::proof{of=thm-solovay-strong-k}
Let $c$ be such that $C(\rho) \leq |\rho| + c$ for every $\rho$. Let $\sigma$ have length $n$, and let $j = n + c - C(\sigma) \geq 0$. The number $C(\sigma) = n + c - j$ is computed from the pair $\langle n, j \rangle$, so by :ref{#prop-k-basic}
$$
K(C(\sigma)) \leq^+ K(n, j) \leq^+ K(n) + K(j) \leq^+ K(n) + 2 \log(j + 2).
$$
With $K(\sigma) \leq^+ C(\sigma) + K(C(\sigma))$, also from :ref{#prop-k-basic}, we obtain
$$
K(\sigma) \leq n + K(n) - j + 2 \log(j + 2) + e
$$
for a constant $e$ independent of $\sigma$. If $\sigma$ is strongly K-random with constant $d$, then $j - 2 \log(j + 2) \leq d + e$, which bounds $j$ by a constant depending only on $d$; so $C(\sigma) = n + c - j \geq n - d'$.
:::

The proof shows more: the distance of $K(\sigma)$ from its maximum, $n + K(n) - K(\sigma)$, is at least the distance $n - C(\sigma)$ of $C(\sigma)$ from its maximum, minus a logarithmic term. The converse of the theorem fails: there is a constant $c$ such that, for every $d$, infinitely many strings are C-random with constant $c$ but not strongly K-random with constant $d$ (Solovay; admitted, Downey–Hirschfeldt, Corollary 4.3.8). In Solovay's examples, $|\nu| + K(|\nu|) - K(\nu)$ grows like $\log \log |\nu|$. The plain notion of randomness for strings is weaker.

## Descriptions of a given length

Let $L_n$ be the set of elements of length $n$ of the domain of $U$. The total weight of the domain is at most $1$, so $|L_n| \leq 2^n$. Solovay's lemma says that much fewer descriptions have length $n$ when $n$ is a simple number: their number is controlled by $2^{n - K(n)}$.

:::lemma[Solovay]{#lem-solovay-ln}
$|L_n| \leq 2^{n - K(n) + O(1)}$.
:::

:::proof{of=lem-solovay-ln}
Enumerate the domain of $U$. Whenever, for some $n$ and $k \geq 0$, the number of enumerated elements of $L_n$ reaches $2^k$, enumerate the request $(n, n - k + 1)$. Let $k_n$ be the largest $k$ with $|L_n| \geq 2^k$, when $L_n \neq \emptyset$. The requests concerning $n$ have weight
$$
\sum_{k \leq k_n} 2^{-(n - k + 1)} \leq 2^{-n + k_n} \leq 2^{-n} |L_n|,
$$
so the total weight is at most $\sum_n 2^{-n} |L_n|$, the weight of the domain of $U$, at most $1$. By :ref{#thm-kc}, $K(n) \leq^+ n - k_n + 1$. Hence $|L_n| < 2^{k_n + 1} \leq 2^{n - K(n) + O(1)}$.
:::

Each string $\sigma$ has its shortest descriptions in $L_{K(\sigma)}$. By the lemma, a shortest description of $\sigma$ is determined by $K(\sigma)$ and its position in $L_{K(\sigma)}$, a number written with $K(\sigma) - K^{(2)}(\sigma) + O(1)$ bits. To give $K(\sigma)$, it suffices to give $K^{(2)}(\sigma)$, which together with the length of the position yields $K(\sigma)$, and $K^{(2)}(\sigma)$ costs $K^{(3)}(\sigma)$ bits. This plain description of $\sigma$ is shorter than its shortest prefix-free description.

:::theorem[Solovay]{#thm-solovay-c-upper}
$C(\sigma) \leq^+ K(\sigma) - K^{(2)}(\sigma) + K^{(3)}(\sigma)$.
:::

:::proof{of=thm-solovay-c-upper}
Let $b$ be such that $|L_n| \leq 2^{n - K(n) + b}$ for every $n$. Let $N$ be the plain machine that, on input $\mu$, searches for a prefix $\mu_1$ of $\mu$ in the domain of $U$; if one is found, it is unique, and with $\mu = \mu_1 \mu_2$, the machine computes $n = |\mu_2| + U(\mu_1) - b$, reads $\mu_2$ as a number $i$ in binary, enumerates $L_n$ until its $i$-th element $\tau$ appears, counting from $0$, and outputs $U(\tau)$.

Given $\sigma$, let $\tau$ be a shortest $U$-description of $\sigma$, so that $\tau \in L_{K(\sigma)}$, and let $i$ be its position in the enumeration of $L_{K(\sigma)}$. Since $i < 2^{K(\sigma) - K^{(2)}(\sigma) + b}$, the number $i$ is written in binary, with leading zeros, as a string $\mu_2$ of length exactly $K(\sigma) - K^{(2)}(\sigma) + b$. Let $\mu_1$ be a shortest $U$-description of the number $K^{(2)}(\sigma)$. Then $N$ computes $n = K(\sigma) - K^{(2)}(\sigma) + b + K^{(2)}(\sigma) - b = K(\sigma)$, and outputs $U(\tau) = \sigma$. So $C(\sigma) \leq^+ |\mu_1 \mu_2| = K^{(3)}(\sigma) + K(\sigma) - K^{(2)}(\sigma) + b$.
:::

Combined with $K \leq^+ C + K(C)$, this is the first step of Solovay's theorem relating the two complexities,
$$
K(\sigma) = C(\sigma) + C^{(2)}(\sigma) \pm O(C^{(3)}(\sigma)), \qquad C(\sigma) = K(\sigma) - K^{(2)}(\sigma) \pm O(K^{(3)}(\sigma)),
$$
where $C^{(2)}(\sigma) = C(C(\sigma))$ and $C^{(3)}(\sigma) = C(C(C(\sigma)))$. The rest of the proof is a computation with these estimates (admitted; Downey–Hirschfeldt, Theorem 4.2.2). Solovay also showed that the error terms cannot be improved: the expected next approximation $K = C + C^{(2)} + C^{(3)} \pm O(C^{(4)})$ is false.

::::exercise[Levin's characterization by a minimum]{#ex-levin-minimum difficulty=2 objective="Adapt the machines of Levin's theorem to characterize $C$ as the least $n$ for which $K(\sigma \mid n) \leq n$."}
Let $m_\sigma$ be the least $n$ with $K(\sigma \mid n) \leq n$. Show that $C(\sigma) =^+ m_\sigma$.

:::hint
For $m_\sigma \leq^+ C(\sigma)$, build a conditional prefix-free machine $M$ such that, given $n = C(\sigma) + 2i + 1$, the string $0^i 1 \beta$ describes $\sigma$ when $\beta$ is a shortest $V$-description of $\sigma$; then choose $i$ according to the coding constant of $M$.
:::

:::solution
*$C(\sigma) \leq^+ m_\sigma$.* Let $N$ be the plain machine that, on input $\tau$, searches for a prefix $\mu$ of $\tau$ such that $U_{\mathrm c}(\mu, |\tau|)$ converges, and outputs $U_{\mathrm c}(\mu, |\tau|)$. The prefix is unique when it exists, since the domain of $U_{\mathrm c}(\cdot, |\tau|)$ is prefix-free. Let $n = m_\sigma$ and $\mu$ a shortest description of $\sigma$ given $n$, so $|\mu| \leq n$. Then $\tau = \mu 0^{n - |\mu|}$ has length $n$ and $N(\tau) = \sigma$. So $C(\sigma) \leq^+ n$.

*$m_\sigma \leq^+ C(\sigma)$.* Let $M$ be the conditional machine with $M(0^i 1 \beta, n) = V(\beta)$ when $|\beta| + 2i + 1 = n$, and undefined otherwise. For a fixed $n$, its domain is prefix-free: two strings $0^i 1 \beta$ and $0^{i'} 1 \beta'$ with $i < i'$ differ at position $i$, and with $i = i'$ they have the same length. Let $c$ be such that $K(\rho \mid n) \leq K_M(\rho \mid n) + c$ for all $\rho$ and $n$. Take $i = c$ and $n = C(\sigma) + 2c + 1$, and $\beta$ a shortest $V$-description of $\sigma$. Then $0^c 1 \beta$ is an $M$-description of $\sigma$ given $n$, of length $C(\sigma) + c + 1 = n - c$, so $K(\sigma \mid n) \leq n$. Hence $m_\sigma \leq C(\sigma) + 2c + 1$. (Downey–Hirschfeldt, Theorem 4.1.1, where the second part uses the recursion theorem instead.)
:::
::::

## Notes and references

Levin's theorem is from his 1974 dissertation; the first published proof is in Gács (1974). Solovay's results are from unpublished notes of 1975, circulated widely; Downey and Hirschfeldt (Chapter 4) give the first complete published account, with the proofs followed here (Theorem 4.1.1, Lemmas 4.2.3, 4.2.4 and 4.2.6, Theorem 4.3.2). Miller applied these estimates to prove Muchnik's theorem on the relation between $C$ and $K$ (Downey–Hirschfeldt, Section 4.4).

- P. Gács, *On the symmetry of algorithmic information*, Soviet Mathematics Doklady 15 (1974), 1477–1480.
- R. M. Solovay, *Draft of a paper (or series of papers) on Chaitin's work*, unpublished notes, IBM Thomas J. Watson Research Center, 1975.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Chapter 4.
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, 3rd edition, Springer, 2008, Section 3.9.

:::::exercises
::::exercise{#ex-few-of-complexity-n difficulty=1 objective="Derive from Solovay's lemma a bound on the number of strings of a given prefix-free complexity."}
Show that at most $2^{n - K(n) + O(1)}$ strings $\sigma$ satisfy $K(\sigma) = n$.

:::solution
Each string with $K(\sigma) = n$ has a shortest description in $L_n$, and distinct strings have distinct descriptions. So their number is at most $|L_n| \leq 2^{n - K(n) + O(1)}$ by :ref{#lem-solovay-ln}.
:::
::::

::::exercise{#ex-weakly-k-random difficulty=1 objective="Compare C-randomness with the weak form of K-randomness."}
A string $\sigma$ is **weakly K-random with constant $d$** if $K(\sigma) \geq |\sigma| - d$. Show that every C-random string with constant $d$ is weakly K-random with constant $d + O(1)$, and that every strongly K-random string with constant $d$ is weakly K-random with constant $d$.

:::solution
By :ref{#prop-k-basic} (3), $C \leq^+ K$: if $C(\sigma) \geq |\sigma| - d$, then $K(\sigma) \geq |\sigma| - d - O(1)$. If $K(\sigma) \geq |\sigma| + K(|\sigma|) - d$, then $K(\sigma) \geq |\sigma| - d$ since $K(|\sigma|) \geq 0$. Together with :ref{#thm-solovay-strong-k}, strong K-randomness implies C-randomness, which implies weak K-randomness, each up to a change of constant.
:::
::::

::::exercise[Conditional versions]{#ex-levin-length-condition difficulty=2 objective="Relativize Levin's argument to compare plain complexity given the length with prefix-free complexity given the length."}
Show that $C(\sigma \mid |\sigma|) \leq^+ K(\sigma \mid |\sigma|) \leq^+ C(\sigma \mid |\sigma|) + 2 \log C(\sigma \mid |\sigma|)$, where $C(\sigma \mid \tau)$ is plain conditional complexity and $\log 0$ is read as $0$.

:::solution
The optimal conditional prefix-free machine $U_{\mathrm c}$ is a conditional machine, so $C(\rho \mid \tau) \leq^+ K(\rho \mid \tau)$ for all $\rho$, $\tau$, by optimality of the conditional machine defining plain conditional complexity. For the second inequality, let $W$ be that optimal plain conditional machine, and let $M$ be the conditional machine that, given $\tau$, on input $\bar\alpha\, 01\, \beta$ with $\alpha$ the string of $|\beta|$, outputs $W(\beta, \tau)$. For each $\tau$, its domain is prefix-free, since $\bar\alpha\, 01$ determines $|\beta|$ and hence the end of the input. With $\beta$ a shortest description of $\sigma$ given $\tau = |\sigma|$, the input has length $C(\sigma \mid |\sigma|) + 2 \lfloor \log(C(\sigma \mid |\sigma|) + 1) \rfloor + 2$.
:::
::::

::::exercise[Upper bound on K by C]{#ex-k-iterated-c difficulty=2 objective="Iterate the self-delimitation trick to bound $K$ by iterated plain complexities."}
Show that $K(\sigma) \leq^+ C(\sigma) + C(C(\sigma)) + 2 \log C(C(\sigma))$.

:::solution
Let $M$ be the machine that, on input $\bar\alpha\, 01\, \beta_1 \beta_2$, where $\alpha$ is the string of a number $\ell$, splits $\beta_1\beta_2$ with $|\beta_1| = \ell$, computes the number $m = V(\beta_1)$, requires $|\beta_2| = m$, and outputs $V(\beta_2)$. Its domain is prefix-free: the prefix $\bar\alpha\, 01$ determines $\ell$, hence $\beta_1$, hence $m$, hence the total length of the input. With $\beta_2$ a shortest $V$-description of $\sigma$, of length $m = C(\sigma)$, and $\beta_1$ a shortest $V$-description of $m$, of length $\ell = C(C(\sigma))$, the input has length $2 \lfloor \log(\ell + 1) \rfloor + 2 + \ell + C(\sigma)$. (This is the case $n = 1$ of Downey–Hirschfeldt, Proposition 4.2.1, with a slightly larger error term.)
:::
::::
:::::
