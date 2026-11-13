---
title: The MacDowell–Specker theorem
summary: Strongly definable types, in which one formula decides a whole definable family of formulas; a cohesiveness lemma proved inside a model of PA; Gaifman's theorem that every model of PA has an unbounded strongly definable type; strongly definable unbounded types are definable; every model of PA has a proper elementary end extension, and a model of IΔ₀ has one only if it satisfies PA.
duration: 45
prerequisites: [definable-types]
---

By the previous lesson, a proper elementary end extension of a model $M$ of $\mathrm{PA}$ follows from an unbounded definable type over $M$. If $M$ is countable, one can build a complete type in countably many steps; but a type has as many formulas as $M$ has elements, and for the type to be definable, $M$ must decide, for each formula $\varphi(v, z)$, *all* the instances $\varphi(v, a)$, $a \in M$, in a uniform way. The idea of Gaifman and Phillips is to decide all instances of one formula at once by a single definable set $S$: $S$ should be **cohesive** for the family, eventually inside or eventually outside each set $\{ v : \varphi(v, a) \}$. Such sets exist in $M$ by a construction carried out inside $M$, and only countably many formulas $\varphi$ without parameters have to be handled, so a countable chain of sets suffices, whatever the cardinality of $M$. The types obtained are **strongly definable**.

## Strongly definable types

Throughout, $M$ is a model of $\mathrm{PA}$. We write $\exists^\infty v\ \theta(v)$ for $\forall u\ \exists v \geq u\ \theta(v)$, "there are unboundedly many $v$ with $\theta(v)$", and $\forall^\infty v\ \theta(v)$ for $\neg \exists^\infty v\ \neg \theta(v)$, "all $v$ beyond some bound satisfy $\theta(v)$". For sets $S, R \subseteq M$, $S \subseteq^* R$ means that $S \setminus R$ is bounded in $M$.

Let $p(v)$ be an unbounded complete $M$-type. Every $\theta \in p$ defines an unbounded set: if $\theta(M)$ were below $a$, the formula $\theta(v) \wedge v > a$ of $p$ would not be satisfied in $M$. So if $\theta \in p$ and $M \models \forall^\infty v\ (\theta(v) \rightarrow \varphi(v))$, then $\neg \varphi \notin p$, since $\theta \wedge \neg \varphi$ defines a bounded set; hence $\varphi \in p$. We say that $\theta$ **forces** $\varphi$.

:::definition{#def-ee-strongly-definable}
An unbounded complete $M$-type $p(v)$ is **strongly definable** if for every formula $\varphi(v, z)$ of $\mathcal L_A$ there is $\theta(v) \in p$ such that
$$
M \models \forall z\ \big( \forall^\infty v\ (\theta(v) \rightarrow \varphi(v, z)) \vee \forall^\infty v\ (\theta(v) \rightarrow \neg \varphi(v, z)) \big).
$$
:::

A single formula $\theta$ decides all the instances $\varphi(v, a)$, $a \in M$, together. Strongly definable types are also called **end-extensional** types in the literature. Tuples of parameters are handled by pairing, so one variable $z$ suffices.

:::lemma{#lem-ee-strongly-definable-definable}
Every strongly definable unbounded complete $M$-type $p$ is definable: for $\varphi(v, z)$ and $\theta$ as in the definition,
$$
\{ a \in M : \varphi(v, a) \in p \} = \{ a \in M : M \models \forall^\infty v\ (\theta(v) \rightarrow \varphi(v, a)) \}.
$$
:::

:::proof{of=lem-ee-strongly-definable-definable}
If $M \models \forall^\infty v\ (\theta(v) \rightarrow \varphi(v, a))$, then $\theta$ forces $\varphi(v, a)$, which is in $p$. Otherwise, by the choice of $\theta$, $\theta$ forces $\neg \varphi(v, a)$, which is in $p$, so $\varphi(v, a) \notin p$.
:::

The converse fails: there are unbounded definable types that are not strongly definable (Gaifman, Proposition 2.23, as reported by Wong).

## A cohesiveness lemma inside the model

:::lemma[Cohesive sets]{#lem-ee-cohesive}
Let $S \subseteq M$ be unbounded and $R \subseteq M^2$, both definable in $M$ with parameters, and write $R_z = \{ v : (z, v) \in R \}$. There is an unbounded set $H \subseteq S$, definable in $M$ from the same parameters, such that for every $z \in M$, $H \subseteq^* R_z$ or $H \subseteq^* M \setminus R_z$.
:::

**Idea.** Inside $M$, refine $S$ one $z$ at a time, keeping the half of the current set that is unbounded, $R_z$ if possible and its complement otherwise; then pick one new element in each refinement. The construction is a recursion of length $M$, which $M$ can carry out since it satisfies full induction. The $z$-th refinement contains all elements of $H$ chosen after step $z$, so only the $z$ elements chosen before can fall on the wrong side.

:::proof{of=lem-ee-cohesive}
For a string $b$ of length $j$ (:ref{#def-strings-model}), let
$$
S_b = \{ v \in S : \forall i < j\ (v \in R_i \leftrightarrow b(i) = 1) \},
$$
a set definable uniformly in $b$. Call $b$ **correct** if for every $i < j$, $b(i) = 1$ exactly when $S_{b \restriction i} \cap R_i$ is unbounded. By induction in $M$, for every $j$ there is a correct string of length $j$ with $S_b$ unbounded: the empty string works, and if $b$ is correct with $S_b$ unbounded, then $b 1$ is correct if $S_b \cap R_j = S_{b1}$ is unbounded, and otherwise $b 0$ is correct and $S_{b0} = S_b \setminus R_j$ is unbounded, since $S_b$ is the union of the two. Two correct strings of the same length are equal, by comparing their first difference. Let $b_j$ be the correct string of length $j$; then $b_j \sqsubseteq b_{j'}$ for $j \leq j'$, and the map $j \mapsto b_j$ is definable.

Define, by recursion in $M$, $h_0 = \min S_{b_1}$ and $h_{j+1} = \min \{ v \in S_{b_{j+2}} : v > h_j \}$, which exists since $S_{b_{j+2}}$ is unbounded. Let $H = \{ h_j : j \in M \}$. It is definable, contained in $S$, and unbounded, since $h_j \geq j$ by induction. For $z \in M$ and $j \geq z$, $h_j \in S_{b_{j+1}} \subseteq S_{b_{z+1}}$, which is contained in $R_z$ if $b_{z+1}(z) = 1$ and in $M \setminus R_z$ otherwise. Only $h_0, \dots, h_{z-1}$ may lie on the other side, and they are below $h_z$. So $H \subseteq^* R_z$ or $H \subseteq^* M \setminus R_z$.
:::

:::figure[The proof of :ref{#lem-ee-cohesive}. At step $z$ the current set is split by $R_z$ and an unbounded half is kept; the element $h_z$ is chosen in it, above the previous ones. All later elements of $H$ lie on the same side of $R_z$.]
<svg class="fig" viewBox="0 0 600 200" width="600" role="img" aria-label="Two refinement steps: the set S is split by R_0 and then by R_1, and an unbounded half is kept each time; h_0 is chosen in the first kept half, h_1 above it in the second, so h_1 and all later elements lie in R_0 and outside R_1, while h_0 may lie in R_1"><line x1="60.0" y1="40.0" x2="580.0" y2="40.0" class="muted-stroke" stroke-width="1.0" stroke-dasharray="2 4"/><line x1="60.0" y1="40.0" x2="580.0" y2="40.0" class="accent-stroke" stroke-width="3.0"/><text x="30.0" y="32.0" text-anchor="start" class="label">S</text><line x1="60.0" y1="90.0" x2="580.0" y2="90.0" class="muted-stroke" stroke-width="1.0" stroke-dasharray="2 4"/><line x1="60.0" y1="90.0" x2="140.0" y2="90.0" class="accent-stroke" stroke-width="3.0"/><line x1="230.0" y1="90.0" x2="330.0" y2="90.0" class="accent-stroke" stroke-width="3.0"/><line x1="420.0" y1="90.0" x2="580.0" y2="90.0" class="accent-stroke" stroke-width="3.0"/><text x="30.0" y="82.0" text-anchor="start" class="label">S ∩ R₀</text><line x1="60.0" y1="140.0" x2="580.0" y2="140.0" class="muted-stroke" stroke-width="1.0" stroke-dasharray="2 4"/><line x1="100.0" y1="140.0" x2="140.0" y2="140.0" class="accent-stroke" stroke-width="3.0"/><line x1="260.0" y1="140.0" x2="330.0" y2="140.0" class="accent-stroke" stroke-width="3.0"/><line x1="470.0" y1="140.0" x2="580.0" y2="140.0" class="accent-stroke" stroke-width="3.0"/><text x="30.0" y="132.0" text-anchor="start" class="label">S ∩ R₀ ∖ R₁</text><circle cx="80.0" cy="90.0" r="4" class="ink-fill"/><text x="80.0" y="80.0" text-anchor="middle" class="math" font-size="13">h<tspan class="mrm" font-size="10" dy="3">0</tspan></text><circle cx="280.0" cy="140.0" r="4" class="ink-fill"/><text x="280.0" y="130.0" text-anchor="middle" class="math" font-size="13">h<tspan class="mrm" font-size="10" dy="3">1</tspan></text><text x="300.0" y="172.0" text-anchor="middle" class="label">h₁ and all later elements of H lie in R₀ and outside R₁;</text><text x="300.0" y="190.0" text-anchor="middle" class="label">h₀ lies in R₀ and may lie in R₁</text></svg>
:::

The lemma is the arithmetic counterpart of the existence of cohesive sets in computability: for a uniformly computable sequence of sets, $\emptyset''$ computes an infinite set eventually inside or eventually outside each of them, by the same construction. Here no oracle is needed: the questions "is $S_b \cap R_i$ unbounded?" are answered by formulas of $M$, and the whole construction is a definable recursion. By the same token, if $S$ and $R$ are definable without parameters, so is $H$, uniformly in their definitions.

## Gaifman's theorem and the MacDowell–Specker theorem

:::theorem[Gaifman]{#thm-ee-gaifman-sd}
Every model $M$ of $\mathrm{PA}$ has an unbounded strongly definable complete $M$-type.
:::

:::proof{of=thm-ee-gaifman-sd}
Enumerate the formulas of $\mathcal L_A$ in two free variables as $\varphi_0(v, z), \varphi_1(v, z), \dots$; there are countably many, since they have no parameters. Define definable unbounded sets $M = S_0 \supseteq S_1 \supseteq S_2 \supseteq \cdots$: given $S_i$, apply :ref{#lem-ee-cohesive} to $S_i$ and $R^i = \{ (z, v) : M \models \varphi_i(v, z) \}$, and let $S_{i+1} = H$. Let $\theta_i(v)$ be a formula of $\mathcal L_A(M)$ that defines $S_i$, and
$$
p(v) = \{ \psi(v) \in \mathcal L_A(M) : M \models \forall^\infty v\ (\theta_i(v) \rightarrow \psi(v)) \text{ for some } i \}.
$$
*$p$ is a complete type.* If $\psi, \psi' \in p$, witnessed by $i \leq i'$, then $\psi \wedge \psi' \in p$, witnessed by $i'$, since $S_{i'} \subseteq S_i$. Every $\psi \in p$ is satisfied by unboundedly many elements of $M$, those of $S_i$ beyond the bound; so every finite subset of $p$ is satisfied in $M$, and $p$ contains $v > a$ for each $a \in M$, witnessed by $i = 0$. Every formula of $\mathcal L_A(M)$ in $v$ is $\varphi_i(v, a)$ for some $i$ and some $a \in M$, after pairing the parameters; by the choice of $S_{i+1}$, $\varphi_i(v, a) \in p$ or $\neg \varphi_i(v, a) \in p$, witnessed by $i + 1$.

*$p$ is strongly definable.* For $\varphi_i$, the formula $\theta_{i+1} \in p$ satisfies the condition of :ref{#def-ee-strongly-definable}, by the choice of $S_{i+1}$.
:::

:::quiz[Gaifman's theorem]
The model $M$ may be uncountable. Why does a countable chain $S_0 \supseteq S_1 \supseteq \cdots$ suffice to decide all formulas with parameters?

- [x] Each step handles one formula $\varphi_i(v, z)$ without parameters, for all values $a \in M$ of $z$ at once: the set $S_{i+1}$ is cohesive for the whole definable family $\{ v : \varphi_i(v, a) \}$, $a \in M$.
- [ ] Because $M$ has only countably many definable sets.

  An uncountable model has uncountably many definable sets, since every element is definable from itself.
- [ ] Because a type is determined by its restriction to formulas without parameters.

  The formulas $v > a$ alone show that it is not.

---

Where is it used that $M$ satisfies full induction?

- [x] In :ref{#lem-ee-cohesive}, for the existence of correct strings of every length and for the recursion defining $h_j$, which concern formulas of arbitrary complexity; and in :ref{#prop-ee-conservative-end}, to see that the extension is an end extension.
- [ ] To show that $p$ is consistent.

  Consistency follows from the unboundedness of the sets $S_i$, which are chosen unbounded.
- [ ] To enumerate the formulas $\varphi_i$.

  The enumeration takes place in the metatheory.
:::

:::theorem[MacDowell, Specker]{#thm-ee-macdowell-specker}
Every model of $\mathrm{PA}$ has a proper elementary end extension, which can be chosen conservative.
:::

:::proof{of=thm-ee-macdowell-specker}
Let $p$ be given by :ref{#thm-ee-gaifman-sd}. It is definable by :ref{#lem-ee-strongly-definable-definable}, and unbounded, hence not realized in $M$. By :ref{#cor-ee-definable-end}, $M(p)$ is a proper conservative elementary end extension of $M$.
:::

:::corollary{#cor-ee-pa-characterization}
A model $M$ of $\mathrm I\Delta_0$ has a proper elementary end extension if and only if $M \models \mathrm{PA}$.
:::

:::proof{of=cor-ee-pa-characterization}
($\Leftarrow$) is :ref{#thm-ee-macdowell-specker}. ($\Rightarrow$) Let $K$ be a proper elementary end extension. Let $\varphi(x, y)$ be any formula with parameters in $M$ and $a \in M$ with $M \models \forall x < a\ \exists y\ \varphi(x, y)$. Take $b \in K \setminus M$. For $x < a$, $x \in M$, and a witness $y \in M$ for $x$ in $M$ is a witness in $K$, below $b$. So $K \models \exists b\ \forall x < a\ \exists y < b\ \varphi(x, y)$, and this holds in $M$ by elementarity. So $M$ satisfies the collection scheme for all formulas, in particular $\mathrm B\Sigma_{n+1}$ for every $n$, hence $\mathrm I\Sigma_n$ for every $n$ by :ref{#thm-fo-paris-kirby}.
:::

The argument for ($\Rightarrow$) needs no induction in $K$, unlike :ref{#thm-end-ext-collection}, because full elementarity transfers the existence of the bound $b$ directly. For countable models, the converse :ref{#fact-end-ext-converse} of the theorem of Paris and Kirby is proved by the same method, with an ultrafilter on the $\Delta_k$-definable sets chosen with the help of $\mathrm B\Sigma_{k+1}$ instead of a cohesive chain on all definable sets (Hájek and Pudlák, IV.1.57).

The proof gives more. In :ref{#lem-ee-cohesive}, $H$ is defined uniformly from the definitions of $S$ and $R$, so all the sets $S_i$ can be taken definable without parameters, by formulas $\theta_i$ that do not depend on $M$. The type is then given by the same scheme in every model of $\mathrm{PA}$: $\psi(v, \bar a) \in p$ if and only if $M \models \forall^\infty v\ (\theta_i(v) \rightarrow \psi(v, \bar a))$ for some $i$ (Wong, Remark 9.11).

The theorem does not extend to all languages. In a countable language extending $\mathcal L_A$, a structure satisfying induction for all formulas of the language has a proper elementary end extension, by the same proof. In uncountable languages this fails: Mills (1978) constructed a model of $\mathrm{PA}$ in an uncountable language with no proper elementary end extension, and Enayat (2008) a standard model of $\mathrm{PA}$ in an uncountable language with no conservative elementary extension (Wong, Further comments to Lecture 9).

## Exercises

::::exercise{#ex-ee-iterate-ms difficulty=2}
Show that every model $M$ of $\mathrm{PA}$ has elementary end extensions of every infinite cardinality $\kappa \geq |M|$.

:::solution
Define $M_0 = M$; $M_{\beta+1}$ a proper elementary end extension of $M_\beta$, by :ref{#thm-ee-macdowell-specker}, with an element $d_\beta \in M_{\beta+1} \setminus M_\beta$; and $M_\lambda = \bigcup_{\beta < \lambda} M_\beta$ at limits. A union of a chain of elementary end extensions is an elementary end extension of each member, by the elementary chain theorem and because initial segments of initial segments are initial segments; so each $M_\beta$ is a model of $\mathrm{PA}$ and the construction continues. $M_\kappa$ contains the $\kappa$ distinct elements $d_\beta$, $\beta < \kappa$. Its cardinality is at most $\kappa$ if each step adds at most $\kappa$ elements, which holds for $M(p)$ since its elements are values of definable functions of $M_\beta$, of which there are $|M_\beta|$; so $|M_\kappa| = \kappa$.
:::
::::

::::exercise{#ex-ee-forcing-unbounded difficulty=1}
Give an example showing that, for a complete $M$-type that is not unbounded, a formula $\theta \in p$ with $M \models \forall^\infty v\ (\theta(v) \rightarrow \varphi(v))$ need not imply $\varphi \in p$.

:::solution
Let $a \in M$, $p = \mathrm{tp}(a / M)$, $\theta(v)$ the formula $v = a$ and $\varphi(v)$ the formula $v \neq v$. Only boundedly many $v$ satisfy $\theta$, so $M \models \forall^\infty v\ (\theta(v) \rightarrow \varphi(v))$, while $\neg \varphi \in p$. Forcing in the sense of the lesson is meaningful only for formulas defining unbounded sets, which is what unboundedness of $p$ guarantees for all formulas of $p$.
:::
::::

## Notes and references

The theorem is due to MacDowell and Specker (1961), whose proof works with ultrafilters on the definable sets. The approach through definable types and conservative extensions is due to Gaifman (1976) and Phillips (1974), and is that of Wong's Lecture 9 (Theorem 9.10), which proves a combinatorial principle $\mathrm{COH}$ in $(M, \mathrm{Def}(M)) \models \mathrm{ACA}_0$ (Lemma 9.8); :ref{#lem-ee-cohesive} is its first-order form, proved directly in $M$. The decomposition into :ref{#thm-ee-gaifman-sd} and :ref{#lem-ee-strongly-definable-definable} is Wong's Theorem 10.1 and Lemma 10.2. :ref{#cor-ee-pa-characterization} is part (3) of Theorem IV.1.53 of Hájek and Pudlák. Enayat's survey *63 years of the MacDowell–Specker theorem* (arXiv:2208.03156, 2022) describes the later developments, including the failure of the theorem for uncountable languages.

- R. MacDowell and E. Specker, *Modelle der Arithmetik*, in Infinitistic Methods, Pergamon Press and PWN, 1961, 257–263.
- H. Gaifman, *Models and types of Peano's arithmetic*, Annals of Mathematical Logic 9 (1976), 223–306.
- R. G. Phillips, *Omitting types in arithmetic and conservative extensions*, in Victoria Symposium on Nonstandard Analysis, Lecture Notes in Mathematics 369, Springer, 1974, 195–202.
- G. Mills, *A model of Peano arithmetic with no elementary end extension*, Journal of Symbolic Logic 43 (1978), 563–567.
- A. Enayat, *A standard model of Peano arithmetic with no conservative elementary extension*, Annals of Pure and Applied Logic 156 (2008), 308–318.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 9 and 10.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter IV, Section 1(e).
