---
title: Gaps and strongly definable types
summary: Skolem functions and the gaps of a model of PA; an extension by an unbounded strongly definable type adds exactly one gap; the canonical extension of definable types, and Gaifman's characterization of strongly definable types as the unbounded types with a unique unbounded extension to every elementary extension; iterated extensions.
duration: 40
prerequisites: [macdowell-specker]
---

The MacDowell–Specker theorem gives a proper elementary end extension $M(p)$ of a model $M$ of $\mathrm{PA}$. This lesson describes its shape. The unit of measure is the **gap**: two elements are in the same gap if each is below a definable function of the other. A realization $d$ of an unbounded type sits in a gap above $M$; and when the type is strongly definable, nothing else is added: $M(p)$ is $M$ followed by the single gap of $d$. Strong definability has a characterization by uniqueness, due to Gaifman: a strongly definable type extends in exactly one unbounded way to every elementary extension, which allows the construction to be repeated along any ordinal.

## Skolem functions and gaps

:::definition{#def-ee-skolem}
A **Skolem function** is a formula $\eta(\bar v, x)$ of $\mathcal L_A$ without parameters such that $\mathrm{PA} \vdash \forall \bar v\ \exists! x\ \eta(\bar v, x)$. In every model of $\mathrm{PA}$ it defines a function, written $t(\bar v)$.
:::

Typical Skolem functions are $\bar v \mapsto (\min u)\, \chi(u, \bar v)$ and $\bar v \mapsto (\max u)\, \chi(u, \bar v)$ for a formula $\chi$, with the convention that the value is $0$ when the extremum does not exist. Skolem functions are closed under composition, and for each Skolem function $t(v)$, the function $t^*(v) = \max_{u \leq v} t(u) + v + 1$ is a Skolem function, strictly increasing, with $t^* > t$. For a model $K$ of $\mathrm{PA}$ and $A \subseteq K$, the elements definable from $A$ in the sense of :ref{#def-ee-mp} are the values $t(\bar a)$, $\bar a \in A$, of Skolem functions: if $b$ is the unique element with $\eta(b, \bar a)$, then $(\min x)\, \eta(x, \bar a)$ is a Skolem function of $\bar a$ with value $b$.

:::definition{#def-ee-gap}
Let $K \models \mathrm{PA}$ and $d \in K$. Let
$$
K(d) = \{ x \in K : x < t(d) \text{ for some Skolem function } t \}, \qquad K[d] = \{ x \in K : t(x) < d \text{ for every Skolem function } t \},
$$
and let the **gap** of $d$ be $\mathrm{gap}(d) = K(d) \setminus K[d]$.
:::

Both sets are initial segments of $K$. For $K(d)$ this is clear. If $x < y \in K[d]$ and $t$ is a Skolem function, then $t(x) \leq t'(y) < d$ for the Skolem function $t'(y) = \max_{u \leq y} t(u)$. So $\mathrm{gap}(d)$ is convex. It contains $d$: $d < d + 1$, and the identity is a Skolem function with $d \not< d$.

:::lemma{#lem-ee-gap-criterion}
Let $K \models \mathrm{PA}$ and $c, d \in K$. Then $c \in \mathrm{gap}(d)$ if and only if there are Skolem functions $t, s$ with $t(c) \geq d$ and $s(d) \geq c$.
:::

:::proof{of=lem-ee-gap-criterion}
$c \notin K[d]$ means $t(c) \geq d$ for some Skolem $t$. $c \in K(d)$ means $c < s'(d)$ for some Skolem $s'$; this implies $s(d) \geq c$ for $s = s'$, and conversely $s(d) \geq c$ implies $c < s(d) + 1$.
:::

The criterion is symmetric in $c$ and $d$. With the increasing majorants $t^*$, it shows that "being in the same gap" is an equivalence relation whose classes are the gaps: if $t(c) \geq d$ and $t'(d) \geq e$, then $t'^*(t^*(c)) \geq t'^*(d) \geq e$. Since the criterion only involves inequalities between values of Skolem functions, it is preserved by elementary extensions and substructures: if $K \preccurlyeq K'$ and $c, d \in K$, then $c \in \mathrm{gap}^K(d)$ if and only if $c \in \mathrm{gap}^{K'}(d)$. In $\nat$ there is a single gap. In general $K[0]$ is empty, and $\mathrm{gap}(0) = K(0)$ is the set of elements below some element definable without parameters: it is $\nat$ if $K$ satisfies the theory of $\nat$, and larger otherwise. The other gaps are blocks of elements that definable functions cannot separate.

## One new gap

:::proposition[Gaifman]{#prop-ee-one-gap}
Let $M \models \mathrm{PA}$, $p(v)$ an unbounded strongly definable complete $M$-type, and $d$ a realization of $p$. Then $M(p / d)$ is the disjoint union of $M$ and $\mathrm{gap}(d)$, the gap being computed in $M(p / d)$.
:::

**Idea.** An element $c$ of $M(p)$ is a definable function of $d$, with parameters in $M$, so $c \leq s(d)$ for a Skolem function $s$ that absorbs the parameters. The question is whether $d$ is bounded by a function of $c$. The formula $\theta \in p$ given by strong definability decides, for the family of formulas "$x$ is the value at $v$", whether the value is eventually constant along $\theta$. If it is, $c$ is that constant, an element of $M$. If not, every value is taken only boundedly often along $\theta$, and the bound, a function of $c$, is above $d$.

:::proof{of=prop-ee-one-gap}
Write $N = M(p / d)$. It is an end extension of $M$ (:ref{#thm-ee-macdowell-specker} and its proof), and $d > M$. Every $x \in M$ satisfies $t(x) \in M$, so $t(x) < d$, for every Skolem $t$; so $M \subseteq N[d]$ and $M \cap \mathrm{gap}(d) = \emptyset$.

Let $c \in N$. By :ref{#lem-ee-mp}, after pairing the parameters, $c$ is the unique $x$ with $\eta(x, a, d)$, where $\eta(x, z, v)$ is a formula of $\mathcal L_A$, $a \in M$, and $M \models \forall z\ \forall v\ \exists! x\ \eta(x, z, v)$; this holds in $N$ as well. Apply :ref{#def-ee-strongly-definable} to $\eta$, viewed as a formula in $v$ with the parameter $(x, z)$: there is $\theta(v, b) \in p$, with $\theta \in \mathcal L_A$ and $b \in M$, such that
$$
M \models \forall x\ \forall z\ \big( \forall^\infty v\ (\theta(v, b) \rightarrow \eta(x, z, v)) \vee \forall^\infty v\ (\theta(v, b) \rightarrow \neg \eta(x, z, v)) \big).
$$

*Case 1: $M \models \forall x\ \forall^\infty v\ (\theta(v, b) \rightarrow \neg \eta(x, a, v))$.* Then $c \notin M$: otherwise $\theta(v, b) \wedge \eta(c, a, v)$ would be a formula of $p$ defining a bounded set. So $c > M$, and $a, b < c$. The hypothesis holds in $N$, so the set of $v$ with $\theta(v, b) \wedge \eta(c, a, v)$ is bounded in $N$, and it contains $d$. Let $u(x, w, z)$ be the Skolem function "the largest $v$ with $\theta(v, w) \wedge \eta(x, z, v)$, if this set is non-empty and bounded, and $0$ otherwise", and $t(x) = \max_{w, z \leq x} u(x, w, z)$. Then $t(c) \geq u(c, b, a) \geq d$. Let $s(v) = \max_{z \leq v} (\min x)\, \eta(x, z, v)$; then $s(d) \geq c$, since $a \leq d$. By :ref{#lem-ee-gap-criterion}, $c \in \mathrm{gap}(d)$.

*Case 2: otherwise.* Some $a_0 \in M$ satisfies $M \models \exists^\infty v\ (\theta(v, b) \wedge \eta(a_0, a, v))$. By the choice of $\theta$, $M \models \forall^\infty v\ (\theta(v, b) \rightarrow \eta(a_0, a, v))$: there is $v_0 \in M$ with $M \models \forall v \geq v_0\ (\theta(v, b) \rightarrow \eta(a_0, a, v))$. This holds in $N$, and $d \geq v_0$ satisfies $\theta(d, b)$; so $N \models \eta(a_0, a, d)$, and $c = a_0 \in M$ by uniqueness.
:::

:::figure[An extension by an unbounded strongly definable type, :ref{#prop-ee-one-gap}. The model $M(p/d)$ consists of $M$ and of the gap of $d$: the elements above $M[d]$ and below $t(d)$ for some Skolem function $t$. Every element of the gap is bounded by a Skolem function of $d$ and bounds $d$ by a Skolem function of itself.]
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The extension M(p/d) consists of M followed by the gap of d, between M[d] and the bound given by Skolem functions of d"><line x1="20.0" y1="70.0" x2="560.0" y2="70.0" class="ink-stroke" stroke-width="1.2"/><circle cx="24.0" cy="70.0" r="3.5" class="accent-fill"/><text x="24.0" y="56.0" text-anchor="middle" class="mrm" font-size="13">0</text><line x1="240.0" y1="48.0" x2="240.0" y2="92.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="240.0" y="40.0" text-anchor="middle" class="math" font-size="13">M = M(p)[d]</text><circle cx="330.0" cy="70.0" r="4.5" class="accent-fill"/><text x="330.0" y="56.0" text-anchor="middle" class="math" font-size="14">d</text><circle cx="290.0" cy="70.0" r="3" class="node"/><circle cx="380.0" cy="70.0" r="3" class="node"/><circle cx="440.0" cy="70.0" r="3" class="node"/><circle cx="500.0" cy="70.0" r="3" class="node"/><text x="540.0" y="56.0" text-anchor="middle" class="math" font-size="13">t(d)</text><line x1="540.0" y1="64.0" x2="540.0" y2="76.0" class="ink-stroke" stroke-width="1.4"/><path d="M22.0,88.0 L22.0,94.0 L236.0,94.0 L236.0,88.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="129.0" y="112.0" text-anchor="middle" class="label">M: t(x) &lt; d for every Skolem t</text><path d="M246.0,88.0 L246.0,94.0 L556.0,94.0 L556.0,88.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="401.0" y="112.0" text-anchor="middle" class="label">gap(d): c ≤ s(d) and t(c) ≥ d</text></svg>
:::

:::quiz[one new gap]
In Case 1, why is the set of $v$ with $\theta(v, b) \wedge \eta(c, a, v)$ bounded in $N$?

- [x] The hypothesis of Case 1 is a sentence with parameters $a, b \in M$, true in $M$; it holds in $N$ by elementarity, and its instance at $x = c$ says that this set is bounded.
- [ ] Because $p$ is unbounded.

  Unboundedness of $p$ concerns sets definable with parameters in $M$; the set here has the parameter $c \notin M$.
- [ ] Because $c$ is the unique $x$ with $\eta(x, a, d)$.

  Uniqueness is used in Case 2; for different $v$, $\eta(c, a, v)$ may hold or not.

---

Why does the strong definability of $p$, and not only its definability, matter in this proof?

- [x] A single $\theta \in p$ must decide the formulas $\eta(x, a, v)$ for *all* $x$ at once, including $x = c$ in $N$; definability alone gives, for each $x \in M$, a formula of $p$ deciding $\eta(x, a, v)$, which says nothing about $x = c$.
- [ ] Because definable types are not unbounded.

  Unbounded definable types exist, and some are not strongly definable.
- [ ] Because $N$ would otherwise not be an end extension.

  Definability suffices for the end extension property (:ref{#cor-ee-definable-end}).
:::

There can be no elementary cut strictly inside a gap: an elementary substructure that is an initial segment and contains an element is closed under Skolem functions, hence contains its gap. So the only elementary cuts of $M(p)$ that contain $M$ are $M$ and $M(p)$. Elementary substructures that are not initial segments may still exist strictly between $M$ and $M(p)$, by thinning out the gap of $d$; the next lesson excludes them.

## Extensions of types

Let $K \succcurlyeq M$ and $p$ a complete $M$-type. An **extension** of $p$ to $K$ is a complete $K$-type $q \supseteq p$; one exists, since every finite subset of $p$ is satisfied in $M$, hence in $K$. If $p(v)$ is unbounded, an extension can be chosen unbounded, since each $\theta \in p$ defines a set unbounded in $M$, hence in $K$.

A definable type has a **canonical extension**: with the defining scheme $\mathrm d\varphi$ of $p$, let $q$ consist of the $\varphi(v, \bar a)$ with $\bar a \in K$ and $K \models \mathrm d\varphi(\bar a)$. For finitely many formulas $\varphi_1, \dots, \varphi_k$, the sentences $\forall \bar z\ (\mathrm d\neg\varphi(\bar z) \leftrightarrow \neg \mathrm d\varphi(\bar z))$ and $\forall \bar z_1 \cdots \bar z_k\ (\bigwedge_j \mathrm d\varphi_j(\bar z_j) \rightarrow \exists v\ \bigwedge_j \varphi_j(v, \bar z_j))$ hold in $M$, hence in $K$; so $q$ is a complete $K$-type extending $p$, defined over $K$ by the same scheme. For a strongly definable unbounded $p$, the scheme is given by the formulas $\theta$ of the definition, and the defining sentences of strong definability hold in $K$: the canonical extension is unbounded and strongly definable.

:::theorem[Gaifman]{#thm-ee-unique-extension}
Let $p(v)$ be an unbounded complete $M$-type. Then $p$ is strongly definable if and only if, for every $K \succcurlyeq M$, $p$ has exactly one unbounded extension to $K$.
:::

:::proof{of=thm-ee-unique-extension}
($\Rightarrow$) Let $q_1, q_2$ be unbounded extensions of $p$ to $K$, and $\varphi(v, a) \in q_1$, $a \in K$. Let $\theta \in p$ be given by strong definability for $\varphi$; the defining sentence holds in $K$. Since $\theta \wedge \varphi(v, a) \in q_1$ and $q_1$ is unbounded, $K \models \exists^\infty v\ (\theta(v) \wedge \varphi(v, a))$, so $K \models \forall^\infty v\ (\theta(v) \rightarrow \varphi(v, a))$. As $q_2$ is unbounded and contains $\theta$, it cannot contain $\neg \varphi(v, a)$; so $\varphi(v, a) \in q_2$. By symmetry $q_1 = q_2$.

($\Leftarrow$) Suppose $p$ is not strongly definable, witnessed by $\varphi(v, z)$. Let $c$ be a new constant and
$$
r(c) = \{ \exists^\infty v\ (\theta(v) \wedge \varphi(v, c)) \wedge \exists^\infty v\ (\theta(v) \wedge \neg \varphi(v, c)) : \theta \in p \}.
$$
If the elementary diagram of $M$ together with $r(c)$ were inconsistent, by compactness and since $p$ is closed under conjunction, some $\theta_0, \dots, \theta_n \in p$ would satisfy $M \models \forall z\ \bigvee_{i \leq n} \big( \forall^\infty v\ (\theta_i(v) \rightarrow \neg \varphi(v, z)) \vee \forall^\infty v\ (\theta_i(v) \rightarrow \varphi(v, z)) \big)$. Then $\theta = \bigwedge_i \theta_i \in p$ would witness strong definability for $\varphi$, since $\theta$ implies each $\theta_i$. So there is $K \succcurlyeq M$ with an element $c$ satisfying $r(c)$. In $K$, both $p \cup \{ v > e : e \in K \} \cup \{ \varphi(v, c) \}$ and the same set with $\neg \varphi(v, c)$ are finitely satisfied, by $r(c)$; they extend to two distinct unbounded extensions of $p$ to $K$.
:::

The unique unbounded extension of a strongly definable type is therefore its canonical extension, and the construction of :ref{#thm-ee-macdowell-specker} can be **iterated**. Let $p$ be an unbounded strongly definable $M$-type. Let $M_0 = M$; given $M_\alpha$, let $p_\alpha$ be the unique unbounded extension of $p$ to $M_\alpha$ and $M_{\alpha+1} = M_\alpha(p_\alpha / d_\alpha)$; at limits, take unions. By :ref{#prop-ee-one-gap} applied to each step, $M_\alpha$ is $M$ followed by the increasing sequence of gaps $\mathrm{gap}(d_\beta)$, $\beta < \alpha$.

## Exercises

::::exercise{#ex-ee-iterated-gaps difficulty=2 objective="Apply the one-gap proposition along an iterated construction to describe the models obtained."}
In the iterated construction, show that for every ordinal $\alpha$, $M_\alpha = M \cup \bigcup_{\beta < \alpha} \mathrm{gap}^{M_\alpha}(d_\beta)$, that these gaps are distinct, and that $\mathrm{gap}^{M_\alpha}(d_\beta) < \mathrm{gap}^{M_\alpha}(d_\gamma)$ for $\beta < \gamma$.

:::solution
By induction on $\alpha$. Each $M_\alpha$ is an elementary end extension of the previous ones (:ref{#cor-ee-definable-end}, and unions at limits). For $\alpha + 1$, :ref{#prop-ee-one-gap} gives $M_{\alpha+1} = M_\alpha \cup \mathrm{gap}^{M_{\alpha+1}}(d_\alpha)$, with the gap above $M_\alpha$. For $\beta < \alpha$, gaps are preserved by elementary extensions (remark after :ref{#lem-ee-gap-criterion}); and since $M_\alpha \subseteq_e M_{\alpha+1}$ and $\mathrm{gap}^{M_\alpha}(d_\beta)$ is bounded in $M_\alpha$ by Skolem functions of $d_\beta$, $\mathrm{gap}^{M_{\alpha+1}}(d_\beta) = \mathrm{gap}^{M_\alpha}(d_\beta)$. Limits are unions, and an element of $M_\lambda$ lies in some $M_\alpha$, $\alpha < \lambda$. The new gap lies above all previous ones since $d_\alpha > M_\alpha$, and gaps are convex.
:::
::::

::::exercise{#ex-ee-sd-preserved difficulty=1 objective="Check that strong definability passes to unbounded extensions of the type."}
Show that if $p$ is an unbounded strongly definable $M$-type and $K \succcurlyeq M$, every complete unbounded extension of $p$ to $K$ is strongly definable.

:::solution
For each $\varphi(v, z)$, the formula $\theta \in p$ given by strong definability satisfies a sentence with parameters in $M$, true in $M$, hence in $K$; and $\theta$ belongs to the extension. So the same $\theta$ witnesses strong definability over $K$.
:::
::::

## Notes and references

Skolem functions, the sets $M(d)$ and $M[d]$ and gaps follow Wong's Lecture 10 (Section 10.1, Lemma 10.3). :ref{#prop-ee-one-gap} is Gaifman's Proposition 4.8, Wong's Proposition 10.4, whose proof we follow. :ref{#thm-ee-unique-extension} is Gaifman's Theorem 2.10, Wong's Theorem 10.5. Strongly definable types correspond to P-points of the algebra of definable sets (Blass 1974), and the forcing reading of the construction, with definable unbounded sets as conditions, is discussed by Wong (Further reading to Lecture 10) and in Kirby's survey of ultrafilters and types.

- H. Gaifman, *Models and types of Peano's arithmetic*, Annals of Mathematical Logic 9 (1976), 223–306.
- A. Blass, *On certain types and models for arithmetic*, Journal of Symbolic Logic 39 (1974), 151–162.
- L. A. S. Kirby, *Ultrafilters and types on models of arithmetic*, Annals of Pure and Applied Logic 27 (1984), 215–252.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 10.

:::::exercises
::::exercise{#ex-ee-skolem-majorant difficulty=1 objective="Verify the closure properties of Skolem functions used to manipulate gaps."}
Let $t(v)$ and $s(v)$ be Skolem functions and $u(\bar v)$ a Skolem function of $k$ variables. Show that $s(t(v))$, $t^*(v) = \max_{w \leq v} t(w) + v + 1$ and $U(x) = \max_{\bar y \leq x} u(\bar y)$ are Skolem functions, that $t^*$ is strictly increasing with $t^* > t$, and that $u(\bar y) \leq U(\max \bar y)$.

:::solution
Let $\eta_t, \eta_s, \eta_u$ be the defining formulas. The composition is defined by $\exists y\ (\eta_t(v, y) \wedge \eta_s(y, x))$, and $\mathrm{PA}$ proves that for each $v$ there is exactly one such $x$. In $\mathrm{PA}$, a definable function on $\{ w : w \leq v \}$ is bounded there, by collection (:ref{#thm-fo-parsons}), and the least bound that is a value exists by the least number principle; so $\max_{w \leq v} t(w)$ is defined by a formula for which $\mathrm{PA}$ proves existence and uniqueness, and so is $U$, the tuples $\bar y \leq x$ being coded below a bound depending on $x$. Then $t^*(v + 1) \geq \max_{w \leq v} t(w) + v + 2 > t^*(v)$, and $t^*(v) \geq t(v) + v + 1 > t(v)$. Finally $u(\bar y)$ is one of the values in the maximum defining $U(\max \bar y)$.
:::
::::

::::exercise{#ex-ee-gap-cuts difficulty=2 objective="Show that the sets $K(d)$ and $K[d]$ are the elementary cuts that bound the gap of $d$."}
Let $K \models \mathrm{PA}$ and $d \in K$. An **elementary cut** of $K$ is an initial segment $I$ of $K$ with $I \preccurlyeq K$.

1. Show that $K(d)$ is the smallest elementary cut of $K$ that contains $d$.
2. Show that if $K[d] \neq \emptyset$, then $K[d]$ is the largest elementary cut of $K$ that does not contain $d$.

:::solution
Both sets are initial segments (remark after :ref{#def-ee-gap}). We use the Tarski–Vaught test; the least witness of $\exists y\ \varphi(y, \bar c)$, when there is one, is $w(\bar c)$ for the Skolem function $w(\bar z) = (\min y)\, \varphi(y, \bar z)$.

1. $d < d + 1$, so $d \in K(d)$. If $x < t(d)$ and $y < t'(d)$, then $x + y$ and $x y$ are below the Skolem function $(t(d) + t'(d))^2 + 1$ of $d$; so $K(d)$ is a substructure. Let $\bar c \in K(d)$, all below $t(d)$ for a single Skolem $t$ (take the maximum of finitely many), with $K \models \exists y\ \varphi(y, \bar c)$. With $W(x) = \max_{\bar z \leq x} w(\bar z)$ (:ref{#ex-ee-skolem-majorant}), $w(\bar c) \leq W(t(d)) < W(t(d)) + 1$, so the least witness is in $K(d)$. Hence $K(d) \preccurlyeq K$. If $I$ is an elementary cut containing $d$, then $t(d) \in I$ for every Skolem $t$, since the element defined by $\eta_t(d, x)$ in $I$ is the one defined in $K$; so every $x < t(d)$ is in $I$, and $K(d) \subseteq I$.
2. Since $K[d]$ is a non-empty initial segment, $0 \in K[d]$. If $x, y \in K[d]$ and $t$ is Skolem, then $t(x + y) \leq t'(\max(x, y))$ with $t'(m) = \max_{u \leq 2m} t(u)$, and $t'(\max(x, y)) < d$; similarly for $x y$, with $\max_{u \leq m^2} t(u)$. So $K[d]$ is a substructure. If $\bar c \in K[d]$ and $K \models \exists y\ \varphi(y, \bar c)$, then for every Skolem $t$, $t(w(\bar c)) \leq T(\max \bar c)$ with $T(x) = \max_{\bar z \leq x} t(w(\bar z))$, and $T(\max \bar c) < d$; so $w(\bar c) \in K[d]$, and $K[d] \preccurlyeq K$. It does not contain $d$, since the identity is a Skolem function. If $I$ is an elementary cut with $d \notin I$ and $x \in I$, then $t(x) \in I$ for every Skolem $t$, so $t(x) < d$, as $I$ is an initial segment not containing $d$; hence $x \in K[d]$.

These are the facts stated without proof in Wong's Lecture 10, Section 10.1.
:::
::::

::::exercise{#ex-ee-mp-gap-bound difficulty=1 objective="Show that an extension by an unbounded type is bounded by the Skolem functions of the realization."}
Let $M \models \mathrm{PA}$, $p(v)$ an unbounded complete $M$-type and $d$ a realization. Show that every element of $M(p / d)$ is below $t(d)$ for some Skolem function $t$, so that $M(p / d)$ is the smallest elementary cut of itself containing $d$. Show by an example that this fails for types that are not unbounded.

:::solution
By :ref{#lem-ee-mp}, an element of $M(p / d)$ is $u(\bar m, d)$ for a Skolem function $u$ and $\bar m \in M$, as in the remark after :ref{#def-ee-skolem}. Since $p$ is unbounded, $\bar m < d$, so $u(\bar m, d) \leq T(d)$ for the Skolem function $T(x) = \max_{\bar y \leq x} u(\bar y, x)$, and it is below $T(d) + 1$. By :ref{#ex-ee-gap-cuts}, the smallest elementary cut containing $d$ is $M(p/d)(d)$, which is therefore all of $M(p / d)$. For a counterexample, let $M$ be a non-standard model of $\mathrm{Th}(\nat)$, $a \in M$ non-standard, and $p = \mathrm{tp}(0 / M)$: then $M(p) = M$, and the elements below $t(0)$ for Skolem functions $t$ are the standard numbers (:ref{#ex-ee-gap-zero}), which do not include $a$. The first statement is a remark of Wong (Further comments to Lecture 10).
:::
::::

::::exercise{#ex-ee-gap-zero difficulty=2 objective="Characterize the gap of $0$ through the elements definable without parameters."}
Let $K \models \mathrm{PA}$. Show that $\mathrm{gap}(0) = K(0)$ is the set of elements below some element of $K$ definable without parameters, and that $K(0) = \nat$ if and only if $K \equiv \nat$.

:::solution
The identity is a Skolem function and $0 \not< 0$, so $K[0] = \emptyset$ and $\mathrm{gap}(0) = K(0)$. For a Skolem $t$, $t(0)$ is defined without parameters, by $\eta_t(0, x)$; conversely, an element $b$ defined by $\eta(x)$ without parameters is $t(0)$ for the Skolem function $t(v) = (\min x)\, \eta(x)$. So $K(0) = \{ x : x < b \text{ for some } b \text{ definable without parameters} \}$, and $K(0) = \nat$ if and only if every element definable without parameters is standard.

Suppose $K \equiv \nat$ and $b$ is defined by $\eta(x)$. Then $\exists! x\ \eta(x)$ holds in $K$, hence in $\nat$, at some $n$; and $\eta(\bar n)$ holds in $\nat$, hence in $K$, so $b = n$. Conversely, suppose that every element definable without parameters is standard. We show by induction on the number of quantifiers that every prenex sentence $\sigma$ of $\mathcal L_A$, possibly with numerals, has the same truth value in $K$ and in $\nat$. For quantifier-free sentences, both compute the same closed terms, since $\nat$ is a substructure of $K$. If $\sigma = \exists x\ \pi(x)$ holds in $K$, the least witness is definable without parameters, hence equal to some $n \in \nat$; then $K \models \pi(\bar n)$, so $\nat \models \pi(\bar n)$ by the induction hypothesis, and $\nat \models \sigma$. If $\nat \models \pi(\bar n)$, then $K \models \pi(\bar n)$ by the induction hypothesis. The case $\forall x\ \pi(x)$ follows by negation. So $K \equiv \nat$.
:::
::::

::::exercise{#ex-ee-iterated-cuts difficulty=2 objective="Determine the elementary cuts of a model obtained by iterating a strongly definable type."}
In the iterated construction at the end of the lesson, show that the elementary cuts of $M_\alpha$ that contain $M$ (in the sense of :ref{#ex-ee-gap-cuts}) are exactly the models $M_\gamma$, $\gamma \leq \alpha$.

:::solution
Each $M_\gamma$ contains $M$, is an elementary substructure of $M_\alpha$, and is an initial segment of it, since the construction is a chain of elementary end extensions (:ref{#ex-ee-iterated-gaps}). Conversely, let $I \supseteq M$ be an elementary cut of $M_\alpha$. If $c \in I$, then $K(c) \subseteq I$ by :ref{#ex-ee-gap-cuts}, computed in $M_\alpha$, so $\mathrm{gap}(c) \subseteq I$. By :ref{#ex-ee-iterated-gaps}, $I = M \cup \bigcup_{\beta \in B} \mathrm{gap}^{M_\alpha}(d_\beta)$ with $B = \{ \beta < \alpha : d_\beta \in I \}$. Since $I$ is an initial segment and $d_\beta < d_{\beta'}$ for $\beta < \beta'$, $B$ is an initial segment of $\alpha$, that is, an ordinal $\gamma \leq \alpha$. The elements of $\mathrm{gap}^{M_\alpha}(d_\beta)$, $\beta < \gamma$, are bounded by Skolem functions of $d_\beta \in M_\gamma$, so they lie in $M_\gamma$, an initial segment, and they form $\mathrm{gap}^{M_\gamma}(d_\beta)$. By :ref{#ex-ee-iterated-gaps} applied to $\gamma$, $I = M_\gamma$.
:::
::::
:::::
