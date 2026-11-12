---
title: Forcing questions for Σ⁰₂ sentences
summary: A Π⁰₂ sentence is forced by density, not on all members; a forcing question at level 1 lifts to level 2 by quantifying over extensions, at a cost measured by the complexity of the partial order; questions with answers Σ⁰₁ relative to the condition give jump cone avoidance; weak König's lemma admits cone avoidance and jump cone avoidance at once (Wang).
duration: 45
prerequisites: [jump-cones, effective-forcing/forcing-question, effective-forcing/forcing-with-trees, avoidance/forcing-question-method]
---

At level $1$, a condition forces a sentence when all its members satisfy it, and a forcing question decides which of $\varphi$ and $\neg\varphi$ can be reached in this strong sense below a condition. At level $2$ this is no longer possible for most notions of forcing: no Cohen condition makes all its members infinite, or all of them finite. The forcing relation of :ref{#def-forcing-relation} handles $\Pi^0_2$ sentences by a **density** clause, and a forcing question for $\Sigma^0_2$ sentences has to quantify over the extensions of a condition. This lesson makes the passage from level $1$ to level $2$ explicit, shows that the cost lies in the complexity of the partial order, and proves the abstract jump cone avoidance theorem, in the local form needed for the applications. The examples are Cohen forcing and Jockusch–Soare forcing, for which the result is the theorem of Wang that a path of a $\Pi^0_1$ class can avoid a cone and a jump cone at the same time.

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
If the question at level $1$ is $\Sigma^0_1$-preserving, the last conjunct is $\Pi^0_1$. The lifted question is then $\Sigma^0_2$ as soon as the conditions can be listed by codes such that being a condition and extension are $\Pi^0_1$, or computable relative to a fixed oracle that is absorbed. The three examples of the course behave differently.

:::example{#ex-lifted-questions}
1. **Cohen forcing.** Strings and their order are computable, so $\sigma \mathrel{?{\vdash}} \exists y\ \psi(y)$ if and only if there are $\tau \succeq \sigma$ and $m$ such that no $\rho \succeq \tau$ satisfies $\neg\psi(m)$: a $\Sigma^0_2$ relation. This is the $\Sigma^0_2$-preserving question of :ref{#ex-cohen-question}.
2. **Computable Mathias forcing.** An extension $(\tau, Y)$ of $(\sigma, X)$ is given by a string and an index of $Y$, and "the index defines an infinite subset of $X$" is $\Pi^0_2$. The lifted question is $\Sigma^0_3$, and by :ref{#cor-mathias-no-sigma2} no forcing question at level $2$ can be $\Sigma^0_2$-preserving.
3. **Jockusch–Soare forcing.** With conditions given by indices of $\Pi^0_1$ classes, being a condition is $\Pi^0_1$ but extension is $\Pi^0_2$ (:ref{#prop-js-complexity}), and the lifted question is $\Sigma^0_3$ as written. The question of :ref{#prop-tree-sigma2} avoids the quantification over extensions by deciding $\Sigma^0_2$ sentences on all members, and is $\Sigma^0_2$. The first exercise gives another solution: restricting the conditions so that the extension relation becomes $\Pi^0_1$.
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

## Weak König's lemma

By :ref{#thm-tree-question}, Jockusch–Soare forcing has forcing questions that are $\Sigma^0_1$-preserving and $\Sigma^0_2$-preserving. One generic set satisfies the conclusions of the abstract theorems at levels $1$ and $2$ at once.

:::theorem[Wang]{#thm-wkl-two-cones}
Let $C$ be a non-computable set and $D$ a set with $D \not\leq_T \emptyset'$. Every non-empty $\Pi^0_1$ class $\mathcal P$ has a member $G$ with $C \not\leq_T G$ and $D \not\leq_T G'$.
:::

:::proof{of=thm-wkl-two-cones}
Use Jockusch–Soare forcing below the condition $\mathcal P$. By :ref{#thm-local-cone-avoidance} with $\mathcal M = \{ \emptyset \}$, every sufficiently generic $G$ satisfies $C \not\leq_T G$. By :ref{#thm-local-jump-cone} with $\mathcal M = \{ \emptyset' \}$, every sufficiently generic $G$ satisfies $D \not\leq_T G'$. The union of the two countable families of dense sets is countable, so a filter through $\mathcal P$ generic for both exists (:ref{#lem-rasiowa-sikorski}), and its generic set is a member of $\mathcal P$.
:::

The same generic set avoids countably many cones $C_0, C_1, \dots$ at level $1$ and countably many cones $D_0, D_1, \dots$ at level $2$, since each cone contributes countably many dense sets. Neither basis theorem alone gives the theorem. A low member $G$ of $\mathcal P$ satisfies $D \not\leq_T G'$, but the low basis theorem gives no control over the $\Delta^0_2$ sets that $G$ computes, and $C$ may be one of them. Conversely a member avoiding the cone above $C$ may have a jump computing $D$. For a single cone at each level, the monograph attributes to Lawton a combination of the low basis theorem and the cone avoidance basis theorem: if $C$ is $\Delta^0_2$ and not computable, every non-empty $\Pi^0_1$ class has a low member not computing $C$; the case $C \not\leq_T \emptyset'$ follows from the low basis theorem alone. The forcing proof extends to countably many cones, which Lawton's proof does not.

:::quiz[Wang's theorem]
Why does the proof of :ref{#thm-wkl-two-cones} use the forcing questions of Jockusch–Soare forcing at two levels, rather than a single level?

- [x] Because avoiding the cone above $C$ is controlled by the question for $\Sigma^0_1$ sentences, relative to $\emptyset$, and avoiding the cone above $D$ in the jump by the question for $\Sigma^0_2$ sentences, relative to $\emptyset'$; one generic set meets the dense sets of both.
- [ ] Because the question for $\Sigma^0_2$ sentences does not satisfy property 2.

  It satisfies both properties, by :ref{#thm-tree-question}.
- [ ] Because $C$ may be computable in $\emptyset'$.

  This is why the low basis theorem is not enough; the forcing argument does not need to distinguish the cases.
:::

## Exercises

::::exercise{difficulty=2}
Call a tree $T \subseteq 2^{<\nat}$ **primitive recursive** if its characteristic function is.

1. Let $T$ be a co-c.e. tree, $T = \{ \sigma : \Phi_e(\sigma)\diverge \}$. Show that $S = \{ \sigma : \forall s < |\sigma|\ \Phi_e(\sigma \uh s)[s]\diverge \}$ is a primitive recursive tree with $T \subseteq S$ and $[S] = [T]$.
2. Consider Jockusch–Soare forcing with conditions the infinite primitive recursive trees, given by indices in a computable list of all primitive recursive functions, ordered by inclusion, the members of $T$ being its paths. Show that being a condition and extension are $\Pi^0_1$, that the question "$T \mathrel{?{\vdash}} \Phi^G_e\converge$ if there is $\ell$ such that $\Phi^\sigma_e[\ell]\converge$ for every $\sigma \in T$ of length $\ell$" is a $\Sigma^0_1$-preserving forcing question, and that the lifted question is $\Sigma^0_2$-preserving.

:::solution
1. The predicate $\Phi_e(\rho)[s]\diverge$ is primitive recursive, and primitive recursive predicates are closed under bounded quantification, so $S$ is primitive recursive; it is closed under prefixes since the condition for $\sigma$ includes the one for its prefixes. If $\sigma \in T$, every prefix $\sigma \uh s$ is in $T$, so $\Phi_e(\sigma \uh s)\diverge$ and in particular $\Phi_e(\sigma \uh s)[s]\diverge$: $\sigma \in S$. So $T \subseteq S$ and $[T] \subseteq [S]$. Conversely, let $X \in [S]$ and $\sigma \prec X$. If $\Phi_e(\sigma)[t]\converge$ with $t > |\sigma|$, then $X \uh (t + 1) \notin S$, since the clause for $s = t$ fails. So $\Phi_e(\sigma)\diverge$ for every $\sigma \prec X$, and $X \in [T]$.
2. A primitive recursive function is total, so an index always defines a tree once "closed under prefixes and $\{0,1\}$-valued" is checked, a $\Pi^0_1$ property; infinity is $\Pi^0_1$ (a node at every length); $S \subseteq T$ is $\Pi^0_1$. If some length $\ell$ makes the computation converge in $\ell$ steps on all nodes of that length, every path extends a node of length $\ell$ and satisfies the sentence, so $T$ forces it. Otherwise, for every $\ell$ some node $\sigma \in T$ of length $\ell$ has $\Phi^\sigma_e[\ell]\diverge$. The set $S$ of nodes $\sigma \in T$ with $\Phi^\sigma_e[|\sigma|]\diverge$ is primitive recursive, closed under prefixes by monotonicity of computations, and has a node at every length; so it is a condition. Every path $X$ of $S$ satisfies $\Phi^X_e\diverge$: if the computation converged with use $u$ at stage $s$, the prefix of $X$ of length $\max(u, s)$ would not be in $S$. The question is $\Sigma^0_1$. In the lifted question, "$d$ is a condition", "$d \subseteq c$" and "$d \mathrel{?{\nvdash}} \neg\psi(m)$" are $\Pi^0_1$, so the question is $\Sigma^0_2$. By part 1, every non-empty $\Pi^0_1$ class is the set of paths of an infinite primitive recursive tree, so this gives a second proof of :ref{#thm-wkl-two-cones}.
:::
::::

::::exercise{difficulty=2}
Let $f$ be hyperimmune relative to $\emptyset'$. Using the lifted question of Cohen forcing, show that $f$ is hyperimmune relative to $G'$ for every sufficiently Cohen generic set $G$.

:::solution
Fix $e$. By Post's theorem relativized, there are $\Pi^0_1$ formulas $\psi_{m,k}(y)$, computable from $m$ and $k$, such that "$\Phi^{G'}_e(m)\converge < k$" is equivalent to $\exists y\ \psi_{m,k}(y)$; we write "$\Phi^{G'}_e(m)\converge$" as the $\Sigma^0_2$ sentence $\exists \langle k, y \rangle\ \psi_{m,k}(y)$. The lifted question is then **compact**: if $\sigma \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge$, witnessed by $\tau \succeq \sigma$ and $\langle k, y \rangle$, the same $\tau$ and $y$ witness $\sigma \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < k$.

Let $E_e$ be the set of strings forcing $\Phi^{G'}_e(m)\diverge$, or forcing $\Phi^{G'}_e(m)\converge < f(m)$, for some $m$. Given $\sigma$, let $g$ be the partial $\emptyset'$-computable function such that $g(m)$ is the $k$ of the first pair $(m, k)$ found with $\sigma \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < k$; the search is $\emptyset'$-effective since the question is $\Sigma^0_2$. If $g(m)$ is undefined, then $\sigma \mathrel{?{\nvdash}} \Phi^{G'}_e(m)\converge$ by compactness, and property 2 gives an extension forcing $\Phi^{G'}_e(m)\diverge$. If $g$ is total, it is $\emptyset'$-computable, so $f(m) > g(m)$ for some $m$, and property 1 gives an extension forcing $\Phi^{G'}_e(m)\converge < g(m)$, hence $\Phi^{G'}_e(m)\converge < f(m)$. So $E_e$ is dense. If $G$ comes from a $2$-generic filter meeting every $E_e$, then by :ref{#thm-forcing-truth}, for every $e$, $\Phi^{G'}_e$ is partial or below $f$ at some point, so no $G'$-computable function dominates $f$.
:::
::::

## Notes and references

The discussion of the forcing relation for $\Pi^0_2$ sentences, the forcing question of Cohen forcing at level $2$ and the abstract theorem follow the section *Forcing and density* of the chapter *Jump cone avoidance* of Patey's monograph; the lifted question is stated there for each example separately, and is isolated here as :ref{#def-lifted-question}. :ref{#thm-wkl-two-cones} is due to Wang (2016); the monograph proves it with primitive recursive trees, the route of the first exercise, and states the second exercise, for Cohen forcing, after the abstract theorem; the corresponding statement for $\Pi^0_1$ classes, preserving a hyperimmune function and a function hyperimmune relative to $\emptyset'$ at once, is an exercise there attributed to Le Houérou, Levy Patey and Mimouni (2024). Lawton's theorem is quoted from the monograph, which refers to Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008).

- W. Wang, *The definability strength of combinatorial principles*, Journal of Symbolic Logic 81 (2016), 1531–1554.
- D. R. Hirschfeldt, C. G. Jockusch, Jr., B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, sections *Forcing and density* and *Weak König's lemma*.
