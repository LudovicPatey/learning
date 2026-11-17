---
title: Prefix-free symmetry of information
summary: Conditional prefix-free complexity; the complexity of a pair is the complexity of its first coordinate plus the complexity of the second given a shortest description of the first, up to a constant (Gács, Chaitin).
duration: 35
prerequisites: [conditional-complexity, coding-theorem]
---

For plain complexity, the decomposition $C(\sigma, \tau) = C(\sigma) + C(\tau \mid \sigma)$ holds only up to a logarithmic term, and the term is necessary. Prefix-free complexity removes the cost of separating two descriptions, so a better decomposition can be expected. It does not hold in the naive form $K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma)$, but it holds exactly, up to a constant, when the condition $\sigma$ is replaced by a shortest description $\sigma^*$ of $\sigma$:
$$
K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma^*).
$$
A shortest description carries, besides $\sigma$, the number $K(\sigma)$, and this number is the information missing from the naive formula. The proof is the main application of the coding theorem: the descriptions of all pairs $\langle \sigma, \tau \rangle$, for a fixed $\sigma$, have a total weight of order $2^{-K(\sigma)}$, and the KC theorem converts them, given $\sigma^*$, into descriptions of the strings $\tau$ that are shorter by $K(\sigma)$ bits.

## Conditional prefix-free complexity

:::definition{#def-conditional-prefix-free}
A conditional machine $M$ is **prefix-free** if for every $\tau$ the set $\{ \rho : M(\rho, \tau)\converge \}$ is prefix-free. We write $K_M(\sigma \mid \tau) = C_M(\sigma \mid \tau)$.
:::

The proof of :ref{#thm-optimal-prefix-free} works uniformly in the condition: applying its transformation to the machine $\rho \mapsto M_e(\rho, \tau)$, for each $\tau$ separately, gives an effective list of conditional prefix-free machines containing all of them, and the machine $(0^e 1 \rho, \tau) \mapsto \hat M_e(\rho, \tau)$ is an optimal conditional prefix-free machine. We fix one, $U_{\mathrm c}$, and write $K(\sigma \mid \tau) = K_{U_{\mathrm c}}(\sigma \mid \tau)$; from now on, $U_{\mathrm c}$ denotes this machine, and no longer the optimal plain conditional machine of the previous lesson. As for plain complexity, $K(\sigma) =^+ K(\sigma \mid \varepsilon)$, $K(\sigma \mid \tau) \leq^+ K(\sigma)$, $K(f(\sigma) \mid \tau) \leq^+ K(\sigma \mid \tau)$ and $K(\sigma \mid \tau) \leq^+ K(\sigma \mid g(\tau))$ for partial computable $f$ and $g$, by the arguments of :ref{#prop-conditional-basic}, which produce prefix-free machines from prefix-free machines. For instance, $K(\sigma \mid |\sigma|) \leq^+ |\sigma|$: given $n$, the machine that reads exactly $n$ bits and outputs them has the prefix-free domain $\{0,1\}^n$.

The KC theorem also holds with conditions. The proof of :ref{#thm-kc} is uniform in an index of the request set, so it can be run for every condition at once.

:::lemma{#lem-conditional-kc}
Let $R$ be a c.e. set of triples $(\sigma, \ell, \tau)$ such that for every $\tau$, the request set $R_\tau = \{ (\sigma, \ell) : (\sigma, \ell, \tau) \in R \}$ is bounded. Then $K(\sigma \mid \tau) \leq^+ \ell$ for every $(\sigma, \ell, \tau) \in R$.
:::

:::proof{of=lem-conditional-kc}
Let $M(\rho, \tau)$ be the value at $\rho$ of the machine built by the proof of :ref{#thm-kc} from the enumeration of $R_\tau$ derived from a fixed enumeration of $R$. It is partial computable, and for each $\tau$ the machine $M(\cdot, \tau)$ is prefix-free and satisfies $R_\tau$. Conclude by optimality of $U_{\mathrm c}$.
:::

The lemma is used below with request sets that are **truncated**: given a c.e. set $S$ of triples, let $R$ consist of the triples of $S$ that are enumerated while the total weight of the triples already accepted with the same condition $\tau$, together with the new one, is at most $1$. Then $R$ is c.e., each $R_\tau$ is bounded, and $R_\tau = S_\tau$ whenever the weight of $S_\tau$ is at most $1$. Truncation lets a construction issue requests without knowing in advance which conditions are relevant.

## Shortest descriptions as conditions

Fix an enumeration of the domain of the optimal prefix-free machine $U$. For a string $\sigma$, let $\sigma^*$ be the first description of $\sigma$ of length $K(\sigma)$ in this enumeration. So $U(\sigma^*) = \sigma$ and $|\sigma^*| = K(\sigma)$.

:::proposition{#prop-star}
1. The strings $\sigma$ and $\langle \sigma, K(\sigma) \rangle$ are computed from $\sigma^*$, and $\sigma^*$ is computed from $\langle \sigma, K(\sigma) \rangle$, by fixed partial computable functions. Hence $K(\rho \mid \sigma^*) =^+ K(\rho \mid \sigma, K(\sigma))$ for all $\rho$ and $\sigma$.
2. $K(\sigma^*) =^+ K(\sigma) =^+ K(\sigma, K(\sigma))$.
:::

:::proof{of=prop-star}
1. $\sigma = U(\sigma^*)$ and $K(\sigma) = |\sigma^*|$. Conversely, from $\sigma$ and $k = K(\sigma)$, enumerate the domain of $U$ until a description of $\sigma$ of length $k$ appears; the first one is $\sigma^*$. The equality of conditional complexities follows from the property $K(\rho \mid \tau) \leq^+ K(\rho \mid g(\tau))$, applied in both directions.
2. By 1, $K(\sigma) \leq^+ K(\sigma, K(\sigma)) \leq^+ K(\sigma^*)$. For $K(\sigma^*) \leq^+ K(\sigma)$, let $M$ be the machine that, on input $\rho$, computes $U(\rho)$ and outputs the first description of $U(\rho)$ of length $|\rho|$ in the enumeration of the domain of $U$. Its domain is the domain of $U$, which is prefix-free. If $\rho$ is a shortest description of $\sigma$, then $|\rho| = K(\sigma)$ and $M(\rho) = \sigma^*$.
:::

So the number $K(\sigma)$ is information that comes for free with $\sigma$ when $\sigma$ is described in a shortest way. It is not, in general, information that can be recovered from $\sigma$: Gács and Solovay proved that for all large $n$ some string $\sigma$ of length $n$ has $K(K(\sigma) \mid \sigma) \geq \log n - \log \log n - 3$ (admitted; Downey–Hirschfeldt, Theorem 3.14.2).

## The symmetry theorem

:::theorem[Symmetry of information; Gács, Chaitin]{#thm-symmetry-prefix-free}
$K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma^*)$.
:::

The upper bound describes $\sigma$ by $\sigma^*$, which gives the condition for free, then $\tau$ given $\sigma^*$; the two descriptions are separated by prefix-freeness. For the lower bound, fix $\sigma$, and consider all descriptions of all pairs $\langle \sigma, \tau \rangle$. By the coding theorem applied to the machine that keeps only the first coordinate of the output of $U$, their total weight is at most $2^{c - K(\sigma)}$. Multiplying the weights by $2^{K(\sigma) - c}$ gives a bounded request set, which, given $\sigma^*$ and hence $K(\sigma)$, can be enumerated: a description $\nu$ of $\langle \sigma, \tau \rangle$ becomes a request for a description of $\tau$ of length $|\nu| - K(\sigma) + c$.

:::proof{of=thm-symmetry-prefix-free}
*Upper bound.* Let $M$ be the machine that, on input $\alpha\beta$ with $\alpha$ in the domain of $U$, computes $\sigma = U(\alpha)$ and the first description $\alpha'$ of $\sigma$ of length $|\alpha|$ in the enumeration of the domain of $U$, then computes $\tau = U_{\mathrm c}(\beta, \alpha')$ and outputs $\langle \sigma, \tau \rangle$. Its domain is prefix-free: if $\alpha\beta$ and $\alpha_1\beta_1$ are comparable elements of the domain, then $\alpha$ and $\alpha_1$ are comparable elements of the domain of $U$, hence equal, and then $\beta$ and $\beta_1$ are comparable elements of the domain of $U_{\mathrm c}(\cdot, \alpha')$, hence equal. With $\alpha = \sigma^*$, we get $\alpha' = \sigma^*$, and with $\beta$ a shortest description of $\tau$ given $\sigma^*$, the input $\alpha\beta$ has length $K(\sigma) + K(\tau \mid \sigma^*)$.

*Lower bound.* Let $N$ be the machine that, on input $\nu$, computes $U(\nu)$ and outputs its first coordinate when $U(\nu)$ is a pair, which it always is since $\langle \cdot, \cdot \rangle$ is a bijection. Its domain is the domain of $U$, so it is prefix-free, and $P_N(\sigma) = \sum \{ 2^{-|\nu|} : U(\nu) = \langle \sigma, \tau \rangle \text{ for some } \tau \}$. By :ref{#thm-coding}, there is $c$ with $K(\sigma) \leq -\log P_N(\sigma) + c$, that is,
$$
P_N(\sigma) \leq 2^{c - K(\sigma)} \quad \text{for every } \sigma.
$$
Let $S$ be the c.e. set of triples $(\tau, |\nu| - |\rho| + c, \rho)$ such that $\rho$ and $\nu$ are in the domain of $U$, $U(\nu) = \langle U(\rho), \tau \rangle$, and $|\nu| - |\rho| + c \geq 0$, and let $R$ be its truncation. For the condition $\rho = \sigma^*$, the weight of $S_{\sigma^*}$ is at most
$$
\sum_{\nu : U(\nu) = \langle \sigma, \cdot \rangle} 2^{-|\nu| + K(\sigma) - c} = 2^{K(\sigma) - c} P_N(\sigma) \leq 1,
$$
so $R_{\sigma^*} = S_{\sigma^*}$. Taking for $\nu$ a shortest description of $\langle \sigma, \tau \rangle$, the triple $(\tau, K(\sigma, \tau) - K(\sigma) + c, \sigma^*)$ is in $R$; the length is non-negative since $K(\sigma) \leq^+ K(\sigma, \tau)$, after enlarging $c$ if necessary. By :ref{#lem-conditional-kc}, $K(\tau \mid \sigma^*) \leq^+ K(\sigma, \tau) - K(\sigma)$.
:::

:::figure[The lower bound of :ref{#thm-symmetry-prefix-free}. The descriptions $\nu$ of the pairs with first coordinate $\sigma$ have total weight at most $2^{c - K(\sigma)}$. Given $\sigma^*$, each of them is turned into a request for a description of the second coordinate $\tau$, shorter by $K(\sigma) - c$ bits.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Left: descriptions nu one, nu two, nu three of pairs (sigma, tau one), (sigma, tau two), (sigma, tau one), with total weight at most 2 to the c minus K of sigma. Right: requests for tau one, tau two, tau one, of lengths reduced by K of sigma minus c, with total weight at most 1"><defs><marker id="soi-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="40" y="24" class="label">descriptions of pairs ⟨σ, τ⟩</text><text x="360" y="24" class="label">requests given σ*</text><rect x="40" y="40" width="200" height="26" class="cell"/><text x="140" y="58" text-anchor="middle" class="mrm" font-size="13">ν₁ ↦ ⟨σ, τ₁⟩</text><rect x="360" y="40" width="200" height="26" class="cell head-cell"/><text x="460" y="58" text-anchor="middle" class="mrm" font-size="13">(τ₁, |ν₁| − K(σ) + c)</text><line x1="248" y1="53" x2="352" y2="53" class="ink-stroke" stroke-width="1.1" marker-end="url(#soi-arrow)"/><rect x="40" y="76" width="200" height="26" class="cell"/><text x="140" y="94" text-anchor="middle" class="mrm" font-size="13">ν₂ ↦ ⟨σ, τ₂⟩</text><rect x="360" y="76" width="200" height="26" class="cell head-cell"/><text x="460" y="94" text-anchor="middle" class="mrm" font-size="13">(τ₂, |ν₂| − K(σ) + c)</text><line x1="248" y1="89" x2="352" y2="89" class="ink-stroke" stroke-width="1.1" marker-end="url(#soi-arrow)"/><rect x="40" y="112" width="200" height="26" class="cell"/><text x="140" y="130" text-anchor="middle" class="mrm" font-size="13">ν₃ ↦ ⟨σ, τ₁⟩</text><rect x="360" y="112" width="200" height="26" class="cell head-cell"/><text x="460" y="130" text-anchor="middle" class="mrm" font-size="13">(τ₁, |ν₃| − K(σ) + c)</text><line x1="248" y1="125" x2="352" y2="125" class="ink-stroke" stroke-width="1.1" marker-end="url(#soi-arrow)"/><text x="40" y="166" class="label">total weight ≤ 2^(c − K(σ))</text><text x="360" y="166" class="label">total weight ≤ 1: a KC set</text><text x="300" y="190" text-anchor="middle" class="label">weights multiplied by 2^(K(σ) − c)</text></svg>
:::

:::quiz[the prefix-free symmetry of information]
In the lower bound of :ref{#thm-symmetry-prefix-free}, why is the condition $\sigma^*$ and not $\sigma$?

- [x] The requests have lengths $|\nu| - K(\sigma) + c$, so the machine must know $K(\sigma)$, which is $|\sigma^*|$; it cannot in general be computed from $\sigma$.
- [ ] Because $\sigma^*$ is shorter than $\sigma$.

  $\sigma^*$ may be longer than $\sigma$, since $K(\sigma)$ can exceed $|\sigma|$; its length is not what matters.
- [ ] Because the machine must be prefix-free in the condition.

  Prefix-freeness concerns the descriptions for each fixed condition, not the conditions.

---

Where is the coding theorem used?

- [x] To bound the total weight of the descriptions of the pairs with first coordinate $\sigma$ by $2^{c - K(\sigma)}$, which makes the rescaled requests a bounded request set.
- [ ] To show that $K(\sigma, \tau) \geq K(\sigma)$.

  This follows from the computability of the first projection, without the coding theorem.
- [ ] To build the machine of the upper bound.

  The upper bound only concatenates two descriptions.
:::

Applying the theorem in both orders, as for :ref{#cor-symmetry-plain}, gives a symmetry that holds up to a constant.

:::corollary{#cor-symmetry-prefix-free}
$K(\sigma) - K(\sigma \mid \tau^*) =^+ K(\tau) - K(\tau \mid \sigma^*)$.
:::

:::proof{of=cor-symmetry-prefix-free}
By the theorem, $K(\sigma) + K(\tau \mid \sigma^*) =^+ K(\sigma, \tau) =^+ K(\tau, \sigma) =^+ K(\tau) + K(\sigma \mid \tau^*)$, where the middle equality holds because $\langle \sigma, \tau \rangle \mapsto \langle \tau, \sigma \rangle$ is computable.
:::

The theorem also explains the maximal complexity of strings. A string $\sigma$ of length $n$ and the pair $\langle n, \sigma \rangle$ are computed from each other, so $K(\sigma) =^+ K(n, \sigma)$, and the theorem gives
$$
K(\sigma) =^+ K(n) + K(\sigma \mid n^*) \quad \text{for } |\sigma| = n.
$$
Since $K(\sigma \mid n^*) \leq^+ K(\sigma \mid n) \leq^+ n$, this gives again $K(\sigma) \leq^+ n + K(n)$, and identifies the deficiency from the maximum: $n + K(n) - K(\sigma) =^+ n - K(\sigma \mid n^*)$. A string is **strongly K-random**, $K(\sigma) \geq n + K(n) - d$, if and only if it is incompressible given $n^*$ up to a constant related to $d$.

The naive decomposition $K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma)$ fails. With $\tau$ the number $K(\sigma)$, the left-hand side is $K(\sigma, K(\sigma)) =^+ K(\sigma)$ by :ref{#prop-star}, so the decomposition would give $K(K(\sigma) \mid \sigma) =^+ 0$, contradicting the theorem of Gács and Solovay quoted above. It holds up to the term $K(K(\sigma) \mid \sigma)$, which is at most logarithmic in $K(\sigma)$ (:ref{#ex-naive-decomposition}).

::::exercise[The naive decomposition]{#ex-naive-decomposition difficulty=2 objective="Bound the error of the naive decomposition of the complexity of a pair by the complexity of $K(\sigma)$ given $\sigma$."}
Show that
$$
K(\sigma) + K(\tau \mid \sigma) - K(K(\sigma) \mid \sigma) - O(1) \leq K(\sigma, \tau) \leq K(\sigma) + K(\tau \mid \sigma) + O(1),
$$
and deduce that $K(\sigma, \tau) = K(\sigma) + K(\tau \mid \sigma) \pm O(\log K(\sigma))$ for $K(\sigma) \geq 2$.

:::hint
For the lower bound, describe $\tau$ given $\sigma$ by a description of $K(\sigma)$ given $\sigma$ followed by a description of $\tau$ given $\sigma^*$.
:::

:::solution
*Upper bound.* By :ref{#prop-star} (1), $\sigma$ is computed from $\sigma^*$, so $K(\tau \mid \sigma^*) \leq^+ K(\tau \mid \sigma)$, and the theorem gives $K(\sigma, \tau) \leq^+ K(\sigma) + K(\tau \mid \sigma)$.

*Lower bound.* Let $M$ be the conditional machine that, given $\sigma$, on input $\alpha\beta$ with $\alpha$ in the domain of $U_{\mathrm c}(\cdot, \sigma)$, computes $k = U_{\mathrm c}(\alpha, \sigma)$, then $\sigma^*$ from $\sigma$ and $k$ as in :ref{#prop-star} (1), and outputs $U_{\mathrm c}(\beta, \sigma^*)$. For each condition, its domain is prefix-free, by the argument of the upper bound of the theorem. With $\alpha$ a shortest description of $K(\sigma)$ given $\sigma$ and $\beta$ a shortest description of $\tau$ given $\sigma^*$, we get $K(\tau \mid \sigma) \leq^+ K(K(\sigma) \mid \sigma) + K(\tau \mid \sigma^*)$. With the theorem, $K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma^*) \geq^+ K(\sigma) + K(\tau \mid \sigma) - K(K(\sigma) \mid \sigma)$.

Finally $K(K(\sigma) \mid \sigma) \leq^+ K(K(\sigma)) \leq^+ 2 \log K(\sigma)$ by :ref{#prop-k-basic} (2), which gives the last statement.
:::
::::

## Notes and references

The symmetry of information for prefix-free complexity is due independently to Gács (1974), with Levin, and to Chaitin (1975), who introduced the condition $\sigma^*$. The proof given here, through the coding theorem and the KC theorem, follows Downey and Hirschfeldt (Theorem 3.10.2). The lower bound on $K(K(\sigma) \mid \sigma)$ is due to Gács (1974) and Solovay (unpublished notes, 1975); Downey and Hirschfeldt give a proof (Section 3.14).

- P. Gács, *On the symmetry of algorithmic information*, Soviet Mathematics Doklady 15 (1974), 1477–1480.
- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.10 and 3.14.
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, 3rd edition, Springer, 2008, Section 3.9.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 2.3.

:::::exercises
::::exercise{#ex-star-not-shortest difficulty=2 objective="See that every shortest description can serve as the condition in the symmetry theorem."}
Let $\rho$ be a shortest description of $\sigma$, not necessarily $\sigma^*$. Show that $K(\tau \mid \rho) =^+ K(\tau \mid \sigma^*)$, with a constant independent of $\rho$, $\sigma$ and $\tau$.

:::solution
From $\rho$, compute $\sigma = U(\rho)$ and $K(\sigma) = |\rho|$, and then $\sigma^*$ as in :ref{#prop-star} (1). So $\sigma^* = g(\rho)$ for a fixed partial computable $g$, and $K(\tau \mid \rho) \leq^+ K(\tau \mid \sigma^*)$.

Conversely, $\sigma^*$ need not compute $\rho$, so the theorem is used. The machine of the upper bound of :ref{#thm-symmetry-prefix-free}, modified to use the condition $\alpha$ itself instead of $\alpha'$, that is, $\alpha\beta \mapsto \langle U(\alpha), U_{\mathrm c}(\beta, \alpha) \rangle$, is prefix-free by the same argument. With $\alpha = \rho$ and $\beta$ a shortest description of $\tau$ given $\rho$, it gives $K(\sigma, \tau) \leq^+ K(\sigma) + K(\tau \mid \rho)$. By the lower bound of the theorem, $K(\tau \mid \sigma^*) \leq^+ K(\sigma, \tau) - K(\sigma) \leq^+ K(\tau \mid \rho)$.
:::
::::

::::exercise{#ex-strongly-random-conditional difficulty=1 objective="Translate strong K-randomness into incompressibility given a shortest description of the length."}
Show that for every $d$ there is $d'$ such that, for every string $\sigma$ of length $n$, if $K(\sigma) \geq n + K(n) - d$ then $K(\sigma \mid n^*) \geq n - d'$, and if $K(\sigma \mid n^*) \geq n - d$ then $K(\sigma) \geq n + K(n) - d'$.

:::solution
By the formula $K(\sigma) =^+ K(n) + K(\sigma \mid n^*)$ derived from :ref{#thm-symmetry-prefix-free}, there is $c$ with $|K(\sigma) - K(n) - K(\sigma \mid n^*)| \leq c$ for every $\sigma$ of length $n$. If $K(\sigma) \geq n + K(n) - d$, then $K(\sigma \mid n^*) \geq K(\sigma) - K(n) - c \geq n - d - c$. If $K(\sigma \mid n^*) \geq n - d$, then $K(\sigma) \geq K(n) + n - d - c$. Take $d' = d + c$.
:::
::::

::::exercise[Additivity of information]{#ex-information-additive difficulty=2 objective="Derive from the symmetry theorem the chain rule for three strings with prefix-free complexity."}
Write $K(\sigma, \tau, \rho) = K(\langle \sigma, \langle \tau, \rho \rangle \rangle)$, and let $\langle \sigma, \tau \rangle^*$ be the canonical shortest description of the pair. Show that
$$
K(\sigma, \tau, \rho) =^+ K(\sigma) + K(\tau \mid \sigma^*) + K(\rho \mid \langle \sigma, \tau \rangle^*).
$$

:::solution
The strings $\langle \sigma, \langle \tau, \rho \rangle \rangle$ and $\langle \langle \sigma, \tau \rangle, \rho \rangle$ are computed from each other, so they have the same prefix-free complexity up to a constant. By :ref{#thm-symmetry-prefix-free} applied to the pair $(\langle \sigma, \tau \rangle, \rho)$, $K(\sigma, \tau, \rho) =^+ K(\sigma, \tau) + K(\rho \mid \langle \sigma, \tau \rangle^*)$. By the theorem applied to $(\sigma, \tau)$, $K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma^*)$. Substitute.
:::
::::

::::exercise[Subadditivity on concatenations]{#ex-concatenation-star difficulty=2 objective="Apply the symmetry theorem to concatenations rather than pairs."}
Show that $K(\sigma\tau) \leq^+ K(\sigma) + K(\tau \mid \sigma^*)$, and that $K(\sigma, \tau) =^+ K(\sigma\tau) + K(\sigma \mid (\sigma\tau)^*)$.

:::solution
The concatenation is computed from the pair, so $K(\sigma\tau) \leq^+ K(\sigma, \tau) =^+ K(\sigma) + K(\tau \mid \sigma^*)$. For the second equality, the pairs $\langle \sigma, \tau \rangle$ and $\langle \sigma\tau, \sigma \rangle$ are computed from each other (from $\sigma\tau$ and $\sigma$, the string $\tau$ is the remainder of $\sigma\tau$ after the prefix $\sigma$), so $K(\sigma, \tau) =^+ K(\sigma\tau, \sigma) =^+ K(\sigma\tau) + K(\sigma \mid (\sigma\tau)^*)$ by :ref{#thm-symmetry-prefix-free}. (Downey–Hirschfeldt, Corollary 3.10.3.)
:::
::::
:::::
