---
title: Π¹₁ versus Σ¹₁ and the boundedness theorem
summary: A diagonal argument shows that Π¹₁ is not Σ¹₁; Spector's boundedness theorem bounds the types of a Σ¹₁ set of well-orderings below ω₁ᶜᵏ; applications to the ordinals ω₁ˣ and to ill-founded computable orders without arithmetic descending sequences.
duration: 45
prerequisites: [trees-and-pi11]
---

The previous lesson showed that $\mathrm{WF}$, $\mathrm{WO}$ and $\mathcal O$ are complete $\Pi^1_1$ sets. This lesson shows that they are not $\Sigma^1_1$, by a diagonal argument, and then proves the quantitative form of this fact due to Spector: the order types of a $\Sigma^1_1$ set of computable well-orderings are bounded by a computable ordinal. The boundedness theorem is the main tool of the course on hyperarithmetic sets, where it gives Kleene's theorem $\Delta^1_1 = \mathrm{HYP}$. Two applications close the lesson: the computation of $\omega_1^X$ for arithmetic $X$ and for $X = \mathcal O$, and the existence of ill-founded computable linear orders that look well-founded to every arithmetic sequence.

## Π¹₁ is not Σ¹₁

The separation of $\Pi^1_1$ from $\Sigma^1_1$ is the analogue of the fact that some c.e. set is not co-c.e., and its proof is the same **diagonal argument**: a universal $\Pi^1_1$ set is built, and its diagonal, if it were $\Pi^1_1$, would be one of its own sections. The normal form theorem provides the universal set, by enumerating the trees given by all programs.

:::proposition{#prop-pi11-not-sigma11}
There is a $\Pi^1_1$ set that is not $\Sigma^1_1$. In particular $\mathrm{WF}$ and $\mathrm{WO}$ are not $\Sigma^1_1$.
:::

:::proof{of=prop-pi11-not-sigma11}
For each $e$ and $n$, let $T_{e,n}$ be the set of sequences $\sigma$ such that no prefix $\tau \preceq \sigma$ satisfies $\Phi_e(\langle n, \tau \rangle)[|\sigma|]\converge = 0$. It is a tree, computable uniformly in $e$ and $n$, even when $\Phi_e$ is partial. Let $(T_n)$ be given by :ref{#thm-pi11-normal-form} for a $\Pi^1_1$ set $A$, with $T_n = \{ \sigma : \neg R(n, \tau) \text{ for all } \tau \preceq \sigma \}$, and let $\Phi_e$ compute the characteristic function of $R$, with value $0$ when $R$ holds. A path of $T_n$ is a path of $T_{e,n}$. Conversely, if $f$ is a path of $T_{e,n}$, then for each $k$ the computation $\Phi_e(\langle n, f \uh k \rangle)$ converges at some stage $s$, and $f \uh m \in T_{e,n}$ for $m \geq \max(s, k)$ shows that $R(n, f \uh k)$ fails; so $f$ is a path of $T_n$. Hence $T_{e,n}$ is well-founded if and only if $T_n$ is, and $U = \{ \langle e, n \rangle : T_{e,n} \text{ is well-founded} \}$ is a $\Pi^1_1$ set whose sections $U_e = \{ n : \langle e, n \rangle \in U \}$ include all the $\Pi^1_1$ sets.

Suppose that $U$ were $\Sigma^1_1$. Then its complement would be $\Pi^1_1$, and so would be $D = \{ n : \langle n, n \rangle \notin U \}$, its preimage under the computable map $n \mapsto \langle n, n \rangle$; hence $D = U_e$ for some $e$; then $e \in D \iff \langle e, e \rangle \notin U \iff e \notin U_e = D$, a contradiction. So $U$ is not $\Sigma^1_1$. Since $U$ reduces to $\mathrm{WF}$ and $\mathrm{WO}$, these are not $\Sigma^1_1$ either: $\Sigma^1_1$ sets are closed under computable preimages.
:::

:::quiz[the diagonal argument]
In the proof of :ref{#prop-pi11-not-sigma11}, why are the trees $T_{e,n}$ defined with the clock $[|\sigma|]$, instead of as $\{ \sigma : \Phi_e(\langle n, \tau \rangle) \neq 0 \text{ for all } \tau \preceq \sigma \}$?

- [x] So that they are computable trees for every $e$, including the indices $e$ of partial functions, which the enumeration of all $\Pi^1_1$ sets cannot avoid.
- [ ] So that they are well-founded.

  Well-foundedness depends on $e$ and $n$; the clock only makes the trees computable.
- [ ] So that $U$ is $\Sigma^1_1$.

  The proof shows that $U$ is not $\Sigma^1_1$.
:::

By :ref{#thm-o-complete}, $\mathrm{WO}$ reduces to $\mathcal O$, so $\mathcal O$ is not $\Sigma^1_1$ either; in particular, $\mathcal O$, $\mathrm{WF}$ and $\mathrm{WO}$ are not arithmetic. The rest of this lesson gives a quantitative form of the result: a $\Sigma^1_1$ set of well-orderings has bounded order types.

## Spector's boundedness theorem

Every set of computable ordinals is bounded by $\omega_1^{\mathrm{CK}}$. Spector's theorem says that a set of indices of well-orderings that is $\Sigma^1_1$ stays strictly below. The proof is a **boundedness argument** that recurs throughout higher computability: if a $\Sigma^1_1$ set $A \subseteq \mathrm{WO}$ had types cofinal in $\omega_1^{\mathrm{CK}}$, then the members of $A$ would serve as yardsticks, and a computable linear order would be a well-ordering exactly when it embeds into one of them. This would give a $\Sigma^1_1$ definition of $\mathrm{WO}$, which does not exist.

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

:::figure[The argument of Spector's theorem, under the hypothesis to be refuted: the types of the members of $A$ are cofinal in $\omega_1^{\mathrm{CK}}$, so every computable well-ordering $L_e$ embeds into one of them.]
<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="The order types of the members of A, drawn on the line of computable ordinals, are cofinal below omega one CK; every computable well-ordering embeds into one of them"><defs><marker id="co-sp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><line x1="30" y1="92" x2="520" y2="92" class="axis"/><line x1="520" y1="82" x2="520" y2="102" class="ink-stroke" stroke-width="1.4"/><text x="520" y="122" text-anchor="middle" font-size="16"><tspan class="math">ω</tspan><tspan class="mrm" font-size="11" dy="4">1</tspan><tspan class="mrm" font-size="10" dy="-11">CK</tspan></text><text x="30.0" y="122.0" text-anchor="middle" class="mrm" font-size="15">0</text><circle cx="80" cy="92" r="4" class="accent-fill"/><circle cx="170" cy="92" r="4" class="accent-fill"/><circle cx="250" cy="92" r="4" class="accent-fill"/><circle cx="318" cy="92" r="4" class="accent-fill"/><circle cx="372" cy="92" r="4" class="accent-fill"/><circle cx="414" cy="92" r="4" class="accent-fill"/><circle cx="446" cy="92" r="4" class="accent-fill"/><circle cx="470" cy="92" r="4" class="accent-fill"/><circle cx="488" cy="92" r="4" class="accent-fill"/><circle cx="500" cy="92" r="4" class="accent-fill"/><text x="250.0" y="122.0" text-anchor="middle" class="label" font-size="12">the types |L<tspan font-size="9" dy="3">d</tspan><tspan dy="-3"> </tspan>|, d ∈ A</text><line x1="210" y1="58" x2="210" y2="86" class="ink-stroke" stroke-width="1.2"/><text x="210" y="52" text-anchor="middle" font-size="15"><tspan class="mrm">|</tspan><tspan class="math">L</tspan><tspan class="math" font-size="10" dy="4">e</tspan><tspan class="mrm" dy="-4">|</tspan></text><path d="M216,62 Q262,40 312,82" class="muted-stroke" stroke-width="1.2" marker-end="url(#co-sp)"/><text x="330.0" y="46.0" text-anchor="start" class="label" font-size="12">L<tspan font-size="9" dy="3">e</tspan><tspan dy="-3"> </tspan> embeds into some L<tspan font-size="9" dy="3">d</tspan><tspan dy="-3"> </tspan></text></svg>
:::

Both hypotheses are needed. The set $\mathrm{WO}$ itself is a $\Pi^1_1$ subset of $\mathrm{WO}$ whose types are all the computable ordinals, so $\Sigma^1_1$ cannot be replaced by $\Pi^1_1$. And a $\Sigma^1_1$ set of indices of linear orders that are not all well-orderings may contain orders of every computable type, for instance the arithmetic set of all indices of linear orders.

:::corollary{#cor-boundedness}
1. For every computable ordinal $\alpha$, the set $\mathrm{WO}_{< \alpha}$ of indices $e \in \mathrm{WO}$ with $|L_e| < \alpha$ is $\Delta^1_1$.
2. The set $\mathcal O$ is not $\Sigma^1_1$ (a second proof, independent of :ref{#thm-o-complete}).
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

## Applications

The first application compares the ordinals $\omega_1^X$, introduced at the end of :ref{to="computable-ordinals/markwald"}, with $\omega_1^{\mathrm{CK}}$.

:::proposition{#prop-omega1-relative}
1. If $X$ is arithmetic, then $\omega_1^X = \omega_1^{\mathrm{CK}}$.
2. $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$.
:::

:::proof{of=prop-omega1-relative}
1. Every computable ordinal is $X$-computable, so $\omega_1^X \geq \omega_1^{\mathrm{CK}}$. Suppose $\omega_1^X > \omega_1^{\mathrm{CK}}$, and let $W$ be an $X$-computable well-ordering of type at least $\omega_1^{\mathrm{CK}}$. Then $e \in \mathrm{WO}$ if and only if $e$ is an index of a computable linear order and $\exists h$ ($h$ is an order-preserving injection from $L_e$ into $W$): if $e \in \mathrm{WO}$, then $|L_e| < \omega_1^{\mathrm{CK}} \leq |W|$ and the comparison theorem gives $h$; conversely, an order that embeds into a well-ordering is a well-ordering. Since $X$ is arithmetic, so is $W$, and the condition is $\Sigma^1_1$. This contradicts :ref{#prop-pi11-not-sigma11}.
2. By :ref{#thm-o-complete}, $\mathrm{WO} \leq_m \mathcal O$, so $\mathrm{WO}$ is computable in $\mathcal O$. Let $S$ be the ordered sum of the orders $L_e$, $e \in \mathrm{WO}$, in increasing order of $e$: its elements are the pairs $\langle e, x \rangle$ with $e \in \mathrm{WO}$ and $x$ in the field of $L_e$, compared first by $e$, then by $L_e$. It is computable in $\mathcal O$, and it is a well-ordering, since a descending sequence would have eventually constant first components and then descend in some $L_e$. Its type is at least $|L_e|$ for every $e \in \mathrm{WO}$, hence at least $\omega_1^{\mathrm{CK}}$. So $\omega_1^{\mathrm{CK}}$ is $\mathcal O$-computable, by (1) of :ref{#prop-computable-ordinals-basic} relativized, and $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$.
:::

The course on hyperarithmetic sets extends (1) to every hyperarithmetic $X$. Spector proved more: $\omega_1^X > \omega_1^{\mathrm{CK}}$ exactly when $\mathcal O$ is hyperarithmetic in $X$ (Nies, Theorem 9.1.14).

The second application is an **overspill** argument. A $\Sigma^1_1$ property that holds of every computable well-ordering must also hold of some ill-founded computable linear order, since otherwise it would define $\mathrm{WO}$. Choosing the property "has no arithmetic descending sequence" gives ill-founded orders that arithmetic sets cannot distinguish from well-orderings.

:::proposition{#prop-pseudo-wo}
There is a computable linear order that is not a well-ordering but has no arithmetic descending sequence.
:::

:::proof{of=prop-pseudo-wo}
By Post's theorem (:ref{#thm-post}), a function is arithmetic if and only if it is computable in $\emptyset^{(n)}$ for some $n$. Let $B$ be the set of indices $e$ of computable linear orders such that for all $n$ and $i$, $\Phi_i^{\emptyset^{(n)}}$ is not a total descending sequence of $L_e$. Then $\mathrm{WO} \subseteq B$. The set $B$ is $\Sigma^1_1$: $e \in B$ if and only if $e$ is an index of a linear order and there is a set $X$ with $X^{[0]} = \emptyset$, $X^{[n+1]} = (X^{[n]})'$ for every $n$, and such that for all $n$ and $i$, $\Phi_i^{X^{[n]}}$ is not a total descending sequence of $L_e$. Here $X^{[n]} = \{ x : \langle n, x \rangle \in X \}$; the conditions on $X$ are arithmetic, since "$Z = Y'$" is, and they are satisfied by exactly one set, whose columns are the sets $\emptyset^{(n)}$. Since $\mathrm{WO}$ is not $\Sigma^1_1$ (:ref{#prop-pi11-not-sigma11}), $B \neq \mathrm{WO}$, and any $e \in B \setminus \mathrm{WO}$ is an index of the required order.
:::

Harrison (1968) went further: some computable linear order that is not a well-ordering has no hyperarithmetic descending sequence, and its well-founded part has type $\omega_1^{\mathrm{CK}}$. This is proved in the course on hyperarithmetic sets (:ref{#thm-harrison}). Such **pseudo-well-orderings** are the basis of the method of pseudohierarchies in reverse mathematics (Simpson, Section V.4).

## Exercises

::::exercise{#ex-tree-boundedness difficulty=1}
Show that the set of indices $e$ such that $W_e$, viewed as a set of sequences, is a well-founded tree is $\Pi^1_1$, and that every $\Sigma^1_1$ set of such indices has ranks bounded below $\omega_1^{\mathrm{CK}}$.

:::solution
"$W_e$ is closed under prefixes" is arithmetic and "no function is a path of $W_e$" is $\Pi^1_1$. For the bound, the Kleene–Brouwer ordering restricted to $W_e$ is a c.e. linear order, uniformly in $e$; preceded by a copy of $\omega$, it has an infinite field, and :ref{#prop-computable-ordinals-basic} (3) gives a total computable function $f$ such that $f(e)$ is an index of a computable linear order isomorphic to $\omega + (W_e, <_{\mathrm{KB}})$. If $W_e$ is a well-founded tree, then $f(e) \in \mathrm{WO}$ and $|L_{f(e)}| \geq \mathrm{rk}(W_e)$, by :ref{#thm-kleene-brouwer}. The image under $f$ of a $\Sigma^1_1$ set $B$ of such indices, $\{ d : \exists e\, (e \in B \wedge f(e) = d) \}$, is a $\Sigma^1_1$ subset of $\mathrm{WO}$, so its types, and hence the ranks of the trees $W_e$, $e \in B$, are bounded below $\omega_1^{\mathrm{CK}}$ by :ref{#thm-boundedness}.
:::
::::

::::exercise{#ex-o-bounded difficulty=1}
Show that for every $\Sigma^1_1$ set $A \subseteq \mathcal O$, there is $b \in \mathcal O$ with $|a| < |b|$ for every $a \in A$.

:::solution
Let $f$ be the total computable function of :ref{#prop-constructive-computable}. The set $\{ e : \exists a\, (a \in A \wedge f(a) = e) \}$ is a $\Sigma^1_1$ subset of $\mathrm{WO}$, so by :ref{#thm-boundedness} there is $\gamma < \omega_1^{\mathrm{CK}}$ with $|a| = |L_{f(a)}| \leq \gamma$ for every $a \in A$. The ordinal $\gamma + 1$ is computable, hence constructive (:ref{#cor-constructive-computable}): any notation $b$ of $\gamma + 1$ works.
:::
::::

## Notes and references

The diagonal argument that $\Pi^1_1$ is not $\Sigma^1_1$ is Kleene's (1955); in descriptive set theory, the corresponding result, that the set of codes of countable well-orderings is not analytic, is due to Lusin and Sierpiński. Spector (1955) proved the boundedness theorem. Simpson proves that $\mathrm{WO}$ is not $\Sigma^1_1$ in Theorems V.1.9 and V.1.10, by the same diagonal argument, and that $\mathcal O^X$ is not $\Sigma^1_1$ in $X$ in Lemma VIII.3.4, for a variant of $\mathcal O$; he states the $\Sigma^1_1$ bounding principle as Lemma V.6.2 and discusses pseudohierarchies in Section V.4. Monin and Patey prove the boundedness lemma in their section on the Kleene–Suslin theorem, in the chapter *Beyond hyperarithmetic*, and treat pseudo-well-orders and Harrison's theorem later in that chapter. Nies proves $\omega_1^{\mathcal O} > \omega_1^{\mathrm{CK}}$ as Exercise 9.1.8 and Spector's characterization of $\omega_1^X > \omega_1^{\mathrm{CK}}$ as Theorem 9.1.14.

- S. C. Kleene, *Arithmetical predicates and function quantifiers*, Transactions of the American Mathematical Society 79 (1955), 312–340.
- C. Spector, *Recursive well-orderings*, Journal of Symbolic Logic 20 (1955), 151–163.
- J. Harrison, *Recursive pseudo-well-orderings*, Transactions of the American Mathematical Society 131 (1968), 526–543.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.1, V.4, V.6 and VIII.3.
- B. Monin and L. Patey, *Computability theory*, chapter *Beyond hyperarithmetic*.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.1.
