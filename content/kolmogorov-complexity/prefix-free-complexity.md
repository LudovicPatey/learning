---
title: Prefix-free complexity
summary: Machines whose domain is prefix-free; the optimal prefix-free machine and the complexity K; subadditivity, the Kraft inequality, and the comparison between K and C.
duration: 45
prerequisites: [computable-sequences]
---

The defects of plain complexity, the logarithmic cost of pairs and the oscillation of initial segments, have a common cause: a description of length $\ell$ conveys, besides its bits, the number $\ell$. In the proof of the oscillation theorem, this hidden information is exactly what compresses the initial segment. Levin and Chaitin proposed to restrict descriptions to **self-delimiting** ones: a machine reads its input bit by bit from a tape with no end marker and decides by itself when to stop reading, so that its output cannot depend on the length of the input beyond what the bits read so far tell. The descriptions of such a machine then form a prefix-free set: no description is a proper prefix of another, since the machine stops at the shorter one before reading further. The resulting complexity $K$ exceeds $C$ by at most a logarithmic term, but it is subadditive, its values satisfy the Kraft inequality, and it gives a definition of random sequences.

## Prefix-free machines

:::definition{#def-prefix-free-machine}
A set of strings $W$ is **prefix-free** if no element of $W$ is a proper prefix of another element of $W$. A machine $M$ is **prefix-free** if its domain is prefix-free. For a prefix-free machine $M$, we write $K_M(\sigma) = C_M(\sigma)$.
:::

The sets $\{ 0^n 1 : n \in \nat \}$ and $\{ \bar\rho\, 01 : \rho \in \bstr \}$, with $\bar\rho$ the string $\rho$ with each bit doubled, are prefix-free. The set of all strings, and any set containing both $\sigma$ and $\sigma 0$, are not. For instance, the machine $\bar\rho\, 01 \mapsto \rho$ is prefix-free and describes every string $\rho$ with $2|\rho| + 2$ bits, while the identity machine, which gives plain complexity its bound $|\sigma|$, is not prefix-free.

A prefix-free set $W$ corresponds to pairwise disjoint cylinders $[\tau] = \{ X \in \cs : \tau \prec X \}$, $\tau \in W$, or equivalently to pairwise disjoint dyadic intervals of $[0, 1]$, the interval of $\tau$ being the set of reals with a binary expansion beginning with $\tau$, of length $2^{-|\tau|}$. The **weight** of $W$ is $\sum_{\tau \in W} 2^{-|\tau|}$, the total length of these intervals.

:::figure[The prefix-free set $\{00, 010, 10, 110\}$ and its dyadic intervals. Its weight is $\tfrac14 + \tfrac18 + \tfrac14 + \tfrac18 = \tfrac34$.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="The prefix-free set 00, 010, 10, 110 as leaves of the binary tree, and the corresponding disjoint dyadic intervals of the unit interval, of total length 3/4"><line x1="300.0" y1="24" x2="170.0" y2="68" class="ink-stroke" stroke-width="1.2"/><line x1="300.0" y1="24" x2="430.0" y2="68" class="ink-stroke" stroke-width="1.2"/><line x1="170.0" y1="68" x2="105.0" y2="112" class="ink-stroke" stroke-width="1.2"/><line x1="170.0" y1="68" x2="235.0" y2="112" class="ink-stroke" stroke-width="1.2"/><line x1="430.0" y1="68" x2="365.0" y2="112" class="ink-stroke" stroke-width="1.2"/><line x1="430.0" y1="68" x2="495.0" y2="112" class="ink-stroke" stroke-width="1.2"/><line x1="235.0" y1="112" x2="202.5" y2="156" class="ink-stroke" stroke-width="1.2"/><line x1="235.0" y1="112" x2="267.5" y2="156" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="495.0" y1="112" x2="462.5" y2="156" class="ink-stroke" stroke-width="1.2"/><line x1="495.0" y1="112" x2="527.5" y2="156" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="300.0" cy="24" r="3.5" class="ink-fill"/><circle cx="170.0" cy="68" r="3.5" class="ink-fill"/><circle cx="430.0" cy="68" r="3.5" class="ink-fill"/><circle cx="105.0" cy="112" r="6" class="node"/><text x="105.0" y="134" text-anchor="middle" class="mrm" font-size="12">00</text><line x1="105.0" y1="140" x2="105.0" y2="196" class="muted-stroke" stroke-dasharray="2 3"/><circle cx="235.0" cy="112" r="3.5" class="ink-fill"/><circle cx="365.0" cy="112" r="6" class="node"/><text x="365.0" y="134" text-anchor="middle" class="mrm" font-size="12">10</text><line x1="365.0" y1="140" x2="365.0" y2="196" class="muted-stroke" stroke-dasharray="2 3"/><circle cx="495.0" cy="112" r="3.5" class="ink-fill"/><circle cx="202.5" cy="156" r="6" class="node"/><text x="202.5" y="178" text-anchor="middle" class="mrm" font-size="12">010</text><line x1="202.5" y1="184" x2="202.5" y2="196" class="muted-stroke" stroke-dasharray="2 3"/><circle cx="267.5" cy="156" r="3.5" class="muted-fill"/><circle cx="462.5" cy="156" r="6" class="node"/><text x="462.5" y="178" text-anchor="middle" class="mrm" font-size="12">110</text><line x1="462.5" y1="184" x2="462.5" y2="196" class="muted-stroke" stroke-dasharray="2 3"/><circle cx="527.5" cy="156" r="3.5" class="muted-fill"/><text x="310.0" y="20" class="mrm" font-size="13">ε</text><rect x="40" y="198" width="520" height="22" class="cell"/><rect x="41.0" y="198" width="128.0" height="22" class="cell head-cell"/><text x="105.0" y="213" text-anchor="middle" class="mrm" font-size="11">2⁻²</text><rect x="171.0" y="198" width="63.0" height="22" class="cell head-cell"/><text x="202.5" y="213" text-anchor="middle" class="mrm" font-size="11">2⁻³</text><rect x="301.0" y="198" width="128.0" height="22" class="cell head-cell"/><text x="365.0" y="213" text-anchor="middle" class="mrm" font-size="11">2⁻²</text><rect x="431.0" y="198" width="63.0" height="22" class="cell head-cell"/><text x="462.5" y="213" text-anchor="middle" class="mrm" font-size="11">2⁻³</text><text x="40.0" y="236" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="300.0" y="236" text-anchor="middle" class="mrm muted" font-size="11">1/2</text><text x="560.0" y="236" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="40" y="260" class="label">The interval of τ is the set of reals whose binary expansion begins with τ;</text><text x="40" y="276" class="label">the intervals of a prefix-free set are disjoint, so their lengths add up to at most 1 (here 3/4).</text></svg>
:::

:::proposition[Kraft inequality]{#prop-kraft}
The weight of a prefix-free set of strings is at most $1$.
:::

:::proof{of=prop-kraft}
It suffices to treat finite prefix-free sets $W$. Let $\ell$ be larger than the length of every element of $W$. The sets $\{ \rho \in \{0,1\}^\ell : \tau \preceq \rho \}$, for $\tau \in W$, are pairwise disjoint, since a string $\rho$ extending two elements of $W$ would make them comparable; and the one indexed by $\tau$ has $2^{\ell - |\tau|}$ elements. So $\sum_{\tau \in W} 2^{\ell - |\tau|} \leq 2^\ell$.
:::

Conversely, Kraft observed that for every sequence of lengths $\ell_0, \ell_1, \dots$ with $\sum_i 2^{-\ell_i} \leq 1$, there is a prefix-free sequence of strings $\tau_i$ with $|\tau_i| = \ell_i$. When the lengths are sorted, $\ell_0 \leq \ell_1 \leq \cdots$, one takes for $\tau_i$ the first $\ell_i$ bits of the binary expansion of $\sum_{j < i} 2^{-\ell_j}$: the intervals are placed side by side from left to right. For instance, the lengths $1, 2, 3, 3$ give $0, 10, 110, 111$. An effective version, in which the lengths arrive one at a time in any order, is the KC theorem of :ref{to="kolmogorov-complexity/kc-theorem"}; it is the main tool for building prefix-free machines.

To build an optimal prefix-free machine, one would like to imitate the invariance theorem with an enumeration of the prefix-free machines. Whether a machine is prefix-free is not decidable from its index, so the proof uses all machines and trims each of them to a prefix-free one: a description is accepted only if it is incomparable with all the descriptions accepted before it, in the order in which computations converge. A prefix-free machine is left unchanged by this operation.

:::theorem{#thm-optimal-prefix-free}
There is a prefix-free machine $U$ that is **optimal among prefix-free machines**: for every prefix-free machine $M$, $K_U \leq^+ K_M$.
:::

:::proof{of=thm-optimal-prefix-free}
We first transform every machine into a prefix-free one, without changing prefix-free machines. Given an index $e$, let $\hat M_e$ be the machine that, on input $\sigma$, enumerates the domain of $M_e$ in order of convergence, using a fixed dovetailing of the computations $M_e(\tau)[s]$, and keeps a list $L$ of the strings enumerated so far that have been **accepted**. A newly enumerated string is accepted if it is incomparable with every string already accepted. $\hat M_e(\sigma)$ converges, with value $M_e(\sigma)$, if and only if $\sigma$ is enumerated and accepted.

The set of accepted strings is prefix-free, by construction, and it is the domain of $\hat M_e$; the acceptance of a string does not depend on the input $\sigma$, since the enumeration is the same for all inputs. If the domain of $M_e$ is prefix-free, every enumerated string is accepted, and $\hat M_e = M_e$. An index of $\hat M_e$ is computable from $e$.

Let $U(0^e 1 \tau) = \hat M_e(\tau)$. The domain of $U$ is the union of the sets $0^e 1\, \mathrm{dom}(\hat M_e)$, which are prefix-free and pairwise incomparable for different $e$; so $U$ is prefix-free. If $M = M_e$ is prefix-free, $K_U(\sigma) \leq K_M(\sigma) + e + 1$.
:::

We fix such a machine $U$ and write $K(\sigma) = K_U(\sigma)$, the **prefix-free complexity** of $\sigma$. As for $C$, statements of the form $f \leq^+ g$ about $K$ do not depend on the choice of $U$, and $K(n)$ denotes the complexity of the string associated with $n$. The proofs of :ref{#prop-c-basic} (2) and of :ref{#thm-c-not-computable} carry over: $K(f(\sigma)) \leq^+ K(\sigma)$ for partial computable $f$, since the domain of the machine $\tau \mapsto f(U(\tau))$ is contained in that of $U$, hence prefix-free; $K$ is not computable; and $K$ is approximable from above, with the computable bound $K(\sigma) \leq 2|\sigma| + d$, given by the prefix-free machine $\bar\rho\, 01 \mapsto \rho$, in place of $C(\sigma) \leq |\sigma| + d$.

:::quiz[prefix-free machines]
In the proof of :ref{#thm-optimal-prefix-free}, why does $\hat M_e$ enumerate the whole domain of $M_e$, instead of only checking the computations on its own input $\sigma$ and on the prefixes of $\sigma$?

- [x] Because the decision to accept $\sigma$ must be the same in every run, and must take into account extensions of $\sigma$ as well as prefixes; a global enumeration, identical for all inputs, guarantees both.

  A check limited to prefixes would accept both $\sigma$ and an extension $\tau$ of $\sigma$ when $M_e(\tau)$ converges before $M_e(\sigma)$.
- [ ] Because the domain of $M_e$ is computable.

  It is only c.e.; this is why its elements are enumerated in order of convergence.
- [ ] To make $\hat M_e$ total.

  $\hat M_e$ is partial in general.
:::

## Properties of K

:::proposition{#prop-k-basic}
1. $K(\langle \sigma, \tau \rangle) \leq^+ K(\sigma) + K(\tau)$.
2. $K(\sigma) \leq^+ |\sigma| + K(|\sigma|)$, and $K(\sigma) \leq^+ |\sigma| + 2 \log |\sigma|$ for $|\sigma| \geq 2$.
3. $C(\sigma) \leq^+ K(\sigma)$, and $K(\sigma) \leq^+ C(\sigma) + K(C(\sigma)) \leq^+ C(\sigma) + 2 \log C(\sigma)$, where $\log 0$ is read as $0$.
4. $\sum_\sigma 2^{-K(\sigma)} \leq 1$.
:::

:::proof{of=prop-k-basic}
1. Let $M$ be the machine that, on input $\alpha$, searches for a decomposition $\alpha = \alpha_0 \alpha_1$ with $\alpha_0, \alpha_1$ in the domain of $U$, and outputs $\langle U(\alpha_0), U(\alpha_1) \rangle$. The decomposition is unique when it exists, since the domain of $U$ is prefix-free; it is found by enumerating the domain of $U$ and testing the prefixes of $\alpha$. The domain of $M$ is prefix-free: if $\alpha_0\alpha_1$ and $\alpha_0'\alpha_1'$ are both in it and comparable, then $\alpha_0$ and $\alpha_0'$ are comparable elements of the domain of $U$, hence equal, and then $\alpha_1$ and $\alpha_1'$ are comparable, hence equal. Concatenating shortest descriptions of $\sigma$ and $\tau$ gives $K_M(\langle \sigma, \tau \rangle) \leq K(\sigma) + K(\tau)$.
2. The machine that, on input $\alpha_0 \alpha_1$ with $\alpha_0$ in the domain of $U$ and $|\alpha_1| = U(\alpha_0)$, read as a number, outputs $\alpha_1$, is prefix-free, by the same argument as in 1. It gives the first inequality. For the second, $K(n) \leq^+ 2 \log n$ for $n \geq 2$: the prefix-free machine $\bar\rho\, 01 \mapsto \rho$ describes the string $\rho$ associated with $n$ with $2|\rho| + 2$ bits.
3. $U$ is a machine, so $C \leq^+ K_U = K$. For the second inequality, let $M$ be the machine that, on input $\alpha_0 \alpha_1$ with $\alpha_0$ in the domain of $U$ and $|\alpha_1| = U(\alpha_0)$, outputs $V(\alpha_1)$, where $V$ is the optimal plain machine defining $C$. It is prefix-free, and a shortest $U$-description of the number $C(\sigma)$ followed by a shortest $V$-description of $\sigma$ is an $M$-description of $\sigma$. The last inequality follows from the bound $K(n) \leq^+ 2 \log n$ of 2, the finitely many strings with $C(\sigma) \leq 1$ being absorbed in the constant.
4. The shortest $U$-descriptions of distinct strings are distinct elements of the domain of $U$, so the sum is at most the weight of the domain of $U$, which is at most $1$ by :ref{#prop-kraft}.
:::

Property 4 is the essential difference with plain complexity: $\sum_\sigma 2^{-C(\sigma)}$ diverges, since there are $2^n$ strings of length $n$ with $C(\sigma) \leq^+ n$, so that the sum over each length is bounded from below by a positive constant. It implies that $K$ exceeds the length infinitely often.

:::corollary{#cor-k-above-length}
For every $c$ there is a string $\sigma$ with $K(\sigma) > |\sigma| + c$. More precisely, for every $n$ there is a string of length $n$ with $K(\sigma) \geq n + K(n) - d$, for a constant $d$ independent of $n$.
:::

:::proof{of=cor-k-above-length}
For the first statement: if $K(\sigma) \leq |\sigma| + c$ for every $\sigma$, then $\sum_{|\sigma| = n} 2^{-K(\sigma)} \geq 2^{-c}$ for every $n$, and the sum over all lengths diverges, contradicting :ref{#prop-k-basic} (4). The second statement is :ref{#thm-k-counting}, proved in the last lesson of the course with the coding theorem.
:::

By :ref{#prop-k-basic} (2) and the corollary, the maximal complexity of a string of length $n$ is $n + K(n) + O(1)$, and it exceeds $n$ by an unbounded amount, since $K(n)$ is unbounded. The term $K(n)$ is the cost of self-delimitation: a prefix-free description of $\sigma$ must also determine where it ends, which requires information about $|\sigma|$.

:::quiz[properties of K]
In the proof of :ref{#prop-k-basic} (1), where is the prefix-freeness of $U$ used?

- [x] To make the decomposition $\alpha = \alpha_0\alpha_1$ unique, and to show that the new machine is again prefix-free.
- [ ] To show that $\langle \sigma, \tau \rangle$ is computable from $\sigma$ and $\tau$.

  The pairing function is computable regardless of $U$.
- [ ] To bound $K(\sigma)$ by $|\sigma|$.

  No such bound holds for $K$; :ref{#cor-k-above-length} shows that $K(\sigma) > |\sigma| + c$ for some $\sigma$.

---

Why does $\sum_\sigma 2^{-C(\sigma)}$ diverge?

- [x] Because for each $n$, the $2^n$ strings of length $n$ have $C(\sigma) \leq n + d$, so their contribution is at least $2^{-d}$, and there are infinitely many lengths.
- [ ] Because $C$ is not computable.

  $K$ is not computable either, and its sum converges.
- [ ] Because $C(\sigma) \geq |\sigma|$ for some $\sigma$ of each length.

  This gives a lower bound on $C$, hence an upper bound on the terms; it does not cause divergence.
:::

## Prefix-free complexity of initial segments

The proof of :ref{#thm-oscillation} does not carry over to $K$: the machine in its proof, $\alpha \mapsto \beta\alpha$, is not prefix-free, since it accepts every string. In the next course, a sequence $X$ is called **random** when $K(X \uh n) \geq n - c$ for some constant $c$ and every $n$. That course proves that such sequences exist, and in fact that almost every sequence, in the sense of the uniform measure, is random; the last lesson of this course gives an example, Chaitin's number $\Omega$. Computable sequences are far from random, since $K(X \uh n) \leq^+ K(n) \leq^+ 2 \log n$.

:::proposition{#prop-k-segments-computable}
If $X$ is computable, then $K(X \uh n) =^+ K(n)$.
:::

:::proof{of=prop-k-segments-computable}
As for :ref{#prop-computable-segments}: $n \mapsto X \uh n$ and $\sigma \mapsto |\sigma|$ are computable, and partial computable functions do not increase $K$ by more than a constant.
:::

Unlike the case of $C$ (:ref{#thm-chaitin-computable}), the converse fails: there are non-computable sequences with $K(X \uh n) \leq^+ K(n)$, the **K-trivial** sequences, a central topic of the theory of algorithmic randomness.

## Exercises

::::exercise{difficulty=1}
Show that $K(\sigma\tau) \leq^+ K(\sigma) + K(\tau)$. Show that $K$ is not monotone up to a constant on numbers: there are pairs $n_j \leq m_j$ with $K(m_j) - K(n_j)$ tending to $-\infty$.

:::solution
The first inequality follows from :ref{#prop-k-basic} (1), since $\langle \sigma, \tau \rangle \mapsto \sigma\tau$ is computable. For the second, let $n_j$ be a number whose associated string $\sigma$ has length $j$ and satisfies $C(\sigma) \geq j$, by :ref{#prop-incompressible-count}; then $K(\sigma) \geq j - d$ for a constant $d$, by :ref{#prop-k-basic} (3). Such numbers lie between $2^j - 1$ and $2^{j+1} - 2$. Let $m_j = 2^{j+1}$, computable from $j$, so that $K(m_j) \leq^+ K(j) \leq^+ 2 \log j$ for $j \geq 2$. Then $K(m_j) - K(n_j) \leq 2 \log j - j + O(1)$ tends to $-\infty$.
:::
::::

::::exercise{difficulty=2}
Show that $K(\sigma) \leq^+ |\sigma| + \log |\sigma| + 2 \log \log |\sigma|$ for $|\sigma| \geq 4$, and more generally that every iteration of the bound $K(n) \leq^+ \log n + K(\lfloor \log n \rfloor)$ improves the upper bound on $K(\sigma)$.

:::solution
By :ref{#prop-k-basic} (2) applied to the string associated with $n$, of length $\ell = \lfloor \log(n+1) \rfloor$, $K(n) \leq^+ \ell + K(\ell) \leq^+ \log n + K(\ell)$. Applying (2) again to $K(\ell)$ with the bound $2 \log$ gives $K(n) \leq^+ \log n + 2 \log \log n$ for $n \geq 4$. Then $K(\sigma) \leq^+ |\sigma| + K(|\sigma|) \leq^+ |\sigma| + \log |\sigma| + 2 \log \log |\sigma|$. Iterating, $K(\sigma) \leq^+ |\sigma| + \log |\sigma| + \log \log |\sigma| + \cdots$, each stage replacing a term $2 \log^{(k)}$ by $\log^{(k)} + 2 \log^{(k+1)}$.
:::
::::

## Notes and references

Prefix-free complexity was introduced by Levin (1974) and Chaitin (1975), with a related notion due to Gács. The Kraft inequality and its converse for sorted lengths are due to Kraft (1949). The bound $K \leq^+ C + K(C)$ is Proposition 2.4.1 of Nies's book, and $K(\sigma) \leq^+ |\sigma| + K(|\sigma|)$ is due to Chaitin (Downey–Hirschfeldt, Theorem 3.7.4). The definition of randomness through $K$ and its equivalence with Martin-Löf randomness are due to Levin, Schnorr and Chaitin, and are treated in the next course. K-trivial sequences were introduced by Chaitin and studied by Solovay, and later by Downey, Hirschfeldt, Nies and Stephan.

- L. A. Levin, *Laws of information conservation (nongrowth) and aspects of the foundation of probability theory*, Problems of Information Transmission 10 (1974), 206–210.
- G. J. Chaitin, *A theory of program size formally identical to information theory*, Journal of the ACM 22 (1975), 329–340.
- L. G. Kraft, *A device for quantizing, grouping, and coding amplitude modulated pulses*, Master's thesis, MIT, 1949.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.5 and 3.7.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 2.2 and 2.4.
