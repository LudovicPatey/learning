---
title: The hyperarithmetic sets are the Δ¹₁ sets
summary: The H-sets are uniformly Δ¹₁ along O; quantification over hyperarithmetic sets is Π¹₁; H-sets compute the sets of trees of bounded rank; Kleene's theorem that a set is hyperarithmetic if and only if it is Δ¹₁, through Spector's boundedness theorem.
duration: 50
prerequisites: [spector-uniqueness, computable-ordinals/markwald, computable-ordinals/trees-and-pi11, computable-ordinals/boundedness]
---

The computable sets are the sets that are both $\Sigma^0_1$ and $\Pi^0_1$. One level up in the analytic hierarchy, Kleene proved the analogous statement for the $\Delta^1_1$ sets: they are exactly the hyperarithmetic sets, built from below by iterating the jump along computable ordinals. The analogy between $\Pi^1_1$ and c.e. sets, and between $\Delta^1_1$ and computable sets, runs through the whole theory, with $\omega_1^{\mathrm{CK}}$ playing the role of $\omega$. The two inclusions have different flavors. That hyperarithmetic sets are $\Delta^1_1$ is a matter of definability: $H_a$ is the unique set satisfying an arithmetic description along $a$, and "the unique $Y$ such that" can be expressed both with $\exists Y$ and with $\forall Y$. The converse needs an ordinal bound: a $\Pi^1_1$ set is a set of indices of well-founded trees, and when it is also $\Sigma^1_1$, Spector's boundedness theorem bounds the ranks of these trees below $\omega_1^{\mathrm{CK}}$; below a fixed computable ordinal, well-foundedness is decided by an H-set.

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

The converse inclusion requires a computation of well-foundedness by H-sets, up to a fixed rank. For uniformity, it is convenient to work with c.e. trees. For a number $i$, let $T^i$ be the set of prefixes of the elements of $W_i$, viewed as a set of sequences: it is a c.e. tree, uniformly in $i$, and every c.e. tree is $T^i$ for some $i$. There is a total computable function $s$ such that $T^{s(i, n)} = (T^i)_{\langle n \rangle} = \{ \tau : \langle n \rangle \tau \in T^i \}$, and the relation $\langle n \rangle \in T^i$ is c.e. For $x \in \mathcal O$, let
$$
\mathrm{Rk}_{<x} = \{ i : T^i \text{ is well-founded and } \mathrm{rk}(T^i) < |x| \}.
$$

The computation follows the definition of the rank (:ref{#def-tree-rank}), illustrated in :ref{#fig-tree-ranks}: a tree has rank at most $\beta$ if and only if each of its subtrees $T_{\langle n \rangle}$ has rank less than $\beta$. One quantifier over $n$ is added at each successor step, and one existential quantifier over the fundamental sequence at each limit step; the H-sets absorb both.

:::figure[A well-founded tree; each node $\sigma$ is labeled with the rank of the subtree $T_\sigma$ above it. The tree has rank $4$, the label of the root $\varepsilon$, and it has rank less than $\beta + 1$ exactly when each subtree $T_{\langle n \rangle}$ has rank less than $\beta$.]{#fig-tree-ranks}
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="A finite well-founded tree; each node is labeled with its rank, the supremum of the ranks of its children plus one"><line x1="300" y1="30" x2="120" y2="90" class="ink-stroke" stroke-width="1.2"/><line x1="300" y1="30" x2="300" y2="90" class="ink-stroke" stroke-width="1.2"/><line x1="300" y1="30" x2="480" y2="90" class="ink-stroke" stroke-width="1.2"/><line x1="300" y1="90" x2="250" y2="150" class="ink-stroke" stroke-width="1.2"/><line x1="300" y1="90" x2="350" y2="150" class="ink-stroke" stroke-width="1.2"/><line x1="480" y1="90" x2="480" y2="150" class="ink-stroke" stroke-width="1.2"/><line x1="350" y1="150" x2="350" y2="210" class="ink-stroke" stroke-width="1.2"/><line x1="480" y1="150" x2="430" y2="210" class="ink-stroke" stroke-width="1.2"/><line x1="480" y1="150" x2="530" y2="210" class="ink-stroke" stroke-width="1.2"/><line x1="530" y1="210" x2="530" y2="270" class="ink-stroke" stroke-width="1.2"/><circle cx="300" cy="30" r="4.5" class="accent-fill"/><text x="310" y="24" class="mrm" font-size="13">4</text><circle cx="120" cy="90" r="4.5" class="ink-fill"/><text x="130" y="84" class="mrm" font-size="13">0</text><circle cx="300" cy="90" r="4.5" class="ink-fill"/><text x="310" y="84" class="mrm" font-size="13">2</text><circle cx="480" cy="90" r="4.5" class="ink-fill"/><text x="490" y="84" class="mrm" font-size="13">3</text><circle cx="250" cy="150" r="4.5" class="ink-fill"/><text x="260" y="144" class="mrm" font-size="13">0</text><circle cx="350" cy="150" r="4.5" class="ink-fill"/><text x="360" y="144" class="mrm" font-size="13">1</text><circle cx="480" cy="150" r="4.5" class="ink-fill"/><text x="490" y="144" class="mrm" font-size="13">2</text><circle cx="350" cy="210" r="4.5" class="ink-fill"/><text x="360" y="204" class="mrm" font-size="13">0</text><circle cx="430" cy="210" r="4.5" class="ink-fill"/><text x="440" y="204" class="mrm" font-size="13">0</text><circle cx="530" cy="210" r="4.5" class="ink-fill"/><text x="540" y="204" class="mrm" font-size="13">1</text><circle cx="530" cy="270" r="4.5" class="ink-fill"/><text x="540" y="264" class="mrm" font-size="13">0</text><text x="288" y="34" text-anchor="end" class="mrm" font-size="13">ε</text><text x="40" y="270" class="label">leaves have rank 0;</text><text x="40" y="286" class="label">a node has rank sup(rank of child + 1)</text></svg>
:::

:::lemma[Spector]{#lem-rank-sets}
There is an oracle procedure $\Xi$ such that for every $x \in \mathcal O$ and every $i$, the computation $\Xi^{H_{2^x}}(x, i)$ halts, with output $1$ if $i \in \mathrm{Rk}_{<x}$ and $0$ otherwise. In other words, $\mathrm{Rk}_{<x} \leq_T H_{2^x}$, uniformly in $x$.
:::

:::proof{of=lem-rank-sets}
By effective transfinite recursion (:ref{to="h-sets"}), by cases on $x$, the oracle $X$ being $H_{2^x} = H_x'$; as in the proof of :ref{#lem-notations-below}, the sets $H_x$, and $H_{2^b}$ when $x = 2^b$, are computed from $X$ by :ref{#prop-h-sets-uniform}.

1. $x = 1$. Output $0$: no tree has rank less than $0$.
2. $x = 2^b$ with $b \geq 1$. A tree $T$ is well-founded of rank less than $|b| + 1$ if and only if, for every $n$ with $\langle n \rangle \in T$, the tree $T_{\langle n \rangle}$ is well-founded of rank less than $|b|$: if $T$ is well-founded, then $\mathrm{rk}(T) \leq |b|$ if and only if $\mathrm{rk}(T_{\langle n \rangle}) + 1 \leq |b|$ for every such $n$; and $T$ is well-founded if and only if all the trees $T_{\langle n \rangle}$ are. So
   $$
   i \in \mathrm{Rk}_{<x} \iff \forall n\ \big(\langle n \rangle \notin T^i \vee s(i, n) \in \mathrm{Rk}_{<b}\big).
   $$
   The relation $\langle n \rangle \notin T^i$ is decided by $\emptyset'$, and $s(i, n) \in \mathrm{Rk}_{<b}$ by $\Xi^{H_{2^b}}(b, s(i, n))$; both oracles are computable in $H_{2^b}$ (:ref{#prop-h-sets-uniform}, with $2^b \neq 1$). The condition is $\Pi^0_1(H_{2^b})$, and it is answered by $H_{2^b}' = X$.
3. $x = 3 \cdot 5^f$. Since $|x| = \sup_m |x_m|$, a tree has rank less than $|x|$ if and only if it has rank less than $|x_m|$ for some $m$. So $i \in \mathrm{Rk}_{<x}$ if and only if $\exists m\ \Xi^{H_{2^{x_m}}}(x_m, i) = 1$, where $H_{2^{x_m}}$ is a column of $H_x$. This is a $\Sigma^0_1(H_x)$ condition, answered by $H_x' = X$.

By induction on $x \in \mathcal O$, the computation halts with the correct output, the recursive calls being made at $b$ and at the $x_m$, which are below $x$.
:::

:::lemma{#lem-wf-rank-hyp}
For every computable ordinal $\alpha$, the set $\mathrm{WF}_{< \alpha}$ of indices of computable trees that are well-founded of rank less than $\alpha$ is hyperarithmetic.
:::

:::proof{of=lem-wf-rank-hyp}
Let $x$ be a notation of $\alpha$ (:ref{#cor-constructive-computable}), and let $g$ be a total computable function with $W_{g(i)} = \{ \sigma : \Phi_i(\sigma)\converge = 1 \}$. If $i$ is an index of a computable tree, this tree is $T^{g(i)}$. So $\mathrm{WF}_{<\alpha}$ is the set of $i$ that are indices of computable trees, a $\Pi^0_2$ condition decided by $\emptyset''$, and such that $g(i) \in \mathrm{Rk}_{<x}$, decided by $H_{2^x}$ (:ref{#lem-rank-sets}). Both oracles are hyperarithmetic, and so is their join (:ref{#prop-hyp-ideal}).
:::

:::quiz[ranks and H-sets]
In case 2 of the proof of :ref{#lem-rank-sets}, why is the condition answered by $H_{2^b}'$ rather than by $H_{2^b}$?

- [x] Because it contains an unbounded universal quantifier over the immediate successors $\langle n \rangle$ of the root: a tree on $\nat$ may be infinitely branching, and checking all its subtrees is a $\Pi^0_1$ question relative to $H_{2^b}$.
- [ ] Because the relation $\langle n \rangle \in T^i$ is only c.e.

  This relation is decided by $\emptyset' \leq_T H_{2^b}$; the jump is needed for the quantifier over $n$.
- [ ] Because the rank of $T^i$ might be a limit ordinal.

  In case 2, the bound $|b| + 1$ is a successor; the trees considered have rank at most $|b|$, whatever its form.
:::

:::theorem[Kleene]{#thm-kleene-delta11}
A set of numbers is $\Delta^1_1$ if and only if it is hyperarithmetic.
:::

:::proof{of=thm-kleene-delta11}
Hyperarithmetic sets are $\Delta^1_1$ by :ref{#prop-h-delta11}. Conversely, let $A$ be $\Delta^1_1$. By the normal form theorem (:ref{#thm-pi11-normal-form}), there is a computable function $n \mapsto t(n)$ such that $n \in A$ if and only if $t(n)$ is an index of a well-founded computable tree. The set $S = \{ t(n) : n \in A \}$ is $\Sigma^1_1$, since $m \in S$ if and only if $\exists n\, (t(n) = m \wedge n \in A)$ with $A$ a $\Sigma^1_1$ set, and it consists of indices of well-founded trees. By the boundedness theorem in the form of :ref{#ex-tree-boundedness} (stated there for c.e. indices of trees, which are computed from the indices $t(n)$ by a computable function), the ranks of the trees in $S$ have a supremum $\gamma < \omega_1^{\mathrm{CK}}$. Let $\alpha = \gamma + 1$, a computable ordinal greater than all these ranks. Then $n \in A$ if and only if $t(n) \in \mathrm{WF}_{< \alpha}$: if $n \in A$, the rank of $t(n)$ is less than $\alpha$; if $n \notin A$, the tree $t(n)$ is not well-founded. So $A$ is computable in $\mathrm{WF}_{<\alpha}$, which is hyperarithmetic by :ref{#lem-wf-rank-hyp}.
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

Kleene (1955) proved that the $\Delta^1_1$ sets are exactly the hyperarithmetic sets; the classical counterpart in descriptive set theory is Suslin's theorem that the Borel sets are the sets that are both analytic and co-analytic, which is why the result is often called the **Suslin–Kleene theorem**. Spector's boundedness theorem gives the proof presented here, and Spector (1955) also proved the computation of ranks by H-sets (:ref{#lem-rank-sets}), which we prove as in Monin and Patey. The H-sequences of :ref{#def-h-sequence} play the role of the formula $H(a, X, Y)$ in Simpson's proof of the theorem in $\mathsf{ACA}_0$ (Theorem VIII.3.19), which also uses the boundedness of $\Sigma^1_1$ sets of well-orderings. The converse of :ref{#cor-hyp-quantifier}, that every $\Pi^1_1$ set has this form, is the theorem of Spector and Gandy on hyperarithmetic quantifiers (Simpson, notes to Section VIII.3 and Theorem VIII.3.27).

- S. C. Kleene, *Hierarchies of number-theoretic predicates*, Bulletin of the American Mathematical Society 61 (1955), 193–213.
- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- B. Monin and L. Patey, *Computability theory*, chapters "Hyperarithmetic sets" and "Beyond hyperarithmetic".
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section VIII.3.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009.
