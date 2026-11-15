---
title: Forcing design for the free set theorem
summary: The design method for the free set theorem for pairs; optional and required properties; one of two candidates; limit patterns; cone avoidance; the case of triples.
duration: 45
prerequisites: [erdos-moser-hyperimmunities, reducibilities/preservation, ramsey-theorem/seetapun]
---

The free set theorem is a second example of the design method of :ref{to="separation-design/erdos-moser-design"}, with an invariant having several required clauses. For pairs, the conclusion also follows from Ramsey's theorem for pairs; the point is the design, which extends to all tuple sizes, where Ramsey's theorem codes the jump and the free set theorem does not.

## Free sets

Let $f : [\nat]^n \to \nat$. A set $H$ is **free** for $f$ if for every $\nu \in [H]^n$ with $f(\nu) \in H$, we have $f(\nu) \in \nu$. The **free set theorem** $\mathsf{FS}^n$ is the problem whose instances are the functions $f : [\nat]^n \to \nat$ and whose solutions are their infinite free sets. Subsets of free sets are free. A free set yields **thin** sets: if $H$ is free and $x \in H$, then $x \notin f[H \setminus \{ x \}]^n$ (:ref{#ex-fs-thin}). Cholak, Giusto, Hirst and Jockusch proved $\mathsf{FS}^2$ from $\mathsf{RT}^2_2$ (Hirschfeldt, *Slicing the Truth*, Theorem 9.35).

:::lemma{#lem-sd-fs1}
Every $f : \nat \to \nat$ has an infinite free set computable in $f$.
:::

:::proof{of=lem-sd-fs1}
If some value $v$ has an infinite preimage, $f^{-1}(v) \setminus \{ v \}$ is free: $f$ takes there the value $v$, which is not in it. Otherwise every preimage is finite, and we choose $h_0 = 0$ and $h_{m+1}$ the least $y > h_m$ larger than $f(h_0), \dots, f(h_m)$ with $f(y) \notin \{ h_0, \dots, h_m \}$; it exists since the preimages of $h_0, \dots, h_m$ are finite. If $f(h_j) = h_l$ with $j \neq l$, then $l < j$ is excluded by the choice of $h_j$, and $l > j$ by $h_l > f(h_j)$.
:::

Fix a set $Z$, a $Z$-computable $f : [\nat]^2 \to \nat$, and a class $\mathcal M$ of reservoirs; strings, compatibility and members are as for $\mathsf{EM}$ conditions. We write $f(a, b)$ for $f(\{ a, b \})$, and $f_a$ for the function $y \mapsto f(a, y)$.

## Step 1: extendibility

Let $(\sigma, X)$ be a Mathias condition with a free stem, and $Y \subseteq X$ infinite and free. A pair $\{ a, b \}$ of $\sigma \cup Y$ colored in $(\sigma \cup Y) \setminus \{ a, b \}$ falls, up to symmetry, in one of four cases:

1. $a, b \in \sigma$, $f(a, b) \in Y$: avoided by removing finitely many reservoir elements;
2. $a \in \sigma$, $b \in Y$, $f(a, b) \in Y$: avoided by restricting the reservoir to a free set for each $f_a$ (:ref{#lem-sd-fs1});
3. $a \in \sigma$, $b \in Y$, $f(a, b) \in \sigma$;
4. $a, b \in Y$, $f(a, b) \in \sigma$.

Cases 1 and 2 are **optional**; cases 3 and 4 are **required**: no restriction helps if almost every reservoir pair has its color in $\sigma$.

:::definition{#def-sd-fs-condition}
An **$\mathsf{FS}^2$ condition** is a pair $(\sigma, X)$ with $X \in \mathcal M$ infinite and $\min X \geq |\sigma|$, such that for every pair $\{ a, b \} \subseteq \sigma \cup X$:

(a) if $a \in \sigma$, then $f(a, b) \notin X \setminus \{ b \}$;

(b) $f(a, b) \notin \sigma \setminus \{ a, b \}$.
:::

Property (b) for pairs in $\sigma$ says that $\sigma$ is free. If $Y \subseteq X$ is infinite and free, then $\sigma \cup Y$ is free: a color in $\sigma$ is excluded by (b); a color in $Y$ of a pair meeting $\sigma$ is excluded by (a), since $Y \subseteq X$ (for a pair inside $\sigma$, (a) excludes all of $X$); and pairs inside $Y$ are handled by freeness of $Y$. Both properties pass to subsets of the reservoir.

Adding one element $x \in X$ to the stem endangers (b) through the pairs of reservoir elements colored $x$, which is case 4 for the new stem. Ramsey's theorem for triples would give a reservoir avoiding the color $x$ or consisting of pairs colored $x$; with two candidates, Ramsey's theorem for pairs suffices.

:::lemma{#lem-sd-fs-extension}
Let $\mathcal M$ be a Turing ideal containing $Z$ such that every coloring $c : [\nat]^2 \to 2$ in $\mathcal M$ has an infinite homogeneous set in $\mathcal M$. For every $\mathsf{FS}^2$ condition $(\sigma, X)$ and distinct $x_0, x_1 \in X$, there are $i < 2$ and an extension of $(\sigma, X)$ with stem $\sigma \cup \{ x_i \}$.
:::

:::proof{of=lem-sd-fs-extension}
Let $c(\{ a, b \}) = 1$ if $f(a, b) = x_1$ and $0$ otherwise, on pairs of $X' = X \setminus [0, \max(x_0, x_1)]$, and let $H \subseteq X'$ be infinite, homogeneous and in $\mathcal M$. If its color is $1$, no pair of $H$ is colored $x_0$; let $i = 0$. Otherwise no pair of $H$ is colored $x_1$; let $i = 1$. Let $Y \subseteq H$ be an infinite free set for $f_{x_i}$, in $\mathcal M$ by :ref{#lem-sd-fs1}, minus the finitely many colors of pairs of $\sigma \cup \{ x_i \}$. Property (a) for $(\sigma \cup \{ x_i \}, Y)$ holds for $a \in \sigma$ since $Y \subseteq X$, and for $a = x_i$ by the choice of $Y$. For (b), a color in $\sigma$ is excluded by (b) for $(\sigma, X)$. A pair $\{ a, b \}$ colored $x_i \notin \{ a, b \}$ cannot have an element in $\sigma$, by (a) for $(\sigma, X)$, since $x_i \in X$; nor lie in $Y$, by the choice of $i$.
:::

## Step 2: block extendibility

A free block $\rho \subseteq X$ added to the stem breaks (b) if a pair $\{ a, y \}$, with $a \in \rho$ and $y$ in the future reservoir, or a pair of future elements, is colored by an element of $\rho$ outside the pair. What matters is the **limit behavior** of the coloring on the elements below a bound $k$: the colors below $k$ taken by the pairs of the future reservoir, and, for each $a < k$, by the pairs $\{ a, y \}$.

:::definition{#def-sd-fs-stabilize}
A **limit pattern** is a pair $g = (g_\emptyset, (g_a)_{a \in \nat})$ of sets of at most one element each. An infinite set $Y$ **stabilizes** $[0, k)$ with the pattern $g$ if $f[Y]^2 \cap [0, k) \subseteq g_\emptyset$ and, for every $a < k$, $f_a[Y] \cap [0, k) \subseteq g_a$. A finite set $\rho$ is **$g$-free** if $g_\emptyset \cap \rho = \emptyset$ and $g_a \cap \rho \subseteq \{ a \}$ for every $a \in \rho$.
:::

If $\mathcal M$ is as in :ref{#lem-sd-fs-extension} and also closed under $\mathsf{RT}^2_k$ for every $k$, every $X \in \mathcal M$ contains an infinite $Y \in \mathcal M$, above $k$, stabilizing $[0, k)$: color each pair of $X \setminus [0, k)$ by its color if it is below $k$, and by $k$ otherwise, and take a homogeneous set; then for each $a < k$ in turn, apply the pigeonhole principle to $f_a$ capped at $k$. 

:::lemma{#lem-sd-fs-block}
Let $(\sigma, X)$ be an $\mathsf{FS}^2$ condition, $Y \subseteq X \setminus [0, k)$ an infinite set stabilizing $[0, k)$ with a pattern $g$, and $\rho \subseteq X \cap [0, k)$ a free and $g$-free set. Then $(\sigma \cup \rho, Y)$ satisfies (b).
:::

:::proof{of=lem-sd-fs-block}
Let $\{ a, b \} \subseteq \sigma \cup \rho \cup Y$ have a color $r \in (\sigma \cup \rho) \setminus \{ a, b \}$. If $r \in \sigma$, this contradicts (b) for $(\sigma, X)$. So $r \in \rho$. If $a \in \sigma$, then $r \in X \setminus \{ b \}$ contradicts (a) for $(\sigma, X)$. If $a, b \in \rho$, it contradicts freeness of $\rho$. If $a \in \rho$ and $b \in Y$, then $r = f_a(b) < k$, so $r \in g_a \cap \rho \subseteq \{ a \}$, a contradiction. If $a, b \in Y$, then $r \in f[Y]^2 \cap [0, k) \subseteq g_\emptyset$, and $g_\emptyset \cap \rho = \emptyset$.
:::

Property (a) is then restored by restricting $Y$ to a free set for each $f_a$, $a \in \rho$, and removing finitely many colors. The pattern of a future reservoir is unknown, so the question quantifies over all patterns. The patterns form a compact space: coded as a subset of $\nat \cup \nat^2$, a pattern is a set whose sections have at most one element, a $\Pi^0_1$ condition; and $g$-freeness of $\rho$ depends only on the finitely many bits $g_\emptyset \cap \rho$ and $g_a \cap \rho$, $a \in \rho$.

:::lemma{#lem-sd-fs-question}
Let $\mathcal M$ be a Scott ideal containing $Z$ and closed under $\mathsf{RT}^2_k$ for every $k$. For an $\mathsf{FS}^2$ condition $c = (\sigma, X)$ and a $\Sigma^0_1$ sentence $\varphi$, let $c \mathrel{?{\vdash}} \varphi$ hold if for every pattern $g$ there is a string $\tau$ compatible with $(\sigma, X)$, whose new elements form a free and $g$-free set, satisfying $\varphi$. Then the relation is $\Sigma^0_1(X \oplus Z)$, and if $c \mathrel{?{\vdash}} \varphi$, some extension forces $\varphi$; otherwise some extension forces $\neg \varphi$.
:::

:::proof{of=lem-sd-fs-question}
*Complexity.* As in the proof of :ref{#lem-sd-em-question}, the finite approximations of patterns without a witness of length and convergence time bounded by their size form a tree computable in $X \oplus Z$, finite if and only if the answer is positive.

*Positive answer.* There is $\ell \geq |\sigma|$ such that for every pattern a witness $\tau$ has $|\tau| \leq \ell$. Let $Y \in \mathcal M$ stabilize $[0, \ell)$ inside $X$, with a pattern $g$, and let $\tau$ be a witness for $g$, with new elements $\rho \subseteq X \cap [0, \ell)$. By :ref{#lem-sd-fs-block}, $(\tau, Y)$ satisfies (b); restricting $Y$ as above gives a condition, whose members extend $\tau$ and satisfy $\varphi$.

*Negative answer.* The patterns without witness form a non-empty $\Pi^0_1(X \oplus Z)$ class, so one of them, $g$, belongs to $\mathcal M$. Let $Y_0 = X \setminus g_\emptyset$, and let $Y \subseteq Y_0$ be infinite and free for the function equal on $a$ to the element of $g_a$ if there is one, and to $a$ otherwise (:ref{#lem-sd-fs1}); $Y \in \mathcal M$, and every finite subset of $Y$ is $g$-free. The condition $(\sigma, Y)$ forces $\neg \varphi$: a member satisfying $\varphi$ would give a compatible string satisfying $\varphi$, with new elements in $Y$, hence $g$-free, and free since the member is free; a witness for $g$.
:::

:::quiz[the free set question]
Why does the question quantify over all patterns, rather than use the pattern of the reservoir $X$ itself?

- [x] Because $X$ need not stabilize any interval, and the pattern of a stabilizing subset depends on the bound and on choices made with $\mathsf{RT}^2_k$; quantifying over the compact space of patterns keeps the question $\Sigma^0_1(X \oplus Z)$.
- [ ] Because patterns are infinite objects.

  Only finitely many bits matter; the issue is that they are unknown.
- [ ] Because $X$ is not free.

  Freeness of the reservoir is never required.

:::

## Step 3: computational properties

The operations on reservoirs are restrictions, free sets (computably true by :ref{#lem-sd-fs1}), homogeneous sets for colorings of pairs with finitely many colors, and members of $\Pi^0_1$ classes, relative to $X \oplus Z$. So $\mathcal M$ must be a Scott ideal containing $Z$ closed under every $\mathsf{RT}^2_k$. For a weakness property preserved by $\mathsf{WKL}$ and by every $\mathsf{RT}^2_k$, the construction of :ref{#lem-preservation-ideal}, dovetailing instances of all these problems, gives such an ideal inside the property.

:::theorem{#thm-sd-fs2-cone}
$\mathsf{FS}^2$ admits cone avoidance.
:::

:::proof{of=thm-sd-fs2-cone}
Let $C \not\leq_T Z$, and $\mathcal W_C = \{ W : C \not\leq_T W \}$. It is preserved by $\mathsf{WKL}$ (:ref{#thm-cone-avoidance-basis}) and by $\mathsf{RT}^2_2$ (:ref{#thm-seetapun}), hence by every $\mathsf{RT}^2_k$: for a coloring with $k + 1$ colors, a homogeneous set $H$ for "color $0$ or not", avoiding the cone together with $Z$, either has color $0$ or carries a $(Z \oplus H)$-computable coloring with $k$ colors, and induction applies relative to $Z \oplus H$. Let $\mathcal M \subseteq \mathcal W_C$ be an ideal as in step 3, containing $Z$. Build a sequence of $\mathsf{FS}^2$ conditions from $(\varepsilon, \nat)$, with :ref{#lem-sd-fs-extension} for growth and the three-case argument of :ref{#thm-sd-em-cone} with the question of :ref{#lem-sd-fs-question} for each functional. The union of the stems is infinite, free, a member of every condition, and does not compute $C$ together with $Z$.
:::

## Triples and beyond

For $f : [\nat]^3 \to \nat$, the analysis gives six cases; the optional ones are avoided by $\mathsf{FS}^1$ and $\mathsf{FS}^2$ for $f_{a,b}$ and $f_a$, and adding an element or stabilizing $[0, k)$ needs colorings of triples. Ramsey's theorem for triples cannot be used, since it codes $\emptyset'$ (:ref{#prop-rt32-jump}). One uses instead the thin set theorems $\mathsf{RT}^3_{<\infty, \ell}$: every coloring of triples with finitely many colors has an infinite set on which at most $\ell$ colors appear. With $\ell + 1$ candidates, one of them is missed; patterns have at most $\ell$ elements. Wang proved that for $\ell$ large enough, $\mathsf{RT}^n_{<\infty, \ell}$ admits cone avoidance, and deduced by this induction on $n$ that every $\mathsf{FS}^n$ admits strong cone avoidance; Cholak and Patey determined the optimal $\ell$, a Catalan number. These results are admitted; so $\mathsf{FS}^3$ is strictly weaker than $\mathsf{ACA}_0$, while $\mathsf{RT}^3_2$ is equivalent to it.

::::exercise{#ex-fs-thin difficulty=1 objective="Derive thin sets from free sets."}
Let $f : [\nat]^n \to \nat$ and $H$ be an infinite free set for $f$. Show that for every $x \in H$, the color $x$ does not appear on $[H \setminus \{ x \}]^n$. Deduce that $\mathsf{FS}^n$ implies the thin set theorem for $n$-tuples, whose solutions are the infinite sets $H$ with $f[H]^n \neq \nat$.

:::solution
If $\nu \in [H \setminus \{ x \}]^n$ had $f(\nu) = x$, then $f(\nu) \in H$ and freeness would give $x \in \nu$, which is false. So $f[H \setminus \{ x \}]^n \neq \nat$, and $H \setminus \{ x \}$ is an infinite thin set computable in $H$.
:::
::::

## Notes and references

The design follows the section *Free set theorem* of the chapter *Forcing design* of Patey's monograph, which treats triples; pairs are treated here because all the ingredients are proved in the platform. Free sets were introduced by Friedman (FOM, 1999) and studied by Cholak, Giusto, Hirst and Jockusch (2005); Wang (2014) proved strong cone avoidance for every $\mathsf{FS}^n$, and Cholak and Patey (2020) found the exact thresholds for the thin set theorems.

- L. Patey, *Lowness and avoidance*, chapter *Forcing design*, section *Free set theorem*.
- P. A. Cholak, M. Giusto, J. L. Hirst and C. G. Jockusch, Jr., *Free sets and reverse mathematics*, in *Reverse Mathematics 2001*, Lecture Notes in Logic 21, Association for Symbolic Logic, 2005, 104–119.
- W. Wang, *Some logically weak Ramseyan theorems*, Advances in Mathematics 261 (2014), 1–25.
- P. A. Cholak and L. Patey, *Thin set theorems and cone avoidance*, Transactions of the American Mathematical Society 373 (2020), 2743–2773.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 9.8.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Section 9.2.3.

:::::exercises
::::exercise{#ex-fs-examples difficulty=1 objective="Find free sets for explicit functions, and run the construction of the free set theorem for singletons."}
1. Let $f(\{ x, y \}) = x + y$. Show that the set of powers of $2$ is free for $f$.
2. Let $f(\{ x, y \}) = |x - y|$. Show that the set of powers of $3$ is free for $f$.
3. Let $f(x) = x + 1$. Compute the free set built in the proof of :ref{#lem-sd-fs1}.

:::solution
1. For $a < b$, $2^a + 2^b = 2^a (1 + 2^{b-a})$, and $1 + 2^{b-a}$ is odd and larger than $1$, so the sum is not a power of $2$. So no pair of the set has its color in the set, and the set is free.
2. For $a < b$, $3^b - 3^a = 3^a (3^{b-a} - 1)$, and $3^{b-a} - 1$ is at least $2$ and congruent to $2$ modulo $3$, so it is not a power of $3$, and neither is the difference. The set is free for the same reason.
3. Every preimage has at most one element, so the second case applies. We show that $h_m = 2m$ by induction: $h_0 = 0$, and $h_{m+1}$ is the least $y > 2m$ larger than $f(h_0), \dots, f(h_m)$, whose maximum is $2m + 1$, with $f(y) \notin \{ 0, 2, \dots, 2m \}$; $y = 2m + 2$ qualifies, since $f(2m + 2)$ is odd. The free set is the set of even numbers: $f$ maps it to odd numbers.
:::
::::

::::exercise{#ex-fs-one-candidate difficulty=1 objective="See on an example why two candidates are needed to add an element to the stem of an $\mathsf{FS}^2$ condition."}
Let $f(\{ a, b \}) = 0$ for every pair. Show that $(\varepsilon, \nat)$ is an $\mathsf{FS}^2$ condition, that no extension of it has $0$ in its stem, and determine the extension given by :ref{#lem-sd-fs-extension} for $x_0 = 0$ and $x_1 = 1$.

:::solution
The stem is empty, so (a) and (b) hold. Let $(\tau, Y)$ be an extension with $0 \in \tau$. For $a < b$ in $Y$, $f(a, b) = 0 \in \tau \setminus \{ a, b \}$, since $\min Y \geq |\tau| > 0$; this violates (b). In the proof of the lemma, $c(\{ a, b \}) = 1$ if and only if $f(a, b) = x_1 = 1$, which never holds; so $H$ has color $0$, no pair of $H$ is colored $1$, and $i = 1$. The function $f_1$ is constantly $0$, so every subset of $H$ is free for $f_1$, and the extension is $(\{ 1 \}, Y)$ with $Y \subseteq \{ y : y \geq 2 \}$ infinite. One checks (a): $f(1, b) = 0 \notin Y$; and (b): no color equals $1$. The infinite free sets for $f$ are exactly the infinite sets not containing $0$.
:::
::::

::::exercise{#ex-fs-hyperimmunity difficulty=2 objective="Prove that $\mathsf{FS}^2$ preserves one hyperimmunity with its forcing question, and locate the obstacle to two."}
1. Show that $\mathsf{FS}^2$ admits preservation of hyperimmunity, with the conditions and the question of this lesson.
2. Let $h_0, h_1$ be as in :ref{#prop-sd-rt22-two}. Show that no Turing ideal $\mathcal M$ closed under $\mathsf{RT}^2_2$ consists of sets $X$ such that $h_0$ and $h_1$ are $X$-hyperimmune. Which step of the argument of item 1 fails for two hyperimmunities?

:::solution
1. Let $h$ be $Z$-hyperimmune and $\mathcal W$ the class of sets $W$ such that $h$ is $W$-hyperimmune. It is preserved by $\mathsf{WKL}$ and $\mathsf{RT}^2_2$ (:ref{#thm-hyperimmunity-examples}), hence by every $\mathsf{RT}^2_k$, by the induction on $k$ of the proof of :ref{#thm-sd-fs2-cone}. As in step 3, there is a Scott ideal $\mathcal M \subseteq \mathcal W$ containing $Z$ and closed under every $\mathsf{RT}^2_k$. The question of :ref{#lem-sd-fs-question} is compact: if $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge$, the proof of its complexity gives $\ell$ such that every pattern has a witness $\tau$ with $|\tau| \leq \ell$ and $\Phi^{Z \oplus \tau}_e(x)[\ell]\converge$; for $k$ larger than all these values, the same witnesses show $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge < k$. Now build a sequence of $\mathsf{FS}^2$ conditions with reservoirs in $\mathcal M$, with :ref{#lem-sd-fs-extension} for growth and, for each $e$, the task of the proof of :ref{#thm-sd-em-hyperimmunities}: either some $x$ has a negative answer, and an extension forces divergence at $x$, or the bounds $k$ define a total $(X \oplus Z)$-computable function $g$, some $x$ has $g(x) < h(x)$, and an extension forces $\Phi^{Z \oplus G}_e(x) < g(x)$. The union of the stems is an infinite free set $G$ such that $h$ is $(Z \oplus G)$-hyperimmune.
2. The computable coloring $f$ of :ref{#prop-sd-rt22-two} would belong to $\mathcal M$, together with an infinite homogeneous set $H$; but $h_0$ or $h_1$ is not $H$-hyperimmune. The question is not disjunctive, so the forcing part of item 1 handles any number of functions; what fails is step 3, the existence of reservoirs: the design uses $\mathsf{RT}^2_2$ on the reservoirs.
:::
::::

::::exercise{#ex-fs-friedman difficulty=2 objective="Derive the free set theorem for pairs from Ramsey's theorem for triples with four colors, following Friedman."}
Let $f : [\nat]^2 \to \nat$. For $a_1 < a_2 < a_3$, let $g(\{ a_1, a_2, a_3 \})$ be the least $i \in \{ 1, 2, 3 \}$ such that $f(\{ a_j : j \neq i \}) = a_i$, and $0$ if there is none. Show that every infinite set homogeneous for $g$ is free for $f$. Deduce $\mathsf{FS}^2 \leq_c \mathsf{RT}^3_4$, and explain why this does not give cone avoidance.

:::solution
Let $H$ be infinite and homogeneous for $g$ with color $i$. Suppose $i \geq 1$. Choose in $H$ elements $a_j$ for $j < i$, then $b < c$ above them, then elements $a_j$ for $i < j \leq 3$ above $c$. The triples obtained with $b$ and with $c$ in position $i$ both have color $i$, so $f(\{ a_j : j \neq i \}) = b$ and $= c$, a contradiction. So $i = 0$. Let $\nu = \{ x, y \} \subseteq H$ with $f(\nu) = z \in H$ and $z \notin \nu$. In the increasing enumeration of $\{ x, y, z \}$, $z$ is at some position $i$, and $f$ of the two other elements is $z$; so $g(\{ x, y, z \}) \neq 0$, a contradiction. So $H$ is free. The coloring $g$ is computable in $f$, and its infinite homogeneous sets are solutions, so $\mathsf{FS}^2 \leq_c \mathsf{RT}^3_4$. Ramsey's theorem for triples does not admit cone avoidance, since some computable coloring of triples has all its homogeneous sets computing $\emptyset'$ (:ref{#prop-rt32-jump}); this is why the lesson designs a forcing for $\mathsf{FS}^2$ itself. Adapted from Hirschfeldt, *Slicing the Truth*, the argument of Friedman after Exercise 9.33.
:::
::::

::::exercise{#ex-fs-downward difficulty=1 objective="Show by padding that free sets for $(n+1)$-tuples give free sets for $n$-tuples."}
Let $n \geq 1$ and $f : [\nat]^n \to \nat$, and let $f'(\nu) = f(\nu \setminus \{ \max \nu \})$ for $\nu \in [\nat]^{n+1}$. Show that every infinite free set for $f'$ is free for $f$. Deduce that $\mathsf{FS}^{n+1}$ implies $\mathsf{FS}^n$ on Turing ideals.

:::solution
Let $H$ be infinite and free for $f'$, and $\nu \in [H]^n$ with $f(\nu) \in H$. Choose $a \in H$ larger than $\max \nu$ and than $f(\nu)$. Then $f'(\nu \cup \{ a \}) = f(\nu) \in H$, so $f(\nu) \in \nu \cup \{ a \}$ by freeness, and $f(\nu) \neq a$ since $f(\nu) < a$. So $f(\nu) \in \nu$. Since $f'$ is computable in $f$, a Turing ideal satisfying $\mathsf{FS}^{n+1}$ satisfies $\mathsf{FS}^n$. Adapted from Hirschfeldt, *Slicing the Truth*, Exercise 9.33(c).
:::
::::
:::::
