---
title: Induction, collection and coded sets
summary: In IΔ₀ + exp, IΣₙ means that bounded Σₙ-definable sets are coded (Friedman), and BΣₙ₊₁ that bounded Δₙ₊₁-definable sets are coded; BΣₙ₊₁ + exp proves IΣₙ.
duration: 40
prerequisites: [coding, induction-collection]
---

Once finite sets are coded, induction and collection become comprehension principles. A coded set is finite from the point of view of the model, and nonempty coded sets have least and largest elements. This lesson shows that, in $\mathrm I\Delta_0 + \mathrm{exp}$, $\Sigma_n$ induction says exactly that every bounded $\Sigma_n$-definable set is coded, and $\Sigma_{n+1}$ collection that every bounded $\Delta_{n+1}$-definable set is coded. The implication from $\mathrm B\Sigma_{n+1}$ to $\mathrm I\Sigma_n$ then becomes the inclusion of $\Sigma_n$ in $\Delta_{n+1}$.

## Induction is comprehension for Σₙ sets

From now on, $M$ is a model of $\mathrm I\Delta_0 + \mathrm{exp}$, so that coded sets are available (lesson 6). A set $S \subseteq M$ is **piecewise coded** if for every $a \in M$ there is $c \in M$ with $\forall x < a\ (x \in c \leftrightarrow x \in S)$: each bounded piece $S \cap [0, a)$ is coded. By :ref{#thm-delta0-comprehension}, every $\Delta_0$-definable set is piecewise coded.

:::theorem[Friedman]{#thm-friedman-coded}
Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $n \geq 0$. Then $M \models \mathrm I\Sigma_n$ if and only if every $\Sigma_n$-definable subset of $M$ is piecewise coded.
:::

A coded set is finite from the point of view of $M$, and nonempty coded sets have least elements. So piecewise coding gives least elements to definable sets, which is induction. Conversely, the code of $S \cap [0, a)$ is found as the least $c$ that contains $S \cap [0, a)$: the property "$c$ contains $S \cap [0, a)$" is $\Pi_n$, and its least witness cannot contain any element outside $S$, since removing it would give a smaller witness.

:::proof{of=thm-friedman-coded}
For $n = 0$, both sides hold, by hypothesis and by :ref{#thm-delta0-comprehension}. Let $n \geq 1$.

Suppose every $\Sigma_n$-definable set is piecewise coded, and let $\theta(x)$ be $\Sigma_n$, with parameters, and $M \models \theta(b)$. Let $c$ code $\{ x < b + 1 : \theta(x) \}$. Then $b \in c$, and the least element $m$ of $c$, given by the least number principle for the bounded formula $x \in c$, is the least $x$ with $\theta(x)$, since every $x \leq m$ is below $b + 1$. So $M \models \mathrm L\Sigma_n$, hence $M \models \mathrm I\Sigma_n$ (:ref{#prop-fo-least-number}).

Conversely, suppose $M \models \mathrm I\Sigma_n$, so $M \models \mathrm L\Pi_n$. Let $\theta(x)$ be $\Sigma_n$, with parameters, let $a \in M$ and $e = 2^a$, and consider
$$
\pi(c) \equiv c < e \wedge \forall x < a\ \big(\theta(x) \rightarrow x \in c\big).
$$
The formula $\theta(x) \rightarrow x \in c$ is equivalent to $\neg \theta(x) \vee x \in c$, which is $\Pi_n$, and the bounded universal quantifier keeps it $\Pi_n$; so $\pi$ is $\Pi_n$, with parameters $a$, $e$ and those of $\theta$. The code of $[0, a)$, given by :ref{#thm-delta0-comprehension}, satisfies $\pi$. By $\mathrm L\Pi_n$, there is a least $c$ with $\pi(c)$. Suppose some $x < a$ belongs to $c$ and does not satisfy $\theta$. By :ref{#lem-ack-basic}, $c - 2^x$ codes the elements of $c$ other than $x$; it is less than $c$, hence less than $e$, and it contains every $x' < a$ with $\theta(x')$. So $\pi(c - 2^x)$, contradicting the minimality of $c$. Hence $c$ codes $\{ x < a : \theta(x) \}$ below $a$.
:::

:::quiz[coded Σₙ sets]
In the proof of :ref{#thm-friedman-coded}, why is the code taken as the *least* $c$ containing the set, rather than built by induction on $a$ as in :ref{#thm-delta0-comprehension}?

- [x] The statement "$\{ x < t : \theta(x) \}$ has a code" contains $\theta$ on both sides of an equivalence, so it is neither $\Sigma_n$ nor $\Pi_n$, and no induction available applies to it; the property "contains the set" is $\Pi_n$, and the least number principle for $\Pi_n$ formulas applies.
- [ ] Because the least code is unique.

  Codes of a bounded set below $2^a$ are unique anyway, by extensionality.
- [ ] Because $\mathrm L\Pi_n$ is stronger than $\mathrm I\Sigma_n$.

  They are equivalent; the choice is about the complexity of the formula, not about the strength of the scheme.
:::

## Collection is comprehension for Δₙ₊₁ sets

A set $S \subseteq M$ is **$\Delta_{n+1}$-definable** in $M$ if it is defined by a $\Sigma_{n+1}$ formula and also by a $\Pi_{n+1}$ formula, both with parameters. Every $\Sigma_n$-definable set is $\Delta_{n+1}$-definable, by adding vacuous quantifiers.

:::theorem{#thm-collection-coded}
Let $M$ be a model of $\mathrm I\Delta_0 + \mathrm{exp}$ and $n \geq 0$. Then $M \models \mathrm B\Sigma_{n+1}$ if and only if every $\Delta_{n+1}$-definable subset of $M$ is piecewise coded.
:::

:::proof{of=thm-collection-coded}
*Collection gives coding*, by induction on $n$. Assume $M \models \mathrm B\Sigma_{n+1}$, and let $S$ be defined by $\exists y\ \varphi(x, y)$ and by $\forall y\ \psi(x, y)$, with $\varphi \in \Pi_n$ and $\psi \in \Sigma_n$, after contraction of quantifiers. Let $a \in M$. For every $x < a$, either $x \in S$, and some $y$ satisfies $\varphi(x, y)$, or $x \notin S$, and some $y$ satisfies $\neg \psi(x, y)$. So $\forall x < a\ \exists y\ (\varphi(x, y) \vee \neg \psi(x, y))$, and the formula in parentheses is $\Pi_n$, hence $\Sigma_{n+1}$. Collection gives $b$ with $\forall x < a\ \exists y < b\ (\varphi(x, y) \vee \neg \psi(x, y))$. For $x < a$,
$$
\exists y < b\ \varphi(x, y) \;\Rightarrow\; x \in S \;\Rightarrow\; \forall y < b\ \psi(x, y) \;\Rightarrow\; \exists y < b\ \varphi(x, y),
$$
the last step because some $y < b$ satisfies $\varphi(x, y)$ or $\neg \psi(x, y)$, and the second option is excluded. So $S \cap [0, a)$ is defined by $x < a \wedge \exists y < b\ \varphi(x, y)$ and by $x < a \wedge \forall y < b\ \psi(x, y)$. If $n = 0$, these formulas are bounded, and :ref{#thm-delta0-comprehension} gives a code. If $n \geq 1$, $M$ satisfies $\mathrm B\Sigma_n$, so by Parsons' lemma the first formula is $\Pi_n$ and the second $\Sigma_n$ in $M$: the set $S \cap [0, a)$ is $\Delta_n$-definable, and it is coded by the induction hypothesis.

*Coding gives collection.* Assume that every $\Delta_{n+1}$-definable set is piecewise coded. In particular every $\Sigma_n$-definable set is, so $M \models \mathrm I\Sigma_n$ by :ref{#thm-friedman-coded}, hence $M \models \mathrm L\Pi_n$, and $M \models \mathrm B\Sigma_n$ if $n \geq 1$. Consider an instance of $\Sigma_{n+1}$ collection. Contracting the quantifiers $\exists y\, \exists z$ into one, we may write it $\forall x < a\ \exists w\ \varphi(x, w)$ with $\varphi \in \Pi_n$; a bound on $w$ bounds the original witnesses. Assume $a > 0$. For $x < a$, let $f(x)$ be the least $w$ with $\varphi(x, w)$, given by $\mathrm L\Pi_n$. The relation $w = f(x)$ is $\varphi(x, w) \wedge \forall w' < w\ \neg \varphi(x, w')$, the conjunction of a $\Pi_n$ formula and of a formula that is $\Sigma_n$ in $M$ by Parsons' lemma (bounded if $n = 0$). Let
$$
\theta(x) \equiv x < a \wedge \forall x' < a\ \big(x \leq x' \rightarrow f(x') \leq f(x)\big),
$$
where $f(x') \leq f(x)$ stands for $\exists w' \leq f(x)\ \varphi(x', w')$. The formula $\theta(x)$ is equivalent in $M$ both to
$$
x < a \wedge \exists w\ \big(w = f(x) \wedge \forall x' < a\ (x \leq x' \rightarrow \exists w' \leq w\ \varphi(x', w'))\big)
$$
and to the same formula with $\exists w\, (w = f(x) \wedge \cdots)$ replaced by $\forall w\, (w = f(x) \rightarrow \cdots)$, since $f(x)$ exists and is unique for $x < a$. The inner formula $\forall x' < a\ (x \leq x' \rightarrow \exists w' \leq w\ \varphi)$ is $\Pi_n$ in $M$, by Parsons' lemma, and $w = f(x)$ is a conjunction of a $\Pi_n$ and a $\Sigma_n$ formula; so the first form is $\Sigma_{n+1}$ and the second $\Pi_{n+1}$. Thus $S = \{ x : \theta(x) \}$ is $\Delta_{n+1}$-definable, and bounded by $a$, so it is coded. It contains $a - 1$, hence it has a least element $w_0$, and let $b = f(w_0)$.

We claim that $f(x) \leq b$ for every $x < a$. For $x \geq w_0$, this is $\theta(w_0)$. Suppose that some $x < w_0$ has $f(x) > b$, that is, $\forall w \leq b\ \neg \varphi(x, w)$, a formula that is $\Sigma_n$ in $M$ by Parsons' lemma. The set $T$ of such $x < w_0$ is coded, by :ref{#thm-friedman-coded}, and nonempty, so it has a largest element $x_0$, by the least number principle applied to the set of its upper bounds. Then $\theta(x_0)$ holds: for $x_0 < x' < w_0$, $x' \notin T$, so $f(x') \leq b < f(x_0)$; for $w_0 \leq x' < a$, $f(x') \leq b < f(x_0)$ by $\theta(w_0)$. This contradicts the minimality of $w_0$, since $x_0 < w_0$. Hence $\forall x < a\ \exists w < b + 1\ \varphi(x, w)$, which is the instance of collection.
:::

:::figure[The proof that coded $\Delta_{n+1}$ sets give collection, with $f(x)$ the least witness for $x < a$. The highlighted points are the $x$ such that $f(x) \geq f(x')$ for all $x' \in [x, a)$; they form a $\Delta_{n+1}$-definable set, whose least element is $w$. The value $b = f(w)$ bounds $f$ on $[w, a)$ by definition, and on $[0, w)$ because a point $x < w$ with $f(x) > b$ would give, taking the largest one, a highlighted point below $w$.]
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="The values f(x) of the least witness function for x up to a; the points x where f(x) is at least f on the interval from x to a are highlighted; w is the least of them, and b = f(w) bounds f everywhere"><line x1="50" y1="190" x2="552" y2="190" class="axis"/><line x1="50" y1="190" x2="50" y2="28" class="axis"/><line x1="60" y1="190" x2="60" y2="151" class="muted-stroke" stroke-width="1"/><circle cx="60" cy="151" r="4" class="node"/><line x1="96" y1="190" x2="96" y2="99" class="muted-stroke" stroke-width="1"/><circle cx="96" cy="99" r="4" class="node"/><line x1="132" y1="190" x2="132" y2="164" class="muted-stroke" stroke-width="1"/><circle cx="132" cy="164" r="4" class="node"/><line x1="168" y1="190" x2="168" y2="73" class="muted-stroke" stroke-width="1"/><circle cx="168" cy="73" r="4" class="node"/><line x1="204" y1="190" x2="204" y2="138" class="muted-stroke" stroke-width="1"/><circle cx="204" cy="138" r="4" class="node"/><line x1="240" y1="190" x2="240" y2="125" class="muted-stroke" stroke-width="1"/><circle cx="240" cy="125" r="4" class="node"/><line x1="276" y1="190" x2="276" y2="47" class="muted-stroke" stroke-width="1"/><circle cx="276" cy="47" r="4.5" class="accent-fill"/><line x1="312" y1="190" x2="312" y2="112" class="muted-stroke" stroke-width="1"/><circle cx="312" cy="112" r="4" class="node"/><line x1="348" y1="190" x2="348" y2="86" class="muted-stroke" stroke-width="1"/><circle cx="348" cy="86" r="4.5" class="accent-fill"/><line x1="384" y1="190" x2="384" y2="151" class="muted-stroke" stroke-width="1"/><circle cx="384" cy="151" r="4" class="node"/><line x1="420" y1="190" x2="420" y2="99" class="muted-stroke" stroke-width="1"/><circle cx="420" cy="99" r="4.5" class="accent-fill"/><line x1="456" y1="190" x2="456" y2="125" class="muted-stroke" stroke-width="1"/><circle cx="456" cy="125" r="4" class="node"/><line x1="492" y1="190" x2="492" y2="112" class="muted-stroke" stroke-width="1"/><circle cx="492" cy="112" r="4.5" class="accent-fill"/><line x1="528" y1="190" x2="528" y2="138" class="muted-stroke" stroke-width="1"/><circle cx="528" cy="138" r="4.5" class="accent-fill"/><line x1="50" y1="47" x2="552" y2="47" class="accent-stroke" stroke-width="1.2" stroke-dasharray="4 3"/><text x="38.0" y="52.0" text-anchor="middle" class="math" font-size="14">b</text><text x="276.0" y="208.0" text-anchor="middle" class="math" font-size="14">w</text><text x="528.0" y="208.0" text-anchor="middle" class="math" font-size="14">a − 1</text><text x="50" y="208" text-anchor="middle" class="mrm" font-size="13">0</text><text x="30.0" y="34.0" text-anchor="middle" class="math" font-size="13">f(x)</text><circle cx="300" cy="18" r="4.5" class="accent-fill"/><text x="310" y="22" class="label">f(x) ≥ f(x′) for all x′ ∈ [x, a)</text></svg>
:::

:::quiz[coded Δₙ₊₁ sets]
In the proof that collection gives coding, why does collection apply to the formula $\varphi(x, y) \vee \neg \psi(x, y)$ rather than to $\varphi(x, y)$?

- [x] Because $\varphi(x, y)$ has a witness only for $x \in S$; collection needs a witness for every $x < a$, and the second disjunct provides one when $x \notin S$, thanks to the $\Pi_{n+1}$ definition of $S$.
- [ ] Because $\varphi(x, y) \vee \neg \psi(x, y)$ is simpler than $\varphi$.

  Both are $\Pi_n$; the disjunct is added to make the hypothesis of collection true.
- [ ] Because $\neg \psi$ is needed to make the formula $\Sigma_{n+1}$.

  The formula $\varphi$ alone is $\Pi_n$, hence $\Sigma_{n+1}$; the complexity is not the issue.
:::

:::corollary[Paris, Kirby]{#cor-bsigma-exp}
For every $n \geq 0$, $\mathrm I\Delta_0 + \mathrm{exp} + \mathrm B\Sigma_{n+1}$ proves $\mathrm I\Sigma_n$.
:::

:::proof{of=cor-bsigma-exp}
Let $M \models \mathrm I\Delta_0 + \mathrm{exp} + \mathrm B\Sigma_{n+1}$. By :ref{#thm-collection-coded}, every $\Delta_{n+1}$-definable set is piecewise coded, in particular every $\Sigma_n$-definable set, and $M \models \mathrm I\Sigma_n$ by :ref{#thm-friedman-coded}. The completeness theorem turns this into a proof.
:::

The axiom $\mathrm{exp}$ is not needed: the direct proof of :ref{#thm-fo-paris-kirby} works over $\mathrm I\Delta_0$. The proof through coded sets explains the result: collection for $\Sigma_{n+1}$ formulas makes bounded $\Delta_{n+1}$ sets finite, and $\Sigma_n$ sets are $\Delta_{n+1}$. Slaman (2004) proved that over $\mathrm I\Delta_0 + \mathrm{exp}$, $\mathrm B\Sigma_n$ is equivalent to induction for $\Delta_n$ formulas; without $\mathrm{exp}$, the case $n = 1$ is open.

## Exercises

::::exercise{difficulty=2}
Let $M$ be a model of $\mathrm{PA}$ with a non-standard element defined by a bounded formula, and $K = K_1(M)$ its set of $\Sigma_1$-definable elements, which is a model of $\mathrm I\Delta_0$ in which $\mathrm B\Sigma_1$ fails (lesson :ref{to="induction-conservation/separations"} of the course on induction and conservation). Show that $K \models \mathrm{exp}$. Deduce that $\mathrm I\Delta_0 + \mathrm{exp}$ does not prove $\mathrm B\Sigma_1$.

:::solution
Let $a \in K$. In $M$, which satisfies $\mathrm{exp}$, the power $2^a$ is the only element $y$ with $\varepsilon(a, y)$, a bounded formula with the parameter $a \in K$. By the first item of the lemma on definable elements in that lesson, an element defined by a $\Sigma_1$ formula with parameters in $K$ belongs to $K$; so $2^a \in K$. Since $K$ is a $\Sigma_1$-elementary substructure of $M$, $K \models \varepsilon(a, 2^a)$. So $K \models \mathrm{exp}$, and $K$ is a model of $\mathrm I\Delta_0 + \mathrm{exp} + \neg \mathrm B\Sigma_1$.
:::
::::

## Notes and references

The characterization of $\Sigma_n$ induction by coded sets is attributed to H. Friedman in Wong's Lecture 2, where the characterization of collection by $\Delta_{n+1}$ sets is called folklore; both are proved in Wong's Lecture 3, whose proof of the second we follow. Hájek and Pudlák prove the forward directions in the form "piecewise coded" (Theorem I.2.7, Lemma I.2.13), and credit the notion to Kossak and the theorem to Clote (1985). The implication $\mathrm B\Sigma_{n+1} \Rightarrow \mathrm I\Sigma_n$ is due to Paris and Kirby (1978). Slaman's theorem is in Slaman (2004); the question whether $\mathrm I\Delta_1$ proves $\mathrm B\Sigma_1$, or $\mathrm L\Delta_1$, without exponentiation, is due to Paris, and remains open according to Wong's notes. Another open problem on collection is whether $\mathrm I\Delta_0 + \neg \mathrm{exp}$ proves $\mathrm B\Sigma_1$, while $\mathrm I\Delta_0 + \mathrm{exp}$ does not, by the exercise; Adamowicz, Kołodziejczyk and Paris (2012) relate it to the existence of truth definitions in models of $\mathrm I\Delta_0 + \neg \mathrm{exp}$, and explain why it has resisted.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 2(a), and the bibliographical remarks to Chapter I.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 2 and 3.
- T. A. Slaman, *Σₙ-bounding and Δₙ-induction*, Proceedings of the American Mathematical Society 132 (2004), 2449–2456.
- Z. Adamowicz, L. A. Kołodziejczyk and J. Paris, *Truth definitions without exponentiation and the Σ₁ collection scheme*, Journal of Symbolic Logic 77 (2012), 649–655.
