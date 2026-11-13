---
title: Jump PA avoidance
summary: A problem admits jump PA avoidance if its instances have solutions whose jump is not PA relative to the jump of the parameter; such problems do not imply cohesiveness on ω-models; low bases give jump PA avoidance, weakly low bases do not.
duration: 30
prerequisites: [compactness-avoidance/pa-avoidance, lowness/beyond-zero-jump, ramsey-theorem/cohesiveness, ramsey-theorem/stable-colorings, reducibilities/preservation]
---

The course on compactness avoidance showed how to build solutions that are not PA, and the course on jump cone avoidance how to control the jump of a solution. This course combines the two: it builds solutions $Y$ whose jump $Y'$ is not PA relative to $\emptyset'$. The motivation is cohesiveness. By a theorem of Jockusch and Stephan (:ref{#prop-coh-no-low}), some computable sequence of sets has only cohesive sets whose jump is PA relative to $\emptyset'$. A problem whose computable instances always have solutions with a jump that is not PA relative to $\emptyset'$ therefore cannot prove cohesiveness on ω-models. The main theorem of the course, due to Monin and Patey, is that the pigeonhole principle for $\Delta^0_2$ sets has this property; it follows that stable Ramsey's theorem for pairs does not imply Ramsey's theorem for pairs on ω-models.

This lesson defines jump PA avoidance, shows how it builds ω-models without cohesive sets, and places the main combinatorial principles with respect to it. The next lesson gives the abstract tool, compactness avoidance one level up: a forcing question for $\Sigma^0_2$ sentences, with answers $\Sigma^0_1$ relative to $\emptyset'$, that can force two negative answers at once. The difficulty, treated in the rest of the course, is that the variants of Mathias forcing used for combinatorial principles do not have such a question.

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

  $P$ can be chosen low relative to $Z'$, so that it does not compute $Z''$; the obstruction is that $P$ itself is PA relative to $Z'$, and a jump below $P$ is allowed to be PA relative to $Z'$ as well.
:::

## Exercises

::::exercise{difficulty=1}
Show that if $\mathsf P$ and $\mathsf Q$ admit jump PA avoidance, so does the problem whose instances are pairs $(X_0, X_1)$ of an instance of $\mathsf P$ and an instance of $\mathsf Q$, with the pairs of solutions as solutions.

:::solution
Let $D \leq_T Z$ with $Z'$ not PA relative to $D'$, and $X_0, X_1 \leq_T Z$. Jump PA avoidance of $\mathsf P$ gives a solution $Y_0$ to $X_0$ with $(Z \oplus Y_0)'$ not PA relative to $D'$. Apply jump PA avoidance of $\mathsf Q$ with $Z \oplus Y_0$ in place of $Z$: since $D \leq_T Z \oplus Y_0$ and $X_1 \leq_T Z \oplus Y_0$, there is a solution $Y_1$ to $X_1$ with $(Z \oplus Y_0 \oplus Y_1)'$ not PA relative to $D'$. The pair $(Y_0, Y_1)$ is computable from $Y_0 \oplus Y_1$.
:::
::::

::::exercise{difficulty=2}
Show that there are sets $Y_0$ and $Y_1$ such that neither $Y_0'$ nor $Y_1'$ is PA relative to $\emptyset'$, but $(Y_0 \oplus Y_1)'$ is. Explain why :ref{#def-jump-pa-avoidance} asks that $(Z \oplus Y)'$, and not only $Y'$, be not PA relative to $D'$.

:::solution
By the Sacks splitting theorem, admitted here (see :ref{to="reducibilities/preservation"}), $\emptyset'$ is the join of two low c.e. sets $Y_0$ and $Y_1$. Then $Y_0' \equiv_T Y_1' \equiv_T \emptyset'$, which is not PA relative to $\emptyset'$. But $Y_0 \oplus Y_1 \geq_T \emptyset'$, so $(Y_0 \oplus Y_1)' \geq_T \emptyset''$, and $\emptyset''$ is PA relative to $\emptyset'$: it computes the function equal to $1 - J^{\emptyset'}(x)$ when $J^{\emptyset'}(x)$ is defined and to $0$ otherwise, since it decides whether $\Phi^{\emptyset'}_x(x)$ converges.

So the class $\mathcal W$ of the proof of :ref{#prop-jump-pa-model} is not closed under joins, while a Turing ideal is. The construction of :ref{#lem-preservation-ideal} adds the solutions one at a time, and each new solution must remain in $\mathcal W$ together with all the sets built before it, which are coded in $Z$. A property asking only that $Y'$ be not PA relative to $\emptyset'$ could hold for every problem's solutions separately without giving any Turing ideal inside $\mathcal W$.
:::
::::

## Notes and references

Jump PA avoidance, with the two parameters $D \leq_T Z$, follows the section *Context and motivation* of the chapter *Jump compactness avoidance* of Patey's monograph, where the strong version is mentioned in a note. Jockusch and Stephan (1993) proved that the degrees of the sets cohesive for the family of primitive recursive sets are exactly the degrees whose jump is PA relative to $\emptyset'$; only the direction of :ref{#prop-coh-no-low} is used here. The ω-models of $\mathsf{COH}$ with jumps below a fixed set PA relative to $\emptyset'$ come from :ref{to="lowness/beyond-zero-jump"}.

- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- C. G. Jockusch, Jr. and F. Stephan, *Correction to "A cohesive set which is not high"*, Mathematical Logic Quarterly 43 (1997), 569.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Context and motivation*.
