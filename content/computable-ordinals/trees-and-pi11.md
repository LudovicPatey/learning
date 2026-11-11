---
title: Well-founded trees and Π¹₁ sets
summary: Well-founded trees and their ranks; the Kleene–Brouwer ordering; the normal form of Π¹₁ sets as sets of indices of well-founded trees; the Π¹₁-completeness of well-foundedness and well-ordering; Π¹₁ is not Σ¹₁; Spector's boundedness theorem.
duration: 45
prerequisites: [kleene-o]
---

The arithmetic hierarchy classifies sets defined by quantifiers over numbers. Quantifying over sets or functions gives the **analytic** hierarchy, whose first level, the $\Pi^1_1$ sets, is the central object of higher computability. This lesson shows that the $\Pi^1_1$ sets are exactly the sets $\{ n : T_n \text{ is well-founded} \}$ for uniformly computable sequences of trees $(T_n)$, that being a well-ordering is a complete $\Pi^1_1$ property, and that the $\Sigma^1_1$ sets of well-orderings have bounded order types. The last result, Spector's boundedness theorem, is the main tool of the next course.

## Trees on ℕ and their ranks

A **tree** $T \subseteq \nat^{<\nat}$ is a set of finite sequences of numbers closed under prefixes. A **path** of $T$ is a function $f \in \nat^\nat$ all of whose prefixes belong to $T$. The tree is **well-founded** if it has no path. For $\sigma \in T$, write $T_\sigma = \{ \tau : \sigma\tau \in T \}$.

:::definition{#def-tree-rank}
The **rank** of a well-founded tree is defined by transfinite recursion: $\mathrm{rk}(T) = \sup \{ \mathrm{rk}(T_{\langle n \rangle}) + 1 : \langle n \rangle \in T \}$, and $\mathrm{rk}(\emptyset) = 0$.
:::

The recursion is legitimate because the relation "$\tau$ properly extends $\sigma$", restricted to a well-founded tree, has no infinite increasing chains. The rank of a well-founded tree is a countable ordinal, and every countable ordinal is the rank of some well-founded tree. A tree with a path has no rank.

The **Kleene–Brouwer ordering** on $\nat^{<\nat}$ is defined by $\sigma <_{\mathrm{KB}} \tau$ if $\sigma$ properly extends $\tau$, or if $\sigma(i) < \tau(i)$ at the first position $i$ where they differ. It is a computable linear order: extensions come before their prefixes, and incomparable sequences are compared lexicographically.

:::theorem{#thm-kleene-brouwer}
A tree $T$ is well-founded if and only if $<_{\mathrm{KB}}$ restricted to $T$ is a well-ordering. In that case, its order type is at least $\mathrm{rk}(T)$.
:::

:::proof{of=thm-kleene-brouwer}
If $T$ has a path $f$, then $f \uh 0 >_{\mathrm{KB}} f \uh 1 >_{\mathrm{KB}} \cdots$ is a descending sequence.

Suppose $T$ well-founded; we prove by induction on $\mathrm{rk}(T)$ that $(T, <_{\mathrm{KB}})$ is a well-ordering of type at least $\mathrm{rk}(T)$. If $T$ is empty, both are $0$. Otherwise, the nodes of $T$ other than the root are the sequences $\langle n \rangle \tau$ with $\tau \in T_{\langle n \rangle}$, and the ordering compares first the initial numbers $n$, then the sequences $\tau$ by the Kleene–Brouwer ordering; the root comes last. So $(T, <_{\mathrm{KB}})$ is the ordered sum of the orderings $(T_{\langle n \rangle}, <_{\mathrm{KB}})$ for $n = 0, 1, 2, \dots$ with $\langle n \rangle \in T$, followed by one element. Each summand is a well-ordering of type at least $\mathrm{rk}(T_{\langle n \rangle})$, by the induction hypothesis, and an ordered sum of well-orderings indexed by a well-ordering is a well-ordering. Its type is at least $\mathrm{rk}(T_{\langle n \rangle}) + 1$ for every $n$, hence at least $\mathrm{rk}(T)$.
:::

:::quiz[the Kleene–Brouwer ordering]
Why do extensions come **before** their prefixes in the Kleene–Brouwer ordering?

- [x] So that a path, which gives longer and longer prefixes, yields a descending sequence; with the opposite convention, a path would give an increasing sequence, compatible with well-ordering.
- [ ] So that the ordering is computable.

  Both conventions give computable orderings; the choice matters for well-foundedness.
- [ ] So that the root is the least element.

  With this convention the root is the largest element.
:::

## Π¹₁ sets and their normal form

:::definition{#def-pi11-set}
A set $A \subseteq \nat$ is **$\Pi^1_1$** if there is an arithmetic formula $\varphi(n, X)$ such that $n \in A \iff \forall X \subseteq \nat\ \varphi(n, X)$. It is **$\Sigma^1_1$** if its complement is $\Pi^1_1$, and **$\Delta^1_1$** if it is both.
:::

Quantifiers over functions $f \in \nat^\nat$ can be used instead of quantifiers over sets, by coding a function by its graph; the class is the same. Every arithmetic set is $\Delta^1_1$. Relativized to an oracle $Y$, one obtains the $\Pi^1_1(Y)$ sets.

:::theorem[Kleene normal form]{#thm-pi11-normal-form}
A set $A$ is $\Pi^1_1$ if and only if there is a uniformly computable sequence of trees $(T_n)$ such that $n \in A$ if and only if $T_n$ is well-founded.
:::

:::proof{of=thm-pi11-normal-form}
($\Leftarrow$) $T_n$ is well-founded if and only if $\forall f\ \exists m\ f \uh m \notin T_n$, a $\Pi^1_1$ formula.

($\Rightarrow$) Write $n \in A \iff \forall f\, \varphi(n, f)$ with $\varphi$ arithmetic in prenex form. We first show, by induction on the number of number quantifiers, that every prenex arithmetic formula $\psi(f)$ is equivalent to a formula $\forall h\ \exists y\ \theta(f, h, y)$ with $\theta$ bounded.

- A bounded formula $\theta$ is equivalent to $\forall h\, \exists y\, \theta$, with dummy variables.
- If $\psi \equiv \forall x\, \chi(x)$ and $\chi(x) \equiv \forall h\, \exists y\, \theta(x, h, y)$, then $\psi \equiv \forall h'\, \exists y\, \theta(h'(0), h'', y)$, where $h''(i) = h'(i+1)$: the single function $h'$ codes both $x$ and $h$.
- If $\psi \equiv \exists x\, \chi(x)$ and $\chi(x) \equiv \forall h\, \exists y\, \theta(x, h, y)$, then $\psi \equiv \forall H\, \exists x\, \exists y\, \theta(x, H^{[x]}, y)$, where $H^{[x]}(i) = H(\langle x, i \rangle)$. Indeed, if $x_0$ witnesses $\psi$, then $\chi(x_0)$ applies to $H^{[x_0]}$. Conversely, if $\psi$ fails, choose for each $x$ a function $h_x$ with $\neg \exists y\, \theta(x, h_x, y)$, and let $H^{[x]} = h_x$; then $\exists x\, \exists y\, \theta(x, H^{[x]}, y)$ fails. The two existential quantifiers merge into one.

So $n \in A \iff \forall g\, \exists y\, \theta(n, g, y)$, where $g$ codes $f$ and the auxiliary function, and $\theta$ is bounded. The evaluation of the bounded formula $\theta(n, g, y)$ queries $g$ at finitely many arguments only. Let $R(n, \sigma)$ hold if for some $y < |\sigma|$, the evaluation of $\theta(n, g, y)$ with $\sigma$ in place of $g$ queries only arguments below $|\sigma|$ and returns true. Then $R$ is computable, and $\exists y\, \theta(n, g, y) \iff \exists m\, R(n, g \uh m)$: from left to right, take $m$ larger than $y$ and than every argument queried; from right to left, $g$ and $g \uh m$ agree on the queried arguments. Let $T_n = \{ \sigma : \neg R(n, \tau) \text{ for every } \tau \preceq \sigma \}$. Then $T_n$ is a tree, uniformly computable, and it has a path $g$ if and only if $\exists y\, \theta(n, g, y)$ fails for $g$, that is, if and only if $n \notin A$.
:::

The proof uses the axiom of choice in the third case, a countable choice of functions; this is harmless in the metatheory.

:::corollary{#cor-pi11-complete}
Let $\mathrm{WF}$ be the set of indices of computable trees that are well-founded, and $\mathrm{WO}$ the set of indices of computable linear orders that are well-orderings. Both are $\Pi^1_1$, and every $\Pi^1_1$ set is many-one reducible to each of them.
:::

:::proof{of=cor-pi11-complete}
Both definitions are $\Pi^1_1$: "for every $f$, $f$ is not a path", and "for every $f$, $f$ is not a descending sequence", together with the arithmetic conditions of being a tree or a linear order. If $A$ is $\Pi^1_1$, the normal form gives a computable function $n \mapsto$ an index of $T_n$, reducing $A$ to $\mathrm{WF}$. Composing with the computable map sending an index of a tree to an index of its Kleene–Brouwer ordering reduces $A$ to $\mathrm{WO}$, by :ref{#thm-kleene-brouwer}.
:::

The set $\mathcal O$ of notations is also $\Pi^1_1$: it is the least set closed under the three rules of :ref{#def-kleene-o}, so $a \in \mathcal O$ if and only if $a$ belongs to every set that is closed under the rules, together with a relation playing the role of $<_{\mathcal O}$; this is a $\Pi^1_1$ condition. It is also $\Pi^1_1$-complete, a result we admit (Sacks, *Higher Recursion Theory*, Section I.5).

## Π¹₁ is not Σ¹₁

:::proposition{#prop-pi11-not-sigma11}
There is a $\Pi^1_1$ set that is not $\Sigma^1_1$. In particular $\mathrm{WF}$ and $\mathrm{WO}$ are not $\Sigma^1_1$.
:::

:::proof{of=prop-pi11-not-sigma11}
For each $e$ and $n$, let $T_{e,n}$ be the set of sequences $\sigma$ such that no prefix $\tau \preceq \sigma$ satisfies $\Phi_e(\langle n, \tau \rangle)[|\sigma|]\converge = 0$. It is a tree, computable uniformly in $e$ and $n$, even when $\Phi_e$ is partial. Let $(T_n)$ be given by :ref{#thm-pi11-normal-form} for a $\Pi^1_1$ set $A$, with $T_n = \{ \sigma : \neg R(n, \tau) \text{ for all } \tau \preceq \sigma \}$, and let $\Phi_e$ compute the characteristic function of $R$, with value $0$ when $R$ holds. A path of $T_n$ is a path of $T_{e,n}$. Conversely, if $f$ is a path of $T_{e,n}$, then for each $k$ the computation $\Phi_e(\langle n, f \uh k \rangle)$ converges at some stage $s$, and $f \uh m \in T_{e,n}$ for $m \geq \max(s, k)$ shows that $R(n, f \uh k)$ fails; so $f$ is a path of $T_n$. Hence $T_{e,n}$ is well-founded if and only if $T_n$ is, and $U = \{ \langle e, n \rangle : T_{e,n} \text{ is well-founded} \}$ is a $\Pi^1_1$ set whose sections $U_e = \{ n : \langle e, n \rangle \in U \}$ include all the $\Pi^1_1$ sets.

Suppose that $U$ were $\Sigma^1_1$. Then its complement would be $\Pi^1_1$, and so would be $D = \{ n : \langle n, n \rangle \notin U \}$, its preimage under the computable map $n \mapsto \langle n, n \rangle$; hence $D = U_e$ for some $e$; then $e \in D \iff \langle e, e \rangle \notin U \iff e \notin U_e = D$, a contradiction. So $U$ is not $\Sigma^1_1$. Since $U$ reduces to $\mathrm{WF}$ and $\mathrm{WO}$, these are not $\Sigma^1_1$ either: $\Sigma^1_1$ sets are closed under computable preimages.
:::

## Spector's boundedness theorem

For an index $e$ of a computable linear order, write $L_e$ for this order; for $e \in \mathrm{WO}$, its order type $|L_e|$ is a computable ordinal.

:::theorem[Spector]{#thm-boundedness}
If $A \subseteq \mathrm{WO}$ is $\Sigma^1_1$, then $\sup \{ |L_e| : e \in A \} < \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=thm-boundedness}
The supremum is at most $\omega_1^{\mathrm{CK}}$; suppose that it is equal to $\omega_1^{\mathrm{CK}}$. Then for every index $e$,
$$
\begin{aligned}
e \in \mathrm{WO} \iff{} & L_e \text{ is a linear order and } \exists d\, \big(d \in A \wedge \exists h\ \\
& (h \text{ is an order-preserving injection from } L_e \text{ into } L_d)\big).
\end{aligned}
$$
If $e \in \mathrm{WO}$, then $|L_e| < \omega_1^{\mathrm{CK}}$, so some $d \in A$ has $|L_d| \geq |L_e|$, and $L_e$ embeds into $L_d$ by the comparison theorem (:ref{#thm-wo-comparison}). Conversely, a linear order that embeds into a well-ordering is a well-ordering, since a descending sequence would be mapped to a descending sequence. The right-hand side is $\Sigma^1_1$: "$d \in A$" is $\Sigma^1_1$, "$h$ is an order-preserving injection" is arithmetic, and existential quantifiers combine. So $\mathrm{WO}$ would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}.
:::

:::corollary{#cor-boundedness}
1. For every computable ordinal $\alpha$, the set $\mathrm{WO}_{< \alpha}$ of indices $e \in \mathrm{WO}$ with $|L_e| < \alpha$ is $\Delta^1_1$.
2. The set $\mathcal O$ is not $\Sigma^1_1$.
:::

:::proof{of=cor-boundedness}
1. Let $d$ be an index of a computable well-ordering of type $\alpha$. Then $e \in \mathrm{WO}_{<\alpha}$ if and only if $L_e$ is a linear order that embeds into a proper initial segment of $L_d$, a $\Sigma^1_1$ condition; and if and only if $e \in \mathrm{WO}$ and $L_d$ does not embed into $L_e$, a $\Pi^1_1$ condition, since "$L_d$ embeds into $L_e$" is $\Sigma^1_1$.
2. Let $f$ be the total computable function of :ref{#prop-constructive-computable}, which maps every $a \in \mathcal O$ to an index of a computable well-ordering of type $|a|$. If $\mathcal O$ were $\Sigma^1_1$, then $\{ e : \exists a\, (a \in \mathcal O \wedge f(a) = e) \}$ would be a $\Sigma^1_1$ subset of $\mathrm{WO}$ containing well-orderings of every computable type, by :ref{#cor-constructive-computable}. This contradicts :ref{#thm-boundedness}.
:::

:::quiz[the boundedness theorem]
In the proof of :ref{#thm-boundedness}, why does the unboundedness of $A$ make $\mathrm{WO}$ a $\Sigma^1_1$ set?

- [x] Because a computable linear order is then a well-ordering exactly when it embeds into some member of $A$, and this is expressed with existential quantifiers over a number, a function, and the $\Sigma^1_1$ condition $d \in A$.
- [ ] Because $A$ is equal to $\mathrm{WO}$.

  $A$ may be much smaller than $\mathrm{WO}$; it only needs to contain arbitrarily long well-orderings.
- [ ] Because every well-ordering is computable.

  This is false, since $\omega_1^{\mathrm{CK}}$ is not computable, and it is not needed: only the well-orderings with an index in $\mathrm{WO}$ are concerned.

---

Why is "embedding into a well-ordering" enough to guarantee well-foundedness?

- [x] Because an order-preserving map sends a descending sequence to a descending sequence, and the target has none.
- [ ] Because the embedding is computable.

  The embedding is an arbitrary function; only order preservation is used.
- [ ] Because both orders are computable.

  Computability plays no role in this step.
:::

## Exercises

::::exercise{difficulty=1}
Show that the set of indices $e$ such that $W_e$, viewed as a set of sequences, is a well-founded tree is $\Pi^1_1$, and that every $\Sigma^1_1$ set of such indices has ranks bounded below $\omega_1^{\mathrm{CK}}$.

:::solution
"$W_e$ is closed under prefixes" is arithmetic and "no function is a path of $W_e$" is $\Pi^1_1$. For the bound, the Kleene–Brouwer ordering restricted to $W_e$ is a c.e. linear order, uniformly in $e$; preceded by a copy of $\omega$, it has an infinite field, and :ref{#prop-computable-ordinals-basic} (3) gives a total computable function $f$ such that $f(e)$ is an index of a computable linear order isomorphic to $\omega + (W_e, <_{\mathrm{KB}})$. If $W_e$ is a well-founded tree, then $f(e) \in \mathrm{WO}$ and $|L_{f(e)}| \geq \mathrm{rk}(W_e)$, by :ref{#thm-kleene-brouwer}. The image under $f$ of a $\Sigma^1_1$ set $B$ of such indices, $\{ d : \exists e\, (e \in B \wedge f(e) = d) \}$, is a $\Sigma^1_1$ subset of $\mathrm{WO}$, so its types, and hence the ranks of the trees $W_e$, $e \in B$, are bounded below $\omega_1^{\mathrm{CK}}$ by :ref{#thm-boundedness}.
:::
::::

::::exercise{difficulty=2}
Show that $\omega_1^{\mathrm{CK}}$ is the supremum of the ranks of the computable well-founded trees, and that some computable tree has a path but no computable path.

:::solution
A computable well-founded tree has computable Kleene–Brouwer ordering, of type at least its rank, so its rank is computable. Conversely, a computable well-ordering $L$ of type $\alpha$ gives the computable tree of finite $L$-descending sequences, which is well-founded, of rank at least $\alpha$: by induction, the subtree above a one-element sequence $\langle x \rangle$ has rank at least the type of the initial segment below $x$.

For the second statement, let $T$ be the set of $\sigma \in 2^{<\nat}$ such that $\sigma(e) \neq \Phi_e(e)$ for every $e < |\sigma|$ with $\Phi_e(e)[|\sigma|]\converge$. It is a computable tree, and its paths are the $\{0,1\}$-valued functions $f$ with $f(e) \neq \Phi_e(e)$ whenever $\Phi_e(e)\converge$. It has a path, for instance $f(e) = 1$ if $\Phi_e(e)\converge = 0$ and $f(e) = 0$ otherwise. No path $f$ is computable: if $f = \Phi_e$, then $\Phi_e(e)\converge = f(e)$, a contradiction. (This is the tree of :ref{#thm-dnc2-no-computable}.)
:::
::::

## Notes and references

Kleene (1955) introduced the analytic hierarchy and proved the normal form theorem; the use of well-founded trees is due to Lusin and Sierpiński in descriptive set theory, and to Brouwer for the ordering. Spector (1955) proved the boundedness theorem. Moschovakis's *Descriptive Set Theory* presents the effective theory in the general setting of Polish spaces.

- S. C. Kleene, *Arithmetical predicates and function quantifiers*, Transactions of the American Mathematical Society 79 (1955), 312–340.
- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009.
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
