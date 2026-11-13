---
title: Gaps and strongly definable types
summary: Skolem functions and the gaps of a model of PA; an extension by an unbounded strongly definable type adds exactly one gap; the canonical extension of definable types, and Gaifman's characterization of strongly definable types as the unbounded types with a unique unbounded extension to every elementary extension; iterated extensions.
duration: 45
prerequisites: [macdowell-specker]
---

The MacDowell–Specker theorem gives a proper elementary end extension $M(p)$ of a model $M$ of $\mathrm{PA}$. This lesson describes what the extension looks like. The natural unit of measure in a model of $\mathrm{PA}$ is the **gap**: two elements are in the same gap if each is below a definable function of the other. A realization $d$ of an unbounded type sits in a gap above $M$; and when the type is strongly definable, nothing else is added: $M(p)$ is $M$ followed by the single gap of $d$. Strong definability also has a characterization by uniqueness, due to Gaifman: a strongly definable type extends in exactly one unbounded way to every elementary extension, which allows the construction to be repeated along any ordinal.

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

The criterion is symmetric in $c$ and $d$. With the increasing majorants $t^*$, it shows that "being in the same gap" is an equivalence relation whose classes are the gaps: if $t(c) \geq d$ and $t'(d) \geq e$, then $t'^*(t^*(c)) \geq t'^*(d) \geq e$. Since the criterion only involves inequalities between values of Skolem functions, it is preserved by elementary extensions and substructures: if $K \preccurlyeq K'$ and $c, d \in K$, then $c \in \mathrm{gap}^K(d)$ if and only if $c \in \mathrm{gap}^{K'}(d)$. In $\nat$ there is a single gap; in a non-standard model, the standard part $\nat$ is contained in $K[d]$ for every non-standard $d$, and the gaps of non-standard elements are the blocks of elements that cannot be separated by definable functions.

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
<svg class="fig" viewBox="0 0 600 160" width="600" role="img" aria-label="The extension M(p/d) consists of M followed by the gap of d, between M[d] and the bound given by Skolem functions of d"><line x1="20.0" y1="70.0" x2="560.0" y2="70.0" class="ink-stroke" stroke-width="1.2"/><circle cx="24.0" cy="70.0" r="3.5" class="accent-fill"/><text x="24.0" y="56.0" text-anchor="middle" class="mrm" font-size="13">0</text><line x1="240.0" y1="48.0" x2="240.0" y2="92.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="240.0" y="40.0" text-anchor="middle" class="math" font-size="13">M = M(p)[d]</text><circle cx="330.0" cy="70.0" r="4.5" class="accent-fill"/><text x="330.0" y="56.0" text-anchor="middle" class="math" font-size="14">d</text><circle cx="290.0" cy="70.0" r="3" class="node"/><circle cx="380.0" cy="70.0" r="3" class="node"/><circle cx="440.0" cy="70.0" r="3" class="node"/><circle cx="500.0" cy="70.0" r="3" class="node"/><text x="540.0" y="56.0" text-anchor="middle" class="math" font-size="13">t(d)</text><line x1="540.0" y1="64.0" x2="540.0" y2="76.0" class="ink-stroke" stroke-width="1.4"/><path d="M22.0,88.0 L22.0,94.0 L236.0,94.0 L236.0,88.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="129.0" y="112.0" text-anchor="middle" class="label">M: below every Skolem function of d</text><path d="M246.0,88.0 L246.0,94.0 L556.0,94.0 L556.0,88.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="401.0" y="112.0" text-anchor="middle" class="label">gap(d): c ≤ s(d) and t(c) ≥ d</text></svg>
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

::::exercise{#ex-ee-iterated-gaps difficulty=2}
In the iterated construction, show that for every ordinal $\alpha$, $M_\alpha = M \cup \bigcup_{\beta < \alpha} \mathrm{gap}^{M_\alpha}(d_\beta)$, that these gaps are distinct, and that $\mathrm{gap}^{M_\alpha}(d_\beta) < \mathrm{gap}^{M_\alpha}(d_\gamma)$ for $\beta < \gamma$.

:::solution
By induction on $\alpha$. Each $M_\alpha$ is an elementary end extension of the previous ones (:ref{#cor-ee-definable-end}, and unions at limits). For $\alpha + 1$, :ref{#prop-ee-one-gap} gives $M_{\alpha+1} = M_\alpha \cup \mathrm{gap}^{M_{\alpha+1}}(d_\alpha)$, with the gap above $M_\alpha$. For $\beta < \alpha$, gaps are preserved by elementary extensions (remark after :ref{#lem-ee-gap-criterion}); and since $M_\alpha \subseteq_e M_{\alpha+1}$ and $\mathrm{gap}^{M_\alpha}(d_\beta)$ is bounded in $M_\alpha$ by Skolem functions of $d_\beta$, $\mathrm{gap}^{M_{\alpha+1}}(d_\beta) = \mathrm{gap}^{M_\alpha}(d_\beta)$. Limits are unions, and an element of $M_\lambda$ lies in some $M_\alpha$, $\alpha < \lambda$. The new gap lies above all previous ones since $d_\alpha > M_\alpha$, and gaps are convex.
:::
::::

::::exercise{#ex-ee-sd-preserved difficulty=1}
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
