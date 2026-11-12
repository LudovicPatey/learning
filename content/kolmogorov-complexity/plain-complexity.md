---
title: Plain Kolmogorov complexity
summary: The complexity of a string is the length of its shortest description by an optimal machine; the invariance theorem; most strings are incompressible; the complexity of pairs.
duration: 45
prerequisites: [fundamentals/ce-sets]
---

The string $0000\cdots0$ of length one million can be described in a few words, while a typical string obtained by tossing a coin one million times seems to admit no description shorter than itself. Kolmogorov complexity makes this distinction precise: the complexity of a string is the length of its shortest description, where descriptions are inputs of an algorithm that reconstructs the string. The definition depends on the algorithm, but only up to an additive constant, provided that the algorithm is optimal. This lesson sets up the definition, proves that most strings are incompressible, and shows that the complexity of a pair is not bounded by the sum of the complexities of its components. The next lesson shows that the complexity function is not computable.

## Conventions

We work with binary strings $\bstr$. Natural numbers are identified with strings through the **length-lexicographic** enumeration $\varepsilon, 0, 1, 00, 01, 10, 11, 000, \dots$: the number $n$ is the $n$-th string in this list, counting from $0$. The string associated with $n$ has length $\lfloor \log(n + 1) \rfloor$, where $\log$ denotes the logarithm in base $2$. The number of strings of length less than $n$ is $2^n - 1$. The **binary representation** of a number, which is used occasionally, is a different coding; it is always named as such.

We fix a computable bijection $\langle \cdot, \cdot \rangle : \bstr \times \bstr \to \bstr$ for coding pairs. All partial computable functions between countable sets of finite objects are understood through these codings.

## Description machines

:::definition{#def-description-machine}
A **machine** is a partial computable function $M : \bstr \to \bstr$. If $M(\tau) = \sigma$, the string $\tau$ is an **$M$-description** of $\sigma$. The **complexity of $\sigma$ relative to $M$** is
$$
C_M(\sigma) = \min \{ |\tau| : M(\tau) = \sigma \},
$$
with $C_M(\sigma) = \infty$ if $\sigma$ has no $M$-description.
:::

For instance, the identity machine gives $C_M(\sigma) = |\sigma|$, and the machine $\tau \mapsto 0^{n}$, where $n$ is the number coded by $\tau$, describes $0^n$ with about $\log n$ bits. The machine $\tau \mapsto 0^{2^{2^n}}$, with $n$ again the number coded by $\tau$, compresses even more: the string $0^{2^{2^n}}$ has a description of length about $\log n$. A machine that compresses some strings well may compress others badly. A single machine can even describe any one given string with the empty description: for a fixed $\sigma$, the machine $M_\sigma$ with $M_\sigma(\varepsilon) = \sigma$ gives $C_{M_\sigma}(\sigma) = 0$. So no machine is better than all others without an additive cost, and the right notion is optimality up to a constant depending on the machine compared.

We write $f \leq^+ g$ if there is a constant $c$ such that $f(x) \leq g(x) + c$ for every $x$, and $f =^+ g$ if $f \leq^+ g$ and $g \leq^+ f$.

:::definition{#def-optimal-machine}
A machine $U$ is **optimal**, or **universal**, if for every machine $M$ there is a constant $c_M$ with $C_U(\sigma) \leq C_M(\sigma) + c_M$ for every string $\sigma$, that is, $C_U \leq^+ C_M$.
:::

The idea of the next proof is that a universal machine can simulate any machine $M_e$ once it knows the index $e$. A description for the universal machine is therefore an index followed by an $M_e$-description. The index must be written so that the machine can tell where it ends, and its length is the constant $c_M$.

:::theorem[Invariance theorem; Solomonoff, Kolmogorov]{#thm-invariance}
There is an optimal machine. If $U$ and $V$ are optimal, then $C_U =^+ C_V$.
:::

:::proof{of=thm-invariance}
Let $(M_e)$ be an enumeration of the machines, with $M_e(\tau) = \Phi_e(\tau)$ through the identification of strings with numbers. Define $U(0^e 1 \tau) = M_e(\tau)$, and let $U$ be undefined on the strings of the form $0^e$. Every string other than $0^e$ decomposes uniquely as $0^e 1 \tau$, so $U$ is well defined, and it is partial computable by the universality of the enumeration. If $\tau$ is an $M_e$-description of $\sigma$, then $0^e 1 \tau$ is a $U$-description of $\sigma$ of length $|\tau| + e + 1$. So $C_U \leq C_{M_e} + e + 1$.

If $U$ and $V$ are optimal, then $C_U \leq^+ C_V$ by optimality of $U$ applied to the machine $V$, and symmetrically.
:::

We fix an optimal machine $U$ once and for all, and write $C(\sigma) = C_U(\sigma)$, the **(plain) Kolmogorov complexity** of $\sigma$. By the invariance theorem, the statements of the form $f \leq^+ g$ involving $C$ do not depend on this choice. A statement about the value of $C$ at a particular string, such as $C(0101) = 3$, depends on $U$ and has no intrinsic meaning: the theory is asymptotic. For a number $n$, $C(n)$ is the complexity of the string associated with $n$.

:::proposition{#prop-c-basic}
1. $C(\sigma) \leq^+ |\sigma|$.
2. For every partial computable function $f : \bstr \to \bstr$, $C(f(\sigma)) \leq^+ C(\sigma)$ for every $\sigma$ in the domain of $f$.
3. $C(n) \leq^+ \log n$ for $n \geq 1$, and $C(|\sigma|) \leq^+ C(\sigma)$.
:::

:::proof{of=prop-c-basic}
1. Apply the optimality of $U$ to the identity machine.
2. The machine $M(\tau) = f(U(\tau))$ satisfies $C_M(f(\sigma)) \leq C(\sigma)$: a shortest $U$-description of $\sigma$ is an $M$-description of $f(\sigma)$. Conclude by optimality.
3. The first inequality is 1, since the string associated with $n$ has length $\lfloor \log(n+1) \rfloor \leq \log n + 1$. The second is 2 with $f(\sigma) = |\sigma|$.
:::

The second item says that an algorithm cannot create information: the complexity of the output of a computation is bounded by the complexity of its input, up to a constant depending only on the algorithm. If $f$ is a computable bijection, the inequality holds in both directions, so $C(f(\sigma)) =^+ C(\sigma)$; this is why the choice of the codings of numbers and pairs does not matter.

## Incompressible strings

:::definition{#def-incompressible}
A string $\sigma$ is **$c$-incompressible** if $C(\sigma) \geq |\sigma| - c$.
:::

For instance, for every $c$, the string $0^n$ is not $c$-incompressible when $n$ is large enough, since $C(0^n) \leq^+ \log n$ by :ref{#ex-compressible-strings} below, and $\log n + O(1) < n - c$ for large $n$. The proposition below shows that, on the contrary, most strings are incompressible. Its proof is the **counting argument**, the basic technique of the subject: there are fewer short descriptions than strings.

:::proposition{#prop-incompressible-count}
For every $n$ and $c$, fewer than $2^{n-c}$ strings $\sigma$ satisfy $C(\sigma) < n - c$. In particular, for every $n$ there is a string of length $n$ with $C(\sigma) \geq n$, and at least $2^n - 2^{n-c}$ strings of length $n$ are $c$-incompressible.
:::

:::proof{of=prop-incompressible-count}
A string $\sigma$ with $C(\sigma) < n - c$ has a description of length less than $n - c$, and distinct strings have distinct descriptions, since $U$ is a function. There are $2^{n-c} - 1$ strings of length less than $n - c$.
:::

So at least half of the strings of each length are $1$-incompressible, and the proportion of strings of length $n$ that can be compressed by more than $c$ bits, that is, with $C(\sigma) < n - c$, is less than $2^{-c}$. Incompressibility is the first formal approximation of randomness for finite strings: a string with a regularity that an algorithm can exploit is compressible. The proof does not exhibit an incompressible string, and the next lesson shows that no algorithm can produce infinitely many of them.

:::example{#ex-compressible-strings}
1. $C(0^n) =^+ C(n) \leq^+ \log n$ for $n \geq 1$: item 2 of :ref{#prop-c-basic}, applied to the computable function $n \mapsto 0^n$, gives $C(0^n) \leq^+ C(n)$, and item 3 gives $C(n) = C(|0^n|) \leq^+ C(0^n)$.
2. If $\sigma$ has length $2n$ and the bits of $\sigma$ at odd positions are all $0$, then $C(\sigma) \leq^+ n$: a description is the string of the bits at even positions.
3. Let $\sigma$ be a string of length $n$ containing exactly $k$ ones. It is determined by $n$, $k$ and its rank among the $\binom{n}{k}$ strings of length $n$ with $k$ ones. When $k \leq n/4$, the number $\log \binom{n}{k}$ is at most $n h(1/4) < 0.82\, n$, where $h(p) = -p \log p - (1 - p) \log (1 - p)$ is the binary entropy function, and $\sigma$ is compressible by a linear number of bits for large $n$. For the bound, let $p = k/n$ with $0 < k \leq n/4$: the term of index $k$ in the binomial expansion of $(p + (1 - p))^n = 1$ gives $\binom{n}{k} p^k (1 - p)^{n - k} \leq 1$, that is, $\log \binom{n}{k} \leq n h(p)$, and $h(p) \leq h(1/4)$ since $h$ is increasing on $[0, 1/2]$. The triple is coded with a logarithmic overhead by the technique of :ref{#prop-c-pairs} below.
:::

The third example says that an incompressible string satisfies a weak form of the law of large numbers: its proportion of ones cannot stay below $1/4$ for large $n$. Statistical regularities of random strings are obtained in this way, as consequences of incompressibility.

:::quiz[the invariance theorem and its consequences]
In the proof of :ref{#thm-invariance}, why are descriptions for $U$ of the form $0^e 1 \tau$, rather than $e\tau$ with $e$ written in binary?

- [x] Because the code $0^e 1$ can be separated from $\tau$ without further information, whereas a binary representation of $e$ followed by $\tau$ does not show where $e$ ends.
- [ ] Because binary representations of numbers are not computable.

  Binary representations are computable; the problem is the delimitation.
- [ ] To make $U$ total.

  $U$ is partial, since the machines $M_e$ are.

---

Why does :ref{#prop-incompressible-count} not exhibit a particular incompressible string?

- [x] It is a counting argument: it shows that the strings of small complexity are few, without saying which strings they are; the next lesson shows that no algorithm can list infinitely many incompressible strings.
- [ ] Because incompressible strings of length $n$ exist only for large $n$.

  They exist for every $n$, including $n = 0$: $C(\varepsilon) \geq 0$.
- [ ] Because the proof uses the axiom of choice.

  The argument is finite counting.
:::

## Pairs

The complexity of a pair is not bounded by the sum of the complexities. A description of $\sigma$ followed by a description of $\tau$ does not tell where the first one ends. The length of the first description has to be coded as well, in a form that indicates its own end: each of its bits is doubled, and the pair $01$, which cannot occur at an odd position of a doubled string, marks the end.

:::figure[A description of $\langle \sigma, \tau \rangle$ for the machine of the proof below. The number $\ell = C(\sigma)$, written with each bit doubled and followed by $01$, tells where the shortest description $\alpha_0$ of $\sigma$ ends and the shortest description $\alpha_1$ of $\tau$ begins.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="An input of the machine of the pair proposition: the length of the first description written with doubled bits, the separator 01, then the two descriptions"><rect x="20" y="60" width="160" height="30" class="cell"/><text x="100.0" y="80" text-anchor="middle" class="math" font-size="16">ρ</text><line x1="94.0" y1="66" x2="106.0" y2="66" class="ink-stroke" stroke-width="1"/><rect x="180" y="60" width="34" height="30" class="cell head-cell"/><text x="197.0" y="80" text-anchor="middle" class="math" font-size="16">01</text><rect x="214" y="60" width="150" height="30" class="cell"/><text x="289.0" y="80" text-anchor="middle" class="math" font-size="16">α₀</text><rect x="364" y="60" width="190" height="30" class="cell"/><text x="459.0" y="80" text-anchor="middle" class="math" font-size="16">α₁</text><path d="M21.0,46.0 L21.0,52.0 L179.0,52.0 L179.0,46.0" class="ink-stroke" stroke-width="1.1"/><text x="100.0" y="38" text-anchor="middle" class="label">ℓ = |α₀|, bits doubled</text><path d="M215.0,46.0 L215.0,52.0 L363.0,52.0 L363.0,46.0" class="ink-stroke" stroke-width="1.1"/><text x="289.0" y="38" text-anchor="middle" class="label">shortest description of σ</text><path d="M365.0,46.0 L365.0,52.0 L553.0,52.0 L553.0,46.0" class="ink-stroke" stroke-width="1.1"/><text x="459.0" y="38" text-anchor="middle" class="label">shortest description of τ</text><path d="M21.0,104.0 L21.0,98.0 L179.0,98.0 L179.0,104.0" class="muted-stroke" stroke-width="1.1"/><text x="100.0" y="116" text-anchor="middle" class="label">≈ 2 log C(σ) bits</text><path d="M215.0,130.0 L215.0,124.0 L553.0,124.0 L553.0,130.0" class="muted-stroke" stroke-width="1.1"/><text x="384.0" y="142" text-anchor="middle" class="label">C(σ) + C(τ) bits, split after the first ℓ</text></svg>
:::

:::proposition{#prop-c-pairs}
$C(\langle \sigma, \tau \rangle) \leq^+ C(\sigma) + C(\tau) + 2 \log C(\sigma)$, where $\log 0$ is read as $0$.
:::

:::proof{of=prop-c-pairs}
For a string $\rho = \rho_0 \cdots \rho_{k-1}$, let $\bar\rho = \rho_0 \rho_0 \rho_1 \rho_1 \cdots \rho_{k-1} \rho_{k-1}$. A string of the form $\bar\rho\, 01\, \alpha$ determines $\rho$ and $\alpha$: read pairs of bits until the first pair $01$. Let $M$ be the machine that, on an input of the form $\bar\rho\, 01\, \alpha$, interprets $\rho$ as a number $\ell$, splits $\alpha = \alpha_0 \alpha_1$ with $|\alpha_0| = \ell$, and outputs $\langle U(\alpha_0), U(\alpha_1) \rangle$. If $\alpha_0$ and $\alpha_1$ are shortest descriptions of $\sigma$ and $\tau$, and $\rho$ is the string of the number $|\alpha_0| = C(\sigma)$, the input has length $2|\rho| + 2 + C(\sigma) + C(\tau)$, and $|\rho| \leq \log C(\sigma) + 1$. Conclude by optimality of $U$.
:::

The logarithmic term cannot be replaced by a constant. Fix $n \geq 1$. There are $(n + 1) 2^n$ pairs $(\sigma, \tau)$ with $|\sigma| + |\tau| = n$, and their codes $\langle \sigma, \tau \rangle$ are distinct. By the argument of :ref{#prop-incompressible-count}, fewer than $2^{n + \lfloor \log n \rfloor} \leq n 2^n$ strings have complexity less than $n + \lfloor \log n \rfloor$, so one of these pairs satisfies $C(\langle \sigma, \tau \rangle) \geq n + \lfloor \log n \rfloor$. With $d$ such that $C(\rho) \leq |\rho| + d$ for every $\rho$, this pair also satisfies $C(\sigma) + C(\tau) \leq n + 2d$, so the difference is at least $\lfloor \log n \rfloor - 2d$, which is unbounded. This defect is the starting point of the prefix-free complexity of a later lesson.

:::quiz[the complexity of pairs]
In the proof of :ref{#prop-c-pairs}, why is the length of $\alpha_0$ coded, and not the length of $\alpha_1$?

- [x] Either would do: the total length of the input is available to the machine, so knowing one of the two lengths determines the other. Coding $|\alpha_0| = C(\sigma)$ gives the bound with $2 \log C(\sigma)$.

  Coding $|\alpha_1|$ instead gives the symmetric bound with $2 \log C(\tau)$.
- [ ] Because $\alpha_1$ is the last block, so its length need not be known.

  Knowing where $\alpha_1$ ends is not enough: the machine must know where it begins, which is the same information as $|\alpha_0|$.
- [ ] Because $C(\sigma) \leq C(\tau)$.

  No such assumption is made; the bound holds for all pairs.
:::

## Exercises

::::exercise{difficulty=1}
Show that shortest descriptions are incompressible: there is a constant $b$ such that, if $\tau$ is a shortest $U$-description of some string, then $C(\tau) \geq |\tau| - b$.

:::solution
Let $M$ be the machine $\rho \mapsto U(U(\rho))$, and let $c_M$ be such that $C \leq C_M + c_M$. Let $\tau$ be a shortest $U$-description of $\sigma$, so that $|\tau| = C(\sigma)$, and let $\rho$ be a shortest $U$-description of $\tau$. Then $M(\rho) = \sigma$, so $C(\sigma) \leq |\rho| + c_M = C(\tau) + c_M$. Hence $C(\tau) \geq |\tau| - c_M$, and $b = c_M$ works.
:::
::::

::::exercise{difficulty=2}
Show that $C(\sigma\tau) \leq^+ C(\sigma) + C(\tau) + 2 \log \log C(\sigma) + \log C(\sigma)$ for strings with $C(\sigma) \geq 4$.

:::hint
Code the number $\ell = C(\sigma)$ by its string $\rho$ preceded by the length of $\rho$ written with doubled bits.
:::

:::solution
Let $\rho$ be the string associated with $\ell = C(\sigma)$ and $\lambda$ the string associated with the number $|\rho|$. The input $\bar\lambda\, 01\, \rho\, \alpha_0 \alpha_1$, with $\alpha_0, \alpha_1$ shortest descriptions of $\sigma$ and $\tau$, determines $\lambda$ by the end mark, then $\rho$, of known length $|\rho|$, then $\ell$ and the split of the rest. The machine that decodes it and outputs $U(\alpha_0) U(\alpha_1)$ gives $C(\sigma\tau) \leq^+ 2|\lambda| + |\rho| + C(\sigma) + C(\tau)$, with $|\rho| \leq \log \ell + 1$ and $|\lambda| \leq \log(\log \ell + 2) \leq \log \log \ell + 1$ for $\ell \geq 4$.
:::
::::

## Notes and references

Solomonoff (1960–1964), Kolmogorov (1965) and Chaitin (1966) introduced the complexity of strings independently, with different motivations: inductive inference, the definition of information and randomness, and the length of programs. The invariance theorem is due to Solomonoff and Kolmogorov. The pair bound and the counting argument are standard (Downey–Hirschfeldt, Propositions 3.1.3 and 3.1.5); the incompressibility of shortest descriptions is Exercise 2.1.3 of Nies's book. Li and Vitányi's book is the standard reference on Kolmogorov complexity and its applications; Shen, Uspensky and Vereshchagin give a textbook account in the tradition of the Moscow school.

- A. N. Kolmogorov, *Three approaches to the quantitative definition of information*, Problems of Information Transmission 1 (1965), 1–7.
- R. J. Solomonoff, *A formal theory of inductive inference I*, Information and Control 7 (1964), 1–22.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 3.1.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 2.1.
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, 4th edition, Springer, 2019.
- A. Shen, V. A. Uspensky and N. Vereshchagin, *Kolmogorov Complexity and Algorithmic Randomness*, Mathematical Surveys and Monographs 220, American Mathematical Society, 2017.
