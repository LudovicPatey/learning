---
title: Weak König's lemma and two cones
summary: First-jump constructions give a path of a Π⁰₁ class avoiding a cone, or one whose jump avoids a cone, but not both; the forcing questions of Jockusch–Soare forcing at levels 1 and 2 give both at once (Wang).
duration: 20
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

::::exercise[Primitive recursive trees]{#ex-wkl-primitive-trees difficulty=2 objective="Restrict Jockusch–Soare forcing to primitive recursive trees so that extension becomes $\Pi^0_1$ and the lifted question $\Sigma^0_2$."}
Call a tree $T \subseteq 2^{<\nat}$ **primitive recursive** if its characteristic function is.

1. Let $T$ be a co-c.e. tree, $T = \{ \sigma : \Phi_e(\sigma)\diverge \}$. Show that $S = \{ \sigma : \Phi_e(\tau)[|\sigma|]\diverge \text{ for every } \tau \preceq \sigma \}$ is a primitive recursive tree with $T \subseteq S$ and $[S] = [T]$.
2. Consider Jockusch–Soare forcing with conditions the infinite primitive recursive trees, given by indices in a computable list of all primitive recursive functions, ordered by inclusion, the members of $T$ being its paths. Show that being a condition and extension are $\Pi^0_1$, that the question "$T \mathrel{?{\vdash}} \Phi^G_e\converge$ if there is $\ell$ such that $\Phi^\sigma_e[\ell]\converge$ for every $\sigma \in T$ of length $\ell$" is a $\Sigma^0_1$-preserving forcing question, and that the lifted question is $\Sigma^0_2$-preserving.

:::solution
1. The predicate $\Phi_e(\tau)[s]\diverge$ is primitive recursive, and primitive recursive predicates are closed under bounded quantification, so $S$ is primitive recursive. It is closed under prefixes: if $\sigma \in S$, $\rho \preceq \sigma$ and $\tau \preceq \rho$, then $\Phi_e(\tau)[|\sigma|]\diverge$, hence $\Phi_e(\tau)[|\rho|]\diverge$, since a computation that converges by stage $|\rho|$ converges by the later stage $|\sigma|$. If $\sigma \in T$, every prefix $\tau$ of $\sigma$ is in $T$, so $\Phi_e(\tau)\diverge$, and in particular $\Phi_e(\tau)[|\sigma|]\diverge$: $\sigma \in S$. So $T \subseteq S$ and $[T] \subseteq [S]$. Conversely, let $X \in [S]$ and $\tau \prec X$. If $\Phi_e(\tau)[t]\converge$, let $n = \max(t, |\tau|)$; then $\tau$ is a prefix of $X \uh n$ with $\Phi_e(\tau)[n]\converge$, so $X \uh n \notin S$, a contradiction. So $\Phi_e(\tau)\diverge$ for every $\tau \prec X$, and $X \in [T]$.
2. A primitive recursive function is total, so an index always defines a tree once "closed under prefixes and $\{0,1\}$-valued" is checked, a $\Pi^0_1$ property; infinity is $\Pi^0_1$ (a node at every length); $S \subseteq T$ is $\Pi^0_1$. If some length $\ell$ makes the computation converge in $\ell$ steps on all nodes of that length, every path extends a node of length $\ell$ and satisfies the sentence, so $T$ forces it. Otherwise, for every $\ell$ some node $\sigma \in T$ of length $\ell$ has $\Phi^\sigma_e[\ell]\diverge$. The set $S$ of nodes $\sigma \in T$ with $\Phi^\sigma_e[|\sigma|]\diverge$ is primitive recursive, closed under prefixes by monotonicity of computations, and has a node at every length; so it is a condition. Every path $X$ of $S$ satisfies $\Phi^X_e\diverge$: if the computation converged with use $u$ at stage $s$, the prefix of $X$ of length $\max(u, s)$ would not be in $S$. The question is $\Sigma^0_1$. In the lifted question, "$d$ is a condition", "$d \subseteq c$" and "$d \mathrel{?{\nvdash}} \neg\psi(m)$" are $\Pi^0_1$, so the question is $\Sigma^0_2$. By part 1, every non-empty $\Pi^0_1$ class is the set of paths of an infinite primitive recursive tree, so this gives a second proof of :ref{#thm-wkl-two-cones}.
:::
::::

::::exercise[ω-models without high members]{#ex-wkl-no-high-ideal difficulty=2 objective="Build Turing ideals and Scott ideals without high members by preserving a weakness property, and separate $\mathsf{DOM}$ from problems with jump cone avoidance."}
1. Let $\mathsf P$ admit jump cone avoidance. Show that there is a Turing ideal satisfying $\mathsf P$ none of whose members is high. Deduce that $\mathsf{DOM}$ (:ref{#ex-jca-problems}) is not ω-reducible to $\mathsf P$, and that the ideal does not contain $\emptyset'$.
2. Let $C$ be non-computable. Show that there is a Scott ideal none of whose members is high or computes $C$.

:::solution
1. Let $\mathcal W$ be the class of sets $Y$ with $\emptyset'' \not\leq_T Y'$. It is closed downward under Turing reducibility, since $W \leq_T Y$ implies $W' \leq_T Y'$, and it contains $\emptyset$. Let $Z \in \mathcal W$ and $X \leq_T Z$ an instance. The set $C = \emptyset''$ satisfies $C \not\leq_T Z'$, so jump cone avoidance gives a solution $Y$ with $\emptyset'' \not\leq_T (Z \oplus Y)'$, that is, $Z \oplus Y \in \mathcal W$. So $\mathsf P$ preserves $\mathcal W$ (:ref{#def-weakness}), and :ref{#lem-preservation-ideal} gives a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf P$. The instance $\emptyset \in \mathcal I$ of $\mathsf{DOM}$ has no solution in $\mathcal I$, since a dominant function is high by Martin's theorem; so $\mathcal I$ satisfies $\mathsf P$ but not $\mathsf{DOM}$, and $\mathsf{DOM} \not\leq_\omega \mathsf P$. Finally $\emptyset'$ is high, so $\emptyset' \notin \mathcal I$.
2. Let $\mathcal W$ be the class of sets $Y$ with $C \not\leq_T Y$ and $\emptyset'' \not\leq_T Y'$, closed downward. Let $Z \in \mathcal W$ and $T$ a $Z$-computable infinite binary tree. :ref{#thm-wkl-two-cones} relativized to $Z$, with $D = \emptyset''$, which satisfies $D \not\leq_T Z'$, gives a path $G$ with $C \not\leq_T Z \oplus G$ and $\emptyset'' \not\leq_T (Z \oplus G)'$. So $\mathsf{WKL}$ preserves $\mathcal W$, and :ref{#lem-preservation-ideal} gives a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf{WKL}$, that is, a Scott ideal (:ref{#prop-wkl-scott}).
:::
::::

## Notes and references

:ref{#thm-wkl-two-cones} is due to Wang (2016), in a paper on the preservation of definitions. The monograph, in the section *Weak König's lemma* of the chapter *Jump cone avoidance*, proves it with primitive recursive trees, the route of :ref{#ex-wkl-primitive-trees}; the proof given here combines two theorems of :ref{to="effective-forcing/forcing-question"}. The statement on Lawton's theorem is quoted from the monograph, which refers to Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008); it has not been checked in that paper. The monograph also states, as an exercise attributed to Le Houérou, Levy Patey and Mimouni (2024), the corresponding statement for hyperimmunity (:ref{#ex-wkl-two-hyperimmunities}).

- W. Wang, *The definability strength of combinatorial principles*, Journal of Symbolic Logic 81 (2016), 1531–1554.
- D. R. Hirschfeldt, C. G. Jockusch, Jr., B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- Q. Le Houérou, L. Levy Patey and A. Mimouni, *The reverse mathematics of the pigeonhole hierarchy*, arXiv:2407.01236 (2024).
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Weak König's lemma*.

:::::exercises
::::exercise[Hyperimmunity at two levels]{#ex-wkl-two-hyperimmunities difficulty=2 objective="Use the compactness of the questions of Jockusch–Soare forcing on primitive recursive trees at both levels to preserve two hyperimmunities at once."}
Let $f$ be a hyperimmune function and $g$ a function hyperimmune relative to $\emptyset'$. Show that every non-empty $\Pi^0_1$ class $\mathcal P$ has a member $G$ such that $f$ is hyperimmune relative to $G$ and $g$ is hyperimmune relative to $G'$. Use the notion of forcing of :ref{#ex-wkl-primitive-trees}.

:::solution
By part 1 of :ref{#ex-wkl-primitive-trees}, $\mathcal P = [T_0]$ for an infinite primitive recursive tree $T_0$; we use the conditions below $T_0$. For a $\Sigma^0_1$ sentence $\varphi$ and a condition $T$, write $T \mathrel{?{\vdash}} \varphi$ for the question of that exercise.

*Level 1.* Write "$\Phi^G_e(m)\converge < b$" for the $\Sigma^0_1$ sentence saying that the computation converges with a value less than $b$. The question is **compact**: if a length $\ell$ witnesses $T \mathrel{?{\vdash}} \Phi^G_e(m)\converge$, the finitely many nodes of length $\ell$ give finitely many values, and for $b$ larger than all of them the same $\ell$ witnesses $T \mathrel{?{\vdash}} \Phi^G_e(m)\converge < b$. Given $T$, let $h(m)$ be the first $b$ found, in a search over $b$ and $\ell$, with $T \mathrel{?{\vdash}} \Phi^G_e(m)\converge < b$; since the question is $\Sigma^0_1$ uniformly, $h$ is partial computable. If $h(m)$ is undefined, then $T \mathrel{?{\nvdash}} \Phi^G_e(m)\converge$ by compactness, and property 2 gives an extension all of whose members satisfy $\Phi^G_e(m)\diverge$. If $h$ is total, it is computable, so $f(m) > h(m)$ for some $m$, and $T$ itself forces $\Phi^G_e(m)\converge < h(m)$. In both cases, all members $G$ of the extension satisfy: $\Phi^G_e$ is partial or $\Phi^G_e(m) < f(m)$ for some $m$.

*Level 2.* Write "$\Phi^{G'}_e(m)\converge$" and "$\Phi^{G'}_e(m)\converge < b$" as the $\Sigma^0_2$ sentences $\exists \langle k, y \rangle\ \psi_m(k, y)$ and $\exists \langle k, y \rangle\ \psi^b_m(k, y)$ of :ref{#ex-cohen-jump-hyperimmunity}, with $\psi^b_m(k, y)$ equal to the sentence $\psi_m(k, y)$ if $k < b$ and to a false sentence otherwise. The lifted question is compact: a witness $(S, \langle k, y \rangle)$ of $T \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge$ is a witness of $T \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < k + 1$, since the sentences $\neg\psi_m(k, y)$ and $\neg\psi^{k+1}_m(k, y)$ are the same. The lifted question is $\Sigma^0_2$ uniformly, so the function $h(m)$, the first $b$ found with $T \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < b$, is partial $\emptyset'$-computable. As at level 1, either some extension forces $\Phi^{G'}_e(m)\diverge$, or $h$ is total and $\emptyset'$-computable, $g(m) > h(m)$ for some $m$, and some extension forces $\Phi^{G'}_e(m)\converge < h(m)$, by :ref{#lem-lifted-question}.

Both families of conditions are dense below $T_0$. A $2$-generic filter through $T_0$ meeting all of them gives, by :ref{#thm-forcing-truth}, a member $G$ of $\mathcal P$ such that no total $\Phi^G_e$ dominates $f$ and no total $\Phi^{G'}_e$ dominates $g$. Adapted from an exercise of the chapter *Jump cone avoidance* of Patey's monograph, attributed there to Le Houérou, Levy Patey and Mimouni (2024).
:::
::::

::::exercise[No non-computable Δ⁰₂ set below]{#ex-wkl-delta2-free difficulty=2 objective="Apply Wang's theorem to countably many cones to obtain PA sets and Scott ideals without high members and without non-computable $\Delta^0_2$ members."}
1. Show that there is a set $G$ PA relative to $\emptyset$, not high, such that every $\Delta^0_2$ set computable in $G$ is computable. Deduce that $G$ is neither low nor $\Delta^0_2$.
2. Show that there is a Scott ideal none of whose members is high, and every $\Delta^0_2$ member of which is computable.

:::solution
1. The non-computable $\Delta^0_2$ sets form a countable family $C_0, C_1, \dots$. By the remark after :ref{#thm-wkl-two-cones}, the non-empty $\Pi^0_1$ class of $\{0, 1\}$-valued DNC functions has a member $G$ with $C_n \not\leq_T G$ for every $n$ and $\emptyset'' \not\leq_T G'$. The set $G$ is PA and not high. It is not computable, since no computable function is DNC; if it were $\Delta^0_2$, it would be some $C_n$, and $C_n \leq_T G$. A low set $X$ satisfies $X \leq_T X' \leq_T \emptyset'$, so it is $\Delta^0_2$; hence $G$ is not low.
2. Let $\mathcal W$ be the class of sets $Y$ such that $\emptyset'' \not\leq_T Y'$ and every $\Delta^0_2$ set computable in $Y$ is computable. It is closed downward, since $X \leq_T Y$ implies $X' \leq_T Y'$. Let $Z \in \mathcal W$ and $T$ an infinite $Z$-computable tree. Every $C_n$ satisfies $C_n \not\leq_T Z$, and $\emptyset'' \not\leq_T Z'$. The proof of :ref{#thm-wkl-two-cones} relativizes to $Z$: the questions of Jockusch–Soare forcing relative to $Z$ are $\Sigma^0_1(Z)$ and $\Sigma^0_2(Z)$, and the countably many cones give countably many dense sets. So $T$ has a path $G$ with $C_n \not\leq_T Z \oplus G$ for every $n$ and $\emptyset'' \not\leq_T (Z \oplus G)'$, that is, $Z \oplus G \in \mathcal W$. So $\mathsf{WKL}$ preserves $\mathcal W$, and :ref{#lem-preservation-ideal} gives a Turing ideal contained in $\mathcal W$ and satisfying $\mathsf{WKL}$, a Scott ideal by :ref{#prop-wkl-scott}.

A Scott ideal contains PA sets, so by part 1 such an ideal contains non-$\Delta^0_2$ sets but no non-computable $\Delta^0_2$ set.
:::
::::

::::exercise[Two cones for Cohen generic sets]{#ex-wkl-cohen-two-cones difficulty=1 objective="Obtain the conclusion of Wang's theorem for Cohen generic sets, and see why it says nothing about members of $\Pi^0_1$ classes without computable members."}
Let $C$ be non-computable and $D \not\leq_T \emptyset'$. Show that every sufficiently Cohen generic set $G$ satisfies $C \not\leq_T G$ and $D \not\leq_T G'$. Show that a $1$-generic set is never a member of a $\Pi^0_1$ class without computable members.

:::solution
The question of Cohen forcing (:ref{#ex-cohen-question}) is $\Sigma^0_1$-preserving at level $1$ and $\Sigma^0_2$-preserving at level $2$, the latter being its lifted question (:ref{#ex-lifted-questions}, item 1). By :ref{#thm-local-cone-avoidance} with $\mathcal M = \{ \emptyset \}$ and :ref{#thm-local-jump-cone} with $\mathcal M = \{ \emptyset' \}$, the two conclusions hold for sets generic for two countable families of dense sets, hence for one set generic for both.

Let $\mathcal P = [T]$ with $T$ a computable tree, and $W$ the set of strings $\sigma$ such that, for some length $\ell$, no node of $T$ of length $\ell$ extends $\sigma$; by König's lemma this means $[\sigma] \cap \mathcal P = \emptyset$ by König's lemma; $W$ is c.e. If $G$ is $1$-generic, either a prefix of $G$ is in $W$, and $G \notin \mathcal P$, or a prefix $\sigma$ of $G$ has no extension in $W$. In the second case every $\tau \succeq \sigma$ satisfies $[\tau] \cap \mathcal P \neq \emptyset$, so $[\sigma] \subseteq \mathcal P$ since $\mathcal P$ is closed, and the computable set $\sigma 0 0 \cdots$ is a member of $\mathcal P$. So the Cohen generic sets are no substitute for :ref{#thm-wkl-two-cones}, whose point is to stay inside $\mathcal P$.
:::
::::

::::exercise[All cones at once]{#ex-wkl-all-cones difficulty=1 objective="Compare the avoidance of all cones at once at the two levels, and relate it to lowness."}
Let $\mathcal P$ be a non-empty $\Pi^0_1$ class with no computable member.

1. Show that no member $G$ of $\mathcal P$ satisfies $C \not\leq_T G$ for every non-computable $C$.
2. Show that a member $G$ satisfies $D \not\leq_T G'$ for every $D \not\leq_T \emptyset'$ if and only if $G$ is low, and that such members exist.
3. Explain why part 2 does not prove :ref{#thm-wkl-two-cones}.

:::solution
1. Take $C = G$, which is not computable.
2. If $G$ is low and $D \not\leq_T \emptyset'$, then $D \not\leq_T G'$, since $G' \leq_T \emptyset'$. If $G$ is not low, $D = G'$ satisfies $D \not\leq_T \emptyset'$ and $D \leq_T G'$. Low members exist by the low basis theorem.
3. A low member avoids every cone at level 2, but at level 1 it computes some non-computable $\Delta^0_2$ sets, at least itself, and may compute the given $C$. Wang's theorem trades the cones at level 2 that are avoided, now one or countably many, for the freedom to avoid a cone at level 1 above a $\Delta^0_2$ set.
:::
::::
:::::
