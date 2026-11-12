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

## Exercises

::::exercise{difficulty=1}
Let $\mathcal S$ be a countable ω-model of $\mathsf{RCA}_0$, that is, a countable Turing ideal. Show directly that $\mathcal S$ is contained in a countable ω-model of $\mathsf{WKL}_0$, and explain why the forcing argument is only needed for non-standard models.

:::solution
Let $T \in \mathcal S$ be an infinite binary tree. It has a path $G$ in $\mathcal P(\nat)$, and the class of sets computable in $G \oplus A$ for some $A \in \mathcal S$ is a countable Turing ideal containing $\mathcal S$ and $G$. Iterating as in the proof of :ref{#thm-harrington} gives a countable Turing ideal $\mathcal N \supseteq \mathcal S$ in which every infinite tree has a path, which is an ω-model of $\mathsf{WKL}_0$ by :ref{#thm-rca-turing-ideal}. No condition on $G$ is needed, because every ω-model satisfies full induction. In a non-standard model, the fact that every initial segment of $G$ belongs to the model does not guarantee $\Sigma^0_1$ induction for formulas mentioning $G$; the forcing construction is designed to ensure it.
:::
::::

::::exercise{difficulty=2}
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
