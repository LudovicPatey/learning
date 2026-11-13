---
title: Lachlan's theorem
summary: A non-standard model of PA with a full satisfaction class is recursively saturated (Lachlan); with the theorem of Kotlarski, Krajewski and Lachlan, a countable non-standard model of PA has a full satisfaction class exactly when it is recursively saturated; satisfaction classes with induction, and disjunctive correctness.
duration: 40
prerequisites: [satisfaction-classes, truth-and-provability/provably-total]
---

The previous lesson built full satisfaction classes on countable recursively saturated models. Lachlan's theorem gives the converse: a non-standard model of Peano arithmetic with a full satisfaction class is recursively saturated. The two theorems together say that, for countable non-standard models, carrying a full satisfaction class is a model-theoretic property of the model, recursive saturation, and has no influence on its theory.

If the satisfaction class satisfied induction, the proof would be overspill, as in :ref{#thm-inductive-sat}. Without induction, the only information about non-standard formulas is local: each Tarski clause relates a formula to its direct subformulas, and a chain of applications of the clauses can only be followed for standardly many steps. Lachlan's argument builds a sequence of formulas $\beta_i$, defined for every $i$ in the model, such that each $\beta_{i+1}$ is evaluated from $\beta_i$ in standardly many steps. Following the sequence downward from a non-standard index then leads, in standardly many steps, to a contradiction.

Throughout, $M$ is a non-standard model of $\mathrm{PA}$ with a full satisfaction class $S$ (:ref{#def-sat-class}), and assignments are evaluated at the variables $v_0$ and $v_1$: for $x, c \in M$, $e_x$ is the sequence $\langle x, c \rangle$ of length $2$. By the uniqueness of codes (:ref{#lem-ack-basic}, extensionality), $e_x[0 := y] = e_y$. On standard formulas, $S$ is satisfaction in $M$ (:ref{#ex-sat-classes}).

## A partition of the model

:::lemma{#lem-lachlan-partition}
Let $p(v, c)$ be a recursive type over $M$, with one parameter, omitted in $M$. There is a computable sequence of standard formulas $\alpha_k(v_0, v_1)$, $k \in \nat$, with $\alpha_0 = (v_0 \neq v_0)$, such that the sets $A_k = \{ x : M \models \alpha_k(x, c) \}$ satisfy: $A_0 = \emptyset$, the sets $A_k$ for $k \geq 1$ are non-empty and pairwise disjoint, and $M = \bigcup_{k \in \nat} A_k$.
:::

:::proof{of=lem-lachlan-partition}
A finite type is realized, so $p$ is infinite; let $\theta'_0, \theta'_1, \dots$ be a computable enumeration of it, and $\theta_i = \bigwedge_{j < i} \theta'_j$, with $\theta_0 = (v = v)$. Let
$$
\theta^*_i(v) \equiv \exists a \leq v\ \exists b \leq v\ \big( v = \langle a, b \rangle \wedge \theta_i(a, c) \wedge \bar i \leq b \big),
$$
with the pairing of :ref{#fact-pairing}. Then $\theta^*_0$ holds of every element, since pairing is a bijection, and $\theta^*_{i+1}$ implies $\theta^*_i$. The element $\langle a, i \rangle$, with $a$ satisfying $\theta_{i+1}(a, c)$, which exists since $p$ is a type, satisfies $\theta^*_i$ and not $\theta^*_{i+1}$. If $\langle a, b \rangle$ satisfied every $\theta^*_i$, then $a$ would realize $p$. Let $\alpha_0 = (v_0 \neq v_0)$ and $\alpha_{i+1}(v_0, v_1) = \theta^*_i(v_0) \wedge \neg \theta^*_{i+1}(v_0)$, with $c$ replaced by $v_1$. The sets $A_{i+1}$ are non-empty and pairwise disjoint, since the $\theta^*_i$ decrease; every $x$ lies in $A_{i+1}$ for the least $i$ such that $\theta^*_{i+1}(x)$ fails.
:::

The pairing with $b \geq i$ makes each difference $A_{i+1}$ non-empty without deciding, non-effectively, which formulas of $p$ are redundant.

## The formulas of Lachlan

Inside $M$, define by primitive recursion formulas $\beta_i$ and $\gamma_{i,k}$, for $i \in M$ and $k \leq i + 1$, with free variables among $v_0, v_1$:
$$
\begin{aligned}
\beta_0 &= (v_0 \neq v_0), \qquad \gamma_{i, i+1} = (v_0 \neq v_0), \\
\gamma_{i,k} &= \big( \exists v_0 (\beta_i \wedge \alpha_k) \wedge \alpha_{k+1} \big) \vee \big( \neg \exists v_0 (\beta_i \wedge \alpha_k) \wedge \gamma_{i,k+1} \big) \quad (k \leq i), \\
\beta_{i+1} &= \big( \neg \exists v_0\, \beta_i \wedge \alpha_1 \big) \vee \big( \exists v_0\, \beta_i \wedge \gamma_{i,0} \big).
\end{aligned}
$$
Read with true satisfaction, $\beta_{i+1}$ says: "if $\beta_i$ defines the empty set, then $\alpha_1$; otherwise $\alpha_{k+1}$, for the first $k \leq i$ such that $\beta_i$ meets $\alpha_k$". The functions $k \mapsto \ulcorner \alpha_k \urcorner$ and $(i, k) \mapsto (\ulcorner \beta_i \urcorner, \ulcorner \gamma_{i,k} \urcorner)$ are primitive recursive, and by :ref{#thm-pr-provably-total} their recursion equations hold in $M$ for all $i, k \in M$. For standard $k$, the code $\alpha_k$ computed in $M$ is the standard formula $\alpha_k$; for non-standard $i$, $\beta_i$ is a non-standard formula. The nested form of $\gamma_{i,k}$, an "if, else if" chain, matters: to reach the $k$-th case, the clauses for $\vee$ and $\wedge$ are applied $k$ times from the outside, and each step decides the remaining cases by a single false conjunct.

For $i \in M$, let $B_i = \{ x \in M : S(\beta_i, e_x) \}$.

:::lemma{#lem-lachlan-step}
Let $i \in M$.

1. If $B_i = \emptyset$, then $B_{i+1} = A_1$.
2. If $B_i \neq \emptyset$, let $k_0 \in \nat$ be least with $B_i \cap A_{k_0} \neq \emptyset$. If $k_0 \leq i$, then $B_{i+1} = A_{k_0 + 1}$.
:::

:::proof{of=lem-lachlan-step}
By the clause for $\exists v_0$ and $e_x[0 := y] = e_y$, $S(\exists v_0\, \beta_i, e_x)$ holds if and only if $S(\beta_i, e_y)$ for some $y$, that is, $B_i \neq \emptyset$. Similarly, for standard $k$, the clauses for $\exists v_0$ and $\wedge$, and the correctness of $S$ on the standard formula $\alpha_k$, give: $S(\exists v_0 (\beta_i \wedge \alpha_k), e_x)$ if and only if $B_i \cap A_k \neq \emptyset$. These truth values do not depend on $x$.

1. The clauses for $\vee$, $\wedge$ and $\neg$ give $S(\beta_{i+1}, e_x) \leftrightarrow S(\alpha_1, e_x)$, that is, $x \in A_1$.
2. Now $S(\beta_{i+1}, e_x) \leftrightarrow S(\gamma_{i,0}, e_x)$. For standard $k < k_0$, $k \leq i$, the first disjunct of $\gamma_{i,k}$ is false for $S$ and the second reduces to $\gamma_{i,k+1}$: $S(\gamma_{i,k}, e_x) \leftrightarrow S(\gamma_{i,k+1}, e_x)$. Applying this $k_0$ times, a standard number of times, $S(\gamma_{i,0}, e_x) \leftrightarrow S(\gamma_{i,k_0}, e_x)$. At $k_0 \leq i$, the first disjunct reduces to $\alpha_{k_0 + 1}$ and the second is false, so $S(\gamma_{i,k_0}, e_x) \leftrightarrow x \in A_{k_0 + 1}$.
:::

Since the sets $A_k$ cover $M$, the number $k_0$ always exists when $B_i \neq \emptyset$.

:::lemma{#lem-lachlan-values}
1. For every standard $i$, $B_i = A_i$.
2. For every non-standard $i$, $B_i = A_m$ for some standard $m \geq 2$.
3. For every non-standard $i$ and standard $m \geq 1$, if $B_{i+1} = A_{m+1}$, then $B_i = A_m$.
:::

:::proof{of=lem-lachlan-values}
1. By induction in the metatheory. $B_0 = \emptyset = A_0$, since $\beta_0$ is standard. If $B_i = A_i$ with $i = 0$, then $B_1 = A_1$ by :ref{#lem-lachlan-step} (1). If $i \geq 1$, then $A_i$ is non-empty and meets no other $A_k$, so $k_0 = i \leq i$, and $B_{i+1} = A_{i+1}$ by :ref{#lem-lachlan-step} (2).
2. First, $B_i \neq \emptyset$ for every non-standard $i$. Write $i = j + 1$, with $j$ non-standard. If $B_j = \emptyset$, then $B_i = A_1 \neq \emptyset$. Otherwise $k_0$ is standard, hence $k_0 \leq j$, and $B_i = A_{k_0 + 1} \neq \emptyset$. Now apply this to $j$: $B_j \neq \emptyset$, so $B_i = A_{k_0 + 1}$, and $k_0 \geq 1$ since $A_0 = \emptyset$ meets nothing.
3. By item 2, $B_i = A_{m'}$ with $m' \geq 2$. This set is non-empty and meets only $A_{m'}$, so $k_0 = m'$, and $B_{i+1} = A_{m' + 1}$ by :ref{#lem-lachlan-step} (2), $m'$ being standard and $i$ non-standard. The sets $A_k$, $k \geq 1$, are distinct, so $m' = m$.
:::

:::theorem[Lachlan]{#thm-lachlan}
Every non-standard model of $\mathrm{PA}$ with a full satisfaction class is recursively saturated.
:::

:::proof{of=thm-lachlan}
Let $p$ be a recursive type over $M$; pairing its parameters into one, write it $p(v, c)$. Suppose that it is omitted, and take the formulas of :ref{#lem-lachlan-partition}. Let $\nu$ be non-standard. By :ref{#lem-lachlan-values} (2), $B_\nu = A_m$ for a standard $m \geq 2$. Applying item 3 of the same lemma $m - 1$ times, to the non-standard indices $\nu - 1, \dots, \nu - m + 1$, gives $B_{\nu - m + 1} = A_1$. But $\nu - m + 1$ is non-standard, and item 2 gives $B_{\nu - m + 1} = A_{m''}$ with $m'' \geq 2$, a set disjoint from $A_1$ and non-empty. This contradiction shows that $p$ is realized.
:::

:::figure[Lachlan's argument. The sets $A_k$ partition $M$. Along the standard indices, $B_i = A_i$. At a non-standard index $\nu$, $B_\nu$ is some $A_m$, and each step down lowers the index of the set by one, so that $m - 1$ steps down reach $A_1$ at a non-standard index, where only sets $A_{m''}$ with $m'' \geq 2$ can occur.]
<svg class="fig" viewBox="0 0 600 210" width="600" role="img" aria-label="The sets B_i along the indices: B_i equals A_i for standard i; at a non-standard index nu, B_nu is A_m, and each step down lowers m by one until A_1 is reached at a non-standard index, which is impossible"><defs><marker id="rs-la" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><line x1="20.0" y1="120.0" x2="580.0" y2="120.0" class="ink-stroke" stroke-width="1.2"/><circle cx="40.0" cy="120.0" r="3.5" class="accent-fill"/><text x="40.0" y="142.0" text-anchor="middle" class="math" font-size="13">B<tspan class="mrm" font-size="9" dy="3">0</tspan></text><text x="40.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="9" dy="3">0</tspan></text><circle cx="90.0" cy="120.0" r="3.5" class="accent-fill"/><text x="90.0" y="142.0" text-anchor="middle" class="math" font-size="13">B<tspan class="mrm" font-size="9" dy="3">1</tspan></text><text x="90.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="9" dy="3">1</tspan></text><circle cx="140.0" cy="120.0" r="3.5" class="accent-fill"/><text x="140.0" y="142.0" text-anchor="middle" class="math" font-size="13">B<tspan class="mrm" font-size="9" dy="3">2</tspan></text><text x="140.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="9" dy="3">2</tspan></text><circle cx="190.0" cy="120.0" r="3.5" class="accent-fill"/><text x="190.0" y="142.0" text-anchor="middle" class="math" font-size="13">B<tspan class="mrm" font-size="9" dy="3">3</tspan></text><text x="190.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="9" dy="3">3</tspan></text><text x="115.0" y="170.0" text-anchor="middle" class="label">standard indices: Bᵢ = Aᵢ</text><line x1="260.0" y1="102.0" x2="260.0" y2="138.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="260.0" y="160.0" text-anchor="middle" class="math" font-size="13">ℕ</text><circle cx="360.0" cy="120.0" r="3.5" class="node"/><text x="360.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="10" dy="3">1</tspan></text><text x="360" y="142" text-anchor="middle" class="math" font-size="13">ν−m+1</text><circle cx="420.0" cy="120.0" r="3.5" class="node"/><text x="420.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="10" dy="3">2</tspan></text><circle cx="480.0" cy="120.0" r="3.5" class="node"/><text x="480.0" y="106.0" text-anchor="middle" class="math" font-size="13">⋯</text><circle cx="540.0" cy="120.0" r="3.5" class="node"/><text x="540.0" y="106.0" text-anchor="middle" class="math" font-size="13">A<tspan class="mrm" font-size="10" dy="3">m</tspan></text><text x="540" y="142" text-anchor="middle" class="math" font-size="13">ν</text><path d="M540,90 Q510.0,62 484,88" class="ink-stroke" fill="none" stroke-width="1.2" marker-end="url(#rs-la)"/><path d="M480,90 Q450.0,62 424,88" class="ink-stroke" fill="none" stroke-width="1.2" marker-end="url(#rs-la)"/><path d="M420,90 Q390.0,62 364,88" class="ink-stroke" fill="none" stroke-width="1.2" marker-end="url(#rs-la)"/><text x="450.0" y="50.0" text-anchor="middle" class="label">each step down lowers the index by one</text><text x="450.0" y="170.0" text-anchor="middle" class="label">at a non-standard index, A₁ cannot occur</text></svg>
:::

:::quiz[Lachlan's theorem]
Why does the proof need the sets $A_k$ to be non-empty?

- [x] In :ref{#lem-lachlan-step} (2) and :ref{#lem-lachlan-values}, a set $B_i = A_m$ must meet $A_m$ and no other $A_k$, so that $k_0 = m$; an empty $A_m$ would meet nothing, and the sequence would restart at $A_1$.
- [ ] To make the sequence $(\alpha_k)$ computable.

  Computability comes from the enumeration of $p$; non-emptiness is obtained by the pairing trick.
- [ ] Because $S$ is only correct on non-empty sets.

  $S$ is correct on all standard formulas.

---

Why are the conditions on $\beta_i$ nested as "if, else if" in $\gamma_{i,k}$, rather than written as one disjunction $\bigvee_{k \leq i} (\ldots \wedge \alpha_{k+1})$?

- [x] For a non-standard disjunction, the clause for $\vee$ shows only that the first standardly many disjuncts are evaluated correctly; the remaining non-standard disjunction may be true for $S$ although each of its disjuncts is false. In the nested form, the case $k_0$ is followed by a disjunct containing a false conjunct, which settles the rest.
- [ ] Because a disjunction of non-standard length is not a formula of $M$.

  It is a formula of $M$; the issue is how $S$ evaluates it.
- [ ] Because the nested form is shorter.

  Both forms have length of order $i$ times the length of $\beta_i$.
:::

## The characterization and its limits

:::corollary{#cor-lachlan-characterization}
A countable non-standard model of $\mathrm{PA}$ has a full satisfaction class if and only if it is recursively saturated. In particular, the models of :ref{#prop-rs-definable} have none, and every model of $\mathrm{PA}$ is elementarily equivalent to a model with a full satisfaction class.
:::

:::proof{of=cor-lachlan-characterization}
:ref{#thm-lachlan} and :ref{#thm-kkl}. The last statement follows from :ref{#thm-rs-existence}.
:::

So $\mathrm{CT}^-$ is conservative over $\mathrm{PA}$ (:ref{#cor-ct-conservative}), but its models are not arbitrary: their arithmetic parts are recursively saturated, or standard. Induction changes the first fact. If a model of $\mathrm{PA}$ has a full satisfaction class satisfying induction for bounded formulas of $\mathcal L_A \cup \{ S \}$, then it satisfies $\mathrm{Con}(\mathrm{PA})$ (Kotlarski, 1986; Krajewski, 1976; see Wong's Lecture 14): the theory $\mathrm{CT}_0$ so obtained is not conservative over $\mathrm{PA}$. Enayat and Pakhomov (2019) located the source of this strength in the pathology of the previous lesson: $\mathrm{CT}^-$ together with **disjunctive correctness**, the statement that a finite disjunction of any length is true if and only if one of its disjuncts is true, is the same theory as $\mathrm{CT}_0$; in particular it proves $\mathrm{Con}(\mathrm{PA})$.

## Exercises

::::exercise{difficulty=1}
Show that a full satisfaction class for a model $M$ of $\mathrm{PA}$ is not definable in $M$ with parameters.

:::solution
By :ref{#ex-sat-classes} (2), it satisfies condition 2 of :ref{#def-inductive-sat}; apply the exercise of :ref{to="recursive-saturation/resplendence"}.
:::
::::

::::exercise{difficulty=2}
Let $\eta_k$, $k \in M$, be formulas given by a primitive recursive function, and $\bigvee_{k < m} \eta_k$ defined head first: $\bigvee_{k < 0} \eta_k = (v_0 \neq v_0)$ and $\bigvee_{k < m + 1} \eta_k = \eta_0 \vee \bigvee_{k < m} \eta_{k+1}$. Let $S$ be a full satisfaction class and $m$ non-standard. Show that if $S(\eta_{k_0}, e)$ for some standard $k_0 < m$, then $S(\bigvee_{k < m} \eta_k, e)$; and that the converse can fail, using the exercise of the previous lesson.

:::solution
By the clause for $\vee$, applied $k_0 + 1$ times from the outside, $S(\bigvee_{k < m} \eta_k, e)$ holds if one of $S(\eta_0, e), \dots, S(\eta_{k_0}, e)$ holds. For the converse, take $\eta_k = (0 \neq 0)$ for every $k$ and $m = a$ non-standard. The solution of the exercise of the previous lesson applies to the formulas $\bigvee_{k < m'} \eta_k$ in place of $\delta_{m'}$, and gives a full satisfaction class for which $\bigvee_{k < a} \eta_k$ is true, while every $\eta_k$, a standard false sentence, is false.
:::
::::

## Notes and references

:ref{#thm-lachlan} is due to Lachlan (1981); the proof follows Wong's presentation (Theorem 14.4), with two changes: the pairing in :ref{#lem-lachlan-partition}, which makes the sets $A_k$ non-empty, and the nested form of the formulas $\gamma_{i,k}$, which makes the evaluation of the case $k_0$ independent of the non-standard tail. Smith (1989) observed that the formulas of the type need not be standard. Wong's Lecture 14 also proves, with a version of Lachlan's theorem for expanded languages, Schlipf's theorem that countable recursively saturated structures are chronically resplendent.

- A. H. Lachlan, *Full satisfaction classes and recursive saturation*, Canadian Mathematical Bulletin 24 (1981), 295–297.
- H. Kotlarski, *Bounded induction and satisfaction classes*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 32 (1986), 531–544.
- A. Enayat and F. Pakhomov, *Truth, disjunction, and induction*, Archive for Mathematical Logic 58 (2019), 753–766.
- S. Krajewski, *Non-standard satisfaction classes*, in Set Theory and Hierarchy Theory, Lecture Notes in Mathematics 537, Springer, 1976, 121–144.
- S. T. Smith, *Nonstandard definability*, Annals of Pure and Applied Logic 42 (1989), 21–43.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 14.
