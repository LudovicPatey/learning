---
title: Parikh's theorem and exponentiation
summary: Parikh's theorem, by a cut closed under the terms of a model; the bounded graph of exponentiation; IΔ₀ does not prove that exponentiation is total, a model of IΔ₀ + ¬exp, and IΣ₁ proves exp.
duration: 30
prerequisites: [bounded-induction]
---

By Parikh's theorem, if $\mathrm I\Delta_0$ proves that every $x$ has some $y$ with a bounded property, then such a $y$ can be found below a polynomial in $x$. In particular, $\mathrm I\Delta_0$ does not prove that $2^x$ exists for every $x$. The proof is the first example of a recurring method: to show that a theory does not prove a statement, find inside a model a cut that is closed under the right operations, hence a model of the theory, but in which the statement fails.

## Parikh's theorem

:::theorem[Parikh]{#thm-parikh}
Let $\theta(\bar x, y)$ be a $\Delta_0$ formula. If $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y\ \theta(\bar x, y)$, then there is a term $t(\bar x)$ such that $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y < t(\bar x)\ \theta(\bar x, y)$.
:::

The idea is to collect, in a model where no term bound works for some parameters $\bar c$, everything below the values $t(\bar c)$ of all terms. This is a cut closed under addition and multiplication, hence a model of $\mathrm I\Delta_0$, and it contains no witness for $\theta(\bar c, y)$; so $\mathrm I\Delta_0$ cannot prove $\forall \bar x\ \exists y\ \theta$. Compactness is used to obtain a single model in which all the term bounds fail at once.

:::proof{of=thm-parikh}
Suppose that $\mathrm I\Delta_0 \nvdash \forall \bar x\ \exists y < t(\bar x)\ \theta(\bar x, y)$ for every term $t$. Let $\bar c$ be new constants and
$$
T = \mathrm I\Delta_0 \cup \{ \forall y < t(\bar c)\ \neg \theta(\bar c, y) : t \text{ a term} \}.
$$
A finite subset of $T$ mentions finitely many terms $t_1, \dots, t_k$; let $t = t_1 + \cdots + t_k$. By hypothesis, some model of $\mathrm I\Delta_0$ has elements $\bar a$ with $\forall y < t(\bar a)\ \neg \theta(\bar a, y)$, and since $t_i(\bar a) \leq t(\bar a)$, interpreting $\bar c$ as $\bar a$ satisfies the finite subset. By compactness, $T$ has a model $M$. Let
$$
I = \{ b \in M : b < t(\bar c) \text{ for some term } t \}.
$$
It is an initial segment, it contains each $c_i$, since $c_i < c_i + 1$, and it is closed under successor, addition and multiplication: if $b < t$ and $b' < s$, then $b + 1 < t + 1$, $b + b' < t + s$, and $b \cdot b' < t \cdot s$ (if $b' = 0$ this holds since $0 < t \cdot s$, both $t$ and $s$ being positive; otherwise $b b' < t b' < t s$ by the monotonicity axiom). By :ref{#lem-cut-model}, $I$ is a model of $\mathrm I\Delta_0$ containing $\bar c$, so $I \models \exists y\ \theta(\bar c, y)$: some $b \in I$ satisfies $I \models \theta(\bar c, b)$, hence $M \models \theta(\bar c, b)$ by :ref{#lem-delta0-absolute}. But $b < t(\bar c)$ for some term $t$, and $M \models \forall y < t(\bar c)\ \neg \theta(\bar c, y)$: a contradiction.
:::

:::figure[The cut of the proof of Parikh's theorem, drawn for one parameter $a$. The cut $I$ consists of the elements below some $t(a)$, such as $a, a^2, a^3, \dots$; it is a model of $\mathrm I\Delta_0$. All the elements $y$ with $\theta(a, y)$ lie above it, so $I$ satisfies $\neg \exists y\ \theta(a, y)$.]
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The cut I of the proof of Parikh&apos;s theorem: the elements below the values t(a) of the terms at a; it is closed under addition and multiplication, and contains no y with theta(a, y), whose witnesses all lie above I"><line x1="20" y1="70" x2="580" y2="70" class="ink-stroke" stroke-width="1.2"/><circle cx="24" cy="70" r="3.5" class="accent-fill"/><text x="24" y="58" text-anchor="middle" class="mrm" font-size="13">0</text><text x="70.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><circle cx="130" cy="70" r="3.5" class="accent-fill"/><text x="130.0" y="58.0" text-anchor="middle" class="math" font-size="14">a</text><circle cx="190" cy="70" r="3.5" class="accent-fill"/><text x="190.0" y="58.0" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="-6">2</tspan><tspan dy="6"> </tspan></text><circle cx="245" cy="70" r="3.5" class="accent-fill"/><text x="245.0" y="58.0" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="-6">3</tspan><tspan dy="6"> </tspan></text><circle cx="295" cy="70" r="3.5" class="accent-fill"/><text x="295.0" y="58.0" text-anchor="middle" class="math" font-size="14">a<tspan class="mrm" font-size="10" dy="-6">4</tspan><tspan dy="6"> </tspan></text><text x="330.0" y="74.0" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="360" y1="48" x2="360" y2="92" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><circle cx="430" cy="70" r="3.5" class="node"/><circle cx="490" cy="70" r="3.5" class="node"/><circle cx="545" cy="70" r="3.5" class="node"/><path d="M405,46 L405,40 L565,40 L565,46" class="muted-stroke" stroke-width="1.2"/><text x="485.0" y="30" text-anchor="middle" class="label">all y with θ(a, y)</text><path d="M22,86 L22,92 L354,92 L354,86" class="muted-stroke" stroke-width="1.2"/><text x="188.0" y="110" text-anchor="middle" class="label">the cut I: below some t(a)</text><path d="M366,86 L366,92 L578,92 L578,86" class="muted-stroke" stroke-width="1.2"/><text x="472.0" y="110" text-anchor="middle" class="label">M ∖ I</text></svg>
:::

:::quiz[Parikh's theorem]
Why must the cut $I$ in the proof be closed under multiplication?

- [x] To be a substructure of $M$, so that :ref{#lem-cut-model} applies and $I$ is a model of $\mathrm I\Delta_0$.
- [ ] To contain the parameters $\bar c$.

  The parameters are below the terms $c_i + 1$; this uses only that $I$ is defined from all terms.
- [ ] To make $I$ closed under successor.

  Closure under successor follows from closure under addition alone, or directly from the fact that $t + 1$ is a term.

:::

## Exponentiation

The function $x \mapsto 2^x$ is not a symbol of $\mathcal L_A$, and its natural definition, "there is a sequence $1, 2, 4, \dots, y$ of length $x + 1$", needs a coding of sequences, and the coding of :ref{to="coding"} itself uses exponentiation. Its graph has a bounded definition, which we admit.

:::fact[Bennett; Paris; Dimitracopoulos]{#fact-exp}
There is a $\Delta_0$ formula $\varepsilon(x, y)$ such that $\nat \models \varepsilon(x, y)$ if and only if $y = 2^x$, and $\mathrm I\Delta_0$ proves
1. $\varepsilon(0, 1)$, and $\varepsilon(x, y) \rightarrow \varepsilon(x + 1, y + y)$;
2. $\varepsilon(x, y) \wedge \varepsilon(x, y') \rightarrow y = y'$;
3. $\varepsilon(x, y) \wedge x' < x \rightarrow \exists y' < y\ \varepsilon(x', y')$.
:::

We write $y = 2^x$ for $\varepsilon(x, y)$, and say that $2^x$ exists if some $y$ satisfies it. In a model $M$ of $\mathrm I\Delta_0$, the elements $x$ for which $2^x$ exists form an initial segment containing the standard numbers, and the usual laws, such as $x < 2^x$, $2^{x + y} = 2^x \cdot 2^y$ and $x < y \leftrightarrow 2^x < 2^y$, hold whenever the powers involved exist. Each law is proved by a bounded induction in which a power that exists serves as a parameter bounding the others, as in the proof of comprehension for bounded formulas (:ref{to="ackermann-coding"}); see Hájek and Pudlák, Theorem I.1.30. We use these laws without comment.

:::definition{#def-exp}
The axiom $\mathrm{exp}$ is the $\Pi_2$ sentence $\forall x\ \exists y\ \varepsilon(x, y)$. An **exponential cut** of a model is a cut closed under $x \mapsto 2^x$.
:::

:::corollary{#cor-idelta0-exp}
$\mathrm I\Delta_0$ does not prove $\mathrm{exp}$.
:::

:::proof{of=cor-idelta0-exp}
Otherwise, by :ref{#thm-parikh}, there is a term $t(x)$ such that $\mathrm I\Delta_0$ proves $\forall x\ \exists y < t(x)\ \varepsilon(x, y)$. This sentence is true in $\nat$, so $2^x < t(x)$ for every $x \in \nat$. But the value of $t(x)$ in $\nat$ is given by a polynomial with coefficients in $\nat$, so $t(x) \leq c (x + 1)^d$ for some $c, d \in \nat$, and $2^x > c(x + 1)^d$ for all large $x$.
:::

:::example[A model of IΔ₀ + ¬exp]{#ex-idelta0-not-exp}
Let $M$ be a non-standard model of $\mathrm{Th}(\nat)$ and $a \in M$ non-standard, and let $I_a = \{ b \in M : b < t(a) \text{ for some term } t \}$. As in the proof of Parikh's theorem, $I_a$ is a model of $\mathrm I\Delta_0$. For every term $t(x)$, some $n \in \nat$ satisfies $\nat \models \forall x \geq \bar n\ \exists y\ (\varepsilon(x, y) \wedge t(x) < y)$; this sentence holds in $M$, and $a \geq n$, so the power $2^a$ computed in $M$ exceeds $t(a)$. Hence $2^a \notin I_a$. If some $b \in I_a$ satisfied $I_a \models \varepsilon(a, b)$, then $M \models \varepsilon(a, b)$ by absoluteness, and $b = 2^a$ by uniqueness, a contradiction. So $I_a \models \mathrm I\Delta_0 + \neg \mathrm{exp}$.
:::

Exponentiation is provable from slightly more induction.

:::proposition{#prop-isigma1-exp}
$\mathrm I\Sigma_1$ proves $\mathrm{exp}$.
:::

:::proof{of=prop-isigma1-exp}
Apply $\Sigma_1$ induction to $\exists y\ \varepsilon(x, y)$: it holds for $x = 0$, with $y = 1$, and if $\varepsilon(x, y)$ then $\varepsilon(x + 1, y + y)$, by :ref{#fact-exp}.
:::

So the model $I_a$ of the example is a model of $\mathrm I\Delta_0$ in which $\Sigma_1$ induction fails, for the formula $\exists y\ \varepsilon(x, y)$: the set of $x$ for which $2^x$ exists is a $\Sigma_1$-definable proper cut of $I_a$. The theory $\mathrm I\Delta_0 + \mathrm{exp}$, between $\mathrm I\Delta_0$ and $\mathrm I\Sigma_1$, is the setting of the coding of finite sets and sequences (:ref{to="ackermann-coding"}).

## Exercises

::::exercise{#ex-exponential-cut difficulty=2 objective="Use the absoluteness of the bounded graph of exponentiation to read exponentiation in a cut as closure of the cut."}
Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $I$ a cut of $M$ closed under addition and multiplication. Show that $I \models \mathrm{exp}$ if and only if $I$ is an exponential cut, and that $I \not\models \mathrm I\Sigma_1$ if $I$ is not exponential.

:::solution
For $a, b \in I$, $I \models \varepsilon(a, b)$ if and only if $M \models \varepsilon(a, b)$, by :ref{#lem-delta0-absolute} and :ref{#lem-cut-model}, that is, if and only if $b$ is the power $2^a$ computed in $M$. So $I \models \exists y\ \varepsilon(a, y)$ if and only if $2^a \in I$. If $I$ is not exponential, $I \not\models \mathrm{exp}$, hence $I \not\models \mathrm I\Sigma_1$ by :ref{#prop-isigma1-exp}.
:::
::::

## Notes and references

Parikh (1971) proved the theorem that bears his name, in a proof-theoretic form; the model-theoretic proof by a cut is the one of Hájek and Pudlák (Theorem V.1.4), who state it for theories with a $\Pi_1$ axiomatization. Bennett (1962) first gave a bounded definition of the graph of exponentiation; Paris found another one, and Dimitracopoulos verified that $\mathrm I\Delta_0$ proves its recursion clauses (Hájek and Pudlák, Chapter V, Section 3(c), and the bibliographical remarks to Chapter V); see also Gaifman and Dimitracopoulos (1982). Wong's lecture notes (Lecture 2) state the fact in the form used here.

- R. Parikh, *Existence and feasibility in arithmetic*, Journal of Symbolic Logic 36 (1971), 494–508.
- J. H. Bennett, *On spectra*, PhD thesis, Princeton University, 1962.
- H. Gaifman and C. Dimitracopoulos, *Fragments of Peano's arithmetic and the MRDP theorem*, in Logic and Algorithmic, Monographies de L'Enseignement Mathématique 30, Genève, 1982, 187–206.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(a), Chapter V, Sections 1 and 3.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 2.

:::::exercises
::::exercise{#ex-parikh-smallest-cut difficulty=1 objective="Identify the cut of the proof of Parikh's theorem as the least cut containing the parameters and closed under the operations."}
Show that the cut $I$ of the proof of :ref{#thm-parikh} is the smallest cut of $M$ that contains $\bar c$ and is closed under addition and multiplication.

:::solution
A cut $J$ containing $\bar c$ and closed under addition and multiplication contains $0$ and $1$, as a nonempty initial segment closed under successor, hence it contains the value $t(\bar c)$ of every term, by induction on the term. Being an initial segment, it contains every $b < t(\bar c)$. So $I \subseteq J$, and $I$ itself is such a cut.
:::
::::

::::exercise{#ex-term-bound-power difficulty=1 objective="Bound every term by a power of the sum of its variables, to give the bound of Parikh's theorem a uniform shape."}
For a tuple $\bar x = (x_1, \dots, x_n)$, let $s(\bar x) = x_1 + \cdots + x_n + 2$, and write $s^k$ for the product of $k$ copies of $s$, with $s^0 = 1$. Show that for every term $t(\bar x)$ there is $k \in \nat$ such that $\mathrm{PA}^- \vdash t(\bar x) \leq s(\bar x)^k$. Deduce that the term of :ref{#thm-parikh} may be taken of the form $s(\bar x)^k$.

:::solution
We use the monotonicity laws of :ref{#ex-pam-cancellation}, and $1 \leq s$, $2 \leq s$, which hold since $0 \leq x_i$. They give $s^j \leq s^k$ for $j \leq k$. By induction on $t$. For $t = 0$ or $t = 1$, take $k = 0$: $0 < 1$ and $1 \leq 1$. For $t = x_i$, take $k = 1$: $x_i \leq s$ by :ref{#ex-pam-cancellation}. If $t_1 \leq s^{k_1}$ and $t_2 \leq s^{k_2}$, let $k = \max(k_1, k_2)$; then $t_1 + t_2 \leq s^k + s^k = 2 \cdot s^k \leq s \cdot s^k = s^{k+1}$, and $t_1 \cdot t_2 \leq s^{k_1} \cdot s^{k_2} = s^{k_1 + k_2}$. If $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y < t(\bar x)\ \theta$, then also $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y < s(\bar x)^k\ \theta$, since $y < t \leq s^k$.
:::
::::

::::exercise{#ex-parikh-pi1-theories difficulty=2 objective="Extend Parikh's theorem to every theory with a $\Pi_1$ axiomatization, by checking which property of $\mathrm I\Delta_0$ the proof uses." lessons="bounded-induction"}
Let $T$ be a theory containing $\mathrm{PA}^-$ and equivalent to a set of $\Pi_1$ sentences. Show that if $T \vdash \forall \bar x\ \exists y\ \theta(\bar x, y)$ with $\theta$ bounded, then $T \vdash \forall \bar x\ \exists y < t(\bar x)\ \theta(\bar x, y)$ for some term $t$. Deduce that $\mathrm I\Delta_0$ together with all the $\Pi_1$ sentences true in $\nat$ does not prove $\mathrm{exp}$.

:::solution
Repeat the proof of :ref{#thm-parikh} with $T$ in place of $\mathrm I\Delta_0$. Compactness gives a model $M$ of $T$ with elements $\bar c$ such that $M \models \forall y < t(\bar c)\ \neg \theta(\bar c, y)$ for every term $t$. The set $I$ of elements below some $t(\bar c)$ is an initial segment, closed under successor, addition and multiplication, by the computation of the proof, which uses only $\mathrm{PA}^-$. So $I$ is a substructure of $M$ and $I \subseteq_e M$. Every $\Pi_1$ sentence true in $M$ is true in $I$ by :ref{#cor-sigma1-upward}, so $I \models T$, and $I \models \exists y\ \theta(\bar c, y)$. A witness $b \in I$ satisfies $M \models \theta(\bar c, b)$ by :ref{#lem-delta0-absolute}, and $b < t(\bar c)$ for some $t$: a contradiction. This is the only place where the proof of :ref{#thm-parikh} used $\mathrm I\Delta_0$, through :ref{#lem-cut-model}.

The theory $T = \mathrm I\Delta_0 \cup \{ \pi : \pi \text{ a } \Pi_1 \text{ sentence true in } \nat \}$ is equivalent to a set of $\Pi_1$ sentences by :ref{#lem-idelta0-pi1}, and it is true in $\nat$. If it proved $\mathrm{exp}$, it would prove $\forall x\ \exists y < t(x)\ \varepsilon(x, y)$ for some term $t$, a sentence that is then true in $\nat$; this is impossible, as in the proof of :ref{#cor-idelta0-exp}.
:::
::::

::::exercise{#ex-parikh-sigma1-pi1 difficulty=2 objective="See that Parikh's theorem extends to $\Sigma_1$ formulas by contraction of quantifiers, and fails for $\Pi_1$ formulas."}
1. Show that the conclusion of :ref{#thm-parikh} holds when $\theta(\bar x, y)$ is a $\Sigma_1$ formula.
2. Let $\theta(x, y) \equiv \varepsilon(x, y) \vee \forall z\ \neg \varepsilon(x, z)$. Show that $\theta$ is equivalent to a $\Pi_1$ formula, that $\mathrm I\Delta_0 \vdash \forall x\ \exists y\ \theta(x, y)$, and that for no term $t$ does $\mathrm I\Delta_0$ prove $\forall x\ \exists y < t(x)\ \theta(x, y)$.

:::solution
1. Write $\theta(\bar x, y) \equiv \exists z\ \delta(\bar x, y, z)$ with $\delta$ bounded; a block of several quantifiers $\exists z$ is treated in the same way, with tuples coded by iterated pairs. Let
$$
\delta'(\bar x, w) \equiv \exists y < w + 1\ \exists z < w + 1\ \big(w = \langle y, z \rangle \wedge \delta(\bar x, y, z)\big),
$$
which is bounded, since the graph of pairing is (:ref{#fact-pairing}). If $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y\ \exists z\ \delta$, then $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists w\ \delta'$, with $w = \langle y, z \rangle$, since $y, z \leq \langle y, z \rangle$. By :ref{#thm-parikh}, $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists w < t(\bar x)\ \delta'(\bar x, w)$ for some term $t$. A witness $w = \langle y, z \rangle < t$ gives $y \leq w < t$ with $\delta(\bar x, y, z)$, so $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y < t(\bar x)\ \theta(\bar x, y)$.

2. The formula $\theta$ is logically equivalent to $\forall z\ (\varepsilon(x, y) \vee \neg \varepsilon(x, z))$, which is $\Pi_1$. The sentence $\forall x\ \exists y\ \theta(x, y)$ is logically valid: if some $z$ satisfies $\varepsilon(x, z)$, take $y = z$; otherwise every $y$ satisfies the second disjunct. In $\nat$, $2^x$ exists for every $x$, so $\theta(x, y)$ holds if and only if $y = 2^x$. If $\mathrm I\Delta_0$ proved $\forall x\ \exists y < t(x)\ \theta(x, y)$, this sentence would be true in $\nat$, and $2^x < t(x)$ for every $x$, which fails for large $x$ as in the proof of :ref{#cor-idelta0-exp}.
:::
::::

::::exercise{#ex-ia-log-cut difficulty=2 objective="Analyze the cut on which exponentiation is defined in a model of $\mathrm I\Delta_0 + \neg \mathrm{exp}$, by transferring true sentences from $\nat$."}
Let $M$, $a$ and $I_a$ be as in :ref{#ex-idelta0-not-exp}, with powers $2^x$ computed in $M$, and let $J = \{ x \in I_a : 2^x \in I_a \}$. Show that $J$ is the set of $x \in I_a$ such that $I_a \models \exists y\ \varepsilon(x, y)$, that it is a proper cut of $I_a$ closed under addition, and that it is not closed under multiplication.

:::solution
Since $M \models \mathrm{Th}(\nat)$, every sentence true in $\nat$ holds in $M$; we use this for the laws of exponentiation. For $x, b \in I_a$, $I_a \models \varepsilon(x, b)$ if and only if $M \models \varepsilon(x, b)$, by :ref{#lem-delta0-absolute}, that is, if and only if $b = 2^x$. So $x \in J$ if and only if $I_a \models \exists y\ \varepsilon(x, y)$.

*$J$ is a cut closed under addition.* If $x' < x \in J$, then $2^{x'} < 2^x \in I_a$, so $2^{x'} \in I_a$. The elements $0$ and $1$ belong to $J$, since $1, 2 \in I_a$. If $x, x' \in J$, then $2^{x + x'} = 2^x \cdot 2^{x'} \in I_a$, since $I_a$ is closed under multiplication. So $J$ is closed under addition, hence under successor. It is proper, since $2^a \notin I_a$ by :ref{#ex-idelta0-not-exp}, so $a \in I_a \setminus J$.

*$J$ is not closed under multiplication.* The sentence "for every $u \geq 1$ there is $x$ with $2^x \leq u < 2^{x+1}$" is true in $\nat$; let $x \in M$ satisfy $2^x \leq a < 2^{x+1}$. Then $x \in J$, since $2^x \leq a$, and $x$ is non-standard, since otherwise $a < 2^{x+1}$ would be standard. Also $x < 2^x \leq a$, so $x \cdot x < a \cdot a$ and $x \cdot x \in I_a$. Suppose $2^{x \cdot x} \in I_a$, so $2^{x \cdot x} < t(a)$ for a term $t$. By :ref{#ex-term-bound-power}, $t(a) \leq (a + 2)^k \leq a^{2k}$ for some standard $k$, since $a + 2 \leq a \cdot a$. Let $m = 2k + 1$. The sentence
$$
\forall x\ \forall u\ \big(\overline{m + 1} \leq x \wedge u < 2^{x + 1} \rightarrow u^m < 2^{x \cdot x}\big),
$$
written with $\varepsilon$, is true in $\nat$: $u^m < 2^{(x+1) m}$, and $(x + 1) m \leq x \cdot x$ for $x \geq m + 1$, since then $x \cdot x \geq (m + 1) x = m x + x \geq m x + m$. It holds in $M$, and $x$ is non-standard, so $a^m < 2^{x \cdot x}$. But $2^{x \cdot x} < t(a) \leq a^{2k} < a^m$: a contradiction. So $x \cdot x \notin J$.
:::
::::
:::::
