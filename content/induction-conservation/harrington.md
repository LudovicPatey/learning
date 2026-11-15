---
title: Harrington's conservation theorem
summary: WKL₀ proves the same Π¹₁ sentences as RCA₀ (Harrington), by iterating the addition of generic paths over a countable model; the first-order part of WKL₀ and the partial realization of Hilbert's program.
duration: 30
prerequisites: [forcing-subtrees, pigeonhole]
---

Weak König's lemma is not provable in $\mathsf{RCA}_0$: the computable sets form an ω-model of $\mathsf{RCA}_0$ in which it fails. Harrington proved that it nevertheless adds no new arithmetic consequences, nor even new $\Pi^1_1$ consequences. The proof shows that every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$. In an ω-model, adding a path through a tree only requires closing under Turing reducibility, since induction holds automatically. In a non-standard model, the path must be chosen so that $\Sigma^0_1$ induction survives; the previous lesson does this for one tree (:ref{#thm-path-induction}). This lesson iterates the construction, in the same way as ω-models of $\mathsf{WKL}_0$ are built by iterating the addition of a path (:ref{#thm-low-scott}), and draws the consequences. The iteration is a general method: to show that a principle $\forall X\, (F(X) \rightarrow \exists Y\, G(X, Y))$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, it suffices to add solutions to its instances one at a time while preserving $\Sigma^0_1$ induction. The same method gives conservation results for Ramsey-type principles, such as the cohesiveness principle (Cholak, Jockusch and Slaman).

## Π¹₁ conservation

:::proposition{#prop-pi11-conservation-method}
Let $S \subseteq T$ be $\mathcal L_2$-theories. If every countable model of $S$ has an ω-extension satisfying $T$, then $T$ is $\Pi^1_1$-conservative over $S$.
:::

:::proof{of=prop-pi11-conservation-method}
Let $\forall X\, \varphi(X)$ be a $\Pi^1_1$ sentence, with $\varphi$ arithmetic, not provable in $S$. A countable model $\mathcal M$ of $S + \exists X\, \neg \varphi(X)$ contains a set $A$ with $\mathcal M \models \neg \varphi(A)$. Let $\mathcal N$ be an ω-extension of $\mathcal M$ satisfying $T$. Then $A$ belongs to $\mathcal N$, and $\mathcal N \models \neg \varphi(A)$ since $\varphi$ is arithmetic. So $T$ does not prove $\forall X\, \varphi(X)$.
:::

:::theorem[Harrington]{#thm-harrington}
Every countable model of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf{WKL}_0$. Consequently, $\mathsf{WKL}_0$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, and a conservative extension of $\mathrm I\Sigma_1$.
:::

The second statement follows from the first by :ref{#prop-pi11-conservation-method}, since every sentence of $\mathcal L_1$ is $\Pi^1_1$, and by :ref{#thm-rca0-isigma1}. The rest of the lesson proves the first statement.

## From one path to a model of WKL₀

Recall from the previous lesson that $\mathcal M[G]$ is the ω-extension of $\mathcal M$ whose sets are those $\Delta^0_1$-definable in $\mathcal M \cup \{ G \}$, the analogue of the sets computable in $G$ and a set of $\mathcal M$.

:::lemma{#lem-harrington-extension}
Let $\mathcal M$ be a model of $\mathsf{RCA}_0$ and $G \subseteq M$ such that $\mathcal M \cup \{ G \}$ satisfies $\mathsf I\Sigma^0_1$. Then $\mathcal M[G]$ is an ω-extension of $\mathcal M$ satisfying $\mathsf{RCA}_0$, and $G \in \mathcal M[G]$. If $G$ is a path through a tree $T \in \mathcal M$, it is a path through $T$ in the sense of $\mathcal M[G]$.
:::

:::proof{of=lem-harrington-extension}
Every set of $\mathcal S$, and $G$, is defined by a bounded formula, so belongs to $\mathcal M[G]$. By hypothesis and :ref{#thm-induction-collection}, $\mathcal M \cup \{ G \}$ satisfies $\mathsf B\Sigma^0_1$. So :ref{#lem-delta1-substitution} applies to $\mathcal M \cup \{ G \}$ and finitely many sets of $\mathcal M[G]$: every $\Sigma^0_1$ or $\Pi^0_1$ formula with parameters in $\mathcal M[G]$ is equivalent in $\mathcal M[G]$ to a formula of the same class with parameters in $\mathcal M \cup \{ G \}$. As in the proof of :ref{#thm-rca0-isigma1}, $\Sigma^0_1$ induction in $\mathcal M[G]$ reduces to $\Sigma^0_1$ induction in $\mathcal M \cup \{ G \}$, and $\Delta^0_1$ comprehension holds because a set $\Delta^0_1$-definable with parameters in $\mathcal M[G]$ is $\Delta^0_1$-definable with parameters in $\mathcal M \cup \{ G \}$. Finally, "every initial segment of $G$ belongs to $T$" is an arithmetic statement about $G$ and $T$, so it has the same meaning in $\mathcal M[G]$ as outside.
:::

:::figure[The construction of :ref{#thm-harrington}. Each model $\mathcal M_{i+1} = \mathcal M_i[G]$ has the same numbers as $\mathcal M_i$, and adds a path through one tree while keeping $\Sigma^0_1$ induction. A bookkeeping of the pairs $(i_0, i_1)$ ensures that every tree of every $\mathcal M_{i_0}$ is treated at some later stage, so the union is a model of $\mathsf{WKL}_0$.]
<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="A chain of countable models M0, M1, M2, with the same numbers; at each step a path G through one tree is added; the union N is a model of WKL0"><defs><marker id="ic-t-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="40" y="40" width="70" height="40" rx="4" class="cell"/><text x="75.0" y="66.0" text-anchor="middle" class="math" font-size="16">M<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="112" y1="60" x2="168" y2="60" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-t-arrow)"/><text x="140.0" y="30" text-anchor="middle" class="label">add a path</text><rect x="170" y="40" width="70" height="40" rx="4" class="cell"/><text x="205.0" y="66.0" text-anchor="middle" class="math" font-size="16">M<tspan class="mrm" font-size="10" dy="4">1</tspan></text><line x1="242" y1="60" x2="298" y2="60" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-t-arrow)"/><text x="270.0" y="30" text-anchor="middle" class="label">add a path</text><rect x="300" y="40" width="70" height="40" rx="4" class="cell"/><text x="335.0" y="66.0" text-anchor="middle" class="math" font-size="16">M<tspan class="mrm" font-size="10" dy="4">2</tspan></text><line x1="372" y1="60" x2="410" y2="60" class="ink-stroke" stroke-width="1.2" marker-end="url(#ic-t-arrow)"/><text x="391.0" y="30" text-anchor="middle" class="label">add a path</text><text x="422" y="66" class="mrm" font-size="15">⋯</text><rect x="460" y="40" width="110" height="40" rx="4" class="cell head-cell"/><text x="515" y="66" text-anchor="middle" class="label">union N</text><text x="300" y="110" text-anchor="middle" class="label">same numbers throughout; each step keeps Σ⁰₁ induction; the union satisfies WKL₀</text></svg>
:::

:::proof{of=thm-harrington}
Let $\mathcal M_0$ be a countable model of $\mathsf{RCA}_0$. We build countable ω-extensions $\mathcal M_0 \subseteq \mathcal M_1 \subseteq \cdots$, all models of $\mathsf{RCA}_0$, as follows. Fix a bijection $i \mapsto (i_0, i_1)$ from $\nat$ to $\nat^2$ with $i_0 \leq i$. At step $i$, consider the $i_1$-th set of $\mathcal M_{i_0}$, in a fixed enumeration of its sets. If it is an $\mathcal M_i$-infinite tree $T$, let $\mathcal M_{i+1} = \mathcal M_i[G]$ for a path $G$ through $T$ such that $\mathcal M_i \cup \{ G \}$ satisfies $\mathsf I\Sigma^0_1$, given by :ref{#thm-path-induction} applied to $\mathcal M_i$; otherwise let $\mathcal M_{i+1} = \mathcal M_i$. By :ref{#lem-harrington-extension}, every $\mathcal M_{i+1}$ is a model of $\mathsf{RCA}_0$; it is countable, since its sets are defined by formulas with parameters in the countable structure $\mathcal M_i \cup \{ G \}$.

Let $\mathcal N$ be the union: same first-order part, and the union of the second-order parts. Every instance of the axioms of $\mathsf{RCA}_0$ in $\mathcal N$ has finitely many set parameters, all in some $\mathcal M_i$, and is arithmetic apart from the conclusion of comprehension; it holds in $\mathcal M_i$, with the same meaning, and the set given by comprehension in $\mathcal M_i$ belongs to $\mathcal N$. So $\mathcal N \models \mathsf{RCA}_0$. If $T \in \mathcal N$ is an infinite tree in the sense of $\mathcal N$, it is the $i_1$-th set of some $\mathcal M_{i_0}$, and it is infinite in the sense of $\mathcal M_i$ at step $i$, since this is arithmetic; so a path through $T$ was added at step $i$, and it belongs to $\mathcal N$. So $\mathcal N \models \mathsf{WKL}_0$.
:::

## Consequences

By :ref{#thm-harrington}, $\mathsf{WKL}_0$ and $\mathsf{RCA}_0$ prove the same arithmetic sentences, and even the same $\Pi^1_1$ sentences. Compactness arguments, such as the boundedness of continuous functions on $[0, 1]$ or Gödel's completeness theorem for countable languages, both provable in $\mathsf{WKL}_0$ (Simpson, Sections IV.2 and IV.3), therefore have no consequences for the natural numbers beyond $\mathrm I\Sigma_1$. Since $\mathrm I\Sigma_1$ is $\Pi_2$-conservative over primitive recursive arithmetic (Parsons), every $\Pi_2$ sentence of $\mathcal L_1$ provable in $\mathsf{WKL}_0$ is provable in primitive recursive arithmetic, a system regarded as finitistic in Hilbert's sense. This is Friedman's conservation theorem (Simpson, Theorem IX.3.16), which Simpson presents as a partial realization of Hilbert's program (Remark IX.3.18).

The theorem does not extend to $\Pi^1_2$ sentences: $\mathsf{WKL}$ itself is $\Pi^1_2$.

:::quiz[the generic extension]
Why is the extension $\mathcal M[G]$ taken, rather than $\mathcal M \cup \{ G \}$?

- [x] Because $\mathcal M \cup \{ G \}$ does not satisfy $\Delta^0_1$ comprehension in general: sets computable from $G$ and sets of $\mathcal M$, such as $G \oplus A$, must be added.
- [ ] Because $\mathcal M \cup \{ G \}$ does not satisfy $\Sigma^0_1$ induction.

  It does, by the choice of $G$ (:ref{#thm-path-induction}); this is the hypothesis of :ref{#lem-harrington-extension}.
- [ ] Because $G$ is not a path in $\mathcal M \cup \{ G \}$.

  It is a path in both structures, since the property is arithmetic.

---

Why does the proof of :ref{#thm-harrington} handle each tree at a stage $i$ with $i_0 \leq i$?

- [x] Because the tree must already belong to $\mathcal M_i$ when its path is added; the enumeration of pairs revisits every set of every $\mathcal M_{i_0}$ at a later stage.
- [ ] Because the trees must be handled in increasing order of size.

  The order is only a bookkeeping device.
- [ ] Because $\mathcal M_i$ is finite.

  Each $\mathcal M_i$ is countable and infinite.
:::

::::exercise{#ex-wkl-not-bsigma2 difficulty=2 objective="Combine Harrington's theorem with the separation of $\mathrm I\Sigma_1$ from $\mathrm B\Sigma_2$ and with Hirst's theorem."}
Show that $\mathsf{WKL}_0$ proves neither $\mathsf B\Sigma^0_2$ nor $\mathsf{RT}^1_{<\infty}$.

:::solution
By :ref{#thm-isigma-not-bsigma}, there is a model of $\mathrm I\Sigma_1$ in which some instance of $\Sigma_2$ collection, an $\mathcal L_1$ sentence $\sigma$, fails. So $\mathrm I\Sigma_1$ does not prove $\sigma$, and by :ref{#thm-harrington}, neither does $\mathsf{WKL}_0$. Since $\sigma$ is an instance of $\mathsf B\Sigma^0_2$, $\mathsf{WKL}_0$ does not prove $\mathsf B\Sigma^0_2$. By :ref{#thm-hirst}, which holds over $\mathsf{RCA}_0 \subseteq \mathsf{WKL}_0$, it does not prove $\mathsf{RT}^1_{<\infty}$ either.
:::
::::

## Notes and references

Harrington's theorem (1977) was unpublished; it was communicated by Friedman, and Simpson gives the first published proof, Theorem IX.2.1, together with the consequences for Hilbert's program in Section IX.3. The iteration presented here follows Monin and Patey, chapter *Induction and conservation*; Hirschfeldt, Proposition 7.10, and Dzhafarov and Mummert, Corollary 5.9.6 and Section 7.7, isolate the same general method for $\Pi^1_1$ conservation, and apply it to the cohesiveness principle (Cholak, Jockusch and Slaman).

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections IX.2–IX.3.
- S. G. Simpson, *Partial realizations of Hilbert's program*, Journal of Symbolic Logic 53 (1988), 349–363.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 7.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.9 and 7.7.
- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.

:::::exercises
::::exercise{#ex-omega-wkl-direct difficulty=1 objective="Compare the construction of ω-models of $\mathsf{WKL}_0$ with Harrington's construction, and see why no genericity is needed in ω-models."}
Let $\mathcal S$ be a countable ω-model of $\mathsf{RCA}_0$, that is, a countable Turing ideal. Show directly that $\mathcal S$ is contained in a countable ω-model of $\mathsf{WKL}_0$, and explain why the forcing argument is only needed for non-standard models.

:::solution
Let $T \in \mathcal S$ be an infinite binary tree. It has a path $G$ in $\mathcal P(\nat)$, and the class of sets computable in $G \oplus A$ for some $A \in \mathcal S$ is a countable Turing ideal containing $\mathcal S$ and $G$. Iterating as in the proof of :ref{#thm-harrington} gives a countable Turing ideal $\mathcal N \supseteq \mathcal S$ in which every infinite tree has a path, which is an ω-model of $\mathsf{WKL}_0$ by :ref{#thm-rca-turing-ideal}. No condition on $G$ is needed, because every ω-model satisfies full induction. In a non-standard model, the fact that every initial segment of $G$ belongs to the model does not guarantee $\Sigma^0_1$ induction for formulas mentioning $G$; the forcing construction is designed to ensure it.
:::
::::

::::exercise{#ex-wkl-first-order-structures difficulty=1 objective="Combine Friedman's expansion with Harrington's theorem to identify the first-order parts of the models of $\mathsf{WKL}_0$."}
Show that a countable $\mathcal L_1$-structure is the first-order part of a model of $\mathsf{WKL}_0$ if and only if it is a model of $\mathrm I\Sigma_1$.

:::solution
If $(M, \mathcal S) \models \mathsf{WKL}_0$, then it satisfies the instances of $\Sigma^0_1$ induction for formulas of $\mathcal L_1$, whose truth depends only on $M$; so $M \models \mathrm I\Sigma_1$. Conversely, if $M$ is a countable model of $\mathrm I\Sigma_1$, the proof of :ref{#thm-rca0-isigma1} gives a countable model $(M, \mathcal D)$ of $\mathsf{RCA}_0$, and :ref{#thm-harrington} gives an ω-extension of it satisfying $\mathsf{WKL}_0$, whose first-order part is still $M$.
:::
::::

::::exercise{#ex-pi11-method difficulty=2 objective="Prove the general method for $\Pi^1_1$ conservation over $\mathsf{RCA}_0$ by iterating the addition of solutions with bookkeeping."}
Let $\mathsf P$ be a sentence $\forall X\, (\theta(X) \rightarrow \exists Y\, \psi(X, Y))$ with $\theta$ and $\psi$ arithmetic. Suppose that for every countable model $\mathcal M$ of $\mathsf{RCA}_0$ and every set $X$ of $\mathcal M$ with $\mathcal M \models \theta(X)$, there is $G \subseteq M$ such that $\mathcal M \cup \{ G \}$ satisfies $\mathsf I\Sigma^0_1$ and $\psi(X, G)$. Show that $\mathsf{RCA}_0 + \mathsf P$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$. Which choice of $\theta$, $\psi$ gives :ref{#thm-harrington}?

:::solution
By :ref{#prop-pi11-conservation-method}, it suffices to show that every countable model $\mathcal M_0$ of $\mathsf{RCA}_0$ has an ω-extension satisfying $\mathsf P$. Fix a bijection $i \mapsto (i_0, i_1)$ from $\nat$ to $\nat^2$ with $i_0 \leq i$, and build countable models $\mathcal M_0 \subseteq \mathcal M_1 \subseteq \cdots$ of $\mathsf{RCA}_0$ with the same first-order part. At step $i$, let $X$ be the $i_1$-th set of $\mathcal M_{i_0}$ in a fixed enumeration. If $\mathcal M_i \models \theta(X)$, choose $G$ for $\mathcal M_i$ and $X$ as in the hypothesis and let $\mathcal M_{i+1} = \mathcal M_i[G]$; otherwise let $\mathcal M_{i+1} = \mathcal M_i$. By :ref{#lem-harrington-extension}, $\mathcal M_{i+1}$ is a model of $\mathsf{RCA}_0$ containing $G$, and it is countable. Since $\psi$ is arithmetic, $\mathcal M_{i+1} \models \psi(X, G)$.

Let $\mathcal N$ be the union. It satisfies $\mathsf{RCA}_0$, by the argument of the proof of :ref{#thm-harrington}. Let $X \in \mathcal N$ with $\mathcal N \models \theta(X)$. Then $X$ is the $i_1$-th set of some $\mathcal M_{i_0}$; at the step $i$ corresponding to $(i_0, i_1)$, $\mathcal M_i \models \theta(X)$, since $\theta$ is arithmetic, so a set $G$ with $\mathcal M_{i+1} \models \psi(X, G)$ was added, and $\mathcal N \models \psi(X, G)$. So $\mathcal N \models \mathsf P$.

Harrington's theorem is the case where $\theta(X)$ says that $X$ is an infinite binary tree and $\psi(X, Y)$ that $Y$ is a path through it; the hypothesis is :ref{#thm-path-induction}. This is Hirschfeldt, Proposition 7.10.
:::
::::

::::exercise{#ex-wkl-l1-axioms difficulty=2 objective="Extend Harrington's conservation theorem to base theories with additional first-order axioms, and see why axioms with set parameters are not covered."}
Let $\Gamma$ be a set of sentences of $\mathcal L_1$. Show that $\mathsf{WKL}_0 + \Gamma$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \Gamma$; for instance, with $\Gamma = \mathrm I\Sigma_2$. Why does the argument not show that $\mathsf{WKL}_0 + \mathsf B\Sigma^0_2$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathsf B\Sigma^0_2$, where the scheme $\mathsf B\Sigma^0_2$ allows set parameters?

:::solution
Let $\mathcal M$ be a countable model of $\mathsf{RCA}_0 + \Gamma$. By :ref{#thm-harrington}, it has an ω-extension $\mathcal N$ satisfying $\mathsf{WKL}_0$. A sentence of $\mathcal L_1$ has no set variables, so its truth only depends on the first-order part, which is the same in $\mathcal M$ and $\mathcal N$; so $\mathcal N \models \Gamma$. By :ref{#prop-pi11-conservation-method}, $\mathsf{WKL}_0 + \Gamma$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \Gamma$.

An instance of $\mathsf B\Sigma^0_2$ with set parameters is the universal closure $\forall \bar X\ \beta(\bar X)$ of an arithmetic formula: a $\Pi^1_1$ sentence. Such sentences are preserved from $\mathcal N$ down to $\mathcal M$, not upwards: $\mathcal N$ contains new sets, such as the paths added in the construction, and nothing in the proof of :ref{#thm-harrington} ensures that the instances of $\mathsf B\Sigma^0_2$ with these sets as parameters hold in $\mathcal N$. The forcing preserves $\mathsf I\Sigma^0_1$ only.
:::
::::

::::exercise{#ex-coh-conservation difficulty=3 objective="Apply the general method of $\Pi^1_1$ conservation with Mathias forcing over a non-standard model to show that cohesiveness proves no new $\Pi^1_1$ sentences."}
A sequence of sets $\vec R = (R_i)$ is coded by a set whose $i$-th column is $R_i$. The principle $\mathsf{COH}$ states: for every sequence $\vec R$, there is an infinite set $G$ such that for every $i$ there is $w$ with $\forall x > w\ (x \in G \rightarrow x \in R_i)$ or $\forall x > w\ (x \in G \rightarrow x \notin R_i)$. Show that $\mathsf{RCA}_0 + \mathsf{COH}$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, and that it does not prove $\mathsf B\Sigma^0_2$.

Use :ref{#ex-pi11-method} and **Mathias forcing** over a countable model $\mathcal M = (M, \mathcal S)$ of $\mathsf{RCA}_0$: conditions are pairs $(F, I)$ of an $\mathcal M$-finite set $F$, coded by a number, and an unbounded set $I \in \mathcal S$, with every element of $F$ less than every element of $I$; $(F', I')$ extends $(F, I)$ if $F \subseteq F' \subseteq F \cup I$ and $I' \subseteq I$.

:::solution
Fix $\vec R \in \mathcal S$. We build a sequence $(F_0, I_0) \geq (F_1, I_1) \geq \cdots$, starting from $(\emptyset, M)$, that meets countably many dense sets of conditions, and let $G = \bigcup_j F_j$. Every $F_{j'}$ with $j' \geq j$ is included in $F_j \cup I_j$, so $G \subseteq F_j \cup I_j$ and $G \cap [0, \min I_j) = F_j$ for every $j$.

*Unboundedness.* For $n \in M$, the conditions $(F, I)$ such that $F$ has an element $\geq n$ form a dense set: add to $F$ an element of $I$ above $n$, and remove from $I$ the elements up to it. Meeting them all makes $G$ unbounded. In particular, for every $k$ there is $j$ with $\min I_j > k$, and then $G \uh k$ is the string $\langle F_j \rangle_k$ of length $k$ given by $F_j$.

*Cohesiveness.* For $i \in M$, the conditions with $I \subseteq R_i$ or $I \cap R_i = \emptyset$ form a dense set: given $(F, I)$, the sets $I \cap R_i$ and $I \setminus R_i$ exist by $\Delta^0_1$ comprehension, and one of them is unbounded, since $I$ is; it replaces $I$. If $(F_j, I_j)$ is such a condition and $w = \max F_j$ (or $w = 0$ if $F_j = \emptyset$), every $x \in G$ with $x > w$ belongs to $I_j$, hence to $R_i$, or to its complement, for all $x > w$ at once.

*Induction.* Let $\Theta(x, X)$ be a $\Sigma^0_1$ formula with parameters in $\mathcal M$, and $H$ given by :ref{#lem-sigma1-normal-form} for the full binary tree. For a condition $(F, I)$, let $Q_{F, I}(x)$ be the $\Sigma^0_1$ formula, with parameters $F$, $I$: there are an $\mathcal M$-finite set $E \subseteq I$ and $k$ with $H(x, \langle F \cup E \rangle_k)$. It says that some finite extension of the condition makes $\Theta(x, G)$ true. Let $D_\Theta$ be the set of conditions $(F, I)$ such that either (a) $\neg Q_{F, I}(x)$ for every $x$, or (b) for some $n$, $H(n, \langle F \rangle_k)$ for some $k \leq \min I$, and $\neg Q_{F, I}(x)$ for every $x < n$.

$D_\Theta$ is dense. Let $(F, I)$ be a condition. If $Q_{F, I}(x)$ fails for every $x$, it satisfies (a). Otherwise, by $\mathsf L\Sigma^0_1$ in $\mathcal M$ (:ref{#prop-least-number}), there is a least $n$ with $Q_{F, I}(n)$, witnessed by $E$ and $k$. Let $I' = \{ y \in I : y > k \text{ and } y > \max (F \cup E) \}$, unbounded and in $\mathcal S$. Then $(F \cup E, I')$ extends $(F, I)$ and satisfies (b) with this $n$: $k \leq \min I'$, and if $Q_{F \cup E, I'}(x)$ held for some $x < n$, with a finite $E' \subseteq I'$, then $E \cup E' \subseteq I$ would witness $Q_{F, I}(x)$, contradicting the minimality of $n$.

Suppose the sequence meets $D_\Theta$ at $(F_j, I_j)$. If $\Theta(x, G)$ holds, then $H(x, G \uh k)$ for some $k$; choose $j' \geq j$ with $\min I_{j'} > k$. Then $G \uh k = \langle F_{j'} \rangle_k$ and $F_{j'} = F_j \cup E$ with $E = F_{j'} \setminus F_j \subseteq I_j$ finite, so $Q_{F_j, I_j}(x)$ holds. Hence in case (a), $\Theta(x, G)$ fails for every $x$; in case (b), $\Theta(n, G)$ holds, since $G \uh k = \langle F_j \rangle_k$ for $k \leq \min I_j$, and $\Theta(x, G)$ fails for $x < n$. If the sequence meets $D_\Theta$ for every $\Theta$, then every $\Sigma^0_1$ formula with parameters in $\mathcal M \cup \{ G \}$ that has a solution has a least one: $\mathcal M \cup \{ G \}$ satisfies $\mathsf L\Sigma^0_1$. By the first part of the proof of :ref{#prop-least-number}, which uses only the basic axioms, it satisfies $\mathsf I\Pi^0_1$, which contains $\mathsf I\Delta^0_0$, and therefore $\mathsf I\Sigma^0_1$ by :ref{#thm-isigma-ipi}.

The dense sets used are countably many. So $G$ is unbounded, cohesive for $\vec R$, and $\mathcal M \cup \{ G \} \models \mathsf I\Sigma^0_1$. By :ref{#ex-pi11-method}, with $\theta(X)$ true for every $X$ and $\psi(X, Y)$ saying that $Y$ is infinite and cohesive for the columns of $X$, $\mathsf{RCA}_0 + \mathsf{COH}$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$.

Finally, an instance of $\mathsf B\Sigma^0_2$ not provable in $\mathrm I\Sigma_1$ (:ref{#ex-wkl-not-bsigma2}) is an $\mathcal L_1$ sentence, hence $\Pi^1_1$, and is not provable in $\mathsf{RCA}_0$ by :ref{#thm-rca0-isigma1}; so $\mathsf{RCA}_0 + \mathsf{COH}$ does not prove it. Compare with :ref{#ex-stcoh}. This is due to Cholak, Jockusch and Slaman (2001); adapted from Hirschfeldt, Exercise 7.11.
:::
::::

::::exercise{#ex-majorize difficulty=3 objective="Add dense sets to Harrington's forcing to control the growth of the functions of the generic extension."}
For functions $f, g$ from $M$ to $M$, say that $f$ **majorizes** $g$ if $g(x) \leq f(x)$ for every $x \in M$. Let $\mathcal M = (M, \mathcal S)$ be a countable model of $\mathsf{RCA}_0$. Show that $\mathcal M$ has a countable ω-extension $\mathcal N$ satisfying $\mathsf{WKL}_0$ in which every function is majorized by a function of $\mathcal M$.

:::solution
*One step.* Let $T \in \mathcal S$ be an $\mathcal M$-infinite binary tree and $\mathbb P$ as in the lesson on forcing with infinite subtrees. For a $\Sigma^0_1$ formula $E(x, X)$ with parameters in $\mathcal M$, let $H_E$ be given by :ref{#lem-sigma1-normal-form}, and for $S \in \mathbb P$ and $x \in M$ let $S_x = \{ \rho \in S : \forall k \leq |\rho|\ \neg H_E(x, \rho \uh k) \}$, a tree of $\mathcal S$. Let $D_E$ be the set of $S \in \mathbb P$ such that either (i) $S_x = S$ for some $x$, or (ii) $S_x$ is not $\mathcal M$-infinite for any $x$. It is dense: given $S \in \mathbb P$, if some $S_x$ is $\mathcal M$-infinite, then $S_x \in \mathbb P$ and $(S_x)_x = S_x$, so $S_x$ satisfies (i); otherwise $S$ satisfies (ii). Build the generic path $G$ of :ref{#thm-path-induction}, meeting moreover the sets $D_E$ for all $\Sigma^0_1$ formulas $E$ with parameters in $\mathcal M$; there are countably many, so $\mathcal M \cup \{ G \} \models \mathsf I\Sigma^0_1$ as before.

Let $g$ be a function of $\mathcal M[G]$. Its graph is $\{ p : \Gamma(p, G) \}$ for a $\Sigma^0_1$ formula $\Gamma(p, X)$ with parameters in $\mathcal M$; write $\Gamma(p, X) \equiv \exists z\ \gamma(p, z, X)$ with $\gamma$ bounded, and let $E(x, X) \equiv \exists w\ \varepsilon(x, w, X)$, where $\varepsilon(x, w, X)$ says that $w = \langle y, z \rangle$ for some $y, z \leq w$ with $\gamma(\langle x, y \rangle, z, X)$. By the construction of $H_E$ in the proof of :ref{#lem-sigma1-normal-form}, if $H_E(x, G \uh k)$ then $\varepsilon(x, w, G)$ for some $w < k$, so $g(x) = y \leq w < k$; and $E(x, G)$ holds for every $x$, since $g$ is total. Let $S \in D_E$ be met by the generic sequence; $G$ is a path through $S$. Case (i) is impossible: if $S_x = S$, then $G \uh k \in S_x$ for all $k$, so $H_E(x, G \uh k)$ fails for every $k$, and $E(x, G)$ fails. In case (ii), let $f(x)$ be the least $m$ such that $S_x$ has no string of length $m$. The quantifiers over strings of length $m$ are bounded, so the graph of $f$ is defined by a bounded formula with parameters $S$ and those of $H_E$; $f$ is total by (ii), and belongs to $\mathcal S$ by $\Delta^0_1$ comprehension. Since $G \uh f(x) \in S \setminus S_x$, there is $k \leq f(x)$ with $H_E(x, G \uh k)$, hence $g(x) < k \leq f(x)$. So every function of $\mathcal M[G]$ is majorized by a function of $\mathcal M$.

*Iteration.* Build $\mathcal M_0 = \mathcal M \subseteq \mathcal M_1 \subseteq \cdots$ as in the proof of :ref{#thm-harrington}, using at each step the path just described. Every function of $\mathcal M_{i+1}$ is majorized by a function of $\mathcal M_i$, so, by induction on $i$ and transitivity, by a function of $\mathcal M_0$. The union $\mathcal N$ is a countable ω-extension of $\mathcal M$ satisfying $\mathsf{WKL}_0$, and each of its functions belongs to some $\mathcal M_i$; being a function is arithmetic, so it is one in $\mathcal M_i$ as well. Hence every function of $\mathcal N$ is majorized by a function of $\mathcal M$.

For $\mathcal M = \mathrm{REC}$, this gives an ω-model of $\mathsf{WKL}_0$ whose functions are all dominated by computable functions, as in the computably dominated basis theorem. Adapted from Simpson, Exercise IX.2.8.
:::
::::
:::::
