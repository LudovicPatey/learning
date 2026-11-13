---
title: Jump PA avoidance
summary: A problem admits jump PA avoidance if its instances have solutions whose jump is not PA relative to the jump of the parameter; such problems do not imply cohesiveness on ω-models; a forcing question for Σ⁰₂ sentences that merges two negative answers gives it; Mathias forcing with one reservoir in a partition regular class produces cohesive sets.
duration: 45
prerequisites: [jump-cone-avoidance/sigma2-questions, jump-cone-avoidance/pigeonhole-forcing, compactness-avoidance/weak-merging, lowness/beyond-zero-jump, ramsey-theorem/stable-colorings, reducibilities/preservation]
---

The course on compactness avoidance showed how to build solutions that are not PA, and the course on jump cone avoidance how to control the jump of a solution. This course combines the two: it builds solutions $Y$ whose jump $Y'$ is not PA relative to $\emptyset'$. The motivation is cohesiveness. By a theorem of Jockusch and Stephan (:ref{#prop-coh-no-low}), some computable sequence of sets has only cohesive sets whose jump is PA relative to $\emptyset'$. A problem whose computable instances always have solutions with a jump that is not PA relative to $\emptyset'$ therefore cannot prove cohesiveness on ω-models. The main theorem of the course, due to Monin and Patey, is that the pigeonhole principle for $\Delta^0_2$ sets has this property; it follows that stable Ramsey's theorem for pairs does not imply Ramsey's theorem for pairs on ω-models.

The abstract part of the theory is compactness avoidance one level up: a forcing question for $\Sigma^0_2$ sentences, with answers $\Sigma^0_1$ relative to $\emptyset'$, that can force two negative answers at once. This lesson sets it up. The difficulty, treated in the rest of the course, is that the variants of Mathias forcing used for combinatorial principles do not have such a question.

## The definition

We use the notation of :ref{to="compactness-avoidance/pa-avoidance"}: for a set $D$, $J^D$ is the partial $\{0, 1\}$-valued function $x \mapsto \Phi^D_x(x)$, and a set is PA relative to $D$ if it computes a total $\{0, 1\}$-valued function $f$ with $f(x) \neq J^D(x)$ whenever $J^D(x)$ is defined. The relevant oracle is now the jump $D'$.

:::definition{#def-jump-pa-avoidance}
Let $\mathsf P$ be a problem.

1. $\mathsf P$ admits **jump PA avoidance** if for all sets $D \leq_T Z$ such that $Z'$ is not PA relative to $D'$, and every instance $X \leq_T Z$ of $\mathsf P$, there is a solution $Y$ to $X$ such that $(Z \oplus Y)'$ is not PA relative to $D'$.
2. $\mathsf P$ admits **strong jump PA avoidance** if the same holds for every instance $X$ of $\mathsf P$.
:::

The parameters play the same roles as in :ref{#def-pa-avoidance}. With $D = \emptyset$ the hypothesis is that $Z'$ is not PA relative to $\emptyset'$, and the definition builds ω-models. With $D = Z$ it applies to every $Z$, since $Z'$ is never PA relative to itself, and says that $(Z \oplus Y)'$ is not PA relative to $Z'$. If $D \leq_T Z$, then $D' \leq_T Z'$, so the hypothesis makes sense as a weakness relation between two jumps.

:::proposition{#prop-jump-pa-model}
Let $\mathsf P$ admit jump PA avoidance.

1. There is a Turing ideal $\mathcal I$ satisfying $\mathsf P$ such that $Y'$ is not PA relative to $\emptyset'$ for every $Y \in \mathcal I$.
2. Such an ideal does not satisfy $\mathsf{COH}$. In particular $\mathsf{COH} \not\leq_\omega \mathsf P$.
:::

:::proof{of=prop-jump-pa-model}
1. Let $\mathcal W$ be the class of sets $Y$ such that $Y'$ is not PA relative to $\emptyset'$. It is closed downward, since $W \leq_T Y$ implies $W' \leq_T Y'$ and PA sets are closed upward. It contains $\emptyset$, since $\emptyset'$ is not PA relative to itself. With $D = \emptyset$, jump PA avoidance says that $\mathsf P$ preserves $\mathcal W$ (:ref{#def-weakness}). By :ref{#lem-preservation-ideal}, there is a Turing ideal $\mathcal I \subseteq \mathcal W$ satisfying $\mathsf P$.
2. Let $\vec R$ be the computable sequence of :ref{#prop-coh-no-low}. It belongs to $\mathcal I$, and every $\vec R$-cohesive set has a jump PA relative to $\emptyset'$, so none belongs to $\mathcal I$.
:::

The jump PA sets relative to $\emptyset'$ are exactly what blocks cohesiveness. Conversely, for every set $P$ PA relative to $\emptyset'$, there is a Turing ideal satisfying $\mathsf{COH}$ all of whose members $Y$ have $Y' \leq_T P$ (:ref{#thm-weakly-low-model} with :ref{#thm-coh-weakly-low}). So "every jump is computed by one fixed set PA relative to $\emptyset'$" is compatible with cohesiveness, and "no jump is PA relative to $\emptyset'$" is not.

:::example{#ex-jump-pa-problems}
1. **Problems with a low basis.** If every $Z$-computable instance has a solution $Y$ with $(Z \oplus Y)' \leq_T Z'$, the problem admits jump PA avoidance, since a set computable in $Z'$ is PA relative to $D'$ only if $Z'$ is. This covers $\mathsf{WKL}$ (low basis theorem relativized) and $\mathsf{RT}^1_2$ for $Z$-computable instances.
2. **Weakly low bases do not suffice.** $\mathsf{COH}$ admits a weakly low basis (:ref{#thm-coh-weakly-low}) but not jump PA avoidance: with $D = Z = \emptyset$, the sequence of :ref{#prop-coh-no-low} is a counterexample.
3. **$\mathsf{RT}^2_2$** does not admit jump PA avoidance. The proof of :ref{#thm-rt22-coh} turns a computable sequence $\vec R$ into a computable coloring all of whose infinite homogeneous sets are $\vec R$-cohesive (second exercise of :ref{to="ramsey-theorem/stable-colorings"}).
4. **$\mathsf D^2_2$ and $\mathsf{SRT}^2_2$** admit jump PA avoidance: this is the theorem of Monin and Patey proved in :ref{to="jump-compactness-avoidance/delta2-jump-pa"}.
:::

:::quiz[the definition]
In item 1 of :ref{#prop-jump-pa-model}, why is $\mathcal W$ closed downward under Turing reducibility?

- [x] Because $W \leq_T Y$ implies $W' \leq_T Y'$, and a set computing a set PA relative to $\emptyset'$ is itself PA relative to $\emptyset'$.
- [ ] Because the jump is order-preserving on degrees and injective.

  The jump is not injective on degrees, and injectivity plays no role.
- [ ] Because $\emptyset'$ is not PA relative to $\emptyset'$.

  This shows that $\emptyset \in \mathcal W$, not that $\mathcal W$ is closed downward.

---

Why does a weakly low basis not give jump PA avoidance?

- [x] It gives solutions whose jump is computable in a given set $P$ PA relative to $Z'$; such a jump may be PA relative to $Z'$, and for cohesiveness it sometimes must be.
- [ ] Because a weakly low basis only applies to $\Delta^0_2$ instances.

  It applies to all $Z$-computable instances.
- [ ] Because $P$ may compute $Z''$.

  Even when $P' \leq_T Z''$, the jump of the solution can be PA relative to $Z'$.
:::

## Merging at level 2

Recall from :ref{to="jump-cone-avoidance/sigma2-questions"} the forcing questions for $\Sigma^0_2$ sentences, with property 2 giving an extension that forces a $\Pi^0_2$ sentence in the sense of :ref{#def-forcing-relation}, and the notion of a question that is $\Sigma^0_1(\mathcal M)$-preserving (:ref{#def-jump-question-local}). By Post's theorem relativized, there is a computable function $t$ such that for every set $Z$ and every $G$, "$\Phi^{(Z \oplus G)'}_e(x)\converge = v$" holds if and only if the $\Sigma^0_2$ sentence $\chi_{e, x, v} = \exists y\ \Phi^{Z \oplus G}_{t(e, x, v)}(y)\diverge$ holds. Sentences are about $Z \oplus G$ for a fixed set $Z$.

:::definition{#def-jump-merging}
A forcing question for $\Sigma^0_2$ sentences is **merging** if for every condition $c$ and all $\Sigma^0_2$ sentences $\varphi_0$, $\varphi_1$ with $c \mathrel{?{\nvdash}} \varphi_0$ and $c \mathrel{?{\nvdash}} \varphi_1$, some extension of $c$ forces $\neg\varphi_0$ and $\neg\varphi_1$.
:::

The two negations are $\Pi^0_2$ sentences, forced by density. Merging asks that one condition carry both, so that later extensions cannot satisfy one of $\varphi_0$, $\varphi_1$ while keeping the other false.

:::theorem{#thm-jump-pa-merging}
Let $\mathbb P$ be a notion of forcing with a merging forcing question for $\Sigma^0_2$ sentences that is $\Sigma^0_1(\mathcal M)$-preserving, and let $D$ be a set such that no member of $\mathcal M$ is PA relative to $D'$. For every sufficiently generic set $G$, $(Z \oplus G)'$ is not PA relative to $D'$.
:::

:::proof{of=thm-jump-pa-merging}
For each $e$, let $E_e$ be the set of conditions $d$ for which there is $x$ such that either $J^{D'}(x)$ is defined and $d \Vdash \chi_{e, x, J^{D'}(x)}$, or $d \Vdash \neg\chi_{e, x, 0}$ and $d \Vdash \neg\chi_{e, x, 1}$. We show that $E_e$ is dense. Let $c$ be a condition and $X \in \mathcal M$ as in :ref{#def-jump-question-local}. The set
$$
U = \{ (x, v) \in \nat \times \{0, 1\} : c \mathrel{?{\vdash}} \chi_{e, x, v} \}
$$
is $\Sigma^0_1(X)$.

1. If $(x, J^{D'}(x)) \in U$ for some $x$ with $J^{D'}(x)$ defined, property 1 gives an extension in $E_e$.
2. If $(x, 0), (x, 1) \notin U$ for some $x$, merging gives an extension in $E_e$.
3. Otherwise, let $g(x)$ be the second coordinate of the first pair with first coordinate $x$ in an $X$-computable enumeration of $U$. It is total since case 2 fails, and $g(x) \neq J^{D'}(x)$ whenever $J^{D'}(x)$ is defined since case 1 fails. So $X$ is PA relative to $D'$, which is excluded.

Let $F$ be a $2$-generic filter (:ref{#def-n-generic-notion}) meeting every $E_e$. By :ref{#thm-forcing-truth}, the sentences forced by its conditions hold for $G_F$. For each $e$ there is $x$ such that $\Phi^{(Z \oplus G_F)'}_e(x)$ converges to $J^{D'}(x)$ or has no value in $\{0, 1\}$; so no $\Phi^{(Z \oplus G_F)'}_e$ is a $\{0, 1\}$-valued function DNC relative to $D'$.
:::

This is :ref{#thm-local-pa-avoidance} with $G'$ in place of $G$ and $D'$ in place of $D$, and :ref{#thm-local-jump-cone} with a merging step in the second case.

:::quiz[the abstract theorem]
In case 2 of the proof of :ref{#thm-jump-pa-merging}, why are two separate extensions, one forcing $\neg\chi_{e, x, 0}$ and one forcing $\neg\chi_{e, x, 1}$, useless?

- [x] On the first, $\Phi^{(Z \oplus G)'}_e(x)$ may still converge to $1$, which is a correct value of a DNC function when $J^{D'}(x)$ is undefined or equal to $0$.
- [ ] Because $\Pi^0_2$ sentences are only forced by density.

  Density is how each negation is forced; the issue is that one negation alone leaves a correct value available.
- [ ] Because the question is not $\Sigma^0_2$-preserving.

  Its definability is used in case 3.

---

In case 3, where is the hypothesis on $\mathcal M$ used?

- [x] The function $g$ is computable in the member $X$ of $\mathcal M$ attached to $c$ and is DNC relative to $D'$, so $X$ would be PA relative to $D'$.
- [ ] To show that $U$ is $\Sigma^0_1(X)$.

  This is the definition of a $\Sigma^0_1(\mathcal M)$-preserving question.
- [ ] To show that $g$ is total.

  Totality comes from the failure of case 2.
:::

:::example{#ex-cohen-jump-pa}
For Cohen forcing, let $\sigma \mathrel{?{\vdash}} \varphi$ if some $\tau \succeq \sigma$ forces $\varphi$ (:ref{#ex-cohen-question}). It is $\Sigma^0_2$-preserving, that is, $\Sigma^0_1(\{\emptyset'\})$-preserving. If $\sigma \mathrel{?{\nvdash}} \varphi_0$ and $\sigma \mathrel{?{\nvdash}} \varphi_1$, then $\sigma$ itself forces $\neg\varphi_0$ and $\neg\varphi_1$ by item 3 of :ref{#prop-forcing-basic}, so the question is merging. Since $\emptyset'$ is not PA relative to $\emptyset'$, :ref{#thm-jump-pa-merging} with $Z = D = \emptyset$ shows that every sufficiently generic set $G$ has a jump that is not PA relative to $\emptyset'$.
:::

The Cohen question is merging for the simplest reason: a negative answer is witnessed by the condition itself. Questions with this property, called **$\Pi^0_2$-extremal** in the monograph, are merging. For Mathias-type forcing, a negative answer about a $\Sigma^0_2$ sentence is witnessed by a restriction of the possible reservoirs, and two restrictions may be incompatible. The next section shows that this is unavoidable for notions of forcing with one reservoir.

## Mathias forcing with one reservoir

:::proposition{#prop-one-reservoir-cohesive}
Let $\mathcal I$ be a Turing ideal and $\mathcal P$ a non-trivial partition regular class. Consider Mathias conditions $(\sigma, X)$ with $X \in \mathcal I \cap \mathcal P$, with Mathias extension. Let $\vec R \in \mathcal I$ be a sequence of sets. For each $n$, the conditions with $X \subseteq R_n$ or $X \subseteq \overline{R_n}$ are dense, and so are the conditions whose stem has at least $n$ elements. Every set that is a member of conditions meeting all these dense sets is $\vec R$-cohesive.
:::

:::proof{of=prop-one-reservoir-cohesive}
Let $(\sigma, X)$ be a condition. The sets $X \cap R_n$ and $X \setminus R_n$ cover $X \in \mathcal P$, so one of them is in $\mathcal P$; it is in $\mathcal I$, since $X$ and $R_n$ are. So $(\sigma, X \cap R_n)$ or $(\sigma, X \setminus R_n)$ is an extension in the first dense set. Since $\mathcal P$ is non-trivial, $X$ is infinite; adding an element $x \in X$ above $|\sigma|$ to the stem and replacing $X$ by $X \setminus \{0, \dots, x\}$, which is in $\mathcal P$ by :ref{#lem-partition-regular-basic}, gives the second. A set $G$ that is a member of $(\sigma, X)$ with $X \subseteq R_n$ satisfies $G \setminus \{0, \dots, |\sigma| - 1\} \subseteq R_n$, and it is infinite by the second family.
:::

With $\mathcal I$ the computable sets and $\vec R$ the sequence of :ref{#prop-coh-no-low}, the sets built by such a notion of forcing have jumps PA relative to $\emptyset'$, whatever $\mathcal P$ is. This applies to the forcing of :ref{to="jump-cone-avoidance/pigeonhole-forcing"}, whose reservoirs lie in the core of a cohesive class. The obstruction is the operation of splitting the reservoir along a set and keeping a part: a forcing that allows it produces cohesive sets.

## Exercises

::::exercise{difficulty=1}
Show that if $\mathsf P$ and $\mathsf Q$ admit jump PA avoidance, so does the problem whose instances are pairs $(X_0, X_1)$ of an instance of $\mathsf P$ and an instance of $\mathsf Q$, with the pairs of solutions as solutions.

:::solution
Let $D \leq_T Z$ with $Z'$ not PA relative to $D'$, and $X_0, X_1 \leq_T Z$. Jump PA avoidance of $\mathsf P$ gives a solution $Y_0$ to $X_0$ with $(Z \oplus Y_0)'$ not PA relative to $D'$. Apply jump PA avoidance of $\mathsf Q$ with $Z \oplus Y_0$ in place of $Z$: since $D \leq_T Z \oplus Y_0$ and $X_1 \leq_T Z \oplus Y_0$, there is a solution $Y_1$ to $X_1$ with $(Z \oplus Y_0 \oplus Y_1)'$ not PA relative to $D'$. The pair $(Y_0, Y_1)$ is computable from $Y_0 \oplus Y_1$.
:::
::::

## Notes and references

Jump PA avoidance, with the two parameters $D \leq_T Z$, and the abstract theorem for merging questions follow the sections *Context and motivation* and *Jump PA avoidance* of the chapter *Jump compactness avoidance* of Patey's monograph, where the abstract theorem is left as an exercise and the Cohen example is proved directly, and the section *Mathias forcing and COH*, for the cohesiveness of generic sets with one reservoir. The characterization of the degrees of cohesive sets for the primitive recursive sets, whose jumps are exactly the sets PA relative to $\emptyset'$, is due to Jockusch and Stephan (1993); only the direction of :ref{#prop-coh-no-low} is used here. Liu's lemma is from Liu (2012).

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, sections *Context and motivation* and *Jump PA avoidance*.
