---
title: Learning from text
summary: Learning from positive information only; positive infinitary formulas; a family is learnable from text if and only if each member is singled out by a positive infinitary Σ₂ sentence (Bazhenov, Fokina, Rossegger, Soskova, Vatev); the equivalence structures with one or two infinite classes are learnable from informant but not from text; complete classes and continuous embeddings.
duration: 35
prerequisites: [learning-from-informant]
---

An informant gives both what is true and what is false. In classical learning theory, Gold distinguished this from learning from **text**, where only positive examples are given: a language is presented by its words, never by its non-words. For structures, a text lists the atomic facts that hold and never the ones that fail. The learner must then cope with missing information. That $a$ and $b$ are in different classes of an equivalence relation, for example, is never stated. This lesson proves the characterization of learnability from text by Bazhenov, Fokina, Rossegger, Soskova and Vatev. It has the same shape as the characterization for informant, with positive formulas, and it separates the two notions on a pair of equivalence structures.

## Texts and positive formulas

The vocabulary contains both $=$ and $\neq$ as relation symbols, so that "$a$ and $b$ are distinct" is a positive fact. For a structure $\mathcal S$ with domain $\nat$, its **positive diagram** $D^+(\mathcal S)$ is the set of atomic sentences, with constants from $\nat$, true in $\mathcal S$.

:::definition[Bazhenov, Fokina, Rossegger, Soskova, Vatev]{#def-txtex}
A **text** for $\mathcal S$ is a sequence of atomic sentences whose set of terms is $D^+(\mathcal S)$. A family $\mathcal K = \{ \mathcal B_i : i \in \nat \}$ of pairwise non-isomorphic structures is **TxtEx-learnable** if some learner $M$ satisfies: for every $i$, every copy $\mathcal S$ of $\mathcal B_i$ with domain $\nat$ and every text $T$ for $\mathcal S$, the sequence $M(T \uh n)$ is eventually equal to $i$.
:::

Removing the negated facts from an informant leaves a text. So a learner from text, applied to the positive part of an informant, is a learner from informant: TxtEx-learnable families are InfEx-learnable (:ref{#ex-text-implies-informant}).

The formulas that match texts are those that a text can confirm or refute.

:::definition{#def-positive-formulas}
The **positive infinitary formulas** of low complexity are defined as follows.
- A $\Sigma^p_0$ formula is a finite conjunction of atomic formulas; a $\Pi^p_0$ formula is a finite disjunction of negated atomic formulas.
- A $\Sigma^p_1$ formula is a countable disjunction of formulas $\exists \bar x\, \alpha$ with $\alpha$ in $\Sigma^p_0$; a $\Pi^p_1$ formula is a countable conjunction of formulas $\forall \bar y\, \beta$ with $\beta$ in $\Pi^p_0$.
- A $\Sigma^p_2$ formula is a countable disjunction of formulas $\exists \bar x\, (\xi \wedge \psi)$ with $\xi$ in $\Sigma^p_1$ (or $\Sigma^p_0$) and $\psi$ in $\Pi^p_1$ (or $\Pi^p_0$).
:::

A $\Pi^p_0$ formula $\neg \alpha_1 \vee \cdots \vee \neg \alpha_r$ is the negation of the $\Sigma^p_0$ formula $\alpha_1 \wedge \cdots \wedge \alpha_r$. Moving the disjunction and the existential quantifiers of $\xi$ to the front, every $\Sigma^p_2$ sentence is equivalent to a sentence in the **normal form**
$$
\bigvee_{k} \exists \bar x \Big( \alpha_k(\bar x) \wedge \bigwedge_{l} \forall \bar y\ \neg \beta_{k, l}(\bar x, \bar y) \Big),
$$
with each $\alpha_k$ and $\beta_{k, l}$ a finite conjunction of atomic formulas. A text confirms $\alpha_k(\bar a)$ when all its atoms have appeared, and refutes the disjunct for $\bar a$ when all the atoms of some $\beta_{k, l}(\bar a, \bar c)$ have appeared.

## The characterization

:::theorem[Bazhenov, Fokina, Rossegger, Soskova, Vatev]{#thm-txtex-characterization}
Let $\mathcal K = \{ \mathcal B_i : i \in \nat \}$ be a family of pairwise non-isomorphic infinite structures. Then $\mathcal K$ is TxtEx-learnable if and only if there are $\Sigma^p_2$ sentences $\psi_i$ such that, for all $i$ and $j$,
$$
\mathcal B_j \models \psi_i \iff i = j.
$$
:::

:::proof{of=thm-txtex-characterization}
($\Leftarrow$) Write each $\psi_i$ in normal form, with disjuncts indexed by $k$, conjunctions $\alpha_{i, k}$ and $\beta_{i, k, l}$, and $\bar x$ of length $n_{i, k}$. A candidate is a triple $(i, k, \bar a)$ with $\bar a$ a tuple of $n_{i, k}$ numbers. A finite sequence $\rho$ of atomic sentences **confirms** it if every atom of $\alpha_{i, k}(\bar a)$ occurs in $\rho$, and **refutes** it if, for some $l$ and some tuple $\bar c$, every atom of $\beta_{i, k, l}(\bar a, \bar c)$ occurs in $\rho$. Fix an ordering of the candidates of type $\omega$. Let $M(\rho)$ be the first coordinate of the least candidate confirmed and not refuted by $\rho$, and $0$ if there is none.

Let $T$ be a text for a copy $\mathcal S$ of $\mathcal B_j$. Since $\mathcal S \models \psi_j$, some candidate $t_0 = (j, k_0, \bar a_0)$ satisfies $\alpha_{j, k_0}(\bar a_0)$ and $\neg \beta_{j, k_0, l}(\bar a_0, \bar c)$ for all $l$ and $\bar c$. It is confirmed by a long enough initial segment of $T$, and never refuted: a text contains only true atoms. Let $t = (i, k, \bar a)$ with $i \neq j$ precede $t_0$. If $\alpha_{i, k}(\bar a)$ is false in $\mathcal S$, some atom of it is false and never appears, so $t$ is never confirmed. If it is true, then, since $\mathcal S \not\models \psi_i$, some $\beta_{i, k, l}(\bar a, \bar c)$ is true in $\mathcal S$. All its atoms appear in $T$, and from then on $t$ is refuted. So from some point on, every candidate preceding $t_0$ that is confirmed and not refuted has first coordinate $j$, and $M(T \uh n) = j$.

($\Rightarrow$) Let $M$ learn $\mathcal K$ from text, and fix $i$. Define realizations and locking sequences as for informant (:ref{#def-locking}), with finite sequences of atomic sentences in place of facts. The proof of :ref{#lem-locking} applies verbatim, with texts in place of informants: the completion step appends the true atomic sentences about the numbers already used. So $\mathcal B_i$ has a locking sequence $\sigma$, with realization $\nu$. Every extension of $\sigma$ realized over $\nu$ is again locking, so we may assume that $\sigma$ contains the sentence $m \neq m'$ for any two distinct numbers $m, m'$ it mentions.

Use variables $\bar x$ for the numbers of $\sigma$ and, for $\tau \succeq \sigma$, variables $\bar y$ for the new numbers of $\tau$. Let $\theta^+_\tau(\bar x, \bar y)$ be the conjunction of the atoms of $\tau$ with numbers replaced by their variables, and let $\delta(\bar x, \bar y)$ be the disjunction of the formulas $\neg (u \neq v)$ for distinct variables $u, v$. Let
$$
\psi_i \equiv \exists \bar x \Big( \theta^+_\sigma(\bar x) \wedge \bigwedge_{\tau \succeq \sigma,\ M(\tau) \neq i} \forall \bar y\ \big( \neg \theta^+_\tau(\bar x, \bar y) \vee \delta(\bar x, \bar y) \big) \Big).
$$
The formula $\neg \theta^+_\tau \vee \delta$ is a finite disjunction of negated atomic formulas, so $\psi_i$ is $\Sigma^p_2$. It says: there are elements satisfying the atoms of $\sigma$ such that no extension of $\sigma$ on which $M$ changes its mind is realized by distinct elements extending them.

*$\mathcal B_i \models \psi_i$*, with $\bar x$ interpreted by $\nu$. If distinct elements $\bar b$ satisfied $\theta^+_\tau(\nu(\bar m), \bar b)$ for some $\tau \succeq \sigma$ with $M(\tau) \neq i$, then $\tau$ would be realized over $\nu$, and the locking property would give $M(\tau) = i$.

*$\mathcal B_j \not\models \psi_i$ for $j \neq i$.* Suppose that $\bar a$ witnesses $\psi_i$ in $\mathcal B_j$. The elements of $\bar a$ are distinct, since $\theta^+_\sigma$ contains the atoms $x \neq x'$. Take a copy $\mathcal S$ of $\mathcal B_j$ with domain $\nat$ in which the numbers of $\sigma$ name the elements of $\bar a$, and a text for $\mathcal S$ beginning with $\sigma$. Every initial segment $\tau \succeq \sigma$ of this text consists of true atoms about distinct elements $\bar a \bar b$. So $\theta^+_\tau(\bar a, \bar b)$ holds and $\delta(\bar a, \bar b)$ fails, and by the choice of $\bar a$, $M(\tau) = i$. So $M$ fails on a copy of $\mathcal B_j$.
:::

:::quiz[learning from text]
In the proof of ($\Rightarrow$), why does $\psi_i$ contain the disjunction $\delta$ of formulas $\neg (u \neq v)$?

- [x] The atoms of $\tau$ may be satisfied by a non-injective assignment, which is not a realization. The disjunct $\delta$ restricts the universal statement to distinct elements, as the locking property requires. The formula stays positive because $\neq$ is a symbol of the vocabulary.
- [ ] To make $\psi_i$ false in $\mathcal B_j$.

  Falsity in $\mathcal B_j$ comes from a text of a copy of $\mathcal B_j$; the disjunct $\delta$ is needed for truth in $\mathcal B_i$.
- [ ] Because texts may repeat atoms.

  Repetitions do not matter; the issue is that atoms alone do not say that distinct numbers name distinct elements.

---

In ($\Leftarrow$), why does the learner from text need the confirmation step, absent from the learner from informant?

- [x] From a text, the learner cannot see that an atom is false; it must wait until the positive part $\alpha_{i, k}(\bar a)$ of a candidate has appeared, while a candidate whose positive part is false is simply never confirmed.
- [ ] Because texts are not computable.

  The learner need not be computable; confirmation is needed for correctness.
- [ ] To make the learner converge faster.

  Without confirmation, a candidate with a false positive part, preceding the correct one, would never be eliminated, and the learner would converge to a wrong index.
:::

## Separating the two notions

Positive information cannot show that two elements are in different classes of an equivalence relation. This is the reason for the following separation, first proved by Fokina, Kötzing and San Mauro. The proof below uses :ref{#thm-txtex-characterization}. Write $[\omega : 1]$ for the equivalence structure with one infinite class, and $[\omega : 2]$ for the one with two infinite classes, in the vocabulary $\{ E, =, \neq \}$.

:::proposition[Fokina, Kötzing, San Mauro]{#prop-text-informant-separation}
The family $\{ [\omega : 1], [\omega : 2] \}$ is InfEx-learnable but not TxtEx-learnable.
:::

:::proof{of=prop-text-informant-separation}
The finitary sentences $\forall x\, \forall y\, E(x, y)$ and $\exists x\, \exists y\, \neg E(x, y)$ are $\Sigma^{\mathrm{inf}}_2$ and separate the two structures in both directions, so the family is InfEx-learnable (:ref{#thm-infex-characterization}).

We show that every $\Sigma^p_2$ sentence $\psi$ true in $\mathcal A = [\omega : 1]$ is true in $[\omega : 2]$, so that no $\psi_0$ as in :ref{#thm-txtex-characterization} exists. Write $\psi$ in normal form, and let a disjunct and a tuple $\bar a$ witness it in $\mathcal A$, taken with domain $\nat$. Let $\mathcal B$ be the structure with the same domain, with two infinite classes, the elements of $\bar a$ all in the same class. Every atom true in $\mathcal B$ is true in $\mathcal A$: $E$ holds everywhere in $\mathcal A$, and $=$ and $\neq$ are the same in both. The atoms of $\alpha(\bar a)$ are true in $\mathcal B$, since they are equalities, inequalities, or instances of $E$ between elements of $\bar a$, which are in one class. If some $\beta_l(\bar a, \bar c)$ were true in $\mathcal B$, all its atoms would be true in $\mathcal A$, contradicting the choice of $\bar a$. So the disjunct holds in $\mathcal B$, and $\mathcal B \cong [\omega : 2]$ satisfies $\psi$.
:::

The argument shows a general principle: if $\mathcal B$ has a copy whose positive diagram is contained in that of a copy of $\mathcal A$, in a way that keeps any finite configuration of $\mathcal A$, then $\mathcal A$ cannot be singled out from $\mathcal B$ by a $\Sigma^p_2$ sentence. Monotonicity is the essential feature of positive information.

::::exercise{#ex-text-finite-classes difficulty=1 objective="Find positive Σ₂ sentences that separate two equivalence structures."}
Let $[1 : \omega]$ be the equivalence structure with infinitely many classes of size $1$, and $[2 : \omega]$ the one with infinitely many classes of size $2$, in the vocabulary $\{ E, =, \neq \}$. Show that the family $\{ [1 : \omega], [2 : \omega] \}$ is TxtEx-learnable.

:::solution
The sentence $\forall y\, \forall z\, \big( \neg E(y, z) \vee \neg (y \neq z) \big)$ is $\Pi^p_1$, hence $\Sigma^p_2$; it says that equivalent elements are equal, which holds in $[1 : \omega]$ and fails in $[2 : \omega]$. The sentence $\exists x\, \exists y\, \big( E(x, y) \wedge x \neq y \big)$ is $\Sigma^p_1$, hence $\Sigma^p_2$; it holds in $[2 : \omega]$ and fails in $[1 : \omega]$. By :ref{#thm-txtex-characterization}, the family is TxtEx-learnable.
:::
::::

## Complete classes and continuity

Both characterizations have a topological form. A learner turns a copy into a sequence of guesses. Bazhenov, Fokina and San Mauro showed that the InfEx-learnable families are those that embed, by a continuous map on atomic diagrams (Cantor space), into one fixed learnable class $\mathcal K_{st}$. This is a class of structures with infinitely many unary predicates $P_k$: in its $i$-th member, the predicate $P_i$ carries the order $1 + \eta$ and the others carry $\eta$. For text, Bazhenov, Fokina, Rossegger, Soskova and Vatev proved that the TxtEx-learnable families are those that embed into the class of equivalence structures $[\omega : \omega, i + 1 : \omega]$, by a map continuous in the Scott topology on positive diagrams. These maps are the generalized enumeration operators of the course on enumeration degrees. The class $\mathcal K_{st}$ is also complete for TxtEx-learnability. As noted in the previous lesson, InfEx-learnability is equivalent to a continuous reduction of isomorphism to $E_0$. The corresponding characterization of TxtEx-learnability by Scott-continuous reductions was asked by the same authors in 2024.

## Notes and references

:ref{#thm-txtex-characterization} is Theorem 3 of Bazhenov, Fokina, Rossegger, Soskova and Vatev (2024). Their proof of ($\Leftarrow$) is the learner given here; their proof of ($\Rightarrow$) goes through a Scott-continuous embedding into the class of equivalence structures above and a pull-back theorem for positive formulas. The direct proof with locking sequences given here is written for this course, along the lines of their Proposition 3. :ref{#prop-text-informant-separation} is Theorem 1.4 of Fokina, Kötzing and San Mauro; the proof via positive sentences is written for this course, while the 2024 paper gives a proof by monotonicity of Scott-continuous maps. Positive infinitary formulas were introduced by the same group in their work on a Lopez-Escobar theorem for continuous domains (2023).

- N. Bazhenov, E. Fokina, D. Rossegger, A. Soskova and S. Vatev, *Learning families of algebraic structures from text*, arXiv:2402.05744, 2024.
- N. Bazhenov, E. Fokina, D. Rossegger, A. Soskova and S. Vatev, *A Lopez-Escobar theorem for continuous domains*, arXiv:2301.09940, 2023.
- E. Fokina, T. Kötzing and L. San Mauro, *Limit learning equivalence structures*, Proceedings of ALT 2019, PMLR 98 (2019), 383–403.
- N. Bazhenov and L. San Mauro, *On the Turing complexity of learning finite families of algebraic structures*, Journal of Logic and Computation 31 (2021), 1891–1900.

:::::exercises
::::exercise{#ex-text-implies-informant difficulty=1 objective="Turn a learner from text into a learner from informant."}
Show that every TxtEx-learnable family is InfEx-learnable, directly from the definitions.

:::solution
Let $M$ learn $\mathcal K$ from text. For a finite sequence $\rho$ of facts, let $\rho^+$ be the subsequence of its atomic sentences, and let $M'(\rho) = M(\rho^+)$. If $I$ is an informant for a copy $\mathcal S$, the subsequence $I^+$ of its atomic sentences lists exactly $D^+(\mathcal S)$, so it is a text for $\mathcal S$; the initial segments of $I^+$ are the sequences $(I \uh n)^+$. If $I^+$ is infinite, $M(I^+ \uh m)$ converges to the correct index, and so does $M'(I \uh n) = M((I \uh n)^+)$. The positive diagram of an infinite structure is infinite (it contains $m = m$ for every $m$), so $I^+$ is infinite.
:::
::::

::::exercise{#ex-text-linear-orders difficulty=2 objective="See that for linear orders, with the order and inequality as symbols, positive information determines the diagram."}
Consider linear orders in the vocabulary $\{ <, =, \neq \}$. Show that a family of linear orders is TxtEx-learnable if and only if it is InfEx-learnable.

:::solution
One direction is :ref{#ex-text-implies-informant}. For the other, let $M$ learn the family from informant. From a finite sequence $\rho$ of atomic sentences, compute a finite sequence of facts $f(\rho)$: list the sentences of $\rho$, and, for each atomic sentence $\varphi$ about numbers mentioned in $\rho$ whose negation is implied by an atom of $\rho$, add $\neg \varphi$. Precisely, $a < b$ implies $\neg (b < a)$, $\neg (a = b)$ and $\neg (b = a)$; $a = b$ implies $\neg (a \neq b)$ and $\neg (a < b)$; $a \neq b$ implies $\neg (a = b)$; we also add $\neg (a < a)$ and $\neg(a \neq a)$ for each number $a$. The map $f$ is monotone, so for a text $T$ the sequences $f(T \uh n)$ are initial segments of a single sequence $f(T)$. Every fact of $f(T)$ is true. In a linear order, for distinct $a$ and $b$, exactly one of $a < b$ and $b < a$ holds, and $a \neq b$ holds; so every false atomic sentence about $a, b$ is refuted by an atom that eventually appears in $T$. Hence $f(T)$ is an informant for the same copy. Let $M'(\rho) = M(f(\rho))$. On a text $T$ for a copy of $\mathcal B_i$, the sequences $f(T \uh n)$ are initial segments of $f(T)$ of non-decreasing and unbounded lengths, so $M'(T \uh n) = M(f(T \uh n))$ converges to the limit of $M$ along the informant $f(T)$, which is $i$.
:::
::::
:::::
