---
title: Computable reducibility
summary: Reductions that use a single instance of the stronger problem; computable and strong computable reducibility; König's lemma is ω-reducible but not computably reducible to the jump; Scott's theorem that every PA degree bounds a Scott ideal, and the coincidence of ω-reducibility and computable reducibility to WKL; cylinders.
duration: 35
prerequisites: [omega-reducibility]
---

An ω-reduction may use any number of instances of $\mathsf Q$, each built from the solutions of the previous ones. Dzhafarov proposed to count: a **computable reduction** solves an instance of $\mathsf P$ with a single instance of $\mathsf Q$. This finer notion separates problems that are equivalent in ω-models, and it is the analogue for problems of the reductions of complexity theory.

## Computable and strong computable reducibility

:::definition{#def-computable-reducible}
Let $\mathsf P$ and $\mathsf Q$ be problems.

1. $\mathsf P$ is **computably reducible** to $\mathsf Q$, written $\mathsf P \leq_c \mathsf Q$, if every instance $X$ of $\mathsf P$ computes an instance $\widetilde X$ of $\mathsf Q$ such that, for every solution $\widetilde Y$ to $\widetilde X$, the set $X \oplus \widetilde Y$ computes a solution to $X$.
2. $\mathsf P$ is **strongly computably reducible** to $\mathsf Q$, written $\mathsf P \leq_{sc} \mathsf Q$, if moreover $\widetilde Y$ alone computes a solution to $X$.
3. $\mathsf P$ is **computably true** if every instance computes a solution to itself.
:::

Strong reducibility forbids the use of the original instance in the second step: all the information needed must be coded in the solutions of $\mathsf Q$. Both relations are preorders, and $\mathsf P \leq_{sc} \mathsf Q$ implies $\mathsf P \leq_c \mathsf Q$.

:::proposition{#prop-c-omega}
If $\mathsf P \leq_c \mathsf Q$, then $\mathsf P \leq_\omega \mathsf Q$. A problem $\mathsf P$ is computably true if and only if $\mathsf P \leq_c \mathsf{Id}$, if and only if every Turing ideal satisfies it.
:::

:::proof{of=prop-c-omega}
Let $\mathcal I \models \mathsf Q$ and $X \in \mathcal I$ an instance of $\mathsf P$. The instance $\widetilde X \leq_T X$ belongs to $\mathcal I$, so it has a solution $\widetilde Y \in \mathcal I$; then $X \oplus \widetilde Y \in \mathcal I$ computes a solution to $X$, which belongs to $\mathcal I$.

If $\mathsf P$ is computably true, take $\widetilde X = X$ as an instance of $\mathsf{Id}$. Conversely, if $\mathsf P \leq_c \mathsf{Id}$, the only solution to $\widetilde X$ is $\widetilde X \leq_T X$, so $X$ computes a solution. If every Turing ideal satisfies $\mathsf P$, so does $\{ Y : Y \leq_T X \}$, so $X$ computes a solution. Conversely, if $\mathsf P$ is computably true, every instance in a Turing ideal computes a solution, which belongs to the ideal.
:::

For instance, $\mathsf{RT}^1_2$ is computably true: one of the two color classes is infinite, and it is computable from the coloring. The game of the previous lesson refines into a hierarchy: write $\mathsf P \leq^n_\omega \mathsf Q$ if Player 2 has a strategy in $G(\mathsf Q \rightarrow \mathsf P)$ that wins within $n + 1$ rounds, that is, after at most $n$ instances of $\mathsf Q$. Then $\mathsf P \leq^0_\omega \mathsf Q$ means that $\mathsf P$ is computably true, and $\mathsf P \leq_c \mathsf Q$ implies $\mathsf P \leq^1_\omega \mathsf Q$, with equivalence when $\mathsf Q$ has a computable instance.

:::proposition{#prop-kl-not-c-j}
$\mathsf{KL} \leq^2_\omega \mathsf J$, but $\mathsf{KL} \not\leq_c \mathsf J$.
:::

:::proof{of=prop-kl-not-c-j}
Player 2 plays $T$, then $T'$, and receives $T''$, which computes a path through $T$, as in :ref{#prop-kl-j}.

No set is PA relative to itself, since it would compute a function that differs from every function it computes; so by :ref{#thm-konig-strength} there is an infinite computable finitely branching tree $T$ without $\emptyset'$-computable path. Every instance $\widetilde X \leq_T T$ of $\mathsf J$ is computable, so its solution $\widetilde X'$ is computable in $\emptyset'$, and $T \oplus \widetilde X' \leq_T \emptyset'$ computes no path through $T$.
:::

So computable reducibility is strictly finer than ω-reducibility. It is also incomparable with provability over $\mathsf{RCA}_0$: a proof may use the hypothesis several times, and a computable reduction may rely on properties of the standard natural numbers, such as instances of induction, that $\mathsf{RCA}_0$ does not prove. In practice, many implications over $\mathsf{RCA}_0$ are proved by computable reductions that formalize in $\mathsf{RCA}_0$.

:::quiz[computable reducibility]
In the proof of :ref{#prop-kl-not-c-j}, why does a single instance of $\mathsf J$ not suffice?

- [x] Because the instance must be computable from the computable tree $T$, so it is computable, and its jump is computable in $\emptyset'$, which computes no path through $T$.
- [ ] Because $\mathsf J$ has a unique solution.

  Uniqueness is not the issue: the unique solution $\widetilde X'$ is computable in $\emptyset'$, which is not enough.
- [ ] Because $T$ has no computable path.

  Many trees without computable paths have paths computable in $\emptyset'$; $T$ was chosen to have none.
:::

## Computable reductions to weak König's lemma

For $\mathsf{WKL}$, the two reducibilities coincide, because a single instance of $\mathsf{WKL}$ can produce a whole Scott ideal.

:::theorem[Scott]{#thm-scott-pa}
Let $A$ be a set and $P$ a set that computes $A$ and is PA relative to $A$. There is a Scott ideal containing $A$ all of whose members are computable in $P$.
:::

:::proof{of=thm-scott-pa}
For a set $Z$, let $D^Z$ be the class of $\{0, 1\}$-valued functions $g$ with $g(e) \neq \Phi^Z_e(e)$ whenever $\Phi^Z_e(e)$ converges; it is a non-empty $\Pi^0_1(Z)$ class, uniformly in $Z$. Let $\mathcal C$ be the class of sequences $(X_i)_{i \in \nat}$, coded as $\bigoplus_i X_i$, such that $X_0 = A$ and, for every $i$, $X_{i+1} \in D^{Z_i}$, where $Z_i = X_0 \oplus \cdots \oplus X_i$. It is a $\Pi^0_1(A)$ class, non-empty since each $D^{Z_i}$ is non-empty. Since $P$ computes $A$ and is PA relative to $A$, it computes a member $(X_i)$ of $\mathcal C$, by :ref{#thm-pa-characterization} relativized to $A$; and every $Z_i$ is computable in $P$.

Let $\mathcal I = \{ Y : \exists i\ Y \leq_T Z_i \}$, a Turing ideal containing $A$, with all members computable in $P$. The set $Z_{i+1} = Z_i \oplus X_{i+1}$ computes $Z_i$ and a $\{0, 1\}$-valued function that is diagonally non-computable relative to $Z_i$, so it is PA relative to $Z_i$, by :ref{#thm-pa-characterization} relativized to $Z_i$; hence it is PA relative to every $Y \leq_T Z_i$, since every non-empty $\Pi^0_1(Y)$ class is a $\Pi^0_1(Z_i)$ class. So every member $Y \leq_T Z_i$ of $\mathcal I$ has a member $Z_{i+1}$ of $\mathcal I$ that is PA relative to it, and $\mathcal I$ is a Scott ideal by :ref{#prop-wkl-scott}.
:::

The sets $Z_i$ are used rather than the $X_i$: a function that is diagonally non-computable relative to $Z$ need not compute $Z$, and the join ensures that the sequence increases.

:::theorem[Hirschfeldt, Jockusch]{#thm-wkl-omega-c}
For every problem $\mathsf P$, $\mathsf P \leq_\omega \mathsf{WKL}$ if and only if $\mathsf P \leq_c \mathsf{WKL}$.
:::

:::proof{of=thm-wkl-omega-c}
One direction is :ref{#prop-c-omega}. Suppose $\mathsf P \leq_\omega \mathsf{WKL}$, and let $X$ be an instance of $\mathsf P$. Let $\widetilde X$ be an $X$-computable infinite binary tree whose paths are the members of $D^X$, the $\{0, 1\}$-valued functions diagonally non-computable relative to $X$. For every path $\widetilde Y$, the set $X \oplus \widetilde Y$ computes $X$ and is PA relative to $X$. By :ref{#thm-scott-pa}, there is a Scott ideal $\mathcal I$ containing $X$, all of whose members are computable in $X \oplus \widetilde Y$. It satisfies $\mathsf{WKL}$, hence $\mathsf P$, so $X$ has a solution in $\mathcal I$, which is computable in $X \oplus \widetilde Y$.
:::

:::quiz[Scott ideals]
Why does the proof of :ref{#thm-scott-pa} use the joins $Z_i$, rather than requiring $X_{i+1}$ to be diagonally non-computable relative to $X_i$?

- [x] Because a function diagonally non-computable relative to $X_i$ need not compute $X_i$, so the classes of sets computable in the $X_i$ need not increase, and their union need not be a Turing ideal.
- [ ] Because $D^{X_i}$ may be empty.

  Each such class is non-empty.
- [ ] Because $\mathcal C$ would not be a $\Pi^0_1$ class.

  It would still be $\Pi^0_1(A)$; the problem is the structure of the resulting ideal.

---

In the proof of :ref{#thm-wkl-omega-c}, why is a single instance of $\mathsf{WKL}$ enough?

- [x] Because one path through a tree of diagonally non-computable functions is PA relative to the instance, and a PA set computes a whole Scott ideal, inside which the ω-reduction can be carried out.
- [ ] Because $\mathsf{WKL}$ is computably true.

  It is not: some computable trees have no computable path.
- [ ] Because $\mathsf P$ uses only one instance of $\mathsf{WKL}$.

  The ω-reduction may use many instances; they are all solved inside the Scott ideal.
:::

## Cylinders

The **product** $\mathsf P \times \mathsf Q$ of two problems has as instances the sets $X_0 \oplus X_1$ with $X_0$ an instance of $\mathsf P$ and $X_1$ an instance of $\mathsf Q$, and as solutions the sets $Y_0 \oplus Y_1$ with $Y_i$ a solution to $X_i$.

:::definition{#def-cylinder}
A problem $\mathsf Q$ is a **cylinder** if $\mathsf{Id} \times \mathsf Q \leq_{sc} \mathsf Q$.
:::

A cylinder can code any given set into its solutions. For cylinders, the strong and the ordinary reducibilities agree.

:::proposition{#prop-cylinder}
A problem $\mathsf Q$ is a cylinder if and only if, for every problem $\mathsf P$, $\mathsf P \leq_c \mathsf Q$ implies $\mathsf P \leq_{sc} \mathsf Q$.
:::

:::proof{of=prop-cylinder}
Suppose $\mathsf Q$ is a cylinder and $\mathsf P \leq_c \mathsf Q$. Let $X$ be an instance of $\mathsf P$, and $\widetilde X \leq_T X$ the instance of $\mathsf Q$ given by the reduction. Then $X \oplus \widetilde X$ is an instance of $\mathsf{Id} \times \mathsf Q$, so there is an instance $V \leq_T X \oplus \widetilde X \leq_T X$ of $\mathsf Q$ such that every solution $W$ to $V$ computes $X \oplus \widetilde Y$ for some solution $\widetilde Y$ to $\widetilde X$. Then $W$ computes a solution to $X$. So $\mathsf P \leq_{sc} \mathsf Q$. Conversely, $\mathsf{Id} \times \mathsf Q \leq_c \mathsf Q$ always holds, with $\widetilde X = X_1$; if computable reductions to $\mathsf Q$ are strong, $\mathsf Q$ is a cylinder.
:::

:::proposition{#prop-wkl-cylinder}
$\mathsf{WKL}$ and $\mathsf J$ are cylinders. Consequently, $\mathsf P \leq_\omega \mathsf{WKL}$ implies $\mathsf P \leq_{sc} \mathsf{WKL}$.
:::

:::proof{of=prop-wkl-cylinder}
Given a set $X$ and a binary tree $T$, let $S$ be the tree of strings $\sigma$ such that $\sigma(2i + 1) = X(i)$ for all $2i + 1 < |\sigma|$, and the string $\tau$ of the even bits of $\sigma$ belongs to $T$. It is computable in $X \oplus T$, infinite if $T$ is, and its paths are exactly the sets $P \oplus X$ with $P$ a path through $T$; each of them computes $X \oplus P$. For $\mathsf J$, the jump of $X \oplus T$ computes $X \oplus T'$. The consequence follows from :ref{#thm-wkl-omega-c} and :ref{#prop-cylinder}.
:::

Strong reducibility is strictly stronger than computable reducibility in general. For instance, $\mathsf{Id} \leq_c \mathsf{RT}^1_2$, since the solution may use the instance. But $\mathsf{Id} \not\leq_{sc} \mathsf{RT}^1_2$: for a non-computable $X$, every $X$-computable coloring has an infinite homogeneous set that does not compute $X$, by the theorem of Dzhafarov and Jockusch (:ref{#thm-dj-cone-avoidance}). So $\mathsf{RT}^1_2$ is not a cylinder.

## Exercises

::::exercise{difficulty=1}
Show that $\leq_c$ is transitive.

:::solution
Let $\mathsf P \leq_c \mathsf Q \leq_c \mathsf R$, and $X$ an instance of $\mathsf P$. Let $\widetilde X \leq_T X$ be the instance of $\mathsf Q$, and $\widehat X \leq_T \widetilde X$ the instance of $\mathsf R$ given by the second reduction for $\widetilde X$. Then $\widehat X \leq_T X$. For every solution $\widehat Y$ to $\widehat X$, $\widetilde X \oplus \widehat Y$ computes a solution $\widetilde Y$ to $\widetilde X$, and $X \oplus \widetilde Y$ computes a solution to $X$. Since $\widetilde X \leq_T X$, the set $X \oplus \widehat Y$ computes $X \oplus \widetilde Y$, hence a solution to $X$.
:::
::::

::::exercise{difficulty=2}
Show that $\mathsf{RT}^2_2 \not\leq_c \mathsf{WKL}$, and that $\mathsf{WKL} \not\leq_c \mathsf{RT}^1_2$.

:::solution
By :ref{#thm-wkl-omega-c}, $\mathsf{RT}^2_2 \leq_c \mathsf{WKL}$ would give $\mathsf{RT}^2_2 \leq_\omega \mathsf{WKL}$, which fails by :ref{#ex-wkl-kl-rt22}. For the second statement, $\mathsf{RT}^1_2$ is computably true, so $\mathsf{WKL} \leq_c \mathsf{RT}^1_2$ would make $\mathsf{WKL}$ computably true, by transitivity and :ref{#prop-c-omega}. But there is an infinite computable binary tree without computable path (:ref{#thm-dnc2-no-computable}).
:::
::::

## Notes and references

Computable reducibility was introduced by Dzhafarov (2015) in his study of cohesiveness, and strong computable reducibility at the same time. Scott (1962) proved that every PA degree bounds a Scott ideal, in the language of completions of Peano arithmetic; Hirschfeldt and Jockusch derived the coincidence of the reducibilities to $\mathsf{WKL}$.

- D. D. Dzhafarov, *Cohesive avoidance and strong reductions*, Proceedings of the American Mathematical Society 143 (2015), 869–876.
- D. Scott, *Algebras of sets binumerable in complete extensions of arithmetic*, in Recursive Function Theory, Proceedings of Symposia in Pure Mathematics 5, American Mathematical Society, 1962, 117–121.
- D. R. Hirschfeldt and C. G. Jockusch, *On notions of computability-theoretic reduction between Π¹₂ principles*, Journal of Mathematical Logic 16 (2016), 1650002.
