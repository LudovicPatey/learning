---
title: Weak König's lemma and two cones
summary: First-jump constructions give a path of a Π⁰₁ class avoiding a cone, or one whose jump avoids a cone, but not both; the forcing questions of Jockusch–Soare forcing at levels 1 and 2 give both at once (Wang).
duration: 35
prerequisites: [sigma2-questions, pi01-classes/basis-theorems]
---

Jump cone avoidance for $\mathsf{WKL}$ comes for free from first-jump control (:ref{#ex-jca-problems}). This lesson asks for more: a path $G$ of a $\Pi^0_1$ class with $C \not\leq_T G$ and $D \not\leq_T G'$ at the same time, for a non-computable set $C$ and a set $D \not\leq_T \emptyset'$. The first section explains why the basis theorems of the first level do not give it. The second proves it with one generic set for Jockusch–Soare forcing, using the forcing questions of the two levels together: this is the theorem of Wang, the first application of :ref{#thm-local-jump-cone}. The next lesson proves the same statement for cohesiveness, where the notion of forcing has to be redesigned.

## The limits of first-jump control

The basis theorems of the first level give paths with one of the two properties.

- The **low basis theorem** gives a path $G$ with $G' \leq_T \emptyset'$, hence $D \not\leq_T G'$. It gives no control over the $\Delta^0_2$ sets that $G$ computes, and a given non-computable $C \leq_T \emptyset'$ may be one of them.
- The **cone avoidance basis theorem** (:ref{#thm-cone-avoidance-basis}) gives a path with $C \not\leq_T G$, and no control over its jump.
- A **weakly low basis** gives a path with $G' \leq_T P$, where $P$ is PA relative to $\emptyset'$ and $D \not\leq_T P$. Since $P$ computes $\emptyset'$, this says nothing about the non-computable sets $C \leq_T \emptyset'$.

In each case, the construction controls one jump and leaves the other free. If $C \not\leq_T \emptyset'$, a low path satisfies both properties, since every set it computes is computable in $\emptyset'$; the difficulty is the case of a $\Delta^0_2$ set $C$. Both hypotheses of the theorem below are necessary: if $C$ is computable, every set computes it, and if $D \leq_T \emptyset'$, then $D \leq_T G'$ for every $G$.

## Wang's theorem

By :ref{#thm-tree-question}, Jockusch–Soare forcing has forcing questions that are $\Sigma^0_1$-preserving and $\Sigma^0_2$-preserving. One generic set satisfies the conclusions of the abstract theorems at levels $1$ and $2$ at once.

:::theorem[Wang]{#thm-wkl-two-cones}
Let $C$ be a non-computable set and $D$ a set with $D \not\leq_T \emptyset'$. Every non-empty $\Pi^0_1$ class $\mathcal P$ has a member $G$ with $C \not\leq_T G$ and $D \not\leq_T G'$.
:::

:::proof{of=thm-wkl-two-cones}
Use Jockusch–Soare forcing below the condition $\mathcal P$. By :ref{#thm-local-cone-avoidance} with $\mathcal M = \{ \emptyset \}$, every sufficiently generic $G$ satisfies $C \not\leq_T G$. By :ref{#thm-local-jump-cone} with $\mathcal M = \{ \emptyset' \}$, every sufficiently generic $G$ satisfies $D \not\leq_T G'$. The union of the two countable families of dense sets is countable, so a filter through $\mathcal P$ generic for both exists (:ref{#lem-rasiowa-sikorski}), and its generic set is a member of $\mathcal P$.
:::

The same generic set avoids countably many cones $C_0, C_1, \dots$ at level $1$ and countably many cones $D_0, D_1, \dots$ at level $2$, since each cone contributes countably many dense sets. For a single cone at each level, the monograph attributes to Lawton a combination of the low basis theorem and the cone avoidance basis theorem: if $C$ is $\Delta^0_2$ and not computable, every non-empty $\Pi^0_1$ class has a low member not computing $C$. With the remark of the previous section, this gives the theorem for one pair $C$, $D$; the monograph notes that Lawton's proof, unlike the forcing proof, does not extend to countably many cones.

:::quiz[Wang's theorem]
Why does the proof of :ref{#thm-wkl-two-cones} use the forcing questions of Jockusch–Soare forcing at two levels, rather than a single level?

- [x] Because avoiding the cone above $C$ is controlled by the question for $\Sigma^0_1$ sentences, relative to $\emptyset$, and avoiding the cone above $D$ in the jump by the question for $\Sigma^0_2$ sentences, relative to $\emptyset'$; one generic set meets the dense sets of both.
- [ ] Because the question for $\Sigma^0_2$ sentences does not satisfy property 2.

  It satisfies both properties, by :ref{#thm-tree-question}.
- [ ] Because $C$ may be computable in $\emptyset'$.

  This is why the low basis theorem is not enough; the forcing argument does not need to distinguish the cases.

---

In the proof, why is the question for $\Sigma^0_2$ sentences taken to be $\Sigma^0_1(\{ \emptyset' \})$-preserving, rather than $\Sigma^0_1(\{ \emptyset \})$-preserving?

- [x] Because the question of :ref{#thm-tree-question} for $\Sigma^0_2$ sentences is $\Sigma^0_2$, that is, $\Sigma^0_1$ relative to $\emptyset'$, and not $\Sigma^0_1$ in general; the third case of :ref{#thm-local-jump-cone} for $\mathcal M = \{ \emptyset' \}$ then needs $D \not\leq_T \emptyset'$, which is the hypothesis.
- [ ] Because $\emptyset'$ is a member of $\mathcal P$.

  It need not be; $\mathcal M$ concerns the definability of the question, not the members of the class.
- [ ] Because the question for $\Sigma^0_1$ sentences is $\Sigma^0_1$ relative to $\emptyset'$.

  It is $\Sigma^0_1$, which is used for the cone above $C$.
:::

## Exercises

::::exercise{difficulty=2}
Call a tree $T \subseteq 2^{<\nat}$ **primitive recursive** if its characteristic function is.

1. Let $T$ be a co-c.e. tree, $T = \{ \sigma : \Phi_e(\sigma)\diverge \}$. Show that $S = \{ \sigma : \Phi_e(\tau)[|\sigma|]\diverge \text{ for every } \tau \preceq \sigma \}$ is a primitive recursive tree with $T \subseteq S$ and $[S] = [T]$.
2. Consider Jockusch–Soare forcing with conditions the infinite primitive recursive trees, given by indices in a computable list of all primitive recursive functions, ordered by inclusion, the members of $T$ being its paths. Show that being a condition and extension are $\Pi^0_1$, that the question "$T \mathrel{?{\vdash}} \Phi^G_e\converge$ if there is $\ell$ such that $\Phi^\sigma_e[\ell]\converge$ for every $\sigma \in T$ of length $\ell$" is a $\Sigma^0_1$-preserving forcing question, and that the lifted question is $\Sigma^0_2$-preserving.

:::solution
1. The predicate $\Phi_e(\tau)[s]\diverge$ is primitive recursive, and primitive recursive predicates are closed under bounded quantification, so $S$ is primitive recursive. It is closed under prefixes: if $\sigma \in S$, $\rho \preceq \sigma$ and $\tau \preceq \rho$, then $\Phi_e(\tau)[|\sigma|]\diverge$, hence $\Phi_e(\tau)[|\rho|]\diverge$, since a computation that converges by stage $|\rho|$ converges by the later stage $|\sigma|$. If $\sigma \in T$, every prefix $\tau$ of $\sigma$ is in $T$, so $\Phi_e(\tau)\diverge$, and in particular $\Phi_e(\tau)[|\sigma|]\diverge$: $\sigma \in S$. So $T \subseteq S$ and $[T] \subseteq [S]$. Conversely, let $X \in [S]$ and $\tau \prec X$. If $\Phi_e(\tau)[t]\converge$, let $n = \max(t, |\tau|)$; then $\tau$ is a prefix of $X \uh n$ with $\Phi_e(\tau)[n]\converge$, so $X \uh n \notin S$, a contradiction. So $\Phi_e(\tau)\diverge$ for every $\tau \prec X$, and $X \in [T]$.
2. A primitive recursive function is total, so an index always defines a tree once "closed under prefixes and $\{0,1\}$-valued" is checked, a $\Pi^0_1$ property; infinity is $\Pi^0_1$ (a node at every length); $S \subseteq T$ is $\Pi^0_1$. If some length $\ell$ makes the computation converge in $\ell$ steps on all nodes of that length, every path extends a node of length $\ell$ and satisfies the sentence, so $T$ forces it. Otherwise, for every $\ell$ some node $\sigma \in T$ of length $\ell$ has $\Phi^\sigma_e[\ell]\diverge$. The set $S$ of nodes $\sigma \in T$ with $\Phi^\sigma_e[|\sigma|]\diverge$ is primitive recursive, closed under prefixes by monotonicity of computations, and has a node at every length; so it is a condition. Every path $X$ of $S$ satisfies $\Phi^X_e\diverge$: if the computation converged with use $u$ at stage $s$, the prefix of $X$ of length $\max(u, s)$ would not be in $S$. The question is $\Sigma^0_1$. In the lifted question, "$d$ is a condition", "$d \subseteq c$" and "$d \mathrel{?{\nvdash}} \neg\psi(m)$" are $\Pi^0_1$, so the question is $\Sigma^0_2$. By part 1, every non-empty $\Pi^0_1$ class is the set of paths of an infinite primitive recursive tree, so this gives a second proof of :ref{#thm-wkl-two-cones}.
:::
::::

::::exercise{difficulty=2}
1. Let $\mathsf P$ admit jump cone avoidance. Show that there is a Turing ideal satisfying $\mathsf P$ none of whose members is high. Deduce that $\mathsf{DOM}$ (:ref{#ex-jca-problems}) is not ω-reducible to $\mathsf P$, and that the ideal does not contain $\emptyset'$.
2. Let $C$ be non-computable. Show that there is a Scott ideal none of whose members is high or computes $C$.

:::solution
1. Let $\mathcal W$ be the class of sets $Y$ with $\emptyset'' \not\leq_T Y'$. It is closed downward under Turing reducibility, since $W \leq_T Y$ implies $W' \leq_T Y'$, and it contains $\emptyset$. Let $Z \in \mathcal W$ and $X \leq_T Z$ an instance. The set $C = \emptyset''$ satisfies $C \not\leq_T Z'$, so jump cone avoidance gives a solution $Y$ with $\emptyset'' \not\leq_T (Z \oplus Y)'$, that is, $Z \oplus Y \in \mathcal W$. So $\mathsf P$ preserves $\mathcal W$ (:ref{#def-weakness}), and :ref{#lem-preservation-ideal} gives a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf P$. The instance $\emptyset \in \mathcal I$ of $\mathsf{DOM}$ has no solution in $\mathcal I$, since a dominant function is high by Martin's theorem; so $\mathcal I$ satisfies $\mathsf P$ but not $\mathsf{DOM}$, and $\mathsf{DOM} \not\leq_\omega \mathsf P$. Finally $\emptyset'$ is high, so $\emptyset' \notin \mathcal I$.
2. Let $\mathcal W$ be the class of sets $Y$ with $C \not\leq_T Y$ and $\emptyset'' \not\leq_T Y'$, closed downward. Let $Z \in \mathcal W$ and $T$ a $Z$-computable infinite binary tree. :ref{#thm-wkl-two-cones} relativized to $Z$, with $D = \emptyset''$, which satisfies $D \not\leq_T Z'$, gives a path $G$ with $C \not\leq_T Z \oplus G$ and $\emptyset'' \not\leq_T (Z \oplus G)'$. So $\mathsf{WKL}$ preserves $\mathcal W$, and :ref{#lem-preservation-ideal} gives a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf{WKL}$, that is, a Scott ideal (:ref{#prop-wkl-scott}).
:::
::::

## Notes and references

:ref{#thm-wkl-two-cones} is due to Wang (2016), in a paper on the preservation of definitions. The monograph, in the section *Weak König's lemma* of the chapter *Jump cone avoidance*, proves it with primitive recursive trees, the route of the first exercise; the proof given here combines two theorems of :ref{to="effective-forcing/forcing-question"}. The statement on Lawton's theorem is quoted from the monograph, which refers to Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008); it has not been checked in that paper. The monograph also states, as an exercise attributed to Le Houérou, Levy Patey and Mimouni (2024), the corresponding statement for hyperimmunity: a $\Pi^0_1$ class has a member preserving at once a hyperimmune function and a function hyperimmune relative to $\emptyset'$.

- W. Wang, *The definability strength of combinatorial principles*, Journal of Symbolic Logic 81 (2016), 1531–1554.
- D. R. Hirschfeldt, C. G. Jockusch, Jr., B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Weak König's lemma*.
