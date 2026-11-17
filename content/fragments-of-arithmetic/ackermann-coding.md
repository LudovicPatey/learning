---
title: Coding finite sets
summary: Ackermann's coding of finite sets by binary expansions, in IΔ₀ + exp; splitting, insertion and removal, extensionality; comprehension for bounded formulas.
duration: 30
prerequisites: [parikh]
---

Inside a model of arithmetic, the only objects are numbers, and finite sets, sequences, formulas or computations must be coded by numbers, with a membership relation defined by a simple formula whose properties are provable in a weak theory. In Ackermann's coding (1937), a number codes the set of positions of the digits $1$ in its binary expansion. Inside a non-standard model, the coded sets are the bounded sets that the model can "see"; they may have a non-standard number of elements. This lesson codes finite sets and proves comprehension for bounded formulas; the next one codes finite sequences.

The coding uses exponentiation, through the bounded formula $\varepsilon(x, y)$ of :ref{#fact-exp}. Throughout the lesson we work in $\mathrm I\Delta_0 + \mathrm{exp}$, so that $2^x$ exists for every $x$. Gödel's β-function (:ref{#def-beta}) avoids exponentiation, but the proof that it codes every sequence of a non-standard length uses $\Sigma_1$ induction (Hájek and Pudlák, I.1.46–I.1.50).

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


The proofs of :ref{#lem-ack-basic} and of the theorem only use powers $2^x$ with $x \leq a$, and these exist as soon as $2^a$ exists, by :ref{#fact-exp}. So the theorem holds in every model of $\mathrm I\Delta_0$ for those $a$ such that $2^a$ exists. Unions, intersections and differences of coded sets are coded, by comprehension applied to the corresponding Boolean combinations, with $a$ above all the elements concerned.

## Exercises

::::exercise{#ex-ack-parity difficulty=1 objective="Relate Ackermann membership to the parity of a quotient, using the uniqueness of division."}
Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves: $i \in c$ if and only if the quotient of $c$ by $2^i$ is odd. In $\nat$, this says that the digit of $2^i$ in $c$ is the parity of $\lfloor c / 2^i \rfloor$.

:::solution
Divide $c$ by $2^i$, $c = 2^i v + r$ with $r < 2^i$, and divide $v$ by $2$, $v = 2u + e$ with $e \leq 1$ (:ref{#prop-idelta0-basic}). Then $c = 2^{i+1} u + (2^i e + r)$ and $2^i e + r < 2^i + 2^i = 2^{i+1}$. By the uniqueness of division, $2^i e + r$ is the remainder of $c$ modulo $2^{i+1}$. It is at least $2^i$ if $e = 1$, and equal to $r < 2^i$ if $e = 0$. So $i \in c$ if and only if $e = 1$, that is, if and only if $v$ is odd.
:::
::::

## Notes and references

The coding of hereditarily finite sets by binary expansions is due to Ackermann (1937). The development in $\mathrm I\Delta_0 + \mathrm{exp}$ follows Hájek and Pudlák, Chapter I, Section 1(b) (bits, Lemma I.1.31; elementary properties, Lemmas I.1.32–I.1.34; comprehension, Theorem I.1.36; extensionality, Corollary I.1.38), where exponentiation is a function symbol of the language; the formula of :ref{#def-ack-membership} follows Wong's Lecture 2, with the bounded graph of exponentiation. Codings that work without exponentiation are discussed in the notes of the next lesson.

- W. Ackermann, *Die Widerspruchsfreiheit der allgemeinen Mengenlehre*, Mathematische Annalen 114 (1937), 305–315.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(b).
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 2.

:::::exercises
::::exercise{#ex-ack-examples difficulty=1 objective="Compute Ackermann codes in $\nat$, and derive the codes of singletons and of shifted sets from the splitting property."}
1. In $\nat$, find the set coded by $100$ and the code of $\{1, 3, 4\}$.
2. Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves that $2^a$ codes $\{a\}$: $i \in 2^a \leftrightarrow i = a$.
3. Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves that $c \cdot 2^k$ codes $\{ k + j : j \in c \}$: $i \in c \cdot 2^k$ if and only if $i = k + j$ for some $j \in c$.

:::solution
1. $100 = 64 + 32 + 4 = 2^6 + 2^5 + 2^2$ codes $\{2, 5, 6\}$, and $\{1, 3, 4\}$ is coded by $2 + 8 + 16 = 26$.

2. First, $i \in 1 \leftrightarrow i = 0$: if $i \in 1$, then $2^i \leq 1$ by :ref{#lem-ack-basic}, so $i = 0$, since $i \geq 1$ would give $2^i \geq 2$; and $1 = 2 \cdot 0 + 1$ with remainder $1 \geq 2^0$, so $0 \in 1$. Also $0$ codes the empty set, since $i \in 0$ would give $2^i \leq 0$. Apply the splitting property to $2^a = 2^a \cdot 1 + 0$: for $i < a$, $i \in 2^a \leftrightarrow i \in 0$, which fails; for every $j$, $a + j \in 2^a \leftrightarrow j \in 1 \leftrightarrow j = 0$. Every $i \geq a$ is $a + j$ for some $j$, by axiom 5. So $a$ is the only element of $2^a$.

3. Apply the splitting property to $c \cdot 2^k = 2^k \cdot c + 0$: no $i < k$ belongs to it, and $k + j$ belongs to it if and only if $j \in c$. Every $i \geq k$ has the form $k + j$.
:::
::::

::::exercise{#ex-ack-subset-order difficulty=2 objective="Prove by bounded induction, with a power as a parameter, that Ackermann codes are monotone for inclusion."}
Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves: if every element of $c$ is an element of $d$, then $c \leq d$, and $c < d$ unless $c = d$.

:::solution
Let $a = c + d$; then $c, d \leq a < 2^a$. Let $w = 2^a$, and apply bounded induction, with parameters $a$ and $w$, to the statement $\psi(x)$: if $x \leq a$, then for all $c', d' < w$ with $c', d' < 2^x$ and $\forall i < x\ (i \in c' \rightarrow i \in d')$, we have $c' \leq d'$. Here $2^x$ is the element $e \leq w$ with $\varepsilon(x, e)$, so $\psi$ is bounded. For $x = 0$, $c' = d' = 0$. Assume $\psi(x)$, $x + 1 \leq a$, and let $c', d' < 2^{x+1}$ with every element of $c'$ below $x + 1$ in $d'$; by :ref{#lem-ack-basic} (item 3), all elements of $c'$ and $d'$ are at most $x$.

- If $x \in c'$, then $x \in d'$. By item 4, $c' - 2^x$ and $d' - 2^x$ code the elements of $c'$ and $d'$ other than $x$; these are below $x$, so both numbers are below $2^x$ by item 3, and the inclusion still holds. By $\psi(x)$, $c' - 2^x \leq d' - 2^x$, so $c' \leq d'$.
- If $x \notin c'$ and $x \in d'$, then $c' < 2^x$ by item 3, and $2^x \leq d'$ by item 1.
- If $x \notin c'$ and $x \notin d'$, then $c', d' < 2^x$, and $\psi(x)$ applies.

So $\psi(x + 1)$. By induction, $\psi(a)$ holds, and it applies to $c$ and $d$, whose elements are all below $a$. If $c \neq d$, they do not have the same elements below $a$ by extensionality (item 5), so $d$ has an element not in $c$, and $c \leq d$, $c \neq d$ give $c < d$.
:::
::::

::::exercise{#ex-ack-disjoint-union difficulty=2 objective="Show by bounded induction on the size of the interval that adding the codes of disjoint sets codes their union."}
Show that $\mathrm I\Delta_0 + \mathrm{exp}$ proves: if $c$ and $d$ have no common element, then $c + d$ codes the union of the sets coded by $c$ and $d$.

:::solution
Let $a = c + d$, so that $c, d < 2^a$ and all their elements are below $a$ (:ref{#lem-ack-basic}, item 3); let $w = 2^{a+1}$. Apply bounded induction, with parameters $a$ and $w$, to $\psi(x)$: if $x \leq a$, then for all $c' < 2^x$ and $d' < 2^a$ with no common element below $a$, every $i < a + 1$ satisfies $i \in c' + d' \leftrightarrow (i \in c' \vee i \in d')$. The quantifiers over $c', d'$ are bounded by $w$, and the powers $2^x$, $2^a$ are bounded by $w$, so $\psi$ is bounded. Since $c' + d' < 2^{a+1}$, item 3 shows that all elements of $c' + d'$ are below $a + 1$, so $\psi(x)$ says that $c' + d'$ codes the union.

For $x = 0$, $c' = 0$ codes the empty set and $c' + d' = d'$. Assume $\psi(x)$ and $x + 1 \leq a$, and let $c' < 2^{x+1}$ and $d' < 2^a$ be disjoint. If $x \notin c'$, then $c' < 2^x$ and $\psi(x)$ applies. If $x \in c'$, then $x < a$ and $x \notin d'$. By item 4, $c'' = c' - 2^x$ codes the elements of $c'$ other than $x$, and $c'' < 2^x$; and $d'' = d' + 2^x$ codes the elements of $d'$ together with $x$, and $d'' < 2^a$ by item 3, all its elements being below $a$. The sets coded by $c''$ and $d''$ are disjoint. By $\psi(x)$, $c'' + d'' = c' + d'$ codes their union, which is the union of the sets coded by $c'$ and $d'$. So $\psi(x + 1)$. By induction, $\psi(a)$, which applies to $c$ and $d$.
:::
::::

::::exercise{#ex-comprehension-needs-exp difficulty=1 objective="See that comprehension for bounded formulas fails as soon as a power does not exist." lessons="parikh"}
Let $M$ be a model of $\mathrm I\Delta_0$ and $b \in M$ such that $2^b$ does not exist in $M$. Show that no $c \in M$ satisfies $\forall i < b\ (i \in c)$. Deduce that :ref{#thm-delta0-comprehension} fails in every model of $\mathrm I\Delta_0 + \neg \mathrm{exp}$, for the formula $i = i$.

:::solution
Since $2^0 = 1$ exists, $b \neq 0$, so $b = b' + 1$. If $b' \in c$, the definition of $i \in c$ provides $p$ with $\varepsilon(b', p)$, and then $\varepsilon(b, p + p)$ by :ref{#fact-exp}: so $2^b$ exists, a contradiction. In a model of $\mathrm I\Delta_0 + \neg \mathrm{exp}$, some $b$ has no power $2^b$, and no element codes $\{ i < b : i = i \}$ below $b$, below $2^b$ or anywhere.
:::
::::

::::exercise[Ackermann's interpretation]{#ex-ack-hf difficulty=2 objective="Show that Ackermann membership on $\nat$ is isomorphic to membership on the hereditarily finite sets."}
Let $\mathrm{HF} = \bigcup_k V_k$ be the set of hereditarily finite sets, with $V_0 = \emptyset$ and $V_{k+1}$ the set of subsets of $V_k$. Define $F : \nat \to \mathrm{HF}$ by $F(n) = \{ F(i) : i \in \mathrm{Ack}(n) \}$, computed in $\nat$. Show that $F$ is well defined and is an isomorphism of $(\nat, E)$ onto $(\mathrm{HF}, \in)$, where $i \mathrel E n$ means $i \in \mathrm{Ack}(n)$.

:::solution
*Definition.* If $i \in \mathrm{Ack}(n)$, then $i < n$ (:ref{#lem-ack-basic}), so $F$ is defined by course-of-values recursion; by induction on $n$, $F(n)$ is a finite set of elements of $\mathrm{HF}$, hence an element of $\mathrm{HF}$ (if $F(i) \in V_{k_i}$ for each of the finitely many $i \in \mathrm{Ack}(n)$, then $F(n) \subseteq V_k$ for $k = \max k_i$, using $V_j \subseteq V_{j+1}$, so $F(n) \in V_{k+1}$).

*Injectivity*, by induction on $\max(n, m)$. Suppose $F(n) = F(m)$. For $i \in \mathrm{Ack}(n)$, $F(i) \in F(m)$, so $F(i) = F(j)$ for some $j \in \mathrm{Ack}(m)$; since $i < n$ and $j < m$, $\max(i, j) < \max(n, m)$, and $i = j$ by the induction hypothesis. So $\mathrm{Ack}(n) \subseteq \mathrm{Ack}(m)$, and symmetrically; hence $n = m$, since $n = \sum_{i \in \mathrm{Ack}(n)} 2^i$.

*Surjectivity*, by induction on $k$: every $x \in V_{k+1}$ is a finite set of elements of $V_k$, which are $F(i_1), \dots, F(i_r)$ for distinct $i_1, \dots, i_r$ by the induction hypothesis. Let $n = 2^{i_1} + \cdots + 2^{i_r}$; then $\mathrm{Ack}(n) = \{ i_1, \dots, i_r \}$ by the uniqueness of binary expansions, and $F(n) = x$.

*Isomorphism.* If $i \in \mathrm{Ack}(n)$, then $F(i) \in F(n)$ by definition. Conversely, if $F(i) \in F(n)$, then $F(i) = F(j)$ for some $j \in \mathrm{Ack}(n)$, and $i = j$ by injectivity. This is the interpretation of hereditarily finite sets in arithmetic given by Ackermann (1937).
:::
::::
:::::
