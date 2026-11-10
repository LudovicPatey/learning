---
title: Plain Kolmogorov complexity
summary: The complexity of a string is the length of its shortest description by an optimal machine; the invariance theorem; incompressible strings; the complexity function is not computable but is approximable from above.
duration: 40
prerequisites: [fundamentals/ce-sets]
---

The string $0000\cdots0$ of length one million can be described in a few words, while a typical string obtained by tossing a coin one million times seems to admit no description shorter than itself. Kolmogorov complexity makes this distinction precise: the complexity of a string is the length of its shortest description, where descriptions are inputs of an algorithm that reconstructs the string. The definition depends on the algorithm, but only up to an additive constant, provided that the algorithm is optimal. This lesson sets up the definition, proves that most strings are incompressible, and shows that the complexity function is not computable.

## Conventions

We work with binary strings $\bstr$. Natural numbers are identified with strings through the **length-lexicographic** enumeration $\varepsilon, 0, 1, 00, 01, 10, 11, 000, \dots$: the number $n$ is the $n$-th string in this list, counting from $0$. The string associated with $n$ has length $\lfloor \log(n + 1) \rfloor$, where $\log$ denotes the logarithm in base $2$. In particular, the number of strings of length less than $n$ is $2^n - 1$.

We fix a computable bijection $\langle \cdot, \cdot \rangle : \bstr \times \bstr \to \bstr$ for coding pairs. All partial computable functions between countable sets of finite objects are understood through these codings.

## Description machines

:::definition{#def-description-machine}
A **machine** is a partial computable function $M : \bstr \to \bstr$. If $M(\tau) = \sigma$, the string $\tau$ is an **$M$-description** of $\sigma$. The **complexity of $\sigma$ relative to $M$** is
$$
C_M(\sigma) = \min \{ |\tau| : M(\tau) = \sigma \},
$$
with $C_M(\sigma) = \infty$ if $\sigma$ has no $M$-description.
:::

For instance, the identity machine gives $C_M(\sigma) = |\sigma|$, and the machine $\tau \mapsto 0^{n}$, where $n$ is the number coded by $\tau$, describes $0^n$ with about $\log n$ bits. A machine that compresses some strings well may compress others badly; the following notion selects the machines that are optimal up to a constant.

We write $f \leq^+ g$ if there is a constant $c$ such that $f(x) \leq g(x) + c$ for every $x$, and $f =^+ g$ if $f \leq^+ g$ and $g \leq^+ f$.

:::definition{#def-optimal-machine}
A machine $U$ is **optimal**, or **universal**, if for every machine $M$ there is a constant $c_M$ with $C_U(\sigma) \leq C_M(\sigma) + c_M$ for every string $\sigma$, that is, $C_U \leq^+ C_M$.
:::

:::theorem[Invariance theorem; Solomonoff, Kolmogorov]{#thm-invariance}
There is an optimal machine. If $U$ and $V$ are optimal, then $C_U =^+ C_V$.
:::

:::proof{of=thm-invariance}
Let $(M_e)$ be an enumeration of the machines, with $M_e(\tau) = \Phi_e(\tau)$ through the identification of strings with numbers. Define $U(0^e 1 \tau) = M_e(\tau)$, and let $U$ be undefined on the strings of the form $0^e$. Every string other than $0^e$ decomposes uniquely as $0^e 1 \tau$, so $U$ is well defined, and it is partial computable by the universality of the enumeration. If $\tau$ is an $M_e$-description of $\sigma$, then $0^e 1 \tau$ is a $U$-description of $\sigma$ of length $|\tau| + e + 1$. So $C_U \leq C_{M_e} + e + 1$.

If $U$ and $V$ are optimal, then $C_U \leq^+ C_V$ by optimality of $U$ applied to the machine $V$, and symmetrically.
:::

We fix an optimal machine $U$ once and for all, and write $C(\sigma) = C_U(\sigma)$, the **(plain) Kolmogorov complexity** of $\sigma$. By the invariance theorem, the statements of the form $f \leq^+ g$ involving $C$ do not depend on this choice. For a number $n$, $C(n)$ is the complexity of the string associated with $n$.

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

The second item says that an algorithm cannot create information: the complexity of the output of a computation is bounded by the complexity of its input, up to a constant depending only on the algorithm.

## Incompressible strings

:::definition{#def-incompressible}
A string $\sigma$ is **$c$-incompressible** if $C(\sigma) \geq |\sigma| - c$.
:::

:::proposition{#prop-incompressible-count}
For every $n$ and $c$, fewer than $2^{n-c}$ strings $\sigma$ satisfy $C(\sigma) < n - c$. In particular, for every $n$ there is a string of length $n$ with $C(\sigma) \geq n$, and at least $2^n - 2^{n-c}$ strings of length $n$ are $c$-incompressible.
:::

:::proof{of=prop-incompressible-count}
A string $\sigma$ with $C(\sigma) < n - c$ has a description of length less than $n - c$, and distinct strings have distinct descriptions, since $U$ is a function. There are $2^{n-c} - 1$ strings of length less than $n - c$.
:::

So at least half of the strings of each length are $1$-incompressible, and the proportion of strings of length $n$ that can be compressed by $c$ bits is less than $2^{-c}$. Incompressibility is the first formal approximation of randomness for finite strings: a string with a regularity that an algorithm can exploit is compressible.

:::example{#ex-compressible-strings}
1. $C(0^n) =^+ C(n) \leq^+ \log n$: the machine $\tau \mapsto 0^{n}$, with $n$ the number associated with $\tau$, gives $C(0^n) \leq^+ C(n)$, and $C(n) \leq^+ C(0^n)$ by :ref{#prop-c-basic}.
2. If $\sigma$ has length $2n$ and the bits of $\sigma$ at odd positions are all $0$, then $C(\sigma) \leq^+ n$: a description is the string of the bits at even positions.
3. Let $\sigma$ be a string of length $n$ containing exactly $k$ ones. It is determined by $n$, $k$ and its rank among the $\binom{n}{k}$ strings of length $n$ with $k$ ones. When $k \leq n/4$, the number $\log \binom{n}{k}$ is at most $n h(1/4) < 0.82\, n$, where $h$ is the binary entropy function, and $\sigma$ is compressible by a linear number of bits for large $n$. (The bound on the binomial coefficient is classical; the coding of the triple uses the technique of :ref{#prop-c-pairs} below.)
:::

## Pairs

The complexity of a pair is not bounded by the sum of the complexities. A description of $\sigma$ followed by a description of $\tau$ does not tell where the first one ends. The length of the first description has to be coded as well.

:::proposition{#prop-c-pairs}
$C(\langle \sigma, \tau \rangle) \leq^+ C(\sigma) + C(\tau) + 2 \log C(\sigma)$, where $\log 0$ is read as $0$.
:::

:::proof{of=prop-c-pairs}
For a string $\rho = \rho_0 \cdots \rho_{k-1}$, let $\bar\rho = \rho_0 \rho_0 \rho_1 \rho_1 \cdots \rho_{k-1} \rho_{k-1}$. A string of the form $\bar\rho\, 01\, \alpha$ determines $\rho$ and $\alpha$: read pairs of bits until the first pair $01$. Let $M$ be the machine that, on an input of the form $\bar\rho\, 01\, \alpha$, interprets $\rho$ as a number $\ell$, splits $\alpha = \alpha_0 \alpha_1$ with $|\alpha_0| = \ell$, and outputs $\langle U(\alpha_0), U(\alpha_1) \rangle$. If $\alpha_0$ and $\alpha_1$ are shortest descriptions of $\sigma$ and $\tau$, and $\rho$ is the string of the number $|\alpha_0| = C(\sigma)$, the input has length $2|\rho| + 2 + C(\sigma) + C(\tau)$, and $|\rho| \leq \log C(\sigma) + 1$.
:::

The logarithmic term cannot be removed in general; this defect motivates the prefix-free complexity of a later lesson.

:::quiz[the invariance theorem and its consequences]
In the proof of :ref{#thm-invariance}, why are descriptions for $U$ of the form $0^e 1 \tau$, rather than $e\tau$ with $e$ written in binary?

- [x] Because the code $0^e 1$ can be separated from $\tau$ without further information, whereas a binary representation of $e$ followed by $\tau$ does not show where $e$ ends.
- [ ] Because binary representations of numbers are not computable.

  Binary representations are computable; the problem is the delimitation.
- [ ] To make $U$ total.

  $U$ is partial, since the machines $M_e$ are.

---

Why does :ref{#prop-incompressible-count} not exhibit a particular incompressible string?

- [x] It is a counting argument: it shows that the strings of small complexity are few, without saying which strings they are, and no algorithm can list incompressible strings, as the next section shows.
- [ ] Because incompressible strings of length $n$ exist only for large $n$.

  They exist for every $n$, including $n = 0$: $C(\varepsilon) \geq 0$.
- [ ] Because the proof uses the axiom of choice.

  The argument is finite counting.
:::

## Non-computability

:::theorem{#thm-c-not-computable}
1. The function $C$ is not computable. More precisely, if $g : \bstr \to \nat$ is a partial computable function such that $g(\sigma) \leq C(\sigma)$ for every $\sigma$ in its domain, then $g$ is bounded.
2. The function $C$ is **approximable from above**: there is a computable function $(s, \sigma) \mapsto C_s(\sigma)$, non-increasing in $s$, with $\lim_s C_s(\sigma) = C(\sigma)$.
:::

:::proof{of=thm-c-not-computable}
1. Suppose that $g$ is unbounded on its domain. Let $f(n)$ be the first string $\sigma$ found, in an enumeration of the domain of $g$, with $g(\sigma) > n$. Then $f$ is total computable, and $C(f(n)) \geq g(f(n)) > n$. By :ref{#prop-c-basic}, $C(f(n)) \leq^+ C(n) \leq^+ \log n$. So $n < \log n + c$ for some constant $c$ and every $n \geq 1$, which fails for large $n$. If $C$ were computable, it would be such a function $g$, and it is unbounded by :ref{#prop-incompressible-count}.
2. Let $d$ be a constant with $C(\sigma) \leq |\sigma| + d$. Let $C_s(\sigma)$ be the least length of a string $\tau$ with $|\tau| \leq |\sigma| + d$ and $U(\tau)[s]\converge = \sigma$, or $|\sigma| + d$ if there is none. It is computable, non-increasing in $s$, and equal to $C(\sigma)$ from the stage at which a shortest description converges.
:::

The proof formalizes the **Berry paradox**, "the least number that cannot be defined in fewer than twenty words": the first string of complexity larger than $n$ has a description of length about $\log n$. Statement 1 says more than non-computability: no algorithm certifies that strings have large complexity, except for finitely many values. This is a form of Gödel's incompleteness theorem, due to Chaitin. Let $T$ be a theory with a c.e. set of axioms that proves only true statements of the form "$C(\sigma) > n$". Searching through the proofs of $T$ gives a partial computable $g$, with $g(\sigma)$ the first $n$ found such that $T$ proves "$C(\sigma) > n$". By 1, $g$ is bounded: there is a number $n_0$ such that $T$ proves no statement "$C(\sigma) > n$" with $n \geq n_0$, although all but finitely many strings satisfy $C(\sigma) > n_0$.

Approximations from above make $C$ computable in $\emptyset'$, by the limit lemma: $C(\sigma)$ is the value of $C_s(\sigma)$ at the first stage $s$ such that no description shorter than $C_s(\sigma)$ ever converges, a $\Pi^0_1$ condition. Conversely, $C$ computes $\emptyset'$; a proof of this result of Kummer and Gács is beyond the scope of this lesson, but the following weaker statement is an exercise.

:::quiz[non-computability of C]
In the proof of :ref{#thm-c-not-computable} (1), where is the hypothesis $g \leq C$ used?

- [x] To deduce $C(f(n)) > n$ from the choice of $f(n)$, which satisfies $g(f(n)) > n$.
- [ ] To show that $f$ is computable.

  $f$ is computable because $g$ is partial computable with unbounded values on its domain; the inequality is not needed for this.
- [ ] To show that $C(f(n)) \leq^+ \log n$.

  This bound comes from the computability of $f$, by :ref{#prop-c-basic}.

---

Why is $C$ approximable from above, and not from below?

- [x] Because the discovery of a new description can only decrease the current upper bound, while the absence of a short description is never confirmed at a finite stage.
- [ ] Because $C(\sigma) \leq |\sigma| + d$.

  This bound only provides a starting value for the approximation.
- [ ] Because $U$ is total.

  $U$ is partial, which is exactly why short descriptions may appear late.
:::

## Exercises

::::exercise{difficulty=1}
Let $X$ be the set of strings $\sigma$ such that $U(\sigma)$ converges. Show that $\emptyset' \leq_T X$.

:::solution
Let $M$ be the machine with $M(0^e) = 0^s$, where $s$ is the least stage with $\Phi_e(e)[s]\converge$, and $M$ undefined elsewhere. Let $d$ be such that $C \leq C_M + d$. If $\Phi_e(e)$ converges at stage $s$, then $C(0^s) \leq e + d$. With oracle $X$, list the strings $\tau$ of length at most $e + d$ such that $U(\tau)$ converges, compute their outputs, and let $t$ be the largest number such that $0^t$ is one of them. Then $\Phi_e(e)$ converges if and only if $\Phi_e(e)[t]\converge$.
:::
::::

::::exercise{difficulty=1}
Fix $c$. Show that the set $R_c = \{ \sigma : C(\sigma) \geq |\sigma| - c \}$ of $c$-incompressible strings is immune: it is infinite and has no infinite c.e. subset.

:::solution
$R_c$ contains a string of each length by :ref{#prop-incompressible-count}, so it is infinite. If $W \subseteq R_c$ were an infinite c.e. set, the partial computable function $g(\sigma) = \max(|\sigma| - c, 0)$ with domain $W$ would satisfy $g \leq C$ on its domain, and it would be unbounded, since $W$ contains strings of arbitrary length. This contradicts :ref{#thm-c-not-computable}.
:::
::::

## Notes and references

Solomonoff (1960–1964), Kolmogorov (1965) and Chaitin (1966) introduced the complexity of strings independently, with different motivations: inductive inference, the definition of information and randomness, and the length of programs. Chaitin's form of the incompleteness theorem dates from 1974. Kummer (1996) proved that the set of compressible strings is truth-table complete, and the Turing completeness of $C$ is due to Gács. Li and Vitányi's book is the standard reference on Kolmogorov complexity.

- A. N. Kolmogorov, *Three approaches to the quantitative definition of information*, Problems of Information Transmission 1 (1965), 1–7.
- R. J. Solomonoff, *A formal theory of inductive inference I*, Information and Control 7 (1964), 1–22.
- G. J. Chaitin, *Information-theoretic limitations of formal systems*, Journal of the ACM 21 (1974), 403–424.
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, 4th edition, Springer, 2019.
