---
title: Computation relative to an oracle
summary: Oracle machines and Turing functionals; computations with finite oracles, stages and the use principle.
duration: 55
prerequisites: [fundamentals/ce-sets]
---

A non-computable set can be seen as an unsolvable problem. To compare unsolvable problems with one another, Turing introduced in 1939 machines that may consult an **oracle**: a set $X \subseteq \nat$, given as an infinite external resource, which the machine may query at any time for the value of $X(n)$. A set is then computable *relative to* $X$ if some oracle machine decides it with oracle $X$. This lesson defines oracle computations and proves the property that makes them manageable. The next lesson shows that the results of the course on fundamentals hold relative to any oracle.

An algorithm cannot survey an infinite oracle, but a halting computation lasts finitely many steps and reads finitely many of its bits; everything about the computation can be read off a prefix of the oracle. This remark, the **use principle**, underlies every construction of this course.

## Strings and sequences

We use the notation of :ref{#def-cantor-space}. A **string** is an element $\sigma$ of $\bstr$, the set of finite binary sequences; $|\sigma|$ is its length, $\sigma(n)$ its $n$-th bit for $n < |\sigma|$, and $\varepsilon$ the empty string. For strings $\sigma$ and $\tau$ and $X \in \cs$:

- $\sigma \preceq \tau$ means that $\sigma$ is a **prefix** of $\tau$, and $\sigma \prec X$ that $\sigma$ is a prefix of $X$;
- $\sigma$ and $\tau$ are **compatible** if one is a prefix of the other, and **incompatible** otherwise;
- $\sigma \tau$ and $\sigma i$ denote concatenations, for $i \in \{0, 1\}$, and $X \uh n = X(0) \cdots X(n-1)$;
- $[\sigma] = \{ X \in \cs : \sigma \prec X \}$ is the **cylinder** of $\sigma$.

Strings are coded by integers in a fixed computable way, so that the usual operations on them are primitive recursive. Sets of integers are identified with elements of $\cs$. For instance, if $X$ is the set of even numbers, then $X \uh 5 = 10101$; the strings $10$ and $101$ are compatible, the strings $10$ and $11$ are not, and $[10]$ is the set of all $Y$ with $0 \in Y$ and $1 \notin Y$.

## Oracle machines

:::definition{#def-oracle-machine}
An **oracle machine** is a Turing machine with a second, read-only tape, the **oracle tape**, whose cells are indexed by $\nat$, and a second head on it, starting on cell $0$. Its transition function has the form
$$
\delta : (Q \setminus \{ q_h \}) \times \Gamma \times \{0, 1\} \to Q \times \Gamma \times \{L, R\} \times \{L, S, R\}:
$$
in state $q$, reading $a$ on the work tape and $b$ under the oracle head, the machine writes $a'$ on the work tape, moves the work head in direction $D$ and the oracle head in direction $D'$ ($S$ meaning that it stays; a move to the left from cell $0$ leaves it on cell $0$), and enters the state $q'$, where $\delta(q, a, b) = (q', a', D, D')$.

With **oracle** $X \in \cs$, the oracle tape contains $X(k)$ on cell $k$. Inputs and outputs follow the conventions of :ref{#def-tm-computes}.
:::

:::figure[An oracle machine with oracle $X$. The oracle head starts on cell $0$ and moves by at most one cell per step, so the cells it has read always form an initial segment of the oracle tape.]
<svg class="fig" viewBox="0 0 600 254" width="600" role="img" aria-label="An oracle machine: a work tape, a read-only oracle tape holding the bits of X, and a finite control; the cells read form the use"><text x="10" y="44" class="label">work tape</text><rect x="120" y="24" width="34" height="34" class="cell"/><text x="137.0" y="47" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect x="154" y="24" width="34" height="34" class="cell"/><text x="171.0" y="47" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="188" y="24" width="34" height="34" class="cell"/><text x="205.0" y="47" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="222" y="24" width="34" height="34" class="cell head-cell"/><text x="239.0" y="47" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="256" y="24" width="34" height="34" class="cell"/><text x="273.0" y="47" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect x="290" y="24" width="34" height="34" class="cell"/><text x="307.0" y="47" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="324" y="24" width="34" height="34" class="cell"/><text x="341.0" y="47" text-anchor="middle" class="mrm" font-size="16">1</text><rect x="358" y="24" width="34" height="34" class="cell"/><text x="375.0" y="47" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect x="392" y="24" width="34" height="34" class="cell"/><text x="409.0" y="47" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><rect x="426" y="24" width="34" height="34" class="cell"/><text x="443.0" y="47" text-anchor="middle" class="mrm muted" font-size="16">⊔</text><text x="468" y="47" class="mrm muted" font-size="16">⋯</text><text x="10" y="196" class="label">oracle tape</text><rect x="120" y="176" width="34" height="34" class="cell"/><text x="137.0" y="199" text-anchor="middle" class="mrm" font-size="16">0</text><text x="137.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">0</text><rect x="154" y="176" width="34" height="34" class="cell"/><text x="171.0" y="199" text-anchor="middle" class="mrm" font-size="16">1</text><text x="171.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">1</text><rect x="188" y="176" width="34" height="34" class="cell"/><text x="205.0" y="199" text-anchor="middle" class="mrm" font-size="16">1</text><text x="205.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">2</text><rect x="222" y="176" width="34" height="34" class="cell"/><text x="239.0" y="199" text-anchor="middle" class="mrm" font-size="16">0</text><text x="239.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">3</text><rect x="256" y="176" width="34" height="34" class="cell head-cell"/><text x="273.0" y="199" text-anchor="middle" class="mrm" font-size="16">1</text><text x="273.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">4</text><rect x="290" y="176" width="34" height="34" class="cell"/><text x="307.0" y="199" text-anchor="middle" class="mrm muted" font-size="16">0</text><text x="307.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">5</text><rect x="324" y="176" width="34" height="34" class="cell"/><text x="341.0" y="199" text-anchor="middle" class="mrm muted" font-size="16">0</text><text x="341.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">6</text><rect x="358" y="176" width="34" height="34" class="cell"/><text x="375.0" y="199" text-anchor="middle" class="mrm muted" font-size="16">1</text><text x="375.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">7</text><rect x="392" y="176" width="34" height="34" class="cell"/><text x="409.0" y="199" text-anchor="middle" class="mrm muted" font-size="16">0</text><text x="409.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">8</text><rect x="426" y="176" width="34" height="34" class="cell"/><text x="443.0" y="199" text-anchor="middle" class="mrm muted" font-size="16">1</text><text x="443.0" y="226" text-anchor="middle" class="mrm muted" font-size="11">9</text><text x="468" y="199" class="mrm muted" font-size="16">⋯</text><path d="M122,240 L122,246 L288,246 L288,240" class="accent-stroke" stroke-width="1.4"/><text x="298" y="248" class="label">cells read so far: the use</text><rect x="179.0" y="90" width="150" height="54" rx="8" class="soft-fill accent-stroke" stroke-width="1.3"/><text x="254.0" y="113" text-anchor="middle" class="label">finite control</text><text x="254.0" y="134" text-anchor="middle" class="math" font-size="18">q<tspan class="mrm" font-size="12" dy="4">2</tspan></text><line x1="239.0" y1="58" x2="239.0" y2="90" class="accent-stroke" stroke-width="1.4" stroke-dasharray="4 3"/><line x1="273.0" y1="144" x2="273.0" y2="176" class="accent-stroke" stroke-width="1.4" stroke-dasharray="4 3"/><text x="346" y="112" class="label">δ(q, a, b) = (q′, a′, D, D′):</text><text x="346" y="128" class="label">read a on the work tape and b = X(k)</text><text x="346" y="144" class="label">on the oracle tape; write a′, move both heads</text></svg>
:::

An oracle machine computes, for each oracle $X$, a partial function $\nat^k \rightharpoonup \nat$. Ordinary Turing machines are the oracle machines that ignore their oracle. Oracle machines are coded by integers as ordinary machines are; the integers that are not codes are treated as coding a machine that never halts.

:::definition{#def-functional}
For $e, k \in \nat$, the **Turing functional** $\Phi_e$ is the map which sends an oracle $X$ to the partial function $\Phi^X_e : \nat^k \rightharpoonup \nat$ computed by the oracle machine of code $e$ with oracle $X$. We also write $\Phi_e(X, \vec x)$ for $\Phi_e^X(\vec x)$.
:::

The notation is consistent with the course on fundamentals once a convention is fixed: from now on, $\Phi_e$ denotes the functional of index $e$, and when no oracle is written, $\Phi_e(x)$ stands for $\Phi^{\emptyset}_e(x)$, $\Phi_e(x)[s]$ for $\Phi^{\emptyset}_e(x)[s]$ (defined below) and $W_e$ for $\dom(\Phi^{\emptyset}_e)$. The partial computable functions of that course are exactly the functions $\Phi^{\emptyset}_e$, or $\Phi^X_e$ for any computable $X$ (see the exercises of the next lesson), although a function need not have the same indices in the two enumerations. Since every ordinary machine is an oracle machine, every partial computable function is $\Phi^X_e$ for some $e$ and every $X$.

A single functional behaves differently on different oracles, and the domain of $\Phi^X_e$ depends on $X$ in general.

:::example{#ex-functionals}
1. The machine which, on input $n$, moves its oracle head to cell $2n$ and outputs the bit it reads computes the functional $X \mapsto (n \mapsto X(2n))$. It is total for every oracle.
2. The machine which, on input $n$, moves its oracle head to cell $n + 1$ and then to the right until it reads a $1$, and outputs the position of that cell, computes $n \mapsto \min \{ m > n : m \in X \}$. With an infinite oracle it is total; with a finite oracle $X$ it diverges on every $n \geq \max X$, and on every $n$ if $X = \emptyset$. The same machine thus computes a total function with some oracles and a partial one with others.
:::

:::example{#ex-oracle-domination}
Let $X$ be an infinite set whose principal function $p_X$ (:ref{#lem-subsets-of-n}) grows fast enough that $\Phi_e(e)\converge$ implies $\Phi_e(e)[p_X(e)]\converge$, for every $e$. Then there is an oracle machine computing $\emptyset'$ with oracle $X$: on input $e$, read the oracle until its $e$-th element $p_X(e)$ is found, then run $\Phi_e(e)$ for $p_X(e)$ stages, and answer $1$ if and only if it has converged. Fast-growing sets can thus compute the halting set; this phenomenon is studied in the lesson on limit computability.
:::

## Computations with finite oracles

A halting computation is finite, so it reads only finitely many cells of the oracle. To exploit this, we give a meaning to computations with a finite string as oracle. For a string $\sigma$, the computation **with oracle $\sigma$** is the computation of the machine in which the oracle tape contains $\sigma(k)$ on the cells $k < |\sigma|$; it is considered **undefined** as soon as the oracle head reaches a cell $k \geq |\sigma|$. A computation with oracle $\sigma$ thus either halts having read only bits of $\sigma$, or runs forever within $\sigma$, or stops being defined because it asks for a bit that $\sigma$ does not provide.

:::definition{#def-finite-oracle}
For $\sigma \in \bstr$, $e, x, s \in \nat$:

1. $\Phi^\sigma_e(x)\converge = y$ means that the computation of the machine $e$ on input $x$ with oracle $\sigma$ halts in a standard configuration with output $y$, without the oracle head reaching a cell $k \geq |\sigma|$;
2. $\Phi^\sigma_e(x)[s]\converge = y$ means that moreover $e, x < s$ and the code of this computation is smaller than $s$;
3. for $X \in \cs$, $\Phi^X_e(x)[s] \simeq \Phi^{X \uh s}_e(x)[s]$.
:::

Item 3 is the convention that at stage $s$ only the first $s$ bits of the oracle are available. Write $\Psi$ for the functional of the machine of item 2 of :ref{#ex-functionals}. Then $\Psi^{\sigma}(0)\converge = 2$ for $\sigma = 101$, a prefix of the set of even numbers, while the computation with oracle $\sigma = 10$ is undefined: it reaches cell $2$, beyond the end of the string.

As in :ref{#thm-kleene-normal-form-proof}, the relation "$t$ codes a halting computation of the machine $e$ on input $x$ with oracle $\sigma$" is primitive recursive in $(\sigma, e, x, t)$: configurations now include the position of the oracle head, and each step consults one bit of $\sigma$, available since $\sigma$ is part of the data. A computation of code $t$ has fewer than $t$ steps, and the oracle head moves at most one cell per step, so it reads only cells $k < t$.

:::proposition{#prop-oracle-stages}
1. The relation $\Phi^\sigma_e(x)[s]\converge = y$ is primitive recursive in $(\sigma, e, x, s, y)$.
2. *Monotonicity.* If $\Phi^\sigma_e(x)[s]\converge = y$, $\sigma \preceq \tau$ and $s \leq s'$, then $\Phi^\tau_e(x)[s']\converge = y$.
3. *Approximation.* For every $X \in \cs$: $\Phi^X_e(x)\converge = y$ if and only if $\Phi^X_e(x)[s]\converge = y$ for some $s$, if and only if $\Phi^\sigma_e(x)\converge = y$ for some $\sigma \prec X$.
:::

:::proof{of=prop-oracle-stages}
1. $\Phi^\sigma_e(x)[s]\converge = y$ holds if and only if $e, x < s$ and some $t < s$ codes a halting computation of $e$ on $x$ with oracle $\sigma$, with output $U(t) = y$: a bounded quantification of a primitive recursive relation.
2. The computation with oracle $\sigma$ reads only cells $k < |\sigma|$, where $\tau$ agrees with $\sigma$; so with oracle $\tau$ the machine performs the same steps, and the computation has the same code.
3. If $\Phi^X_e(x)\converge = y$, let $t$ be the code of the computation with oracle $X$. It reads only cells $k < t$, so it is also the computation with oracle $X \uh t$, and $\Phi^X_e(x)[s]\converge = y$ for $s = \max(e, x, t) + 1$, since $X \uh t \preceq X \uh s$. If $\Phi^X_e(x)[s]\converge = y$, then $\sigma = X \uh s$ works. Finally, if $\Phi^\sigma_e(x)\converge = y$ with $\sigma \prec X$, the computation with oracle $X$ performs the same steps, by the argument of item 2.
:::

Item 3 is the form in which the proposition is used most often: convergence with an infinite oracle is a $\Sigma^0_1$ property of the oracle, witnessed by a prefix and a halting computation. Divergence is not witnessed in this way. That asymmetry reappears in every finite extension argument of this course, where convergence is secured by fixing a prefix, and divergence by showing that no prefix makes the computation converge.

## The use principle

:::definition{#def-use}
If $\Phi^X_e(x)\converge$, the **use** of the computation, written $\use^X_e(x)$, is $1$ plus the largest cell read by the oracle head during the computation (the head reads cell $0$ initially, so the use is at least $1$).
:::

For the machine of item 2 of :ref{#ex-functionals}, with $X$ the set of even numbers, the computation on input $3$ reads the cells $0, 1, \dots, 4$ and outputs $4$; its use is $5$. In general the use of that machine on input $n$ is $1 + \min \{ m > n : m \in X \}$, which is not bounded by any function of $n$ alone: the use depends on the oracle.

:::theorem[Use principle]{#thm-use-principle}
If $\Phi^X_e(x)\converge = y$ with use $u$, then $\Phi^Y_e(x)\converge = y$, with the same use, for every $Y$ such that $Y \uh u = X \uh u$. In particular $\Phi^{X \uh u}_e(x)\converge = y$.
:::

:::proof{of=thm-use-principle}
By induction on the number of steps, the computations with oracles $X$ and $Y$ pass through the same configurations: the oracle head stays within the cells $k < u$ during the computation with oracle $X$, and there $X$ and $Y$ agree, so each step reads the same oracle bit. Hence the computation with oracle $Y$ halts after the same number of steps, with the same output, and reads the same cells. The last statement is the same argument with the finite oracle $X \uh u$, of length $u$.
:::

The use principle says that the value of a convergent computation depends only on a finite part of the oracle. In topological terms, which are developed in the course on $\Pi^0_1$ classes, the partial map $X \mapsto \Phi^X_e(x)$ is **continuous** on its domain, for the product topology on $\cs$: if $\Phi^X_e(x)\converge = y$, then $\Phi^Y_e(x)\converge = y$ on the whole open neighborhood $[X \uh u]$ of $X$. Consequently, a function on $\cs$ that is not continuous, such as the map sending $X$ to $1$ if $X$ is finite and to $0$ otherwise, is not computed by any functional.

:::quiz[the use principle]
Why do the cells read during a computation form an initial segment $\{0, \dots, u-1\}$ of the oracle tape?

- [x] Because the oracle head starts on cell $0$ and moves by at most one cell at each step, so it cannot reach a cell without passing through all smaller ones.

  With a different model, for instance one where the machine writes a number $n$ and asks whether $n \in X$, the set of queried positions need not be an initial segment; the use is then defined as $1$ plus the largest position queried, and the use principle holds in the same form.
- [ ] Because the use principle requires it.

  It is the other way around: the shape of the model makes the use principle straightforward.
- [ ] Because $X$ is an initial segment of $\nat$.

  $X$ is an arbitrary set.

---

Let $\Phi^X_e(x)\converge$ with use $u$, and let $Y$ differ from $X$ only at position $u$. What can be said of $\Phi^Y_e(x)$?

- [x] It converges, to the same value, since $Y \uh u = X \uh u$.
- [ ] Nothing: the computation may read position $u$.

  By definition of the use, it reads only positions $k < u$.
- [ ] It diverges.

  Nothing in the computation distinguishes $X$ from $Y$.

---

Which statement is the content of item 3 of :ref{#prop-oracle-stages}?

- [x] Convergence with an infinite oracle is witnessed by a finite object: a prefix of the oracle together with a halting computation.
- [ ] Every computation with a finite oracle converges.

  It may read beyond the string, or run forever.
- [ ] Convergence with oracle $X$ is decidable from $X$.

  Convergence is witnessed at a finite stage, but divergence is not; deciding convergence with oracle $X$ is the jump of $X$, studied in a later lesson.

---

Why is the map $F(X) = 1$ if $X$ is finite, $F(X) = 0$ otherwise, not computed by any functional?

- [x] If $\Phi^X_e(0) = F(X)$ for every $X$, the computation with oracle $\emptyset$ outputs $1$ with some use $u$; the infinite set $Y = \{ n : n \geq u \}$ agrees with $\emptyset$ below $u$, so $\Phi^Y_e(0) = 1$, while $F(Y) = 0$.

  The use principle forbids a functional from distinguishing two oracles that agree on the cells it reads.
- [ ] Because the set of finite sets is countable.

  Countability plays no role: what matters is that finiteness cannot be detected from a prefix.
- [ ] Because $F$ takes only two values.

  Many computable maps take only two values, for instance $X \mapsto X(0)$.
:::

## Exercises

::::exercise{difficulty=1}
Show that the partial function $(X, e, x) \mapsto \use^X_e(x)$ is computed by an oracle machine: there is $v$ with $\Phi^X_v(e, x) \simeq \use^X_e(x)$ for every $X$, $e$ and $x$.

:::solution
Let $T(\sigma, e, x, t)$ be the primitive recursive relation "$t$ codes a halting computation of $e$ on $x$ with oracle $\sigma$". On input $(e, x)$ with oracle $X$, for $t = 0, 1, 2, \dots$, read $X \uh t$ on the oracle tape and test $T(X \uh t, e, x, t)$. By :ref{#prop-oracle-stages}, the search terminates if and only if $\Phi^X_e(x)\converge$, and then $t$ codes the computation with oracle $X$, since that computation reads only cells below its code. The use is $1$ plus the largest oracle head position appearing in the configurations coded by $t$, which is computed from $t$. If $\Phi^X_e(x)\diverge$, the search diverges, as it should.
:::
::::

::::exercise{difficulty=2}
Let $\Phi_e$ be a functional such that $\Phi^X_e$ is total for every $X \in \cs$. Show that there is a computable function $b$ such that $\use^X_e(x) \leq b(x)$ for all $X$ and $x$.

:::hint
Use König's lemma, or the compactness of $\cs$: for a fixed $x$, consider the strings $\sigma$ on which the computation $\Phi^\sigma_e(x)$ does not yet converge.
:::

:::solution
First, for every string $\sigma$, the computation of the machine $e$ on input $x$ with oracle $\sigma$ either halts or reaches a cell $k \geq |\sigma|$ after finitely many steps. Otherwise it would run forever while reading only cells $k < |\sigma|$, and with any oracle $X \succ \sigma$ it would perform the same steps, so that $\Phi^X_e(x)\diverge$, contradicting the hypothesis. Hence the relation $\Phi^\sigma_e(x)\converge$ is decidable: run the computation until one of the two events occurs.

Fix $x$, and let $T_x$ be the set of strings $\sigma$ such that $\Phi^{\tau}_e(x)\diverge$ for every $\tau \preceq \sigma$. It is closed under prefixes and decidable. If $T_x$ contained strings of every length, then by König's lemma (an infinite binary tree has an infinite path) there would be $X$ with all its prefixes in $T_x$, and then $\Phi^X_e(x)\diverge$ by :ref{#prop-oracle-stages}, a contradiction. So there is a length $\ell$ such that no string of length $\ell$ belongs to $T_x$, and the least such $\ell$ is found by testing the $2^\ell$ strings of length $\ell = 0, 1, 2, \dots$ in turn. Let $b(x)$ be this $\ell$. Every $X$ has a prefix $\tau$ of length at most $b(x)$ with $\Phi^\tau_e(x)\converge$, and then $\use^X_e(x) \leq |\tau| \leq b(x)$ by the use principle.
:::
::::

## Notes and references

Oracle machines were introduced by Turing in his Princeton thesis, published in 1939, in the study of ordinal logics. Post (1944, 1948) and Kleene and Post (1954) made relative computability the central notion of the theory; the paper of Kleene and Post set out the properties of oracle computations, the use principle among them (Soare 2016, §6.1). The model with an oracle tape follows Soare's textbook (Definition 3.2.1); models with query states give the same notion of relative computability. Conventions on the use differ by one: Soare defines it as the largest cell read, Downey and Hirschfeldt, like this course, as $1$ plus the largest cell read. The use principle is Theorem 3.3.9 of Soare (2016) and Proposition 2.4.1 of Downey and Hirschfeldt (2010); Monin and Patey treat oracle computations and the use property in the chapter on Turing degrees.

- A. M. Turing, *Systems of logic based on ordinals*, Proceedings of the London Mathematical Society (2) 45 (1939), 161–228.
- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §§3.1–3.3.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.4.
