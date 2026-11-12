---
title: PA degrees
summary: Sets computing a diagonally non-computable {0,1}-valued function; equivalence with computing a member of every non-empty Π⁰₁ class and with separating disjoint c.e. sets; completions of Peano arithmetic.
duration: 45
prerequisites: [basis-theorems]
---

Some sets compute a member of every non-empty $\Pi^0_1$ class: they can solve, uniformly, every problem whose solutions form a $\Pi^0_1$ class. These sets are characterized by a simple diagonal property — they compute a $\{0, 1\}$-valued function that differs from every computable function on the diagonal — and, historically, by their ability to compute a complete consistent extension of Peano arithmetic. Their degrees are the **PA degrees**. They are not necessarily complete, and not even necessarily above any given non-computable set: by the basis theorems, there are low PA degrees.

## Definition and characterizations

:::definition{#def-pa-degree}
A set $X$ is **of PA degree**, or **PA**, if $X$ computes a member of $\mathrm{DNC}_2$, that is, a function $f : \nat \to \{0, 1\}$ with $f(e) \neq \Phi_e(e)$ for every $e$ such that $\Phi_e(e)\converge$.
:::

The class of PA sets is closed upward under Turing reducibility. By :ref{#thm-dnc2-no-computable}, no computable set is PA. The halting set is PA: the function $f(e) = 1$ if $\Phi_e(e)\converge = 0$, and $f(e) = 0$ otherwise, is computable in $\emptyset'$ and belongs to $\mathrm{DNC}_2$.

The three properties of the next theorem describe the same power in three ways: a single diagonal task, a uniform family of separation tasks, and the solution of every problem with a $\Pi^0_1$ set of solutions. The proof turns each task into the next. A separation problem is reduced to the diagonal by a program whose behavior on its own index encodes the problem (SMN). A $\Pi^0_1$ class is reduced to separation by racing the enumerations of the non-extendible nodes: at each node, the separating set chooses a successor that is not seen to die first.

:::figure[The characterizations of PA sets, with the main idea of each implication proved in this lesson.]
<svg class="fig" viewBox="0 0 600 226" width="600" role="img" aria-label="Four equivalent properties of a set X, with the implications proved in the lesson"><defs><marker id="ah-pa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="20" y="20" width="230" height="54" rx="6" class="state"/><text x="135.0" y="43" text-anchor="middle" font-size="13">X computes a member of DNC₂</text><text x="135.0" y="61" text-anchor="middle" font-size="13">(X is PA)</text><rect x="350" y="20" width="230" height="54" rx="6" class="state"/><text x="465.0" y="43" text-anchor="middle" font-size="13">X computes a separating set</text><text x="465.0" y="61" text-anchor="middle" font-size="13">for all disjoint c.e. A, B</text><rect x="350" y="150" width="230" height="54" rx="6" class="state"/><text x="465.0" y="173" text-anchor="middle" font-size="13">X computes a member of every</text><text x="465.0" y="191" text-anchor="middle" font-size="13">non-empty Π⁰₁ class</text><rect x="20" y="150" width="230" height="54" rx="6" class="state"/><text x="135.0" y="173" text-anchor="middle" font-size="13">X computes a complete consistent</text><text x="135.0" y="191" text-anchor="middle" font-size="13">extension of Peano arithmetic</text><line x1="252" y1="47" x2="348" y2="47" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/><text x="300" y="40" text-anchor="middle" class="label">SMN</text><line x1="465" y1="76" x2="465" y2="148" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/><text x="473" y="116" text-anchor="start" class="label">race of enumerations</text><line x1="348" y1="177" x2="252" y2="177" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/><text x="300" y="170" text-anchor="middle" class="label">completions</text><line x1="350" y1="152" x2="252" y2="74" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/><text x="318" y="100" text-anchor="start" class="label">DNC₂ is Π⁰₁</text><line x1="135" y1="148" x2="135" y2="76" class="ink-stroke" stroke-width="1.3" marker-end="url(#ah-pa)"/><text x="127" y="116" text-anchor="end" class="label">f(e) from</text><text x="127" y="132" text-anchor="end" class="math" font-size="14">θ<tspan class="mrm" font-size="10" dy="4">e,0</tspan><tspan class="label" dy="-4"> ∈ S</tspan></text></svg>
:::

:::theorem{#thm-pa-characterization}
For every set $X$, the following are equivalent:

1. $X$ is PA;
2. for every pair of disjoint c.e. sets $A$ and $B$, $X$ computes a set $C$ separating them: $A \subseteq C$ and $C \cap B = \emptyset$;
3. $X$ computes a member of every non-empty $\Pi^0_1$ class.
:::

:::proof{of=thm-pa-characterization}
(1 ⇒ 2) Let $f \leq_T X$ be a member of $\mathrm{DNC}_2$, and $A$, $B$ disjoint c.e. sets. By the parameter form of SMN, there is a computable $q$ such that the program $q(n)$, on any input, enumerates $A$ and $B$, outputs $0$ if $n$ appears in $A$, and $1$ if $n$ appears in $B$; it diverges if $n$ belongs to neither. So $\Phi_{q(n)}(q(n)) = 0$ if $n \in A$, $= 1$ if $n \in B$, and diverges otherwise. Let $C = \{ n : f(q(n)) = 1 \}$, computable in $X$. If $n \in A$, then $f(q(n)) \neq 0$, so $n \in C$; if $n \in B$, then $f(q(n)) \neq 1$, so $n \notin C$.

(2 ⇒ 3) Let $\mathcal P = [T]$ be non-empty, with $T$ computable. For a string $\sigma$, non-extendibility of $\sigma 0$ and of $\sigma 1$ are $\Sigma^0_1$ properties (:ref{#prop-pi01-emptiness}); fix enumerations of them by stages. Let $A$ be the set of strings $\sigma$ such that the non-extendibility of $\sigma 0$ is confirmed at some stage $s$ and that of $\sigma 1$ is not confirmed at any stage $t < s$, and $B$ the set of strings $\sigma$ such that the non-extendibility of $\sigma 1$ is confirmed at some stage $s$ and that of $\sigma 0$ is not confirmed at any stage $t \leq s$. These sets are c.e. and disjoint, so $X$ computes a set $C$ separating them. Define $\sigma_0 = \varepsilon$ and $\sigma_{n+1} = \sigma_n 1$ if $\sigma_n \in C$, $\sigma_{n+1} = \sigma_n 0$ otherwise. We show by induction that $\sigma_n$ is extendible. If $\sigma_n$ is extendible, at least one of its successors is. If both are, so is $\sigma_{n+1}$. If only $\sigma_n 1$ is, then the non-extendibility of $\sigma_n 0$ is confirmed at some stage and that of $\sigma_n 1$ never, so $\sigma_n \in A \subseteq C$ and $\sigma_{n+1} = \sigma_n 1$. If only $\sigma_n 0$ is, then $\sigma_n \in B$, so $\sigma_n \notin C$ and $\sigma_{n+1} = \sigma_n 0$. Hence the sequence $\bigcup_n \sigma_n$, computable in $C$ and so in $X$, is a member of $\mathcal P$.

(3 ⇒ 1) $\mathrm{DNC}_2$ is a non-empty $\Pi^0_1$ class (:ref{#thm-dnc2-no-computable}).
:::

The proof of (2 ⇒ 3) is uniform: from an index of $T$, one computes the indices of $A$ and $B$, and the member is obtained from the separating set by a fixed procedure. Combined with (1 ⇒ 2), it shows that a single member of $\mathrm{DNC}_2$ computes members of all non-empty $\Pi^0_1$ classes, uniformly in their indices. For this reason $\mathrm{DNC}_2$ is called a **universal** $\Pi^0_1$ class. Conditions 2 and 3 are not about a single class: by (3 ⇒ 1), a set computing a member of the one class $\mathrm{DNC}_2$ already has the power of condition 3.

:::quiz[the characterization of PA degrees]
In (1 ⇒ 2), why does the program $q(n)$ ignore its input?

- [x] So that its behavior on its own index $q(n)$, the only input $f$ is diagonalizing against, is determined by the membership of $n$ in $A$ or $B$.
- [ ] To make $q$ computable.

  $q$ is computable by SMN whatever the program does with its input.
- [ ] Because $A$ and $B$ have no input.

  The sets $A$ and $B$ are fixed; the parameter $n$ is built into the program.

---

In (2 ⇒ 3), what happens at a node $\sigma_n$ both of whose successors are extendible?

- [x] Neither non-extendibility is ever confirmed, so $\sigma_n$ is in neither $A$ nor $B$, and the separating set may choose either successor; both are correct.
- [ ] The construction fails, since $C$ is not defined at $\sigma_n$.

  $C$ is a set, defined everywhere; outside $A \cup B$ its values are arbitrary, and any value works.
- [ ] $\sigma_n$ belongs to both $A$ and $B$.

  $A$ and $B$ are disjoint by construction.
:::

## Consequences of the basis theorems

:::corollary{#cor-pa-basis}
1. There is a low PA set.
2. There is a computably dominated PA set.
3. For every non-computable set $C$, there is a PA set that does not compute $C$.
:::

:::proof{of=cor-pa-basis}
Apply :ref{#thm-low-basis}, :ref{#thm-dominated-basis} and :ref{#thm-cone-avoidance-basis} to the non-empty $\Pi^0_1$ class $\mathrm{DNC}_2$, all of whose members are PA.
:::

So the ability to compute a member of every non-empty $\Pi^0_1$ class does not require much computational power in other respects: a low PA set has the same jump as a computable set, and it computes a solution to every problem with a $\Pi^0_1$ set of solutions. On the other hand, a PA set is never computable, since it computes a member of $\mathrm{DNC}_2$. Among the c.e. sets, the situation is opposite: a c.e. set of PA degree is Turing complete (Jockusch and Soare, *Degrees of members of Π⁰₁ classes*, 1972; we admit this result, which also follows from Arslanov's completeness criterion, proved in the course on immunity and growth). In particular, no low PA set is c.e.

:::quiz[low PA sets]
A low PA set $X$ computes a member of every non-empty $\Pi^0_1$ class. Does it follow that every non-empty $\Pi^0_1$ class has a low member?

- [x] Yes: every member computed by $X$ is computable in a low set, hence low itself, since lowness is closed downward.

  This gives a second proof of the low basis theorem, once a low PA set is known to exist; but the existence of a low PA set was itself derived from the low basis theorem.
- [ ] No: the members computed by $X$ may have a larger jump than $X$.

  If $Y \leq_T X$, then $Y' \leq_T X'$.
- [ ] Only for classes without computable members.

  Classes with computable members have computable, hence low, members.
:::

## Completions of Peano arithmetic

The name PA comes from logic. Fix a computable coding of the sentences of arithmetic by integers. A set $S$ of sentences is **consistent** if no contradiction is provable from it, and **complete** if for every sentence $\varphi$, either $\varphi \in S$ or $\neg \varphi \in S$. We use two facts from logic, which we admit.

- *Proofs are checkable.* For a computable set of axioms, the relation "$p$ codes a proof of $\varphi$ from the axioms" is computable, so the set of theorems is c.e.
- *Peano arithmetic proves true computations.* If $\Phi_e(e)\converge = v$, then Peano arithmetic $\mathrm{PA}$ proves the sentence $\theta_{e,v}$ expressing "$\Phi_e(e)$ converges with value $v$", and proves $\neg \theta_{e,w}$ for every $w \neq v$. Here $\theta_{e,v}$ is the $\Sigma_1$ sentence obtained from :ref{#cor-sigma1-ce}, and the statement is the $\Sigma_1$-completeness of $\mathrm{PA}$, together with the uniqueness of the output, provable in $\mathrm{PA}$.

We also use that $\mathrm{PA}$ is consistent, since its axioms are true in $\nat$.

:::theorem{#thm-pa-completions}
A set $X$ is PA if and only if it computes a complete consistent set of sentences containing the axioms of $\mathrm{PA}$.
:::

:::proof{of=thm-pa-completions}
($\Rightarrow$) Identify a set of sentences with its characteristic function on codes, and let $\mathcal C$ be the class of sets $S$ such that: for every sentence $\varphi$, exactly one of $\varphi$ and $\neg \varphi$ belongs to $S$; every axiom of $\mathrm{PA}$ belongs to $S$; and no proof of a contradiction uses only premises from $S$. Its members are exactly the complete consistent sets of sentences containing $\mathrm{PA}$. A set fails to belong to $\mathcal C$ if and only if one of the following finite witnesses exists: a sentence $\varphi$ with both or neither of $\varphi, \neg \varphi$ in $S$; an axiom of $\mathrm{PA}$ not in $S$; or a proof of a contradiction whose premises are in $S$. Each witness involves finitely many bits of $S$, and, by the first fact, can be recognized by an algorithm. So the complement of $\mathcal C$ is a $\Sigma^0_1$ class, and $\mathcal C$ is a $\Pi^0_1$ class. It is non-empty, since the set of sentences true in $\nat$ belongs to it. By :ref{#thm-pa-characterization}, $X$ computes a member of $\mathcal C$.

($\Leftarrow$) Let $S \leq_T X$ be a complete consistent set containing $\mathrm{PA}$. Let $f(e) = 1$ if $\theta_{e,0} \in S$, and $f(e) = 0$ otherwise; $f$ is computable in $X$. If $\Phi_e(e)\converge = 0$, then $\mathrm{PA} \vdash \theta_{e,0}$; since $S$ is complete, contains $\mathrm{PA}$ and is consistent, $\theta_{e,0} \in S$ (otherwise $\neg \theta_{e,0} \in S$ and $S$ would be inconsistent), so $f(e) = 1 \neq 0$. If $\Phi_e(e)\converge = 1$, then $\mathrm{PA} \vdash \neg \theta_{e,0}$, so $\theta_{e,0} \notin S$ by consistency, and $f(e) = 0 \neq 1$. If $\Phi_e(e)$ converges to another value or diverges, there is nothing to check. So $f \in \mathrm{DNC}_2$.
:::

The theorem says that a set computes a completion of Peano arithmetic if and only if it is PA. A finer statement, due to Solovay and admitted here, is that the PA degrees are exactly the Turing degrees of completions of Peano arithmetic: every PA set has the same degree as some completion. The proof builds the completion by a finite extension construction relative to a given completion (Downey and Hirschfeldt, Theorem 2.21.3).

The second direction contains Gödel's first incompleteness theorem in Rosser's form: a complete consistent extension of $\mathrm{PA}$ is not computable, since it would compute a member of $\mathrm{DNC}_2$. The first direction shows that this is the only obstruction: any degree that computes a member of $\mathrm{DNC}_2$ computes a completion. Combined with :ref{#cor-pa-basis}, there are low completions of Peano arithmetic.

## Exercises

::::exercise{difficulty=1}
Show that $X$ is PA if and only if every partial computable function $\psi : \nat \rightharpoonup \{0, 1\}$ has a total $X$-computable extension.

:::solution
If $X$ is PA, let $A = \{ n : \psi(n)\converge = 0 \}$ and $B = \{ n : \psi(n)\converge = 1 \}$, disjoint c.e. sets, and let $D \leq_T X$ separate $B$ from $A$: $B \subseteq D$ and $D \cap A = \emptyset$. The characteristic function of $D$ is a total $X$-computable extension of $\psi$.

Conversely, let $\psi(e) \simeq 1 - \Phi_e(e)$ when $\Phi_e(e)\converge \in \{0, 1\}$, and $\psi(e)$ undefined otherwise; $\psi$ is partial computable with values in $\{0, 1\}$. Let $g$ be a total $X$-computable extension, and let $f(e) = g(e)$ if $g(e) \in \{0, 1\}$ and $f(e) = 0$ otherwise. If $\Phi_e(e)\converge \in \{0, 1\}$, then $f(e) = g(e) = 1 - \Phi_e(e) \neq \Phi_e(e)$. If $\Phi_e(e)\converge \geq 2$, then $f(e) \in \{0, 1\}$ differs from it. So $f \in \mathrm{DNC}_2$, and $X$ is PA.
:::
::::

::::exercise{difficulty=2 #ex-pa-relative}
A set $Y$ is **PA relative to $X$** if it computes a function $f : \nat \to \{0, 1\}$ with $f(e) \neq \Phi^X_e(e)$ whenever $\Phi^X_e(e)\converge$. Show that if $Y$ is PA relative to $X$, then $X \leq_T Y$.

:::solution
The proof of :ref{#thm-pa-characterization} relativizes: $Y$ computes a member of every non-empty $\Pi^0_1(X)$ class, that is, every class $[T]$ with $T$ an $X$-computable tree. The singleton $\{ X \}$ is such a class, with tree $\{ X \uh n : n \in \nat \}$. So $Y$ computes its only member, $X$.
:::
::::

## Notes and references

The degrees of completions of Peano arithmetic were studied by Scott (1962), who showed that a completion computes a member of every non-empty $\Pi^0_1$ class (the **Scott basis theorem**). Solovay showed, in unpublished work, that the degrees of completions are closed upward, and hence that they are exactly the degrees computing a member of every non-empty $\Pi^0_1$ class. Jockusch and Soare characterized these degrees by separating sets of effectively inseparable pairs, proved the existence of low PA degrees (in *Π⁰₁ classes and degrees of theories*), and showed that c.e. PA degrees are complete (in *Degrees of members of Π⁰₁ classes*). The characterization by $\{0, 1\}$-valued diagonally non-computable functions is credited to Jockusch and Soare and to Solovay by Downey and Hirschfeldt (Theorem 2.22.2). The incompleteness theorem in the form used here is due to Rosser (1936).

Soare's *Turing Computability* treats PA degrees in Chapter 10, Downey and Hirschfeldt in Sections 2.21–2.22, and Hirschfeldt's *Slicing the Truth* in Section 3.1 (Theorems 3.16–3.21).

- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in *Recursive Function Theory*, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- C. G. Jockusch and R. I. Soare, *Degrees of members of Π⁰₁ classes*, Pacific Journal of Mathematics 40 (1972), 605–616.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- J. B. Rosser, *Extensions of some theorems of Gödel and Church*, Journal of Symbolic Logic 1 (1936), 87–91.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Chapter 10.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 2.21–2.22.
- D. R. Hirschfeldt, *Slicing the Truth*, Lecture Notes Series of the Institute for Mathematical Sciences, National University of Singapore, 28, World Scientific, 2015, Section 3.1.
