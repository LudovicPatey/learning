---
title: Randomness for computable measures
summary: Martin-Löf randomness for a computable probability measure on Cantor space; atoms are computable; the representation of reals by sequences relative to a measure; a non-computable sequence random for a computable measure is Turing equivalent to a random sequence for the uniform measure (Levin, Kautz).
duration: 35
prerequisites: [ce-sets, martin-lof-randomness/martin-lof-tests, pi01-classes/computable-members]
---

The uniform measure models a fair coin. A biased coin, which shows $1$ with probability $p$, gives another measure on Cantor space, and another notion of randomness: a sequence random for the biased coin has a frequency of $1$s equal to $p$, so it is not random for the fair coin. Randomness depends on the measure. But computational properties do not, as long as the measure is computable and has no atoms: Levin and Kautz showed that the Turing degrees of the random sequences are the same for every computable continuous measure. The tool is a representation of reals by sequences adapted to the measure, which turns a sequence random for one measure into a real random for the uniform measure, of the same Turing degree.

This lesson develops the part of the theory that the next lesson uses, to prove Demuth's theorem: the image of a random sequence by a truth-table functional is random for the image measure, and hence Turing equivalent to a random sequence for the uniform measure.

## Computable measures

:::definition{#def-computable-measure}
A **premeasure** is a function $\rho : \bstr \to [0, 1]$ with $\rho(\varepsilon) = 1$ and $\rho(\sigma) = \rho(\sigma 0) + \rho(\sigma 1)$ for every $\sigma$. It is **computable** if $\rho(\sigma)$ is a computable real uniformly in $\sigma$. The **measure** $\nu$ of $\rho$ is the unique countably additive function on the Borel classes with $\nu([\sigma]) = \rho(\sigma)$ for every $\sigma$; a measure of this form, with $\rho$ computable, is a **computable measure**.
:::

The existence and uniqueness of $\nu$ are admitted, as for the uniform measure (:ref{#fact-lebesgue-measure}). Examples:

1. The uniform measure $\lambda$, with $\rho(\sigma) = 2^{-|\sigma|}$.
2. For a computable real $p \in [0, 1]$, the **Bernoulli measure** $\mu_p$, with $\rho(\sigma) = p^{k}(1-p)^{|\sigma| - k}$, where $k$ is the number of $1$s in $\sigma$.
3. The measure concentrated on a computable sequence $Z$: $\rho(\sigma) = 1$ if $\sigma \prec Z$ and $0$ otherwise.
4. The image of $\lambda$ by a truth-table functional, in the next lesson.

A **Martin-Löf $\nu$-test** is a uniformly $\Sigma^0_1$ sequence of classes $(\mathcal U_n)$ with $\nu(\mathcal U_n) \leq 2^{-n}$, and a sequence is **$\nu$-random** if it is captured by no Martin-Löf $\nu$-test. When $\nu$ is computable, the measure of a $\Sigma^0_1$ class is a left-c.e. real, uniformly, as in :ref{#prop-measure-effective}, and the proof of :ref{#thm-universal-test} gives a universal $\nu$-test; we do not need it. The $\nu$-random sequences form a class of $\nu$-measure $1$.

An **atom** of $\nu$ is a sequence $A$ with $\nu(\{A\}) > 0$, that is, $\lim_n \nu([A \uh n]) > 0$. A measure without atoms is **continuous**. Every atom is $\nu$-random: a test capturing $A$ would have $\nu(\mathcal U_n) \geq \nu(\{A\}) > 0$ for every $n$. In example 3, the computable sequence $Z$ is $\nu$-random. This is the only way a computable sequence can be random.

:::lemma[Levin, Kautz]{#lem-atoms-computable}
Let $\nu$ be a computable measure. Every atom of $\nu$ is computable. Equivalently, if $A$ is not computable, then $\nu([A \uh n]) \to 0$.
:::

:::proof{of=lem-atoms-computable}
Suppose that $\nu([A \uh n]) > \varepsilon$ for every $n$, for a rational $\varepsilon > 0$. Let $\rho_s(\sigma)$ be a rational with $|\rho(\sigma) - \rho_s(\sigma)| < 2^{-s}$, computable from $s$ and $\sigma$, and let $T = \{ \sigma : \rho_{|\tau|}(\tau) > \varepsilon - 2^{-|\tau|} \text{ for every } \tau \preceq \sigma \}$. It is a computable tree, and $A$ is a path of $T$, since $\rho_n(A \uh n) > \rho(A \uh n) - 2^{-n} > \varepsilon - 2^{-n}$. Every path $B$ of $T$ satisfies $\rho(B \uh n) > \varepsilon - 2^{-n+1}$ for every $n$, so $\nu(\{B\}) \geq \varepsilon$. Distinct paths have disjoint singletons, so $T$ has at most $1/\varepsilon$ paths. A finite $\Pi^0_1$ class has only isolated members, and isolated members of $\Pi^0_1$ classes are computable (:ref{to="pi01-classes/computable-members"}). So $A$ is computable.
:::

## Representing reals relative to a measure

The binary expansion of a real $\alpha$ records, at each step, in which half of the current dyadic interval $\alpha$ lies. Relative to a measure $\nu$, the interval is divided in proportion to the measure.

:::definition{#def-nu-interval}
Let $\nu$ be a computable measure with premeasure $\rho$. For a string $\sigma$ of length $n$, let $l_\sigma = \sum \{ \rho(\tau) : |\tau| = n,\ \tau <_{\mathrm{lex}} \sigma \}$ and let $(\sigma)_\nu = [l_\sigma, l_\sigma + \rho(\sigma)]$. For a real $\alpha \in [0, 1]$, if for every $n$ there is a unique string $\sigma$ of length $n$ with $\alpha \in (\sigma)_\nu$, the sequence $A$ with $\alpha \in (A \uh n)_\nu$ for every $n$ is the **$\nu$-representation** of $\alpha$, written $A = \mathrm{seq}_\nu(\alpha)$.
:::

For each $n$, the intervals $(\sigma)_\nu$ with $|\sigma| = n$ have lengths $\rho(\sigma)$, lie side by side in lexicographic order, and cover $[0, 1]$; the interval $(\sigma)_\nu$ is split into $(\sigma 0)_\nu$ and $(\sigma 1)_\nu$ at the point $l_{\sigma 1} = l_\sigma + \rho(\sigma 0)$. The endpoints $l_\sigma$ are computable reals, uniformly in $\sigma$. A real that is not one of these endpoints lies in the interior of exactly one interval of each length, and these intervals are nested; so $\mathrm{seq}_\nu(\alpha)$ is defined for every real $\alpha$ different from all the $l_\sigma$, in particular for every non-computable $\alpha$. For the uniform measure, $(\sigma)_\lambda$ is the dyadic interval of $\sigma$, and $\mathrm{seq}_\lambda(\alpha)$ is the binary expansion of $\alpha$.

:::figure[The $\nu$-representation for the Bernoulli measure $\mu_{2/3}$, where $1$ has probability $2/3$. The first bit of the representation of $\alpha$ is $1$ because $\alpha \in [1/3, 1]$, the second is $0$ because $\alpha \in [1/3, 5/9]$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The unit interval divided at one third into the intervals of 0 and 1, and the interval of 1 divided at five ninths into the intervals of 10 and 11; a point alpha in the interval of 10"><line x1="40" y1="50" x2="560" y2="50" class="axis"/><rect x="40" y="40" width="173" height="20" class="cell"/><rect x="213" y="40" width="347" height="20" class="cell head-cell"/><text x="126" y="55" text-anchor="middle" class="mrm" font-size="12">(0)</text><text x="386" y="55" text-anchor="middle" class="mrm" font-size="12">(1)</text><rect x="213" y="90" width="116" height="20" class="soft-fill"/><rect x="329" y="90" width="231" height="20" class="cell"/><text x="271" y="105" text-anchor="middle" class="mrm" font-size="12">(10)</text><text x="444" y="105" text-anchor="middle" class="mrm" font-size="12">(11)</text><text x="40" y="80" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="213" y="80" text-anchor="middle" class="mrm muted" font-size="11">1/3</text><text x="329" y="130" text-anchor="middle" class="mrm muted" font-size="11">5/9</text><text x="560" y="80" text-anchor="middle" class="mrm muted" font-size="11">1</text><circle cx="290" cy="100" r="4" class="accent-fill"/><text x="290" y="150" text-anchor="middle" class="math" font-size="14">α</text><line x1="290" y1="106" x2="290" y2="136" class="muted-stroke" stroke-dasharray="3 3"/></svg>
:::

:::lemma[Levin, Kautz]{#lem-seq-degree}
Let $\nu$ be a computable measure and $A = \mathrm{seq}_\nu(\alpha)$, for a real $\alpha$ that is not one of the endpoints $l_\sigma$. Then $A \leq_T \alpha$. If moreover $A$ is not computable, then $\alpha \leq_T A$, so $A \equiv_T \alpha$.
:::

:::proof{of=lem-seq-degree}
Given $A \uh n$, the next bit is $0$ if $\alpha < l_{(A \uh n) 1}$ and $1$ if $\alpha > l_{(A \uh n) 1}$. The real $l_{(A \uh n)1}$ is computable and different from $\alpha$, so the comparison is decided by approximating both reals until they separate. So $A \leq_T \alpha$.

If $A$ is not computable, then $\rho(A \uh n) \to 0$ by :ref{#lem-atoms-computable}. With oracle $A$, the endpoints of $(A \uh n)_\nu$ are computable reals containing $\alpha$ at distance $\rho(A \uh n)$ of each other, so $\alpha$ is approximated to any precision: given $k$, search for $n$ and approximations showing that $\rho(A \uh n) < 2^{-k}$, and output an approximation of $l_{A \uh n}$. So $\alpha \leq_T A$.
:::

## Randomness is preserved

We use the following form of the correspondence between intervals and classes. For computable reals $a < b$, the class $\{ X : a < 0.X < b \}$ is $\Sigma^0_1$, uniformly in indices of $a$ and $b$, and has measure $b - a$: it is generated by the strings $\tau$ with $a < 0.\tau$ and $0.\tau + 2^{-|\tau|} < b$, and strict inequalities between computable reals are $\Sigma^0_1$.

:::theorem[Levin; Kautz]{#thm-levin-kautz}
Let $\nu$ be a computable measure.

1. If $\alpha$ is random, then $\mathrm{seq}_\nu(\alpha)$ is defined and $\nu$-random.
2. If $A$ is $\nu$-random and not computable, then the intervals $(A \uh n)_\nu$ have a single common point $\alpha$, which is random, and $A = \mathrm{seq}_\nu(\alpha) \equiv_T \alpha$.
3. If $\nu$ is continuous, a Turing degree contains a random sequence if and only if it contains a $\nu$-random sequence.
:::

:::proof{of=thm-levin-kautz}
1. A random real is not computable, so it is not an endpoint $l_\sigma$, and $A = \mathrm{seq}_\nu(\alpha)$ is defined. Suppose that $A$ is captured by a $\nu$-test $(\mathcal U_i)$, and let $(W_i)$ be uniformly c.e. prefix-free sets of strings generating the classes $\mathcal U_i$ (:ref{#lem-prefix-free-generator}; its proof does not depend on the measure). For each $i$, let $\sigma_0, \sigma_1, \dots$ be the enumeration of $W_{i+1}$, and let $\widehat{\mathcal U}_i$ be the union of the classes $\{ X : 0.X \in J_k \}$, where $J_k$ is the open interval obtained by enlarging $(\sigma_k)_\nu$ by $2^{-i-k-3}$ on each side. These classes are uniformly $\Sigma^0_1$, and
$$
\lambda(\widehat{\mathcal U}_i) \leq \sum_k \big( \rho(\sigma_k) + 2 \cdot 2^{-i-k-3} \big) = \nu(\mathcal U_{i+1}) + 2^{-i-1} \leq 2^{-i},
$$
since the cylinders $[\sigma_k]$ are pairwise disjoint. For each $i$, $A$ extends some $\sigma_k \in W_{i+1}$, so $\alpha \in (\sigma_k)_\nu \subseteq J_k$, and the binary expansion of $\alpha$ is in $\widehat{\mathcal U}_i$. So $\alpha$ is captured by a Martin-Löf test, a contradiction.

2. Since $A$ is not computable, $\rho(A \uh n) \to 0$ by :ref{#lem-atoms-computable}, and the nested closed intervals $(A \uh n)_\nu$ have a single common point $\alpha$. Suppose that $\alpha$ is captured by a Martin-Löf test $(\mathcal U_i)$, generated by uniformly c.e. prefix-free sets $(W_i)$. For each $i$, with $\sigma_0, \sigma_1, \dots$ the enumeration of $W_{i+1}$, let $I_k$ be the open interval obtained by enlarging the dyadic interval $[0.\sigma_k, 0.\sigma_k + 2^{-|\sigma_k|}]$ by $2^{-i-k-3}$ on each side, and let $\widehat{\mathcal U}_i$ be generated by the strings $\tau$ with $(\tau)_\nu \subseteq I_k$ for some $k$. These classes are uniformly $\Sigma^0_1$, since the condition is a strict inequality between computable reals. The maximal strings $\tau$ with $(\tau)_\nu \subseteq I_k$ are pairwise incomparable, so their intervals have disjoint interiors inside $I_k$, and the $\nu$-measure of the class they generate is at most the length of $I_k$. Hence $\nu(\widehat{\mathcal U}_i) \leq \sum_k |I_k| \leq \lambda(\mathcal U_{i+1}) + 2^{-i-1} \leq 2^{-i}$. For each $i$, the expansion of $\alpha$ extends some $\sigma_k \in W_{i+1}$, so $\alpha$ is in the dyadic interval of $\sigma_k$, and $(\alpha - 2^{-i-k-3}, \alpha + 2^{-i-k-3}) \subseteq I_k$. Since $\rho(A \uh m) \to 0$ and $\alpha \in (A \uh m)_\nu$, for large $m$ we get $(A \uh m)_\nu \subseteq I_k$, so $A \in \widehat{\mathcal U}_i$. So $A$ is captured by a $\nu$-test, a contradiction, and $\alpha$ is random.

Being random, $\alpha$ is not computable, hence not an endpoint $l_\sigma$. So for each $n$, $(A \uh n)_\nu$ is the only interval of length $n$ containing $\alpha$, and $A = \mathrm{seq}_\nu(\alpha)$. By :ref{#lem-seq-degree}, $A \equiv_T \alpha$.

3. If $\alpha$ is random, $A = \mathrm{seq}_\nu(\alpha)$ is $\nu$-random by 1. It is not computable: a computable $\nu$-random sequence is an atom (:ref{#ex-computable-not-random-continuous}), and $\nu$ has none. So $A \equiv_T \alpha$ by :ref{#lem-seq-degree}. Conversely, a $\nu$-random sequence is not computable, for the same reason, and 2 gives a random sequence of the same degree.
:::

:::quiz[randomness for computable measures]
In part 2 of the proof of :ref{#thm-levin-kautz}, where is it used that $A$ is not computable?

- [x] To have $\rho(A \uh m) \to 0$, so that the intervals $(A \uh m)_\nu$ around $\alpha$ eventually fit inside the enlarged dyadic interval $I_k$; for an atom, they could stay large.
- [ ] To show that the classes $\widehat{\mathcal U}_i$ are $\Sigma^0_1$.

  This only uses the computability of the endpoints.
- [ ] To bound the measures $\nu(\widehat{\mathcal U}_i)$.

  The bound holds for every computable measure.

---

Why are the intervals enlarged by $2^{-i-k-3}$ in parts 1 and 2?

- [x] To replace closed intervals with computable endpoints by open ones, which give $\Sigma^0_1$ classes, while keeping the total length of the enlargements below $2^{-i-1}$.
- [ ] Because the measure $\nu$ may have atoms.

  Atoms are handled by the hypothesis that $A$ is not computable; the enlargement concerns effectivity.
- [ ] To make the intervals dyadic.

  The enlarged intervals have computable, not necessarily dyadic, endpoints.
:::

Part 3 is the degree invariance of randomness: for computable continuous measures, the random degrees do not depend on the measure. Without continuity, part 3 fails, and atoms are not the only problem: Kautz built a computable measure that is not concentrated on its atoms and for which no non-computable $\Delta^0_2$ sequence is random (admitted; Downey–Hirschfeldt, Section 6.12).

::::exercise[Bernoulli sequences]{#ex-bernoulli-frequency difficulty=2 objective="Compute with a Bernoulli measure and see that randomness depends on the measure while degrees do not."}
Let $p \in (0, 1)$ be a computable real with $p \neq \tfrac12$. Show that no sequence is both $\lambda$-random and $\mu_p$-random. Show that every $\mu_p$-random sequence is Turing equivalent to a $\lambda$-random sequence.

:::hint
Use the law of large numbers for both measures; for $\mu_p$, the proof of :ref{#prop-large-numbers} applies with the Chernoff bound for a biased coin, admitted.
:::

:::solution
For a measure $\nu$ among $\lambda$ and $\mu_p$, the class of sequences whose frequency of $1$s does not converge to the probability of $1$ is captured by a $\nu$-test, by the argument of :ref{#prop-large-numbers}: the strings of length $n$ whose frequency differs from the probability by more than $\varepsilon$ have total $\nu$-measure at most $2e^{-2\varepsilon^2 n}$ (Hoeffding's inequality, admitted), a computable bound with a convergent sum, which gives a Solovay test for each rational $\varepsilon$. So a $\lambda$-random sequence has frequency $\tfrac12$ and a $\mu_p$-random sequence has frequency $p \neq \tfrac12$; no sequence has both.

The measure $\mu_p$ is computable and continuous, since $\mu_p([\sigma]) \leq \max(p, 1-p)^{|\sigma|} \to 0$. By :ref{#thm-levin-kautz} (3), every non-computable $\mu_p$-random sequence is Turing equivalent to a $\lambda$-random sequence, and every $\mu_p$-random sequence is non-computable, since $\mu_p$ has no atoms and a computable sequence $Z$ is captured by the $\mu_p$-test $([Z \uh n_i])_i$, with $n_i$ computable such that $\mu_p([Z \uh n_i]) \leq 2^{-i}$.
:::
::::

## Notes and references

Randomness for computable measures and its degree invariance are due to Levin (see Zvonkin and Levin, 1970) and were developed in detail by Kautz in his dissertation (1991), whose account Downey and Hirschfeldt follow (Section 6.12, Lemmas 6.12.6 and 6.12.7, Theorem 6.12.9). The proofs here use open intervals with computable endpoints instead of the rational approximations of the intervals $(\sigma)_\nu$ used by Downey and Hirschfeldt. Randomness for non-computable measures, and the theorem of Reimann and Slaman that every non-computable sequence is random for some measure for which it is not an atom, are in Downey and Hirschfeldt, Section 8.7.

- A. K. Zvonkin and L. A. Levin, *The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms*, Russian Mathematical Surveys 25 (1970), 83–124.
- S. M. Kautz, *Degrees of random sets*, PhD thesis, Cornell University, 1991.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 6.12.

:::::exercises
::::exercise{#ex-computable-not-random-continuous difficulty=1 objective="Check that continuity excludes computable random sequences."}
Let $\nu$ be a computable measure. Show that a computable sequence $Z$ is $\nu$-random if and only if it is an atom of $\nu$.

:::solution
Atoms are $\nu$-random, as shown above. Conversely, if $Z$ is computable and not an atom, then $\rho(Z \uh n) \to 0$, and these values are computable reals, uniformly in $n$. For each $i$, search for $n_i$ and an approximation showing that $\rho(Z \uh n_i) < 2^{-i}$; the classes $[Z \uh n_i]$ are uniformly $\Sigma^0_1$ (in fact clopen) and form a $\nu$-test capturing $Z$.
:::
::::

::::exercise{#ex-seq-uniform difficulty=1 objective="Check the representation on the uniform measure."}
Show that for the uniform measure, $l_\sigma = 0.\sigma$ and $(\sigma)_\lambda$ is the dyadic interval of $\sigma$, and that $\mathrm{seq}_\lambda(\alpha)$ is the binary expansion of $\alpha$ for every irrational $\alpha$.

:::solution
The strings of length $n$ lexicographically below $\sigma$ are those whose numbers, read in binary, are smaller than that of $\sigma$; there are $2^n \cdot 0.\sigma$ of them, each of measure $2^{-n}$, so $l_\sigma = 0.\sigma$, and $(\sigma)_\lambda = [0.\sigma, 0.\sigma + 2^{-n}]$. An irrational $\alpha$ is not a dyadic rational, so it is not an endpoint, and the unique string of length $n$ whose interval contains $\alpha$ is the first $n$ bits of its binary expansion.
:::
::::
:::::
