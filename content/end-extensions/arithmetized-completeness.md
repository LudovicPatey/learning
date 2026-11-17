---
title: The arithmetized completeness theorem
summary: Provability and consistency inside a model of IΣ₁; Henkin's proof of the completeness theorem carried out in the model, with a path through the tree of completions given by the low basis theorem; a theory consistent in M has a model that is an end extension of M, with an elementary diagram Δ₂-definable in M.
duration: 40
prerequisites: [low-basis-isigma1, truth-and-provability/bounded-satisfaction, pi01-classes/pa-degrees]
---

Henkin's proof of the completeness theorem is finite combinatorics on proofs, and it can be carried out inside a model $M$ of arithmetic. If $M$ believes that a theory $T$ is consistent, $M$ completes $T$ along a path through the tree of completions and reads off a term model. Seen from outside, it is a structure $K$ satisfying every standard axiom of $T$. What makes it a tool for building models of arithmetic is that $K$ contains $M$ as an initial segment: the numerals of $M$ name elements of $K$, and $M$ knows that every element below a numeral $\bar a$ equals one of $\bar 0, \dots, \overline{a - 1}$. This is the **arithmetized completeness theorem**. The low basis theorem of the previous lesson gives it in $\mathrm I\Sigma_1$, with a model whose diagram is $\Delta_2$-definable in $M$.

## Provability inside a model

Throughout, $M$ is a model of $\mathrm I\Sigma_1$, and $\mathcal L$ is the language $\mathcal L_A$ extended by finitely many constant symbols. Terms, formulas and proofs of $\mathcal L$ are coded as in :ref{#fact-syntax}. A **formula of $M$** is an element of $M$ that $M$ believes to be the code of a formula; it may have non-standard length. We write $\psi$ both for an actual formula and for its code, and call actual formulas **standard**. For $a \in M$, the **numeral** $\bar a$ is the closed term $(\cdots((0 + 1) + 1) \cdots) + 1$ with $a$ occurrences of $1$; $a \mapsto \bar a$ is $\Delta_1$ by :ref{#cor-course-of-values-provable}, and $\bar a$ is non-standard when $a$ is.

A **theory of $M$** is a set of sentences of $M$, possibly in a language extending $\mathcal L$ by constants of $M$, that is $\Delta_1$-definable in $M$ with parameters. For such $T$, $\mathrm{Prov}_T(\psi)$ says that some $p$ is a proof of $\psi$ from finitely many sentences of $T$ (and logical axioms), and $\mathrm{Con}(T)$ is $\neg \mathrm{Prov}_T(\ulcorner 0 = 1 \urcorner)$, a $\Pi_1$ formula. For a finite set $F$ of sentences of $M$, that is, a set coded in $M$, we write $T \cup F$ for the theory obtained by adding $F$.

:::fact[Logic in IΣ₁]{#fact-ee-logic}
$\mathrm I\Sigma_1$ proves the following, for every theory $T$, every finite set $F$ of sentences and all sentences $\theta, \psi, \psi_i$:

1. (**Henkin constants**) There is a language $\mathcal L^H \supseteq \mathcal L$, $\Delta_1$-definable, with a constant $c_\varphi$ for each formula $\varphi(x)$ of $\mathcal L^H$ with one free variable, such that if $T$ is consistent, so is $T^H = T \cup \{ \exists x\ \varphi(x) \rightarrow \varphi(c_\varphi) \}$.
2. (**Lindenbaum**) If $T \cup F$ is consistent, then $T \cup F \cup \{\theta\}$ or $T \cup F \cup \{\neg \theta\}$ is consistent.
3. (**Contradictions**) If $T \cup F \vdash \psi$, then $T \cup F \cup \{\neg \psi\}$ is inconsistent. If $F$ contains a disjunction $\bigvee_{i < k} \psi_i$ of a coded sequence of sentences and all the $\neg \psi_i$, $i < k$, then $F$ is inconsistent. If $T \vdash \theta$ for every $\theta \in F$ and $T \cup F$ is inconsistent, then $T$ is inconsistent.
4. (**Numerals**) For all $a, b$: $\mathrm{PA}^-$ proves $\bar a + \bar b = \overline{a + b}$, $\bar a \cdot \bar b = \overline{a b}$, $\bar a < \bar b$ if $a < b$, $\neg\, \bar a = \bar b$ if $a \neq b$, and $\forall x\, (x < \bar a \rightarrow \bigvee_{i < a} x = \bar \imath)$.
5. (**Equality and deduction**) If $T \vdash \psi(t)$ and $T \vdash s = t$ for closed terms $s, t$, then $T \vdash \psi(s)$. If $T \vdash \theta$ and $T \vdash \theta \rightarrow \psi$, then $T \vdash \psi$; if $T \vdash \forall x\, \varphi(x)$, then $T \vdash \varphi(t)$ for every closed term $t$.
6. (**New constants**) If $d$ is a constant that does not occur in $T$, and $T \cup F$ is inconsistent, then $T \cup F[d := t]$ is inconsistent for every closed term $t$, where $F[d := t]$ is obtained by replacing $d$ by $t$ in the sentences of $F$.

Moreover, for standard formulas $\psi_1, \dots, \psi_k, \psi$ such that $\psi_1, \dots, \psi_k \vdash \psi$ in first-order logic, and constants $\bar c$ of $\mathcal L^H$ in $M$, $M$ satisfies $\{\psi_1(\bar c), \dots, \psi_k(\bar c)\} \vdash \psi(\bar c)$.
:::

We admit the fact: each item formalizes an elementary fact of logic by $\Sigma_1$ induction on proofs, and the last statement holds because the actual proof, with $\bar c$ substituted, is a proof in the sense of $M$. Hájek and Pudlák carry out these formalizations in Chapter I, Section 4(a); the delicate item is Henkin's (their Theorem I.4.10), and item 4 is part of formalized $\Sigma_1$-completeness (Theorem I.4.32).

## The theorem

:::theorem[Arithmetized completeness theorem]{#thm-ee-act}
Let $M \models \mathrm I\Sigma_1$ and $T$ a theory of $M$ in the language $\mathcal L$ that contains the axioms of $\mathrm{PA}^-$. If $M \models \mathrm{Con}(T)$, there is an $\mathcal L$-structure $K$ such that:

1. $M \subseteq_e K$, after identifying $M$ with its image;
2. for every standard formula $\psi(\bar x)$ of $\mathcal L$ and every tuple $\bar a$ of $M$, if $M \models \mathrm{Prov}_T(\psi(\bar{\bar a}))$, then $K \models \psi(\bar a)$, where $\bar{\bar a}$ is the tuple of numerals; in particular, $K$ satisfies every standard sentence of $T$;
3. every element of $K$ is named by a constant of $\mathcal L^H$, and there is a set $H$ of sentences of $M$, $\Delta_2$-definable in $M$, such that for every standard formula $\psi(\bar x)$ and constants $\bar c$, $K \models \psi(\bar c^K)$ if and only if $\psi(\bar c) \in H$.
:::

**Idea.** Add Henkin witnesses, complete the theory along a path through the $\Delta_1$ tree of finite attempts, and build the model of constants. The low basis theorem gives a path whose finite parts are elements of $M$, on which the complete theory is checked. Item 4 of the fact gives the end extension.

:::proof{of=thm-ee-act}
*The tree of completions.* By item 1 of :ref{#fact-ee-logic}, $M \models \mathrm{Con}(T^H)$. For a string $\sigma$, let $\Theta(\sigma)$ be the finite set of the sentences $s$ of $\mathcal L^H$ with $s < \mathrm{len}(\sigma)$ and digit $1$ at $s$, together with the negations $\neg s$ of the sentences $s < \mathrm{len}(\sigma)$ with digit $0$ at $s$. Let $\mathrm{Tr}$ be the set of strings $\sigma$ such that no $p < \mathrm{len}(\sigma)$ is a proof of $0 = 1$ from $T^H \cup \Theta(\sigma)$. It is a $\Delta_1$ binary tree of $M$: if $\sigma \sqsubseteq \tau$, then $\Theta(\sigma) \subseteq \Theta(\tau)$ and fewer proofs are considered for $\sigma$.

It is unbounded. The formula "some string $\sigma$ of length $\ell$ satisfies $\mathrm{Con}(T^H \cup \Theta(\sigma))$" is a bounded existential quantifier in front of a $\Pi_1$ formula, hence $\Pi_1$ in $M$ (:ref{#lem-fo-collection-closure}). It holds for $\ell = 0$, by $\mathrm{Con}(T^H)$, and passes from $\ell$ to $\ell + 1$ by item 2 of the fact if $\ell$ is a sentence, trivially otherwise. By $\Pi_1$ induction (:ref{#thm-fo-isigma-ipi}), it holds for all $\ell$; and such a $\sigma$ belongs to $\mathrm{Tr}$.

*The complete theory.* By :ref{#thm-ee-low-basis}, $\mathrm{Tr}$ has a path $X$ that is low over $M$, hence $\Delta_2$-definable. Let $H$ be the set of the sentences $s$ with $X(s) = 1$ and of the negations $\neg s$ of the sentences with $X(s) = 0$, so that $H = \bigcup_\ell \Theta(X \restriction \ell)$; it is $\Delta_2$-definable. For every sentence $s$, $s \in H$ or $\neg s \in H$. We prove three properties of $H$.

(i) For every $\ell$, $M \models \mathrm{Con}(T^H \cup \Theta(X \restriction \ell))$. Otherwise some proof $p$ of $0 = 1$ uses $\Theta(X \restriction \ell)$. Let $\ell' > \max(\ell, p)$. Then $\Theta(X \restriction \ell) \subseteq \Theta(X \restriction \ell')$, and $p < \ell'$ contradicts $X \restriction \ell' \in \mathrm{Tr}$.

(ii) If $M \models T^H \cup \Theta(X \restriction \ell) \vdash \psi$ for some $\ell$, then $\psi \in H$. Otherwise $\neg \psi \in H$, so $\neg \psi \in \Theta(X \restriction \ell')$ for $\ell' > \psi$. With $\ell'' = \max(\ell, \ell')$, $T^H \cup \Theta(X \restriction \ell'')$ proves $\psi$ and contains $\neg \psi$, so it is inconsistent by item 3, contradicting (i).

(iii) If a disjunction $\bigvee_{i < k} \psi_i$ of $M$ belongs to $H$, some $\psi_i$, $i < k$, belongs to $H$. Otherwise $\neg \psi_i \in H$ for every $i < k$. The codes of the $\psi_i$ and of the disjunction are below some $\ell$, so the element $X \restriction \ell$ of $M$ satisfies, in $M$, "the disjunction and all the $\neg \psi_i$, $i < k$, belong to $\Theta(X \restriction \ell)$", each instance $i$ being true. By item 3, $\Theta(X \restriction \ell)$ is inconsistent, contradicting (i).

By (ii), every sentence of $T^H$ is in $H$.

*The term model.* Let $H_{\mathrm{st}}$ be the set of standard sentences of $H$, that is, sentences $\psi(\bar c)$ with $\psi$ an actual formula of $\mathcal L$ with equality and $\bar c$ constants of $\mathcal L^H$ in $M$. It is a complete set of actual sentences of $\mathcal L$ expanded by the constants of $\mathcal L^H$, closed under consequence and consistent: if $\psi_1, \dots, \psi_k \in H_{\mathrm{st}}$ and $\psi_1, \dots, \psi_k \vdash \psi$, then $M$ sees this proof (last statement of the fact), and $\psi \in H$ by (ii); so $0 = 1 \notin H$ by (i). It contains the Henkin axioms of its formulas. Henkin's proof of the completeness theorem applies: the set $K$ of equivalence classes of constants $c$ of $\mathcal L^H$ under $c \sim d \iff (c = d) \in H$, with the operations and relations read off $H$ (for constants $c, d$, the Henkin constant $e$ of $x = c + d$ satisfies $(c + d = e) \in H$ by (ii)), is an $\mathcal L$-structure in which every element is the class of a constant, and for every actual formula $\psi(\bar x)$, $K \models \psi([\bar c])$ if and only if $\psi(\bar c) \in H$. This is item 3, writing $\bar c^K$ for $[\bar c]$.

*The embedding.* For $a \in M$, let $c_a$ be the Henkin constant of the formula $x = \bar a$. Since $\exists x\ (x = \bar a)$ is provable, (ii) gives $(c_a = \bar a) \in H$. By item 4 of the fact and item 5, applied to finitely many sentences of $H$ and then (ii), $H$ contains $c_0 = 0$, $c_1 = 1$, $c_a + c_b = c_{a+b}$, $c_a \cdot c_b = c_{ab}$, $c_a < c_b$ if $a < b$, and $\neg\, c_a = c_b$ if $a \neq b$. So $a \mapsto [c_a]$ is an embedding of $M$ into $K$; we identify $a$ with $[c_a]$.

*End extension.* Let $[c] < [c_a]$ in $K$, that is, $(c < c_a) \in H$. By item 4, $\mathrm{PA}^- \vdash \forall x\, (x < \bar a \rightarrow \bigvee_{i < a} x = \bar \imath)$, so with $c < c_a$ and $c_a = \bar a$, item 5 and (ii) give $\bigvee_{i < a} c = \bar \imath \in H$. By (iii), $(c = \bar \imath) \in H$ for some $i < a$, so $(c = c_i) \in H$ by (ii), and $[c] = [c_i] = i$. So $M \subseteq_e K$.

*Item 2.* If $M \models \mathrm{Prov}_T(\psi(\bar{\bar a}))$, then $\psi(\bar{\bar a}) \in H$ by (ii), and with $c_{a_j} = \bar a_j$, item 5 and (ii) give $\psi(\bar c_{\bar a}) \in H$, a standard sentence. So $K \models \psi(\bar a)$.
:::

:::figure[The arithmetized completeness theorem. The constants of $\mathcal L^H$ name the elements of $K$, and $c_a$ names $a$. The sentence $\forall x\,(x < \bar a \rightarrow \bigvee_{i<a} x = \bar\imath)$ of $H$ forces every element below $a$ to be some $i < a$, so $M$ is an initial segment of $K$.]
<svg class="fig" viewBox="0 0 600 170" width="600" role="img" aria-label="The model K built from constants contains M as an initial segment: the constant c_a names a, and the elements below a are the constants c_i for i below a"><line x1="20.0" y1="80.0" x2="580.0" y2="80.0" class="ink-stroke" stroke-width="1.2"/><circle cx="24.0" cy="80.0" r="3.5" class="accent-fill"/><text x="24.0" y="66.0" text-anchor="middle" class="mrm" font-size="13">0</text><circle cx="70.0" cy="80.0" r="3.5" class="accent-fill"/><circle cx="110.0" cy="80.0" r="3.5" class="accent-fill"/><circle cx="150.0" cy="80.0" r="3.5" class="accent-fill"/><circle cx="190.0" cy="80.0" r="3.5" class="accent-fill"/><text x="130.0" y="66.0" text-anchor="middle" class="math" font-size="13">c<tspan class="mrm" font-size="10" dy="3">i</tspan></text><circle cx="240.0" cy="80.0" r="4" class="ink-fill"/><text x="240.0" y="66.0" text-anchor="middle" class="math" font-size="13">a = [c<tspan class="mrm" font-size="10" dy="3">a</tspan><tspan dy="-3">]</tspan></text><line x1="330.0" y1="58.0" x2="330.0" y2="102.0" class="accent-stroke" stroke-width="1.6" stroke-dasharray="4 3"/><text x="330.0" y="50.0" text-anchor="middle" class="math" font-size="14">M</text><circle cx="400.0" cy="80.0" r="3.5" class="node"/><circle cx="460.0" cy="80.0" r="3.5" class="node"/><circle cx="520.0" cy="80.0" r="3.5" class="node"/><path d="M22.0,96.0 L22.0,102.0 L236.0,102.0 L236.0,96.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="129.0" y="120.0" text-anchor="middle" class="label">every [c] &lt; a equals some [cᵢ], i &lt; a</text><path d="M336.0,96.0 L336.0,102.0 L578.0,102.0 L578.0,96.0" class="muted-stroke" fill="none" stroke-width="1.2"/><text x="457.0" y="120.0" text-anchor="middle" class="label">new elements: classes of other constants</text><text x="300.0" y="26.0" text-anchor="middle" class="label">K = constants of the Henkin language, modulo provable equality in H</text></svg>
:::

:::quiz[the arithmetized completeness theorem]
In the proof that $M$ is an initial segment of $K$, why is property (iii) of $H$ needed, and not only property (ii)?

- [x] The disjunction $\bigvee_{i < a} c = \bar \imath$ has $a$ disjuncts, non-standardly many when $a$ is non-standard; to put one of them in $H$, one argues inside $M$, where $X \restriction \ell$ is an element and item 3 applies to the coded sequence of disjuncts.
- [ ] Because the disjunction is not provable from $T^H$.

  It is provable from $T^H$ together with the two sentences $c < c_a$ and $c_a = \bar a$ of $H$; property (ii) puts it in $H$.
- [ ] Because $H$ is not complete.

  $H$ contains $s$ or $\neg s$ for every sentence $s$ of $M$; deciding the disjuncts one at a time does not show that one of non-standardly many is in $H$.

:::

Unlike omitting types arguments, the proof does not use the countability of $M$; and $K$ is described inside $M$ through the $\Delta_2$-definable set $H$. The relativization to $\mathrm I\Sigma_{m+1}$ is stated in the next lesson, where it is used.

::::exercise{#ex-ee-act-pi1-reflection difficulty=2 objective="Derive from the arithmetized completeness theorem that a theory consistent in $M$ proves only $\Pi_1$ statements true in $M$."}
Let $M \models \mathrm I\Sigma_1$ and $T$ a theory of $M$ in $\mathcal L_A$ containing $\mathrm{PA}^-$, with $M \models \mathrm{Con}(T)$. Let $\pi(\bar x)$ be a standard $\Pi_1$ formula and $\bar a$ a tuple of $M$ with $M \models \mathrm{Prov}_T(\pi(\bar{\bar a}))$. Show that $M \models \pi(\bar a)$.

:::solution
Let $K$ be given by :ref{#thm-ee-act}. By item 2, $K \models \pi(\bar a)$. Write $\pi(\bar x) = \forall \bar y\ \delta(\bar x, \bar y)$ with $\delta$ bounded. If $M \models \neg \pi(\bar a)$, some $\bar b \in M$ satisfies $M \models \neg \delta(\bar a, \bar b)$; since $M \subseteq_e K$ (item 1), $K \models \neg \delta(\bar a, \bar b)$ by :ref{#lem-delta0-absolute}, and $K \models \neg \pi(\bar a)$, a contradiction. The end extension property is what transfers the failure of $\pi$ from $M$ to $K$; an arbitrary model of $T$ containing $M$ as a substructure would not do.
:::
::::

## The standard model

:::corollary[Low completeness theorem]{#cor-ee-low-completeness}
Every consistent computable theory $T$ in $\mathcal L_A$, extended by finitely many constants, that contains $\mathrm{PA}^-$ has a model whose elementary diagram, coded by the set $H$ of :ref{#thm-ee-act}, is low.
:::

:::proof{of=cor-ee-low-completeness}
In $\nat$, $T$ is $\Delta_1$-definable and $\nat \models \mathrm{Con}(T)$. :ref{#thm-ee-act} gives $K$ and $H$, computable in a path $X$ that is low over $\nat$, hence low; so $H$ is low, and by item 3 it decides every sentence $\psi(\bar c)$ about the elements of $K$.
:::

With :ref{#thm-pa-completions}, the corollary contains the existence of low completions of $\mathrm{PA}$.

## Notes and references

The arithmetization of the completeness theorem goes back to Hilbert and Bernays (1939), according to the bibliographical remarks of Hájek and Pudlák to Chapter I. The classical form is "$\mathrm{PA}$ proves that every consistent $\Delta_1$ theory has a full $\Delta_2$ model". Theorem I.4.27 of Hájek and Pudlák is the low version: in $\mathrm I\Sigma_1$, a consistent $\Delta_1$ theory has a full model that is low $\Sigma_0(\Sigma_1)$, and in $\mathrm B\Sigma_2$ one that is low $\Delta_2$; their model carries a full satisfaction relation defined in $M$. :ref{#thm-ee-act} is an external form, in which the $\Delta_2$ bound on $H$ in $\mathrm I\Sigma_1$ comes from the proof of :ref{#thm-ee-low-basis}. Wong's Lecture 4 proves the external form over models of $\mathrm{WKL}_0$, with the same end extension argument. Hájek and Pudlák mention earlier partial improvements by McAloon (1978) and Paris (1981).

- D. Hilbert and P. Bernays, *Grundlagen der Mathematik II*, Springer, 1939.
- K. McAloon, *Completeness theorems, incompleteness theorems and models of arithmetic*, Transactions of the American Mathematical Society 239 (1978), 253–277.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 4(a)–(b).
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 4.

:::::exercises
::::exercise{#ex-ee-act-any-path difficulty=1 lessons="trees-isigma1" objective="Locate where the proof of the arithmetized completeness theorem uses the lowness of the path."}
In the proof of :ref{#thm-ee-act}, let $X$ be any path through $\mathrm{Tr}$ in the sense of :ref{#def-ee-tree}, not necessarily low, and define $H$ from $X$ as in the proof. Show that properties (i)–(iii) still hold, and that the structure $K$ built from $H$ satisfies items 1 and 2 and the first half of item 3. Which conclusion needs the low basis theorem? (For countable $M$, such paths exist by :ref{#ex-ee-countable-paths}.)

:::solution
Property (i) uses only that $X \restriction \ell' \in \mathrm{Tr}$ for every $\ell'$, which holds for every path. Property (ii) uses (i) and item 3 of :ref{#fact-ee-logic}. Property (iii) uses that $X \restriction \ell$ is an element of $M$, so that the statement "the disjunction and all the $\neg \psi_i$, $i < k$, belong to $\Theta(X \restriction \ell)$" can be evaluated in $M$; this is part of the definition of a path. The construction of the term model, the embedding and the end extension property use only (i)–(iii) and the facts of logic. So $K$ satisfies items 1 and 2, its elements are named by constants, and $K \models \psi(\bar c^K)$ if and only if $\psi(\bar c) \in H$. What is lost is the definability of $H$: it is $\Delta_2$-definable because $X$ is low over $M$, by the choice of $X$ in :ref{#thm-ee-low-basis}. This bound is what :ref{#cor-ee-low-completeness} uses, and the next lesson uses it to describe the sets coded in $K$.
:::
::::

::::exercise{#ex-ee-act-false-sigma1 difficulty=1 objective="Show that a provable $\Sigma_1$ sentence false in $M$ forces the model of the arithmetized completeness theorem to be a proper extension."}
Let $M$, $T$ and $K$ be as in :ref{#thm-ee-act}, and let $\delta(x, \bar y)$ be a standard bounded formula and $\bar a \in M$ such that $M \models \mathrm{Prov}_T(\exists x\ \delta(x, \bar{\bar a}))$ and $M \models \neg \exists x\ \delta(x, \bar a)$. Show that $K \neq M$ and that every witness of $\exists x\ \delta(x, \bar a)$ in $K$ lies above $M$.

:::solution
By item 2, $K \models \exists x\ \delta(x, \bar a)$. Let $b \in K$ be a witness. If $b \in M$, then $M \models \delta(b, \bar a)$ by :ref{#lem-delta0-absolute}, since $M \subseteq_e K$, contradicting the hypothesis. So $b \notin M$, hence $K \neq M$, and $b > M$ since $M$ is an initial segment of $K$. The next lesson uses this with the sentence $\neg \mathrm{Con}(\mathrm{PA})$, which is $\Sigma_1$.
:::
::::

::::exercise{#ex-ee-act-closure difficulty=2 objective="Check that the complete theory of the proof is consistent and closed under provability as seen by $M$."}
In the proof of :ref{#thm-ee-act}:

1. Show that for every sentence $s$ of $M$ in $\mathcal L^H$, exactly one of $s$ and $\neg s$ belongs to $H$, and that $X(s) = 1$ for every $s \in H$.
2. Let $F$ be a finite set of sentences of $M$, coded in $M$, all of which belong to $H$, and $\psi$ a sentence of $M$ with $M \models \mathrm{Prov}_{T^H \cup F}(\psi)$. Show that $\psi \in H$.

:::solution
1. By definition of $H$, $s \in H$ if $X(s) = 1$ and $\neg s \in H$ if $X(s) = 0$. Suppose $s, \neg s \in H$. For $\ell$ large enough, both belong to $\Theta(X \restriction \ell)$; then $T^H \cup \Theta(X \restriction \ell)$ proves $s$ by a proof of one line, and contains $\neg s$, so it is inconsistent by item 3 of :ref{#fact-ee-logic}, contradicting property (i). If $s \in H$ and $X(s) = 0$, then $\neg s \in H$ as well, which was just excluded; so $X(s) = 1$.
2. Let $\ell > F$. Every element $s$ of $F$ is below $F$ (:ref{#lem-ack-basic}), lies in $H$, and so satisfies $X(s) = 1$ by item 1; hence $s \in \Theta(X \restriction \ell)$. The statement "$\forall s \in F\ (s \in \Theta(X \restriction \ell))$" is a bounded statement about the elements $F$ and $X \restriction \ell$ of $M$, true at every $s \in M$ coded by $F$; so it holds in $M$. A proof of $\psi$ from $T^H \cup F$ is then a proof of $\psi$ from $T^H \cup \Theta(X \restriction \ell)$, since it uses finitely many sentences of $T^H \cup F$. By property (ii), $\psi \in H$.
:::
::::

::::exercise{#ex-ee-act-not-delta1 difficulty=1 objective="See that the bound $\Delta_2$ on the diagram cannot be improved to $\Delta_1$, by the theory of PA degrees."}
Show that for $M = \nat$ and $T = \mathrm{PA}$, the set $H$ of :ref{#thm-ee-act} is never computable, whatever path is used. Deduce that $\Delta_2$ cannot be replaced by $\Delta_1$ in item 3.

:::solution
$\nat \models \mathrm{Con}(\mathrm{PA})$. By property (i) and item 1 of :ref{#ex-ee-act-closure}, the set of sentences of $\mathcal L_A$ that belong to $H$ is complete and consistent, and by (ii) it contains the axioms of $\mathrm{PA}$. It is computable in $H$, since the codes of sentences of $\mathcal L_A$ form a computable set. If $H$ were computable, this completion of $\mathrm{PA}$ would be computable, and the computable set $\emptyset$ would be PA by :ref{#thm-pa-completions}; but no computable set is PA, by :ref{#thm-dnc2-no-computable}. So $H$ is not computable, that is, not $\Delta_1$-definable in $\nat$ (:ref{#thm-definable-arithmetic}).
:::
::::

::::exercise{#ex-ee-act-pa-minus difficulty=1 objective="See why the theory must contain $\mathrm{PA}^-$ for the model to extend $M$."}
Let $T$ be the theory $\{ \forall x\ \forall y\ (x = y) \}$ of $\nat$. Show that $\nat \models \mathrm{Con}(T)$ and that no model of $T$ contains a copy of $\nat$. Which step of the proof of :ref{#thm-ee-act} fails?

:::solution
$T$ has a model with one element, so it is consistent, and $\nat \models \mathrm{Con}(T)$, since $\mathrm{Con}(T)$ is a $\Pi_1$ sentence and its negation, a $\Sigma_1$ sentence, would give an actual proof of $0 = 1$ from $T$. A model of $T$ has one element, and $\nat$ is infinite, so it has no copy of $\nat$. The embedding step fails: it uses item 4 of :ref{#fact-ee-logic}, that $\mathrm{PA}^-$ proves $\neg\, \bar a = \bar b$ for $a \neq b$, to put the sentences $\neg\, c_a = c_b$ into $H$; here $H$ contains $c_a = c_b$ for all $a, b$.
:::
::::
:::::
