---
title: Kleene's O
summary: Kleene's system of notations O, its partial order and the inversion principle, the computable well-orderings of the notations below a given one, and addition of notations by effective transfinite recursion.
duration: 45
prerequisites: [computable-well-orderings, fundamentals/fixed-point]
---

A computable well-ordering determines an ordinal, but hides how this ordinal is built: by :ref{#prop-wo-not-transparent}, one cannot decide from an index whether the type is a successor. Kleene's notations make the construction explicit. A notation is a number that says whether the ordinal is zero, a successor or a limit; for a successor, it contains a notation of the predecessor, and for a limit, a program enumerating notations of an increasing sequence converging to it. Functions on ordinals can then be defined by recursion on notations, with the recursion theorem providing the self-reference. This lesson defines the set $\mathcal O$ of notations, shows that every ordinal with a notation is computable, and introduces this **effective transfinite recursion** with the addition of notations. The next lesson uses it to prove the converse, due to Markwald and Kleene.

## Kleene's O

:::definition[Kleene]{#def-kleene-o}
The set $\mathcal O \subseteq \nat$ of **notations**, the map $a \mapsto |a|$ from $\mathcal O$ to ordinals, and the relation $<_{\mathcal O}$ are defined simultaneously as the least sets satisfying:

1. $1 \in \mathcal O$ and $|1| = 0$;
2. if $a \in \mathcal O$, then $2^a \in \mathcal O$, $|2^a| = |a| + 1$, and $b <_{\mathcal O} 2^a$ if and only if $b = a$ or $b <_{\mathcal O} a$;
3. if $\Phi_e$ is total, $\Phi_e(n) \in \mathcal O$ and $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$ for every $n$, then $3 \cdot 5^e \in \mathcal O$, $|3 \cdot 5^e| = \sup_n |\Phi_e(n)|$, and $b <_{\mathcal O} 3 \cdot 5^e$ if and only if $b <_{\mathcal O} \Phi_e(n)$ for some $n$.

An ordinal is **constructive** if it is $|a|$ for some $a \in \mathcal O$.
:::

A notation tells which case applies, by its prime factorization, and gives the predecessor or a fundamental sequence. The cases are exclusive on $\mathcal O$: $1 = 2^0$, but $0 \notin \mathcal O$, so $1$ is not of the form $2^a$ with $a \in \mathcal O$. A finite ordinal $n$ has exactly one notation, obtained from $1$ by $n$ applications of $a \mapsto 2^a$, but every infinite constructive ordinal has infinitely many: a limit has one for each program of each of its fundamental sequences, and $\lambda + n$ has one for each notation of $\lambda$. The relation $<_{\mathcal O}$ is a partial order on $\mathcal O$ with $b <_{\mathcal O} a \Rightarrow |b| < |a|$, but two notations of the same ordinal on different branches are incomparable.

:::example{#ex-notations}
The notations of $0, 1, 2, 3$ are $1$, $2 = 2^1$, $4 = 2^2$ and $16 = 2^4$. Let $e$ be an index of the total computable function $n \mapsto$ (the notation of $n$), obtained by iterating $a \mapsto 2^a$ from $1$. Its values are in $\mathcal O$ and $<_{\mathcal O}$-increasing, so $3 \cdot 5^e \in \mathcal O$ is a notation of $\omega$, and $2^{3 \cdot 5^e}$ is a notation of $\omega + 1$. If $e' \neq e$ is another index of the same function, then $3 \cdot 5^{e'}$ is another notation of $\omega$. The notations below each of them are the finite ones, so neither is below the other, nor below a successor of the other. Iterating $a \mapsto 2^a$ from $3 \cdot 5^e$ gives a computable $<_{\mathcal O}$-increasing sequence, whose limit is a notation of $\omega \cdot 2$.
:::

:::figure[The beginning of $\mathcal O$. Arrows point from a notation to its successor. The notations of the finite ordinals form a single chain; above it, $\mathcal O$ branches, with one branch for each notation of $\omega$. Notations on different branches are incomparable for $<_{\mathcal O}$.]
<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="Kleene's O near omega: the chain of notations of the finite ordinals, and two notations of omega on different branches, each with its successors"><defs><marker id="co-otree" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><circle cx="40" cy="120" r="4" class="ink-fill"/><text x="40" y="144" text-anchor="middle" class="mrm" font-size="15">1</text><circle cx="100" cy="120" r="4" class="ink-fill"/><text x="100" y="144" text-anchor="middle" class="mrm" font-size="15">2</text><circle cx="160" cy="120" r="4" class="ink-fill"/><text x="160" y="144" text-anchor="middle" class="mrm" font-size="15"><tspan class="mrm">2</tspan><tspan font-size="10" dy="-7">2</tspan></text><circle cx="220" cy="120" r="4" class="ink-fill"/><text x="220" y="144" text-anchor="middle" class="mrm" font-size="15"><tspan class="mrm">2</tspan><tspan font-size="10" dy="-7">4</tspan></text><line x1="46" y1="120" x2="93" y2="120" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><line x1="106" y1="120" x2="153" y2="120" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><line x1="166" y1="120" x2="213" y2="120" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><text x="262.0" y="125.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><line x1="282" y1="120" x2="322" y2="58" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#co-otree)"/><circle cx="330" cy="52" r="5" class="accent-fill"/><text x="330" y="40" text-anchor="middle" font-size="15"><tspan class="mrm">3·5</tspan><tspan class="math" font-size="10" dy="-7">e</tspan></text><line x1="337" y1="52" x2="413" y2="52" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><circle cx="420" cy="52" r="4" class="ink-fill"/><line x1="427" y1="52" x2="503" y2="52" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><circle cx="510" cy="52" r="4" class="ink-fill"/><text x="560.0" y="57.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><text x="420.0" y="40.0" text-anchor="middle" class="label" font-size="12">|·| = ω + 1</text><text x="510.0" y="40.0" text-anchor="middle" class="label" font-size="12">|·| = ω + 2</text><line x1="282" y1="120" x2="322" y2="182" class="muted-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#co-otree)"/><circle cx="330" cy="188" r="5" class="accent-fill"/><text x="330" y="214" text-anchor="middle" font-size="15"><tspan class="mrm">3·5</tspan><tspan class="math" font-size="10" dy="-7">e′</tspan></text><line x1="337" y1="188" x2="413" y2="188" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><circle cx="420" cy="188" r="4" class="ink-fill"/><line x1="427" y1="188" x2="503" y2="188" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-otree)"/><circle cx="510" cy="188" r="4" class="ink-fill"/><text x="560.0" y="193.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><text x="420.0" y="176.0" text-anchor="middle" class="label" font-size="12">|·| = ω + 1</text><text x="510.0" y="176.0" text-anchor="middle" class="label" font-size="12">|·| = ω + 2</text><text x="130.0" y="98.0" text-anchor="middle" class="label" font-size="12">notations of 0, 1, 2, 3</text><text x="332.0" y="125.0" text-anchor="start" class="label" font-size="12">incomparable</text></svg>
:::

Since $\mathcal O$ is defined as the least set closed under three rules, each of its elements comes from one of the rules. This **inversion** principle is used in every proof that a number is not a notation.

:::lemma[Inversion]{#lem-o-inversion}
1. $0 \notin \mathcal O$, and if $a \neq 0$ and $2^a \in \mathcal O$, then $a \in \mathcal O$.
2. If $3 \cdot 5^e \in \mathcal O$, then $\Phi_e$ is total, and $\Phi_e(n) \in \mathcal O$ and $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$ for every $n$.
3. If $a \in \mathcal O$ and $b <_{\mathcal O} a$, then $b \in \mathcal O$ and $|b| < |a|$.
:::

:::proof{of=lem-o-inversion}
Let $\mathcal O^*$ be the set of $a \in \mathcal O$ such that $a = 1$, or $a = 2^c$ for some $c \in \mathcal O$, or $a = 3 \cdot 5^e$ for some $e$ satisfying the conclusion of (2), and such that every $b <_{\mathcal O} a$ is in $\mathcal O$ and satisfies $|b| < |a|$. Then $\mathcal O^*$, with the restriction of $<_{\mathcal O}$, satisfies the three rules of :ref{#def-kleene-o}: $1 \in \mathcal O^*$; if $a \in \mathcal O^*$, then $2^a = 2^c$ with $c = a \in \mathcal O$, and the elements below $2^a$ are $a$ and the elements below $a$, of ordinals at most $|a| < |a| + 1$; the limit rule is checked in the same way, using $|\Phi_e(n)| < |\Phi_e(n+1)| \leq \sup_m |\Phi_e(m)|$. By minimality, $\mathcal O \subseteq \mathcal O^*$. Now $0$ is neither $1$, nor a power of $2$, nor of the form $3 \cdot 5^e$, so $0 \notin \mathcal O$. If $a \neq 0$, then $2^a \neq 1$ and $2^a$ is not of the form $3 \cdot 5^e$; so if $2^a \in \mathcal O = \mathcal O^*$, then $2^a = 2^c$ with $c \in \mathcal O$, and $c = a$. Items (2) and (3) are part of the definition of $\mathcal O^*$, by unique factorization.
:::

:::proposition{#prop-kleene-o-basic}
1. For $a \in \mathcal O$, the set $\{ b : b <_{\mathcal O} a \}$ is well-ordered by $<_{\mathcal O}$, with order type $|a|$, and $\{ |b| : b <_{\mathcal O} a \} = |a|$. In particular the constructive ordinals are closed downward.
2. There is a c.e. relation $R$ such that for every $a \in \mathcal O$ and every $b$, $b <_{\mathcal O} a$ if and only if $(b, a) \in R$.
:::

:::proof{of=prop-kleene-o-basic}
1. By induction along the inductive definition. For $1$, the set is empty. For $2^a$, the set is $\{ b : b <_{\mathcal O} a \} \cup \{ a \}$, of type $|a| + 1$, with ordinals $|a| \cup \{ |a| \} = |a| + 1$. For $3 \cdot 5^e$, the set is the increasing union of the sets below $\Phi_e(n)$, each an initial segment of the next one by the induction hypothesis and the fact that $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$; its type and its set of ordinals are the supremum $\sup_n |\Phi_e(n)|$.
2. Let $R$ be the least relation containing, for every $a \geq 1$, the pair $(a, 2^a)$ and the pairs $(b, 2^a)$ with $(b, a) \in R$, and containing $(b, 3 \cdot 5^e)$ whenever $\Phi_e(n)\converge$ and $(b, \Phi_e(n)) \in R$ or $b = \Phi_e(n)$, for some $n$. It is generated by c.e. rules, so it is c.e. By induction on $a \in \mathcal O$, $R(\cdot, a)$ is $\{ b : b <_{\mathcal O} a \}$; the restriction $a \geq 1$ ensures that $R(\cdot, 1)$ is empty.
:::

The relation $<_{\mathcal O}$ is therefore c.e. on each initial segment, uniformly in a notation of its upper bound. The set $\mathcal O$ itself is not c.e., nor even arithmetic: the lesson on $\Pi^1_1$ sets shows that it is $\Pi^1_1$-complete (:ref{#thm-o-complete}), hence not $\Sigma^1_1$.

## From notations to well-orderings and back

:::proposition{#prop-constructive-computable}
Every constructive ordinal is computable. Moreover, there is a total computable function that maps every $a \in \mathcal O$ to an index of a computable well-ordering of type $|a|$.
:::

:::proof{of=prop-constructive-computable}
Let $R$ be the c.e. relation of :ref{#prop-kleene-o-basic} (2), and let $S_a$ be the set of pairs $(b, c)$ with $(b, a) \in R$, $(c, a) \in R$, and $b = c$ or $(b, c) \in R$. It is c.e., uniformly in $a$. For $a \in \mathcal O$, every $c <_{\mathcal O} a$ is in $\mathcal O$ (:ref{#lem-o-inversion}), so $S_a$ is the order $\leq_{\mathcal O}$ on $\{ b : b <_{\mathcal O} a \}$, a well-ordering of type $|a|$ by :ref{#prop-kleene-o-basic} (1).

It is decidable whether $a$ is one of the notations $1, 2^1, 2^{2^1}, \dots$ of the finite ordinals; if it is the notation of $n$, output a fixed index of the usual order on $\{ 0, \dots, n - 1 \}$. Otherwise, if $a \in \mathcal O$, the sequence $a, a_1, a_2, \dots$ with $a = 2^{a_1}$, $a_1 = 2^{a_2}$, … reaches a notation $3 \cdot 5^e \leq_{\mathcal O} a$, so $|a| \geq \omega$ and $S_a$ has an infinite field; output the index given by :ref{#prop-computable-ordinals-basic} (3) for $S_a$. This function is total computable, and its value on $a \in \mathcal O$ is an index of a computable well-ordering of type $|a|$.
:::

The converse requires arithmetic on notations. Addition is the first example of **effective transfinite recursion**. Classically, $\alpha + \beta$ is defined by recursion on $\beta$, with three cases. On notations, the three cases are recognized from the prime factorization of $b$, and the recursion is carried out by a program that calls itself, which the recursion theorem allows. Two features recur in every later use of the method. First, the program is total without any assumption on its input: in the limit case it does not evaluate the fundamental sequence, it only computes an index of a new sequence. Second, the properties of the output (being a notation, having the right ordinal) are proved separately, by induction on the notation $b$.

:::lemma{#lem-notation-sum}
There is a total computable function $+_{\mathcal O}$ such that for all $a, b \in \mathcal O$, $a +_{\mathcal O} b \in \mathcal O$, $|a +_{\mathcal O} b| = |a| + |b|$, $a \leq_{\mathcal O} a +_{\mathcal O} b$, $a <_{\mathcal O} a +_{\mathcal O} b$ when $b \neq 1$, and $a +_{\mathcal O} c <_{\mathcal O} a +_{\mathcal O} b$ whenever $c <_{\mathcal O} b$.
:::

:::proof{of=lem-notation-sum}
By the recursion theorem (:ref{#cor-self-reference}), applied to a pair $(a, b)$ as input, there is a partial computable function $+_{\mathcal O}$ satisfying
$$
\begin{aligned}
a +_{\mathcal O} 1 &= a, \\
a +_{\mathcal O} 2^c &= 2^{a +_{\mathcal O} c} \quad \text{for } c \geq 1, \\
a +_{\mathcal O} 3 \cdot 5^e &= 3 \cdot 5^{h(a, e)},
\end{aligned}
$$
where $h(a, e)$ is an index of the function $n \mapsto a +_{\mathcal O} \Phi_e(n)$, computed from $a$, $e$ and the index of $+_{\mathcal O}$ given by the recursion theorem, and $a +_{\mathcal O} b = 1$ for all other $b$. It is total, by induction on $b$: the successor case calls the function on $c < 2^c$, and the limit case only computes an index, without evaluating $\Phi_e$.

The properties are proved by induction on $b \in \mathcal O$. For $b = 1$ they are immediate. For $b = 2^c$ with $c \in \mathcal O$, the notation $a +_{\mathcal O} b = 2^{a +_{\mathcal O} c}$ belongs to $\mathcal O$, with $|a +_{\mathcal O} b| = |a| + |c| + 1 = |a| + |b|$, and $a \leq_{\mathcal O} a +_{\mathcal O} c <_{\mathcal O} a +_{\mathcal O} b$; if $d <_{\mathcal O} b$, then $d \leq_{\mathcal O} c$, so $a +_{\mathcal O} d \leq_{\mathcal O} a +_{\mathcal O} c <_{\mathcal O} a +_{\mathcal O} b$. For $b = 3 \cdot 5^e$, the terms $a +_{\mathcal O} \Phi_e(n)$ are in $\mathcal O$, and $a +_{\mathcal O} \Phi_e(n) <_{\mathcal O} a +_{\mathcal O} \Phi_e(n+1)$ by the last property for $\Phi_e(n+1)$; so $a +_{\mathcal O} b \in \mathcal O$, and $|a +_{\mathcal O} b| = \sup_n (|a| + |\Phi_e(n)|) = |a| + |b|$, since addition is continuous in its right argument. If $d <_{\mathcal O} b$, then $d <_{\mathcal O} \Phi_e(n)$ for some $n$, and $a +_{\mathcal O} d <_{\mathcal O} a +_{\mathcal O} \Phi_e(n) <_{\mathcal O} a +_{\mathcal O} b$. Finally $a \leq_{\mathcal O} a +_{\mathcal O} \Phi_e(0) <_{\mathcal O} a +_{\mathcal O} b$.
:::

:::quiz[effective transfinite recursion]
Why is the function $+_{\mathcal O}$ total, even on numbers $b$ that are not notations?

- [x] Each call on $b = 2^c$ makes one call on the smaller number $c$, and a call on $b = 3 \cdot 5^e$ only computes an index $h(a, e)$, without running $\Phi_e$; so every computation terminates, by induction on $b$ as a number.
- [ ] Because the recursion theorem always produces total functions.

  It produces a fixed point of the defining equations, which may be partial: the equation $\Phi_e(x) \simeq \Phi_e(x) + 1$ has only the nowhere defined solution.
- [ ] Because the induction on $b \in \mathcal O$ shows that $a +_{\mathcal O} b$ is a notation.

  That induction concerns only notations $b$, and assumes that the values are defined. Totality is proved separately, for all numbers.
:::

The sum of notations is the tool of the next lesson, which proves the converse of :ref{#prop-constructive-computable}. Its uses in the course on hyperarithmetic sets follow the same pattern: a program defined by the recursion theorem, total by construction, whose values are shown to be correct by induction on notations.

## Exercises

::::exercise{difficulty=1}
Show that $\varepsilon_0 = \sup \{ \omega, \omega^\omega, \omega^{\omega^\omega}, \dots \}$ is computable.

:::solution
By the recursion theorem, as in :ref{#lem-notation-sum}, there is a total computable function $p$ with $p(1) = 2^1$ (the notation of $1$), $p(2^c) = 3 \cdot 5^{k(c)}$ for $c \geq 1$, where $\Phi_{k(c)}(0) = p(c)$ and $\Phi_{k(c)}(n+1) = \Phi_{k(c)}(n) +_{\mathcal O} p(c)$, and $p(3 \cdot 5^e) = 3 \cdot 5^{k'(e)}$ with $\Phi_{k'(e)}(n) = p(\Phi_e(n))$. By induction on $b \in \mathcal O$, $p(b) \in \mathcal O$, $|p(b)| = \omega^{|b|}$, and $c <_{\mathcal O} b$ implies $p(c) <_{\mathcal O} p(b)$. For $b = 2^c$: $p(c) \neq 1$ since $|p(c)| \geq 1$, so by :ref{#lem-notation-sum} the notations $\Phi_{k(c)}(n)$ are $<_{\mathcal O}$-increasing, of types $\omega^{|c|} \cdot (n+1)$, with supremum $\omega^{|c| + 1}$; and $c' \leq_{\mathcal O} c$ gives $p(c') \leq_{\mathcal O} p(c) = \Phi_{k(c)}(0) <_{\mathcal O} p(b)$. For $b = 3 \cdot 5^e$, the sequence $p(\Phi_e(n))$ is $<_{\mathcal O}$-increasing by the induction hypothesis, and its supremum is $\omega^{|b|}$ by continuity of exponentiation.

Let $x_0 = p(2^1)$, a notation for $\omega$, and $x_{n+1} = x_n +_{\mathcal O} p(x_n)$. Then $x_n <_{\mathcal O} x_{n+1}$, since $p(x_n) \neq 1$, and $|x_{n+1}| \geq \omega^{|x_n|}$, so $|x_n|$ is at least the tower $\omega^{\omega^{\cdots}}$ of height $n + 1$. The sequence $(x_n)$ is computable, and $3 \cdot 5^e$ for an index $e$ of it is a notation of an ordinal at least $\varepsilon_0$. The constructive ordinals being closed downward, $\varepsilon_0$ is constructive, hence computable by :ref{#prop-constructive-computable}.
:::
::::

## Notes and references

Church and Kleene (1936–1938) introduced constructive ordinals and the system $\mathcal O$. The recursion theorem first appeared in Kleene's paper of 1938 on notations, where it serves effective transfinite recursions such as the addition of notations. Monin and Patey define $\mathcal O$, the addition of notations and the conversion of notations into well-orderings in the section *Effective ordinals* of their chapter on transfinite numbers, and draw the partial order $<_{\mathcal O}$ in their motivating section on Kleene's $\mathcal O$. Sacks's monograph is the standard reference for higher computability theory.

- S. C. Kleene, *On notation for ordinal numbers*, Journal of Symbolic Logic 3 (1938), 150–155.
- B. Monin and L. Patey, *Computability theory*, chapter *Transfinite numbers*, sections *Kleene's O* and *Effective ordinals*.
- G. E. Sacks, *Higher Recursion Theory*, Perspectives in Mathematical Logic, Springer, 1990.
