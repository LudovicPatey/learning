---
title: Resplendence
summary: Craig's trick; every countable recursively saturated structure is resplendent, and expands to a model of any recursive theory with finitely many parameters consistent with its elementary diagram (Barwise, Ressayre); a countable non-standard model of PA is recursively saturated exactly when it carries an inductive satisfaction class for standard formulas.
duration: 35
prerequisites: [recursively-saturated-models]
---

Saturation is about elements: a saturated structure contains every element that it could consistently contain. **Resplendence** is the same property for relations: a resplendent structure can be expanded by new relations satisfying any property that some elementary extension of it could satisfy. The theorem of Barwise and Ressayre says that countable recursively saturated structures are resplendent. It is the main tool for constructing **expansions** of recursively saturated models without leaving them: in the next lesson it produces full satisfaction classes, and in this one it produces satisfaction classes for standard formulas that satisfy induction.

The proof follows Ressayre. It is a Henkin construction in which the witnesses are taken among the elements of the model, instead of new constants; recursive saturation provides them, through types whose formulas are listed by a proof search.

## Resplendent structures

:::definition{#def-resplendent}
A structure $M$ for a recursive language $\mathcal L$ is **resplendent** if for every recursive language $\mathcal L^* \supseteq \mathcal L$ and every $\mathcal L^*(M)$-sentence $\varphi$ consistent with $\mathrm{ElemDiag}(M)$, there is an expansion $M^*$ of $M$ to $\mathcal L^*$ with $M^* \models \varphi$.
:::

The sentence $\varphi$ has finitely many parameters from $M$. Consistency with $\mathrm{ElemDiag}(M)$ means that some elementary extension of $M$ has an expansion satisfying $\varphi$; resplendence asks for an expansion of $M$ itself.

:::example{#ex-resplendent}
1. Let $M$ be a countable recursively saturated model of $\mathrm{PA}$, $c, d \in M$ with $\mathrm{tp}(c) = \mathrm{tp}(d)$, $\mathcal L^* = \mathcal L_A \cup \{ F \}$ with $F$ a unary function symbol, and $\varphi$ the sentence "$F$ is an automorphism and $F(c) = d$". By :ref{#thm-rs-existence}, $M$ has a countable recursively saturated elementary extension $N$, in which $c$ and $d$ still have the same type; by :ref{#cor-bf-homogeneous}, $N$ has an automorphism mapping $c$ to $d$. So $\varphi$ is consistent with $\mathrm{ElemDiag}(M)$, and resplendence of $M$ would give the homogeneity of $M$ itself.
2. The model $\nat$ is not resplendent. Let $\varphi$ say that $U$ is a non-empty set without least element. In a non-standard elementary extension of $\nat$, the set of non-standard elements satisfies $\varphi$; so $\varphi$ is consistent with $\mathrm{ElemDiag}(\nat)$, but no subset of $\nat$ satisfies it.
:::

## Craig's trick

Recursive saturation applies to recursive types; the types of the proof below are only listed by a computation.

:::lemma[Craig]{#lem-craig}
Let $p(\bar v)$ be a set of formulas with finitely many parameters, whose set of codes is computably enumerable. There is a recursive set $p'(\bar v)$ with the same parameters, realized by the same tuples in every structure, and such that $p$ is finitely satisfiable if and only if $p'$ is. In particular, a recursively saturated structure realizes every type of this kind.
:::

:::proof{of=lem-craig}
Let $\theta_0, \theta_1, \dots$ be a computable enumeration of $p$, and let $p'$ consist of the formulas $\theta_n^{(n+1)} = \theta_n \wedge \cdots \wedge \theta_n$, with $n + 1$ conjuncts. A formula $\eta$ belongs to $p'$ if and only if it is a conjunction of $n + 1$ copies of one formula, for some $n$ bounded by the length of $\eta$, and this formula is the $n$-th one enumerated; this is decidable. Each $\theta_n^{(n+1)}$ is logically equivalent to $\theta_n$, which gives the other statements.
:::

## The theorem of Barwise and Ressayre

:::theorem[Barwise; Ressayre]{#thm-barwise-ressayre}
Let $M$ be a countable recursively saturated structure for a recursive language $\mathcal L$, $\mathcal L^* \supseteq \mathcal L$ a recursive language, and $\Phi$ a recursive set of $\mathcal L^*(M)$-sentences with finitely many parameters, consistent with $\mathrm{ElemDiag}(M)$. There is an expansion $M^*$ of $M$ to $\mathcal L^*$ with $M^* \models \Phi$. In particular, $M$ is resplendent.
:::

:::proof{of=thm-barwise-ressayre}
*The plan.* Enumerate the $\mathcal L^*(M)$-formulas with at most the free variable $v$ as $\psi_0, \psi_1, \dots$, using that $M$ is countable. We choose $\mathcal L^*(M)$-sentences $\varphi_0, \varphi_1, \dots$ such that each $\Phi_n = \Phi \cup \{ \varphi_k : k < n \}$ satisfies
$$
\Phi_n \cup \mathrm{ElemDiag}(M) \text{ is consistent}, \tag{$*$}
$$
and $\varphi_n$ is either $\forall v\, \neg \psi_n$ or $\psi_n(a)$ for some $a \in M$. Then $\Phi_\omega = \bigcup_n \Phi_n$ is consistent with $\mathrm{ElemDiag}(M)$, and:

- it is complete: for a sentence $\sigma = \psi_n$, $\varphi_n$ is $\neg \sigma$ or $\sigma$;
- it contains $\mathrm{ElemDiag}(M)$: if $\sigma \in \mathrm{ElemDiag}(M)$, then $\neg \sigma$ is not in $\Phi_\omega$, so $\sigma$ is;
- it has witnesses in $M$: if $\exists v\, \psi_n \in \Phi_\omega$, then $\varphi_n$ is not $\forall v\, \neg \psi_n$, so it is $\psi_n(a)$ for some $a \in M$.

By Henkin's construction, $\Phi_\omega$ has a model whose elements are the interpretations of the constants $a \in M$; distinct constants have distinct interpretations, by the sentences $a \neq b$ of $\mathrm{ElemDiag}(M)$, and the $\mathcal L$-reduct is $M$. This model is the required expansion.

*One step.* Suppose $(*)$ holds for $\Phi_n$, and let $\bar c$ list the parameters of $\Phi_n$ and of $\psi_n$; write $\Phi_n(\bar c)$ and $\psi_n(v, \bar c)$. If $\varphi_n = \forall v\, \neg \psi_n$ keeps $(*)$, choose it. Otherwise, by compactness, $\Phi_n(\bar c) \cup \{ \alpha(\bar c, \bar e) \} \vdash \exists v\, \psi_n(v, \bar c)$ for some $\alpha \in \mathrm{ElemDiag}(M)$, with further parameters $\bar e$; since $\bar e$ occurs neither in $\Phi_n$ nor in $\psi_n$, the sentence $\alpha'(\bar c) = \exists \bar w\ \alpha(\bar c, \bar w)$ of $\mathrm{ElemDiag}(M)$ satisfies $\Phi_n \cup \{ \alpha' \} \vdash \exists v\, \psi_n(v, \bar c)$. If some $c_i$ is such that $\psi_n(c_i, \bar c)$ keeps $(*)$, choose it. Otherwise, in the same way, there are $\beta_i(\bar c) \in \mathrm{ElemDiag}(M)$ with $\Phi_n \cup \{ \beta_i \} \vdash \neg \psi_n(c_i, \bar c)$. Let
$$
p(v) = \Big\{ \theta(v, \bar c) \in \mathcal L(\bar c) : \Phi_n(\bar c) \vdash \forall v\, \big( \psi_n(v, \bar c) \wedge \textstyle\bigwedge_i v \neq c_i \rightarrow \theta(v, \bar c) \big) \Big\}.
$$
It is a set of $\mathcal L$-formulas with parameters $\bar c$, and computably enumerable, since $\Phi_n$ is computable and proofs from it can be listed. It is closed under conjunction, and each of its formulas is satisfiable in $M$: if $\theta \in p$, then $\Phi_n \vdash \alpha' \wedge \bigwedge_i \beta_i \rightarrow \exists v\, \theta(v, \bar c)$; this is an $\mathcal L(M)$-sentence, so it holds in $M$, otherwise its negation, in $\mathrm{ElemDiag}(M)$, would contradict $(*)$; and $M$ satisfies $\alpha'$ and the $\beta_i$. By :ref{#lem-craig}, some $a \in M$ realizes $p$. Since $v \neq c_i$ belongs to $p$, $a$ is not among $\bar c$. Let $\varphi_n = \psi_n(a, \bar c)$.

*The step keeps $(*)$.* Otherwise $\Phi_n \cup \{ \psi_n(a, \bar c) \} \vdash \neg \gamma(a, \bar c, \bar e)$ for some $\gamma \in \mathrm{ElemDiag}(M)$, with $\bar e$ new parameters, so $\Phi_n \cup \{ \psi_n(a, \bar c) \} \vdash \theta(a, \bar c)$, where $\theta(v, \bar c) = \forall \bar w\ \neg \gamma(v, \bar c, \bar w)$. The constant $a$ occurs neither in $\Phi_n$ nor in $\psi_n(v, \bar c)$, so $\Phi_n \vdash \forall v\, (\psi_n(v, \bar c) \rightarrow \theta(v, \bar c))$, and $\theta \in p$. Then $M \models \theta(a, \bar c)$, which contradicts $M \models \gamma(a, \bar c, \bar e)$.
:::

:::quiz[the theorem of Barwise and Ressayre]
Why does the type $p$ contain the formulas $v \neq c_i$?

- [x] The realizer $a$ must not be a parameter of $\Phi_n$ or $\psi_n$, so that a proof from $\Phi_n \cup \{ \psi_n(a, \bar c) \}$ can be generalized on the constant $a$; the case where some $c_i$ works was handled before.
- [ ] To make $p$ computably enumerable.

  The enumerability comes from listing proofs; the formulas $v \neq c_i$ are put in the implication only.
- [ ] Because $\psi_n(v, \bar c)$ is false of each $c_i$ in $M$.

  The sentences $\neg \psi_n(c_i, \bar c)$ follow from $\Phi_n$ and $\beta_i$; they concern the expansion, not $M$.

---

Where is it used that $\Phi$ has finitely many parameters?

- [x] The type $p$ must have finitely many parameters for recursive saturation to apply; its parameters are those of $\Phi_n$ and $\psi_n$.
- [ ] To enumerate the formulas $\psi_n$.

  The enumeration uses the countability of $M$.
- [ ] To make $\Phi_\omega$ complete.

  Completeness comes from the choice of each $\varphi_n$.
:::

For uncountable structures the theorem fails: there are uncountable recursively saturated models of $\mathrm{PA}$ that are not resplendent (see the next lesson). Conversely, Barwise showed that every resplendent structure for a finite language is recursively saturated (Schlipf, 1978), so for countable structures in a finite language, such as models of $\mathrm{PA}$, the two notions coincide.

## Inductive satisfaction classes for standard formulas

Assignments are coded as in :ref{#def-sat-table}: an assignment is a number $e$, with values $e(i)$.

:::definition{#def-inductive-sat}
Let $M$ be a model of $\mathrm{PA}$. An **inductive partial satisfaction class** for $M$ is a set $S \subseteq M^2$ such that, in the language $\mathcal L_A \cup \{ S \}$:

1. $(M, S)$ satisfies the induction scheme for all formulas of $\mathcal L_A \cup \{ S \}$;
2. for every standard formula $\theta(v_0, \dots, v_k)$ of $\mathcal L_A$, $(M, S) \models \forall e\ \big( S(\ulcorner \theta \urcorner, e) \leftrightarrow \theta(e(0), \dots, e(k)) \big)$.
:::

Condition 2 concerns the standard formulas only; what $S$ does on non-standard codes is not constrained. By Tarski's argument, no such $S$ is definable in $M$ (:ref{#ex-inductive-sat-undefinable}). Condition 1 makes overspill available for formulas mentioning $S$, which is what recursive saturation needs.

:::theorem{#thm-inductive-sat}
A countable non-standard model $M$ of $\mathrm{PA}$ is recursively saturated if and only if it has an inductive partial satisfaction class.
:::

:::proof{of=thm-inductive-sat}
($\Leftarrow$) Let $p(v, \bar c)$ be a recursive type, with its formulas written $\theta(v_0, v_1, \dots, v_m)$, $v$ being $v_0$ and $\bar c$ the values of $v_1, \dots, v_m$. It is coded by some $s$ (:ref{#thm-ssy-turing-ideal}). Let
$$
\varphi(k) \equiv \exists v\ \forall z < k\ \big( z \in s \rightarrow S(z, \langle v, \bar c \rangle) \big).
$$
For standard $k$, finitely many standard formulas of $p$ have codes below $k$ in $s$; a common realizer $v$ satisfies $\varphi(k)$, by condition 2. The set $\{ k : (M, S) \models \varphi(k) \}$ is an initial segment containing $\nat$. It is not $\nat$: otherwise $\varphi$ would define $\nat$ in $(M, S)$, and induction for $\varphi$ in $(M, S)$ would give $\varphi(k)$ for every $k$, since $\nat$ contains $0$ and is closed under successor. So $\varphi(k)$ holds for a non-standard $k$; a witness $v$ satisfies $S(\ulcorner \theta \urcorner, \langle v, \bar c \rangle)$ for every $\theta \in p$, since its code is standard, below $k$ and in $s$, and so $M \models \theta(v, \bar c)$ by condition 2.

($\Rightarrow$) Let $\Psi$ be the set of $\mathcal L_A \cup \{ S \}$-sentences consisting of the induction axioms for all formulas of $\mathcal L_A \cup \{ S \}$ and the sentences of condition 2 for all standard $\theta$. It is recursive and has no parameters. It is consistent with $\mathrm{ElemDiag}(M)$: a finite part mentions condition 2 for finitely many formulas $\theta_1, \dots, \theta_m$ only; let $S_0 \subseteq M^2$ be defined in $M$ by $\bigvee_j \big( z = \ulcorner \theta_j \urcorner \wedge \theta_j(e(0), \dots, e(k_j)) \big)$. Since $S_0$ is definable in $M$, every formula of $\mathcal L_A \cup \{ S \}$ is equivalent in $(M, S_0)$ to a formula of $\mathcal L_A$, so the induction axioms hold in $(M, S_0)$, as $M \models \mathrm{PA}$; and condition 2 holds for $\theta_1, \dots, \theta_m$, the codes being distinct. So $(M, S_0)$ satisfies the finite part and $\mathrm{ElemDiag}(M)$. By :ref{#thm-barwise-ressayre}, $M$ has an expansion $(M, S) \models \Psi$.
:::

:::quiz[inductive satisfaction classes]
In the direction ($\Leftarrow$) of :ref{#thm-inductive-sat}, which property of $S$ replaces the truth definitions $\mathrm{Sat}_{\Sigma_n}$ used in :ref{#lem-fe-realize}?

- [x] $S$ evaluates the standard formulas of every complexity at once, and induction holds for formulas mentioning $S$, so overspill applies to $\varphi$; no truth definition of $M$ covers all complexities.
- [ ] $S$ is definable in $M$.

  No relation satisfying condition 2 is definable in $M$, by Tarski's argument (:ref{#ex-inductive-sat-undefinable}).
- [ ] $S$ is correct on non-standard formulas.

  Nothing is required of $S$ on non-standard codes; the realizer is only checked on standard formulas.
:::

The theorem shows how close recursive saturation is to truth: a countable model of $\mathrm{PA}$ is recursively saturated exactly when it can be expanded by a predicate that is a satisfaction relation for standard formulas and satisfies induction. The next two lessons study the dual situation, where the predicate must satisfy Tarski's conditions on all formulas of the model, standard or not, and no induction is required.

::::exercise{#ex-inductive-sat-undefinable difficulty=2 objective="Adapt Tarski's diagonal argument to show that satisfaction for standard formulas is not definable with parameters."}
Let $M$ be a model of $\mathrm{PA}$. Show that no $S \subseteq M^2$ satisfying condition 2 of :ref{#def-inductive-sat} is definable in $M$ with parameters.

:::solution
Suppose $S$ is defined by $\sigma(z, e, c)$, with a parameter $c$ (several parameters are paired into one). Let $\theta(v_0, v_1)$ be the formula $\neg \sigma(v_0, \langle v_0, v_1 \rangle, v_1)$, with $\langle v_0, v_1 \rangle$ the sequence of length $2$, and $d = \ulcorner \theta \urcorner$, a standard number. By condition 2, applied with $e = \langle d, c \rangle$, $S(d, \langle d, c \rangle)$ holds if and only if $\theta(d, c)$, that is, if and only if $\neg \sigma(d, \langle d, c \rangle, c)$, that is, if and only if $\neg S(d, \langle d, c \rangle)$, a contradiction.
:::
::::

## Notes and references

:ref{#thm-barwise-ressayre} was proved by Barwise with admissible sets (*Admissible Sets and Structures*, Theorem IV.5.7, as cited by Wong) and by Ressayre (1977, Theorem 2.3); the proof here is Ressayre's, as presented in Wong's Lecture 7. :ref{#lem-craig} is Craig's trick (1953). :ref{#thm-inductive-sat} is the content of the further exercises (a)–(c) of Wong's Lecture 7. Schlipf (1977) proved that countable recursively saturated structures are even chronically resplendent: the expansion can be chosen resplendent (Wong, Theorem 14.5); whether every resplendent structure is chronically resplendent was asked by Schlipf.

- J. Barwise, *Admissible Sets and Structures*, Springer, 1975.
- J.-P. Ressayre, *Models with compactness properties relative to an admissible language*, Annals of Mathematical Logic 11 (1977), 31–55.
- W. Craig, *On axiomatizability within a system*, Journal of Symbolic Logic 18 (1953), 30–32.
- J. S. Schlipf, *Toward model theory through recursive saturation*, Journal of Symbolic Logic 43 (1978), 183–206.
- J. S. Schlipf, *A guide to the identification of admissible sets above structures*, Annals of Mathematical Logic 12 (1977), 151–192.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 7 and 14.
- R. Kaye, *Models of Peano Arithmetic*, Oxford University Press, 1991.

:::::exercises
::::exercise{#ex-craig-theorem difficulty=1 objective="Apply Craig's trick to theories: every theory with a computably enumerable set of axioms has a computable set of axioms."}
Let $\mathcal L$ be a recursive language and $\Gamma$ a set of $\mathcal L$-sentences whose set of codes is computably enumerable. Show that some computable set $\Gamma'$ of $\mathcal L$-sentences has the same models as $\Gamma$, hence the same consequences.

:::solution
If $\Gamma$ is empty, take $\Gamma' = \Gamma$. Otherwise let $\sigma_0, \sigma_1, \dots$ be a computable enumeration of $\Gamma$, possibly with repetitions, and $\Gamma' = \{ \sigma_n^{(n+1)} : n \in \nat \}$, where $\sigma^{(n+1)}$ is the conjunction of $n + 1$ copies of $\sigma$. To decide whether a sentence $\eta$ belongs to $\Gamma'$, check, for each $n$ smaller than the length of $\eta$, whether $\eta$ is the conjunction of $n + 1$ copies of a sentence $\sigma$, and if so compute $\sigma_n$ and compare it with $\sigma$; finitely many computations, each terminating. Each $\sigma_n^{(n+1)}$ is logically equivalent to $\sigma_n$, so a structure satisfies $\Gamma'$ if and only if it satisfies $\Gamma$. This is Craig's theorem (1953), of which :ref{#lem-craig} is the version for types.
:::
::::

::::exercise{#ex-respl-consistency-theory difficulty=2 objective="Show by compactness that, without parameters, consistency with the elementary diagram reduces to consistency with the theory."}
Let $M$ be a structure for a recursive language $\mathcal L$, $\mathcal L^* \supseteq \mathcal L$, and $\Phi$ a set of $\mathcal L^*$-sentences without parameters from $M$. Show that $\Phi$ is consistent with $\mathrm{ElemDiag}(M)$ if and only if it is consistent with $\mathrm{Th}(M)$. Deduce that if $M$ and $N$ are countable recursively saturated structures with $\mathrm{Th}(M) = \mathrm{Th}(N)$ and $\Phi$ is recursive, then $M$ has an expansion satisfying $\Phi$ if and only if $N$ has one.

:::solution
Since $\mathrm{Th}(M) \subseteq \mathrm{ElemDiag}(M)$, one direction is clear. Suppose $\Phi \cup \mathrm{Th}(M)$ has a model $K^*$, and that $\Phi \cup \mathrm{ElemDiag}(M)$ is inconsistent. By compactness, there are a finite $\Phi_0 \subseteq \Phi$ and a sentence $\alpha(\bar c) \in \mathrm{ElemDiag}(M)$, a conjunction of finitely many, with its parameters $\bar c$ displayed, such that $\Phi_0 \vdash \neg \alpha(\bar c)$. The constants $\bar c$ do not occur in $\Phi_0$, so $\Phi_0 \vdash \forall \bar w\ \neg \alpha(\bar w)$. But $\exists \bar w\ \alpha(\bar w)$ belongs to $\mathrm{Th}(M)$, so it holds in $K^*$, which also satisfies $\Phi_0$: a contradiction.

If $\mathrm{Th}(M) = \mathrm{Th}(N)$, the first part shows that $\Phi$ is consistent with $\mathrm{ElemDiag}(M)$ if and only if it is consistent with $\mathrm{ElemDiag}(N)$. By :ref{#thm-barwise-ressayre}, applied with no parameters, the first condition is equivalent to the existence of an expansion of $M$ satisfying $\Phi$, and the second to that of an expansion of $N$; an expansion satisfying $\Phi$ makes $\Phi$ consistent with the elementary diagram.
:::
::::

::::exercise{#ex-respl-definable-model difficulty=2 objective="See why recursive saturation is needed in the theorem of Barwise and Ressayre, with the model of definable elements." lessons="recursively-saturated-models"}
Let $T$ be a complete consistent extension of $\mathrm{PA}$ other than the theory of $\nat$, and $K$ the model of $T$ formed by the elements definable without parameters in some model of $T$ (:ref{#prop-rs-definable}). Let $\Psi$ be the recursive set of sentences of the proof of :ref{#thm-inductive-sat}, which says that $S$ is an inductive partial satisfaction class. Show that $\Psi$ is consistent with $\mathrm{ElemDiag}(K)$, but that $K$ has no expansion satisfying $\Psi$.

:::solution
By :ref{#thm-rs-existence}, $T$ has a countable recursively saturated model $M$, non-standard since it satisfies $T$ and is recursively saturated. By :ref{#thm-inductive-sat}, $M$ has an expansion $(M, S) \models \Psi$, so $\Psi$ is consistent with $\mathrm{Th}(M) = T = \mathrm{Th}(K)$. The set $\Psi$ has no parameters, so it is consistent with $\mathrm{ElemDiag}(K)$ by :ref{#ex-respl-consistency-theory}.

The model $K$ is countable and non-standard, and it is not recursively saturated, by :ref{#prop-rs-definable}. If $(K, S) \models \Psi$, then $S$ is an inductive partial satisfaction class for $K$, and the direction ($\Leftarrow$) of :ref{#thm-inductive-sat} shows that $K$ is recursively saturated, a contradiction. So the conclusion of :ref{#thm-barwise-ressayre} fails for $K$.
:::
::::

::::exercise{#ex-inductive-sat-theory difficulty=2 objective="Use induction for an inductive satisfaction class to code the theory of the model in its standard system." lessons="recursively-saturated-models, fragments-of-arithmetic/ackermann-coding"}
Let $M$ be a non-standard model of $\mathrm{PA}$ with an inductive partial satisfaction class $S$. Show directly, using induction in $(M, S)$, that $\mathrm{Th}(M) \in \mathrm{SSy}(M)$.

:::solution
Let $\psi(b) \equiv \exists c\ \big( c < 2^b \wedge \forall z < b\ (z \in c \leftrightarrow S(z, 0)) \big)$, a formula of $\mathcal L_A \cup \{ S \}$. It holds for $b = 0$, with $c = 0$. Suppose $\psi(b)$, with a witness $c$. Every element of $c$ is less than $b$ (:ref{#lem-ack-basic}, item 3), so $b \notin c$. If $S(b, 0)$, let $c' = c + 2^b$, which codes the elements of $c$ together with $b$ (item 4); otherwise $c' = c$. In both cases $c' < 2^{b+1}$ and $c'$ witnesses $\psi(b + 1)$. By induction in $(M, S)$, $\psi(b)$ holds for every $b$.

Take $b$ non-standard and $c$ a witness. For a standard number $z$, $z \in c$ if and only if $S(z, 0)$. If $z$ is the code of a sentence $\sigma$, condition 2 of :ref{#def-inductive-sat} gives $S(\ulcorner \sigma \urcorner, 0) \leftrightarrow M \models \sigma$. So $\mathrm{Th}(M)$ is the intersection of $\mathrm{Ack}(c) \cap \nat$ with the computable set of codes of sentences, and belongs to $\mathrm{SSy}(M)$ by :ref{#thm-ssy-turing-ideal}. By :ref{#thm-inductive-sat}, $M$ is recursively saturated when it is countable, and this agrees with :ref{#prop-rs-realized-coded}; the argument above does not use countability.
:::
::::
:::::
