---
title: End extensions from consistency
summary: Applications of the arithmetized completeness theorem. Every model of IΣ₁ is a proper exponential cut of a model of IΔ₀ + exp; every model of PA has, for each n, a proper Σₙ-elementary end extension satisfying PA; a model of PA + Con(PA) has an end extension satisfying PA + ¬Con(PA), which is not Σ₁-elementary.
duration: 45
prerequisites: [arithmetized-completeness, cuts-and-extensions/collection-end-extensions, truth-and-provability/finite-axiomatizability]
---

The arithmetized completeness theorem turns a consistency statement true in $M$ into an end extension of $M$. To use it, one needs consistency statements that $M$ satisfies, and these come from proof theory: a theory proves the consistency of weaker theories. This lesson gives three applications, each paired with a consistency fact that we admit. They show both the strength of the method, which applies to models of any cardinality, and its limits: the end extensions it produces satisfy the standard axioms of a theory, but they need not be elementary, and in general they cannot be. Elementary end extensions require the different method of the next lessons.

## Exponential cuts

The extensions given by :ref{#thm-ee-act} need not be proper. A new constant forces properness.

:::lemma{#lem-ee-proper-end}
Let $M$, $T$ be as in :ref{#thm-ee-act}, with $M \models \mathrm{Con}(T)$, let $d$ be a constant symbol that does not occur in $T$, and let $T' = T \cup \{ d > \bar a : a \in M \}$. Then $T'$ is a theory of $M$ with $M \models \mathrm{Con}(T')$, and $M$ has a proper end extension $K$ that satisfies the conclusions of :ref{#thm-ee-act} for $T'$.

:::proof{of=lem-ee-proper-end}
The set of sentences $d > \bar a$, $a \in M$, is $\Delta_1$-definable, since $a \mapsto \bar a$ is $\Delta_1$; so $T'$ is $\Delta_1$-definable. Suppose $M \models \neg \mathrm{Con}(T')$, and let $p$ be a proof of $0 = 1$. The sentences $d > \bar a$ that it uses have codes below $p$, so they are among those with $a < b$ for some $b$, and $T \cup F$ is inconsistent for $F = \{ d > \bar a : a < b \}$. By item 6 of :ref{#fact-ee-logic}, with $t = \bar b$, $T \cup \{ \bar b > \bar a : a < b \}$ is inconsistent. By item 4, $T$ proves each of these sentences, so $T$ is inconsistent by item 3, contradicting $\mathrm{Con}(T)$. Apply :ref{#thm-ee-act} to $T'$: the resulting $K$ satisfies $d^K > a$ for every $a \in M$, by item 2, so $d^K \notin M$.
:::


:::fact[Consistency of IΔ₀ + exp]{#fact-ee-con-efa}
$\mathrm I\Sigma_1$ proves $\mathrm{Con}(\mathrm I\Delta_0 + \mathrm{exp})$, where $\mathrm I\Delta_0 + \mathrm{exp}$ is the theory of $M$ defined by the natural $\Delta_1$ definition of its axioms.
:::

The proof is proof-theoretic: it uses the elimination of cuts, which needs the totality of a function growing faster than all iterated exponentials, provable in $\mathrm I\Sigma_1$ (:ref{#thm-pr-provably-total}). Simpson proves the statement in $\mathrm{RCA}_0$ (Theorem II.8.11, "consistency of EFA"), whose first-order consequences are those of $\mathrm I\Sigma_1$; Wong uses it as Fact 4.10.

:::theorem{#thm-ee-exp-cut}
Every model $M$ of $\mathrm I\Sigma_1$ has a proper end extension $K \models \mathrm I\Delta_0 + \mathrm{exp}$. $M$ is a proper exponential cut of $K$.
:::

:::proof{of=thm-ee-exp-cut}
Every axiom of $\mathrm I\Delta_0 + \mathrm{exp}$ is a standard element of $M$ satisfying the definition of the axioms, so $M$'s version of the theory contains all of them, possibly with non-standard instances of induction as well; it contains $\mathrm{PA}^-$. By :ref{#fact-ee-con-efa}, $M$ satisfies its consistency. By :ref{#lem-ee-proper-end}, $M$ has a proper end extension $K$ satisfying every standard axiom, that is, $K \models \mathrm I\Delta_0 + \mathrm{exp}$. The cut $M$ of $K$ is closed under exponentiation: for $a \in M$, the power $2^a$ of $M$ satisfies the bounded formula of :ref{#def-exp} in $M$, hence in $K$ by :ref{#lem-delta0-absolute}, so it is the power $2^a$ of $K$.
:::

By :ref{#thm-scott-wkl-cut}, the pair $(M, \mathrm{Cod}(K/M))$ then satisfies weak König's lemma, and by :ref{#ex-ee-cod-delta2}, the sets in $\mathrm{Cod}(K/M)$ are $\Delta_2$-definable in $M$. The theorem is the first-order half of a converse to Scott's theorem. The full converse concerns a model $(M, \mathcal X)$ of $\mathrm{WKL}_0$ and asks for $K$ with $\mathrm{Cod}(K/M) = \mathcal X$: for countable models it is due to Scott and Tanaka, and Wong proves it (Theorem 4.13, following Enayat) by iterating a second-order version of the arithmetized completeness theorem, in which the theory and the path are taken from $\mathcal X$.

## Partially elementary end extensions of models of PA

A model of $\mathrm{PA}$ satisfies the consistency of each finite part of $\mathrm{PA}$, and more: of each $\mathrm I\Sigma_k$ together with all true sentences of bounded complexity. For $n \geq 1$, let $\mathrm{Tr}_{\Sigma_n}$ be the set of the $\Sigma^*_n$ sentences $\sigma$ of $M$ in $\mathcal L_A$ such that $\mathrm{Sat}_{\Sigma_n}(\sigma, 0)$ (:ref{#def-sat-n}); their closed terms include the numerals $\bar a$ of all $a \in M$, standard or not. It is $\Sigma_n$-definable in $M$, not $\Delta_1$, and $\mathrm{Con}$ is defined for it as for theories of $M$, with a $\Sigma_n$ formula in place of the $\Delta_1$ definition of the axioms. Let $\mathrm I\Sigma^*_k$ be the theory of $M$ consisting of $\mathrm{PA}^-$ and the induction axioms for $\Sigma^*_j$ formulas, $j \leq k$; it is $\Delta_1$-definable uniformly in $k$, also for non-standard $k$.

:::fact[Reflection]{#fact-ee-reflection}
Let $n \geq 1$.

1. For every $k \in \nat$, $\mathrm{PA}$ proves $\mathrm{Con}(\mathrm I\Sigma^*_k \cup \mathrm{Tr}_{\Sigma_n})$.
2. For every standard $\Sigma^*_n$ formula $\varphi(\bar x)$, $\mathrm I\Sigma_1$ proves $\forall \bar a\ \big(\mathrm{Sat}_{\Sigma_n}(\varphi(\bar{\bar a}), 0) \leftrightarrow \varphi(\bar a)\big)$.
:::

Item 1 follows from Theorem I.4.33 of Hájek and Pudlák, $\mathrm I\Sigma_j \vdash \mathrm{Con}(\mathrm{Tr}_{\Pi_{j+1}})$ for $j \geq 1$, in the way their Corollary I.4.34 derives $\mathrm I\Sigma_{k+1} \vdash \mathrm{Con}(\mathrm I\Sigma_k)$. Their $\mathrm{Tr}_{\Pi_{j+1}}$ is the set of all true $\Pi^*_{j+1}$ sentences in the sense of the model, closed terms included, so it contains the sentences with numerals of non-standard elements; their Corollary I.4.34(2) uses this for a single true sentence. For $j = \max(k + 1, n)$, $\mathrm I\Sigma_j$ proves that every axiom of $\mathrm I\Sigma^*_k$, standard or not, is equivalent, by a prenex transformation carried out uniformly in $\mathrm I\Sigma_1$, to a true $\Pi^*_{k+2}$ sentence (the truth of the induction axioms uses induction for $\mathrm{Sat}_{\Sigma_k}$), and that every sentence of $\mathrm{Tr}_{\Sigma_n}$ is a true $\Pi^*_{j+1}$ sentence. The proof of Theorem I.4.33 interprets the Skolem functions of finitely many true sentences by least witnesses and checks the resulting open theory in the universe. Item 2 is :ref{#cor-snowing} together with the evaluation of numerals.

:::remark{#rem-ee-act-relativized}
With :ref{#rem-ee-low-basis-relativized}, :ref{#thm-ee-act} holds for $M \models \mathrm I\Sigma_{m+1}$ and a theory $T$ that is $\Delta_{m+1}$-definable in $M$, with $H$ now $\Delta_{m+2}$-definable: the facts of logic relativize, a $\Sigma_1$ formula in a $\Delta_{m+1}$-definable set being $\Sigma_{m+1}$. The proof below uses this case with $m = n + 1$.
:::

:::theorem{#thm-ee-sigma-n-end}
Let $M \models \mathrm{PA}$ and $n \in \nat$. Then $M$ has a proper end extension $K \models \mathrm{PA}$ with $M \preccurlyeq_n K$.
:::

**Idea.** $M$ cannot express the consistency of its whole elementary diagram, but it expresses the consistency of its $\Sigma_{n+1}$ diagram through the partial truth definition $\mathrm{Sat}_{\Sigma_{n+1}}$. Overspill then replaces "each $\mathrm I\Sigma_k$" by a single $\mathrm I\Sigma^*_b$ with $b$ non-standard, which contains every axiom of $\mathrm{PA}$.

:::proof{of=thm-ee-sigma-n-end}
We may take $n \geq 1$, and assume that $M$ is non-standard, since a proper elementary extension of $\nat$ is an end extension (:ref{#prop-standard-part}). Let $\theta(x)$ be the formula $\mathrm{Con}(\mathrm I\Sigma^*_x \cup \mathrm{Tr}_{\Sigma_{n+1}})$. By item 1 of :ref{#fact-ee-reflection}, $M \models \theta(k)$ for every $k \in \nat$. By overspill (:ref{#cor-overspill}, applied in $M \models \mathrm{PA}$ to the standard cut), $M \models \theta(b)$ for some non-standard $b$.

The theory $T = \mathrm I\Sigma^*_b \cup \mathrm{Tr}_{\Sigma_{n+1}} \cup \{ d > \bar a : a \in M \}$, with a new constant $d$, is $\Delta_{n+2}$-definable in $M$, and $M \models \mathrm{Con}(T)$ by the argument of :ref{#lem-ee-proper-end}, which uses only the facts of logic. By :ref{#thm-ee-act}, in the relativized form of :ref{#rem-ee-act-relativized} with $m = n + 1$, there is $K \supseteq_e M$ satisfying every standard sentence of $T$, with $d^K \notin M$. For each standard $k < b$, every standard axiom of $\mathrm I\Sigma^*_k$ is a standard sentence of $T$, so $K$ satisfies $\mathrm{PA}^-$ and induction for all $\Sigma^*_k$ formulas; by :ref{#lem-isigma-star}, $K \models \mathrm I\Sigma_k$ for every $k$, that is, $K \models \mathrm{PA}$.

Let $\varphi(\bar x)$ be a $\Sigma_n$ formula and $\bar a \in M$. By :ref{#lem-variable-bounds}, $\varphi$ is equivalent in $\mathrm I\Sigma_1$ to a $\Sigma^*_n$ formula $\varphi^*$, and $\neg \varphi$ to a $\Pi^*_n$ formula $\varphi^-$; both are $\Sigma^*_{n+1}$ formulas, and the equivalences hold in $M$ and in $K$. If $M \models \varphi(\bar a)$, then $\mathrm{Sat}_{\Sigma_{n+1}}(\varphi^*(\bar{\bar a}), 0)$ holds in $M$ by item 2 of the fact, so $\varphi^*(\bar{\bar a}) \in T$, and $K \models \varphi^*(\bar a)$ by item 2 of :ref{#thm-ee-act}; so $K \models \varphi(\bar a)$. The same argument with $\varphi^-$ shows that $M \models \neg \varphi(\bar a)$ implies $K \models \neg \varphi(\bar a)$. So $M \preccurlyeq_n K$.
:::

:::quiz[partially elementary end extensions]
Why does the proof use $\mathrm I\Sigma^*_b$ with $b$ non-standard, rather than the theory $\mathrm{PA}$ of $M$?

- [x] $M$ need not satisfy the consistency of its version of $\mathrm{PA}$ together with $\mathrm{Tr}_{\Sigma_{n+1}}$; it satisfies the consistency of each $\mathrm I\Sigma^*_k \cup \mathrm{Tr}_{\Sigma_{n+1}}$ with $k$ standard, and overspill gives a non-standard $b$, so that $\mathrm I\Sigma^*_b$ still contains every standard axiom of $\mathrm{PA}$.
- [ ] Because $\mathrm{PA}$ is not $\Delta_1$-definable in $M$.

  Its axioms form a $\Delta_1$-definable set; the obstacle is consistency.
- [ ] Because $K$ would otherwise be equal to $M$.

  Properness comes from the constant $d$.

---

Why does the argument give $M \preccurlyeq_n K$ for a fixed $n$, and not $M \preccurlyeq K$?

- [x] The theory $T$ contains the $\Sigma_{n+1}$ diagram of $M$ through the partial truth definition $\mathrm{Sat}_{\Sigma_{n+1}}$; the full elementary diagram is not definable in $M$, by Tarski's theorem relativized to $M$.
- [ ] Because $K$ satisfies only $\mathrm I\Sigma_b$.

  $K$ satisfies all of $\mathrm{PA}$, since it satisfies every standard axiom of $\mathrm I\Sigma^*_b$.
- [ ] Because overspill applies only to $\Sigma_n$ formulas.

  In a model of $\mathrm{PA}$, overspill applies to formulas of any complexity.
:::

For countable models, the same result follows from recursive saturation (Wong, introduction to Lecture 9), and an omitting types argument even gives elementary end extensions. The arithmetized completeness theorem needs no countability, but it reaches only a fixed level of elementarity.

## An end extension that is not elementary

The theory used need not be true in $M$. By Gödel's second incompleteness theorem, formalized in $\mathrm{PA}$, $\mathrm{PA}$ proves $\mathrm{Con}(\mathrm{PA}) \rightarrow \mathrm{Con}(\mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA}))$: if $\mathrm{PA} + \neg\mathrm{Con}(\mathrm{PA})$ is inconsistent, then $\mathrm{PA}$ proves $\mathrm{Con}(\mathrm{PA})$, and then $\mathrm{PA}$ is inconsistent, an implication that $\mathrm{PA}$ proves (Hájek and Pudlák, Chapter III, Section 2). We admit it.

:::theorem{#thm-ee-not-elementary}
Every model $M$ of $\mathrm{PA} + \mathrm{Con}(\mathrm{PA})$ has a proper end extension $K \models \mathrm{PA} + \neg\mathrm{Con}(\mathrm{PA})$. The extension is not $\Sigma_1$-elementary.
:::

:::proof{of=thm-ee-not-elementary}
$M$ satisfies $\mathrm{Con}(\mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA}))$, so :ref{#thm-ee-act} gives $K \supseteq_e M$ satisfying every standard sentence of this theory, that is, $K \models \mathrm{PA} + \neg \mathrm{Con}(\mathrm{PA})$. The $\Sigma_1$ sentence $\neg\mathrm{Con}(\mathrm{PA})$ holds in $K$ and fails in $M$; so $M \not\preccurlyeq_1 K$ and $K \neq M$.
:::

The proof of $0 = 1$ that $K$ contains lies above $M$: no element of $M$ is a proof, since $M \models \mathrm{Con}(\mathrm{PA})$ and the proof predicate of $\mathrm{PA}$, which is $\Delta_1$, has the same value at elements of $M$ in $M$ and in $K$ (:ref{#cor-sigma1-upward}, applied to its $\Sigma_1$ definition and to that of its negation). The extension is $\Sigma_0$-elementary, as every end extension (:ref{#lem-delta0-absolute}), and :ref{#thm-end-ext-collection} with $n = 0$ only says that $M \models \mathrm B\Sigma_1$, which is known. By the same theorem, a proper end extension $K \models \mathrm{PA}$ with $M \preccurlyeq_n K$ for all $n$ would show that $M$ satisfies every $\mathrm B\Sigma_{n+1}$; the next lessons show that every model of $\mathrm{PA}$ has such an extension.

## Exercises

::::exercise{#ex-ee-sigma1-up difficulty=1}
Let $M \subseteq_e K$ with $K$ given by :ref{#thm-ee-not-elementary}. Show that every $\Sigma_1$ formula with parameters in $M$ that holds in $M$ holds in $K$, and give a $\Pi_1$ sentence true in $M$ and false in $K$.

:::solution
The first statement is :ref{#cor-sigma1-upward}, since $M \subseteq_e K$. The sentence $\mathrm{Con}(\mathrm{PA})$ is $\Pi_1$, true in $M$ and false in $K$.
:::
::::

::::exercise{#ex-ee-con-sigma1 difficulty=1}
Let $M \models \mathrm{PA} + \mathrm{Con}(\mathrm{PA})$ and let $K \models \mathrm{PA}$ be an end extension of $M$ with $M \preccurlyeq_1 K$. Show that $K \models \mathrm{Con}(\mathrm{PA})$, and deduce that the extension of :ref{#thm-ee-not-elementary} cannot be obtained from :ref{#thm-ee-sigma-n-end}.

:::solution
$\mathrm{Con}(\mathrm{PA})$ is a $\Pi_1$ sentence true in $M$; its negation is $\Sigma_1$, and if it held in $K$ it would hold in $M$ by $M \preccurlyeq_1 K$. So $K \models \mathrm{Con}(\mathrm{PA})$. The extensions of :ref{#thm-ee-sigma-n-end} with $n \geq 1$ therefore satisfy $\mathrm{Con}(\mathrm{PA})$ when $M$ does, while that of :ref{#thm-ee-not-elementary} does not: the two theorems use the arithmetized completeness theorem with theories that contain, respectively, the true $\Sigma_{n+1}$ sentences of $M$ and a sentence false in $M$.
:::
::::

::::exercise{#ex-ee-cod-delta2 difficulty=2}
In the situation of :ref{#thm-ee-act}, show that every set $\mathrm{Ack}(d) \cap M$, for $d \in K$, is $\Delta_2$-definable in $M$.

:::solution
Let $d = [c]$ for a constant $c$. For $x \in M$, $x = [c_x]$, where $x \mapsto c_x$ is a $\Delta_1$ function, the Henkin constant of the formula $v = \bar x$. By item 3, $x \in \mathrm{Ack}(d)$ in $K$ if and only if the sentence $c_x \in \mathrm{Ack}(c)$, with the bounded formula of :ref{#def-ack-membership}, belongs to $H$. The map from $x$ to this sentence is $\Delta_1$, and $H$ is $\Delta_2$-definable; so $\mathrm{Ack}(d) \cap M$ is $\Delta_2$-definable.
:::
::::

## Notes and references

:ref{#thm-ee-exp-cut} is the first-order part of Wong's Corollary 4.11, proved there for the first-order part of a model of $\mathrm{WKL}_0$; Wong's Theorem 4.13 (Scott, Tanaka; proof of Enayat) gives the converse to Scott's theorem for countable models of $\mathrm{WKL}_0$. :ref{#fact-ee-con-efa} is Simpson's Theorem II.8.11. :ref{#fact-ee-reflection} follows from Theorem I.4.33 and Corollary I.4.34 of Hájek and Pudlák; the latter also gives $\mathrm I\Sigma_{k+1} \vdash \mathrm{Con}(\mathrm I\Sigma_k)$. The use of the arithmetized completeness theorem to build end extensions of models of $\mathrm{PA}$ goes back to the work of McAloon cited in the previous lesson; Smoryński's lectures survey its applications.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009, Section II.8.
- K. Tanaka, *The self-embedding theorem of WKL₀ and a non-standard method*, Annals of Pure and Applied Logic 84 (1997), 41–49.
- A. Enayat, *A new proof of Tanaka's theorem*, in New Studies in Weak Arithmetics, CSLI Lecture Notes 211, 2013, 93–102.
- C. Smoryński, *Lectures on nonstandard models of arithmetic*, in Logic Colloquium '82, North-Holland, 1984, 1–70.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 4(c), and Chapter III, Section 2.
- T. L. Wong, *Model theory of arithmetic*, lecture notes, Lectures 4 and 9.
