---
title: Selman's theorem
summary: A is enumeration reducible to B if and only if A is c.e. in every set in which B is c.e.; the non-uniform notion coincides with the uniform one; proof by forcing with finite enumerations of B; an enumeration degree is determined by the total degrees above it.
duration: 20
prerequisites: [enumeration-operators, turing-degrees/finite-extensions]
---

Enumeration reducibility asks for a uniform procedure: one operator that turns every enumeration of $B$ into an enumeration of $A$. A weaker, non-uniform requirement is that every enumeration of $B$ computes some enumeration of $A$, possibly by a procedure that depends on the enumeration. Selman's theorem says that the two requirements are equivalent. It has a structural consequence that organizes the whole theory: an enumeration degree is determined by the total degrees above it. The proof is a finite extension argument, in the style of the Kleene–Post theorem, in which the conditions are finite pieces of an enumeration of $B$.

## The theorem

An **enumeration** of a non-empty set $B$ is a total function $f : \nat \to \nat$ with range $B$. A set is c.e. in $f$ if it is c.e. in the graph of $f$. For every enumeration $f$ of $B$, the set $B$ is c.e. in $f$; conversely, if $B$ is c.e. in $X$ and non-empty, then $X$ computes an enumeration of $B$. So "$B$ is c.e. in $X$" means "$X$ computes an enumeration of $B$".

:::theorem[Selman]{#thm-selman}
For all sets $A$ and $B$, the following are equivalent.
1. $A \leq_e B$.
2. For every set $X$, if $B$ is c.e. in $X$, then $A$ is c.e. in $X$.
:::

The first statement is uniform: one operator works for all $X$. The second is not: the procedure enumerating $A$ from $X$ may depend on $X$. By :ref{#prop-ce-in-e}, "$B$ is c.e. in $X$" means $B \leq_e X \oplus \overline X$, so the theorem has a degree-theoretic form.

:::corollary{#cor-selman-degrees}
For enumeration degrees $\mathbf a$ and $\mathbf b$, $\mathbf a \leq \mathbf b$ if and only if every total degree above $\mathbf b$ is above $\mathbf a$.
:::

:::proof{of=cor-selman-degrees}
Let $A \in \mathbf a$ and $B \in \mathbf b$. The total degrees above $\mathbf b$ are the degrees of the sets $X \oplus \overline X$ with $B \leq_e X \oplus \overline X$, that is, with $B$ c.e. in $X$. So the condition on total degrees is statement 2 of :ref{#thm-selman}.
:::

**Intuition.** Assume $A \not\leq_e B$. We build an enumeration $f$ of $B$, by finite pieces, such that $A$ is not c.e. in $f$: for each $e$, the $e$-th oracle machine must fail to enumerate $A$ from $f$. At the step for $e$, with a finite piece $\sigma$ built so far, we look for an extension of $\sigma$, still made of elements of $B$, that makes the machine enumerate some number outside $A$. If there is one, we take it. If there is none, then everything the machine can enumerate from extensions of $\sigma$ lies in $A$, and the set of these numbers is enumeration reducible to $B$: it is described by finite subsets of $B$, the new values of the extensions. Since $A \not\leq_e B$, this set misses some element of $A$, which the machine can then never enumerate.

:::proof{of=thm-selman}
(1 ⇒ 2) If $A = \Gamma(B)$ and $B$ is c.e. in $X$, then $X$ enumerates $B$, hence $A$, by the procedure following :ref{#def-enumeration-reducibility}.

(2 ⇒ 1) Assume $A \not\leq_e B$; we find $X$ such that $B$ is c.e. in $X$ but $A$ is not. If $B$ is empty, $A$ is not c.e. (otherwise $A \leq_e B$), and $X = \emptyset$ works. Let $B$ be non-empty, and $b_0, b_1, \ldots$ a list of its elements, with repetitions if $B$ is finite. Conditions are finite sequences $\sigma$ of elements of $B$; for an oracle machine with index $e$, write $n \in W^\sigma_e$ if the machine halts on $n$ within $|\sigma|$ steps with oracle $\sigma$, querying only values $\sigma(i)$ for $i < |\sigma|$. If $\sigma$ is an initial segment of $f$ and $n \in W^\sigma_e$, then $n \in W^f_e$; conversely every $n \in W^f_e$ belongs to $W^{f \restriction s}_e$ for $s$ large.

We build conditions $\sigma_0 \subseteq \sigma_1 \subseteq \cdots$, starting from the empty sequence, and let $f = \bigcup_s \sigma_s$. At step $2k$, append $b_k$: $\sigma_{2k+1} = \sigma_{2k} b_k$. This makes $f$ total with range $B$. At step $2e + 1$, let $\sigma = \sigma_{2e+1}$.
- If there are a condition $\tau \supseteq \sigma$ and a number $n \notin A$ with $n \in W^\tau_e$, let $\sigma_{2e+2}$ be such a $\tau$. Then $n \in W^f_e \setminus A$.
- Otherwise, let $C$ be the set of $n$ such that $n \in W^{\sigma \rho}_e$ for some finite sequence $\rho$ of elements of $B$. Then $C \subseteq A$, by the case assumption. And $C \leq_e B$: $n \in C$ if and only if there is a finite sequence $\rho$ with $n \in W^{\sigma \rho}_e$ and with the set $D$ of its values contained in $B$; the pairs $\langle n, D \rangle$ obtained in this way, with $\sigma$ fixed, form a c.e. set of axioms. Since $A \not\leq_e B$, $C \neq A$: choose $n \in A \setminus C$, and let $\sigma_{2e+2} = \sigma$. For every enumeration $f \supseteq \sigma$ of $B$, $n \notin W^f_e$: otherwise $n \in W^{f \restriction s}_e$ for some $s \geq |\sigma|$, and $f \restriction s = \sigma \rho$ with $\rho$ a sequence of elements of $B$, so $n \in C$.

In both cases $W^f_e \neq A$. So $A$ is not c.e. in $f$, while $B$ is, as the range of $f$.
:::

The construction is not effective: it asks questions about $A$ and $B$. This is necessary, since $X$ must escape every enumeration of $A$, and the theorem holds for arbitrary sets.

:::quiz[the proof of Selman's theorem]
In the second case of the step for $e$, where is it used that $A \not\leq_e B$?

- [x] To find an element of $A$ outside $C$: the set $C$ is enumeration reducible to $B$ and contained in $A$, so it cannot be all of $A$.
- [ ] To show that $C \subseteq A$.

  This comes from the failure of the first case: no extension makes the machine enumerate a number outside $A$.
- [ ] To show that $f$ is an enumeration of $B$.

  The even steps make $f$ onto $B$; they do not use the hypothesis.

---

Why must the extensions $\tau$ considered in the first case consist of elements of $B$?

- [x] Because $f$ must remain an enumeration of $B$: a value outside $B$ would be in the range of $f$, and $B$ would not be the range.
- [ ] To make the first case decidable.

  The question is not decidable either way; the construction is not effective.
- [ ] Because the machine only reads elements of $B$.

  The machine reads the values of $f$, whatever they are; the constraint comes from the requirement that $f$ enumerate $B$.

---

Why is $C$ enumeration reducible to $B$ rather than merely c.e. in $B$?

- [x] Membership in $C$ is witnessed by a finite sequence whose set of values must be contained in $B$, which is positive information about $B$; no negative information is used.
- [ ] Because $C \subseteq A$.

  The inclusion is a separate fact; reducibility comes from the form of the witnesses.
- [ ] Because $\sigma$ is finite.

  The finiteness of $\sigma$ makes it a fixed parameter of the axioms; the form of the witnesses is what makes them positive.
:::

## Consequences

By :ref{#cor-selman-degrees}, an enumeration degree is determined by the set of total degrees above it: two sets have the same enumeration degree if and only if they are c.e. in the same sets. The set of Turing degrees in which $B$ is c.e. plays the role of a degree spectrum, as in computable structure theory, and the theorem says that it determines the enumeration degree of $B$ (:ref{#ex-selman-spectrum}).

The total degrees are therefore an **automorphism base**: an automorphism of $\mathcal D_e$ that fixes every total degree is the identity, since it preserves the set of total degrees above each degree. Once it is known that the total degrees are first-order definable in $\mathcal D_e$, a theorem of the course on definability, every automorphism of $\mathcal D_e$ restricts to an automorphism of the total degrees, hence of the Turing degrees, and is determined by this restriction.

::::exercise{#ex-selman-spectrum difficulty=1 objective="Translate Selman's theorem into a statement on the sets of degrees in which a set is c.e."}
For a set $B$, let $\mathrm{Sp}(B)$ be the set of Turing degrees $\mathbf x$ such that $B$ is c.e. in some (equivalently, every) set of degree $\mathbf x$. Show that $\mathrm{Sp}(B) = \mathrm{Sp}(A)$ if and only if $A \equiv_e B$, and that $\mathrm{Sp}(B) \subseteq \mathrm{Sp}(A)$ if and only if $A \leq_e B$.

:::solution
"$B$ is c.e. in $X$" depends only on the Turing degree of $X$, so $\mathrm{Sp}(B)$ is well defined. $\mathrm{Sp}(B) \subseteq \mathrm{Sp}(A)$ says that $A$ is c.e. in every $X$ in which $B$ is c.e., which by :ref{#thm-selman} is equivalent to $A \leq_e B$. Applying this in both directions gives the first statement.
:::
::::

## Notes and references

:ref{#thm-selman} is due to Selman (1971); the proof by forcing with finite enumerations is the standard one. Its degree form, :ref{#cor-selman-degrees}, is the starting point of the analysis of the automorphisms of $\mathcal D_e$ through the total degrees (Soskova's survey, Section 4.1).

- A. L. Selman, *Arithmetical reducibilities I*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 17 (1971), 335–350.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Theorem 4.3.

:::::exercises
::::exercise{#ex-selman-uniform difficulty=2 objective="Extract a uniform reduction from a non-uniform hypothesis by the dichotomy of the proof."}
Let $A$ and $B$ be sets such that $A$ is c.e. in every enumeration of $B$. Without quoting :ref{#thm-selman}, explain how its proof produces an operator $\Gamma$ and a finite sequence $\sigma$ of elements of $B$ such that $A = \Gamma(B)$, and why the dependence on $\sigma$ is harmless.

:::solution
Run the construction for the index $e$ of a machine. Since $A$ is c.e. in the enumeration $f$ built, $A = W^f_e$ for some $e$; at step $2e + 1$, the first case cannot have occurred (it puts a number outside $A$ into $W^f_e$), so the second case holds with some $\sigma$, and the set $C$ is enumeration reducible to $B$ and contained in $A$. Moreover $C \supseteq A$: every $n \in A = W^f_e$ is in $W^{f \restriction s}_e$ for large $s$, and $f \restriction s = \sigma \rho$ with $\rho$ in $B$. So $A = C = \Gamma(B)$, where $\Gamma$ has the axioms $\langle n, D \rangle$ for the sequences $\rho$ with values in $D$ and $n \in W^{\sigma \rho}_e$. The parameter $\sigma$ is a finite sequence, fixed once and for all, so it is part of the c.e. set of axioms: the reduction is uniform.
:::
::::

::::exercise{#ex-selman-total difficulty=1 objective="Check that enumeration reducibility agrees with Turing reducibility on total sets."}
Let $A$ and $B$ be total sets. Show that $A \leq_e B$ if and only if $A \leq_T B$.

:::solution
A total set satisfies $A \equiv_e A \oplus \overline A$. If $A \leq_e B$, then $A \leq_e B \oplus \overline B$, so $A$ is c.e. in $B$ by :ref{#prop-ce-in-e}, and, as $\overline A \leq_e A$, so is $\overline A$; hence $A \leq_T B$. Conversely, if $A \leq_T B$, then by :ref{#prop-ce-in-e}, $A \oplus \overline A \leq_e B \oplus \overline B \equiv_e B$. So on total sets the two reducibilities agree, which is the content of :ref{#thm-myhill-embedding}.
:::
::::
:::::
