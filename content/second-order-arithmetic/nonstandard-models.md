---
title: Non-standard models
summary: Non-standard models of arithmetic and of RCA₀; full structures have a standard first-order part; overspill; the standard part is never a set of a model of RCA₀; finite versus bounded sets.
duration: 40
prerequisites: [rca0]
---

The ω-models of the previous lesson measure comprehension: their numbers are the true natural numbers, so every instance of induction holds in them, and two systems that differ only in their induction axioms have the same ω-models. To see induction at work, one needs models whose first-order part contains **non-standard** numbers, larger than every standard number. This lesson shows that such models exist, explains why the semantics of second-order arithmetic must allow them, and proves the basic tool for working in them, **overspill**: a property expressed by a $\Sigma^0_1$ formula that holds of every standard number must hold of some non-standard number. Its consequence is that the sets of a model never single out the standard numbers, and that "finite" in a model of $\mathsf{RCA}_0$ differs from finite in reality.

Throughout, $k^{\mathcal M}$ denotes the interpretation in a structure $\mathcal M$ of the term $1 + \cdots + 1$ with $k$ summands ($0^{\mathcal M}$ for $k = 0$). The elements $k^{\mathcal M}$ are the **standard** elements of $\mathcal M$; when the map $k \mapsto k^{\mathcal M}$ is not onto, $\mathcal M$ is **non-standard**.

## Existence

Let $T$ be the set of first-order sentences, in the language of arithmetic, that are true in $\nat$. Add a new constant $c$ and the sentences $c > k$ for every $k \in \nat$, where $k$ stands for the term $1 + \cdots + 1$. Every finite subset of this theory is satisfied by $\nat$, with $c$ interpreted as a large enough number, so by the compactness theorem the whole theory has a model $M$. In $M$, the element $c$ is above every standard element.

The standard elements of such an $M$ form an initial segment: from the axioms $\neg (m < 0)$ and $m < n + 1 \leftrightarrow (m < n \vee m = n)$, an induction on $k$ in the metatheory shows that every element below $k^{M}$ is some $j^{M}$ with $j < k$. Above them come the non-standard elements; since $M$ satisfies the true sentences "every non-zero number has a predecessor" and "the order is linear and discrete", each non-standard element lies in a block of elements ordered like $\mathbb Z$ (:ref{#fig-nonstandard-order}).

:::figure[The order of a non-standard model of arithmetic. The standard part is an initial segment that contains $0$ and is closed under successor, but it has an upper bound $c$. The induction axiom therefore fails as soon as the standard part is a set of the model.]{#fig-nonstandard-order}
<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="The order of a non-standard model: the standard numbers, followed by blocks ordered like the integers"><line x1="20" y1="60" x2="196" y2="60" class="ink-stroke" stroke-width="1.2"/><circle cx="30" cy="60" r="3.5" class="accent-fill"/><text x="30" y="48" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="60" cy="60" r="3.5" class="accent-fill"/><text x="60" y="48" text-anchor="middle" class="mrm" font-size="13">1</text><circle cx="90" cy="60" r="3.5" class="accent-fill"/><text x="90" y="48" text-anchor="middle" class="mrm" font-size="13">2</text><circle cx="120" cy="60" r="3.5" class="accent-fill"/><text x="120" y="48" text-anchor="middle" class="mrm" font-size="13">3</text><circle cx="150" cy="60" r="3.5" class="accent-fill"/><text x="150" y="48" text-anchor="middle" class="mrm" font-size="13">4</text><circle cx="180" cy="60" r="3.5" class="accent-fill"/><text x="218" y="64" text-anchor="middle" class="mrm" font-size="14">⋯</text><line x1="248" y1="60" x2="372" y2="60" class="ink-stroke" stroke-width="1.2"/><text x="236" y="64" text-anchor="middle" class="mrm" font-size="14">⋯</text><text x="386" y="64" text-anchor="middle" class="mrm" font-size="14">⋯</text><circle cx="260" cy="60" r="3.5" class="ink-fill"/><circle cx="285" cy="60" r="3.5" class="ink-fill"/><circle cx="310" cy="60" r="3.5" class="ink-fill"/><circle cx="335" cy="60" r="3.5" class="ink-fill"/><circle cx="360" cy="60" r="3.5" class="ink-fill"/><line x1="398" y1="60" x2="522" y2="60" class="ink-stroke" stroke-width="1.2"/><text x="386" y="64" text-anchor="middle" class="mrm" font-size="14">⋯</text><text x="536" y="64" text-anchor="middle" class="mrm" font-size="14">⋯</text><circle cx="410" cy="60" r="3.5" class="ink-fill"/><circle cx="435" cy="60" r="3.5" class="ink-fill"/><circle cx="460" cy="60" r="3.5" class="ink-fill"/><circle cx="485" cy="60" r="3.5" class="ink-fill"/><circle cx="510" cy="60" r="3.5" class="ink-fill"/><text x="435" y="48" text-anchor="middle" class="math" font-size="13">c<tspan class="mrm">−1</tspan></text><text x="460" y="48" text-anchor="middle" class="math" font-size="13">c</text><text x="485" y="48" text-anchor="middle" class="math" font-size="13">c<tspan class="mrm">+1</tspan></text><path d="M22,80 L22,86 L200,86 L200,80" class="muted-stroke" stroke-width="1.2"/><text x="111.0" y="104" text-anchor="middle" class="label">standard part: 0, 1, 2, …</text><path d="M236,80 L236,86 L540,86 L540,80" class="muted-stroke" stroke-width="1.2"/><text x="388.0" y="104" text-anchor="middle" class="label">non-standard numbers: blocks ordered like ℤ</text><text x="300" y="132" text-anchor="middle" class="label">the standard part contains 0, is closed under successor, and is bounded by c</text></svg>
:::

Non-standard first-order parts can be completed into models of second-order theories.

:::example{#ex-definable-model}
Let $M$ be a non-standard model of the true first-order sentences, and let $\mathcal S$ be the class of subsets of $M$ definable in $M$ by first-order formulas with parameters from $M$. Then $(M, \mathcal S)$ is a model of $\mathsf{RCA}_0$, and even of arithmetic comprehension. An arithmetic formula $\varphi(n)$ with set parameters $X_1, \dots, X_k \in \mathcal S$ becomes a first-order formula with parameters from $M$ when each atomic formula $t \in X_i$ is replaced by a definition of $X_i$. The set it defines is then definable, hence in $\mathcal S$: this gives comprehension for arithmetic formulas. For induction, the first-order sentence
$$
\forall \bar y\, \big( (\psi(0, \bar y) \wedge \forall n\, (\psi(n, \bar y) \rightarrow \psi(n+1, \bar y))) \rightarrow \forall n\, \psi(n, \bar y) \big)
$$
is true in $\nat$ for every first-order formula $\psi$, hence true in $M$; applied to the translation $\psi$ of $\varphi$, it gives induction for $\varphi$.
:::

## Full structures are standard

The second-order part of the model of :ref{#ex-definable-model} is much smaller than $\mathcal P(M)$. This is necessary: a full structure satisfying the induction axiom has no non-standard numbers.

:::proposition[Dedekind]{#prop-full-standard}
Let $\mathcal M = (M, \mathcal P(M), \dots)$ be a full structure satisfying the basic axioms and the induction axiom. Then the map $k \mapsto k^{\mathcal M}$ is an isomorphism from $\nat$ onto the first-order part of $\mathcal M$.
:::

:::proof{of=prop-full-standard}
Let $D = \{ k^{\mathcal M} : k \in \nat \}$. It belongs to $\mathcal P(M)$, contains $0^{\mathcal M}$ and is closed under successor, so $D = M$ by the induction axiom. The map is injective: if $k^{\mathcal M} = l^{\mathcal M}$ with $k < l$ and $k$ least, then $k \neq 0$ by the axiom $n + 1 \neq 0$, and the axiom $m + 1 = n + 1 \rightarrow m = n$ gives a smaller counterexample $k - 1, l - 1$. The recursion equations for $+$ and $\cdot$ show by induction on $l$ (in the metatheory) that $k^{\mathcal M} + l^{\mathcal M} = (k + l)^{\mathcal M}$ and $k^{\mathcal M} \cdot l^{\mathcal M} = (k l)^{\mathcal M}$, and the two axioms on $<$ show by induction on $l$ that $k^{\mathcal M} < l^{\mathcal M}$ if and only if $k < l$.
:::

:::quiz[full structures]
In the proof of :ref{#prop-full-standard}, where is it used that the structure is full?

- [x] To apply the induction axiom to $D$: the axiom only speaks of sets of the second-order part, and $D$ belongs to it because every subset of $M$ does.
- [ ] To show that the map is injective.

  Injectivity uses only the two axioms on successor.
- [ ] To compute $k^{\mathcal M} + l^{\mathcal M}$.

  The recursion equations for $+$ hold in every model of the basic axioms.
:::

So the full semantics pins down $\nat$: $\mathsf Z_2$ has a unique full model up to isomorphism. This is why it is not the semantics of reverse mathematics. No effective proof system is complete for it, since the sentences true in $\mathcal P(\nat)$ do not form a computably enumerable set: they include all true first-order sentences, which are not even arithmetically definable, by Tarski's theorem. Henkin semantics keeps the completeness theorem, at the price of admitting models such as :ref{#ex-definable-model}, from which sets like the standard part are missing.

## Overspill

In a non-standard model, the standard part is a subset of $M$ that contains $0$, is closed under successor, and is not all of $M$. If it were defined by a formula for which induction holds, induction would fail. Turned around, this gives the main tool for non-standard models.

:::proposition[overspill]{#prop-overspill}
Let $\mathcal M$ be a non-standard model of $\mathsf{RCA}_0$, and $\varphi(n)$ a $\Sigma^0_1$ or $\Pi^0_1$ formula with parameters from $\mathcal M$. If $\mathcal M \models \varphi(k^{\mathcal M})$ for every $k \in \nat$, then $\mathcal M \models \varphi(c)$ for some non-standard $c$.
:::

:::proof{of=prop-overspill}
Suppose that $\varphi$ holds in $\mathcal M$ exactly at the standard elements. Then $\mathcal M \models \varphi(0)$, and $\mathcal M \models \forall n\, (\varphi(n) \rightarrow \varphi(n+1))$: if $\varphi(n)$ holds, $n$ is standard, so is $n + 1$, and $\varphi(n + 1)$ holds. By $\Sigma^0_1$ induction, or $\Pi^0_1$ induction (:ref{#prop-pi01-induction}), $\mathcal M \models \forall n\, \varphi(n)$, so $\varphi$ holds at a non-standard element, a contradiction.
:::

The proof uses only the induction scheme for $\varphi$, so overspill holds for every class of formulas for which the model satisfies induction: for all arithmetic formulas in a model of arithmetic comprehension, for instance.

:::corollary{#cor-standard-not-set}
In a non-standard model $(M, \mathcal S)$ of $\mathsf{RCA}_0$, the set of standard elements does not belong to $\mathcal S$. More generally, a set $X \in \mathcal S$ that contains every standard element contains a non-standard one.
:::

:::proof{of=cor-standard-not-set}
Apply :ref{#prop-overspill} to the bounded formula $n \in X$.
:::

## Finite and bounded sets

In $\mathsf{RCA}_0$, finite sets are coded by numbers: there is a coding in which "$i$ belongs to the set coded by $c$" is expressed by a bounded formula, and $\mathsf{RCA}_0$ proves that every bounded set has a code and that every coded set exists (Simpson, Theorem II.2.5; Dzhafarov–Mummert, Theorem 5.5.8 and Proposition 5.5.9). So in a model $(M, \mathcal S)$ of $\mathsf{RCA}_0$, a set $X \subseteq M$ is coded by an element of $M$ if and only if $X \in \mathcal S$ and $X$ is bounded in $M$. Such sets are called **$\mathcal M$-finite**, and they are the sets that the model regards as finite.

In a non-standard model, the two notions of finiteness come apart in both directions.

- For a non-standard $c$, the set $\{ i : i \leq c \}$ is $\mathcal M$-finite, since it is bounded and defined by a bounded formula, hence in $\mathcal S$. From outside, it is infinite: it contains every standard element.
- The set of standard elements is bounded by $c$, and is not $\mathcal M$-finite, since it is not in $\mathcal S$ by :ref{#cor-standard-not-set}.

Arguments by induction must therefore be read inside the model. "By induction on the size of a finite set" refers to $\mathcal M$-finite sets and their sizes in $M$, and is valid only for formulas within reach of the available induction.

:::quiz[overspill]
In the proof of :ref{#prop-overspill}, why does $\mathcal M \models \varphi(n) \rightarrow \varphi(n+1)$ hold for a non-standard $n$?

- [x] Because $\varphi(n)$ is false at every non-standard $n$, under the assumption made for a contradiction, so the implication holds vacuously.
- [ ] Because $\varphi$ is $\Sigma^0_1$.

  The complexity of $\varphi$ is used only to apply the induction scheme; the implication at non-standard $n$ comes from the assumption that $\varphi$ fails there.
- [ ] Because $n + 1$ is standard when $n$ is.

  This is the argument for standard $n$; for non-standard $n$, the antecedent is false.

---

Why does :ref{#cor-standard-not-set} not contradict the fact that $\{ i : i \leq c \}$, for a non-standard $c$, belongs to $\mathcal S$?

- [x] Because $\{ i : i \leq c \}$ contains non-standard elements, such as $c$ itself, as the corollary predicts for a set of $\mathcal S$ containing every standard element.
- [ ] Because $\{ i : i \leq c \}$ is not bounded.

  It is bounded by $c$.
- [ ] Because the corollary only applies to infinite sets.

  The corollary applies to every set of $\mathcal S$ that contains all standard elements, whatever the model thinks of its size.
:::

## The role of induction

In a model of $\mathsf{RCA}_0$, induction holds for $\Sigma^0_1$ formulas, but may fail for $\Sigma^0_2$ formulas; the failure takes the form of a proper initial segment of the first-order part, closed under successor and defined by a $\Sigma^0_2$ formula, much like the standard part in :ref{#fig-nonstandard-order}. Statements of combinatorics can then fail for reasons that have nothing to do with comprehension. Hirst showed that the infinite pigeonhole principle for arbitrarily many colors is equivalent over $\mathsf{RCA}_0$ to $\Sigma^0_2$ bounding, a consequence of $\Sigma^0_2$ induction; it holds in every ω-model, and fails in some non-standard models of $\mathsf{RCA}_0$. In the other direction, the first-order part of $\mathsf{RCA}_0$ is exactly $\mathrm I\Sigma_1$: every first-order sentence provable in $\mathsf{RCA}_0$ is provable from the basic axioms and $\Sigma_1$ induction (Friedman). The proofs build, from a model of $\mathrm I\Sigma_1$, a second-order part made of definable sets, as in :ref{#ex-definable-model}. These results are the subject of the course on induction and conservation (:ref{to="induction-conservation/first-order-parts"}).

## Exercises

::::exercise{difficulty=1}
**Underspill.** Let $\mathcal M$ be a non-standard model of $\mathsf{RCA}_0$ and $\varphi$ a $\Sigma^0_1$ or $\Pi^0_1$ formula with parameters. Show that if $\mathcal M \models \varphi(c)$ for every non-standard $c$, then $\mathcal M \models \varphi(k^{\mathcal M})$ for some $k \in \nat$.

:::solution
Otherwise $\neg \varphi$ holds at every standard element. The formula $\neg \varphi$ is equivalent to a $\Pi^0_1$ or $\Sigma^0_1$ formula, so by :ref{#prop-overspill} it holds at some non-standard $c$, contradicting the hypothesis.
:::
::::

::::exercise{difficulty=2}
Let $(M, \mathcal S)$ be a non-standard model of $\mathsf{RCA}_0$ and $X \in \mathcal S$ a set all of whose elements are standard. Show that $X$ is finite (in reality) and $\mathcal M$-finite. Show that the hypothesis that the model is non-standard is needed.

:::solution
Suppose that $X$ is infinite. Then for every $k \in \nat$ there is an element of $X$ above $k^{\mathcal M}$, so the $\Sigma^0_1$ formula $\exists m\, (m \geq n \wedge m \in X)$ holds at every standard $n$. By :ref{#prop-overspill}, it holds at some non-standard $c$: some $m \geq c$ belongs to $X$. Such an $m$ is non-standard, since the standard elements form an initial segment, a contradiction. So $X$ is finite, hence bounded by a standard element, and $\mathcal M$-finite since it belongs to $\mathcal S$.

In an ω-model, every element is standard, and $X = \nat$ belongs to $\mathcal S$ without being finite.
:::
::::

## Notes and references

Non-standard models of first-order arithmetic and of its fragments are the subject of the track on models of arithmetic (:ref{to="fragments-of-arithmetic/pa-minus"}).

The categoricity of the second-order Peano axioms is due to Dedekind (1888); :ref{#prop-full-standard} is Dzhafarov–Mummert, Theorem 5.12.2, and their Section 5.12 discusses full semantics. Overspill and underspill are classical in the model theory of arithmetic; Dzhafarov–Mummert, Proposition 6.2.2, state them for arbitrary cuts, and Kaye's book treats them in detail. Finite sets in $\mathsf{RCA}_0$ are coded in Simpson, Section II.2, and the distinction between finite and bounded sets is discussed in Dzhafarov–Mummert, Sections 5.5.2 and 6.2, and Hirschfeldt, Section 4.2. Hirst's theorem is from his thesis (1987) and is Dzhafarov–Mummert, Theorem 6.5.1; the first-order part of $\mathsf{RCA}_0$ is Simpson, Corollary IX.1.11.

- R. Dedekind, *Was sind und was sollen die Zahlen?*, Vieweg, 1888.
- J. L. Hirst, *Combinatorics in Subsystems of Second Order Arithmetic*, Ph.D. thesis, The Pennsylvania State University, 1987.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections II.2 and IX.1.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 4.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.5, 5.12, 6.2 and 6.5.
