---
title: Σ¹₁ classes and pseudo-well-orderings
summary: Σ¹₁ classes as projections of closed sets of Baire space; a computable tree with paths but no hyperarithmetic path; the Kleene basis theorem; Harrison's computable linear orders that are ill-founded but have no hyperarithmetic descending sequence; consequences for reverse mathematics.
duration: 35
prerequisites: [kleene-theorem]
---

In Cantor space, every non-empty $\Pi^0_1$ class has a low member. In Baire space, the situation changes completely: a computable tree on $\nat$ may have paths, none of them hyperarithmetic. The classes of sets definable by an existential set quantifier, the $\Sigma^1_1$ classes, are the projections of such trees, and their members can be very complex. This lesson proves the existence of computable trees without hyperarithmetic paths, the Kleene basis theorem, and the existence of **pseudo-well-orderings**: computable linear orders that look well-ordered to the hyperarithmetic sets. These objects explain why the hyperarithmetic sets do not form a model of $\mathsf{ATR}_0$.

## Σ¹₁ classes

:::definition{#def-sigma11-class}
A class $\mathcal A \subseteq \cs$ is **$\Sigma^1_1$** if there is an arithmetic formula $\varphi(X, Y)$ with $X \in \mathcal A \iff \exists Y\, \varphi(X, Y)$.
:::

By the normal form theorem (:ref{#thm-pi11-normal-form}), applied with the set variable $X$ as a parameter, every $\Sigma^1_1$ class is the projection of the set of paths of a computable tree: there is a computable tree $S$ of pairs $(\sigma, \tau) \in 2^{<\nat} \times \nat^{<\nat}$ of the same length such that $X \in \mathcal A$ if and only if $(X, f)$ is a path of $S$ for some $f \in \nat^\nat$. Every $\Pi^0_1$ class, and every hyperarithmetic singleton, is $\Sigma^1_1$.

## Trees without hyperarithmetic paths

:::theorem[Kleene]{#thm-no-hyp-path}
There is a computable tree $T \subseteq \nat^{<\nat}$ that has a path but no hyperarithmetic path.
:::

:::proof{of=thm-no-hyp-path}
Suppose that every computable tree with a path has a hyperarithmetic path. Then for every index $i$ of a computable tree,
$$
i \notin \mathrm{WF} \iff \exists X \in \mathrm{HYP}\ (X \text{ is a path of } T_i),
$$
and the right-hand side is $\Pi^1_1$ by :ref{#cor-hyp-quantifier}. So the complement of $\mathrm{WF}$ would be $\Pi^1_1$, and $\mathrm{WF}$ would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}.
:::

Hence the hyperarithmetic sets are not a basis for $\Sigma^1_1$ classes, nor even for the projections of $\Pi^0_1$ classes of Baire space. The difference with Cantor space comes from compactness: a computable binary tree has a leftmost path computable in $\emptyset'$, because the extendible nodes form a $\Pi^0_1$ set; for a tree on $\nat$, extendibility is $\Sigma^1_1$.

:::theorem[Kleene basis theorem]{#thm-kleene-basis}
Every non-empty $\Sigma^1_1$ class has a member computable in $\mathcal O$.
:::

:::proof{of=thm-kleene-basis}
Let $S$ be a computable tree of pairs whose projection is the class. Let $E$ be the set of nodes $(\sigma, \tau) \in S$ above which $S$ has a path; it is $\Sigma^1_1$, so its complement is $\Pi^1_1$ and many-one reducible to $\mathcal O$, which is $\Pi^1_1$-complete (admitted in :ref{to="computable-ordinals/trees-and-pi11"}). So $E \leq_T \mathcal O$. The root belongs to $E$. Define a path by choosing at each step the first immediate successor, in the order of codes, that belongs to $E$; one exists, since a path through the current node passes through one of its successors. The resulting path $(X, f)$ is computable in $E$, hence in $\mathcal O$, and $X$ belongs to the class.
:::

The bound is optimal in a strong sense: by :ref{#thm-no-hyp-path}, no hyperarithmetic degree suffices. Gandy (1960) refined the theorem: every non-empty $\Sigma^1_1$ class has a member $X$ with $\omega_1^X = \omega_1^{\mathrm{CK}}$ that does not hyperarithmetically compute $\mathcal O$. This **Gandy basis theorem** is the analogue of the low basis theorem, with $\omega_1^X = \omega_1^{\mathrm{CK}}$ playing the role of lowness; it is admitted here (Sacks, *Higher Recursion Theory*, Section III.1).

:::quiz[trees without hyperarithmetic paths]
In the proof of :ref{#thm-no-hyp-path}, why would the hypothesis make $\mathrm{WF}$ a $\Sigma^1_1$ set?

- [x] Because ill-foundedness, a $\Sigma^1_1$ property, would be equivalent to the existence of a hyperarithmetic path, a $\Pi^1_1$ property; so the complement of $\mathrm{WF}$ would be $\Pi^1_1$.
- [ ] Because every hyperarithmetic set is $\Sigma^1_1$.

  The relevant fact is the complexity of quantifying over hyperarithmetic sets, not the complexity of each of them.
- [ ] Because $\mathrm{WF}$ is $\Pi^1_1$.

  This is true but gives no contradiction by itself.

---

Why is the analogous statement false for binary trees?

- [x] Because a computable binary tree with a path has a path computable in $\emptyset'$, the leftmost one, since the extendible nodes of a binary tree form a $\Pi^0_1$ set by compactness.
- [ ] Because binary trees are finite.

  Infinite binary trees exist; compactness makes them tame.
- [ ] Because binary trees have no paths.

  By weak König's lemma, infinite binary trees have paths.
:::

## Pseudo-well-orderings

:::theorem[Harrison]{#thm-harrison}
There is a computable linear order that is not a well-ordering but has no hyperarithmetic descending sequence.
:::

:::proof{of=thm-harrison}
Let $T$ be the tree of :ref{#thm-no-hyp-path}, and $L$ the Kleene–Brouwer ordering on $T$, a computable linear order. Since $T$ has a path, $L$ is not a well-ordering (:ref{#thm-kleene-brouwer}).

Let $D = (\sigma_j)$ be a descending sequence in $L$; we show that $D'$ computes a path of $T$. If $\sigma_{j+1} <_{\mathrm{KB}} \sigma_j$, then $\sigma_{j+1}$ extends $\sigma_j$ or lies to its left, so whenever both are defined at position $0$, $\sigma_{j+1}(0) \leq \sigma_j(0)$. The root appears at most once, so from some point on all $\sigma_j$ are non-empty, and their first values form a non-increasing sequence, eventually constant equal to some $p(0)$. From that point on, all $\sigma_j$ begin with $p(0)$; the sequence $\langle p(0) \rangle$ appears at most once, after which all $\sigma_j$ have length at least $2$, and the same argument applies to their second values, which are eventually constant equal to some $p(1)$; and so on. Each $p \uh k$ is a prefix of some $\sigma_j \in T$, so $p$ is a path of $T$. The limit of a non-increasing sequence of numbers computable in $D$ is computable in $D'$, uniformly, so $p \leq_T D'$.

If $D$ were hyperarithmetic, so would be $D'$ and $p$, contradicting the choice of $T$.
:::

Such an order is a **pseudo-well-ordering**, or **Harrison order**. Harrison showed that its order type is $\omega_1^{\mathrm{CK}} \cdot (1 + \eta) + \rho$, where $\eta$ is the type of the rationals and $\rho < \omega_1^{\mathrm{CK}}$: an initial well-ordered part of length $\omega_1^{\mathrm{CK}}$, followed by densely many copies of it; we admit this description.

:::quiz[Harrison orders]
In the proof of :ref{#thm-harrison}, why are the first values $\sigma_j(0)$ eventually constant?

- [x] Because a step down in the Kleene–Brouwer ordering either extends the current sequence, keeping its first value, or moves to the left, which can only decrease the first value; a non-increasing sequence of numbers is eventually constant.
- [ ] Because $T$ is finitely branching.

  $T$ may be infinitely branching; the argument only uses the ordering.
- [ ] Because $D$ is hyperarithmetic.

  The argument applies to every descending sequence.
:::

## Consequences for reverse mathematics

In the ω-model $\mathrm{HYP}$, a Harrison order $L$ satisfies the arithmetic definition of being a linear order, and it has no descending sequence in the model; so $\mathrm{HYP}$ believes that $L$ is a well-ordering. Statements about well-orderings that hold in $\mathcal P(\nat)$ may then fail in $\mathrm{HYP}$. For instance, a jump hierarchy along $L$, as in the definition of $\mathsf{ATR}_0$, would compute all the sets $H_a$ along the well-ordered initial part of $L$, of length $\omega_1^{\mathrm{CK}}$, hence every hyperarithmetic set; no hyperarithmetic set does that, by the exercises of the previous lesson. With the description of the type of $L$, this shows that $\mathrm{HYP}$ is not an ω-model of $\mathsf{ATR}_0$, as stated in the course on the Big Five; we admit the details (Simpson, *Subsystems of Second Order Arithmetic*, Section VIII.3).

## Exercises

::::exercise{difficulty=1}
Show that every non-empty $\Pi^0_1$ class of subsets of $\nat$ has a hyperarithmetic member, and explain why this does not contradict :ref{#thm-no-hyp-path}.

:::solution
The leftmost path of a computable binary tree with a path is computable in $\emptyset'$ (:ref{#prop-leftmost-path}), hence hyperarithmetic. :ref{#thm-no-hyp-path} concerns trees on $\nat$, whose paths form closed subsets of Baire space, which are not compact; their extendible nodes are not $\Pi^0_1$ in general.
:::
::::

::::exercise{difficulty=2}
Show that the set of indices of computable linear orders with no hyperarithmetic descending sequence is $\Sigma^1_1$, and deduce a second proof of :ref{#thm-harrison}.

:::solution
By :ref{#cor-hyp-quantifier}, "there is a hyperarithmetic descending sequence in $L_e$" is $\Pi^1_1$, so its negation is $\Sigma^1_1$; "$L_e$ is a linear order" is arithmetic. The resulting $\Sigma^1_1$ set $P$ contains $\mathrm{WO}$. If it were equal to $\mathrm{WO}$, then $\mathrm{WO}$ would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}. So some $e \in P \setminus \mathrm{WO}$ is the index of a computable linear order that is not a well-ordering and has no hyperarithmetic descending sequence.
:::
::::

## Notes and references

Kleene (1955) proved the existence of computable trees with paths but no hyperarithmetic paths, and the basis theorem for $\mathcal O$. Gandy (1960) proved the basis theorem that bears his name. Harrison (1968) studied the pseudo-well-orderings and determined their order types.

- R. O. Gandy, *On a problem of Kleene's*, Bulletin of the American Mathematical Society 66 (1960), 501–502.
- J. Harrison, *Recursive pseudo-well-orderings*, Transactions of the American Mathematical Society 131 (1968), 526–543.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
