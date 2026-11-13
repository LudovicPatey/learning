---
title: End extensions and collection
summary: A model with a proper Σₙ-elementary end extension satisfying IΣₙ satisfies BΣₙ₊₁ (Paris and Kirby), and the converse for countable models is stated; Σₙ₊₁ induction is equivalent to collection for partial functions (Friedman).
duration: 40
prerequisites: [cofinal-extensions, fragments-of-arithmetic/definable-cuts]
---

Collection is the scheme that end extensions see. If a model $M$ sits as a proper initial segment inside a model $K$, with enough elementarity, then every element of $K$ above $M$ is a common bound, in $K$, for witnesses chosen in $M$; underspill brings such a bound down into $M$, and $M$ satisfies collection. This lesson proves this theorem of Paris and Kirby and states its converse for countable models. It then proves a strengthening of collection that holds in models of induction, Friedman's **strong collection**, which bounds the witnesses of a partial function; the next lesson uses it to split extensions and to derive a conservation theorem.

## End extensions give collection

:::theorem[Paris, Kirby]{#thm-end-ext-collection}
Let $n \geq 0$, let $M$ be a model of $\mathrm{PA}^-$ and $K$ a model of $\mathrm I\Sigma_n$ such that $M \subseteq_e K$, $M \neq K$ and $M \preccurlyeq_n K$. Then $M \models \mathrm B\Sigma_{n+1}$.
:::

Given an instance $\forall x < a\ \exists y\ \varphi(x, y)$ in $M$, every element $b$ of $K$ above $M$ bounds the witnesses chosen in $M$, and the statement "$b$ bounds witnesses for all $x < a$" is $\Pi_n$ in $K$. It holds on the whole of $K \setminus M$, so by underspill it holds at some $b \in M$; it then transfers down to $M$.

:::proof{of=thm-end-ext-collection}
The model $M$ is a cut of $K$ closed under addition and multiplication, so $M \models \mathrm I\Delta_0$ by :ref{#lem-cut-model}. It remains to prove collection for $\Sigma_{n+1}$ formulas. By contraction of quantifiers (:ref{to="fragments-of-arithmetic/induction-collection"}) if $n = 0$, and by :ref{#ex-fo-bsigma-bpi} if $n \geq 1$, it suffices to prove collection for $\Pi_n$ formulas. Let $\varphi(x, y)$ be $\Pi_n$, with parameters in $M$, and $a \in M$ with $M \models \forall x < a\ \exists y\ \varphi(x, y)$. Let
$$
\psi(b) \equiv \forall x < a\ \exists y < b\ \varphi(x, y).
$$
If $n = 0$, $\psi$ is bounded; if $n \geq 1$, $K \models \mathrm B\Sigma_n$ by :ref{#thm-fo-parsons}, and $\psi$ is equivalent in $K$ to a $\Pi_n$ formula by :ref{#lem-fo-collection-closure}.

*$\psi$ holds on $K \setminus M$.* Let $b \in K \setminus M$ and $x < a$. Then $x \in M$, since $M$ is an initial segment, so some $y \in M$ satisfies $M \models \varphi(x, y)$; then $K \models \varphi(x, y)$, by $M \preccurlyeq_n K$, and $y < b$.

*Underspill.* Since $K \models \mathrm I\Sigma_n$ and $M$ is a proper cut of $K$, underspill for $\Pi_n$ formulas (:ref{#ex-underspill}, a consequence of :ref{#prop-cuts-induction}) gives $b \in M$ with $K \models \psi(b)$.

*Transfer down.* Let $x < a$. Some $y < b$ satisfies $K \models \varphi(x, y)$; then $y \in M$, as $b \in M$, and $M \models \varphi(x, y)$ by $M \preccurlyeq_n K$. So $M \models \forall x < a\ \exists y < b\ \varphi(x, y)$.
:::

:::figure[The proof of :ref{#thm-end-ext-collection}. Every $b \in K \setminus M$ bounds witnesses, chosen in $M$, for all $x < a$. Underspill brings such a bound $b_0$ into $M$, and the witnesses below $b_0$ are elements of $M$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The proof that end extensions give collection: every b in K above M bounds witnesses for all x below a; underspill gives such a bound b0 inside M"><line x1="20.0" y1="80.0" x2="580.0" y2="80.0" class="ink-stroke" stroke-width="1.2"/><circle cx="24.0" cy="80.0" r="3.5" class="accent-fill"/><text x="24" y="66" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="110.0" cy="80.0" r="3.5" class="ink-fill"/><text x="110.0" y="66.0" text-anchor="middle" class="math" font-size="14">a</text><circle cx="250.0" cy="80.0" r="4" class="accent-fill"/><text x="250.0" y="66.0" text-anchor="middle" class="math" font-size="14">b<tspan class="mrm" font-size="10" dy="3">0</tspan></text><line x1="330.0" y1="58.0" x2="330.0" y2="102.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="330.0" y="50.0" text-anchor="middle" class="math" font-size="13">M</text><circle cx="400.0" cy="80.0" r="3.5" class="node"/><circle cx="460.0" cy="80.0" r="3.5" class="node"/><circle cx="520.0" cy="80.0" r="3.5" class="node"/><path d="M460,88 C420,120 300,120 256,88" class="accent-stroke" fill="none" stroke-width="1.4"/><text x="355" y="132" text-anchor="middle" class="label">underspill</text><path d="M370,60 L370,54 L578,54 L578,60" class="muted-stroke" stroke-width="1.2"/><text x="474.0" y="44" text-anchor="middle" class="label">every b ∈ K ∖ M bounds witnesses for x &lt; a</text></svg>
:::

:::quiz[end extensions and collection]
Where is the hypothesis $K \models \mathrm I\Sigma_n$ used?

- [x] In the underspill step, which needs $\Pi_n$ induction in $K$, and, for $n \geq 1$, to make $\psi$ a $\Pi_n$ formula of $K$ through $\mathrm B\Sigma_n$.
- [ ] To show that $M$ satisfies $\mathrm I\Delta_0$.

  This uses only that $M$ is a cut of a model of $\mathrm I\Delta_0$ closed under the operations.
- [ ] To transfer $\varphi(x, y)$ from $M$ to $K$.

  This uses $M \preccurlyeq_n K$, not induction in $K$.

---

Where is it used that $M \neq K$?

- [x] Underspill concerns a property that holds on the non-empty set $K \setminus M$; if $M = K$ the hypothesis is empty and nothing follows.
- [ ] To have $M \preccurlyeq_n K$.

  Elementarity is a hypothesis, and holds trivially for $M = K$.
- [ ] To show that $x < a$ implies $x \in M$.

  This uses only that $M$ is an initial segment of $K$.
:::

The converse direction is also due to Paris and Kirby: collection gives elementary end extensions. Its proof constructs the extension as an ultrapower of $M$ by definable functions, with an ultrafilter on the definable sets of $M$ chosen with the help of collection; this method of definable types belongs to the next course of the track, where it gives the theorem of MacDowell and Specker. We state the result.

:::fact[Paris, Kirby]{#fact-end-ext-converse}
Let $n \geq 1$ and $M$ a countable model of $\mathrm I\Delta_0$. Then $M \models \mathrm B\Sigma_{n+1}$ if and only if $M$ has a proper $\Sigma_{n+1}$-elementary end extension that satisfies $\mathrm I\Delta_0$.
:::

The extension is only required to satisfy $\mathrm I\Delta_0$, so the implication from right to left is not an instance of :ref{#thm-end-ext-collection} as proved here, which needs $\mathrm I\Sigma_n$ in $K$. It follows, by induction on $n$, from the stronger theorem of Adamowicz, Clote and Wilkie recalled in the notes, which only needs $\mathrm I\Sigma_{n-1}$ in $K$: if $M$ already satisfies $\mathrm B\Sigma_n$, hence $\mathrm I\Sigma_{n-1}$, then $K$ satisfies $\mathrm I\Sigma_{n-1}$ too, since this theory is axiomatized by $\Pi_{n+1}$ sentences, which go up from $M$ to a $\Sigma_{n+1}$-elementary extension. Hájek and Pudlák give a direct proof (IV.1.56). In the other direction, their construction of the extension needs $n \geq 1$. For $n = 0$, a proper $\Sigma_1$-elementary end extension satisfying $\mathrm I\Delta_0$ already gives $\mathrm B\Sigma_2$ (Hájek and Pudlák, Theorem IV.1.53 (2)), and whether every countable model of $\mathrm B\Sigma_1$ has a proper end extension satisfying $\mathrm I\Delta_0$ is an open problem of Paris (Wong, Question 6.9).

The theory of the extension is not determined by this fact, and the best possible end extensions are the subject of recent work. Clote asked, after Kaufmann, whether every countable model of $\mathrm B\Sigma_{n+2}$ has a proper $\Sigma_{n+2}$-elementary end extension satisfying $\mathrm B\Sigma_{n+1}$; Mengzhou Sun (2025) answered positively.

## Collection for partial functions

Collection bounds the values of a definable function on $[0, a)$ that is *total* on $[0, a)$. **Strong collection** asks the same for partial functions: whatever subset of $[0, a)$ has witnesses, a single bound $b$ catches a witness for each of its elements. This is stronger, because the set of elements that have a witness may be more complex than its witnesses, and its strength is that of induction one level up.

:::theorem[Friedman]{#thm-strong-collection}
Let $n \geq 0$. Over $\mathrm I\Delta_0$, $\mathrm I\Sigma_{n+1}$ is equivalent to the **strong $\Pi_n$ collection** scheme: the universal closures of
$$
\exists b\ \forall x < a\ \big( \exists y\ \eta(x, y) \rightarrow \exists y < b\ \eta(x, y) \big)
$$
for $\eta \in \Pi_n$, with parameters.
:::

:::proof{of=thm-strong-collection}
*Induction gives strong collection.* Assume $\mathrm I\Sigma_{n+1}$; it contains $\mathrm I\Sigma_1$, hence $\mathrm{exp}$ (:ref{#prop-isigma1-exp}). By :ref{#thm-friedman-coded}, some $c$ codes $\{ x < a : \exists y\ \eta(x, y) \}$ below $a$. Then $\forall x < a\ \exists y\ (x \notin c \vee \eta(x, y))$: for $x \in c$ a witness exists, and otherwise any $y$ will do. The formula in parentheses is $\Pi_n$, hence $\Sigma_{n+1}$, and $\mathrm B\Sigma_{n+1}$, which $\mathrm I\Sigma_{n+1}$ proves (:ref{#thm-fo-parsons}), gives $b$ with $\forall x < a\ \exists y < b\ (x \notin c \vee \eta(x, y))$. If $x < a$ has a witness, then $x \in c$, and some $y < b$ satisfies $\eta(x, y)$.

*Strong collection gives induction*, by induction on $n$. Strong $\Pi_n$ collection contains strong $\Pi_{n-1}$ collection for $n \geq 1$, so the induction hypothesis gives $\mathrm I\Sigma_n$, hence $\mathrm B\Sigma_n$ if $n \geq 1$; for $n = 0$ we have $\mathrm I\Delta_0$. Let $\varphi(x) \equiv \exists y\ \eta(x, y)$ with $\eta \in \Pi_n$ (after contraction), and assume $\varphi(0)$, $\forall x\, (\varphi(x) \rightarrow \varphi(x + 1))$ and $\neg \varphi(a)$. Strong collection gives $b$ with $\forall x < a + 1\ (\varphi(x) \rightarrow \exists y < b\ \eta(x, y))$. Let $\psi(x) \equiv \exists y < b\ \eta(x, y)$, which is bounded if $n = 0$ and $\Pi_n$ by :ref{#lem-fo-collection-closure} if $n \geq 1$. For $x \leq a$, $\varphi(x) \leftrightarrow \psi(x)$. Apply $\Pi_n$ induction (:ref{#thm-fo-isigma-ipi}), or bounded induction if $n = 0$, to $x \leq a \rightarrow \psi(x)$: it holds at $0$, and if $x + 1 \leq a$ and $\psi(x)$, then $\varphi(x)$, $\varphi(x + 1)$ and $\psi(x + 1)$. So $\psi(a)$, hence $\varphi(a)$, a contradiction.
:::

:::quiz[strong collection]
In the proof that induction gives strong collection, why is the set $\{ x < a : \exists y\ \eta(x, y) \}$ coded first, rather than applying collection directly?

- [x] Collection needs a witness for every $x < a$. The formula $\exists y\ \eta(x, y) \rightarrow \eta(x, y)$ would provide one, but it is $\Sigma_{n+1} \rightarrow \Pi_n$, that is, of complexity $\Pi_{n+1} \vee \Pi_n$, too high for $\mathrm B\Sigma_{n+1}$; replacing the hypothesis by the bounded formula $x \in c$ keeps the formula $\Pi_n$.
- [ ] Because $\mathrm I\Sigma_{n+1}$ does not prove $\mathrm B\Sigma_{n+1}$.

  It does, by Parsons' theorem; the issue is the complexity of the formula to which collection is applied.
- [ ] To make the bound $b$ smaller than $a$.

  No relation between $b$ and $a$ is claimed.
:::

The same theorem holds for strong $\Sigma_{n+1}$ collection, as the exercise below shows.

## Exercises

::::exercise{difficulty=1}
The **strong $\Sigma_{n+1}$ collection** scheme consists of the universal closures of $\exists b\ \forall x < a\ (\exists y\ \varphi(x, y) \rightarrow \exists y < b\ \varphi(x, y))$ for $\varphi \in \Sigma_{n+1}$. Show that, over $\mathrm I\Delta_0$, it is equivalent to strong $\Pi_n$ collection, hence to $\mathrm I\Sigma_{n+1}$.

:::solution
A $\Pi_n$ formula is $\Sigma_{n+1}$, so strong $\Sigma_{n+1}$ collection implies strong $\Pi_n$ collection. Conversely, let $\varphi(x, y) \equiv \exists z\ \eta(x, y, z)$ with $\eta \in \Pi_n$, a block of quantifiers $\exists z$ being contracted to one by pairing (:ref{#fact-pairing}). Let $\eta'(x, w) \equiv \exists y \leq w\ \exists z \leq w\ (w = \langle y, z \rangle \wedge \eta(x, y, z))$; since the pair $w$ determines $y$ and $z$, $\eta'$ is equivalent in $\mathrm I\Delta_0$ to $\forall y \leq w\ \forall z \leq w\ (w = \langle y, z \rangle \rightarrow \eta(x, y, z)) \wedge \exists y \leq w\ \exists z \leq w\ (w = \langle y, z \rangle)$, a $\Pi_n$ formula logically, as the bounded universal quantifiers merge with the first block of $\eta$. Strong $\Pi_n$ collection for $\eta'$ gives $b$ such that every $x < a$ with $\exists w\ \eta'(x, w)$ has such a $w < b$. If $x < a$ and $\exists y\ \varphi(x, y)$, then $\exists w\ \eta'(x, w)$, so some $w = \langle y, z \rangle < b$ satisfies $\eta(x, y, z)$; since $y \leq w$, $y < b$ and $\varphi(x, y)$. For $n = 0$ the same argument applies with $\eta$ bounded.
:::
::::

## Notes and references

:ref{#thm-end-ext-collection} is Wong's Theorem 6.3 and Lemma IV.1.22 of Hájek and Pudlák (Paris and Kirby, 1978). Wong reports that Adamowicz, Clote and Wilkie showed that for $n \geq 1$ the hypothesis on $K$ can be weakened to $\mathrm I\Sigma_{n-1}$, citing Clote (1985). :ref{#fact-end-ext-converse} is Theorem IV.1.53 (1) of Hájek and Pudlák, proved there by a definable ultrapower (IV.1.56–1.57); the case $n = 0$ is their Theorem IV.1.53 (2). The question of Clote and Kaufmann is Wong's Question 6.11, and Paris's problem on end extensions of models of $\mathrm B\Sigma_1$ is his Question 6.9; the answer to the first is in Sun (2025). :ref{#thm-strong-collection} is Wong's Theorem 6.4, attributed there to H. Friedman, with the remark that $\Pi_n$ may be replaced by $\Sigma_{n+1}$ (Remark 6.5); the proof of the second direction given here, by an induction on the bounded formula $\psi$, replaces Wong's argument.

- J. B. Paris and L. A. S. Kirby, *Σₙ-collection schemas in arithmetic*, in Logic Colloquium '77, North-Holland, 1978, 199–209.
- P. Clote, *Partition relations in arithmetic*, in Methods in Mathematical Logic, Lecture Notes in Mathematics 1130, Springer, 1985, 32–68.
- M. Sun, *The Kaufmann–Clote question on end extensions of models of arithmetic and the weak regularity principle*, Journal of Symbolic Logic, 2025 (arXiv:2409.03527).
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 6.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Sections 1(c) and 1(e).
