---
title: Least numbers, definable cuts and overspill
summary: The least number principles for Σₙ and Πₙ formulas are equivalent to Σₙ induction; a model of PA⁻ satisfies IΣₙ exactly when no proper cut is Σₙ-definable, or Πₙ-definable, with parameters; overspill and underspill for arbitrary cuts.
duration: 35
prerequisites: [induction-collection]
---

Induction for a formula says that the set it defines, if it contains $0$ and is closed under successor, is the whole model. This lesson first shows that the least number principles for $\Sigma_n$ and $\Pi_n$ formulas are equivalent to $\Sigma_n$ induction, which completes the hierarchy of the previous lesson; the proofs already apply induction to the definition of a cut. It then turns induction into a statement about cuts: a model satisfies $\Sigma_n$ induction exactly when none of its proper cuts is definable by a $\Sigma_n$ formula, or by a $\Pi_n$ formula. The second form is immediate; the first needs collection, and its proof shows that a failure of collection also produces a definable cut. The consequence used everywhere in the model theory of arithmetic is **overspill**: a $\Sigma_n$ or $\Pi_n$ property that holds on a proper cut of a model of $\mathrm I\Sigma_n$ also holds somewhat above it.

## Least number principles

The least number principle is induction in another form. If $\varphi(c)$ holds and $\varphi$ has no least element, then the set of $x$ such that $\varphi$ fails at every $y \leq x$ contains $0$, is closed under successor and omits $c$: it is a proper cut. Proving the least number principle by induction thus amounts to applying induction to the formula that defines this cut, and the only difficulty is its complexity, a bounded universal quantifier in front of $\neg \varphi$.

:::proposition{#prop-fo-least-number}
For every $n \geq 1$, the theories $\mathrm I\Sigma_n$, $\mathrm I\Pi_n$, $\mathrm L\Sigma_n$ and $\mathrm L\Pi_n$ are equivalent over $\mathrm I\Delta_0$.
:::

:::proof{of=prop-fo-least-number}
*$\mathrm L\Pi_n$ implies $\mathrm I\Sigma_n$, and $\mathrm L\Sigma_n$ implies $\mathrm I\Pi_n$.* If induction fails for $\varphi$, with $\neg \varphi(a)$, let $m$ be least with $\neg \varphi(m)$; then $m \neq 0$, $m = m' + 1$ with $\varphi(m')$, hence $\varphi(m)$, a contradiction. The negation of a $\Sigma_n$ formula is $\Pi_n$, and conversely.

*$\mathrm I\Sigma_n$ implies $\mathrm L\Pi_n$.* Let $\varphi$ be $\Pi_n$ with $\varphi(c)$ and no least element. Let $\theta(x) \equiv \forall y < x + 1\ \neg \varphi(y)$; it is $\Sigma_n$ by :ref{#lem-fo-collection-closure}, since $\mathrm I\Sigma_n$ proves $\mathrm B\Sigma_n$ (:ref{#thm-fo-parsons}). If $\varphi(0)$, then $0$ is least; so $\theta(0)$. If $\theta(x)$ and $\varphi(x + 1)$, then $x + 1$ is least; so $\theta(x) \rightarrow \theta(x + 1)$. By induction $\theta(c)$, contradicting $\varphi(c)$.

*$\mathrm I\Pi_n$ implies $\mathrm L\Sigma_n$*, by the same argument for $\varphi \in \Sigma_n$; now $\theta$ is $\Pi_n$ logically, a bounded universal quantifier in front of a $\Pi_n$ formula. With :ref{#thm-fo-isigma-ipi}, the four schemes are equivalent.
:::

:::quiz[least number principles]
In the proof of :ref{#prop-fo-least-number}, Parsons' theorem is used to show that $\mathrm I\Sigma_n$ implies $\mathrm L\Pi_n$, but not to show that $\mathrm I\Pi_n$ implies $\mathrm L\Sigma_n$. Why?

- [x] For $\varphi \in \Pi_n$, the formula $\theta(x) \equiv \forall y < x + 1\ \neg \varphi(y)$ is a bounded universal quantifier in front of a $\Sigma_n$ formula, which is $\Sigma_n$ only under $\mathrm B\Sigma_n$; for $\varphi \in \Sigma_n$, it is a bounded universal quantifier in front of a $\Pi_n$ formula, which is $\Pi_n$ logically.
- [ ] Because $\mathrm I\Pi_n$ is stronger than $\mathrm I\Sigma_n$.

  The two schemes are equivalent (:ref{#thm-fo-isigma-ipi}); the difference lies in the complexity of the auxiliary formula $\theta$.
- [ ] To find the least element of the set defined by $\varphi$.

  The proof is by contradiction and never exhibits a least element; collection is used only for the complexity of $\theta$.
:::

For $n = 0$, the equivalence of $\mathrm I\Delta_0$ and $\mathrm L\Delta_0$ was proved in :ref{to="bounded-induction"} (:ref{#prop-idelta0-basic} and the exercise of that lesson).


## Definable cuts

A set that contains $0$ and is closed under successor need not be an initial segment; but a failure of induction produces a cut, the set of elements below which the formula holds everywhere.

:::proposition{#prop-cuts-induction}
Let $M$ be a model of $\mathrm{PA}^-$ and $n \geq 0$. The following are equivalent:

1. $M \models \mathrm I\Sigma_n$;
2. no proper cut of $M$ is $\Pi_n$-definable in $M$, with parameters;
3. no proper cut of $M$ is $\Sigma_n$-definable in $M$, with parameters.
:::

The equivalence of 1 and 3 is the delicate one. The natural cut associated with a failure of $\Sigma_n$ induction for $\theta$ is $\{ x : \forall x' \leq x\ \theta(x') \}$, a bounded universal quantifier in front of a $\Sigma_n$ formula, which is $\Sigma_n$ only in the presence of collection. The proof shows that a failure of collection also produces a $\Sigma_n$-definable proper cut: the set of $c$ such that the values of the multi-valued function on $[0, c)$ are bounded.

:::proof{of=prop-cuts-induction}
A cut contains $0$ and is closed under successor. So if a proper cut is defined by a formula of a class $\Gamma$, induction fails for this formula, and $\mathrm I\Gamma$ fails. Since $\mathrm I\Sigma_n$ and $\mathrm I\Pi_n$ are equivalent over $\mathrm I\Delta_0$, and both contain $\mathrm I\Delta_0$, this proves that 1 implies 2 and 3.

*2 implies 1.* Suppose $\mathrm I\Sigma_n$ fails. If $\mathrm I\Delta_0$ holds, then $\mathrm I\Pi_n$ fails as well; if not, $\mathrm I\Delta_0 \subseteq \mathrm I\Pi_n$ fails. In both cases there is a $\Pi_n$ formula $\theta(x)$, with parameters, such that $\theta(0)$, $\theta(x) \rightarrow \theta(x + 1)$ for all $x$, and $\neg \theta(c)$ for some $c$. Let $J = \{ x : \forall x' < x + 1\ \theta(x') \}$. A bounded universal quantifier in front of a $\Pi_n$ formula gives a $\Pi_n$ formula, logically, so $J$ is $\Pi_n$-definable. It is an initial segment, contains $0$, is closed under successor, since $x' < x + 2$ implies $x' < x + 1$ or $x' = x + 1$, and $\theta(x + 1)$ follows from $\theta(x)$, and does not contain $c$. So $J$ is a $\Pi_n$-definable proper cut.

*3 implies 1*, by induction on $n$. For $n = 0$, it is the previous case. Let $n \geq 1$ and assume 3. Then no proper cut is $\Sigma_{n-1}$-definable, so $M \models \mathrm I\Sigma_{n-1}$ by the induction hypothesis, and $M \models \mathrm B\Sigma_{n-1}$ by Parsons' theorem if $n \geq 2$.

We first show that $M \models \mathrm B\Sigma_n$. Suppose $\forall x < a\ \exists y\ \theta(x, y)$ with $\theta$ in $\Sigma_n$. Contracting quantifiers, $\theta(x, y)$ is $\exists z\ \eta(x, y, z)$ with $\eta \in \Pi_{n-1}$, and $\forall x < a\ \exists w\ \chi(x, w)$ for $\chi(x, w) \equiv \exists y < w\ \exists z < w\ \eta(x, y, z)$. By Parsons' lemma in $\mathrm B\Sigma_{n-1}$ (or because it is bounded, if $n = 1$), $\chi$ is $\Pi_{n-1}$ in $M$, and so is $\forall x < c\ \exists w < b\ \chi(x, w)$. Let
$$
I = \{ c \in M : \exists b\ \forall x < c\ \exists w < b\ \chi(x, w) \},
$$
a $\Sigma_n$-definable set. It is an initial segment and contains $0$. If $c \in I$ and $c < a$, with bound $b$, let $w_0$ satisfy $\chi(c, w_0)$; then $\max(b, w_0 + 1)$ is a bound for $c + 1$, so $c + 1 \in I$. If $a \notin I$, then every element of $I$ is less than $a$, $I$ is closed under successor, and $I$ is a $\Sigma_n$-definable proper cut, contrary to 3. So $a \in I$: some $b$ satisfies $\forall x < a\ \exists w < b\ \chi(x, w)$, hence $\forall x < a\ \exists y < b\ \theta(x, y)$, which is the instance of collection.

Now suppose that $\Sigma_n$ induction fails for $\theta(x)$, with $\theta(0)$, $\theta(x) \rightarrow \theta(x + 1)$ and $\neg \theta(c)$. As in the previous case, $J = \{ x : \forall x' < x + 1\ \theta(x') \}$ is a proper cut, and it is $\Sigma_n$-definable by Parsons' lemma in $\mathrm B\Sigma_n$: a contradiction with 3.
:::

:::quiz[definable cuts]
In the proof that 3 implies 1, why is collection established before induction?

- [x] Because the cut $J$ associated with a failure of $\Sigma_n$ induction is defined by a bounded universal quantifier in front of a $\Sigma_n$ formula, which is $\Sigma_n$ only in models of $\mathrm B\Sigma_n$.
- [ ] Because $\mathrm B\Sigma_n$ implies $\mathrm I\Sigma_n$.

  It does not: $\mathrm B\Sigma_n$ only implies $\mathrm I\Sigma_{n-1}$, and the converse implication $\mathrm I\Sigma_n \Rightarrow \mathrm B\Sigma_n$ is Parsons' theorem.
- [ ] Because the cut $I$ is needed to define $J$.

  The two cuts are defined independently; $I$ is used only to prove collection.
:::

The proposition is usually applied in the form of **overspill**, which applies in particular to the standard part of a non-standard model.

:::corollary[Overspill]{#cor-overspill}
Let $M \models \mathrm I\Sigma_n$, let $I$ be a proper cut of $M$, and let $\theta(x)$ be a $\Sigma_n$ or $\Pi_n$ formula with parameters in $M$ such that $M \models \theta(x)$ for every $x \in I$. Then for every $b \in M \setminus I$, there is $x \in M \setminus I$ with $x \leq b$ and $M \models \theta(x)$.
:::

:::proof{of=cor-overspill}
Otherwise, the formula $x \leq b \wedge \theta(x)$, which is $\Sigma_n$ or $\Pi_n$, defines exactly $I$: every element of $I$ is below $b$ and satisfies $\theta$, and no element of $M \setminus I$ below $b$ satisfies $\theta$. This contradicts :ref{#prop-cuts-induction}.
:::

## Exercises

::::exercise{#ex-underspill difficulty=1}
(**Underspill.**) Let $M \models \mathrm I\Sigma_n$, $I$ a proper cut of $M$, and $\theta(x)$ a $\Sigma_n$ or $\Pi_n$ formula with parameters such that $M \models \theta(x)$ for every $x \in M \setminus I$. Show that $M \models \theta(x)$ for some $x \in I$.

:::solution
Otherwise $\neg \theta$ holds exactly on $I$: on $I$ by assumption, and nowhere outside $I$ by hypothesis. The formula $\neg \theta$ is $\Pi_n$ or $\Sigma_n$, so $I$ is a $\Pi_n$- or $\Sigma_n$-definable proper cut, contradicting :ref{#prop-cuts-induction}.
:::
::::

::::exercise{#ex-overspill-interval difficulty=2}
Let $M$ be a non-standard model of $\mathrm I\Sigma_n$, $n \geq 1$, and $\theta(x)$ a $\Sigma_n$ formula with parameters such that $M \models \theta(k)$ for every standard $k$. Show that there is a non-standard $c$ such that $M \models \theta(x)$ for every $x \leq c$.

:::solution
The formula $\forall x \leq y\ \theta(x)$ is $\Sigma_n$ in $M$, by :ref{#lem-fo-collection-closure}, since $M \models \mathrm B\Sigma_n$ by :ref{#thm-fo-parsons}. It holds for every standard $y$, since the elements below a standard $y$ are standard. By :ref{#cor-overspill}, applied to the standard part, it holds for some non-standard $c$.
:::
::::

## Notes and references

The equivalence of the induction and least number schemes is Wong's Theorem 2.3 (Lecture 2), attributed there to Paris and Kirby, and Hájek and Pudlák's Theorem I.2.4, proved through their Lemma I.2.8. :ref{#prop-cuts-induction} is Wong's Proposition 3.3 (Lecture 3), given there with a proof sketch that does not mention the role of collection; the proof of the $\Sigma_n$ case given here, through the cut produced by a failure of collection, is added. Overspill goes back to A. Robinson; Wong discusses its variants and underspill. The second-order version of overspill for the standard part is in the course on induction and conservation.

- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 2 and 3.
- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 2(a).
