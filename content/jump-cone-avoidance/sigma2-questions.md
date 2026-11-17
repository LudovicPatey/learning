---
title: Forcing questions for Σ⁰₂ sentences
summary: A Π⁰₂ sentence is forced by density, not on all members; a forcing question at level 1 lifts to level 2 by quantifying over extensions, at a cost measured by the complexity of the partial order; questions with answers Σ⁰₁ relative to the condition give jump cone avoidance.
duration: 30
prerequisites: [jump-cones, effective-forcing/forcing-question, effective-forcing/forcing-with-trees, avoidance/forcing-question-method]
---

At level $1$, a condition forces a sentence when all its members satisfy it, and a forcing question decides which of $\varphi$ and $\neg\varphi$ can be reached in this strong sense below a condition. At level $2$ this is no longer possible for most notions of forcing: no Cohen condition makes all its members infinite, or all of them finite. The forcing relation of :ref{#def-forcing-relation} handles $\Pi^0_2$ sentences by a **density** clause, and a forcing question for $\Sigma^0_2$ sentences has to quantify over the extensions of a condition. This lesson makes the passage from level $1$ to level $2$ explicit, shows that the cost lies in the complexity of the partial order, and proves the abstract jump cone avoidance theorem, in the local form needed for the applications. The examples are Cohen forcing, computable Mathias forcing and Jockusch–Soare forcing; the next lesson applies the theorem to the last one.

## Forcing Π⁰₂ sentences by density

Recall from :ref{#def-forcing-formula} that a $\Sigma^0_2$ sentence has the form $\exists y\ \psi(y)$ with $\psi$ a $\Pi^0_1$ formula, and from :ref{#def-forcing-relation} that $c \Vdash \forall y\ \theta(y)$, for $\theta$ a $\Sigma^0_1$ formula, means that no $d \leq c$ forces $\neg\theta(m)$ for any $m$. When the forcing question at level $1$ satisfies its two properties, this is a density statement: for every $m$, the conditions forcing $\theta(m)$ are dense below $c$. Indeed, for $d \leq c$, no extension of $d$ forces $\neg\theta(m)$, so $d \mathrel{?{\vdash}} \theta(m)$ by property 2 of :ref{#def-forcing-question}, and property 1 gives an extension of $d$ forcing $\theta(m)$. A sufficiently generic filter through $c$ meets all these dense sets (:ref{#lem-dense-below}), and its generic set satisfies $\theta(m)$ for every $m$, which is :ref{#thm-forcing-truth} in this case.

The members of $c$ play no role: in Cohen forcing, every string forces "$G$ is infinite" although it has finite members (:ref{#ex-forcing-relation}). Information about $\Pi^0_2$ sentences is information about the future of the construction, and a condition carries it only through the set of its extensions. This is why the complexity of the partial order enters the complexity of the forcing at level $2$.

## Lifting a forcing question

:::definition{#def-lifted-question}
Let $\mathbb P$ be a notion of forcing with a forcing question for $\Sigma^0_1$ sentences. For a condition $c$ and a $\Sigma^0_2$ sentence $\varphi = \exists y\ \psi(y)$, with $\psi$ a $\Pi^0_1$ formula, the **lifted question** is defined by
$$
c \mathrel{?{\vdash}} \varphi \quad\text{if there are } d \leq c \text{ and } m \text{ with } d \mathrel{?{\nvdash}} \neg\psi(m).
$$
:::

Since $\neg\psi(m)$ is a $\Sigma^0_1$ sentence, $d \mathrel{?{\nvdash}} \neg\psi(m)$ says that, below $d$, the $\Pi^0_1$ sentence $\psi(m)$ can be forced. The lifted question asks whether some extension of $c$ is such a $d$.

:::lemma{#lem-lifted-question}
The lifted question satisfies the two properties of :ref{#def-forcing-question} for $\Sigma^0_2$ sentences:

1. if $c \mathrel{?{\vdash}} \exists y\ \psi(y)$, some extension of $c$ forces $\psi(m)$ for some $m$, hence forces $\exists y\ \psi(y)$, and all its members satisfy it;
2. if $c \mathrel{?{\nvdash}} \exists y\ \psi(y)$, then $c \Vdash \forall y\ \neg\psi(y)$.
:::

:::proof{of=lem-lifted-question}
1. Let $d \leq c$ and $m$ with $d \mathrel{?{\nvdash}} \neg\psi(m)$. By property 2 at level $1$, some $e \leq d$ forces $\psi(m)$: every member of $e$ satisfies $\psi(m)$. By the existential clause of :ref{#def-forcing-relation}, $e \Vdash \exists y\ \psi(y)$.
2. Suppose some $d \leq c$ forces $\psi(m)$ for some $m$. Since the lifted question fails at $c$, $d \mathrel{?{\vdash}} \neg\psi(m)$, and property 1 at level $1$ gives $e \leq d$ forcing $\neg\psi(m)$. By extension (:ref{#prop-forcing-basic}), $e$ also forces $\psi(m)$, which contradicts consistency. So no extension of $c$ forces any $\psi(m)$, which is the definition of $c \Vdash \forall y\ \neg\psi(y)$.
:::

The proof is the induction step of :ref{#thm-tree-question}, at level $1$; it uses only the two properties at level $1$. What changes from one notion of forcing to another is the complexity of the lifted question: it is
$$
\exists d\ \exists m\ \big[\, d \text{ is a condition} \wedge d \leq c \wedge d \mathrel{?{\nvdash}} \neg\psi(m) \,\big].
$$
If the question at level $1$ is $\Sigma^0_1$ uniformly in a code of the condition, as for the three examples below, the last conjunct is $\Pi^0_1$. The lifted question is then $\Sigma^0_2$ as soon as the conditions can be listed by codes such that being a condition and extension are $\Pi^0_1$, or computable relative to a fixed oracle that is absorbed. The three examples of the course behave differently.

:::example{#ex-lifted-questions}
1. **Cohen forcing.** Strings and their order are computable, so $\sigma \mathrel{?{\vdash}} \exists y\ \psi(y)$ if and only if there are $\tau \succeq \sigma$ and $m$ such that no $\rho \succeq \tau$ satisfies $\neg\psi(m)$: a $\Sigma^0_2$ relation. This is the $\Sigma^0_2$-preserving question of :ref{#ex-cohen-question}.
2. **Computable Mathias forcing.** An extension $(\tau, Y)$ of $(\sigma, X)$ is given by a string and an index of $Y$, and "the index defines an infinite subset of $X$" is $\Pi^0_2$. The lifted question is $\Sigma^0_3$, and by :ref{#cor-mathias-no-sigma2} no forcing question at level $2$ can be $\Sigma^0_2$-preserving.
3. **Jockusch–Soare forcing.** With conditions given by indices of $\Pi^0_1$ classes, being a condition is $\Pi^0_1$ but extension is $\Pi^0_2$ (:ref{#prop-js-complexity}), and the lifted question is $\Sigma^0_3$ as written. The question of :ref{#prop-tree-sigma2} avoids the quantification over extensions by deciding $\Sigma^0_2$ sentences on all members, and is $\Sigma^0_2$. An exercise of :ref{to="jump-cone-avoidance/wkl-two-cones"} gives another solution: restricting the conditions so that the extension relation becomes $\Pi^0_1$.
:::

In the second and third examples, the obstacle is not in the forcing question at level $1$, which is $\Sigma^0_1$-preserving, but in the partial order. A notion of forcing designed for second-jump control has a partial order as simple as the constructions allow; this principle guides the next lessons.

:::figure[The two answers of the lifted question at a condition $c$, for $\varphi = \exists y\ \psi(y)$ with $\psi$ a $\Pi^0_1$ formula. Left: some extension $d$ and some $m$ with a negative answer about $\neg\psi(m)$, which gives an extension $e$ all of whose members satisfy $\psi(m)$. Right: every extension $d$ answers positively about every $\neg\psi(m)$; for each $m$, the conditions forcing $\neg\psi(m)$ are dense below $c$, and the generic set satisfies $\forall y\ \neg\psi(y)$ although $c$ may have members that do not.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The two answers of the lifted question at a condition c: either some extension d and some m answer negatively about not psi(m), and an extension e forces psi(m) on all members; or every extension answers positively about every not psi(m), the conditions forcing not psi(m) are dense below c, and the generic set satisfies for all y not psi(y)"><defs><marker id="jc-lq-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="220" y="10" width="160" height="40" rx="6" class="state"/><text x="300.0" y="26.0" text-anchor="middle" class="label">condition c</text><text x="300.0" y="42.0" text-anchor="middle" class="label">φ = ∃y ψ(y), ψ ∈ Π⁰₁</text><rect x="20" y="100" width="240" height="40" rx="6" class="node"/><text x="140.0" y="116.0" text-anchor="middle" class="label">some d ≤ c and m with</text><text x="140.0" y="132.0" text-anchor="middle" class="label">d ?⊬ ¬ψ(m)</text><rect x="20" y="190" width="240" height="40" rx="6" class="state"/><text x="140.0" y="206.0" text-anchor="middle" class="label">e ≤ d: every member</text><text x="140.0" y="222.0" text-anchor="middle" class="label">of e satisfies ψ(m), hence φ</text><rect x="340" y="100" width="240" height="40" rx="6" class="node"/><text x="460.0" y="116.0" text-anchor="middle" class="label">every d ≤ c and every m:</text><text x="460.0" y="132.0" text-anchor="middle" class="label">d ?⊢ ¬ψ(m)</text><rect x="340" y="190" width="240" height="40" rx="6" class="state"/><text x="460.0" y="206.0" text-anchor="middle" class="label">for each m, forcing ¬ψ(m) is dense</text><text x="460.0" y="222.0" text-anchor="middle" class="label">below c: generic G satisfies ¬φ</text><line x1="270" y1="52" x2="160" y2="96" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-lq-arr)"/><line x1="330" y1="52" x2="440" y2="96" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-lq-arr)"/><line x1="140" y1="142" x2="140" y2="186" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-lq-arr)"/><line x1="460" y1="142" x2="460" y2="186" class="ink-stroke" stroke-width="1.2" marker-end="url(#jc-lq-arr)"/><text x="150" y="80" text-anchor="end" class="label">c ?⊢ φ</text><text x="450" y="80" class="label">c ?⊬ φ</text></svg>
:::

:::quiz[the lifted question]
In property 2 of :ref{#lem-lifted-question}, where is consistency of the forcing relation used?

- [x] To exclude an extension $d$ forcing $\psi(m)$: the positive answer at $d$ would produce $e \leq d$ forcing $\neg\psi(m)$, and $e$ would force both $\psi(m)$ and its negation.
- [ ] To show that $c$ itself forces $\neg\psi(m)$ for every $m$.

  This is not claimed and is false in general: $c$ forces the universal sentence by density, not each instance on all members.
- [ ] To show that the lifted question is $\Sigma^0_2$.

  Consistency is a property of the forcing relation, unrelated to definability.

---

Why is the lifted question of computable Mathias forcing $\Sigma^0_3$ rather than $\Sigma^0_2$?

- [x] Because the quantifier over extensions ranges over indices of infinite computable subsets of the reservoir, and recognizing such an index is a $\Pi^0_2$ property.
- [ ] Because its question at level $1$ is not $\Sigma^0_1$-preserving.

  It is, by :ref{#prop-mathias-question}.
- [ ] Because Mathias conditions are not closed classes.

  Their classes of members are closed; the problem is the complexity of the partial order.
:::

## Jump cone avoidance from a forcing question

As at level $1$ (:ref{#def-question-local}), the applications need questions whose answers are simple relative to a set depending on the condition.

:::definition{#def-jump-question-local}
Let $\mathcal M$ be a class of sets. A forcing question for $\Sigma^0_2$ sentences is **$\Sigma^0_1(\mathcal M)$-preserving** if for every condition $c$ there is $X \in \mathcal M$ such that, for every $\Sigma^0_2$ formula $\varphi(\vec x)$, the relation $\{ \vec m : c \mathrel{?{\vdash}} \varphi(\vec m) \}$ is $\Sigma^0_1(X)$.
:::

For $\mathcal M = \{ \emptyset' \}$, this is $\Sigma^0_2$-preservation, by Post's theorem. By Post's theorem relativized, there is a computable function $h$ such that, for all $e$, $x$, $v$ and every set $G$, the sentence "$\Phi^{G'}_e(x)\converge = v$" holds if and only if the $\Sigma^0_2$ sentence $\exists y\ \Phi^G_{h(e, x, v)}(y)\diverge$ holds. We use this translation without further mention.

:::theorem{#thm-local-jump-cone}
Let $\mathbb P$ be a notion of forcing with a forcing question for $\Sigma^0_2$ sentences that is $\Sigma^0_1(\mathcal M)$-preserving. Let $C$ be a set computable in no member of $\mathcal M$. For every sufficiently generic set $G$, $C \not\leq_T G'$.
:::

:::proof{of=thm-local-jump-cone}
For each $e$, let $E_e$ be the set of conditions $d$ for which there is $x$ such that $d \Vdash \Phi^{G'}_e(x)\converge = 1 - C(x)$ or $d \Vdash \neg(\Phi^{G'}_e(x)\converge = C(x))$. We show that $E_e$ is dense. Let $c$ be a condition and $X \in \mathcal M$ as in :ref{#def-jump-question-local}. The set
$$
U = \{ (x, v) \in \nat \times \{0, 1\} : c \mathrel{?{\vdash}} \Phi^{G'}_e(x)\converge = v \}
$$
is $\Sigma^0_1(X)$.

1. If $(x, 1 - C(x)) \in U$ for some $x$, property 1 gives an extension of $c$ forcing $\Phi^{G'}_e(x)\converge = 1 - C(x)$.
2. If $(x, C(x)) \notin U$ for some $x$, property 2 gives an extension forcing the negation of $\Phi^{G'}_e(x)\converge = C(x)$, a $\Pi^0_2$ sentence.
3. Otherwise $U$ is the graph of $C$, and $C \leq_T X$, which is excluded.

Let $F$ be a $2$-generic filter (:ref{#def-n-generic-notion}) meeting every $E_e$. For each $e$, $F$ contains a condition of $E_e$, and by :ref{#thm-forcing-truth} the sentence it forces holds for $G_F$. So $\Phi^{G_F'}_e \neq C$ for every $e$.
:::

The proof is the three-case argument of :ref{#thm-local-cone-avoidance}, with $G'$ in place of $G$. The only new point is that the second case gives a $\Pi^0_2$ sentence, which holds for the generic set by density and genericity, not for all members of the condition. For $\mathcal M = \{ \emptyset' \}$, the theorem is :ref{#cor-question-jump-cone} with $n = 1$, restricted to the cone above $C$.

:::quiz[the abstract theorem]
In case 3 of the proof of :ref{#thm-local-jump-cone}, why is it enough that $U$ is $\Sigma^0_1(X)$, although the sentences involved are $\Sigma^0_2$?

- [x] Because the definability of the question is measured relative to $X \in \mathcal M$, and the hypothesis on $C$ is that $C$ is not computable in any member of $\mathcal M$; a $\Sigma^0_1(X)$ graph of a function makes it $X$-computable.
- [ ] Because $\Sigma^0_2$ sentences about $G'$ are $\Sigma^0_1$ about $G$.

  They are $\Sigma^0_2$ about $G$; the reduction of complexity concerns the question, not the sentences.
- [ ] Because $C$ is $\Delta^0_2$.

  $C$ is arbitrary, subject only to the hypothesis.

---

Why does the conclusion of case 2 not hold for every member of the extension?

- [x] Because the extension forces a $\Pi^0_2$ sentence, which is forced by density; it holds for generic sets through the extension, but may fail for some members.
- [ ] Because property 2 of a forcing question only gives the extension, not a sentence it forces.

  It gives an extension forcing the negation.
- [ ] Because $C$ is not computable in $X$.

  This hypothesis is used in case 3.
:::

## Exercises

::::exercise{#ex-cohen-jump-hyperimmunity difficulty=2 objective="Combine the lifted question of Cohen forcing with a compactness property to preserve a function hyperimmune relative to $\emptyset'$."}
Let $f$ be hyperimmune relative to $\emptyset'$. Using the lifted question of Cohen forcing, show that $f$ is hyperimmune relative to $G'$ for every sufficiently Cohen generic set $G$.

:::solution
Fix $e$. By Post's theorem relativized, there are $\Pi^0_1$ formulas $\psi_m(k, y)$, with indices computable from $m$, such that $\Phi^{G'}_e(m)\converge = k$ if and only if $\exists y\ \psi_m(k, y)$. Write "$\Phi^{G'}_e(m)\converge$" as the $\Sigma^0_2$ sentence $\exists \langle k, y \rangle\ \psi_m(k, y)$, and, for a bound $b$, "$\Phi^{G'}_e(m)\converge < b$" as $\exists \langle k, y \rangle\ \psi^b_m(k, y)$, where $\psi^b_m(k, y)$ behaves as $\psi_m(k, y)$ if $k < b$ and is false otherwise. The lifted question of Cohen forcing depends only on the strings satisfying the formulas involved, so it is **compact**: if $\sigma \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge$, witnessed by $\tau \succeq \sigma$ and $\langle k, y \rangle$, the same witnesses give $\sigma \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < k + 1$.

Let $E_e$ be the set of strings forcing $\Phi^{G'}_e(m)\diverge$ for some $m$, or forcing $\Phi^{G'}_e(m)\converge < b$ for some $m$ and some $b \leq f(m)$. Given $\sigma$, let $g(m)$ be the first $b$ found with $\sigma \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < b$; this partial function is $\emptyset'$-computable, since the question is $\Sigma^0_2$. If $g(m)$ is undefined, then $\sigma \mathrel{?{\nvdash}} \Phi^{G'}_e(m)\converge$ by compactness, and property 2 gives an extension forcing $\Phi^{G'}_e(m)\diverge$. If $g$ is total, it is $\emptyset'$-computable, so $f(m) > g(m)$ for some $m$, and property 1 gives an extension forcing $\Phi^{G'}_e(m)\converge < g(m)$. So $E_e$ is dense. If $G$ comes from a $2$-generic filter meeting every $E_e$, then by :ref{#thm-forcing-truth}, for every $e$, $\Phi^{G'}_e$ is partial or below $f$ at some point, so no $G'$-computable function dominates $f$.
:::
::::

## Notes and references

The discussion of the forcing relation for $\Pi^0_2$ sentences, the forcing question of Cohen forcing at level $2$, the abstract theorem and :ref{#ex-cohen-jump-hyperimmunity} follow the section *Forcing and density* of the chapter *Jump cone avoidance* of Patey's monograph. The lifted question is stated there for each example separately, and is isolated here as :ref{#def-lifted-question}; :ref{#thm-local-jump-cone} is stated here in the local form of :ref{#thm-local-cone-avoidance}, as needed for cohesiveness and for the pigeonhole principle.

- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Forcing and density*.

:::::exercises
::::exercise[Two sentences for Cohen forcing]{#ex-lifted-cohen-examples difficulty=1 objective="Compute the lifted question of Cohen forcing on two $\Sigma^0_2$ sentences, and read off the extensions given by its two properties."}
For Cohen forcing, with the question at level $1$ "$\sigma \mathrel{?{\vdash}} \theta$ if some $\tau \succeq \sigma$ satisfies $\theta$" (:ref{#ex-cohen-question}), compute the lifted question at every string $\sigma$ for the sentences
$$
\begin{gathered}
\varphi_1 = \exists y\ \forall z \geq y\ (z \notin G), \\
\varphi_2 = \exists y\ \big[\, y \geq 1 \wedge \forall z\ (y \leq z < 2y \rightarrow z \notin G) \,\big],
\end{gathered}
$$
"$G$ is finite" and "$G$ misses some interval $[y, 2y)$". Give in each case the extension or the forced sentence provided by :ref{#lem-lifted-question}, and say which sentence holds for every sufficiently generic set.

:::solution
*First sentence.* Here $\psi(m)$ is $\forall z \geq m\ (z \notin G)$ and $\neg\psi(m)$ is $\exists z \geq m\ (z \in G)$. Every string $\tau$ has an extension with a $1$ at a position at least $m$, which satisfies $\neg\psi(m)$; so $\tau \mathrel{?{\vdash}} \neg\psi(m)$ for all $\tau$ and $m$, and the lifted question answers no at every $\sigma$. By property 2, every string forces $\forall y\ \neg\psi(y)$, "$G$ is infinite", as in :ref{#ex-forcing-relation}.

*Second sentence.* Here $\neg\psi(m)$ says $m = 0$ or $G$ has an element in $[m, 2m)$. A string $\tau$ has no extension satisfying it if and only if $m \geq 1$, $|\tau| \geq 2m$ and $\tau(z) = 0$ for $m \leq z < 2m$: if $|\tau| < 2m$, the position $\max(m, |\tau|)$ lies in $[m, 2m)$ and can be set to $1$. Given $\sigma$, take $m = |\sigma| + 1$ and $\tau = \sigma 0^{2m - |\sigma|}$: then $\tau \succeq \sigma$ and $\tau \mathrel{?{\nvdash}} \neg\psi(m)$, so the lifted question answers yes at every $\sigma$. Property 1 gives the extension $\tau$, all of whose members miss $[m, 2m)$.

So every sufficiently generic set is infinite and satisfies $\varphi_2$; it does not satisfy $\varphi_1$.
:::
::::

::::exercise[The lifted question asks for an extension that forces]{#ex-lifted-extension difficulty=2 objective="Characterize the lifted question through the forcing relation, and see that it does not depend on the question chosen at level $1$."}
Let $\mathbb P$ be a notion of forcing with a forcing question for $\Sigma^0_1$ sentences, and $\varphi = \exists y\ \psi(y)$ a $\Sigma^0_2$ sentence. Show that $c \mathrel{?{\vdash}} \varphi$, for the lifted question, if and only if some $d \leq c$ forces $\varphi$ in the sense of :ref{#def-forcing-relation}. Deduce that two forcing questions for $\Sigma^0_1$ sentences have the same lifted question.

:::solution
If $c \mathrel{?{\vdash}} \varphi$, item 1 of :ref{#lem-lifted-question} gives an extension forcing $\varphi$.

Conversely, let $d \leq c$ force $\varphi$. By the existential clause of :ref{#def-forcing-relation}, $d$ forces $\psi(m)$ for some $m$: every member of $d$ satisfies the $\Pi^0_1$ sentence $\psi(m)$. Suppose $d \mathrel{?{\vdash}} \neg\psi(m)$. Property 1 at level $1$ gives $e \leq d$ all of whose members satisfy $\neg\psi(m)$. The members of $e$ are members of $d$ (:ref{#def-forcing-notion}), and $e$ has a member, since its class of members is non-empty; this member satisfies $\psi(m)$ and $\neg\psi(m)$, which is impossible. So $d \mathrel{?{\nvdash}} \neg\psi(m)$, and $d$ and $m$ witness $c \mathrel{?{\vdash}} \varphi$.

The characterization does not mention the question at level $1$, so all forcing questions for $\Sigma^0_1$ sentences have the same lifted question. What the choice at level $1$ changes is the way the lifted question is written, hence the upper bound on its complexity that can be read off. For Jockusch–Soare forcing, an extension of $\mathcal P$ forces $\psi(m)$ if and only if the $\Pi^0_1$ class $\mathcal P \cap \{ X : X \text{ satisfies } \psi(m) \}$ is non-empty, since this class is then such an extension, and every extension forcing $\psi(m)$ is contained in it. So the lifted question, $\Sigma^0_3$ as written in :ref{#ex-lifted-questions}, item 3, holds if and only if some member of $\mathcal P$ satisfies some $\psi(m)$, which is the $\Sigma^0_2$ answer of :ref{#prop-tree-sigma2}.
:::
::::

::::exercise[Preservation of non-Σ⁰₂ definitions]{#ex-non-sigma2-local difficulty=2 objective="Adapt the abstract jump cone avoidance theorem to sets that are not $\Sigma^0_2$, with a two-case argument."}
Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving forcing question for $\Sigma^0_2$ sentences (:ref{#def-jump-question-local}), and let $C$ be a set that is not $\Sigma^0_1(X)$ for any $X \in \mathcal M$. Show that for every sufficiently generic set $G$, $C$ is not $\Sigma^0_2(G)$. What does this give for Cohen forcing?

:::solution
By Post's theorem relativized, the $\Sigma^0_2(G)$ sets are the sets $W^{G'}_e = \{ x : \Phi^{G'}_e(x)\converge \}$, and there are $\Sigma^0_2$ formulas $\varphi_e(x)$, with codes computable from $e$, such that $x \in W^{G'}_e$ if and only if $\varphi_e(x)$ holds of $G$. For each $e$, let $E_e$ be the set of conditions that force $\varphi_e(x)$ for some $x \notin C$, or force $\neg\varphi_e(x)$ for some $x \in C$.

$E_e$ is dense. Let $c$ be a condition and $X \in \mathcal M$ as in :ref{#def-jump-question-local}. The set $U = \{ x : c \mathrel{?{\vdash}} \varphi_e(x) \}$ is $\Sigma^0_1(X)$, so $U \neq C$. If $x \in U \setminus C$, property 1 gives an extension forcing $\varphi_e(x)$. If $x \in C \setminus U$, property 2 gives an extension forcing $\neg\varphi_e(x)$, a $\Pi^0_2$ sentence. There is no third case: the hypothesis on $C$ excludes $U = C$ directly.

A $2$-generic filter meeting every $E_e$ gives, by :ref{#thm-forcing-truth}, a set $G$ with $W^{G'}_e \neq C$ for every $e$. For Cohen forcing and $\mathcal M = \{ \emptyset' \}$ (:ref{#ex-lifted-questions}, item 1): if $C$ is not $\Sigma^0_2$, it is not $\Sigma^0_2(G)$ for any sufficiently generic $G$.
:::
::::

::::exercise[Indices of reservoirs]{#ex-mathias-index-complexity difficulty=1 objective="Show that the quantifier over extensions in the lifted question of computable Mathias forcing ranges over a $\Pi^0_2$-complete set of indices."}
Present a computable Mathias reservoir by an index $e$ such that $\Phi_e$ is the characteristic function of an infinite set. Show that the set $\mathrm{Res}$ of such indices is $\Pi^0_2$ and that every $\Pi^0_2$ set is many-one reducible to it, using that $\mathrm{Inf} = \{ e : W_e \text{ is infinite} \}$ is $\Pi^0_2$-complete.

:::solution
$e \in \mathrm{Res}$ if and only if for every $n$, $\Phi_e(n)$ converges with a value in $\{0, 1\}$, and for every $n$ there is $m > n$ with $\Phi_e(m) = 1$. Both clauses are $\forall\exists$ with a computable matrix, so $\mathrm{Res}$ is $\Pi^0_2$.

Let $g$ be a computable function such that $\Phi_{g(e)}(s) = 1$ if $W_{e, s+1} \neq W_{e, s}$ and $\Phi_{g(e)}(s) = 0$ otherwise. The function $\Phi_{g(e)}$ is total and $\{0, 1\}$-valued for every $e$. If $W_e$ is infinite, new elements appear at infinitely many stages, so $\Phi_{g(e)}$ takes the value $1$ infinitely often; if $W_e$ is finite, only finitely many stages add an element. So $e \in \mathrm{Inf}$ if and only if $g(e) \in \mathrm{Res}$, and every $\Pi^0_2$ set, many-one reducible to $\mathrm{Inf}$, is many-one reducible to $\mathrm{Res}$.

The quantifier over extensions of the lifted question therefore ranges over a set of indices that is not $\Sigma^0_2$; this is the source of the third quantifier in the expression of :ref{#ex-lifted-questions}, item 2. That no other way of writing the question removes it is :ref{#cor-mathias-no-sigma2}.
:::
::::
:::::
