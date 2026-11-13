---
title: Automorphisms and fixed cuts
summary: Countable recursively saturated models of PA have non-trivial automorphisms; the largest initial segment fixed pointwise by an automorphism is closed under exponentiation; conversely, every exponential cut of a countable recursively saturated model of PA is the fixed cut of an automorphism (Smoryński), by a back-and-forth argument with bounded types and the pigeonhole principle.
duration: 45
prerequisites: [back-and-forth, cuts-and-extensions/weak-konig-cuts]
---

An automorphism of a model of arithmetic fixes every element definable without parameters, in particular every standard number. A model all of whose elements are definable, such as the model of :ref{#prop-rs-definable}, has only the identity as automorphism. Countable recursively saturated models are at the other extreme: by homogeneity (:ref{#cor-bf-homogeneous}), any two elements with the same type are exchanged by an automorphism. This lesson asks how much of the model an automorphism can fix. The answer, due to Smoryński, is that the initial segments fixed pointwise by automorphisms are exactly the cuts closed under exponentiation.

The proof is a back-and-forth argument in which the inductive condition is weaker than equality of types: the two tuples must have the same type over every element below a bound $b$, and $b$ decreases at each step while staying above the cut. The lemmas that extend the partial map are proved by coding the behavior of an element with respect to finitely many formulas and parameters below $a$ by a single element below $2^{a^2}$, a technique that recurs in the study of automorphisms.

Throughout, $M$ is a model of $\mathrm{PA}$. All definable sets are then piecewise coded, by :ref{#thm-friedman-coded} applied for every $n$.

## Non-trivial automorphisms

::::exercise{#ex-rs-same-type difficulty=1}
Let $M$ be a recursively saturated model of $\mathrm{PA}$ and $a \in M$ an element not definable without parameters. Show that some $b \neq a$ satisfies $\mathrm{tp}(b) = \mathrm{tp}(a)$.

:::solution
Consider the recursive type with parameter $a$
$$
q(v) = \{ v \neq a \} \cup \{ \theta(a) \leftrightarrow \theta(v) : \theta(x) \in \mathcal L_A \}.
$$
Given $\theta_1, \dots, \theta_k$, let $\eta(x)$ be the conjunction of the $\theta_j(x)$ true of $a$ and of the $\neg \theta_j(x)$ for the others. Then $M \models \eta(a)$, and $a$ is not the only element satisfying $\eta$, since it would be definable by $\eta$. So some $b \neq a$ satisfies the given formulas of $q$. By recursive saturation, $q$ is realized.
:::
::::

By :ref{#prop-rs-definable}, a recursively saturated model has an element not definable without parameters, and by :ref{#cor-bf-homogeneous} the exercise gives: **every countable recursively saturated model of $\mathrm{PA}$ has an automorphism other than the identity.**

:::definition{#def-ifix}
For an automorphism $g$ of $M$, $\mathrm{I_{fix}}(g) = \{ x \in M : g(y) = y \text{ for every } y \leq x \}$.
:::

It contains $0$ and is closed under successor, since $g(x + 1) = g(x) + 1$; so it is a cut (:ref{#def-cut}), containing $\nat$. It is $M$ if and only if $g$ is the identity.

:::proposition{#prop-ifix-exponential}
For every automorphism $g$ of $M$, the cut $\mathrm{I_{fix}}(g)$ is exponential: if $x \in \mathrm{I_{fix}}(g)$, then $2^x \in \mathrm{I_{fix}}(g)$.
:::

:::proof{of=prop-ifix-exponential}
Let $x \in \mathrm{I_{fix}}(g)$ and $y \leq 2^x$. Since $g$ preserves the formula $\varepsilon$ of :ref{#fact-exp}, $g(2^x) = 2^{g(x)} = 2^x$, so $g(y) \leq 2^x$. Both $y$ and $g(y)$ are below $2^{x+1}$, so their elements are below $x + 1$ (:ref{#lem-ack-basic}, item 3). For $i \leq x$, $g(i) = i$, and $g$ preserves the formula $i \in y$; so $i \in y$ if and only if $g(i) \in g(y)$, if and only if $i \in g(y)$. By extensionality (:ref{#lem-ack-basic}, item 5), $g(y) = y$. So every $y \leq 2^x$ is fixed, and $2^x \in \mathrm{I_{fix}}(g)$.
:::

By :ref{#ex-exp-cut-closed}, $\mathrm{I_{fix}}(g)$ is also closed under addition and multiplication.

## Types over a bounded part of the model

For tuples $\bar r, \bar s$ of the same length and $b \in M$, write $\bar r \equiv_b \bar s$ if $\mathrm{tp}(\bar r, x) = \mathrm{tp}(\bar s, x)$ for every $x < b$. If $b > 0$, then $\mathrm{tp}(\bar r) = \mathrm{tp}(\bar s)$, and $\bar r \equiv_{b'} \bar s$ for $b' \leq b$. If an automorphism maps $\bar r$ to $\bar s$ and fixes every element below $b$, then $\bar r \equiv_b \bar s$.

:::lemma[Kotlarski; Smoryński; Vencovská]{#lem-aut-extend}
Let $M$ be recursively saturated, $a \in M$ non-standard, and $\bar r \equiv_{2^{a^2}} \bar s$. For every $r \in M$ there is $s \in M$ with $(\bar r, r) \equiv_a (\bar s, s)$.
:::

The idea: the behavior of $r$ over $\bar r$ and the elements below $a$, for finitely many formulas, is a finite table of size about $a$, coded by an element below $2^{a^2}$; the hypothesis transfers the existence of an element with this table from $\bar r$ to $\bar s$.

:::proof{of=lem-aut-extend}
Consider the recursive type, with parameters $\bar r, \bar s, r, a$,
$$
p(v) = \{ \forall x < a\ \big( \theta(\bar r, r, x) \leftrightarrow \theta(\bar s, v, x) \big) : \theta(\bar u, w, x) \in \mathcal L_A \}.
$$
A realizer $s$ satisfies the conclusion. Let $\theta_0, \dots, \theta_{k-1}$ be formulas; we find $v$ satisfying the corresponding formulas of $p$. Since definable sets are piecewise coded, there is $c$ with
$$
\forall y < ka\ \Big( y \in c \leftrightarrow \exists x < a\ \exists i < k\ \big( y = kx + i \wedge \theta_i(\bar r, r, x) \big) \Big),
$$
and every element of $c$ below $ka$; so $c < 2^{ka}$ by :ref{#lem-ack-basic}, item 3. Let $\chi(\bar u, a, c)$ be the formula
$$
\exists w\ \forall x < a\ \textstyle\bigwedge_{i < k} \big( kx + i \in c \leftrightarrow \theta_i(\bar u, w, x) \big).
$$
It holds of $\bar r$, witnessed by $r$. Its parameters $a$ and $c$ are coded by the single element $\langle a, c \rangle \leq (a + c + 1)^2 \leq 2^{2ka + 2} < 2^{a^2}$, since $k$ is standard and $a$ is not. By $\bar r \equiv_{2^{a^2}} \bar s$, $\chi(\bar s, a, c)$ holds, witnessed by some $v$. For $x < a$ and $i < k$: $\theta_i(\bar s, v, x)$ if and only if $kx + i \in c$, if and only if $\theta_i(\bar r, r, x)$. By recursive saturation, $p$ is realized.
:::

The second lemma produces a moved point below any given element, by counting tables.

:::lemma[Smoryński]{#lem-aut-move}
Let $M$ be recursively saturated, $a \in M$ non-standard, $\bar r \equiv_{2^{a^2}} \bar s$, and $d \geq 2^{a^2}$. There are $r \neq s$ in $M$ with $r < d$ and $(\bar r, r) \equiv_a (\bar s, s)$.
:::

:::proof{of=lem-aut-move}
Consider the recursive type in two variables
$$
p(u, w) = \{ u < d,\ u \neq w \} \cup \{ \forall x < a\ \big( \theta(\bar r, u, x) \leftrightarrow \theta(\bar s, w, x) \big) : \theta \in \mathcal L_A \}.
$$
Given $\theta_0, \dots, \theta_{k-1}$, let $F(u)$, for $u < d$, be the code below $2^{ka}$ of the table of $u$, as in the previous proof: $kx + i \in F(u)$ if and only if $\theta_i(\bar r, u, x)$, for $x < a$, $i < k$. The map $F$ is definable, from $[0, d)$ into $[0, 2^{ka})$, and $2^{ka} < 2^{a^2} \leq d$. By induction on $\ell \leq d$, using concatenation (:ref{#prop-seq-basic}), some sequence of length $d$ lists the values of $F$; the finite pigeonhole principle of :ref{to="fragments-of-arithmetic/coding"} (last exercise), applied to its restriction to length $2^{ka} + 1$, gives $u_1 \neq u_2 < d$ with $F(u_1) = F(u_2) = c$. As in the previous proof, $\bar r \equiv_{2^{a^2}} \bar s$ gives $w$ whose table over $\bar s$ is $c$. Then $w$ differs from $u_1$ or from $u_2$, and that $u_j$, with $w$, satisfies the given formulas. By recursive saturation, applied to the one-variable type of the pair $\langle u, w \rangle$, $p$ is realized.
:::

:::quiz[the extension lemmas]
In :ref{#lem-aut-move}, why is $d \geq 2^{a^2}$ needed?

- [x] So that the definable map $F$ sends the $d$ elements below $d$ into fewer than $d$ codes of tables; by the pigeonhole principle, two elements have the same table, and one of them can be paired with a different element.
- [ ] So that the pair $\langle a, c \rangle$ is below $d$.

  The pair must be below the bound of the hypothesis $\bar r \equiv_{2^{a^2}} \bar s$; $d$ plays no role there.
- [ ] So that $r$ can be chosen non-standard.

  The lemma does not require $r$ to be non-standard.

---

Why does the conclusion of :ref{#lem-aut-extend} have the smaller bound $a$ instead of $2^{a^2}$?

- [x] The proof transfers a statement about the table of $r$ over the elements below $a$, whose code is below $2^{a^2}$; the hypothesis is used at the code, so the information obtained concerns only the elements below $a$.
- [ ] Because the type $p$ would not be recursive with the bound $2^{a^2}$.

  The bound is a parameter; $p$ is recursive for any bound.
- [ ] Because the bound must decrease for the construction to terminate.

  The construction has infinitely many steps; the bounds decrease, but must stay above the cut.
:::

## Smoryński's theorem

:::theorem[Smoryński]{#thm-smorynski}
Let $M$ be a countable recursively saturated model of $\mathrm{PA}$ and $I$ a cut of $M$. Then $I = \mathrm{I_{fix}}(g)$ for some automorphism $g$ of $M$ if and only if $I$ is exponential.
:::

:::proof{of=thm-smorynski}
($\Rightarrow$) :ref{#prop-ifix-exponential}.

($\Leftarrow$) If $I = M$, take the identity; assume $I \neq M$. *Choice of bounds.* For every $b \in M \setminus I$ there is $a \in M \setminus I$ with $2^{a^2} \leq b$: let $a$ be the largest element with $2^{a^2} \leq b$; if $a \in I$, then $(a + 1)^2$ and $2^{(a+1)^2}$ are in $I$, since $I$ is exponential and closed under multiplication (:ref{#ex-exp-cut-closed}), while $2^{(a+1)^2} > b \notin I$, which contradicts that $I$ is an initial segment.

*The construction.* Enumerate $M = \{ m_0, m_1, \dots \}$. We build tuples $\bar r_k, \bar s_k$, each extending the previous one, and $b_k \in M \setminus I$ with $\bar r_k \equiv_{b_k} \bar s_k$. Start with the empty tuples and any $b_0 \in M \setminus I$. At each step, take $a \notin I$ with $2^{a^2}$ below the current bound (and below $m_k$ in the third kind of step), apply a lemma, and let $a$ be the new bound:

- put $m_k$ in the domain, by :ref{#lem-aut-extend};
- put $m_k$ in the range, by :ref{#lem-aut-extend} with the roles of $\bar r$ and $\bar s$ exchanged, since $\equiv_b$ is symmetric;
- if $m_k \notin I$, add a pair $r \neq s$ with $r < m_k$, by :ref{#lem-aut-move} with $d = m_k$.

*The automorphism.* Let $g$ map the entries of $\bar r_k$ to those of $\bar s_k$. Since $\mathrm{tp}(\bar r_k) = \mathrm{tp}(\bar s_k)$, $g$ is a well-defined automorphism, total and surjective by the first two kinds of steps. If $x \in I$ and $x$ is the $i$-th entry of $\bar r_k$, then $x$ is below the bound $b_k \notin I$, and the formula $u_i = x$ belongs to $\mathrm{tp}(\bar r_k, x) = \mathrm{tp}(\bar s_k, x)$; so $g(x) = x$, and $I \subseteq \mathrm{I_{fix}}(g)$. If $m_k \notin I$, the third step moves an element below $m_k$, so $m_k \notin \mathrm{I_{fix}}(g)$. Hence $I = \mathrm{I_{fix}}(g)$.
:::

:::figure[Smoryński's theorem. The automorphism $g$ fixes every element of the exponential cut $I$; below every element above $I$, some element is moved. Each step of the construction keeps the two tuples of the same type over the elements below a bound $b$ above $I$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="An automorphism g fixing the exponential cut I pointwise and moving some element below every element above I"><defs><marker id="rs-sm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="20.0" y1="90.0" x2="580.0" y2="90.0" class="ink-stroke" stroke-width="1.2"/><circle cx="40.0" cy="90.0" r="3" class="muted-fill"/><path d="M34,84 C32,64 48,64 46,82" class="muted-stroke" fill="none" stroke-width="1"/><circle cx="80.0" cy="90.0" r="3" class="muted-fill"/><path d="M74,84 C72,64 88,64 86,82" class="muted-stroke" fill="none" stroke-width="1"/><circle cx="120.0" cy="90.0" r="3" class="muted-fill"/><path d="M114,84 C112,64 128,64 126,82" class="muted-stroke" fill="none" stroke-width="1"/><circle cx="160.0" cy="90.0" r="3" class="muted-fill"/><path d="M154,84 C152,64 168,64 166,82" class="muted-stroke" fill="none" stroke-width="1"/><circle cx="200.0" cy="90.0" r="3" class="muted-fill"/><path d="M194,84 C192,64 208,64 206,82" class="muted-stroke" fill="none" stroke-width="1"/><circle cx="240.0" cy="90.0" r="3" class="muted-fill"/><path d="M234,84 C232,64 248,64 246,82" class="muted-stroke" fill="none" stroke-width="1"/><line x1="280.0" y1="68.0" x2="280.0" y2="112.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="280.0" y="128.0" text-anchor="middle" class="math" font-size="14">I</text><circle cx="320.0" cy="90.0" r="3.5" class="accent-fill"/><circle cx="350.0" cy="90.0" r="3" class="node"/><path d="M320,83 Q335.0,50 350,82" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#rs-sm)"/><circle cx="400.0" cy="90.0" r="3.5" class="accent-fill"/><circle cx="380.0" cy="90.0" r="3" class="node"/><path d="M400,83 Q390.0,50 380,82" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#rs-sm)"/><circle cx="450.0" cy="90.0" r="3.5" class="accent-fill"/><circle cx="500.0" cy="90.0" r="3" class="node"/><path d="M450,83 Q475.0,50 500,82" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#rs-sm)"/><circle cx="540.0" cy="90.0" r="3.5" class="accent-fill"/><circle cx="520.0" cy="90.0" r="3" class="node"/><path d="M540,83 Q530.0,50 520,82" class="accent-stroke" fill="none" stroke-width="1.3" marker-end="url(#rs-sm)"/><text x="140.0" y="130.0" text-anchor="middle" class="label">below I: g(x) = x</text><text x="440.0" y="130.0" text-anchor="middle" class="label">above I: moved points below every element</text></svg>
:::

In particular, $\nat = \mathrm{I_{fix}}(g)$ for some automorphism $g$, which moves arbitrarily small non-standard elements. Exponentiation cannot be weakened to multiplication: for a non-standard $a$, the cut $\{ x : x < a^n \text{ for some } n \in \nat \}$ is closed under addition and multiplication, and not under exponentiation, since $a^n < 2^a$ for every standard $n$; it is the fixed cut of no automorphism.

## Exercises

::::exercise{difficulty=1}
Show that every automorphism of $M$ fixes every element definable in $M$ from fixed parameters, and deduce that the model of :ref{#prop-rs-definable} has no automorphism other than the identity.

:::solution
If $x$ is the only element satisfying $\varphi(x, \bar c)$ and $g(\bar c) = \bar c$, then $g(x)$ satisfies $\varphi(g(x), \bar c)$, so $g(x) = x$. In the model of :ref{#prop-rs-definable}, every element is definable without parameters.
:::
::::

::::exercise{difficulty=2}
Let $g$ be an automorphism of $M$. Show that the set $\{ x \in M : g(x) = x \}$ is an elementary substructure of $M$.

:::solution
Let $F$ be this set. It contains $0$ and $1$ and is closed under the operations, so it is a substructure. Apply the Tarski–Vaught test: if $M \models \exists y\ \varphi(y, \bar c)$ with $\bar c \in F$, the least such $y$ exists by the least number principle in $M$, and it is defined by $\varphi(y, \bar c) \wedge \forall z < y\ \neg \varphi(z, \bar c)$, with parameters in $F$; by the first exercise, it belongs to $F$.
:::
::::

## Notes and references

:ref{#thm-smorynski}, :ref{#lem-aut-extend} and :ref{#lem-aut-move} are Wong's Theorem 8.8 and Lemmas 8.9–8.10, after Smoryński (1982) and Kotlarski (1984); the lemma on extensions was found independently by Kotlarski, Smoryński and Vencovská. Kossak and Kotlarski (1988) characterized the automorphisms of an elementary cut $I$ of a countable recursively saturated model $M$ that extend to automorphisms of $M$, when $I$ is not the infimum of a coded ω-sequence: they are those that preserve $\mathrm{Cod}(M/I)$ in both directions (Wong, Theorem 8.11, proposed there as exercises). The automorphism groups of countable recursively saturated models are studied at length in Kossak and Schmerl's book.

- C. Smoryński, *Back-and-forth inside a recursively saturated model of arithmetic*, in Logic Colloquium '80, Studies in Logic and the Foundations of Mathematics 108, North-Holland, 1982, 273–278.
- H. Kotlarski, *On elementary cuts in recursively saturated models of Peano arithmetic*, Fundamenta Mathematicae 120 (1984), 205–222.
- R. Kossak and H. Kotlarski, *Results on automorphisms of recursively saturated models of PA*, Fundamenta Mathematicae 129 (1988), 9–15.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 8.
- R. Kossak and J. H. Schmerl, *The Structure of Models of Peano Arithmetic*, Oxford University Press, 2006.
