---
title: Computability on Baire space
summary: Computable partial functions on Baire space, given by Turing functionals that read an infinite input and produce an infinite output; computable functions are continuous, and continuous functions are those computable relative to an oracle.
duration: 45
prerequisites: [turing-degrees/oracle-computation, pi01-classes/cantor-space]
---

Computable analysis studies which operations on real numbers, functions and sets can be carried out by algorithms. A real number is an infinite object: an algorithm can only receive it through an infinite sequence of finite approximations, called a **name**, and can only produce a real by writing such a sequence forever. The basic model of computation is therefore a machine that reads an infinite input and writes an infinite output, each output symbol being final once written. This is the **Type-2 Theory of Effectivity** of Weihrauch, whose name refers to functions of type 2, from functions to functions; the idea goes back to Turing (1936–1937), Grzegorczyk and Lacombe (1955).

This lesson sets up the model on Baire space, the space of all names used in the course. The model is the oracle computation of the course on Turing degrees, read differently: the oracle is the input, and the output is a whole sequence. Its main property is that every computable function is continuous. The next lessons attach meanings to names, and the continuity of computable functions becomes the main tool to prove that a problem of analysis is not computable.

## Baire space

**Baire space** is the set $\bs$ of all functions $p : \nat \to \nat$, also called sequences. We write $\str$ for the set of finite sequences of numbers, or **strings**, coded by numbers in the usual way, and use the notation of Cantor space: $|\sigma|$ is the length of $\sigma$, $p \uh n = p(0) \cdots p(n-1)$, $\sigma \preceq \tau$ and $\sigma \prec p$ mean that $\sigma$ is a prefix, and $[\sigma] = \{ p \in \bs : \sigma \prec p \}$ is the **cylinder** of $\sigma$.

A set $\mathcal U \subseteq \bs$ is **open** if it is a union of cylinders, as for Cantor space (:ref{#def-open-closed}); a set $\mathcal A \subseteq \bs$ is **closed** if its complement is open. These are the open sets of the product topology of $\nat^\nat$, and of the metric $d(p, q) = 2^{-n}$, where $n$ is least with $p(n) \neq q(n)$ (and $d(p, p) = 0$): the ball of radius $2^{-n}$ around $p$ is the cylinder $[p \uh (n+1)]$. Cantor space $\cs$ is a closed subset of $\bs$, and its topology is the restriction of that of Baire space. Unlike Cantor space, Baire space is not compact: the cylinders $[n]$, $n \in \nat$, cover it, and no finite subfamily does.

A function $F$ defined on a subset of $\bs$, written $F :\subseteq \bs \to \bs$, is **continuous** if it is continuous for these metrics on its domain $\dom F$: for every $p \in \dom F$ and every $n$, there is $m$ such that $F(q) \uh n = F(p) \uh n$ for every $q \in \dom F \cap [p \uh m]$. In words, every finite part of the output depends only on a finite part of the input. A function $F :\subseteq \bs \to \nat$ is continuous if, for every $p \in \dom F$, there is $m$ with $F(q) = F(p)$ for every $q \in \dom F \cap [p \uh m]$.

## Computable functions on Baire space

Turing functionals have sets as oracles. A sequence $p \in \bs$ is given as an oracle through its graph $\{ \langle n, p(n) \rangle : n \in \nat \}$; we write $\Phi^p_e$ for the functional applied to this set. The pairing function satisfies $\langle n, k \rangle \geq n$, so the first $m$ bits of the characteristic sequence of the graph only concern the values $p(n)$ with $n < m$: they are determined by $p \uh m$. For a string $\sigma \in \str$ of length $m$, we write $\Phi^\sigma_e(n)\converge = v$ if the computation converges with output $v$ using only these $m$ bits, that is, if $\Phi^\tau_e(n)\converge = v$ for the string $\tau$ of the first $m$ bits of the graph of any $p \succ \sigma$ (:ref{#def-finite-oracle}).

:::lemma{#lem-type2-finite}
Let $e, n, v \in \nat$.
1. The relation $\Phi^\sigma_e(n)\converge = v$ is c.e. in $(\sigma, e, n, v)$; if it holds and $\sigma \preceq \tau$, then $\Phi^\tau_e(n)\converge = v$.
2. For $p \in \bs$, $\Phi^p_e(n)\converge = v$ if and only if $\Phi^{p \uh m}_e(n)\converge = v$ for some $m$. In that case, $\Phi^q_e(n)\converge = v$ for every $q \in [p \uh m]$.
:::

:::proof{of=lem-type2-finite}
The first item follows from :ref{#prop-oracle-stages}, items 1 and 2, since the string of the first $m$ bits of the graph is computed from $\sigma$. For the second, if $\Phi^p_e(n)\converge = v$ with use $u$, the computation reads only the first $u$ bits of the graph of $p$, which are determined by $p \uh u$; so $\Phi^{p \uh u}_e(n)\converge = v$. Conversely, if $\Phi^{p \uh m}_e(n)\converge = v$, then for every $q \in [p \uh m]$ the graph of $q$ begins with the same $m$ bits as that of $p$, and the use principle (:ref{#thm-use-principle}) gives $\Phi^q_e(n)\converge = v$.
:::

:::definition{#def-type2-computable}
1. A partial function $F :\subseteq \bs \to \bs$ is **computable** if there is a Turing functional $\Phi_e$ such that, for every $p \in \dom F$, the function $\Phi^p_e$ is total and equal to $F(p)$.
2. A partial function $F :\subseteq \bs \to \nat$ is **computable** if there is $e$ with $\Phi^p_e(0) = F(p)$ for every $p \in \dom F$.
3. A sequence $p \in \bs$ is **computable** if it is computable as a function $\nat \to \nat$.
:::

Nothing is required of $\Phi^p_e$ for $p \notin \dom F$: the functional may be partial there, or total. The domain of a computable function is part of its specification, and the function is computed on its domain only. Functions of several arguments are handled by pairing: $\langle p, q \rangle$ is the sequence with $\langle p, q \rangle(2n) = p(n)$ and $\langle p, q \rangle(2n + 1) = q(n)$, and $\langle p_0, p_1, \dots \rangle(\langle i, n \rangle) = p_i(n)$ codes a sequence of sequences.

Weihrauch defines computability on sequences over a finite alphabet with **Type-2 machines**: Turing machines with a read-only input tape holding the infinite input, work tapes, and a one-way output tape on which the machine writes forever. The output of a Type-2 machine is the infinite sequence written on its output tape, and it is defined if the machine writes infinitely many symbols. The two definitions give the same computable functions. A Type-2 machine computes $F(p)(n)$ by running until $n+1$ symbols have been written; conversely, a functional is simulated by computing $\Phi^p_e(0), \Phi^p_e(1), \dots$ in turn and writing each value when it is found. The definition by functionals lets us use the results of the course on Turing degrees directly.

:::example{#ex-type2-functions}
1. The function $F(p)(n) = p(n) + p(n+1)$ is computable on $\bs$, and so are the shift $p \mapsto (p(1), p(2), \dots)$, the projections $\langle p, q \rangle \mapsto p$ and the sum $\langle p, q \rangle \mapsto p + q$.
2. Let $D$ be the set of $p$ with $p(n) \neq 0$ for infinitely many $n$, and $F(p)$ the sequence of these $n$ in increasing order. Then $F :\subseteq \bs \to \bs$ is computable with domain $D$: the functional searches for the next non-zero value. It is total exactly on $D$, a $\Pi^0_2$ set.
3. A constant function with value $q$ is computable if and only if $q$ is computable.
4. The function $Z : \bs \to \nat$ with $Z(p) = 0$ if $p = 0^\infty$ and $Z(p) = 1$ otherwise is not computable, as the next theorem shows. It solves the problem $\mathsf{LPO}$ of :ref{to="reducibilities/weihrauch"}.
:::

:::figure[Continuity of the function $F(p)(n) = p(n) + p(n+1)$: the inputs $p$ and $q$ agree below $5$, so $F(p)$ and $F(q)$ agree below $4$.]{#fig-use-continuity}
<svg class="fig" viewBox="0 0 640 250" width="640" role="img" aria-label="Two inputs p and q agree on their first five values; the function F(p)(n) = p(n) + p(n+1) gives outputs that agree on their first four values"><defs><marker id="ah-cont2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><text x="36.0" y="70.0" text-anchor="end" class="math" font-size="16">p</text><rect x="50" y="50" width="30" height="30" class="cell head-cell"/><text x="65.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">3</text><rect x="80" y="50" width="30" height="30" class="cell head-cell"/><text x="95.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="110" y="50" width="30" height="30" class="cell head-cell"/><text x="125.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="140" y="50" width="30" height="30" class="cell head-cell"/><text x="155.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="170" y="50" width="30" height="30" class="cell head-cell"/><text x="185.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="200" y="50" width="30" height="30" class="cell"/><text x="215.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">9</text><rect x="230" y="50" width="30" height="30" class="cell"/><text x="245.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">2</text><rect x="260" y="50" width="30" height="30" class="cell"/><text x="275.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">6</text><text x="302.0" y="70.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="36.0" y="150.0" text-anchor="end" class="math" font-size="16">q</text><rect x="50" y="130" width="30" height="30" class="cell head-cell"/><text x="65.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">3</text><rect x="80" y="130" width="30" height="30" class="cell head-cell"/><text x="95.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="110" y="130" width="30" height="30" class="cell head-cell"/><text x="125.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="140" y="130" width="30" height="30" class="cell head-cell"/><text x="155.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">1</text><rect x="170" y="130" width="30" height="30" class="cell head-cell"/><text x="185.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="200" y="130" width="30" height="30" class="cell"/><text x="215.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="230" y="130" width="30" height="30" class="cell"/><text x="245.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">0</text><rect x="260" y="130" width="30" height="30" class="cell"/><text x="275.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">7</text><text x="302.0" y="150.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="366.0" y="70.0" text-anchor="end" class="math" font-size="16">F<tspan class="mrm">(</tspan>p<tspan class="mrm">)</tspan></text><rect x="380" y="50" width="30" height="30" class="cell head-cell"/><text x="395.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="410" y="50" width="30" height="30" class="cell head-cell"/><text x="425.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="440" y="50" width="30" height="30" class="cell head-cell"/><text x="455.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="470" y="50" width="30" height="30" class="cell head-cell"/><text x="485.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">6</text><rect x="500" y="50" width="30" height="30" class="cell"/><text x="515.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">14</text><rect x="530" y="50" width="30" height="30" class="cell"/><text x="545.0" y="70.0" text-anchor="middle" class="mrm" font-size="15">11</text><text x="572.0" y="70.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="366.0" y="150.0" text-anchor="end" class="math" font-size="16">F<tspan class="mrm">(</tspan>q<tspan class="mrm">)</tspan></text><rect x="380" y="130" width="30" height="30" class="cell head-cell"/><text x="395.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">4</text><rect x="410" y="130" width="30" height="30" class="cell head-cell"/><text x="425.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="440" y="130" width="30" height="30" class="cell head-cell"/><text x="455.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="470" y="130" width="30" height="30" class="cell head-cell"/><text x="485.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">6</text><rect x="500" y="130" width="30" height="30" class="cell"/><text x="515.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">5</text><rect x="530" y="130" width="30" height="30" class="cell"/><text x="545.0" y="150.0" text-anchor="middle" class="mrm" font-size="15">0</text><text x="572.0" y="150.0" text-anchor="middle" class="mrm muted" font-size="15">⋯</text><text x="65.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="95.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="125.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="155.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="185.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="215.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">5</text><text x="245.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">6</text><text x="275.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">7</text><text x="395.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">0</text><text x="425.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">1</text><text x="455.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">2</text><text x="485.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">3</text><text x="515.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">4</text><text x="545.0" y="42.0" text-anchor="middle" class="mrm muted" font-size="11">5</text><path d="M50,94 L50,102 L200,102 L200,94" class="accent-stroke" stroke-width="1.4"/><text x="125.0" y="120.0" text-anchor="middle" class="label">p ↾ 5 = q ↾ 5</text><path d="M380,94 L380,102 L500,102 L500,94" class="accent-stroke" stroke-width="1.4"/><text x="440.0" y="120.0" text-anchor="middle" class="label">F(p) ↾ 4 = F(q) ↾ 4</text><line x1="316" y1="65" x2="320" y2="65" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-cont2)"/><line x1="316" y1="145" x2="320" y2="145" class="muted-stroke" stroke-width="1.2" marker-end="url(#ah-cont2)"/><text x="318.0" y="58.0" text-anchor="middle" class="label">Φ</text><text x="318.0" y="138.0" text-anchor="middle" class="label">Φ</text><text x="320.0" y="205.0" text-anchor="middle" class="label">The output F(p)(n) = p(n) + p(n + 1) is computed with use n + 2: the first four outputs read only p ↾ 5,</text><text x="320.0" y="225.0" text-anchor="middle" class="label">so every input that agrees with p below 5 has the same first four outputs.</text></svg>
:::

## Computable functions are continuous

An algorithm that has written a finite part of its output has read only a finite part of its input, and every input with the same finite part leads to the same output so far (:ref{#fig-use-continuity}). This is the use principle, and it is the topological content of computability.

:::theorem{#thm-type2-continuous}
Every computable function $F :\subseteq \bs \to \bs$ or $F :\subseteq \bs \to \nat$ is continuous.
:::

:::proof{of=thm-type2-continuous}
Let $\Phi_e$ compute $F :\subseteq \bs \to \bs$, and let $p \in \dom F$ and $n \in \nat$. For each $i < n$, $\Phi^p_e(i)\converge = F(p)(i)$, so by :ref{#lem-type2-finite} there is $m_i$ such that $\Phi^q_e(i)\converge = F(p)(i)$ for every $q \in [p \uh m_i]$. Let $m = \max_{i < n} m_i$. For $q \in \dom F \cap [p \uh m]$, $F(q)(i) = \Phi^q_e(i) = F(p)(i)$ for every $i < n$, that is, $F(q) \uh n = F(p) \uh n$. The case $F :\subseteq \bs \to \nat$ is the case $n = 1$ of the same argument, applied to $\Phi^p_e(0)$.
:::

The function $Z$ of :ref{#ex-type2-functions} is not continuous at $0^\infty$: every cylinder $[0^m]$ contains $0^m 1 0^\infty$, where $Z$ takes the value $1$. So it is not computable. The argument is the one used for $\mathsf{LLPO}$ in :ref{to="reducibilities/weihrauch"}, and it is the **continuity method** of the whole course: to prove that a function is not computable, prove that it is not continuous, by exhibiting an input whose output requires information that no finite part of the input provides.

:::quiz[the continuity of computable functions]
In the proof of :ref{#thm-type2-continuous}, why is $m$ taken as a maximum over $i < n$?

- [x] Because each output value $F(p)(i)$ is guaranteed on its own cylinder $[p \uh m_i]$, and the $n$ values must be guaranteed simultaneously; the smallest of the $n$ cylinders, $[p \uh m]$, is contained in all of them.
- [ ] Because the use is increasing in $i$.

  The use of $\Phi^p_e(i)$ need not be monotone in $i$; the maximum is what makes the argument independent of this.
- [ ] Because $F(q)$ must be defined.

  Definedness of $F(q)$ is assumed: the statement only concerns $q \in \dom F$.

---

Why does the theorem not show that $F(q)$ is defined for every $q$ close to $p$?

- [x] Because the convergence of $\Phi^q_e(i)$ for finitely many $i$ says nothing about the other values; the domain of a computable function need not be open, as the set $D$ of :ref{#ex-type2-functions} shows.
- [ ] Because $F$ is only continuous, not uniformly continuous.

  Uniform continuity would not help: the issue is the totality of $\Phi^q_e$, which depends on infinitely many computations.
- [ ] Because Baire space is not compact.

  Compactness plays no role in this question.
:::

## Continuity is relative computability

The converse of :ref{#thm-type2-continuous} holds once an oracle is allowed: the oracle stores, for each finite part of the input, which finite part of the output it determines. A function $F :\subseteq \bs \to \bs$ is **computable relative to** $A \subseteq \nat$ if there is $e$ with $\Phi^{A \oplus p}_e = F(p)$ for every $p \in \dom F$, where the oracle $A \oplus p$ is the join of $A$ with the graph of $p$.

:::theorem{#thm-continuous-relative}
A function $F :\subseteq \bs \to \bs$ is continuous if and only if it is computable relative to some oracle $A \subseteq \nat$.
:::

:::proof{of=thm-continuous-relative}
If $F$ is computable relative to $A$, the proof of :ref{#thm-type2-continuous} applies with oracles $A \oplus p$: by the use principle, a computation converging with oracle $A \oplus p$ converges with the same value on every $A \oplus q$ with $q$ agreeing with $p$ on a long enough prefix.

Conversely, let $F$ be continuous. Let $A$ be the set of codes of pairs $(\sigma, \tau) \in \str \times \str$ such that $F(q) \succ \tau$ for every $q \in \dom F \cap [\sigma]$. On oracle $A \oplus p$ and input $n$, the functional searches for a pair $(m, \tau)$ with $|\tau| > n$ and $(p \uh m, \tau) \in A$, and outputs $\tau(n)$. If $p \in \dom F$, continuity gives $m$ with $F(q) \uh (n+1) = F(p) \uh (n+1)$ for every $q \in \dom F \cap [p \uh m]$, so $(p \uh m, F(p) \uh (n+1)) \in A$, and the search terminates. Whatever pair $(p \uh m, \tau)$ is found, $p$ itself belongs to $\dom F \cap [p \uh m]$, so $F(p) \succ \tau$ and the output $\tau(n)$ is $F(p)(n)$.
:::

The oracle $A$ of the proof is in general very complex, and need not be unique; the theorem only says that some oracle works. In particular, there are $2^{\aleph_0}$ continuous functions $\bs \to \bs$ (the constant functions already), and only countably many computable ones. Continuity is thus the non-uniform shadow of computability: a statement of the form "no continuous function does this" is a statement about computability relative to every oracle. For the problems of analysis studied in this course, the obstructions to computability that we find will mostly be of this kind.

Computable functions are closed under composition, with the natural domain: if $F$ and $G$ are computable, then $G \circ F$, defined on $\{ p \in \dom F : F(p) \in \dom G \}$, is computable. A functional computes $G(F(p))(n)$ by simulating the functional of $G$, and answering each of its oracle queries about the graph of $F(p)$ by computing the corresponding value of $F(p)$ with the functional of $F$. Continuous functions are closed under composition as well.

## Exercises

::::exercise{difficulty=1}
Show that the function $\sup :\subseteq \bs \to \nat$, defined on the bounded sequences by $\sup(p) = \max_n p(n)$, is not continuous, and that its restriction to the non-decreasing bounded sequences is not continuous either.

:::solution
Let $p = 0^\infty$, a non-decreasing bounded sequence with $\sup(p) = 0$. For every $m$, the sequence $0^m 1^\infty$ is non-decreasing, bounded, belongs to $[p \uh m]$, and has supremum $1$. So no cylinder around $p$ keeps the value $0$, and $\sup$ is not continuous at $p$, even on the non-decreasing sequences. This is a discrete form of the monotone convergence theorem; its continuous form is studied in the last lesson.
:::
::::

::::exercise{difficulty=2}
Let $F : \bs \to \bs$ be the function with $F(p) = 0^\infty$ if $p$ is computable and $F(p) = 1^\infty$ otherwise. Show that $F$ maps computable sequences to computable sequences and is not computable.

:::solution
$F(p)$ is one of the two computable sequences $0^\infty$ and $1^\infty$, for every $p$. Let $p$ be computable, so $F(p) = 0^\infty$. For every $m$, the cylinder $[p \uh m]$ contains a non-computable sequence $q$, since it contains $2^{\aleph_0}$ sequences and only countably many are computable; then $F(q)(0) = 1 \neq F(p)(0)$. So $F$ is not continuous at $p$, and not computable by :ref{#thm-type2-continuous}. Preserving computable points is thus much weaker than being computable; in analysis, the property of mapping computable points to computable points is sometimes called Banach–Mazur computability, and is not equivalent to computability either (Weihrauch, Section 9.1).
:::
::::

::::exercise{difficulty=2}
Show that every computable $G :\subseteq \bs \to \nat$ extends to a computable function whose domain is open, and that every computable $G :\subseteq \bs \to \bs$ extends to a computable function whose domain is $\Pi^0_2$. Is the domain $D$ of :ref{#ex-type2-functions} open?

:::solution
If $\Phi_e$ computes $G :\subseteq \bs \to \nat$, then $\Phi^p_e(0)$ converges on the open set $\mathcal U = \bigcup \{ [\sigma] : \Phi^\sigma_e(0)\converge \}$ (:ref{#lem-type2-finite}), which contains $\dom G$, and $p \mapsto \Phi^p_e(0)$ is computable on $\mathcal U$ and extends $G$. For $G :\subseteq \bs \to \bs$ computed by $\Phi_e$, the set $\{ p : \forall n\ \exists m\ \Phi^{p \uh m}_e(n)\converge \}$ is $\Pi^0_2$, contains $\dom G$, and $\Phi_e$ computes a total function on it; so every computable function $G :\subseteq \bs \to \bs$ extends to a computable function with a $\Pi^0_2$ domain (Weihrauch, Theorem 2.2.4, in the form "the domain of the function computed by a Type-2 machine is a $G_\delta$ set"). The set $D$ is $\Pi^0_2$ and not open: every cylinder $[\sigma]$ contains $\sigma 0^\infty \notin D$. The natural domains of the two kinds of functions differ accordingly.
:::
::::

## Notes and references

Type-2 machines and the Type-2 Theory of Effectivity are presented in Weihrauch, *Computable Analysis*, Chapter 2: machines and computable string functions in Section 2.1, continuity of computable functions in Section 2.2 (Theorem 2.2.3), where the natural domains of computable functions are also shown to be $G_\delta$ sets (Theorem 2.2.4). The characterization of continuous functions by relative computability, :ref{#thm-continuous-relative}, is the content of Weihrauch's representation of the continuous functions by programs with an oracle (Section 2.3, Lemma 2.3.11). Weihrauch works with sequences over a finite alphabet; Brattka, Hertling and Weihrauch use Baire space, as here. Computability on infinite sequences of numbers goes back to Turing's paper on computable numbers (1936, with a correction in 1937), and to the analyses of Grzegorczyk (1955) and Lacombe (1955); Kleene's functionals of type 2 are the same notion seen from recursion theory.

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Sections 2.1–2.3 and 9.1.
- V. Brattka, P. Hertling and K. Weihrauch, *A tutorial on computable analysis*, in S. B. Cooper, B. Löwe and A. Sorbi (eds.), *New Computational Paradigms*, Springer, 2008, 425–491.
- A. M. Turing, *On computable numbers, with an application to the Entscheidungsproblem*, Proceedings of the London Mathematical Society 42 (1936), 230–265; correction, 43 (1937), 544–546.
- A. Grzegorczyk, *Computable functionals*, Fundamenta Mathematicae 42 (1955), 168–202.
- D. Lacombe, *Extension de la notion de fonction récursive aux fonctions d'une ou plusieurs variables réelles*, Comptes Rendus de l'Académie des Sciences Paris 240 (1955), 2478–2480; 241 (1955), 13–14 and 151–153.
