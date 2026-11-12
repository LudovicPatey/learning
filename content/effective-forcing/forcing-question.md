---
title: The forcing question
summary: Forcing questions and their definability; a forcing question for tree forcings at every level; preservation of non-Σ⁰ₙ sets and cone avoidance for the iterated jumps; compactness and preservation of hyperimmunity; merging and avoidance of PA degrees.
duration: 45
prerequisites: [sacks-forcing, pi01-classes/pa-degrees, immunity-growth/immune-sets]
---

The preservation theorem for Cohen forcing (:ref{#thm-cohen-preservation}) used one fact about the forcing relation: for a condition $c$ and a $\Sigma^0_n$ formula $\varphi(x)$, the set of $m$ such that $c$ can be extended to force $\varphi(m)$ is $\Sigma^0_n$. For tree forcings the forcing relation is too complex for this (:ref{#prop-js-complexity}), but the proof of :ref{#thm-tree-gl2} used a substitute at level $2$: a $\Sigma^0_2$ question whose positive answer yields an extension forcing the sentence, and whose negative answer yields an extension forcing its negation.

A **forcing question** is such a substitute, at every level. It isolates what the density arguments of the previous lessons need, and leaves aside how the extensions are found. This lesson defines forcing questions, builds one for tree forcings, and proves three preservation theorems that hold for every notion of forcing whose forcing question has the right properties: preservation of the arithmetic hierarchy and cone avoidance, preservation of hyperimmunity, and avoidance of PA degrees. The method is due to Monin and Patey, and is used to prove that combinatorial principles admit computationally weak solutions.

## Forcing questions

:::definition{#def-forcing-question}
Let $\mathbb P$ be a notion of forcing. A **forcing question** is a relation $c \mathrel{?{\vdash}} \varphi$ between conditions and sentences of the form $\Sigma^0_n$, $n \geq 1$, such that for every condition $c$ and every such sentence $\varphi$:

1. if $c \mathrel{?{\vdash}} \varphi$, some extension of $c$ forces $\varphi$;
2. if $c \mathrel{?{\nvdash}} \varphi$, some extension of $c$ forces $\neg \varphi$.

The question is **$\Sigma^0_n$-preserving** if for every condition $c$ and every $\Sigma^0_n$ formula $\varphi(\vec x)$, the relation $\{ \vec m : c \mathrel{?{\vdash}} \varphi(\vec m) \}$ is $\Sigma^0_n$.
:::

The question does not decide whether $c$ forces $\varphi$; it tells which of $\varphi$ and $\neg \varphi$ can be forced below $c$, and may answer either way when both can. Every notion of forcing has a forcing question: let $c \mathrel{?{\vdash}} \varphi$ if some extension of $c$ forces $\varphi$; property 2 holds by :ref{#prop-forcing-basic}. The point is definability.

:::example{#ex-cohen-question}
For Cohen forcing, the relation "$\sigma \mathrel{?{\vdash}} \varphi$ if some $\tau \succeq \sigma$ forces $\varphi$" is a forcing question, and it is $\Sigma^0_n$-preserving for every $n$ by :ref{#thm-cohen-forcing-definable}. At level $1$, $\sigma \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if and only if $\Phi^\tau_e(\vec m)\converge$ for some $\tau \succeq \sigma$.
:::

:::theorem{#thm-tree-question}
Jockusch–Soare forcing and computable Sacks forcing have forcing questions that are $\Sigma^0_n$-preserving for every $n \geq 1$.
:::

:::proof{of=thm-tree-question}
Conditions are given by indices. We define $c \mathrel{?{\vdash}} \varphi$ by induction on the level of $\varphi$, and prove properties 1 and 2 together with the following uniform form of preservation: for each $n$, there is a $\Sigma^0_n$ relation that agrees with "$c \mathrel{?{\vdash}} \varphi$" on indices $c$ of conditions and codes of $\Sigma^0_n$ sentences $\varphi$.

*Level $1$.* For Jockusch–Soare forcing, $\mathcal P \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if $\mathcal P$ forces it, a $\Sigma^0_1$ relation by :ref{#prop-js-complexity}. If not, the class $\mathcal P \cap \{ X : \Phi^X_e(\vec m)\diverge \}$ is non-empty and forces the negation. For Sacks forcing, $T \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if some node $T(\rho)$ has $\Phi^{T(\rho)}_e(\vec m)\converge$, a $\Sigma^0_1$ relation. If so, the full subtree above $T(\rho)$ forces the sentence; if not, $T$ forces its negation by :ref{#prop-sacks-complexity}.

*Level $2$.* Let $c \mathrel{?{\vdash}} \varphi$ if $c$ answers yes for $\varphi$ in the sense of :ref{#prop-tree-sigma2}, which gives properties 1 and 2 and the $\Sigma^0_2$ bound.

*Level $k + 1$, $k \geq 2$.* Let $\varphi = \exists y\ \psi(y)$, with $\psi$ a $\Pi^0_k$ formula. Let $c \mathrel{?{\vdash}} \varphi$ if there are a condition $d \leq c$ and a number $m$ with $d \mathrel{?{\nvdash}} \neg \psi(m)$.

1. If $c \mathrel{?{\vdash}} \varphi$, take $d$ and $m$; by property 2 at level $k$, some $e \leq d$ forces $\neg \neg \psi(m) = \psi(m)$, hence forces $\varphi$.
2. If $c \mathrel{?{\nvdash}} \varphi$, then $d \mathrel{?{\vdash}} \neg \psi(m)$ for every $d \leq c$ and every $m$. We show that $c$ forces $\neg \varphi = \forall y\ \neg \psi(y)$, that is, that no $d \leq c$ forces $\psi(m)$. If $d$ did, property 1 at level $k$ would give $e \leq d$ forcing $\neg \psi(m)$, while $e$ forces $\psi(m)$ by extension, contradicting consistency (:ref{#prop-forcing-basic}).
3. "$d$ is a condition" is $\Pi^0_1$ or $\Pi^0_2$, "$d \leq c$" is $\Pi^0_2$ or $\Pi^0_1$ (:ref{#prop-js-complexity}, :ref{#prop-sacks-complexity}), and "$d \mathrel{?{\nvdash}} \neg \psi(m)$" is $\Pi^0_k$ by the induction hypothesis. Since $k \geq 2$, the relation $\exists d\ \exists m\ (\Pi^0_k)$ is $\Sigma^0_{k+1}$.
:::

The step from level $k$ to level $k + 1$ uses only properties 1 and 2 at level $k$ and the fact that conditions and extension are $\Pi^0_2$. The real work is at levels $1$ and $2$, where each notion of forcing needs its own question. The table summarizes the properties of the questions of this lesson and of the next one.

| notion of forcing | $\Sigma^0_1$-preserving | $\Sigma^0_n$-preserving, all $n$ | compact | merging |
| --- | --- | --- | --- | --- |
| Cohen | yes | yes | yes | yes |
| Jockusch–Soare | yes | yes | yes | no |
| computable Sacks | yes | yes | yes | yes |
| computable Mathias | yes | no ($n = 2$) | yes | yes |

## Preservation of the arithmetic hierarchy

The proof of :ref{#thm-cohen-preservation} carries over verbatim, with the forcing question in place of the search for an extension.

:::theorem{#thm-question-preservation}
Let $n \geq 1$, and let $\mathbb P$ be a notion of forcing with a $\Sigma^0_n$-preserving forcing question. If $A$ is not $\Sigma^0_n$, then $A$ is not $\Sigma^0_n(G)$ for every sufficiently generic set $G$.
:::

:::proof{of=thm-question-preservation}
For a $\Sigma^0_n$ formula $\varphi(x)$, let $E_\varphi$ be the set of conditions that force $\varphi(m)$ for some $m \notin A$, or force $\neg \varphi(m)$ for some $m \in A$. Given a condition $c$, the set $U = \{ m : c \mathrel{?{\vdash}} \varphi(m) \}$ is $\Sigma^0_n$, so $U \neq A$. If $m \in U \setminus A$, property 1 gives an extension forcing $\varphi(m)$; if $m \in A \setminus U$, property 2 gives an extension forcing $\neg \varphi(m)$. So $E_\varphi$ is dense. A set $G$ generic for the sets $E_\varphi$ and for the sets $D_\psi$, $\psi$ of level at most $n$, satisfies, for each $\varphi$, $G \models \varphi(m)$ for some $m \notin A$ or $G \models \neg \varphi(m)$ for some $m \in A$ (:ref{#thm-forcing-truth}). No $\Sigma^0_n$ formula defines $A$ with parameter $G$, so $A$ is not $\Sigma^0_n(G)$.
:::

:::figure[The density argument of :ref{#thm-question-preservation}, and of :ref{#thm-cohen-preservation}. The set $U$ of numbers $m$ for which the condition $c$ answers yes about $\varphi(m)$ is $\Sigma^0_n$, so it differs from $A$; an element of the difference gives an extension on which $\varphi$ and $A$ disagree.]
<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="The density argument: the set U of numbers m such that c answers yes to the question about phi(m) differs from A; an element of the difference gives an extension forcing phi(m) with m outside A, or not phi(m) with m in A"><defs><marker id="ef-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="200" y="10" width="200" height="56" rx="6" class="state"/><text x="300.0" y="30" text-anchor="middle" class="label">condition c</text><text x="300.0" y="46" text-anchor="middle" class="label">U = { m : c ?⊢ φ(m) } is Σ⁰ₙ</text><rect x="20" y="128" width="240" height="56" rx="6" class="state"/><text x="140.0" y="148" text-anchor="middle" class="label">m ∈ U, m ∉ A</text><text x="140.0" y="164" text-anchor="middle" class="label">d ≤ c with d ⊩ φ(m)</text><rect x="340" y="128" width="240" height="56" rx="6" class="state"/><text x="460.0" y="148" text-anchor="middle" class="label">m ∈ A, m ∉ U</text><text x="460.0" y="164" text-anchor="middle" class="label">d ≤ c with d ⊩ ¬φ(m)</text><line x1="270" y1="68" x2="160" y2="124" class="ink-stroke" stroke-width="1.2" marker-end="url(#ef-arr)"/><line x1="330" y1="68" x2="440" y2="124" class="ink-stroke" stroke-width="1.2" marker-end="url(#ef-arr)"/><text x="300" y="104" text-anchor="middle" class="label">A is not Σ⁰ₙ, so U ≠ A</text><text x="300" y="206" text-anchor="middle" class="label">either way, φ does not define A from a generic set below d</text></svg>
:::

:::corollary{#cor-question-jump-cone}
Let $n \geq 0$, and let $\mathbb P$ be a notion of forcing with a $\Sigma^0_{n+1}$-preserving forcing question. If $A$ is not computable in $\emptyset^{(n)}$, then $A$ is not computable in $G^{(n)}$ for every sufficiently generic set $G$. In particular this holds for Jockusch–Soare and computable Sacks forcing, for every $n$.
:::

:::proof{of=cor-question-jump-cone}
As in :ref{#cor-cohen-jump-cone}: $A$ or its complement is not $\Sigma^0_{n+1}$, hence not $\Sigma^0_{n+1}(G)$, so $A$ is not computable in $G^{(n)}$ by Post's theorem relativized. The last statement is :ref{#thm-tree-question}.
:::

For Jockusch–Soare forcing and $n = 0$ this is the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}); for $n = 1$, it gives a member of every non-empty $\Pi^0_1$ class whose jump does not compute a given set not computable in $\emptyset'$.

:::quiz[forcing questions]
Why does :ref{#def-forcing-question} not require that $c$ itself force $\varphi$ when $c \mathrel{?{\vdash}} \varphi$?

- [x] Because the density arguments only need an extension of $c$ with the required property, and requiring more would make the question as complex as the forcing relation.
- [ ] Because no condition forces a $\Sigma^0_n$ sentence.

  Conditions force many $\Sigma^0_n$ sentences; the question is about what can be reached below $c$.
- [ ] Because the answer would otherwise be undecidable.

  The issue is the level of definability, not decidability.

---

In the proof of :ref{#thm-tree-question}, where is it used that being a condition and extension are $\Pi^0_2$?

- [x] In the complexity bound at level $k + 1 \geq 3$: the quantifier over extensions $d \leq c$ adds a $\Pi^0_2$ conjunct, which is absorbed in $\Pi^0_k$ since $k \geq 2$.
- [ ] In properties 1 and 2 at level $k + 1$.

  Those follow from properties 1 and 2 at level $k$ and from consistency, for any notion of forcing.
- [ ] At level $1$.

  Level $1$ uses the specific descriptions of :ref{#prop-js-complexity} and :ref{#prop-sacks-complexity}.
:::

## Preservation of hyperimmunity

A function $f$ is **hyperimmune relative to $G$** if no $G$-computable function dominates it (:ref{#def-hyperimmune-fn} relativized). Weakly 1-generic sets compute hyperimmune functions, so Cohen generic sets do not preserve all hyperimmune functions at once; they preserve each one separately. The property needed is that a positive answer about a convergence is witnessed by a finite bound on the value. For a functional $\Phi_e$, let $\Phi_{b(e)}$ be the functional such that $\Phi^G_{b(e)}(m, k)\converge$ if and only if $\Phi^G_e(m)\converge < k$, with $b$ computable; we write "$\Phi^G_e(m)\converge < k$" for this $\Sigma^0_1$ sentence.

:::definition{#def-question-compact}
A forcing question is **compact** (at level $1$) if for every condition $c$, functional $\Phi_e$ and number $m$, if $c \mathrel{?{\vdash}} \Phi^G_e(m)\converge$, then $c \mathrel{?{\vdash}} \Phi^G_e(m)\converge < k$ for some $k$.
:::

:::theorem{#thm-question-hyperimmunity}
Let $\mathbb P$ have a $\Sigma^0_1$-preserving compact forcing question, and let $f$ be a hyperimmune function. For every sufficiently generic set $G$, $f$ is hyperimmune relative to $G$.
:::

:::proof{of=thm-question-hyperimmunity}
Fix $e$, and let $E_e$ be the set of conditions $d$ such that $d \Vdash \Phi^G_e(m)\diverge$ for some $m$, or $d \Vdash \Phi^G_e(m)\converge < f(m)$ for some $m$. Given a condition $c$, the set of pairs $(m, k)$ with $c \mathrel{?{\vdash}} \Phi^G_e(m)\converge < k$ is c.e., since the question is $\Sigma^0_1$-preserving. Let $g$ be the partial computable function such that $g(m)$ is the $k$ of the first such pair enumerated with first coordinate $m$.

- If $g(m)$ is undefined for some $m$, then $c \mathrel{?{\nvdash}} \Phi^G_e(m)\converge$ by compactness, so some extension of $c$ forces $\Phi^G_e(m)\diverge$.
- If $g$ is total, it is computable, so $f(m) > g(m)$ for some $m$, since $f$ is hyperimmune. Some extension of $c$ forces $\Phi^G_e(m)\converge < g(m)$, hence $\Phi^G_e(m)\converge < f(m)$: every member satisfies it.

So $E_e$ is dense. If $G$ is generic for every $E_e$, then for every $e$, $\Phi^G_e$ is partial or $\Phi^G_e(m) < f(m)$ for some $m$, so no $G$-computable function dominates $f$.
:::

The three questions of the previous section are compact. For Cohen forcing, a string $\tau \succeq \sigma$ with $\Phi^\tau_e(m)\converge = v$ gives $\sigma \mathrel{?{\vdash}} \Phi^G_e(m)\converge < v + 1$; for Sacks forcing, a node does the same. For Jockusch–Soare forcing, if all members of $\mathcal P$ make $\Phi_e(m)$ converge, the computations converge on the strings of $T_{\mathcal P}$ of some length $\ell$, as in :ref{#lem-uniform-bound}, and one more than the largest of their values bounds them all. So for each of these notions and each hyperimmune $f$, every sufficiently generic set preserves the hyperimmunity of $f$. For Jockusch–Soare forcing this gives a **hyperimmunity-preserving basis theorem**: every non-empty $\Pi^0_1$ class has a member relative to which a given hyperimmune function remains hyperimmune. Monin and Patey state the theorem at every level $n$, for questions that are compact and $\Sigma^0_{n+1}$-preserving, with $\emptyset^{(n)}$ and $G^{(n)}$ in place of $\emptyset$ and $G$; the proof is the same.

## Avoiding PA degrees

The last property controls two questions at once. Recall that a set is PA if it computes a $\{0, 1\}$-valued DNC function (:ref{#def-pa-degree}).

:::definition{#def-question-merging}
A forcing question is **merging** (at level $1$) if for every condition $c$ and all $\Sigma^0_1$ sentences $\varphi_0$ and $\varphi_1$ with $c \mathrel{?{\nvdash}} \varphi_0$ and $c \mathrel{?{\nvdash}} \varphi_1$, some extension of $c$ forces both $\neg \varphi_0$ and $\neg \varphi_1$.
:::

:::theorem{#thm-question-pa}
Let $\mathbb P$ have a $\Sigma^0_1$-preserving merging forcing question. Every sufficiently generic set $G$ is not PA.
:::

:::proof{of=thm-question-pa}
Fix $e$, and let $E_e$ be the set of conditions $d$ for which there is $i$ such that every member $X$ of $d$ satisfies $\Phi^X_e(i) \notin \{0, 1\}$, the computation diverging or giving another value, or every member satisfies $\Phi^X_e(i)\converge = \Phi_i(i)$, the right-hand side converging. Given a condition $c$, let $g$ be the partial computable function such that $g(i)$ is the first $v \in \{0, 1\}$ found with $c \mathrel{?{\vdash}} \Phi^G_e(i)\converge = v$; it is partial computable since the question is $\Sigma^0_1$-preserving. Let $i$ be an index of $g$, so that $\Phi_i = g$.

- If $g(i)$ is undefined, then $c \mathrel{?{\nvdash}} \Phi^G_e(i)\converge = 0$ and $c \mathrel{?{\nvdash}} \Phi^G_e(i)\converge = 1$, and since the question is merging, some extension of $c$ forces both negations: on its members, $\Phi_e(i)$ does not converge to $0$ or $1$.
- If $g(i) = v$, then $\Phi_i(i) = v$, and some extension of $c$ forces $\Phi^G_e(i)\converge = v = \Phi_i(i)$.

So $E_e$ is dense. If $G$ is generic for every $E_e$, no $\Phi^G_e$ is a $\{0, 1\}$-valued DNC function, so $G$ is not PA.
:::

The questions of Cohen and Sacks forcing are merging: if no extension of $\sigma$, or no node of $T$, makes either of two computations converge, the condition itself forces both divergences. Jockusch–Soare forcing has no $\Sigma^0_1$-preserving merging question: below the condition $\mathrm{DNC}_2$, every generic set is PA, so the conclusion of :ref{#thm-question-pa} fails. Here, two classes $\mathcal P \cap \{ X : \neg \varphi_0(X) \}$ and $\mathcal P \cap \{ X : \neg \varphi_1(X) \}$ can both be non-empty and disjoint.

:::quiz[compactness and merging]
In the proof of :ref{#thm-question-hyperimmunity}, why is compactness needed in the first case?

- [x] To conclude from the absence of any bound $k$ that the question about $\Phi^G_e(m)\converge$ itself is answered negatively, so that property 2 gives an extension forcing divergence.
- [ ] To show that $g$ is computable.

  $g$ is partial computable by $\Sigma^0_1$-preservation alone.
- [ ] To find an $m$ with $f(m) > g(m)$.

  That is the hyperimmunity of $f$, in the second case.

---

In the proof of :ref{#thm-question-pa}, why is $i$ chosen as an index of $g$ itself?

- [x] So that a positive answer $g(i) = v$ makes the forced value $\Phi^G_e(i) = v$ coincide with $\Phi_i(i)$, which defeats diagonal non-computability at $i$.
- [ ] So that $g$ is total.

  $g$ may be partial; the case $g(i)$ undefined is handled by merging.
- [ ] So that $\Phi_i(i)$ diverges.

  If $g(i)$ is defined, $\Phi_i(i)$ converges to it.
:::

## Exercises

::::exercise{#exr-sacks-dnc difficulty=2}
Call a forcing question **$\omega$-merging** if whenever $c \mathrel{?{\nvdash}} \varphi_v$ for all $v$ in an infinite computable sequence of $\Sigma^0_1$ sentences $(\varphi_v)$, some extension of $c$ forces every $\neg \varphi_v$. Show that if a $\Sigma^0_1$-preserving forcing question is $\omega$-merging, every sufficiently generic set computes no DNC function, and that the question of Sacks forcing is $\omega$-merging.

:::solution
Repeat the proof of :ref{#thm-question-pa} with $g(i)$ the first $v \in \nat$ found with $c \mathrel{?{\vdash}} \Phi^G_e(i)\converge = v$. If $g(i)$ is undefined, $c \mathrel{?{\nvdash}} \Phi^G_e(i)\converge = v$ for every $v$, and $\omega$-merging gives an extension forcing all the negations, that is, $\Phi^G_e(i)\diverge$. Otherwise an extension forces $\Phi^G_e(i) = \Phi_i(i)$. So $\Phi^G_e$ is not DNC, for every $e$. For Sacks forcing, $T \mathrel{?{\nvdash}} \varphi_v$ means that no node of $T$ makes the corresponding computation converge, so $T$ forces all the negations at once, by :ref{#prop-sacks-complexity}.
:::
::::

## Notes and references

The forcing question was introduced by Monin and Patey, and appears in several of their papers on the reverse mathematics of Ramsey-type theorems, for instance in *Pigeons do not jump high* (2019), where forcing relations and questions adapted to variants of Mathias forcing are designed to build solutions to the pigeonhole principle that are not high; Patey (2015, arXiv) had used forcing relations with the complexity of the formulas they force to control iterated jumps. The abstract definition and the three preservation theorems of this lesson follow the chapter *Effective forcing* of Monin and Patey, section *Forcing question*, where compactness and merging are called compactness and $\Pi$-merging; the definitions there are given for questions about $\Sigma^0_n$ and $\Pi^0_n$ sentences, and are stated here for $\Sigma^0_1$ sentences only.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics (2019), doi:10.1016/j.aim.2019.06.026; arXiv:1803.09771.
- L. Patey, *Controlling iterated jumps of solutions to combinatorial problems*, arXiv:1509.05340 (2015).
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, sections *Computational complexity and forcing question* and *Forcing question*.
