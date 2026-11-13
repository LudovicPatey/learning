---
title: Full satisfaction classes
summary: Satisfaction classes for sets of formulas of a model, standard or not, defined by Tarski's clauses; every partial satisfaction class closed under subformulas extends, in an elementary extension, to all formulas of the model (Enayat, Visser); every countable recursively saturated model of IΣ₁ has a full satisfaction class (Kotlarski, Krajewski, Lachlan), and the theory of a full satisfaction class without induction is conservative over Peano arithmetic.
duration: 45
prerequisites: [resplendence, truth-and-provability/bounded-satisfaction]
---

By Tarski's theorem, no model of arithmetic defines its own satisfaction relation. One can ask instead for an undefinable relation $S$, added to the model, that obeys Tarski's inductive clauses for **all** formulas of the model, including the non-standard ones. Such an $S$ is a **full satisfaction class**. On non-standard formulas the clauses only relate each formula to its immediate subformulas, and nothing forces induction.

This lesson proves that every countable recursively saturated model of $\mathrm I\Sigma_1$ carries a full satisfaction class (Kotlarski, Krajewski and Lachlan, 1981). The proof follows Enayat and Visser (2015). Because the clauses are **local**, finitely many of them can always be satisfied at once by a recursion on a finite set of formulas; compactness then gives an elementary extension in which all formulas of the original model are handled, iteration gives a full class on a larger model, and resplendence brings it back to the original model. The next lesson proves the converse of the existence theorem.

## Syntax inside a model

Let $M$ be a model of $\mathrm I\Sigma_1$. Formulas are coded as in :ref{#fact-syntax}: atomic formulas $s = t$, $s < t$, the connectives $\neg$, $\wedge$, $\vee$, and the quantifiers $\exists v_i$, $\forall v_i$, $\exists v_i < v_j$, $\forall v_i < v_j$. Let $\mathrm{Form}(z)$ be the $\Delta_1$ definition of the set of codes of formulas, obtained by course-of-values recursion like those of :ref{#fact-syntax}, and $\mathrm{Form}^M = \{ z \in M : M \models \mathrm{Form}(z) \}$. Its elements below the standard cut are the codes of actual formulas; the others are **non-standard formulas**. Each $z \in \mathrm{Form}^M$ decomposes, in $M$, as an atomic formula or as a constructor applied to its **direct subformulas**, which are smaller. Assignments are numbers $e$, with values $e(i)$, and $\mathrm{Val}(t, e)$ is the value of the term $t$ under $e$ (:ref{#fact-syntax}).

:::definition[Krajewski; Kotlarski, Krajewski, Lachlan]{#def-sat-class}
Let $M$ be a model of $\mathrm I\Sigma_1$ and $F \subseteq \mathrm{Form}^M$ a set closed under direct subformulas. An **$F$-satisfaction class** for $M$ is a set $S \subseteq F \times M$ such that, for every $\theta \in F$ and every assignment $e \in M$, with $S(\theta, e)$ for $(\theta, e) \in S$:

1. if $\theta$ is $s = t$, then $S(\theta, e) \leftrightarrow \mathrm{Val}(s, e) = \mathrm{Val}(t, e)$, and similarly for $s < t$;
2. if $\theta$ is $\neg \varphi$, then $S(\theta, e) \leftrightarrow \neg S(\varphi, e)$;
3. if $\theta$ is $\varphi \wedge \psi$, then $S(\theta, e) \leftrightarrow S(\varphi, e) \wedge S(\psi, e)$, and similarly for $\vee$;
4. if $\theta$ is $\exists v_i\, \varphi$, then $S(\theta, e) \leftrightarrow S(\varphi, e[i := x])$ for some $x \in M$, and similarly for $\forall v_i$ with every $x \in M$;
5. if $\theta$ is $\exists v_i < v_j\ \varphi$, then $S(\theta, e) \leftrightarrow S(\varphi, e[i := x])$ for some $x < e(j)$, and similarly for $\forall v_i < v_j$.

A **full satisfaction class** is a $\mathrm{Form}^M$-satisfaction class.
:::

The clauses are finitely many, and each is first-order in $\mathcal L_A \cup \{ S \}$: "$S$ is a full satisfaction class" is a single sentence $\tau(S)$. The theory $\mathrm{CT}^-$ is $\mathrm{PA} + \tau(S)$, in which induction is assumed only for formulas of $\mathcal L_A$. Neither $F$ nor $S$ need be definable, and no induction is required for $S$.

:::example{#ex-sat-classes}
1. In $\nat$, every formula is standard, and satisfaction in $\nat$ is the only full satisfaction class, by induction on formulas.
2. In a model $M$, the standard formulas form a set $F$ closed under direct subformulas; $\{ (\ulcorner \theta \urcorner, e) : \theta \text{ standard}, M \models \theta(e) \}$ is the only $F$-satisfaction class, by induction on formulas in the metatheory. So a full satisfaction class agrees with satisfaction in $M$ on standard formulas.
3. In a model $M$, the set $(\Delta^*_0)^M$ of codes of formulas with variable bounds is closed under direct subformulas, and $\mathrm{Sat}_0$ (:ref{#def-sat0}) defines a $(\Delta^*_0)^M$-satisfaction class for $M$, by :ref{#thm-sat0}. Unbounded quantifiers are what makes full satisfaction classes undefinable.
:::

## The theorem of Enayat and Visser

:::theorem[Enayat, Visser]{#thm-enayat-visser}
Let $M$ be a model of $\mathrm I\Sigma_1$, $F_0 \subseteq \mathrm{Form}^M$ closed under direct subformulas, and $S_0$ an $F_0$-satisfaction class for $M$. There are an elementary extension $K \succcurlyeq M$ and a set $S \subseteq \mathrm{Form}^M \times K$ satisfying the clauses of :ref{#def-sat-class} for every $\theta \in \mathrm{Form}^M$ and every assignment $e \in K$ (with $x$ ranging over $K$), such that $S \cap (F_0 \times M) = S_0$.
:::

All formulas of $M$ are handled, for all assignments of $K$; the new formulas of $K$ are not.

:::proof{of=thm-enayat-visser}
*The theory.* Add to $\mathcal L_A(M)$ a unary predicate $U_\theta$ for each $\theta \in \mathrm{Form}^M$, to be read as the set of assignments satisfying $\theta$. For each $\theta$, let $\tau_\theta$ be its Tarski clause, written with these predicates: for instance, if $\theta = \exists v_i\, \varphi$, $\tau_\theta$ is $\forall e\, \big( U_\theta(e) \leftrightarrow \exists x\ U_\varphi(e[i := x]) \big)$, and if $\theta$ is $s = t$, $\tau_\theta$ is $\forall e\, (U_\theta(e) \leftrightarrow \mathrm{Val}(s, e) = \mathrm{Val}(t, e))$. Let
$$
T = \mathrm{ElemDiag}(M) \cup \{ \tau_\theta : \theta \in \mathrm{Form}^M \} \cup \{ U_\theta(e) : (\theta, e) \in S_0 \} \cup \{ \neg U_\theta(e) : \theta \in F_0,\ e \in M,\ (\theta, e) \notin S_0 \}.
$$
If $(K, (U_\theta^K)_\theta) \models T$, then $K \succcurlyeq M$ after identification, and $S = \{ (\theta, e) : \theta \in \mathrm{Form}^M,\ e \in U_\theta^K \}$ has the required properties: the clauses are the $\tau_\theta$, and the last two parts of $T$ give $S \cap (F_0 \times M) = S_0$. By compactness, it suffices to satisfy a finite part $T_0$ in an expansion of $M$.

*A finite part.* Let $\Theta$ be the finite set of $\theta$ such that $U_\theta$ occurs in $T_0$, and write $\varphi \lhd \theta$ if $\tau_\theta \in T_0$ and $\varphi$ is a direct subformula of $\theta$; then $\varphi \in \Theta$, since $\tau_\theta$ mentions $U_\varphi$. Direct subformulas have smaller codes, so $\lhd$ is well founded on the finite set $\Theta$, and each $\theta \in \Theta$ has a **rank**: $0$ if no $\varphi \lhd \theta$, and otherwise one more than the largest rank of such $\varphi$. Define $U_\theta \subseteq M$ by recursion on the rank:

- rank $0$: if $\theta \in F_0$, $U_\theta = \{ e : (\theta, e) \in S_0 \}$; if $\theta \notin F_0$ is atomic, $U_\theta$ is given by its clause; otherwise $U_\theta = \emptyset$;
- positive rank: $U_\theta$ is defined from the $U_\varphi$, $\varphi \lhd \theta$, by the clause $\tau_\theta$, evaluated in $M$.

Interpret the other predicates as $\emptyset$. The expansion satisfies $\mathrm{ElemDiag}(M)$. It satisfies each $\tau_\theta \in T_0$: if $\theta$ has positive rank, by construction; if $\tau_\theta \in T_0$ and $\theta$ has rank $0$, then $\theta$ has no direct subformula, so it is atomic, and $U_\theta$ is given by its clause, either directly or through $S_0$, which satisfies the atomic clauses. By induction on the rank, $U_\theta = \{ e : (\theta, e) \in S_0 \}$ for every $\theta \in \Theta \cap F_0$: at rank $0$ by definition; at positive rank because the $\varphi \lhd \theta$ belong to $F_0$, where they agree with $S_0$ by induction, and $S_0$ satisfies the clause of $\theta$. So the sentences of $T_0$ about $S_0$ hold.
:::

:::figure[A finite part of the theory in the proof of :ref{#thm-enayat-visser}. The formulas whose predicates occur in it are ordered by $\lhd$; the sets $U_\theta$ are defined rank by rank, from $S_0$ at the bottom when $\theta \in F_0$, and by the Tarski clauses above.]
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="A finite set of formulas ordered by the direct subformula relation, with ranks 0 to 3; the sets U are defined rank by rank, from S0 at rank 0 for formulas of F0 and by the Tarski clauses above"><line x1="180.0" y1="136.0" x2="110.0" y2="184.0" class="muted-stroke" stroke-width="1.2"/><line x1="180.0" y1="136.0" x2="250.0" y2="184.0" class="muted-stroke" stroke-width="1.2"/><line x1="430.0" y1="136.0" x2="430.0" y2="184.0" class="muted-stroke" stroke-width="1.2"/><line x1="300.0" y1="76.0" x2="180.0" y2="124.0" class="muted-stroke" stroke-width="1.2"/><line x1="300.0" y1="76.0" x2="430.0" y2="124.0" class="muted-stroke" stroke-width="1.2"/><line x1="300.0" y1="26.0" x2="300.0" y2="64.0" class="muted-stroke" stroke-width="1.2"/><circle cx="110.0" cy="190.0" r="4.5" class="accent-fill"/><text x="110.0" y="214.0" text-anchor="middle" class="label">in F₀: from S₀</text><circle cx="250.0" cy="190.0" r="4.5" class="accent-fill"/><text x="250.0" y="214.0" text-anchor="middle" class="label">atomic: by its clause</text><circle cx="430.0" cy="190.0" r="4.5" class="accent-fill"/><text x="430.0" y="214.0" text-anchor="middle" class="label">other: ∅</text><circle cx="180.0" cy="130.0" r="4.5" class="node"/><circle cx="430.0" cy="130.0" r="4.5" class="node"/><circle cx="300.0" cy="70.0" r="4.5" class="node"/><circle cx="300.0" cy="20.0" r="4.5" class="node"/><text x="560.0" y="194.0" text-anchor="end" class="label">rank 0</text><text x="560.0" y="134.0" text-anchor="end" class="label">rank 1</text><text x="560.0" y="74.0" text-anchor="end" class="label">rank 2</text><text x="560.0" y="24.0" text-anchor="end" class="label">rank 3</text><text x="80.0" y="70.0" text-anchor="start" class="label">above rank 0:</text><text x="80.0" y="86.0" text-anchor="start" class="label">by the Tarski clauses</text></svg>
:::

:::quiz[the theorem of Enayat and Visser]
Why can a finite part of $T$ be satisfied in $M$ itself, while the whole theory requires an elementary extension?

- [x] A finite part involves finitely many formulas, ordered by a well-founded relation of finite rank, along which the sets $U_\theta$ can be defined in $M$; for all formulas of $M$ at once, the relation of direct subformula has non-standard descending paths, and no recursion of this kind is available.
- [ ] Because $M$ is not recursively saturated.

  The theorem holds for every model of $\mathrm I\Sigma_1$; recursive saturation is used only afterwards, to come back from $K$ to $M$.
- [ ] Because $\mathrm{Form}^M$ is uncountable.

  If $M$ is countable, so is $\mathrm{Form}^M$; the problem is the non-standard depth of formulas, not their number.

---

Where is it used that $F_0$ is closed under direct subformulas?

- [x] In the induction showing that the sets $U_\theta$ agree with $S_0$ on $F_0$: the direct subformulas of a formula of $F_0$ must be in $F_0$, where the induction hypothesis applies.
- [ ] To define the rank.

  The rank is defined on $\Theta$ for any finite set of formulas.
- [ ] To make $T$ consistent with $\mathrm{ElemDiag}(M)$.

  Consistency is what the argument proves; closure is used inside it, for the agreement with $S_0$.
:::

## Full satisfaction classes on recursively saturated models

:::theorem[Kotlarski, Krajewski, Lachlan]{#thm-kkl}
Every countable recursively saturated model of $\mathrm I\Sigma_1$ has a full satisfaction class.
:::

:::proof{of=thm-kkl}
*A chain.* Let $M_0 = M$, $F_0 = \emptyset$ and $S_0 = \emptyset$, an $F_0$-satisfaction class. Given $M_n$ with a $\mathrm{Form}^{M_{n-1}}$-satisfaction class $S_n$ (for $n = 0$, with $\mathrm{Form}^{M_{-1}} = \emptyset$), :ref{#thm-enayat-visser} applied to $M_n$ gives $M_{n+1} \succcurlyeq M_n$ and $S_{n+1} \subseteq \mathrm{Form}^{M_n} \times M_{n+1}$, satisfying the clauses for the formulas of $M_n$ and the assignments of $M_{n+1}$, with $S_{n+1} \cap (\mathrm{Form}^{M_{n-1}} \times M_n) = S_n$. By elementarity, $\mathrm{Form}^{M_n} = \mathrm{Form}^{M_{n+1}} \cap M_n$.

*The union.* Let $M_\omega = \bigcup_n M_n \succcurlyeq M$ and $S_\omega = \bigcup_n S_n$. For $\theta \in \mathrm{Form}^{M_\omega}$ and $e \in M_\omega$, take $n$ with $\theta \in M_n$ and $e \in M_{n+1}$; by the agreement condition, $S_\omega$ and $S_{m+1}$ have the same pairs $(\varphi, e')$ with $\varphi \in M_m$ and $e' \in M_{m+1}$, for every $m$. The clause of $\theta$ at $e$ holds in $S_{m+1}$ for every $m \geq n$, with witnesses $x$ in $M_{m+1}$; for an existential quantifier, a witness in $M_\omega$ lies in some $M_{m+1}$, and conversely. So $S_\omega$ is a full satisfaction class for $M_\omega$, and $M_\omega \models \mathrm{ElemDiag}(M)$.

*Back to $M$.* The sentence $\tau(S)$ is therefore consistent with $\mathrm{ElemDiag}(M)$. By :ref{#thm-barwise-ressayre}, $M$ has an expansion $(M, S) \models \tau(S)$.
:::

Compactness and the locality of the clauses give satisfaction classes in extensions; resplendence turns consistency into existence. The chain and the last step work for every resplendent model of $\mathrm I\Sigma_1$, countable or not. Countability is used only through :ref{#thm-barwise-ressayre}, and cannot be dropped: Smith (1989) gives uncountable recursively saturated models of $\mathrm{PA}$ without full satisfaction classes, which are therefore not resplendent, and Lachlan (1981) an uncountable model of $\mathrm{PA}$ with a full satisfaction class that is not resplendent (both as reported in Wong's Lecture 14).

Full satisfaction classes can be far from truth on non-standard formulas. Let $\delta_1$ be $0 \neq 0$ and $\delta_{m+1}$ be $0 \neq 0 \vee \delta_m$, defined in $M$ for every $m$ by a primitive recursive function. The exercise below shows that some full satisfaction class makes $\delta_a$ true for a non-standard $a$, although each of its disjuncts is false: the clause for $\vee$ only unravels standardly many disjuncts.

:::corollary{#cor-ct-conservative}
$\mathrm{CT}^-$ is conservative over $\mathrm{PA}$: every $\mathcal L_A$-sentence provable in $\mathrm{CT}^-$ is provable in $\mathrm{PA}$.
:::

:::proof{of=cor-ct-conservative}
Suppose $\mathrm{PA} \nvdash \sigma$. Then $\mathrm{PA} + \neg \sigma$ has a countable model, which has a countable recursively saturated elementary extension $M$ (:ref{#thm-rs-existence}). By :ref{#thm-kkl}, $M$ has a full satisfaction class $S$, and $(M, S) \models \mathrm{CT}^- + \neg \sigma$. So $\mathrm{CT}^- \nvdash \sigma$.
:::

Induction for formulas mentioning $S$ changes this (Kotlarski, 1986): adding to $\mathrm{CT}^-$ induction for bounded formulas of $\mathcal L_A \cup \{ S \}$ gives a theory that proves $\mathrm{Con}(\mathrm{PA})$, as recalled in the next lesson.

## Exercises

::::exercise{difficulty=3}
Let $M$ be a countable recursively saturated model of $\mathrm I\Sigma_1$, $a \in M$ non-standard, and $\delta_a$ as above. Show that $M$ has a full satisfaction class $S$ with $S(\delta_a, 0)$: the sentence $\delta_a$ is true for $S$.

:::solution
In the proof of :ref{#thm-enayat-visser} with $F_0$ the standard formulas and $S_0$ satisfaction in $M$ for them, add to $T$ the sentence $U_{\delta_a}(0)$. In a finite part, put $U_{\delta_m} = M$ for every non-standard $m$ with $\delta_m$ of rank $0$, instead of $\emptyset$ (these formulas are neither atomic nor in $F_0$). By induction on the rank, $U_{\delta_m} = M$ for every non-standard $m$ with $\delta_m \in \Theta$: at positive rank, $\delta_m = (0 \neq 0) \vee \delta_{m-1}$ and $U_{\delta_m} = U_{0 \neq 0} \cup U_{\delta_{m-1}} = U_{\delta_{m-1}}$, with $m - 1$ non-standard. The standard $\delta_m$ are in $F_0$ and handled by $S_0$. So the extended theory is consistent, and $K$ carries a $\mathrm{Form}^M$-class $S_1$ with $S_1(\delta_a, 0)$. Run the chain of :ref{#thm-kkl} from $(M_1, S_1) = (K, S_1)$; since $0 \in M$, the agreement conditions keep $(\delta_a, 0)$ in $S_\omega$, so $\tau(S) \wedge S(\delta_a, 0)$ is consistent with $\mathrm{ElemDiag}(M)$, and resplendence gives the class on $M$.
:::
::::

## Notes and references

Satisfaction classes for non-standard formulas were introduced by Krajewski (1976). :ref{#thm-kkl} is due to Kotlarski, Krajewski and Lachlan (1981), who proved it with a version of M-logic; the proof here, through :ref{#thm-enayat-visser}, is that of Enayat and Visser (2015), as presented in Wong's Lecture 14, where the theorem is stated for $\mathrm I\Delta_0 + \mathrm{exp}$. The example of $\delta_a$ is from the paper of Kotlarski, Krajewski and Lachlan. Kotlarski's survey (1991) and Cieśliński's book on axiomatic truth discuss the theory $\mathrm{CT}^-$ and its extensions.

- S. Krajewski, *Non-standard satisfaction classes*, in Set Theory and Hierarchy Theory, Lecture Notes in Mathematics 537, Springer, 1976, 121–144.
- H. Kotlarski, S. Krajewski and A. H. Lachlan, *Construction of satisfaction classes for nonstandard models*, Canadian Mathematical Bulletin 24 (1981), 283–293.
- A. Enayat and A. Visser, *New constructions of satisfaction classes*, in T. Achourioti, H. Galinon, J. Martínez Fernández and K. Fujimoto (eds.), Unifying the Philosophy of Truth, Logic, Epistemology, and the Unity of Science 36, Springer, 2015, 321–335.
- H. Kotlarski, *Full satisfaction classes: a survey*, Notre Dame Journal of Formal Logic 32 (1991), 573–579.
- H. Kotlarski, *Bounded induction and satisfaction classes*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 32 (1986), 531–544.
- A. H. Lachlan, *Full satisfaction classes and recursive saturation*, Canadian Mathematical Bulletin 24 (1981), 295–297.
- S. T. Smith, *Nonstandard definability*, Annals of Pure and Applied Logic 42 (1989), 21–43.
- C. Cieśliński, *The Epistemic Lightness of Truth: Deflationism and its Logic*, Cambridge University Press, 2017.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lecture 14.
