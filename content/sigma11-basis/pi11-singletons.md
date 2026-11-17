---
title: Π¹₁ singletons
summary: Kleene's O and the iterated hyperjumps are Π¹₁ singletons, unlike Σ¹₁ singletons, which are hyperarithmetic; a Π¹₁ singleton is either hyperarithmetic or hyperarithmetically above O.
duration: 20
prerequisites: [kreisel-basis, descriptive-set-theory/uniformization]
---

A $\Pi^0_1$ class of Cantor space with a single member has a computable member, and a $\Sigma^1_1$ class with a single member has a hyperarithmetic member (:ref{#prop-sigma11-singleton}). For $\Pi^1_1$ classes the situation is different: Kleene's $\mathcal O$ is the only member of a $\Pi^1_1$ class, and so are its hyperjumps $\mathcal O^{\mathcal O}$, $\mathcal O^{\mathcal O^{\mathcal O}}$, and so on. A $\Pi^1_1$ singleton is a set defined by a single $\Pi^1_1$ condition, and such conditions can define sets far beyond the hyperarithmetic ones. There is nevertheless a gap: this lesson shows that a $\Pi^1_1$ singleton is either hyperarithmetic or hyperarithmetically above $\mathcal O$, so no $\Pi^1_1$ singleton lies strictly between.

## Examples

:::proposition{#prop-o-pi11-singleton}
The class $\{ \mathcal O \}$ is $\Pi^1_1$.
:::

:::proof{of=prop-o-pi11-singleton}
Let $R$ be the c.e. relation of :ref{#prop-kleene-o-basic} (2), which agrees with $<_{\mathcal O}$ on $\mathcal O$. Say that a set $X$ is **closed** if $1 \in X$, $2^a \in X$ for every $a \in X$, and $3 \cdot 5^e \in X$ for every $e$ such that $\Phi_e$ is total, $\Phi_e(n) \in X$ and $(\Phi_e(n), \Phi_e(n+1)) \in R$ for every $n$. Closedness is an arithmetic property of $X$. We claim that $\mathcal O$ is the only closed subset of $\mathcal O$; then $\{ \mathcal O \} = \{ X : X \subseteq \mathcal O \text{ and } X \text{ is closed} \}$, and "$X \subseteq \mathcal O$", that is $\forall n\, (n \notin X \vee n \in \mathcal O)$, is $\Pi^1_1$.

$\mathcal O$ is closed, by the definition of notations (:ref{#def-kleene-o}), since $R$ agrees with $<_{\mathcal O}$ on $\mathcal O$. Let $X \subseteq \mathcal O$ be closed. On $X$, the relation $R$ coincides with $<_{\mathcal O}$, so $X$ satisfies the closure conditions that define $\mathcal O$ as the least set satisfying them; by minimality, $\mathcal O \subseteq X$, and $X = \mathcal O$.
:::

:::proposition{#prop-hyperjump-singleton}
If $\{ X \}$ is $\Pi^1_1$, then $\{ \mathcal O^X \}$ is $\Pi^1_1$. Hence $\mathcal O$, $\mathcal O^{\mathcal O}$, $\mathcal O^{\mathcal O^{\mathcal O}}, \dots$ are $\Pi^1_1$ singletons.
:::

:::proof{of=prop-hyperjump-singleton}
By :ref{#prop-hyperjump} (1), with a reduction that is uniform in the oracle, there is a computable function $g$ such that $n \in Y$ if and only if $g(n) \in \mathcal O^Y$, for every set $Y$. For a set $Z$, let $\Psi(Z) = \{ n : g(n) \in Z \}$; it is computable from $Z$, and $\Psi(\mathcal O^Y) = Y$. Let $\mathcal P$ be a $\Pi^1_1$ class with $\mathcal P = \{ X \}$. Then
$$
\{ \mathcal O^X \} = \{ Z : \Psi(Z) \in \mathcal P,\ Z \subseteq \mathcal O^{\Psi(Z)},\ Z \text{ is closed relative to } \Psi(Z) \},
$$
where closedness relative to $Y$ is defined as in the proof of :ref{#prop-o-pi11-singleton}, with $Y$-computable fundamental sequences. The three conditions are $\Pi^1_1$: the first because $\Psi$ is computable, the second as in that proof, relativized, and the third because it is arithmetic. If $Z$ satisfies them, then $\Psi(Z) = X$, and $Z = \mathcal O^X$ by the argument of :ref{#prop-o-pi11-singleton} relativized to $X$. Conversely, $\mathcal O^X$ satisfies them, since $\Psi(\mathcal O^X) = X$. The last statement follows by induction, from :ref{#prop-o-pi11-singleton}.
:::

So $\Pi^1_1$ singletons can be far from hyperarithmetic: $\mathcal O^{\mathcal O}$ is not even hyperarithmetic in $\mathcal O$. The hyperjump can be iterated along well-orderings computed by the previous hyperjumps, which gives a transfinite **hierarchy of hyperjumps** made of $\Pi^1_1$ singletons (Monin and Patey, Definition of the hierarchy of hyperjumps).

## The gap theorem

:::lemma{#lem-morphism-rank}
If there is a morphism from a tree $S$ to a well-founded tree $T$, then $S$ is well-founded and $\mathrm{rk}(S) \leq \mathrm{rk}(T)$.
:::

:::proof{of=lem-morphism-rank}
Let $f$ be a morphism. A path of $S$ would be mapped to a path of $T$, so $S$ is well-founded. We show $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(f(\sigma))$ for every $\sigma \in S$, by induction on $\mathrm{rk}_S(\sigma)$, with the notation of :ref{#lem-tree-morphism}. For $\sigma n \in S$, $f(\sigma n)$ is an immediate successor of $f(\sigma)$ in $T$, and by induction $\mathrm{rk}_S(\sigma n) \leq \mathrm{rk}_T(f(\sigma n))$, so $\mathrm{rk}_S(\sigma n) + 1 \leq \mathrm{rk}_T(f(\sigma))$. Taking the supremum over $n$ gives the claim. With $\sigma = \varepsilon$, $\mathrm{rk}(S) \leq \mathrm{rk}(T)$.
:::

:::theorem{#thm-pi11-singleton-gap}
Let $X$ be a $\Pi^1_1$ singleton. Then either $X$ is hyperarithmetic, or $\mathcal O \leq_h X$.
:::

The idea is the boundedness argument once more. A $\Pi^1_1$ class is the class of sets $Y$ for which a tree $T^Y$, computable in $Y$, is well-founded. If $X$ does not collapse $\omega_1^{\mathrm{CK}}$, the rank of $T^X$ is a computable ordinal $\alpha$, and the condition "$T^Y$ is well-founded of rank at most $\alpha$" is $\Sigma^1_1$: it says that $T^Y$ maps by a morphism into a fixed computable tree of rank $\alpha$. This $\Sigma^1_1$ condition still defines $\{ X \}$, so $X$ is a $\Sigma^1_1$ singleton.

:::proof{of=thm-pi11-singleton-gap}
Let $\mathcal P = \{ X \}$ be $\Pi^1_1$. By the normal form theorem relativized, uniformly in the oracle, there is a Turing functional $\Gamma$ such that for every $Y$, $\Gamma^Y$ is (the characteristic function of) a tree $T^Y$, and $Y \in \mathcal P$ if and only if $T^Y$ is well-founded.

Suppose that $\mathcal O \not\leq_h X$. By :ref{#thm-spector-collapse}, $\omega_1^X = \omega_1^{\mathrm{CK}}$. The tree $T^X$ is $X$-computable and well-founded, so its rank $\alpha$ is $X$-computable, by :ref{#prop-rank-computable} relativized, hence computable. Let $R$ be a computable well-founded tree of rank $\alpha$ (:ref{#prop-rank-computable}), and
$$
\mathcal Q = \{ Y : \text{there is a morphism from } T^Y \text{ to } R \}.
$$
It is $\Sigma^1_1$, since "$f$ is a morphism from $T^Y$ to $R$" is arithmetic in $f$ and $Y$. By :ref{#lem-tree-morphism}, $X \in \mathcal Q$. By :ref{#lem-morphism-rank}, every $Y \in \mathcal Q$ has $T^Y$ well-founded, so $Y \in \mathcal P$ and $Y = X$. So $\mathcal Q = \{ X \}$ is a $\Sigma^1_1$ singleton, and $X$ is hyperarithmetic by :ref{#prop-sigma11-singleton}.
:::

:::quiz[Π¹₁ singletons]
In the proof of :ref{#thm-pi11-singleton-gap}, where is the hypothesis $\mathcal O \not\leq_h X$ used?

- [x] To get $\omega_1^X = \omega_1^{\mathrm{CK}}$, so that the rank of the $X$-computable tree $T^X$ is a computable ordinal and can be compared, through morphisms, with a fixed computable tree $R$.
- [ ] To show that $\mathcal Q$ is $\Sigma^1_1$.

  The class $\mathcal Q$ is $\Sigma^1_1$ for every computable tree $R$.
- [ ] To show that $X \in \mathcal P$.

  This holds by definition of $\mathcal P$.

---

Why is $\mathcal Q$ included in $\mathcal P$?

- [x] A morphism into the well-founded tree $R$ forces $T^Y$ to be well-founded, by :ref{#lem-morphism-rank}, and then $Y \in \mathcal P$ by the normal form.
- [ ] Because $\mathcal Q$ is $\Sigma^1_1$ and $\mathcal P$ is $\Pi^1_1$.

  Complexity says nothing about inclusion.
- [ ] Because $X \in \mathcal Q$.

  This shows that $\mathcal Q$ is non-empty, not that it is included in $\mathcal P$.
:::

So the $\Pi^1_1$ singletons skip the hyperdegrees strictly between $\mathbf 0$ and the hyperdegree of $\mathcal O$: a set $X$ with $0 <_h X <_h \mathcal O$, such as the sets of :ref{#ex-hyperlow-nonhyp}, is never a $\Pi^1_1$ singleton. Further results, admitted here: every non-empty $\Pi^1_1$ class contains a $\Pi^1_1$ singleton, uniformly, which gives the Kondo–Addison uniformization theorem for $\Pi^1_1$ relations between sets (Monin–Patey, chapter "$\Sigma^1_1$ and $\Pi^1_1$ classes"); this extends Kreisel's uniformization for relations on numbers (:ref{#thm-kreisel-uniformization}).

::::exercise[Hyperlow sets are not Π¹₁ singletons]{#ex-hyperlow-not-singleton difficulty=1 objective="Apply the gap theorem to hyperlow sets."}
Show that a non-hyperarithmetic set $X$ with $\mathcal O^X \leq_T \mathcal O$ is not a $\Pi^1_1$ singleton.

:::solution
By the proof of :ref{#thm-gandy-basis}, $\mathcal O^X \leq_T \mathcal O$ implies $\mathcal O \not\leq_h X$. If $X$ were a $\Pi^1_1$ singleton, :ref{#thm-pi11-singleton-gap} would make it hyperarithmetic, contrary to the hypothesis.
:::
::::

## Notes and references

That $\mathcal O$ and its hyperjumps are $\Pi^1_1$ singletons, and the gap theorem, go back to Spector and Gandy; the presentation of the examples follows Monin and Patey (section "$\Pi^1_1$ singletons"), and the proof of the gap theorem uses the morphisms of :ref{#lem-tree-morphism}. Guaspari (1974) proved that the class of sets computable in an iterate of the jump along an ordinal they compute is a basis for $\Pi^1_1$ classes; the uniformization theorem for $\Pi^1_1$ relations is due to Kondo (1939) and Addison (1958).

- C. Spector, *Hyperarithmetical quantifiers*, Fundamenta Mathematicae 48 (1959), 313–320.
- D. Guaspari, *A note on the Kondo–Addison theorem*, Journal of Symbolic Logic 39 (1974), 567–570.
- B. Monin and L. Patey, *Computability theory*, chapter "$\Sigma^1_1$ and $\Pi^1_1$ classes", sections "Study of a very special $\Pi^1_1$ class" and "$\Pi^1_1$ singletons".
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990, Part A.

:::::exercises
::::exercise{#ex-pi11-singleton-omega1 difficulty=1 objective="Combine the gap theorem with Spector's theorem."}
Let $X$ be a non-hyperarithmetic $\Pi^1_1$ singleton. Show that $\omega_1^X > \omega_1^{\mathrm{CK}}$.

:::solution
By :ref{#thm-pi11-singleton-gap}, $\mathcal O \leq_h X$, so $\omega_1^X > \omega_1^{\mathrm{CK}}$ by :ref{#thm-spector-collapse}.
:::
::::

::::exercise{#ex-singleton-arithmetic-in-o difficulty=2 objective="Show that Π¹₁ singletons are closed under Turing equivalence, and find a Π¹₁ singleton among the sets arithmetic in O."}
Show that every set Turing equivalent to a $\Pi^1_1$ singleton is a $\Pi^1_1$ singleton. Deduce that $\mathcal O'$ is a $\Pi^1_1$ singleton.

:::solution
Let $\{ X \}$ be $\Pi^1_1$ and $Y \equiv_T X$, with $Y = \Phi^X$ and $X = \Psi^Y$ for Turing functionals $\Phi$ and $\Psi$. Then
$$
\{ Y \} = \{ Z : \Psi^Z \text{ is total},\ \Psi^Z \in \{ X \},\ \Phi^{\Psi^Z} \text{ is total and equal to } Z \}.
$$
Totality and the last equality are arithmetic conditions on $Z$, and "$\Psi^Z \in \{ X \}$" is $\Pi^1_1$, obtained by substituting the $Z$-computable set $\Psi^Z$ in the $\Pi^1_1$ definition of $\{ X \}$. If $Z$ satisfies the conditions, then $\Psi^Z = X$ and $Z = \Phi^X = Y$; and $Y$ satisfies them. So $\{ Y \}$ is $\Pi^1_1$.

The set $\mathcal O'$ is not Turing equivalent to $\mathcal O$, so this does not apply directly. But $\{ \mathcal O' \} = \{ Z : \Psi(Z) \in \{ \mathcal O \} \text{ and } Z = \Psi(Z)' \}$, where $\Psi(Z) = \{ n : g(n) \in Z \}$ for a computable $g$ with $n \in V \iff g(n) \in V'$ for every set $V$. The first condition is $\Pi^1_1$ by :ref{#prop-o-pi11-singleton}, the second is arithmetic, and the only member is $\mathcal O'$, since $\Psi(\mathcal O') = \mathcal O$. The same argument shows that every set arithmetic in a $\Pi^1_1$ singleton $X$ and computing it is a $\Pi^1_1$ singleton.
:::
::::
:::::
