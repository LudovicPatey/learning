---
title: Coding finite sets and sequences
summary: Ackermann's coding of finite sets by binary expansions, in IΔ₀ + exp; the elementary properties of coded sets; comprehension for bounded formulas; coded finite sequences, their operations and the bound on their codes.
duration: 50
prerequisites: [parikh, models-of-computation/coding-sequences]
---

Inside a model of arithmetic, the only objects are numbers, and finite sets, sequences, formulas or computations must be coded by numbers, with a membership relation defined by a simple formula whose properties are provable in a weak theory. In Ackermann's coding (1937), a number codes the set of positions of the digits $1$ in its binary expansion. Inside a non-standard model, the coded sets are the bounded sets that the model can "see"; they may have a non-standard number of elements.

The coding uses exponentiation, through the bounded formula $\varepsilon(x, y)$ of :ref{#fact-exp}. Throughout the lesson we work in $\mathrm I\Delta_0 + \mathrm{exp}$, so that $2^x$ exists for every $x$. Gödel's β-function (:ref{#def-beta}) avoids exponentiation, but its main lemma needs $\Sigma_1$ induction (Hájek and Pudlák, I.1.46–I.1.50).

## Ackermann membership

:::definition{#def-ack-membership}
The formula $i \in c$ is
$$
\exists p < c + 1\ \exists u < c + 1\ \exists q < p + p\ \big(\varepsilon(i, p) \wedge c = (p + p) \cdot u + q \wedge p \leq q\big).
$$
For a model $M$ and $c \in M$, the set **coded** by $c$ is $\mathrm{Ack}(c) = \{ i \in M : M \models i \in c \}$.
:::

The formula is bounded. In words: divide $c$ by $2^{i+1}$; then $i \in c$ if the remainder is at least $2^i$. In $\nat$, $i \in c$ says that the digit of $2^i$ in the binary expansion of $c$ is $1$, and $c = \sum_{i \in \mathrm{Ack}(c)} 2^i$. For instance, $13 = 2^3 + 2^2 + 2^0$ codes $\{0, 2, 3\}$, the number $2^a - 1$ codes $\{0, 1, \dots, a - 1\}$, and $0$ codes the empty set.

:::lemma{#lem-ack-basic}
$\mathrm I\Delta_0 + \mathrm{exp}$ proves:

1. if $i \in c$, then $2^i \leq c$, and therefore $i < c$;
2. (**splitting**) if $c = 2^k \cdot u + q$ with $q < 2^k$, then $i \in c \leftrightarrow i \in q$ for every $i < k$, and $k + j \in c \leftrightarrow j \in u$ for every $j$;
3. $c < 2^a$ if and only if every element of $c$ is less than $a$;
4. if $i \notin c$, then $c + 2^i$ codes the elements of $c$ together with $i$; if $i \in c$, then $c - 2^i$ codes the elements of $c$ other than $i$;
5. (**extensionality**) if $c, d < 2^a$ and $\forall i < a\ (i \in c \leftrightarrow i \in d)$, then $c = d$.
:::

The splitting property says that the digits of $c$ below position $k$ are those of the remainder $q$, and the digits from position $k$ on are those of the quotient $u$, shifted by $k$.

:::figure[The splitting property for $c = 365$ and $k = 5$. Dividing by $2^5$ gives $365 = 2^5 \cdot 11 + 13$. The digits of $c$ at positions $0$ to $4$ are those of $13$, and its digits at positions $5 + j$ are those of $11$ at position $j$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The binary digits of c = 365 = 2 to the 5 times 11 plus 13; the set coded by c is 0, 2, 3, 5, 6, 8; the digits below position 5 are those of 13, the digits from position 5 on are those of 11, shifted by 5"><rect x="70" y="52" width="44" height="34" class="cell"/><text x="92.0" y="75" text-anchor="middle" class="mrm" font-size="15">0</text><text x="92.0" y="104" text-anchor="middle" class="mrm" font-size="12">9</text><rect x="114" y="52" width="44" height="34" class="cell"/><rect x="118" y="56" width="36" height="26" class="soft-fill"/><text x="136.0" y="75" text-anchor="middle" class="mrm" font-size="15">1</text><text x="136.0" y="104" text-anchor="middle" class="mrm" font-size="12">8</text><rect x="158" y="52" width="44" height="34" class="cell"/><text x="180.0" y="75" text-anchor="middle" class="mrm" font-size="15">0</text><text x="180.0" y="104" text-anchor="middle" class="mrm" font-size="12">7</text><rect x="202" y="52" width="44" height="34" class="cell"/><rect x="206" y="56" width="36" height="26" class="soft-fill"/><text x="224.0" y="75" text-anchor="middle" class="mrm" font-size="15">1</text><text x="224.0" y="104" text-anchor="middle" class="mrm" font-size="12">6</text><rect x="246" y="52" width="44" height="34" class="cell"/><rect x="250" y="56" width="36" height="26" class="soft-fill"/><text x="268.0" y="75" text-anchor="middle" class="mrm" font-size="15">1</text><text x="268.0" y="104" text-anchor="middle" class="mrm" font-size="12">5</text><rect x="290" y="52" width="44" height="34" class="cell"/><text x="312.0" y="75" text-anchor="middle" class="mrm" font-size="15">0</text><text x="312.0" y="104" text-anchor="middle" class="mrm" font-size="12">4</text><rect x="334" y="52" width="44" height="34" class="cell"/><rect x="338" y="56" width="36" height="26" class="soft-fill"/><text x="356.0" y="75" text-anchor="middle" class="mrm" font-size="15">1</text><text x="356.0" y="104" text-anchor="middle" class="mrm" font-size="12">3</text><rect x="378" y="52" width="44" height="34" class="cell"/><rect x="382" y="56" width="36" height="26" class="soft-fill"/><text x="400.0" y="75" text-anchor="middle" class="mrm" font-size="15">1</text><text x="400.0" y="104" text-anchor="middle" class="mrm" font-size="12">2</text><rect x="422" y="52" width="44" height="34" class="cell"/><text x="444.0" y="75" text-anchor="middle" class="mrm" font-size="15">0</text><text x="444.0" y="104" text-anchor="middle" class="mrm" font-size="12">1</text><rect x="466" y="52" width="44" height="34" class="cell"/><rect x="470" y="56" width="36" height="26" class="soft-fill"/><text x="488.0" y="75" text-anchor="middle" class="mrm" font-size="15">1</text><text x="488.0" y="104" text-anchor="middle" class="mrm" font-size="12">0</text><line x1="290" y1="38" x2="290" y2="92" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><path d="M72,48 L72,42 L286,42 L286,48" class="muted-stroke" stroke-width="1.2"/><text x="179.0" y="32" text-anchor="middle" class="label">u = 11: k + j ∈ c iff j ∈ u</text><path d="M294,48 L294,42 L508,42 L508,48" class="muted-stroke" stroke-width="1.2"/><text x="401.0" y="32" text-anchor="middle" class="label">q = 13: i ∈ c iff i ∈ q, for i &lt; k</text><text x="30" y="104" text-anchor="middle" class="label">position</text><text x="300" y="152" text-anchor="middle" class="label">c = 365 = 2⁵ · 11 + 13, and the set coded by c is {0, 2, 3, 5, 6, 8}</text></svg>
:::

:::proof{of=lem-ack-basic}
By the uniqueness of division with remainder, $i \in c$ holds if and only if the remainder of $c$ modulo $2^{i+1}$ is at least $2^i$; when $2^i > c$, the remainder is $c$ itself and both sides fail. We use this form throughout.

1. If $i \in c$, with $p = 2^i$ and $c = (p + p)u + q$ as in the definition, then $2^i = p \leq q \leq c$, and $i < 2^i$.

2. Let $i < k$. Divide $q$ by $2^{i+1}$: $q = 2^{i+1} u'' + q''$ with $q'' < 2^{i+1}$. Since $2^k = 2^{i+1} \cdot 2^{k - i - 1}$, we get $c = 2^{i+1} (2^{k - i - 1} u + u'') + q''$. By uniqueness of division (:ref{#prop-idelta0-basic}), $q''$ is the remainder of both $c$ and $q$ modulo $2^{i+1}$, so $i \in c \leftrightarrow 2^i \leq q'' \leftrightarrow i \in q$. Now let $j$ be arbitrary, and divide $u$ by $2^{j+1}$: $u = 2^{j+1} v + r$ with $r < 2^{j+1}$. Then $c = 2^{k + j + 1} v + (2^k r + q)$, and $2^k r + q < 2^k r + 2^k \leq 2^{k + j + 1}$, since $r + 1 \leq 2^{j+1}$. So $2^k r + q$ is the remainder of $c$ modulo $2^{k + j + 1}$, and $k + j \in c$ if and only if $2^k r + q \geq 2^{k + j}$. Since $q < 2^k$, this holds if and only if $r \geq 2^j$, that is, if and only if $j \in u$.

3. If $c < 2^a$ and $i \in c$, then $2^i \leq c < 2^a$ by item 1, so $i < a$. Conversely, suppose $c \geq 2^a$. The set of $x \leq c$ with $2^x \leq c$ is defined by a bounded formula, contains $a$, and is bounded by $c$; let $i$ be its largest element, which exists by the least number principle applied to the set of its upper bounds. Then $2^i \leq c < 2^{i+1}$, so $c = 2^{i+1} \cdot 0 + c$ with remainder $c \geq 2^i$: hence $i \in c$, and $i \geq a$ since $2^a \leq c < 2^{i+1}$.

4. Suppose $i \notin c$, and write $c = 2^{i+1} u + q$ with $q < 2^{i+1}$; then $q < 2^i$. So $c + 2^i = 2^{i+1} u + (2^i + q)$ with $2^i + q < 2^{i+1}$. By item 2 with $k = i + 1$, the elements $\geq i + 1$ of $c$ and of $c + 2^i$ are both determined by $u$, hence equal, and the elements $\leq i$ are those of $q$ and of $2^i + q$ respectively. By item 2 with $k = i$, applied to $2^i + q = 2^i \cdot 1 + q$, the elements $< i$ of $2^i + q$ are those of $q$, and $i \in 2^i + q$ since $0 \in 1$. Finally $i \notin q$ by item 1, since $q < 2^i$. The case $i \in c$ is symmetric: $c = 2^{i+1} u + 2^i + r$ with $r < 2^i$, and $c - 2^i = 2^{i+1} u + r$.

5. Fix $a$ and $w = 2^a$, and apply bounded induction, with parameters $a$ and $w$, to the statement "$x \leq a \rightarrow$ for all $c, d < 2^x$ with the same elements below $x$, $c = d$", where $2^x$ is the element $p \leq w$ with $\varepsilon(x, p)$. For $x = 0$, $c = d = 0$. Let $c, d < 2^{x+1}$ have the same elements below $x + 1$. If $x \in c$, then $x \in d$, and $c - 2^x$ and $d - 2^x$ have the same elements, all below $x$, by item 4; by item 3 they are below $2^x$, so they are equal by the induction hypothesis, and $c = d$. If $x \notin c$, then $x \notin d$; by item 3, $c, d < 2^x$, and the induction hypothesis applies.
:::

## Comprehension for bounded formulas

:::theorem[Δ₀ comprehension]{#thm-delta0-comprehension}
For every $\Delta_0$ formula $\varphi(i, \bar p)$, $\mathrm I\Delta_0 + \mathrm{exp}$ proves
$$
\forall \bar p\ \forall a\ \exists c < 2^a\ \forall i < a\ \big(i \in c \leftrightarrow \varphi(i, \bar p)\big),
$$
and such a $c$ is unique.
:::

The code is built one element at a time, by induction on the length $x$ of the initial interval $[0, x)$ already decided. The statement "$\{ i < x : \varphi(i) \}$ has a code" quantifies over codes, and the only way to keep it bounded is to bound the codes: this is where $2^a$ is needed, as a parameter.

:::proof{of=thm-delta0-comprehension}
Fix $\bar p$ and $a$, and let $w = 2^a$. Apply bounded induction, with parameters $\bar p$, $a$ and $w$, to
$$
\psi(x) \equiv x \leq a \rightarrow \exists c < w\ \exists e < w + 1\ \big(\varepsilon(x, e) \wedge c < e \wedge \forall i < x\ (i \in c \leftrightarrow \varphi(i, \bar p))\big).
$$
For $x = 0$, take $c = 0$ and $e = 1$. Assume $\psi(x)$ and $x + 1 \leq a$, with $c < e = 2^x$. By :ref{#lem-ack-basic} (item 3), every element of $c$ is less than $x$; in particular $x \notin c$. If $\varphi(x, \bar p)$, let $c' = c + 2^x$, which codes the elements of $c$ together with $x$ by item 4; otherwise let $c' = c$. In both cases $c' < 2^x + 2^x = 2^{x+1} \leq 2^a$, and $c'$ codes $\{ i < x + 1 : \varphi(i, \bar p) \}$. So $\psi(x + 1)$ holds. By induction, $\psi(a)$ holds, which gives the required $c < 2^a$. Uniqueness is item 5 of :ref{#lem-ack-basic}.
:::

:::quiz[Δ₀ comprehension]
Why does the induction formula $\psi$ in the proof contain the bounds $c < w$ and $e < w + 1$, with $w = 2^a$ a parameter?

- [x] Without them, $\psi$ would begin with unbounded quantifiers $\exists c\ \exists e$, and bounded induction would not apply to it.
- [ ] To ensure that the code obtained is less than $2^a$.

  The bound $c < e = 2^x$ already gives this at $x = a$; the bound by $w$ is needed for the formula to be bounded at every $x$.
- [ ] Because $2^x$ might not exist for $x \leq a$.

  It exists, by $\mathrm{exp}$; the problem is the form of the formula, not existence.
:::

The proof uses only the existence of $2^a$: the smaller powers exist by :ref{#fact-exp}. So the theorem holds in every model of $\mathrm I\Delta_0$ for those $a$ such that $2^a$ exists. Unions, intersections and differences of coded sets are coded, by comprehension applied to the corresponding Boolean combinations, with $a$ above all the elements concerned.

## Finite sequences

A finite sequence is coded as the graph of a function on an initial interval, a set of pairs $\langle i, v \rangle$ coded by the pairing function of :ref{#fact-pairing}. We write $\langle i, v \rangle \in s$ for the bounded formula $\exists z < s + 1\ (z = \langle i, v \rangle \wedge z \in s)$.

:::definition{#def-coded-sequence}
$\mathrm{Seq}(s, \ell)$, "$s$ codes a sequence of length $\ell$", is the conjunction of
$$
\begin{gathered}
\forall z < s\ \big( z \in s \rightarrow \exists i < \ell\ \exists v < z + 1\ (z = \langle i, v \rangle) \big), \qquad \forall i < \ell\ \exists v < s\ (\langle i, v \rangle \in s), \\
\forall i < \ell\ \forall v < s\ \forall v' < s\ \big( \langle i, v \rangle \in s \wedge \langle i, v' \rangle \in s \rightarrow v = v' \big).
\end{gathered}
$$
:::

The formula is bounded, since $v \leq \langle i, v \rangle < s$ for every pair in $s$. If $\mathrm{Seq}(s, \ell)$ and $\mathrm{Seq}(s, \ell')$, then $\ell = \ell'$: if $\ell < \ell'$, some pair $\langle \ell, v \rangle$ belongs to $s$, but all pairs in $s$ have a first component less than $\ell$. We write $\mathrm{lh}(s) = \ell$ and, for $i < \ell$, $(s)_i$ for the unique $v$ with $\langle i, v \rangle \in s$. Since $\ell \leq s$, the formula $\mathrm{Seq}(s) \equiv \exists \ell < s + 1\ \mathrm{Seq}(s, \ell)$ is bounded, and so are the graphs of $\mathrm{lh}$ and of $(s)_i$. The empty sequence is coded by $0$.

:::proposition{#prop-seq-basic}
$\mathrm I\Delta_0 + \mathrm{exp}$ proves:

1. (**bound**) if $\mathrm{Seq}(s, \ell)$ and $(s)_i < b$ for every $i < \ell$, then $s < 2^{\langle \ell, b \rangle}$;
2. (**definable sequences**) for every $\Delta_0$ formula $\varphi(i, v, \bar p)$: if $\forall i < \ell\ \exists! v < b\ \varphi(i, v, \bar p)$, then there is a sequence $s$ of length $\ell$ with $\varphi(i, (s)_i, \bar p)$ for every $i < \ell$;
3. (**concatenation**) for every sequence $s$ of length $\ell$ and every $v$, there is a sequence $s^\frown v$ of length $\ell + 1$ with $(s^\frown v)_i = (s)_i$ for $i < \ell$ and $(s^\frown v)_\ell = v$;
4. (**restriction**) for every sequence $s$ of length $\ell$ and every $k \leq \ell$, there is a sequence $s \restriction k$ of length $k$ with $(s \restriction k)_i = (s)_i$ for $i < k$.
:::

:::proof{of=prop-seq-basic}
1. Every element of $s$ is a pair $\langle i, v \rangle$ with $i < \ell$ and $v < b$, hence less than $\langle \ell, b \rangle$ by the monotonicity of pairing (:ref{#fact-pairing}). By item 3 of :ref{#lem-ack-basic}, $s < 2^{\langle \ell, b \rangle}$.

2. By :ref{#thm-delta0-comprehension} with $a = \langle \ell, b \rangle$, there is $s$ coding $\{ z < a : \exists i < \ell\ \exists v < b\ (z = \langle i, v \rangle \wedge \varphi(i, v, \bar p)) \}$. Every pair $\langle i, v \rangle$ with $i < \ell$ and $v < b$ is less than $a$, so $s$ contains exactly the pairs $\langle i, v \rangle$ with $i < \ell$, $v < b$ and $\varphi(i, v, \bar p)$. By the hypothesis, this is the graph of a function on $[0, \ell)$, and the three clauses of :ref{#def-coded-sequence} hold.

3. and 4. Apply item 2 to the formulas $(i < \ell \wedge v = (s)_i) \vee (i = \ell \wedge v = v_0)$, with $b = s + v_0 + 1$, and $v = (s)_i$, with $b = s$.
:::

:::quiz[coded sequences]
In the proof of item 2 of :ref{#prop-seq-basic}, why is the hypothesis that the values $v$ are bounded by $b$ needed?

- [x] Comprehension produces codes of subsets of a bounded interval $[0, a)$; the pairs $\langle i, v \rangle$ of the graph must all lie in such an interval, which requires a bound on $v$.
- [ ] To make the function $i \mapsto v$ total.

  Totality on $[0, \ell)$ is part of the hypothesis $\forall i < \ell\ \exists! v$; the bound plays no role in it.
- [ ] To make the formula $\varphi$ bounded.

  $\varphi$ is bounded by hypothesis; the bound $b$ concerns the size of the code.
:::

## Exercises


::::exercise{difficulty=2}
(**Finite pigeonhole principle.**) Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves: if $s$ is a sequence of length $a + 1$ with $(s)_i < a$ for every $i \leq a$, then $(s)_i = (s)_j$ for some $i < j \leq a$.

:::solution
Fix $a$ and the parameter $B = 2^{\langle a + 1, a \rangle}$, which bounds the codes of all sequences of length $x + 1 \leq a + 1$ with values below $x \leq a$, by item 1 of :ref{#prop-seq-basic} and the monotonicity of pairing. Let $\psi(x)$ say: no $s < B$ is an injective sequence of length $x + 1$ with values below $x$. It is bounded, with parameter $B$. $\psi(0)$ holds, since no value is below $0$. Suppose $\psi(x)$ fails at $x + 1 \leq a$, witnessed by an injective $s$ of length $x + 2$ with values below $x + 1$. If no entry equals $x$, then $s \restriction (x + 1)$ is injective with values below $x$. If $(s)_j = x$ with $j = x + 1$, the same restriction works. If $(s)_j = x$ with $j \leq x$, let $s'$ be the sequence of length $x + 1$ equal to $s$ except that $(s')_j = (s)_{x+1}$, given by item 2 of :ref{#prop-seq-basic}; it is injective with values below $x$, because $(s)_{x+1} \neq x$. In each case $\psi(x)$ fails. By bounded induction, $\psi(a)$ holds.
:::
::::


## Notes and references

The coding of hereditarily finite sets by binary expansions is due to Ackermann (1937). The development in $\mathrm I\Delta_0 + \mathrm{exp}$ follows Hájek and Pudlák, Chapter I, Section 1(b) (bits, Lemma I.1.31; elementary properties, Lemmas I.1.32–I.1.34; comprehension, Theorem I.1.36; extensionality, Corollary I.1.38; sequences, Definition I.1.42 and Theorem I.1.43; pigeonhole principle for finite sets, Theorem I.1.41), where exponentiation is a function symbol of the language; the formula of :ref{#def-ack-membership} is the one of Wong's Lecture 2, with the bounded graph of exponentiation. Codings of sequences that work without exponentiation, or without any induction, exist: see Hájek and Pudlák, Chapter V, Section 3, and Jeřábek (2012).

- W. Ackermann, *Die Widerspruchsfreiheit der allgemeinen Mengenlehre*, Mathematische Annalen 114 (1937), 305–315.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(b).
- E. Jeřábek, *Sequence coding without induction*, Mathematical Logic Quarterly 58 (2012), 244–248.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 2 and 3.
