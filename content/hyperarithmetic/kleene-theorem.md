---
title: The hyperarithmetic sets are the Δ¹₁ sets
summary: The H-sets are uniformly Δ¹₁ along O; quantification over hyperarithmetic sets is Π¹₁; Kleene's theorem that a set is hyperarithmetic if and only if it is Δ¹₁, through Spector's boundedness theorem.
duration: 35
prerequisites: [h-sets, computable-ordinals/trees-and-pi11]
---

The computable sets are the sets that are both $\Sigma^0_1$ and $\Pi^0_1$. One level up in the analytic hierarchy, Kleene proved the analogous statement for the $\Delta^1_1$ sets: they are exactly the hyperarithmetic sets, built from below by iterating the jump along computable ordinals. The analogy between $\Pi^1_1$ and c.e. sets, and between $\Delta^1_1$ and computable sets, runs through the whole theory, with $\omega_1^{\mathrm{CK}}$ playing the role of $\omega$. This lesson proves Kleene's theorem; one step, the computation of the ranks of trees by H-sets, is admitted.

## The H-sets are Δ¹₁

By :ref{#prop-kleene-o-basic} (2), there is a c.e. relation $R$ such that, for $a \in \mathcal O$, $R(u, a)$ holds exactly for $u <_{\mathcal O} a$.

:::definition{#def-h-sequence}
For $a \in \nat$, a set $Y$ is an **H-sequence along** $a$ if its columns $Y^{[u]}$ are empty unless $u = a$ or $R(u, a)$, and for every such $u$:

1. if $u = 1$, then $Y^{[u]} = \emptyset$;
2. if $u = 2^c$, then $Y^{[u]} = (Y^{[c]})'$;
3. if $u = 3 \cdot 5^e$, then $Y^{[u]} = \{ \langle w, v \rangle : R(w, u) \text{ and } v \in Y^{[w]} \}$.
:::

Being an H-sequence along $a$ is an arithmetic property of $(Y, a)$.

:::lemma{#lem-h-sequence-unique}
For $a \in \mathcal O$, there is exactly one H-sequence along $a$, and its column $a$ is $H_a$.
:::

:::proof{of=lem-h-sequence-unique}
The set whose column $u$ is $H_u$ for $u \leq_{\mathcal O} a$ and empty otherwise is an H-sequence, by :ref{#def-h-sets}. If $Y$ is an H-sequence along $a$, then $Y^{[u]} = H_u$ for every $u \leq_{\mathcal O} a$, by induction along the well-founded relation $<_{\mathcal O}$: each clause determines $Y^{[u]}$ from the columns below $u$, in the same way as the definition of $H_u$.
:::

:::proposition{#prop-h-delta11}
The relations "$a \in \mathcal O$ and $v \in H_a$" and "$a \in \mathcal O$ and $v \notin H_a$" are $\Pi^1_1$. Consequently, every $H_a$ is $\Delta^1_1$, and every hyperarithmetic set is $\Delta^1_1$.
:::

:::proof{of=prop-h-delta11}
By :ref{#lem-h-sequence-unique}, for $a \in \mathcal O$,
$$
v \in H_a \iff \forall Y\, (Y \text{ is an H-sequence along } a \rightarrow v \in Y^{[a]}) \iff \exists Y\, (Y \text{ is an H-sequence along } a \wedge v \in Y^{[a]}).
$$
The relation $a \in \mathcal O$ is $\Pi^1_1$, and the conjunction with the first form is $\Pi^1_1$; the same holds with $v \notin Y^{[a]}$. For a fixed $a \in \mathcal O$, the two forms show that $H_a$ is $\Pi^1_1$ and $\Sigma^1_1$.

Finally, let $X = \Phi^A_e$ with $A$ a $\Delta^1_1$ set. Then $n \in X$ if and only if there is a string $\sigma$ with $\Phi^\sigma_e(n)\converge = 1$ and $\sigma(i) = A(i)$ for every $i < |\sigma|$, and $n \notin X$ if and only if the same holds with $0$ in place of $1$. The condition $\sigma(i) = A(i)$ for all $i < |\sigma|$ is a bounded conjunction of statements $i \in A$ and $i \notin A$, each of them $\Sigma^1_1$ and $\Pi^1_1$. The classes $\Sigma^1_1$ and $\Pi^1_1$ are closed under conjunction, disjunction and number quantifiers: a universal number quantifier commutes with a universal set quantifier, and an existential number quantifier is absorbed as in the third case of the proof of :ref{#thm-pi11-normal-form}. So $X$ and its complement are $\Sigma^1_1$, that is, $X$ is $\Delta^1_1$.
:::

The uniform version gives a useful closure property: a quantifier over hyperarithmetic sets does not increase the complexity of a $\Pi^1_1$ formula.

:::corollary{#cor-hyp-quantifier}
For every arithmetic formula $\psi(n, X)$, the set $\{ n : \exists X \in \mathrm{HYP}\ \psi(n, X) \}$ is $\Pi^1_1$.
:::

:::proof{of=cor-hyp-quantifier}
A hyperarithmetic set is $\Phi^{H_a}_e$ for some $a \in \mathcal O$ and some $e$ such that $\Phi^{H_a}_e$ is total and $\{0, 1\}$-valued. So $\exists X \in \mathrm{HYP}\ \psi(n, X)$ holds if and only if there are $a$ and $e$ with $a \in \mathcal O$ and
$$
\forall Y\, \big(Y \text{ is an H-sequence along } a \rightarrow (\Phi^{Y^{[a]}}_e \text{ is total and } \{0,1\}\text{-valued} \wedge \psi(n, \Phi^{Y^{[a]}}_e))\big).
$$
The bracket is arithmetic in $Y$, so the whole formula is $\Pi^1_1$: an existential number quantifier in front of a $\Pi^1_1$ formula gives a $\Pi^1_1$ formula, by the closure properties recalled in the proof of :ref{#prop-h-delta11}.
:::

:::quiz[H-sequences]
In :ref{#prop-h-delta11}, why is the hypothesis $a \in \mathcal O$ needed to obtain both a $\Sigma^1_1$ and a $\Pi^1_1$ definition of $H_a$?

- [x] Because existence and uniqueness of the H-sequence are proved by induction along $<_{\mathcal O}$, which is well-founded below $a$ only when $a \in \mathcal O$; for other $a$, there may be no H-sequence or several.
- [ ] Because $R$ is not c.e. for $a \notin \mathcal O$.

  $R$ is c.e. as a relation; its meaning as $<_{\mathcal O}$ is guaranteed only for notations.
- [ ] Because $H_a$ is computable for $a \notin \mathcal O$.

  $H_a$ is only defined for notations.
:::

## Kleene's theorem

The converse inclusion requires a computation of well-foundedness by H-sets, up to a fixed rank.

:::lemma{#lem-wf-rank-hyp}
For every computable ordinal $\alpha$, the set $\mathrm{WF}_{< \alpha}$ of indices of computable trees that are well-founded of rank less than $\alpha$ is hyperarithmetic.
:::

The proof is by effective transfinite recursion on a notation for $\alpha$. A tree $T$ has rank at most $\beta + 1$ if and only if $T_{\langle n \rangle}$ has rank at most $\beta$ for every $n$ with $\langle n \rangle \in T$, a $\Pi^0_1$ condition relative to the set of indices of trees of rank at most $\beta$; for a limit $\lambda$ with fundamental sequence $(\lambda_k)$, it has rank at most $\lambda$ if and only if for every $n$ there is $k$ such that $T_{\langle n \rangle}$ has rank at most $\lambda_k$, a $\Pi^0_2$ condition relative to the sets for the ranks $\lambda_k$. Each step thus costs at most two jumps, and the set of indices of trees of rank at most $|a|$ is computable in $H_b$ for some $b \in \mathcal O$ with $|b| \leq |a| \cdot 2 + 2$, by reductions computed from $a$. Then $\mathrm{WF}_{<\alpha}$ is the set for the rank $\beta$ if $\alpha = \beta + 1$, and the union of the sets for the ranks $\alpha_k$ if $\alpha$ is a limit with fundamental sequence $(\alpha_k)$. Making the uniformity precise requires effective transfinite recursion, and we admit the details; see Sacks, *Higher Recursion Theory*, Section II.1.

:::theorem[Kleene]{#thm-kleene-delta11}
A set of numbers is $\Delta^1_1$ if and only if it is hyperarithmetic.
:::

:::proof{of=thm-kleene-delta11}
Hyperarithmetic sets are $\Delta^1_1$ by :ref{#prop-h-delta11}. Conversely, let $A$ be $\Delta^1_1$. By the normal form theorem (:ref{#thm-pi11-normal-form}), there is a computable function $n \mapsto t(n)$ such that $n \in A$ if and only if $t(n)$ is an index of a well-founded computable tree. The set $S = \{ t(n) : n \in A \}$ is $\Sigma^1_1$, since $m \in S$ if and only if $\exists n\, (t(n) = m \wedge n \in A)$ with $A$ a $\Sigma^1_1$ set, and it consists of indices of well-founded trees. By the boundedness theorem in the form of the first exercise of :ref{to="computable-ordinals/trees-and-pi11"} (stated there for c.e. indices of trees, which are computed from the indices $t(n)$ by a computable function), the ranks of the trees in $S$ have a supremum $\gamma < \omega_1^{\mathrm{CK}}$. Let $\alpha = \gamma + 1$, a computable ordinal greater than all these ranks. Then $n \in A$ if and only if $t(n) \in \mathrm{WF}_{< \alpha}$: if $n \in A$, the rank of $t(n)$ is less than $\alpha$; if $n \notin A$, the tree $t(n)$ is not well-founded. So $A$ is computable in $\mathrm{WF}_{<\alpha}$, which is hyperarithmetic by :ref{#lem-wf-rank-hyp}.
:::

The proof is a template for many results: a $\Delta^1_1$ property is $\Pi^1_1$ with a $\Sigma^1_1$ bound on the ordinals involved, and below a computable ordinal, everything is hyperarithmetic. The theorem relativizes: the $\Delta^1_1(X)$ sets are the sets computable in $H^X_a$ for some $a \in \mathcal O^X$, the H-sets relative to $X$.

:::quiz[Kleene's theorem]
In the proof of :ref{#thm-kleene-delta11}, where is the hypothesis that $A$ is $\Sigma^1_1$ used?

- [x] To make $\{ t(n) : n \in A \}$ a $\Sigma^1_1$ set of well-founded trees, so that the boundedness theorem bounds their ranks below $\omega_1^{\mathrm{CK}}$.
- [ ] To obtain the normal form $n \in A \iff t(n) \in \mathrm{WF}$.

  The normal form uses that $A$ is $\Pi^1_1$.
- [ ] To show that $\mathrm{WF}_{<\alpha}$ is hyperarithmetic.

  This holds for every computable $\alpha$, independently of $A$.

---

Why does the proof fail for $\mathcal O$, which is $\Pi^1_1$?

- [x] Because $\mathcal O$ is not $\Sigma^1_1$: the trees associated with notations have ranks unbounded below $\omega_1^{\mathrm{CK}}$, and no single $\mathrm{WF}_{<\alpha}$ suffices.
- [ ] Because the normal form does not apply to $\mathcal O$.

  It applies to every $\Pi^1_1$ set.
- [ ] Because the trees $t(n)$, $n \in \mathcal O$, have ranks that are not computable ordinals.

  Each of them is a computable well-founded tree, so its rank is a computable ordinal; what fails is a common bound below $\omega_1^{\mathrm{CK}}$.
:::

## Exercises

::::exercise{difficulty=1}
Show that if $S \subseteq \mathcal O$ is $\Sigma^1_1$, then $\sup \{ |a| : a \in S \} < \omega_1^{\mathrm{CK}}$. Deduce that $\mathcal O$ is not $\Sigma^1_1$.

:::solution
By :ref{#prop-kleene-o-basic} (2), the relation $\{ (b, c) : R(b, a) \wedge R(c, a) \wedge (b = c \vee R(b, c)) \}$ is c.e., uniformly in $a$, and for $a \in \mathcal O$ it is the order $\leq_{\mathcal O}$ on the notations below $a$, a well-ordering of type $|a|$. Placing a copy of $\omega$ before it gives a c.e. well-ordering of type $\omega + |a|$ with an infinite field, and the proof of :ref{#prop-computable-ordinals-basic} (3) turns it into a computable well-ordering of $\nat$ of the same type. This gives a computable function $g$, total on all numbers, such that $g(a) \in \mathrm{WO}$ and $|g(a)| = \omega + |a|$ for $a \in \mathcal O$. The set $g(S) = \{ m : \exists a\, (g(a) = m \wedge a \in S) \}$ is a $\Sigma^1_1$ subset of $\mathrm{WO}$, so by :ref{#thm-boundedness} there is $\gamma < \omega_1^{\mathrm{CK}}$ with $\omega + |a| \leq \gamma$, hence $|a| \leq \gamma$, for every $a \in S$. Since $\mathcal O$ contains notations for all computable ordinals, it cannot be $\Sigma^1_1$.
:::
::::

::::exercise{difficulty=2}
Show that no hyperarithmetic set computes all hyperarithmetic sets, and that the relation "$X$ is hyperarithmetic" is $\Pi^1_1$ in $X$.

:::solution
If $A \leq_T H_a$ computed every hyperarithmetic set, it would compute $H_{2^a} = H_a'$, which is impossible. For the second statement, $X$ is hyperarithmetic if and only if there are $a$ and $e$ with $a \in \mathcal O$ and $\forall Y\, (Y \text{ is an H-sequence along } a \rightarrow X = \Phi^{Y^{[a]}}_e)$, by :ref{#lem-h-sequence-unique}; the condition $X = \Phi^{Y^{[a]}}_e$ is arithmetic in $X$ and $Y$. So the relation is $\Pi^1_1$.
:::
::::

## Notes and references

Kleene (1955) proved that the $\Delta^1_1$ sets are exactly the hyperarithmetic sets; the classical counterpart in descriptive set theory is Suslin's theorem that the Borel sets are the sets that are both analytic and co-analytic, which is why the result is often called the **Suslin–Kleene theorem**. Spector's boundedness theorem gives the proof presented here.

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009.
