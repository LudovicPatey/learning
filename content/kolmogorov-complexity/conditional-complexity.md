---
title: Conditional complexity and symmetry of information
summary: The complexity of a string given another string; Kolmogorov's counting bounds for conditional complexity; the symmetry of information for plain complexity, up to a logarithmic term.
duration: 45
prerequisites: [plain-complexity, non-computability]
---

The complexity $C(\sigma)$ measures the information contained in $\sigma$. It is often useful to measure the information that $\sigma$ contains **beyond** what is already known, for instance beyond its length, or beyond another string $\tau$. This is the **conditional complexity** $C(\sigma \mid \tau)$: the length of a shortest description of $\sigma$ for a machine that receives $\tau$ as an auxiliary input. With it, the information that $\tau$ contains about $\sigma$ can be defined as the decrease $C(\sigma) - C(\sigma \mid \tau)$.

The main theorem of the lesson, due to Kolmogorov and Levin, is that this quantity is symmetric: $\tau$ contains as much information about $\sigma$ as $\sigma$ about $\tau$, up to a term logarithmic in the complexity of the pair. It follows from a decomposition of the complexity of a pair, $C(\sigma, \tau) = C(\sigma) + C(\tau \mid \sigma)$ up to a logarithmic term, the analogue of the chain rule $H(X, Y) = H(X) + H(Y \mid X)$ for Shannon entropy. The proof is a counting argument on the finite sets of pairs of bounded complexity. The next lesson shows that for prefix-free complexity, the logarithmic term disappears when the condition is a shortest description instead of the string itself.

## Conditional complexity

:::definition{#def-conditional-machine}
A **conditional machine** is a partial computable function $M : \bstr \times \bstr \to \bstr$. If $M(\rho, \tau) = \sigma$, the string $\rho$ is an **$M$-description of $\sigma$ given $\tau$**. The **complexity of $\sigma$ given $\tau$ relative to $M$** is
$$
C_M(\sigma \mid \tau) = \min \{ |\rho| : M(\rho, \tau) = \sigma \},
$$
with $\min \emptyset = \infty$.
:::

The second argument $\tau$ is the **condition**: it is available to the machine for free, and only the length of $\rho$ is counted. Let $M_0, M_1, \dots$ be an effective list of all conditional machines, and let $U_{\mathrm c}(0^e 1 \rho, \tau) = M_e(\rho, \tau)$. As in the proof of :ref{#thm-invariance}, $U_{\mathrm c}$ is **optimal**: for every conditional machine $M$ there is $c_M$ with $C_{U_{\mathrm c}}(\sigma \mid \tau) \leq C_M(\sigma \mid \tau) + c_M$ for all $\sigma$ and $\tau$; the constant depends on $M$, not on the condition. We fix such a $U_{\mathrm c}$ and write $C(\sigma \mid \tau) = C_{U_{\mathrm c}}(\sigma \mid \tau)$. For numbers and pairs, the condition is the associated string: $C(\sigma \mid n)$ and $C(\sigma \mid \tau, \rho) = C(\sigma \mid \langle \tau, \rho \rangle)$. We also write $C(\sigma, \tau) = C(\langle \sigma, \tau \rangle)$.

Unconditional complexity is complexity given the empty string: the machine $\rho \mapsto U_{\mathrm c}(\rho, \varepsilon)$ gives $C(\sigma) \leq^+ C(\sigma \mid \varepsilon)$, and the conditional machine $(\rho, \tau) \mapsto U(\rho)$, where $U$ is the optimal machine defining $C$, gives $C(\sigma \mid \tau) \leq^+ C(\sigma)$ for every $\tau$. So $C(\sigma) =^+ C(\sigma \mid \varepsilon)$.

:::proposition{#prop-conditional-basic}
1. $C(\sigma \mid \tau) \leq^+ C(\sigma) \leq^+ |\sigma|$, and $C(\sigma \mid \sigma) =^+ 0$.
2. For every partial computable $f$, $C(f(\sigma) \mid \tau) \leq^+ C(\sigma \mid \tau)$ whenever $f(\sigma)$ is defined.
3. For every partial computable $g$, $C(\sigma \mid \tau) \leq^+ C(\sigma \mid g(\tau))$ whenever $g(\tau)$ is defined.
4. $C(\sigma) \leq^+ C(\tau) + C(\sigma \mid \tau) + 2 \log C(\tau)$, where $\log 0$ is read as $0$.
:::

:::proof{of=prop-conditional-basic}
Each inequality is witnessed by a conditional machine, and the optimality of $U_{\mathrm c}$ concludes.

1. The first inequality was shown above, and the second follows from :ref{#prop-c-basic}. The machine $(\rho, \tau) \mapsto \tau$ describes $\sigma$ given $\sigma$ with the empty description.
2. Use $(\rho, \tau) \mapsto f(U_{\mathrm c}(\rho, \tau))$.
3. Use $(\rho, \tau) \mapsto U_{\mathrm c}(\rho, g(\tau))$.
4. As in the proof of :ref{#prop-c-pairs}: on input $\bar\alpha\, 01\, \beta$, where $\alpha$ is the string of a number $\ell$, split $\beta = \beta_0 \beta_1$ with $|\beta_0| = \ell$, compute $\tau = U(\beta_0)$ and output $U_{\mathrm c}(\beta_1, \tau)$. With $\beta_0$ a shortest description of $\tau$ and $\beta_1$ a shortest description of $\sigma$ given $\tau$, the input has length $2 \lfloor \log(C(\tau) + 1) \rfloor + 2 + C(\tau) + C(\sigma \mid \tau)$.
:::

Property 3 says that more information in the condition can only decrease complexity. In particular $C(\sigma \mid \tau, \rho) \leq^+ C(\sigma \mid \tau)$, and $C(\sigma \mid \tau) =^+ C(\sigma \mid \tau')$ whenever each of $\tau$ and $\tau'$ is computed from the other by a fixed partial computable function. Property 4 is the "easy half" of the symmetry of information below.

The counting arguments of the first lesson carry over to conditional complexity, with bounds independent of the condition.

:::theorem[Kolmogorov]{#thm-conditional-counting}
1. For every $\tau$ and every $k \leq n$, fewer than $2^{n - k}$ strings $\sigma$ satisfy $C(\sigma \mid \tau) < n - k$. In particular, every finite set $A$ contains, for every $\tau$, an element $\sigma$ with $C(\sigma \mid \tau) \geq \lfloor \log |A| \rfloor$.
2. Let $B \subseteq \bstr \times \bstr$ be c.e., with finite sections $B_\tau = \{ \sigma : (\sigma, \tau) \in B \}$. Then $C(\sigma \mid \tau) \leq^+ \log |B_\tau|$ for all $\tau$ and $\sigma \in B_\tau$, with a constant independent of $\tau$.
:::

:::proof{of=thm-conditional-counting}
1. For a fixed $\tau$, distinct strings have distinct descriptions given $\tau$, and there are $2^{n-k} - 1$ strings of length less than $n - k$. For the second statement, apply the first with $n = k + \lfloor \log |A| \rfloor$ and $k = 0$: fewer than $2^{\lfloor \log |A| \rfloor} \leq |A|$ strings have $C(\sigma \mid \tau) < \lfloor \log |A| \rfloor$.
2. Let $M(\rho, \tau)$ be the $i$-th element, counting from $0$, in the order of enumeration of $B_\tau$ derived from a fixed enumeration of $B$, where $i$ is the number associated with $\rho$. The $i$-th element of $B_\tau$ is described given $\tau$ by the string of $i$, of length $\lfloor \log(i + 1) \rfloor \leq \log |B_\tau|$, since $i < |B_\tau|$. Conclude by optimality of $U_{\mathrm c}$.
:::

:::example{#ex-conditional-weight}
1. Taking $B = \{ (\sigma, n) : |\sigma| = n \}$ gives $C(\sigma \mid |\sigma|) \leq^+ |\sigma|$, and part 1 gives, for each $n$, a string $\sigma$ of length $n$ with $C(\sigma \mid n) \geq n$. Knowing the length does not help much: $C(\sigma) \leq^+ C(\sigma \mid |\sigma|) + 2 \log |\sigma|$ for $|\sigma| \geq 2$, by :ref{#prop-conditional-basic} (4), since $C(n) \leq^+ \log n$ (:ref{#ex-conditional-length}).
2. Let $B$ be the set of pairs $(\sigma, \langle n, k \rangle)$ with $|\sigma| = n$ and $k$ ones in $\sigma$. Then $C(\sigma \mid n, k) \leq^+ \log \binom{n}{k}$. With part 1 applied to the set of strings of length $n$ with $k$ ones, this is optimal up to a constant: the conditional complexity given $n$ and $k$ of the most complex such string is $\log \binom{n}{k} \pm O(1)$. This is the counting of :ref{#ex-compressible-strings} (3), now without the cost of coding $n$ and $k$.
:::

## Symmetry of information

The **information in $\tau$ about $\sigma$** is $I(\tau : \sigma) = C(\sigma) - C(\sigma \mid \tau)$. By :ref{#prop-conditional-basic}, $I(\tau : \sigma) \geq -O(1)$, $I(\sigma : \sigma) =^+ C(\sigma)$, and $I(\tau : \sigma) \leq^+ C(\sigma)$. There is no reason, a priori, why $I(\tau : \sigma)$ and $I(\sigma : \tau)$ should be related: a long random string $\sigma$ and its first bit $\tau$ satisfy $C(\tau \mid \sigma) =^+ 0$, so $I(\sigma : \tau) =^+ C(\tau) =^+ 0$; and $I(\tau : \sigma) =^+ 0$ as well, since a description of $\sigma$ given $\tau$ becomes a description of $\sigma$ with one more bit, the value of $\tau$. The information is small in both directions. The symmetry theorem says that this is always the case.

:::theorem[Symmetry of information; Kolmogorov, Levin]{#thm-symmetry-plain}
There is a constant $c$ such that for all strings $\sigma$ and $\tau$, with $m = C(\sigma, \tau)$,
$$
\big| C(\sigma, \tau) - C(\sigma) - C(\tau \mid \sigma) \big| \leq c \log(m + 2).
$$
:::

The upper bound $C(\sigma, \tau) \leq C(\sigma) + C(\tau \mid \sigma) + O(\log m)$ is the easy direction: describe $\sigma$, then describe $\tau$ with $\sigma$ as a condition, and pay a logarithmic term to separate the two descriptions. The lower bound says that this is the best way to describe a pair. Its proof counts. Let $A$ be the finite set of pairs of complexity at most $m$, and $A_\sigma$ the set of second coordinates of the pairs in $A$ with first coordinate $\sigma$. Given $\sigma$ and $m$, the set $A_\sigma$ can be enumerated, so $\tau$ is described given $\sigma$ by its position in $A_\sigma$: $C(\tau \mid \sigma)$ is about $\log |A_\sigma|$. If $A_\sigma$ is large, then $\sigma$ belongs to the set of strings whose section in $A$ is large, and this set is small, since $A$ is: so $C(\sigma)$ is about $m - \log |A_\sigma|$. The two estimates add up to $m$.

:::proof{of=thm-symmetry-plain}
All the constants below are independent of $\sigma$ and $\tau$. We use self-delimiting codes for numbers: the code of $j$ is $\bar\alpha\, 01$, where $\alpha$ is the string of $j$, of length at most $2 \log(j + 1) + 2$.

*Upper bound.* Let $M$ be the machine that, on an input $\bar\alpha\, 01\, \beta$ with $\alpha$ the string of $\ell$, splits $\beta = \beta_0 \beta_1$ with $|\beta_0| = \ell$, computes $\sigma = U(\beta_0)$ and $\tau = U_{\mathrm c}(\beta_1, \sigma)$, and outputs $\langle \sigma, \tau \rangle$. With shortest descriptions $\beta_0$ of $\sigma$ and $\beta_1$ of $\tau$ given $\sigma$,
$$
C(\sigma, \tau) \leq^+ C(\sigma) + C(\tau \mid \sigma) + 2 \log(C(\sigma) + 1) + 2.
$$
Since $\sigma$ is computed from $\langle \sigma, \tau \rangle$, $C(\sigma) \leq^+ m$, and the last term is $O(\log(m + 2))$.

*Lower bound.* Let
$$
A = \{ (\mu, \nu) : C(\mu, \nu) \leq m \}, \qquad A_\mu = \{ \nu : (\mu, \nu) \in A \}.
$$
Then $|A| < 2^{m+1}$, since distinct pairs have distinct shortest descriptions. As $C$ is approximable from above (:ref{#thm-c-not-computable}), $A$ is enumerable uniformly in $m$, and $A_\mu$ uniformly in $m$ and $\mu$. Since $\tau \in A_\sigma$, the set $A_\sigma$ is not empty; let $k$ be such that $2^k \leq |A_\sigma| < 2^{k+1}$. Then $k \leq m$.

*Step 1: $C(\tau \mid \sigma) \leq k + O(\log(m+2))$.* Given $\sigma$, the string $\tau$ is determined by $m$ and by the position $i$ of $\tau$ in the enumeration of $A_\sigma$, with $i < 2^{k+1}$. The conditional machine that, on input $\gamma\, \rho$ with $\gamma$ the self-delimiting code of $m$, enumerates $A_\sigma$ and outputs its element of position the number associated with $\rho$, describes $\tau$ given $\sigma$ with $2 \log(m + 1) + 2 + \lfloor \log(i + 1) \rfloor \leq 2 \log(m + 1) + 3 + k$ bits.

*Step 2: $C(\sigma) \leq m - k + O(\log(m+2))$.* Let $B = \{ \mu : |A_\mu| \geq 2^k \}$. It contains $\sigma$, and it is enumerable from $m$ and $k$: enumerate $A$ and list $\mu$ as soon as $2^k$ pairs with first coordinate $\mu$ have appeared. The sections $A_\mu$ are pairwise disjoint pieces of $A$, so $|B|\, 2^k \leq |A| < 2^{m+1}$, and $|B| < 2^{m + 1 - k}$. The machine that, on input $\gamma\, \gamma'\, \rho$, with $\gamma$ and $\gamma'$ the self-delimiting codes of $m$ and $k$, enumerates $B$ and outputs its element of position the number associated with $\rho$, describes $\sigma$ with at most $4 \log(m + 1) + 4 + (m + 1 - k)$ bits, using $k \leq m$.

Adding the two steps, $C(\sigma) + C(\tau \mid \sigma) \leq m + O(\log(m + 2))$.
:::

:::figure[The counting in the proof of :ref{#thm-symmetry-plain}. The pairs of complexity at most $m$ form a set $A$ of fewer than $2^{m+1}$ points. The section $A_\sigma$ has about $2^k$ points, so $\tau$ needs about $k$ bits given $\sigma$; the first coordinates with a section of at least $2^k$ points are fewer than $2^{m+1-k}$, so $\sigma$ needs about $m - k$ bits.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="A grid of pairs; columns are first coordinates mu; the dots of the set A are scattered; three columns, including the column of sigma, have many dots and are highlighted as the set B; the column of sigma contains tau"><line x1="60" y1="210" x2="560" y2="210" class="axis"/><line x1="60" y1="210" x2="60" y2="30" class="axis"/><text x="566" y="214" class="math" font-size="15">μ</text><text x="48" y="30" text-anchor="end" class="math" font-size="15">ν</text><rect x="148" y="38" width="28" height="166" class="soft-fill"/><rect x="298" y="38" width="28" height="166" class="soft-fill"/><rect x="448" y="38" width="28" height="166" class="soft-fill"/><circle cx="87" cy="186" r="3" class="ink-fill"/><circle cx="87" cy="150" r="3" class="ink-fill"/><circle cx="112" cy="174" r="3" class="ink-fill"/><circle cx="162" cy="198" r="3" class="ink-fill"/><circle cx="162" cy="174" r="3" class="ink-fill"/><circle cx="162" cy="150" r="3" class="ink-fill"/><circle cx="162" cy="126" r="3" class="ink-fill"/><circle cx="162" cy="102" r="3" class="ink-fill"/><circle cx="162" cy="78" r="3" class="ink-fill"/><circle cx="212" cy="186" r="3" class="ink-fill"/><circle cx="237" cy="162" r="3" class="ink-fill"/><circle cx="237" cy="198" r="3" class="ink-fill"/><circle cx="262" cy="138" r="3" class="ink-fill"/><circle cx="312" cy="198" r="3" class="ink-fill"/><circle cx="312" cy="174" r="3" class="ink-fill"/><circle cx="312" cy="150" r="3" class="ink-fill"/><circle cx="312" cy="126" r="5" class="accent-fill"/><circle cx="312" cy="102" r="3" class="ink-fill"/><circle cx="312" cy="78" r="3" class="ink-fill"/><circle cx="312" cy="54" r="3" class="ink-fill"/><circle cx="362" cy="186" r="3" class="ink-fill"/><circle cx="387" cy="150" r="3" class="ink-fill"/><circle cx="412" cy="198" r="3" class="ink-fill"/><circle cx="462" cy="198" r="3" class="ink-fill"/><circle cx="462" cy="162" r="3" class="ink-fill"/><circle cx="462" cy="138" r="3" class="ink-fill"/><circle cx="462" cy="114" r="3" class="ink-fill"/><circle cx="462" cy="90" r="3" class="ink-fill"/><circle cx="462" cy="66" r="3" class="ink-fill"/><circle cx="512" cy="174" r="3" class="ink-fill"/><circle cx="537" cy="198" r="3" class="ink-fill"/><text x="312" y="228" text-anchor="middle" class="math" font-size="14">σ</text><text x="330" y="130" class="math" font-size="14">τ</text><text x="362" y="46" class="label">section A_σ: about 2ᵏ points</text><text x="60" y="244" class="label">shaded columns: B = {μ : |A_μ| ≥ 2ᵏ}, fewer than 2ᵐ⁺¹⁻ᵏ of them</text></svg>
:::

:::quiz[the symmetry of information]
In Step 2 of the proof of :ref{#thm-symmetry-plain}, why is the set $B$ small?

- [x] Its elements have pairwise disjoint sections of at least $2^k$ pairs each inside $A$, and $A$ has fewer than $2^{m+1}$ elements.
- [ ] Because $B$ is enumerable from $m$ and $k$.

  Enumerability is what makes a description by position possible; it says nothing about the size of $B$.
- [ ] Because $\sigma$ has small complexity.

  This is the conclusion of Step 2, obtained from the size of $B$.

---

Why does the description of $\tau$ given $\sigma$ in Step 1 include the number $m$?

- [x] Without $m$, the set $A_\sigma$ is not determined, so the position of $\tau$ in an enumeration of $A_\sigma$ does not determine $\tau$.
- [ ] Because $m$ is needed to compute $\sigma$.

  The string $\sigma$ is the condition, available for free.
- [ ] Because the description must be self-delimiting.

  Plain descriptions need not be self-delimiting; the code of $m$ is self-delimiting only so that the machine can separate it from the position.
:::

The theorem says that a shortest description of a pair can be taken, up to a logarithmic term, as a shortest description of the first coordinate followed by a shortest description of the second given the first. Applied in both orders, since $C(\sigma, \tau) =^+ C(\tau, \sigma)$, it gives the symmetry.

:::corollary[Kolmogorov, Levin]{#cor-symmetry-plain}
$I(\sigma : \tau) = I(\tau : \sigma) \pm O(\log(C(\sigma, \tau) + 2))$, and $I(\sigma : \tau) = I(\tau : \sigma) \pm O(\log n)$ for strings of length at most $n \geq 2$.
:::

:::proof{of=cor-symmetry-plain}
By :ref{#thm-symmetry-plain} applied to $\langle \sigma, \tau \rangle$ and to $\langle \tau, \sigma \rangle$, both $C(\sigma) + C(\tau \mid \sigma)$ and $C(\tau) + C(\sigma \mid \tau)$ are equal to $C(\sigma, \tau)$ up to $O(\log(C(\sigma, \tau) + 2))$. Rearranging, $C(\tau) - C(\tau \mid \sigma)$ and $C(\sigma) - C(\sigma \mid \tau)$ differ by the same amount. For strings of length at most $n$, $C(\sigma, \tau) \leq^+ C(\sigma) + C(\tau) + 2 \log C(\sigma) \leq 3n$ for large $n$, by :ref{#prop-c-pairs}.
:::

The logarithmic term cannot be replaced by a constant. Since $C(\tau \mid \sigma) \leq^+ C(\tau)$, an inequality $C(\sigma, \tau) \leq^+ C(\sigma) + C(\tau \mid \sigma)$ would give $C(\sigma, \tau) \leq^+ C(\sigma) + C(\tau)$, which fails by the counting argument after :ref{#prop-c-pairs}. The source of the defect is the delimitation of the two descriptions; the next lesson removes it with prefix-free complexity, at the price of a different condition.

::::exercise[Incompressible pairs]{#ex-incompressible-pairs difficulty=2 objective="Use symmetry of information to show that the halves of an incompressible pair are incompressible and independent, and conversely."}
Let $\sigma$ and $\tau$ be strings of length $n \geq 2$.

1. Show that if $C(\sigma, \tau) \geq 2n - d$, then $C(\sigma) \geq n - d - O(\log n)$ and $C(\tau \mid \sigma) \geq n - d - O(\log n)$, with constants independent of $n$, $d$, $\sigma$ and $\tau$.
2. Show conversely that if $C(\sigma) \geq n - d$ and $C(\tau \mid \sigma) \geq n - d$, then $C(\sigma, \tau) \geq 2n - 2d - O(\log n)$.

:::solution
Let $e$ be a constant with $C(\rho) \leq |\rho| + e$ and $C(\rho \mid \nu) \leq |\rho| + e$ for all $\rho$ and $\nu$ (:ref{#prop-conditional-basic} (1)). By :ref{#prop-c-pairs}, $C(\sigma, \tau) \leq 2n + 2 \log n + O(1)$, so $\log(C(\sigma, \tau) + 2) \leq \log n + O(1)$, and :ref{#thm-symmetry-plain} reads $C(\sigma, \tau) = C(\sigma) + C(\tau \mid \sigma) \pm O(\log n)$.

1. $C(\sigma) \geq C(\sigma, \tau) - C(\tau \mid \sigma) - O(\log n) \geq 2n - d - (n + e) - O(\log n)$, and symmetrically $C(\tau \mid \sigma) \geq C(\sigma, \tau) - C(\sigma) - O(\log n) \geq n - d - O(\log n)$. Only the upper bound of the theorem is used.
2. $C(\sigma, \tau) \geq C(\sigma) + C(\tau \mid \sigma) - O(\log n) \geq 2n - 2d - O(\log n)$. This direction uses the lower bound of the theorem.

So, up to logarithmic terms, a pair of strings of length $n$ is incompressible exactly when its first half is incompressible and its second half is incompressible given the first. The analogue for infinite sequences is van Lambalgen's theorem, in the course on notions of randomness.
:::
::::

## Notes and references

Conditional complexity is in Kolmogorov's 1965 paper, which defines complexity directly in conditional form. The counting bounds are from the same paper (Downey–Hirschfeldt, Theorem 3.2.2). The symmetry of information was proved by Kolmogorov and Levin; the first published account is Zvonkin and Levin (1970), and the proof given here is the one of Li and Vitányi, as in Downey and Hirschfeldt (Theorem 3.3.2). Downey and Hirschfeldt define conditional complexity with the condition as an oracle; the definition with a second argument, used here and by Li and Vitányi, gives the same function up to an additive constant.

- A. N. Kolmogorov, *Three approaches to the quantitative definition of information*, Problems of Information Transmission 1 (1965), 1–7.
- A. K. Zvonkin and L. A. Levin, *The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms*, Russian Mathematical Surveys 25 (1970), 83–124.
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, 3rd edition, Springer, 2008, Section 2.8.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.2 and 3.3.
- A. Shen, V. A. Uspensky and N. Vereshchagin, *Kolmogorov Complexity and Algorithmic Randomness*, American Mathematical Society, 2017, Chapter 2.

:::::exercises
::::exercise{#ex-information-bounds difficulty=1 objective="Check the elementary bounds on the information in one string about another."}
Show that $I(\tau : \sigma) \geq -O(1)$, $I(\tau : \sigma) \leq^+ C(\sigma)$, and $I(\sigma : \sigma) =^+ C(\sigma)$. Show that $I(\tau : \sigma) \geq^+ C(\sigma)$ when $\sigma = f(\tau)$ for a fixed partial computable function $f$.

:::solution
By :ref{#prop-conditional-basic} (1), $C(\sigma \mid \tau) \leq^+ C(\sigma)$, so $I(\tau : \sigma) = C(\sigma) - C(\sigma \mid \tau) \geq -O(1)$; and $C(\sigma \mid \tau) \geq 0$ gives $I(\tau : \sigma) \leq C(\sigma)$. Since $C(\sigma \mid \sigma) =^+ 0$, $I(\sigma : \sigma) =^+ C(\sigma)$. If $\sigma = f(\tau)$, the conditional machine $(\rho, \nu) \mapsto f(\nu)$ describes $\sigma$ given $\tau$ with the empty string, so $C(\sigma \mid \tau) =^+ 0$ and $I(\tau : \sigma) =^+ C(\sigma)$.
:::
::::

::::exercise{#ex-conditional-length difficulty=1 objective="Compare conditional and unconditional complexity when the condition is the length."}
Show that $C(\sigma \mid |\sigma|) \leq^+ C(\sigma)$, and that $C(\sigma) \leq^+ C(\sigma \mid |\sigma|) + 2 \log |\sigma|$ for $|\sigma| \geq 2$. Show that for every $n$ some string $\sigma$ of length $n$ satisfies $C(\sigma \mid n) \geq n$, and that every such string satisfies $C(\sigma) \geq n - O(1)$.

:::solution
The first inequality is :ref{#prop-conditional-basic} (1). For the second, let $n = |\sigma| \geq 2$. By :ref{#prop-conditional-basic} (4) with $\tau = n$, $C(\sigma) \leq^+ C(\sigma \mid n) + C(n) + 2 \log C(n)$, where $\log 0$ is read as $0$. By :ref{#prop-c-basic} (3), $C(n) \leq^+ \log n$, so $2 \log C(n) \leq 2 \log \log n + O(1)$, and $\log n + 2 \log \log n \leq 2 \log n + O(1)$.

By :ref{#thm-conditional-counting} (1) with $\tau = n$ and $k = 0$, fewer than $2^n$ strings have $C(\sigma \mid n) < n$, so one of the $2^n$ strings of length $n$ has $C(\sigma \mid n) \geq n$. For such a string, $C(\sigma) \geq C(\sigma \mid n) - O(1) \geq n - O(1)$ by the first inequality. So incompressibility given the length implies incompressibility, while the converse holds up to the logarithmic term of the second inequality.
:::
::::

::::exercise{#ex-chain-three difficulty=2 objective="Iterate the symmetry of information to decompose the complexity of a triple."}
Show that $C(\sigma, \tau, \rho) = C(\sigma) + C(\tau \mid \sigma) + C(\rho \mid \sigma, \tau) \pm O(\log(m + 2))$, where $m = C(\sigma, \tau, \rho)$ and $C(\sigma, \tau, \rho) = C(\langle \sigma, \langle \tau, \rho \rangle \rangle)$.

:::solution
The maps between $\langle \sigma, \langle \tau, \rho \rangle \rangle$ and $\langle \langle \sigma, \tau \rangle, \rho \rangle$ are computable in both directions, so the two strings have the same complexity up to a constant, by :ref{#prop-conditional-basic} (2). By :ref{#thm-symmetry-plain} applied to the pair $(\langle \sigma, \tau \rangle, \rho)$,
$$
C(\sigma, \tau, \rho) = C(\sigma, \tau) + C(\rho \mid \sigma, \tau) \pm O(\log(m + 2)).
$$
By the theorem applied to $(\sigma, \tau)$, $C(\sigma, \tau) = C(\sigma) + C(\tau \mid \sigma) \pm O(\log(C(\sigma, \tau) + 2))$, and $C(\sigma, \tau) \leq^+ m$, since $\langle \sigma, \tau \rangle$ is computed from the triple. Substituting gives the claim, with $\log(C(\sigma, \tau) + 2) \leq \log(m + 2) + O(1)$.
:::
::::

::::exercise[Binomial coding]{#ex-binomial-coding difficulty=2 objective="Apply the counting bounds of conditional complexity to strings with a prescribed number of ones."}
Let $n \geq 2$ and $0 \leq k \leq n$. Show that every string $\sigma$ of length $n$ with $k$ ones satisfies $C(\sigma) \leq \log \binom{n}{k} + O(\log n)$, and that some such string satisfies $C(\sigma) \geq \log \binom{n}{k} - O(1)$, with constants independent of $n$ and $k$.

:::solution
By :ref{#ex-conditional-weight} (2), $C(\sigma \mid n, k) \leq^+ \log \binom{n}{k}$. By :ref{#prop-conditional-basic} (4), $C(\sigma) \leq^+ C(\sigma \mid n, k) + C(n, k) + 2 \log C(n, k)$. The number $N = n(n + 1) + k$ determines $n$ and $k$, since $0 \leq k \leq n$ places $N$ in the interval $[n(n+1), n(n+1) + n]$, and these intervals are disjoint for distinct $n$; so $\langle n, k \rangle$ is a computable function of $N$, and $C(n, k) \leq^+ C(N) \leq^+ \log N \leq 2 \log(n + 1)$ by :ref{#prop-c-basic}. Hence $C(\sigma) \leq \log \binom{n}{k} + 2 \log(n + 1) + 2 \log \log (n+1) + O(1)$, which is $\log \binom{n}{k} + O(\log n)$.

For the lower bound, the set of strings of length $n$ with $k$ ones has $\binom{n}{k}$ elements, so by :ref{#thm-conditional-counting} (1) one of them satisfies $C(\sigma \mid n, k) \geq \lfloor \log \binom{n}{k} \rfloor$. By :ref{#prop-conditional-basic} (1), $C(\sigma) \geq C(\sigma \mid n, k) - O(1) \geq \log \binom{n}{k} - O(1)$. So the largest complexity of a string of length $n$ with $k$ ones is $\log \binom{n}{k}$ up to $O(\log n)$.
:::
::::
:::::
