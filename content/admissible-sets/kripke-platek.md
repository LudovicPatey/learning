---
title: Kripke–Platek set theory
summary: Δ₀ and Σ formulas; the axioms of Kripke–Platek set theory; Σ-reflection, Σ-collection and Δ-separation; definitions by Σ-recursion; absoluteness for transitive sets; admissible sets, and the c.e. relations as the Σ₁ relations over the hereditarily finite sets.
duration: 35
prerequisites: [computable-ordinals/ordinals, models-of-computation/church-turing-thesis]
---

Higher computability studies computation along the computable ordinals, and the hyperarithmetic sets play the role of the computable sets. Set theory provides a uniform setting for such generalizations: a computation is a definition by recursion along the membership relation, and a computably enumerable relation is a relation defined by an existential formula over a suitable universe of sets. Kripke and Platek isolated the weak set theory needed for this, now called **Kripke–Platek set theory**, KP. Its transitive models, the **admissible sets**, are universes in which recursion along $\in$ works; the smallest one is the set $\mathrm{HF}$ of hereditarily finite sets, over which the existential relations are exactly the c.e. relations. The next lessons show that the second smallest admissible set built by Gödel's constructible hierarchy is $L_{\omega_1^{\mathrm{CK}}}$, whose reals are the hyperarithmetic sets and over which the existential relations on numbers are the $\Pi^1_1$ sets.

This lesson works in the language of set theory, with the single relation symbol $\in$. Proofs inside KP are informal, as is usual in set theory.

## Δ₀ and Σ formulas

:::definition{#def-delta0-sigma}
The **$\Delta_0$ formulas** form the least class of formulas containing the atomic formulas $u \in v$ and $u = v$ and closed under $\neg$, $\wedge$, $\vee$ and the **bounded quantifiers** $(\exists u \in v)$ and $(\forall u \in v)$. The **$\Sigma$ formulas** form the least class containing the $\Delta_0$ formulas and closed under $\wedge$, $\vee$, bounded quantifiers and unbounded existential quantifiers $(\exists u)$. A **$\Sigma_1$ formula** is a formula $(\exists u)\, \varphi$ with $\varphi$ in $\Delta_0$; the $\Pi$ and $\Pi_1$ formulas are defined dually.
:::

$\Delta_0$ formulas play the role of primitive recursive predicates: their truth in a set is decided by inspecting finitely many of its elements, recursively. $\Sigma$ formulas play the role of c.e. predicates. Every $\Sigma_1$ formula is $\Sigma$; the converse holds in KP, by reflection below. For example, "$x$ is transitive", "$x$ is an ordinal" (a transitive set of transitive sets), "$f$ is a function", and "$x = \{ y, z \}$" are $\Delta_0$.

For a formula $\varphi$ and a set $w$, write $\varphi^{(w)}$ for the formula obtained by replacing every unbounded quantifier $(\exists u)$ or $(\forall u)$ of $\varphi$ by $(\exists u \in w)$ or $(\forall u \in w)$. It is $\Delta_0$, with the parameter $w$.

## The axioms

:::definition[Kripke, Platek]{#def-kp}
The theory **KP** consists of the universal closures of:

1. **Extensionality**: $(\forall u)(u \in x \leftrightarrow u \in y) \to x = y$;
2. **Foundation**: $(\exists x)\varphi(x) \to (\exists x)(\varphi(x) \wedge (\forall y \in x) \neg\varphi(y))$, for every formula $\varphi$;
3. **Pair**: $(\exists z)(x \in z \wedge y \in z)$;
4. **Union**: $(\exists y)(\forall u \in x)(\forall v \in u)(v \in y)$;
5. **$\Delta_0$-separation**: $(\exists y)(\forall u)(u \in y \leftrightarrow u \in x \wedge \varphi(u))$, for every $\Delta_0$ formula $\varphi$;
6. **$\Delta_0$-collection**: $(\forall u \in x)(\exists v)\varphi(u, v) \to (\exists y)(\forall u \in x)(\exists v \in y)\varphi(u, v)$, for every $\Delta_0$ formula $\varphi$.
:::

Compared with ZF, KP has no power set axiom, no infinity axiom, and separation and replacement are restricted to $\Delta_0$ formulas. Collection is the form of replacement that survives: if every element of $x$ has a witness, some set contains witnesses for all of them. Foundation is kept for all formulas, since it is the principle of induction along $\in$.

## Σ-reflection and its consequences

:::theorem[Σ-reflection]{#thm-sigma-reflection}
For every $\Sigma$ formula $\varphi$, KP proves $\varphi \leftrightarrow (\exists w)\, \varphi^{(w)}$. Moreover, if $\varphi^{(w)}$ holds and $w \subseteq w'$, then $\varphi^{(w')}$ holds.
:::

:::proof{of=thm-sigma-reflection}
We prove, by induction on the construction of the $\Sigma$ formula $\varphi$, the three statements: (a) $\varphi^{(w)} \wedge w \subseteq w' \to \varphi^{(w')}$; (b) $\varphi^{(w)} \to \varphi$; (c) $\varphi \to (\exists w)\varphi^{(w)}$.

(a) and (b) are clear for $\Delta_0$ formulas, which are unchanged by the relativization, and pass through $\wedge$, $\vee$ and bounded quantifiers, whose bounds are not relativized. For $(\exists u)\psi$: if $(\exists u \in w)\psi^{(w)}$, the same $u$ is in $w'$ and $\psi^{(w')}$ holds by (a) for $\psi$; and $\psi$ holds by (b) for $\psi$.

(c) For $\Delta_0$ formulas, any $w$ works. For $\psi_0 \wedge \psi_1$, take $w_0$ and $w_1$ given by (c) and $w = w_0 \cup w_1$, which exists by pair and union; (a) gives $\psi_i^{(w)}$. Disjunction and $(\exists u \in v)$ are similar. For $(\exists u)\psi$: take $u$ and $w_0$ with $\psi^{(w_0)}(u)$, and $w = w_0 \cup \{ u \}$; then $u \in w$ and $\psi^{(w)}(u)$ by (a). For $(\forall u \in v)\psi$: by the induction hypothesis, $(\forall u \in v)(\exists w)\psi^{(w)}(u)$, where $\psi^{(w)}(u)$ is $\Delta_0$ in $u$ and $w$. By $\Delta_0$-collection, there is $y$ with $(\forall u \in v)(\exists w \in y)\psi^{(w)}(u)$. Let $w' = \bigcup y$, which exists by union and $\Delta_0$-separation; by (a), $(\forall u \in v)\psi^{(w')}(u)$, which is $((\forall u \in v)\psi)^{(w')}$.
:::

Consequently, in KP every $\Sigma$ formula is equivalent to the $\Sigma_1$ formula $(\exists w)\varphi^{(w)}$. Reflection yields the strong forms of collection and separation that make KP a theory of computation.

:::corollary{#cor-sigma-collection}
1. **Σ-collection.** For every $\Sigma$ formula $\varphi$, KP proves: if $(\forall x \in a)(\exists y)\varphi(x, y)$, then there is $b$ with $(\forall x \in a)(\exists y \in b)\varphi(x, y)$ and $(\forall y \in b)(\exists x \in a)\varphi(x, y)$.
2. **Δ-separation.** For every $\Sigma$ formula $\varphi$ and $\Pi$ formula $\psi$, KP proves: if $(\forall x \in a)(\varphi(x) \leftrightarrow \psi(x))$, then $\{ x \in a : \varphi(x) \}$ is a set.
:::

:::proof{of=cor-sigma-collection}
1. The formula $(\forall x \in a)(\exists y)\varphi(x, y)$ is $\Sigma$, so by :ref{#thm-sigma-reflection} there is $c$ with $(\forall x \in a)(\exists y \in c)\varphi^{(c)}(x, y)$. Let $b = \{ y \in c : (\exists x \in a)\varphi^{(c)}(x, y) \}$, which exists by $\Delta_0$-separation. By (b) of the proof of reflection, $\varphi^{(c)}$ implies $\varphi$, so $b$ is as required.
2. The formula $(\forall x \in a)(\varphi(x) \vee \neg\psi(x))$ is equivalent to a $\Sigma$ formula and true, so it reflects to some $c$: $(\forall x \in a)(\varphi^{(c)}(x) \vee \neg\psi^{(c)}(x))$. Let $b = \{ x \in a : \varphi^{(c)}(x) \}$. If $x \in b$, then $\varphi(x)$. If $x \in a$ and $\varphi(x)$, then $\psi(x)$, and $\psi^{(c)}(x)$, since $\Pi$ formulas are downward persistent (the dual of (b)); so $\neg\psi^{(c)}(x)$ fails and $\varphi^{(c)}(x)$ holds, that is $x \in b$.
:::

## Σ-recursion

A class function $F$ is **$\Sigma$** (in KP) if there is a $\Sigma$ formula $\varphi(x, y)$ such that KP proves $(\forall x)(\exists! y)\varphi(x, y)$ and $F(x) = y$ is defined by $\varphi(x, y)$.

:::theorem[Σ-recursion]{#thm-sigma-recursion}
Let $G$ be a $\Sigma$ function of two arguments. There is a $\Sigma$ function $F$ such that KP proves, for every $y$,
$$
F(y) = G(y, \{ (z, F(z)) : z \in y \}).
$$
:::

:::proof{of=thm-sigma-recursion}
Say that $f$ is an **attempt** if $f$ is a function, its domain is transitive, and $f(y) = G(y, f \uh y)$ for every $y$ in its domain, where $f \uh y = \{ (z, f(z)) : z \in y \}$. This is a $\Sigma$ property of $f$. Let $F(y) = v$ if some attempt $f$ has $y$ in its domain and $f(y) = v$; this is $\Sigma$.

*Two attempts agree on their common domain.* Otherwise, by foundation, take an $\in$-minimal $y$ in both domains with $f_1(y) \neq f_2(y)$. Then $f_1 \uh y = f_2 \uh y$, since the domains are transitive, so $f_1(y) = G(y, f_1 \uh y) = f_2(y)$, a contradiction.

*Every $y$ is in the domain of some attempt.* Otherwise, by foundation, take an $\in$-minimal such $y$. Every $z \in y$ is in the domain of an attempt; by $\Sigma$-collection (:ref{#cor-sigma-collection}), there is a set $b$ of attempts covering all $z \in y$. By $\Delta$-separation and union, $f = \bigcup b$ is a set; it is a function by the first step, its domain is transitive, and it is an attempt. Then $f \cup \{ (y, G(y, f \uh y)) \}$ is an attempt with $y$ in its domain, a contradiction.
:::

The theorem is the set-theoretic form of effective transfinite recursion. For instance, the **rank** $\mathrm{rk}(x) = \sup \{ \mathrm{rk}(z) + 1 : z \in x \}$ and the **transitive closure** $\mathrm{TC}(x) = x \cup \bigcup \{ \mathrm{TC}(z) : z \in x \}$ are $\Sigma$ functions in KP.

## Admissible sets

:::definition{#def-admissible}
An **admissible set** is a transitive set $A$ such that $(A, \in)$ is a model of KP. Its **ordinal** $o(A)$ is the least ordinal not in $A$. An ordinal $\alpha$ is **admissible** if $\alpha = o(A)$ for some admissible set $A$.
:::

Truth in a transitive set is related to truth in the universe by **absoluteness**. If $A$ is transitive, then a $\Delta_0$ formula with parameters in $A$ holds in $A$ if and only if it holds in the universe, since its bounded quantifiers range over elements of elements of $A$, which are in $A$. Consequently, a $\Sigma_1$ formula true in $A$ is true in the universe (**upward absoluteness**), and a $\Pi_1$ formula true in the universe is true in $A$. These facts are proved by induction on formulas.

:::example{#ex-hf}
Let $\mathrm{HF}$ be the set of **hereditarily finite** sets, those with a finite transitive closure; $\mathrm{HF} = \bigcup_n V_n$, with $V_0 = \emptyset$ and $V_{n+1}$ the set of subsets of $V_n$. Then $\mathrm{HF}$ is admissible, with $o(\mathrm{HF}) = \omega$, and it is the smallest admissible set (:ref{#ex-hf-smallest}).
:::

:::theorem{#thm-hf-ce}
A relation $S \subseteq \nat^k$ is c.e. if and only if it is $\Sigma_1$-definable over $(\mathrm{HF}, \in)$, the numbers being identified with the finite ordinals.
:::

:::proof{of=thm-hf-ce}
The finite ordinals form a $\Delta_0$-definable subset of $\mathrm{HF}$, and addition and multiplication of finite ordinals are definable by $\Sigma_1$ formulas over $\mathrm{HF}$, by $\Sigma$-recursion; their graphs are also $\Pi_1$, since they are total functions. So every bounded arithmetic formula is equivalent over $\mathrm{HF}$ to a $\Delta_1$ formula, and a c.e. relation, of the form $(\exists i)\psi(i, m)$ with $\psi$ bounded, is $\Sigma_1$ over $\mathrm{HF}$.

Conversely, the map $f(2^{n_1} + \dots + 2^{n_k}) = \{ f(n_1), \dots, f(n_k) \}$, for distinct $n_i$, is a bijection from $\nat$ onto $\mathrm{HF}$ under which $\in$ becomes a computable relation, the code of the finite ordinal $m$ is computable from $m$, and every $\Delta_0$ formula becomes a computable relation, since bounded quantifiers range over finite, computably listed sets. A $\Sigma_1$ relation $(\exists u)\varphi(u, m)$ with $\varphi$ in $\Delta_0$ becomes $(\exists i)$ (computable relation), which is c.e.
:::

So KP over $\mathrm{HF}$ is ordinary computability. The following lessons lift this to the ordinals: the admissible sets of the constructible hierarchy, and in particular $L_{\omega_1^{\mathrm{CK}}}$, are the universes of generalized computations.

:::quiz[Kripke–Platek set theory]
In the proof of :ref{#thm-sigma-reflection}, where is $\Delta_0$-collection used?

- [x] For the bounded universal quantifier $(\forall u \in v)\psi$: each $u \in v$ has its own reflecting set $w$, and collection gathers them into one set $y$, whose union reflects $\psi$ for all $u$ simultaneously.
- [ ] For the unbounded existential quantifier $(\exists u)\psi$.

  There, one adds the witness $u$ to the reflecting set; no collection is needed.
- [ ] For conjunctions.

  Pair and union suffice to merge two reflecting sets.

---

In the proof of :ref{#thm-sigma-recursion}, why must the domains of attempts be transitive?

- [x] So that, for $y$ in the domain, the values $f(z)$ for $z \in y$ are defined, and the condition $f(y) = G(y, f \uh y)$ makes sense; it also lets the uniqueness argument compare $f_1 \uh y$ and $f_2 \uh y$.
- [ ] To make attempts sets.

  Attempts are sets by definition; transitivity concerns their domains.
- [ ] To apply $\Delta_0$-separation.

  Separation is used to form unions of attempts; it does not require transitivity.
:::

::::exercise[Σ-definable functions on sets]{#ex-sigma-image difficulty=2 objective="Use Σ-collection and Δ-separation to show that images of sets under Σ functions are sets."}
Let $F$ be a $\Sigma$ function in KP. Show that KP proves: for every set $a$, the image $F[a] = \{ F(x) : x \in a \}$ and the restriction $F \uh a = \{ (x, F(x)) : x \in a \}$ are sets.

:::solution
Let $\varphi(x, y)$ be a $\Sigma$ formula defining $F$. Since $(\forall x \in a)(\exists y)\varphi(x, y)$, $\Sigma$-collection (:ref{#cor-sigma-collection} (1)) gives $b$ with $(\forall x \in a)(\exists y \in b)\varphi(x, y)$ and $(\forall y \in b)(\exists x \in a)\varphi(x, y)$. Since $F$ is a function, $b = F[a]$. For the restriction, the pairs $(x, y)$ with $x \in a$, $y \in b$ form a set $c$ (built from $a$ and $b$ by pair, union and $\Delta_0$-separation). On $c$, the $\Sigma$ formula $\varphi(x, y)$ is equivalent to the $\Pi$ formula $(\forall y' )(\varphi(x, y') \to y' = y)$, by uniqueness and totality. By $\Delta$-separation (:ref{#cor-sigma-collection} (2)), $\{ (x, y) \in c : \varphi(x, y) \} = F \uh a$ is a set.
:::
::::

## Notes and references

Kripke (1964) and Platek (1966) introduced the theory independently, as a set-theoretic framework for recursion on admissible ordinals, which Kripke related to the recursion theory of Takeuti and Kreisel–Sacks. Barwise's monograph develops admissible sets systematically. The presentation follows Chong and Yu (Sections 3.1 and 3.2: Definition 3.1.4, Theorems 3.1.5–3.1.8, Proposition 3.1.17, Theorems 3.2.4 and 3.2.5); Chong and Yu leave the proof of $\Sigma$-reflection as an exercise, and prove $\Sigma$-recursion by a model-theoretic argument. Sacks (Chapter VII) treats $\Sigma_1$-admissibility for ordinals.

- S. Kripke, *Transfinite recursion on admissible ordinals*, abstracts, Journal of Symbolic Logic 29 (1964), 161–162.
- R. Platek, *Foundations of recursion theory*, PhD thesis, Stanford University, 1966.
- J. Barwise, *Admissible Sets and Structures*, Springer, 1975.
- C. T. Chong and L. Yu, *Recursion Theory: Computational Aspects of Definability*, De Gruyter, 2015, Sections 3.1 and 3.2.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Chapter VII.

:::::exercises
::::exercise{#ex-kp-delta0-examples difficulty=1 objective="Write elementary set-theoretic notions as Δ₀ formulas."}
Write $\Delta_0$ formulas expressing: $x$ is transitive; $x$ is an ordinal; $z = x \cup y$; $f$ is a function from $a$ to $b$; $x = \omega$ (the least non-zero limit ordinal).

:::solution
Transitive: $(\forall u \in x)(\forall v \in u)(v \in x)$. Ordinal: $x$ is transitive and $(\forall u \in x)(u \text{ is transitive})$, using foundation for the linear order. Union: $(\forall u \in z)(u \in x \vee u \in y) \wedge (\forall u \in x)(u \in z) \wedge (\forall u \in y)(u \in z)$. A pair $(u, v) = \{ \{ u \}, \{ u, v \} \}$ is $\Delta_0$-definable, and "$f$ is a function from $a$ to $b$" says that every element of $f$ is a pair $(u, v)$ with $u \in a$ and $v \in b$, the components being found inside the elements of the elements of $f$, and that $(\forall u \in a)$ there is exactly one such pair in $f$; all the quantifiers are bounded by $f$, $a$, $b$ or their elements. Finally $x = \omega$: $x$ is an ordinal, $x \neq \emptyset$, $x$ is a limit ($(\forall u \in x)(\exists v \in x)(u \in v)$), and every element of $x$ is $\emptyset$ or a successor ($(\forall u \in x)(u = \emptyset \vee (\exists v \in u)(u = v \cup \{ v \}))$).
:::
::::

::::exercise{#ex-sigma-upward difficulty=1 objective="Prove upward absoluteness of Σ formulas between transitive sets."}
Let $A \subseteq B$ be transitive sets, and $\varphi$ a $\Sigma$ formula with parameters in $A$. Show that if $A \models \varphi$, then $B \models \varphi$.

:::solution
By induction on $\varphi$. For $\Delta_0$ formulas, both $A$ and $B$ agree with the universe. Conjunction and disjunction are immediate. For $(\exists u \in v)\psi$ and $(\forall u \in v)\psi$ with $v \in A$, the elements of $v$ are the same in $A$ and $B$, since both are transitive, and the induction hypothesis applies to each. For $(\exists u)\psi$: a witness $u \in A$ belongs to $B$, and $B \models \psi(u)$ by induction. The universal unbounded quantifier is the only one that would break the argument, and $\Sigma$ formulas do not contain it.
:::
::::

::::exercise{#ex-v-omega-omega difficulty=2 objective="See why Δ₀-collection is the axiom that makes admissible sets closed under recursion."}
Show that $V_{\omega + \omega}$ satisfies all the axioms of KP except $\Delta_0$-collection, and that $\Delta_0$-collection fails in it.

:::solution
$V_\lambda$ is transitive for every limit $\lambda$, so extensionality and foundation hold; it contains $\{ x, y \}$ and $\bigcup x$ when it contains $x$ and $y$, and every subset of an element of $V_\lambda$ belongs to $V_\lambda$, so separation holds for all formulas.

Let $\varphi(n, v)$ say: $v$ is a function with domain $n \cup \{ n \}$, $v(0) = \omega$, and $v(i \cup \{ i \}) = v(i) \cup \{ v(i) \}$ for every $i \in n$. It is $\Delta_0$ with the parameter $\omega \in V_{\omega + \omega}$, and for each $n \in \omega$ its unique witness $v_n$, whose last value is $\omega + n$, is a finite set of pairs of ordinals below $\omega + n + 1$, so it belongs to $V_{\omega + \omega}$. So $V_{\omega + \omega} \models (\forall n \in \omega)(\exists v)\varphi(n, v)$. A set $y \in V_{\omega + \omega}$ containing witnesses for all $n$ would contain all the $v_n$; the rank of $v_n$ is at least $\omega + n$, so the rank of $y$ would be at least $\omega + \omega$, which is impossible for an element of $V_{\omega + \omega}$. So $\Delta_0$-collection fails, and $V_{\omega + \omega}$ is not admissible. Each stage of the recursion $n \mapsto \omega + n$ exists in $V_{\omega + \omega}$, but the recursion of length $\omega$ cannot be completed there: this is what collection provides in the proof of :ref{#thm-sigma-recursion}.
:::
::::

::::exercise[The smallest admissible set]{#ex-hf-smallest difficulty=2 objective="Check the axioms of KP on the hereditarily finite sets and show minimality."}
Show that $\mathrm{HF}$ is admissible, and that every non-empty admissible set contains $\mathrm{HF}$.

:::solution
$\mathrm{HF}$ is transitive. Extensionality and foundation hold in every transitive set, since $\in$ is well-founded. Pair and union hold, since $\{ x, y \}$ and $\bigcup x$ are hereditarily finite when $x$ and $y$ are. $\Delta_0$-separation holds because a subset of a finite set of hereditarily finite sets is hereditarily finite, and $\Delta_0$ formulas are absolute. For $\Delta_0$-collection, if every element of the finite set $x$ has a witness in $\mathrm{HF}$, the finite set of chosen witnesses is in $\mathrm{HF}$.

Let $A$ be admissible and non-empty. By $\Delta_0$-separation applied to any element of $A$ with the formula $u \neq u$, $\emptyset \in A$. If $x, y \in A$, then $x \cup \{ y \} \in A$: pair and $\Delta_0$-separation give $\{ y \} = \{ u \in z : u = y \}$ and then $\{ x, \{ y \} \}$, and union applied to it gives a superset of $x \cup \{ y \}$, from which $\Delta_0$-separation extracts $x \cup \{ y \}$. Every hereditarily finite set is obtained from $\emptyset$ by finitely many operations $x, y \mapsto x \cup \{ y \}$, by induction on the rank, so $\mathrm{HF} \subseteq A$.
:::
::::

::::exercise{#ex-sigma-not-pi difficulty=1 objective="See the difference between Σ and Π formulas through absoluteness."}
Let $A$ be a transitive set. Give a $\Pi_1$ formula $\varphi(x)$ and $x \in A$ such that $\varphi(x)$ holds in $A$ but not in the universe.

:::solution
Let $\varphi(x)$ be $(\forall y)\, \neg(x \in y)$, which says that $x$ is an element of no set. In the universe it fails for every $x$, since $x \in \{ x \}$. In the transitive set $A = \{ \emptyset \}$ it holds for $x = \emptyset$: the only element of $A$ is $\emptyset$, and $\emptyset \notin \emptyset$. So $\Pi_1$ formulas are not upward absolute.
:::
::::
:::::
