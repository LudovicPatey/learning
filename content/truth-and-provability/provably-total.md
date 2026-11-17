---
title: Provably total functions of IΣ₁
summary: Provably total functions of a theory; every primitive recursive function is provably total in IΣ₁, with its recursion equations, and so are the functions defined by course-of-values recursion.
duration: 35
prerequisites: [fragments-of-arithmetic/coding, fragments-of-arithmetic/induction-collection, fragments-of-arithmetic/parikh, models-of-computation/primitive-recursion]
---

A theory of arithmetic can be measured by the functions it knows to be total. Every total computable function $f$ has a $\Sigma_1$ definition in $\nat$, by :ref{#cor-sigma1-ce} applied to its graph, but a theory may be unable to prove that this definition defines a total function. By Parikh's theorem, a function that $\mathrm I\Delta_0$ proves total through a $\Delta_0$ definition is bounded by a polynomial (:ref{#ex-tp-idelta0-polynomial}). This lesson shows that $\mathrm I\Sigma_1$ proves the totality of every primitive recursive function, and more: it proves their recursion equations, so that the usual recursive definitions of arithmetic, in particular those of syntax used later in the course, can be carried out inside $\mathrm I\Sigma_1$. The technique is to prove, by $\Sigma_1$ induction, the existence of the **sequence of values** of the function. The next lesson states the converse, due to Parsons, Mints and Takeuti, and shows that $\mathrm I\Sigma_1$ does not prove the totality of the Ackermann function while $\mathrm I\Sigma_2$ does.

## Provably total functions

:::definition{#def-provably-total}
Let $T$ be a theory in $\mathcal L_A$ true in $\nat$. A function $f : \nat^k \to \nat$ is **provably total** in $T$ if there is a $\Sigma_1$ formula $\varphi(\bar x, y)$ such that $\nat \models \varphi(\bar x, y) \leftrightarrow f(\bar x) = y$ for all $\bar x, y$, and $T \vdash \forall \bar x\ \exists! y\ \varphi(\bar x, y)$.
:::

In every model $M$ of $T$, such a formula defines a total function $f^M : M^k \to M$, and since $\nat \subseteq_e M$ and $\Sigma_1$ formulas go up (:ref{#cor-sigma1-upward}), $f^M$ extends $f$. The graph of $f^M$ is $\Delta_1$ in $T$: $y = f(\bar x)$ is equivalent to the $\Pi_1$ formula $\forall y'\ (\varphi(\bar x, y') \rightarrow y' = y)$. So a provably total function can be used inside $T$ as a new function symbol, without changing the classes $\Sigma_n$ and $\Pi_n$, as long as $T$ proves enough collection to absorb the bounded quantifiers created by its use.

The definition depends on the formula, not only on the function. Let $\mathrm{Prf}(p)$ be a $\Delta_0$ formula expressing, in $\nat$, that $p$ codes a proof of $0 = 1$ in $\mathrm{PA}$, and let $\varphi(x, y) \equiv y = 0 \wedge \forall p < x\ \neg \mathrm{Prf}(p)$. Since $\mathrm{PA}$ is consistent, $\varphi$ defines the zero function in $\nat$; but $\mathrm{PA} \vdash \forall x\ \exists y\ \varphi(x, y)$ would give $\mathrm{PA} \vdash \forall p\ \neg \mathrm{Prf}(p)$, the consistency of $\mathrm{PA}$, which is impossible by Gödel's second theorem.

## Primitive recursive functions in IΣ₁

The primitive recursive functions are obtained from the basic functions by composition and primitive recursion (:ref{#def-primitive-recursive}). We attach a $\Sigma_1$ formula $\varphi_f$ to each derivation of a primitive recursive function $f$, by induction on the derivation, as in the course on arithmetic definability (:ref{#thm-pr-sigma1}), but with the coding of sequences of the course on fragments of arithmetic instead of the β-function:

- for the basic functions, $y = 0$, $y = x + 1$ and $y = x_i$;
- for $f(\bar x) = h(g_1(\bar x), \dots, g_m(\bar x))$, the formula $\exists \bar z\ \big( \bigwedge_i \varphi_{g_i}(\bar x, z_i) \wedge \varphi_h(\bar z, y) \big)$;
- for $f(\bar x, 0) = g(\bar x)$ and $f(\bar x, n + 1) = h(\bar x, n, f(\bar x, n))$, the formula
$$
\varphi_f(\bar x, n, y) \equiv \exists s\ \Big( \mathrm{Seq}(s, n + 1) \wedge \varphi_g(\bar x, (s)_0) \wedge \forall i < n\ \varphi_h\big(\bar x, i, (s)_i, (s)_{i+1}\big) \wedge (s)_n = y \Big),
$$
which says that $s$ is the sequence of values $f(\bar x, 0), \dots, f(\bar x, n)$.

The last formula is not literally $\Sigma_1$, because of the bounded quantifier $\forall i < n$ in front of the $\Sigma_1$ formula $\varphi_h$; it is $\Sigma_1$ in $\mathrm I\Sigma_1$, by Parsons' lemma (:ref{#lem-fo-collection-closure}) in $\mathrm B\Sigma_1$, which $\mathrm I\Sigma_1$ proves (:ref{#thm-fo-parsons}). We replace it by an equivalent $\Sigma_1$ formula. In $\nat$, each $\varphi_f$ defines the graph of $f$.

:::example{#ex-pr-addition}
Addition is obtained by primitive recursion: $x + 0 = x$ and $x + (n + 1) = (x + n) + 1$, with $g(x) = x$ and $h(x, n, w) = w + 1$, the latter a composition of the successor with a projection. After simplifying $\varphi_g$ and $\varphi_h$ by logic, the formula attached to this derivation is
$$
\varphi_+(x, n, y) \equiv \exists s\ \big( \mathrm{Seq}(s, n + 1) \wedge (s)_0 = x \wedge \forall i < n\ (s)_{i+1} = (s)_i + 1 \wedge (s)_n = y \big),
$$
whose only witness is the sequence $x, x + 1, \dots, x + n$. Here $\forall i < n$ governs a bounded formula, so $\varphi_+$ is already $\Sigma_1$, without Parsons' lemma. The theorem below shows that $\mathrm I\Sigma_1$ proves $\forall x\ \forall n\ \exists! y\ \varphi_+(x, n, y)$ and the two equations; induction on $n$ for the $\Sigma_1$ formula $\varphi_+(x, n, x + n)$ then shows that it holds for all $n$, so that the function defined by $\varphi_+$ is provably equal to the addition of the language. For multiplication, $g(x) = 0$, $h(x, n, w) = w + x$, and $\varphi_h$ is $\varphi_+$ with permuted variables: the bounded quantifier $\forall i < n$ now stands in front of the unbounded $\exists s'$ of $\varphi_+$, and Parsons' lemma is needed.
:::

:::theorem{#thm-pr-provably-total}
Every primitive recursive function is provably total in $\mathrm I\Sigma_1$. More precisely, for every derivation of a primitive recursive function $f$, $\mathrm I\Sigma_1$ proves $\forall \bar x\ \exists! y\ \varphi_f(\bar x, y)$, and it proves the equations of the derivation: if $f$ is obtained by primitive recursion from $g$ and $h$, then, writing $f$, $g$ and $h$ for the functions defined by $\varphi_f$, $\varphi_g$ and $\varphi_h$,
$$
\mathrm I\Sigma_1 \vdash f(\bar x, 0) = g(\bar x) \wedge \forall n\ f(\bar x, n + 1) = h(\bar x, n, f(\bar x, n)),
$$
and similarly for composition.
:::

Totality is proved by induction on $n$, applied to the statement "there is a sequence of values of length $n + 1$". This statement begins with an unbounded $\exists s$, so it is $\Sigma_1$ and no better: this is why $\Sigma_1$ induction, and not bounded induction, is needed. Uniqueness only compares two given sequences, entry by entry, and needs only bounded induction.

:::proof{of=thm-pr-provably-total}
By induction on the derivation; we work in $\mathrm I\Sigma_1$, which contains $\mathrm I\Delta_0 + \mathrm{exp}$ by :ref{#prop-isigma1-exp}, so that coded sequences (:ref{#def-coded-sequence}) are available. The basic functions are clear, and for composition, existence and uniqueness of $y$ follow from those for the $g_i$ and $h$, by logic.

Let $f$ be obtained by primitive recursion from $g$ and $h$, which are provably total by the induction hypothesis. *Existence.* Fix $\bar x$, and apply $\Sigma_1$ induction to $\exists y\ \varphi_f(\bar x, n, y)$, a $\Sigma_1$ formula of $\mathrm I\Sigma_1$ in the variable $n$. For $n = 0$, let $s$ be the sequence of length $1$ whose entry is $g(\bar x)$, given by concatenation (:ref{#prop-seq-basic}) with the empty sequence. If $s$ witnesses $\varphi_f(\bar x, n, y)$, let $w = h(\bar x, n, y)$ and $s' = s^\frown w$; then $s'$ has length $n + 2$, agrees with $s$ below $n + 1$, and $\varphi_h(\bar x, n, (s')_n, (s')_{n+1})$ holds; so $s'$ witnesses $\varphi_f(\bar x, n + 1, w)$.

*Uniqueness.* Let $s$ and $s'$ witness $\varphi_f(\bar x, n, y)$ and $\varphi_f(\bar x, n, y')$. Apply bounded induction, with parameters $s, s', n$, to $i \leq n \rightarrow (s)_i = (s')_i$. For $i = 0$, both entries satisfy $\varphi_g(\bar x, \cdot)$, so they are equal by the uniqueness for $g$. If $(s)_i = (s')_i$ and $i + 1 \leq n$, then $(s)_{i+1}$ and $(s')_{i+1}$ both satisfy $\varphi_h(\bar x, i, (s)_i, \cdot)$, so they are equal by the uniqueness for $h$. At $i = n$, $y = (s)_n = (s')_n = y'$.

*Equations.* $\varphi_f(\bar x, 0, y)$ holds if and only if $\varphi_g(\bar x, y)$, by the case $n = 0$. If $s$ witnesses $\varphi_f(\bar x, n + 1, y)$, then its restriction $s \restriction (n + 1)$ (:ref{#prop-seq-basic}) witnesses $\varphi_f(\bar x, n, (s)_n)$, and $\varphi_h(\bar x, n, (s)_n, y)$; so $f(\bar x, n + 1) = h(\bar x, n, f(\bar x, n))$.
:::

:::quiz[primitive recursion in IΣ₁]
Where does the proof of :ref{#thm-pr-provably-total} use $\Sigma_1$ collection, through Parsons' lemma?

- [x] To know that $\varphi_f$ is $\Sigma_1$ in $\mathrm I\Sigma_1$, despite the bounded quantifier $\forall i < n$ in front of $\varphi_h$; without this, $\Sigma_1$ induction could not be applied to $\exists y\ \varphi_f(\bar x, n, y)$.
- [ ] To bound the entries of the sequence $s$.

  No bound on the entries is needed: the sequence $s^\frown w$ exists for every $w$, by concatenation.
- [ ] In the proof of uniqueness.

  Uniqueness uses bounded induction on a formula with the parameters $s$ and $s'$; no collection is involved.

---

Why is the theorem proved for derivations, and not for functions?

- [x] The formula $\varphi_f$ is built from a derivation; two derivations of the same function give two formulas whose equivalence is true in $\nat$ but need not be proved by the method.
- [ ] Because a primitive recursive function has a unique derivation.

  Every primitive recursive function has infinitely many derivations, for instance by composing with identities.
- [ ] Because provably total functions are not closed under composition.

  They are, as the case of composition in the proof shows.
:::

The same argument applies to **course-of-values recursion** (:ref{#thm-course-of-values}), in which $f(\bar x, n)$ is computed from the whole sequence of previous values: the witness $s$ is again the sequence of values $f(\bar x, 0), \dots, f(\bar x, n)$, and the condition on its entries becomes $\forall i < n + 1\ \varphi_h(\bar x, i, s \restriction i, (s)_i)$, where $s \restriction i$ is the code of the sequence of the first $i$ values, in the coding of :ref{#def-coded-sequence}.

:::corollary{#cor-course-of-values-provable}
If $f$ is defined by course-of-values recursion from a function $h$ provably total in $\mathrm I\Sigma_1$, $f(\bar x, n) = h(\bar x, n, \langle f(\bar x, 0), \dots, f(\bar x, n - 1) \rangle)$, the sequence being coded as in :ref{#def-coded-sequence}, then $f$ is provably total in $\mathrm I\Sigma_1$, and $\mathrm I\Sigma_1$ proves this equation for the function defined by $\varphi_f$.
:::

The proof is that of the theorem, with the restriction $s \restriction i$ in place of the previous entry. The corollary is the form in which the theorem is used: syntactic notions such as "$z$ is the code of a term" or "the value of the term coded by $t$ under the assignment coded by $e$" are defined by course-of-values recursion on codes, since the codes of subterms are smaller than the code of the term, and the corollary provides $\Delta_1$ definitions of them in $\mathrm I\Sigma_1$ together with proofs of their recursive characterizations.

## Exercises

::::exercise{#ex-tp-idelta0-polynomial difficulty=1 objective="Apply Parikh's theorem to bound the functions that $\mathrm I\Delta_0$ proves total through a $\Delta_0$ definition."}
Let $\theta(\bar x, y)$ be a $\Delta_0$ formula such that $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists! y\ \theta(\bar x, y)$, and $f$ the function it defines in $\nat$. Show that $f$ is bounded by a polynomial. Deduce that $x \mapsto 2^x$ is not provably total in $\mathrm I\Delta_0$ through a $\Delta_0$ definition.

:::solution
By Parikh's theorem (:ref{#thm-parikh}), there is a term $t$ with $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y < t(\bar x)\ \theta(\bar x, y)$. In $\nat$, the unique $y$ with $\theta(\bar x, y)$ is $f(\bar x)$, so $f(\bar x) < t(\bar x)$, and $t$ is a polynomial with natural coefficients. The function $2^x$ is not bounded by a polynomial.
:::
::::

::::exercise{#ex-tp-cut-pr-closed difficulty=2 objective="Combine provable totality with the upward persistence of $\Sigma_1$ formulas to show that cuts satisfying $\mathrm I\Sigma_1$ are closed under primitive recursive functions."}
Let $M$ be a model of $\mathrm I\Sigma_1$ and $I$ a cut of $M$, closed under addition and multiplication, such that $I \models \mathrm I\Sigma_1$. Show that $I$ is closed under $f^M$ for every primitive recursive function $f$, where $f^M$ is the function defined in $M$ by the formula $\varphi_f$ of a derivation of $f$.

:::solution
By :ref{#thm-pr-provably-total} applied in $I$, the formula $\varphi_f$ defines a total function $f^I$ on $I$. Let $\bar a \in I$. Then $I \models \varphi_f(\bar a, f^I(\bar a))$, and $\varphi_f$ is a $\Sigma_1$ formula, so $M \models \varphi_f(\bar a, f^I(\bar a))$ by :ref{#cor-sigma1-upward}. By uniqueness in $M$, $f^M(\bar a) = f^I(\bar a)$, which belongs to $I$.
:::
::::

## Notes and references

The closure of the $\mathrm I\Sigma_1$-provably total functions under primitive recursion is Theorem I.1.54 of Hájek and Pudlák, with Lemma I.1.55, which contains the sequence-of-values formula used in the proof above; Remark I.1.56 notes that course-of-values recursion is treated in the same way, and Section I.1(d) uses it for the arithmetization of syntax. The example of a formula whose totality is equivalent to a consistency statement rests on Gödel's second incompleteness theorem. The converse of the theorem is discussed in the next lesson.

- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(c).

:::::exercises
::::exercise{#ex-tp-idelta0-sigma1 difficulty=1 objective="Extend the polynomial bound given by Parikh's theorem to every function provably total in $\mathrm I\Delta_0$, whatever its $\Sigma_1$ definition."}
Let $f : \nat^k \to \nat$ be provably total in $\mathrm I\Delta_0$, in the sense of :ref{#def-provably-total}. Show that $f$ is bounded by a polynomial. Deduce that $x \mapsto 2^x$ is not provably total in $\mathrm I\Delta_0$.

:::solution
Let $\varphi(\bar x, y) \equiv \exists w_1 \cdots \exists w_m\ \delta(\bar x, y, \bar w)$, with $\delta$ a $\Delta_0$ formula, be a $\Sigma_1$ definition of the graph of $f$ such that $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists! y\ \varphi(\bar x, y)$. Let
$$
\theta(\bar x, p) \equiv \exists y < p + 1\ \exists w_1 < p + 1 \cdots \exists w_m < p + 1\ \delta(\bar x, y, \bar w),
$$
a $\Delta_0$ formula. In $\mathrm{PA}^-$, if $\delta(\bar x, y, \bar w)$ holds, then $p = y + w_1 + \dots + w_m$ satisfies $\theta(\bar x, p)$, since each summand is at most $p$. So $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists p\ \theta(\bar x, p)$, and Parikh's theorem (:ref{#thm-parikh}) gives a term $t$ with $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists p < t(\bar x)\ \theta(\bar x, p)$. This sentence is true in $\nat$. For $\bar x \in \nat$, take $p < t(\bar x)$ and $y \leq p$, $\bar w$ with $\delta(\bar x, y, \bar w)$; then $\nat \models \varphi(\bar x, y)$, so $y = f(\bar x)$, and $f(\bar x) \leq p < t(\bar x)$. The term $t$ is a polynomial with natural coefficients.

The function $2^x$ is not bounded by any polynomial, so no $\Sigma_1$ definition of it is proved total by $\mathrm I\Delta_0$. Compared with :ref{#ex-tp-idelta0-polynomial}, the definition need not be bounded: the unbounded witnesses $\bar w$ are bounded together with $y$.
:::
::::

::::exercise{#ex-tp-exists-unique difficulty=2 objective="Replace a $\Sigma_1$ definition proved total, without uniqueness, by one proved to define a function, through least witnesses."}
Let $T \supseteq \mathrm I\Delta_0$ be a theory true in $\nat$, $f : \nat^k \to \nat$, and $\varphi(\bar x, y)$ a $\Sigma_1$ formula such that $\nat \models \varphi(\bar x, y) \leftrightarrow f(\bar x) = y$ for all $\bar x, y$, and $T \vdash \forall \bar x\ \exists y\ \varphi(\bar x, y)$. Show that $f$ is provably total in $T$.

:::solution
Write $\varphi \equiv \exists w_1 \cdots \exists w_m\ \delta$ with $\delta \in \Delta_0$. As in :ref{#ex-tp-idelta0-sigma1}, $\varphi$ is equivalent in $\mathrm{PA}^-$ to $\exists w\ \delta'(\bar x, y, w)$, where $\delta' \equiv \exists w_1 < w + 1 \cdots \exists w_m < w + 1\ \delta$ is $\Delta_0$; so we may assume $\varphi \equiv \exists w\ \delta(\bar x, y, w)$. Let $\varphi'(\bar x, y)$ be
$$
\begin{aligned}
\exists w\ \exists p\ \big( & p = \langle y, w \rangle \wedge \delta(\bar x, y, w) \\
& \wedge \forall p' < p\ \forall y' < p' + 1\ \forall w' < p' + 1\ (p' = \langle y', w' \rangle \rightarrow \neg \delta(\bar x, y', w')) \big),
\end{aligned}
$$
which says that $\langle y, w \rangle$ is the least pair satisfying $\delta$. The relation $p = \langle y, w \rangle$ is $\Delta_0$ (:ref{#fact-pairing}), so $\varphi'$ is $\Sigma_1$.

*In $\nat$.* If $\varphi'(\bar x, y)$ holds, then so does $\varphi(\bar x, y)$, hence $y = f(\bar x)$. Conversely, for $\bar x \in \nat$ some pair satisfies $\delta$, so there is a least one $\langle y, w \rangle$; then $\varphi'(\bar x, y)$, and $y = f(\bar x)$ as before. So $\varphi'$ defines the graph of $f$.

*Existence in $T$.* Work in $T$ and fix $\bar x$. By hypothesis there are $y, w$ with $\delta(\bar x, y, w)$, so the $\Delta_0$ formula $\chi(p) \equiv \exists y' < p + 1\ \exists w' < p + 1\ (p = \langle y', w' \rangle \wedge \delta(\bar x, y', w'))$ holds at $p = \langle y, w \rangle$, because $y, w \leq \langle y, w \rangle$. By the least number principle for $\Delta_0$ formulas (:ref{#prop-idelta0-basic}), there is a least $p$ with $\chi(p)$; write $p = \langle y', w' \rangle$ with $\delta(\bar x, y', w')$. A pair $p'' = \langle y'', w'' \rangle < p$ with $\delta(\bar x, y'', w'')$ would satisfy $\chi(p'')$, against minimality; so $\varphi'(\bar x, y')$ holds, with witnesses $w'$ and $p$.

*Uniqueness in $T$.* Let $\varphi'(\bar x, y_1)$ and $\varphi'(\bar x, y_2)$ hold with witnesses $w_1, p_1$ and $w_2, p_2$. If $p_1 < p_2$, then the last conjunct for $y_2$, applied to $p' = p_1$, $y' = y_1 \leq p_1$, $w' = w_1 \leq p_1$, gives $\neg \delta(\bar x, y_1, w_1)$, a contradiction; similarly $p_2 < p_1$ is impossible. So $p_1 = p_2$, and $y_1 = y_2$ since pairing is a bijection.

Hence $T \vdash \forall \bar x\ \exists! y\ \varphi'(\bar x, y)$, and $f$ is provably total in $T$. This is why the definition may require $\exists !$ without loss: only the existence of values is a real condition.
:::
::::

::::exercise{#ex-tp-pi2-theory difficulty=1 objective="See that provable totality depends only on the $\Pi_2$ sentences that a theory proves."}
Let $\mathrm{Th}_{\Pi_2}(\nat)$ be the set of $\Pi_2$ sentences true in $\nat$.

1. Show that for every $\Sigma_1$ formula $\varphi(\bar x, y)$, the sentence $\forall \bar x\ \exists! y\ \varphi(\bar x, y)$ is logically equivalent to a $\Pi_2$ sentence.
2. Deduce that every total computable function is provably total in $\mathrm{Th}_{\Pi_2}(\nat)$, and that two theories true in $\nat$ that prove the same $\Pi_2$ sentences have the same provably total functions.

:::solution
1. Write $\varphi \equiv \exists \bar w\ \delta(\bar x, y, \bar w)$ with $\delta \in \Delta_0$. The sentence is the universal closure of the conjunction of $\exists y\ \exists \bar w\ \delta(\bar x, y, \bar w)$, a $\Sigma_1$ formula, and of
$$
\forall y\ \forall y'\ \forall \bar w\ \forall \bar w'\ \big( \delta(\bar x, y, \bar w) \wedge \delta(\bar x, y', \bar w') \rightarrow y = y' \big),
$$
a $\Pi_1$ formula. After renaming the bound variables apart, the conjunction is logically equivalent to $\forall y\, \forall y'\, \forall \bar w\, \forall \bar w'\ \exists y''\ \exists \bar w''\ (\cdots)$ with a $\Delta_0$ matrix, and the universal closure over $\bar x$ is $\Pi_2$.

2. Let $f$ be total computable. Its graph is computable, hence c.e., hence defined in $\nat$ by a $\Sigma_1$ formula $\varphi$ (:ref{#cor-sigma1-ce}). Since $f$ is total, $\forall \bar x\ \exists! y\ \varphi(\bar x, y)$ is true in $\nat$, and by item 1 it is equivalent to a sentence of $\mathrm{Th}_{\Pi_2}(\nat)$; so $\mathrm{Th}_{\Pi_2}(\nat)$ proves it, and this theory is true in $\nat$. For the second statement, if $f$ is provably total in $T$ through $\varphi$, the sentence $\forall \bar x\ \exists! y\ \varphi(\bar x, y)$ is equivalent to a $\Pi_2$ sentence proved by $T$, hence by $T'$, and $f$ is provably total in $T'$ through the same formula.

The theory $\mathrm{Th}_{\Pi_2}(\nat)$ is not computably axiomatizable. For a computably axiomatized theory $T$ true in $\nat$, the provably total functions form a proper subclass of the total computable functions, by a diagonal argument over an enumeration of the proofs of totality in $T$. Item 2 is the mechanism of Parsons' proof of the converse of :ref{#thm-pr-provably-total}, stated in the next lesson: $\mathrm I\Sigma_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic, so the two theories have the same provably total functions.
:::
::::

::::exercise{#ex-tp-multiplication difficulty=1 objective="Complete the example of multiplication by an induction inside $\mathrm I\Sigma_1$ on the recursion equations."}
Let $\varphi_\times(x, n, y)$ be the $\Sigma_1$ formula attached, as in :ref{#ex-pr-addition}, to the derivation of multiplication by $x \cdot 0 = 0$ and $x \cdot (n + 1) = x \cdot n + x$, where $h(x, n, w) = w + x$ is obtained from the derivation of addition and projections. Show that $\mathrm I\Sigma_1 \vdash \forall x\ \forall n\ \varphi_\times(x, n, x \cdot n)$, so that the function defined by $\varphi_\times$ is provably equal to the multiplication of the language.

:::solution
Work in $\mathrm I\Sigma_1$, and write $x \otimes n$ for the function defined by $\varphi_\times$ and $x \oplus n$ for the one defined by $\varphi_+$; both are total by :ref{#thm-pr-provably-total}. The formula $\varphi_h(x, n, w, y)$ is, after simplification, $\varphi_+(w, x, y)$, so $h(x, n, w) = w \oplus x$; and $w \oplus x = w + x$ by :ref{#ex-pr-addition}. By :ref{#thm-pr-provably-total}, the equations hold: $x \otimes 0 = 0$, and $x \otimes (n + 1) = h(x, n, x \otimes n) = (x \otimes n) + x$.

Fix $x$, and apply induction on $n$ to $\exists y\ (y = x \cdot n \wedge \varphi_\times(x, n, y))$, which is $\Sigma_1$ since $\varphi_\times$ is. For $n = 0$, $x \otimes 0 = 0 = x \cdot 0$ by the axioms of $\mathrm{PA}^-$. If $x \otimes n = x \cdot n$, then $x \otimes (n + 1) = x \cdot n + x = x \cdot (n + 1)$, by distributivity and $x \cdot 1 = x$. So $x \otimes n = x \cdot n$ for every $n$.
:::
::::

::::exercise{#ex-tp-course-of-values difficulty=2 objective="Carry out the proof of the theorem for course-of-values recursion, where each value depends on the restriction of the sequence of values."}
Let $h$ be provably total in $\mathrm I\Sigma_1$ through the $\Sigma_1$ formula $\varphi_h$, and let
$$
\varphi_f(\bar x, n, y) \equiv \exists s\ \big( \mathrm{Seq}(s, n + 1) \wedge \forall i < n + 1\ \varphi_h(\bar x, i, s \restriction i, (s)_i) \wedge (s)_n = y \big),
$$
where $\varphi_h(\bar x, i, s \restriction i, v)$ abbreviates $\exists t\ (t = s \restriction i \wedge \varphi_h(\bar x, i, t, v))$. Prove in $\mathrm I\Sigma_1$ that $\forall \bar x\ \forall n\ \exists! y\ \varphi_f(\bar x, n, y)$, completing the proof of :ref{#cor-course-of-values-provable}.

:::solution
Work in $\mathrm I\Sigma_1$, which proves $\mathrm{exp}$ (:ref{#prop-isigma1-exp}), so that :ref{#prop-seq-basic} applies. A sequence is a coded set of pairs (:ref{#def-coded-sequence}); two sequences of the same length with the same entries have the same elements, hence are equal by extensionality (:ref{#lem-ack-basic}). So $s \restriction i$ is unique, and the relation $t = s \restriction i$ is bounded, since $t \leq s$. As in the theorem, $\varphi_f$ is $\Sigma_1$ in $\mathrm I\Sigma_1$ by Parsons' lemma (:ref{#lem-fo-collection-closure}), which applies since $\mathrm I\Sigma_1$ proves $\mathrm B\Sigma_1$ (:ref{#thm-fo-parsons}).

*Existence.* Fix $\bar x$ and apply $\Sigma_1$ induction on $n$ to $\exists y\ \varphi_f(\bar x, n, y)$. For $n = 0$, the empty sequence is $0$, the only $s$ with $\mathrm{Seq}(s, 0)$; let $v = h(\bar x, 0, 0)$ and $s = 0^\frown v$, of length $1$, with $s \restriction 0 = 0$. Then $s$ witnesses $\varphi_f(\bar x, 0, v)$. Suppose that $s$ witnesses $\varphi_f(\bar x, n, y)$. Let $v = h(\bar x, n + 1, s)$ and $s' = s^\frown v$, of length $n + 2$. For $i \leq n + 1$, $s' \restriction i$ and $s \restriction i$ (with $s \restriction (n + 1) = s$) have the same length and the same entries, so they are equal. Hence the condition at $i \leq n$ holds for $s'$ because it holds for $s$, and the condition at $i = n + 1$ is $\varphi_h(\bar x, n + 1, s, v)$, true by the choice of $v$. So $s'$ witnesses $\varphi_f(\bar x, n + 1, v)$.

*Uniqueness.* Let $s$ and $s'$ witness $\varphi_f(\bar x, n, y)$ and $\varphi_f(\bar x, n, y')$. Apply bounded induction, with the parameters $s, s', n$, to the $\Delta_0$ formula $\forall j < i\ (j \leq n \rightarrow (s)_j = (s')_j)$. It holds at $i = 0$. If it holds at $i$ and $i \leq n$, then $s \restriction i = s' \restriction i$, since both have length $i$ and the same entries; so $(s)_i$ and $(s')_i$ both satisfy $\varphi_h(\bar x, i, s \restriction i, \cdot)$, and they are equal by the uniqueness for $h$. At $i = n + 1$ this gives $y = (s)_n = (s')_n = y'$.

The difference with :ref{#thm-pr-provably-total} is that the uniqueness is a strong induction: the value at $i$ depends on all earlier entries, which is why the induction hypothesis is stated for all $j < i$.
:::
::::
:::::
