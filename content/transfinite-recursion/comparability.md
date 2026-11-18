---
title: Comparability of well-orderings implies ATR₀
summary: The comparability of countable well-orderings implies arithmetic comprehension and the Σ¹₁ bounding principle; double descent trees; padding the orders of a sequence to a common type, so that a single comparison map gives all comparisons at once; comparability is equivalent to ATR₀ over RCA₀ (Friedman).
duration: 35
prerequisites: [sigma11-separation, pseudohierarchies]
---

$\mathsf{ATR}_0$ proves that any two well-orderings are comparable (:ref{#thm-atr-comparability}). This lesson proves the converse, due to Friedman: comparability is all of $\mathsf{ATR}_0$. So $\mathsf{ATR}_0$ is exactly the theory in which the countable ordinals form a linear order. The proof derives $\Sigma^1_1$ separation. Its main difficulty is uniformity: comparability compares two orders at a time, while a separating set needs infinitely many comparisons at once. The solution is to pad infinitely many orders to a common type, add them up, and compare the two sums: the single comparison map must match the summands one by one.

Let $\mathsf{CWO}$ be the statement that any two countable well-orderings are comparable.

## First consequences of comparability

:::lemma{#lem-cwo-aca}
Over $\mathsf{RCA}_0$, $\mathsf{CWO}$ implies $\mathsf{ACA}_0$.
:::

:::proof{of=lem-cwo-aca}
We prove that every injection $f$ has a range (:ref{#thm-aca-equivalents}). Order $\nat$ by $m \leq_X n \iff f(m) \leq f(n)$, a linear order since $f$ is injective. It is a well-ordering: if $S$ is non-empty and $s \in S$, the set of values $f(m) \leq f(s)$ with $m \in S$ exists by bounded $\Sigma^0_1$ comprehension, and the $m$ giving its least value is the $\leq_X$-least element of $S$. Every element has finitely many predecessors, at most $f(n)$ for $n$. By $\mathsf{CWO}$, $X$ is comparable with $\omega = (\nat, \leq)$. It is not isomorphic to a finite initial segment of $\omega$, being infinite; and $\omega$ is not isomorphic to a proper initial segment $X \uh k$, which is finite. So there is an isomorphism $g : \omega \to X$. Then $m < n$ implies $f(g(m)) < f(g(n))$, so $f(g(m)) \geq m$, and since $g$ is onto,
$$
k \in \mathrm{ran}(f) \iff \exists m \leq k\ f(g(m)) = k,
$$
a bounded condition: the range exists by $\Delta^0_1$ comprehension.
:::

From now on we argue over $\mathsf{ACA}_0$, so that arithmetic transfinite induction is available.

:::lemma{#lem-cwo-embedding}
The following is provable in $\mathsf{ACA}_0 + \mathsf{CWO}$. If $X$ and $Y$ are well-orderings and $X$ embeds into $Y$, then $|X| \leq |Y|$. If moreover $Y$ embeds into $X$, then $|X| = |Y|$.
:::

:::proof{of=lem-cwo-embedding}
Let $e : X \to Y$ be an embedding. If $|X| \leq |Y|$ fails, then by $\mathsf{CWO}$ there is an isomorphism $h$ of $Y$ onto a proper initial segment $X \uh k$. Then $h \circ e$ is an embedding of $X$ into itself with $h(e(k)) <_X k$, which :ref{#ex-wo-not-initial} (1) excludes. If both orders embed into each other, then $|X| \leq |Y|$ and $|Y| \leq |X|$, and by :ref{#ex-wo-not-initial} (2) neither inequality is strict.
:::

:::lemma[Σ¹₁ bounding]{#lem-sigma11-bounding}
The following is provable in $\mathsf{ACA}_0 + \mathsf{CWO}$. Let $\varphi(X)$ be $\Sigma^1_1$, and suppose that every $X$ with $\varphi(X)$ is a well-ordering. Then there is a well-ordering $Y$ with $|X| < |Y|$ for every $X$ such that $\varphi(X)$.
:::

:::proof{of=lem-sigma11-bounding}
Suppose not. Then for every well-ordering $Y$ there is $X$ with $\varphi(X)$ such that $|X| < |Y|$ fails, hence $|Y| \leq |X|$ by $\mathsf{CWO}$. Conversely, a linear order $Y$ with $|Y| \leq |X|$ for a well-ordering $X$ is a well-ordering, being isomorphic to an initial segment of $X$. So $\mathrm{WO}(Y)$ is equivalent to the $\Sigma^1_1$ formula $\mathrm{LO}(Y) \wedge \exists X\, (\varphi(X) \wedge |Y| \leq |X|)$, contradicting :ref{#thm-wo-not-sigma11}.
:::

In classical descriptive set theory, this is the boundedness theorem: an analytic set of well-orderings has bounded order types (:ref{to="computable-ordinals/boundedness"} for its effective form).

## Double descent trees

For a linear order $X$, the **descent tree** $D(X)$ is the tree of the finite sequences $\langle x_0, \ldots, x_{k-1} \rangle$ with $x_0 >_X x_1 >_X \cdots >_X x_{k-1}$. Its paths are the descending sequences of $X$. For linear orders $X$ and $Y$, let $X * Y = \mathrm{KB}(D(X) \otimes D(Y))$, the Kleene–Brouwer ordering of the product tree of :ref{#thm-atr-sigma11-separation}.

:::lemma{#lem-double-descent}
1. ($\mathsf{ACA}_0$) If $X$ or $Y$ is a well-ordering, then $X * Y$ is a well-ordering.
2. ($\mathsf{ACA}_0 + \mathsf{CWO}$) If $X$ is a well-ordering and $Y$ is not, then $|X| \leq |X * Y|$.
:::

:::proof{of=lem-double-descent}
1. A path of $D(X) \otimes D(Y)$ is a pair of descending sequences of $X$ and $Y$. If one of them is a well-ordering, there is none, and :ref{#prop-kb-aca} applies.
2. For $m \in F_X$, let $\sigma_m$ be the $\leq_{\mathrm{KB}}$-least element of $D(X)$ ending with $m$; it exists since $\mathrm{KB}(D(X))$ is a well-ordering by :ref{#prop-kb-aca}, and $m \mapsto \sigma_m$ exists by arithmetic comprehension. If $m <_X n$, then $\sigma_n \langle m \rangle \in D(X)$ ends with $m$, so $\sigma_m \leq_{\mathrm{KB}} \sigma_n \langle m \rangle <_{\mathrm{KB}} \sigma_n$: the map is an embedding of $X$ into $\mathrm{KB}(D(X))$. Let $(y_i)$ be a descending sequence of $Y$. The map $\tau \mapsto \tau \otimes \langle y_0, \ldots, y_{|\tau|-1} \rangle$ embeds $\mathrm{KB}(D(X))$ into $X * Y$: two sequences of pairs with the same second coordinates first differ where the first coordinates do, and the code of a pair increases with its first coordinate. Composing, $X$ embeds into $X * Y$, which is a well-ordering by 1; by :ref{#lem-cwo-embedding}, $|X| \leq |X * Y|$.
:::

So $X * Y$ is a well-ordering as soon as one factor is, and it is long if the other factor is ill-founded.

## Comparability implies ATR₀

:::theorem[Friedman]{#thm-cwo-atr}
Over $\mathsf{RCA}_0$, $\mathsf{CWO}$ is equivalent to $\mathsf{ATR}_0$.
:::

**Intuition.** Given disjoint $\Sigma^1_1$ properties, written as $\neg \mathrm{WO}(X_n)$ and $\neg \mathrm{WO}(Y_n)$, build well-orderings $Z_n$ that are short, below a fixed $U$, when $X_n$ is ill-founded, and long, above $U$, when $Y_n$ is ill-founded. Deciding which case holds for all $n$ at once needs all the comparisons of $Z_n$ with $U$. Pad each $Z_n$ with the same long order, so that all padded orders have the same type as a fixed order $C$, and compare the sum of the padded orders with the sum of copies of $C$. The comparison map must send each summand to the corresponding copy of $C$; restricted to $Z_n$, it reveals whether $Z_n$ is shorter than $U$.

:::proof{of=thm-cwo-atr}
$\mathsf{ATR}_0$ implies $\mathsf{CWO}$ by :ref{#thm-atr-comparability}. Conversely, assume $\mathsf{CWO}$; by :ref{#lem-cwo-aca}, $\mathsf{ACA}_0$ holds. We prove $\Sigma^1_1$ separation and apply :ref{#thm-atr-sigma11-separation}. Let $\varphi_1$ and $\varphi_0$ be disjoint $\Sigma^1_1$ formulas. By the normal form and :ref{#prop-kb-aca}, there are sequences of linear orders $(X_n)$ and $(Y_n)$, Kleene–Brouwer orderings of trees, with $\varphi_1(n) \iff \neg\mathrm{WO}(X_n)$ and $\varphi_0(n) \iff \neg\mathrm{WO}(Y_n)$. So for every $n$, $X_n$ or $Y_n$ is a well-ordering.

*The bound $U$.* If $X_n$ is not a well-ordering, $Y_n$ is one, and $X * Y_n$ is a well-ordering for every linear order $X$ (:ref{#lem-double-descent} (1)). Apply :ref{#lem-sigma11-bounding} to the $\Sigma^1_1$ formula "$Z = X * Y_n$ for some linear order $X$ and some $n$ with $\neg \mathrm{WO}(X_n)$": there is a well-ordering $U$ with $|X * Y_n| < |U|$ whenever $X$ is a linear order and $X_n$ is not a well-ordering.

*The orders $Z_n$.* Let $Z_n = (U + X_n) * Y_n$. If $X_n$ is not a well-ordering, then $|Z_n| < |U|$ by the choice of $U$. If $Y_n$ is not a well-ordering, then $X_n$ and $U + X_n$ are well-orderings, and $|U| \leq |U + X_n| \leq |Z_n|$ by :ref{#lem-double-descent} (2). In all cases $Z_n$ is a well-ordering, by :ref{#lem-double-descent} (1).

*The bound $V$ and the padding.* By :ref{#lem-sigma11-bounding} again, there is a well-ordering $V$ with $|U| < |V|$ and $|Z_n| < |V|$ for every $n$; let $k \in F_V$ and $h$ an isomorphism of $U$ onto $V \uh k$. Let $V \cdot \omega = \sum_m V$, and
$$
B_n = Z_n + V \cdot \omega, \qquad C = V + V \cdot \omega, \qquad Z = \sum_n B_n, \qquad W = \sum_n C.
$$
All are well-orderings (:ref{#lem-sum-wo}). For each $n$, $B_n$ embeds into $C$, through an isomorphism of $Z_n$ onto an initial segment of $V$ followed by the identity of $V \cdot \omega$; and $C$ embeds into $B_n$, by sending the first copy of $V$ and the copies of $V \cdot \omega$ to the successive copies of $V$ in the part $V \cdot \omega$ of $B_n$. By :ref{#lem-cwo-embedding}, $|B_n| = |C|$ for every $n$.

*One comparison map for all summands.* By $\mathsf{CWO}$, let $f$ be an isomorphism of $Z$ onto an initial segment of $W$, or of $W$ onto an initial segment of $Z$; say the first, the second case being symmetric. Let $z_n$ and $w_n$ be the least elements of the $n$-th summands of $Z$ and $W$. We show by induction on $n$, for the arithmetic formula $f(z_n) = w_n$, that $f$ maps $B_n$ onto the $n$-th copy of $C$. For $n = 0$, $f(z_0) = w_0$ since the range is an initial segment. If $f(z_n) = w_n$, the image of $B_n$ is an initial segment of the final segment of $W$ starting at $w_n$, isomorphic to $C$ since $|B_n| = |C|$; the $n$-th copy of $C$ is another such initial segment. Two isomorphic initial segments of a well-ordering are equal, by :ref{#ex-wo-not-initial}; so $f$ maps $B_n$ onto the $n$-th copy of $C$, and $f(z_{n+1}) = w_{n+1}$. Let $f_n : B_n \to C$ be the induced isomorphisms; the sequence exists by arithmetic comprehension.

*The separating set.* Let $e_n = f_n(b_n)$, where $b_n$ is the least element of the part $V \cdot \omega$ of $B_n$, right after $Z_n$. Then $f_n$ maps $Z_n$ onto the initial segment of $C$ below $e_n$. Let $S$ be the set of $n$ such that $e_n$ lies in the first copy of $V$ in $C$ and $e_n <_V k$; it exists by arithmetic comprehension. If $n \in S$, $Z_n$ is isomorphic to $V \uh e_n$, a proper initial segment of $V \uh k$, so $|Z_n| < |U|$. If $n \notin S$, the initial segment of $C$ below $e_n$ contains $V \uh k$ as an initial segment, so $|U| \leq |Z_n|$. By :ref{#ex-wo-not-initial} (2), exactly one of $|Z_n| < |U|$ and $|U| \leq |Z_n|$ holds, so $n \in S$ if and only if $|Z_n| < |U|$. Hence $\varphi_1(n)$ implies $n \in S$, and $\varphi_0(n)$ implies $n \notin S$.
:::

:::quiz[comparability and transfinite recursion]
Why are the orders $Z_n$ padded with $V \cdot \omega$ before being added?

- [x] So that all summands have the same type as $C$: then the comparison of the two sums is forced, summand by summand, to match $B_n$ with the $n$-th copy of $C$, and one map gives all the comparisons.
- [ ] To make the orders $Z_n$ well-orderings.

  They are well-orderings already, by :ref{#lem-double-descent} (1).
- [ ] Because $\mathsf{CWO}$ applies only to orders of the same type.

  It applies to any two well-orderings; the padding is what makes the comparison of the sums informative.

---

Why does the proof use the bound $U$ twice, as a bound and as a threshold?

- [x] As a bound, $U$ is above all the short orders $Z_n$, those for which $X_n$ is ill-founded; as a threshold, it is below all the long ones, since $U$ is an initial segment of $U + X_n$, which embeds into $Z_n$ when $Y_n$ is ill-founded.
- [ ] Because $U$ is the order type of $\omega_1^{\mathrm{CK}}$.

  $U$ is any well-ordering given by the bounding principle; nothing identifies its type.
- [ ] To make $V$ exist.

  $V$ is obtained from the bounding principle applied to the orders $Z_n$ and $U$.
:::

The proof is a reduction of $\Sigma^1_1$ separation to a single instance of comparability, prepared with two applications of the bounding principle. Hirst and others refined the result: weaker forms of comparability, such as the existence of an embedding of one well-ordering into the other, are also equivalent to $\mathsf{ATR}_0$ (Dzhafarov–Mummert, Theorem 12.1.13, by a different route through the $\Sigma^1_1$ axiom of choice).

::::exercise{#ex-bounding-atr difficulty=1 objective="Show that the Σ¹₁ bounding principle implies comparability, hence ATR₀."}
Show in $\mathsf{ACA}_0$ that $\Sigma^1_1$ bounding, as in :ref{#lem-sigma11-bounding} but assumed as a scheme, implies $\mathsf{CWO}$, and deduce that it is equivalent to $\mathsf{ATR}_0$ over $\mathsf{ACA}_0$.

:::solution
Let $X_0$ and $X_1$ be well-orderings, and $\varphi(X) \equiv X = X_0 \vee X = X_1$, an arithmetic formula. By bounding, there is a well-ordering $Y$ with $|X_0| < |Y|$ and $|X_1| < |Y|$: isomorphisms $g_i$ of $X_i$ onto initial segments $Y \uh k_i$. Say $k_0 \leq_Y k_1$. Then $g_1^{-1} \circ g_0$ is an isomorphism of $X_0$ onto the initial segment of $X_1$ below $g_1^{-1}(k_0)$, if $k_0 <_Y k_1$, or onto $X_1$, if $k_0 = k_1$. So $X_0$ and $X_1$ are comparable. By :ref{#thm-cwo-atr}, $\mathsf{ATR}_0$ follows; conversely $\mathsf{ATR}_0$ proves $\mathsf{CWO}$, hence bounding by :ref{#lem-sigma11-bounding}.
:::
::::

## Notes and references

:ref{#thm-cwo-atr} is due to Friedman, with early versions by Steel (Simpson, notes to Section V.6). The proof follows Simpson, Section V.6: :ref{#lem-cwo-aca} is his Lemma V.6.1, :ref{#lem-sigma11-bounding} Lemma V.6.2, :ref{#lem-cwo-embedding} Lemma V.6.3, :ref{#lem-double-descent} Lemma V.6.5 and the theorem his Theorem V.6.8. The argument that the comparison map matches the summands one by one, by induction on $n$, makes explicit a step that Simpson states briefly. Dzhafarov and Mummert, Section 12.1.2, prove the stronger version with embeddings, following Friedman and Hirst.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section V.6.
- H. Friedman and J. L. Hirst, *Weak comparability of well orderings and reverse mathematics*, Annals of Pure and Applied Logic 47 (1990), 11–29.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 12.1.2.

:::::exercises
::::exercise{#ex-cwo-omega difficulty=1 objective="Compare a well-ordering in which every element has finitely many predecessors with ω, as in the proof that comparability implies arithmetic comprehension."}
Show in $\mathsf{RCA}_0 + \mathsf{CWO}$ that every infinite well-ordering $X$ in which every element has only finitely many predecessors is isomorphic to $\omega$.

:::solution
By $\mathsf{CWO}$, $X$ and $\omega$ are comparable. An isomorphism of $X$ onto a proper initial segment $\{ 0, \ldots, k - 1 \}$ of $\omega$ is impossible, since $X$ is infinite and an injection of an infinite set into a finite set contradicts the finite pigeonhole principle. An isomorphism $g$ of $\omega$ onto a proper initial segment $X \uh k$ is impossible too: $X \uh k$ would contain the infinitely many elements $g(0), g(1), \ldots$, all predecessors of $k$. So the comparison is an isomorphism between $X$ and $\omega$.
:::
::::

::::exercise{#ex-double-descent-examples difficulty=1 objective="Compute a double descent ordering in a simple case, and see both parts of the lemma on double descent trees."}
Let $n$ be the finite order $0 < 1 < \cdots < n - 1$, and $\omega^*$ the reverse of the order of $\nat$. Describe $D(n)$ and $D(\omega^*)$. Show that $n * \omega^*$ is an infinite well-ordering, and that $n$ embeds into it.

:::solution
$D(n)$ is the tree of the strictly decreasing sequences of numbers below $n$: it is finite, with one node for each subset of $\{ 0, \ldots, n - 1 \}$, and its branches have length at most $n$. $D(\omega^*)$ is the tree of the strictly increasing sequences of numbers. A node of $D(n) \otimes D(\omega^*)$ of length $k$ is a pair of such sequences of length $k$; there are infinitely many nodes of length $1$, namely $\langle (a, y) \rangle$ for $a < n$ and every $y$, so $n * \omega^*$ is infinite. The product has no path, since $D(n)$ has none, so $n * \omega^*$ is a well-ordering by :ref{#lem-double-descent} (1). For the embedding, take the descending sequence $y_i = i$ of $\omega^*$ and send $m < n$ to $\sigma_m \otimes \langle 0, 1, \ldots, |\sigma_m| - 1 \rangle$, where $\sigma_m$ is the Kleene–Brouwer least decreasing sequence ending with $m$. A decreasing sequence ending with $m$ starts with some $a_0 \geq m$, and the Kleene–Brouwer ordering compares first entries first, so $\sigma_m = \langle m \rangle$; the map $m \mapsto \langle (m, 0) \rangle$ is an embedding of $n$ into $n * \omega^*$, the embedding of :ref{#lem-double-descent} (2).
:::
::::
:::::
