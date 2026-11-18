---
title: Σ¹₁ separation
summary: ATR₀ is equivalent over RCA₀ to Σ¹₁ separation; the forward direction ranks the nodes of trees by a transfinite recursion along a sum of Kleene–Brouwer orderings, the converse separates the true from the false instances of a hierarchy; consequently ATR₀ proves Δ¹₁ comprehension.
duration: 30
prerequisites: [well-orderings]
---

Arithmetic transfinite recursion builds sets by iterating definitions; $\Sigma^1_1$ separation builds them by separating two disjoint $\Sigma^1_1$ properties. The two principles turn out to be equivalent, and the second is often easier to use, since it does not mention well-orderings. This lesson proves the equivalence. The proof of the forward direction shows a recurring idea of the subject: a $\Sigma^1_1$ property is the existence of a path through a tree, and the absence of paths can be certified by ranking the tree into a well-ordering, which a transfinite recursion can do.

:::definition{#def-sigma11-separation}
**$\Sigma^1_1$ separation** is the scheme: for $\Sigma^1_1$ formulas $\varphi_1(n)$ and $\varphi_0(n)$, in which $Z$ does not occur, if no $n$ satisfies both, then there is a set $Z$ with $\varphi_1(n) \rightarrow n \in Z$ and $\varphi_0(n) \rightarrow n \notin Z$ for every $n$.
:::

In computability terms, the $\Sigma^1_1$ sets of numbers are separated by $\Delta^1_1$ sets, that is, by hyperarithmetic sets (Kleene's separation theorem, in the higher computability track). The scheme asks for a separating set in the model.

## Sums of well-orderings and products of trees

For a sequence of linear orders $(X_n)$, the **sum** $\sum_n X_n$ is the order on the pairs $(n, x)$ with $x \in F_{X_n}$, ordered by $n$ first, then by $\leq_{X_n}$. It exists by $\Delta^0_1$ comprehension.

:::lemma{#lem-sum-wo}
The following is provable in $\mathsf{ACA}_0$. If every $X_n$ is a well-ordering, so is $\sum_n X_n$.
:::

:::proof{of=lem-sum-wo}
Let $(n_k, x_k)$ be a descending sequence of the sum. The first coordinates are non-increasing; by arithmetic comprehension, the set of values $n_k$ exists, and its least element $m$ is reached at some $k_0$. Then $n_k = m$ for all $k \geq k_0$, and $(x_k)_{k \geq k_0}$ is a descending sequence of $X_m$, a contradiction.
:::

For trees $T, S \subseteq \nat^{<\nat}$, the **product** $T \otimes S$ is the tree of sequences of pairs $\langle (\sigma(0), \tau(0)), \ldots, (\sigma(k-1), \tau(k-1)) \rangle$ with $\sigma \in T$ and $\tau \in S$ of length $k$. A path of the product is a pair of paths. So if $T$ or $S$ has no path, neither has $T \otimes S$, and $\mathrm{KB}(T \otimes S)$ is a well-ordering by :ref{#prop-kb-aca}. And if $T$ has a path $f$, the map $\tau \mapsto (f \uh |\tau|) \otimes \tau$ sends $S$ into $T \otimes S$, and sends proper extensions to proper extensions, hence to smaller elements of the Kleene–Brouwer ordering.

## From transfinite recursion to separation

:::theorem{#thm-atr-sigma11-separation}
Over $\mathsf{RCA}_0$, $\mathsf{ATR}_0$ is equivalent to $\Sigma^1_1$ separation.
:::

**Intuition for the forward direction.** By the normal form, $\varphi_1(n)$ says that a tree $T_n$ has a path and $\varphi_0(n)$ that a tree $S_n$ has a path. Since they never both hold, the products $T_n \otimes S_n$ have no paths, and their Kleene–Brouwer orderings add up to a single well-ordering $U$. If $T_n$ has a path, $S_n$ can be ranked into $U$, by the map above. If $S_n$ has a path, it cannot be ranked into any well-ordering. A transfinite recursion along $U$ computes, for all $n$ at once, which nodes of $S_n$ have a rank in $U$; the set of $n$ whose root has one separates the two properties.

:::proof{of=thm-atr-sigma11-separation}
($\Rightarrow$) We argue in $\mathsf{ATR}_0$. Let $\varphi_1$ and $\varphi_0$ be disjoint $\Sigma^1_1$ formulas. By the normal form (:ref{#fact-kleene-normal-form}), there are sequences of trees $(T_n)$ and $(S_n)$ with $\varphi_1(n) \iff T_n$ has a path, and $\varphi_0(n) \iff S_n$ has a path. For each $n$, $T_n$ or $S_n$ has no path, so $\mathrm{KB}(T_n \otimes S_n)$ is a well-ordering, and $U = \sum_n \mathrm{KB}(T_n \otimes S_n)$ is a well-ordering by :ref{#lem-sum-wo}.

By arithmetic transfinite recursion along $U$, let $H$ be the hierarchy with
$$
H^{[u]} = \{ (n, \tau) : \tau \in S_n \text{ and for every } k \text{ with } \tau \langle k \rangle \in S_n, \ (n, \tau \langle k \rangle) \in H^{[v]} \text{ for some } v <_U u \},
$$
an arithmetic condition in $H^{[<u]}$. Let $G = \bigcup_u H^{[u]}$, and $Z$ the set of $n$ such that $S_n$ is empty or $(n, \langle\rangle) \in G$; both exist by arithmetic comprehension. Intuitively, $(n, \tau) \in H^{[u]}$ says that $\tau$ has rank at most $u$ in $S_n$.

*If $\varphi_0(n)$, then $n \notin Z$.* Let $f$ be a path of $S_n$; then $S_n$ is not empty. Suppose $(n, \langle\rangle) \in G$, and let $u_k$ be the $\leq_U$-least $u$ with $(n, f \uh k) \in H^{[u]}$, if there is one. For $k = 0$ there is one. If $u_k$ is defined, the definition of $H^{[u_k]}$, applied to the child $f \uh (k+1)$, gives some $v <_U u_k$ with $(n, f \uh (k+1)) \in H^{[v]}$; so $u_{k+1}$ is defined and $u_{k+1} <_U u_k$. The sequence $(u_k)$, which exists by arithmetic comprehension, is descending in the well-ordering $U$: a contradiction. So $(n, \langle\rangle) \notin G$ and $n \notin Z$.

*If $\varphi_1(n)$, then $n \in Z$.* Let $f$ be a path of $T_n$, and for $\tau \in S_n$ let $\rho(\tau) = (n, (f \uh |\tau|) \otimes \tau) \in F_U$. If $\tau \langle k \rangle \in S_n$, then $\rho(\tau \langle k \rangle) <_U \rho(\tau)$. We show, by arithmetic transfinite induction along $U$ (:ref{#lem-ati}), that for every $u$: every $\tau \in S_n$ with $\rho(\tau) = u$ satisfies $(n, \tau) \in H^{[u]}$. Assume it for all $v <_U u$, and let $\rho(\tau) = u$. Every child $\tau \langle k \rangle \in S_n$ has $v = \rho(\tau \langle k \rangle) <_U u$, hence $(n, \tau \langle k \rangle) \in H^{[v]}$ by hypothesis; so $(n, \tau) \in H^{[u]}$. If $S_n$ is not empty, then $\langle\rangle \in S_n$, so $(n, \langle\rangle) \in H^{[\rho(\langle\rangle)]} \subseteq G$. In both cases $n \in Z$.

So $Z$ separates $\varphi_1$ from $\varphi_0$.

($\Leftarrow$) Assume $\Sigma^1_1$ separation. It implies arithmetic comprehension: for a $\Sigma^0_1$ formula $\varphi$, both $\varphi$ and $\neg \varphi$ are $\Sigma^1_1$ (arithmetic formulas are $\Sigma^1_1$ with an empty block of set quantifiers), and a set separating them is $\{ n : \varphi(n) \}$; by :ref{#thm-aca-equivalents}, $\mathsf{ACA}_0$ follows. Now let $W$ be a well-ordering and $\theta$ arithmetic. For $j \in F_W$, write "$Y$ is a hierarchy below $j$" for "$Y$ is a $\theta$-hierarchy along $W \uh j$". Let
$$
\begin{aligned}
\varphi_1(\langle j, n \rangle) &\equiv \exists Y\, \big(Y \text{ is a hierarchy below } j \wedge \theta(n, j, Y)\big), \\
\varphi_0(\langle j, n \rangle) &\equiv \exists Y\, \big(Y \text{ is a hierarchy below } j \wedge \neg\theta(n, j, Y)\big).
\end{aligned}
$$
Both are $\Sigma^1_1$, and they are disjoint, since there is at most one hierarchy below $j$ (:ref{#prop-hierarchy-unique}). Let $Z$ separate them, and for $j \in F_W$ let $Z_j = \{ \langle i, n \rangle \in Z : i <_W j \}$, whose columns are the columns $Z^{[i]}$ of $Z$ for $i <_W j$.

We show by arithmetic transfinite induction that for every $j \in F_W$, $Z_j$ is a hierarchy below $j$ and $Z^{[j]} = \{ n : \theta(n, j, Z_j) \}$. Assume it for all $i <_W j$. Then every column of $Z_j$ satisfies the equation of the hierarchy, since $Z_i$ is the part of $Z_j$ below $i$; so $Z_j$ is a hierarchy below $j$. For each $n$, $\varphi_1(\langle j, n \rangle)$ or $\varphi_0(\langle j, n \rangle)$ holds, with witness $Y = Z_j$, according to whether $\theta(n, j, Z_j)$ holds; by the choice of $Z$, $n \in Z^{[j]}$ if and only if $\theta(n, j, Z_j)$. The set $\{ \langle j, n \rangle \in Z : j \in F_W \}$ is then a $\theta$-hierarchy along $W$.
:::

:::quiz[Σ¹₁ separation and transfinite recursion]
In the forward direction, why is the separating set defined through ranks of $S_n$ rather than through paths of $T_n$?

- [x] Because "$T_n$ has a path" is $\Sigma^1_1$ and cannot be decided by arithmetic comprehension, while the hierarchy of ranks is built by arithmetic transfinite recursion, and having a rank is then arithmetic in the hierarchy.
- [ ] Because $T_n$ never has a path.

  $T_n$ has a path exactly when $\varphi_1(n)$ holds.
- [ ] Because ranks of $T_n$ would give the same set.

  Ranking $T_n$ would require a map into $U$ when $S_n$ has a path, which the construction does not provide; the asymmetry is in the choice of $\rho$.

---

In the converse direction, where is the well-foundedness of $W$ used?

- [x] In the uniqueness of hierarchies below $j$, which makes $\varphi_1$ and $\varphi_0$ disjoint, and in the arithmetic transfinite induction that verifies the result.
- [ ] To apply $\Sigma^1_1$ separation, which needs a well-ordering.

  The scheme mentions no well-ordering.
- [ ] To show that $\varphi_1(n, j)$ is $\Sigma^1_1$.

  It is $\Sigma^1_1$ for any linear order $W$.
:::

The forward direction uses the full strength of the hypothesis only through one recursion along $U$, whose length depends on the instance. In $\mathrm{HYP}$, the ω-model of the hyperarithmetic sets, Kleene's separation theorem gives a hyperarithmetic separating set for any two disjoint $\Sigma^1_1$ sets of numbers, yet $\mathrm{HYP}$ is not a model of $\mathsf{ATR}_0$ (:ref{#prop-hyp-not-atr0}). There is no contradiction: in $\mathrm{HYP}$, the set quantifiers of a $\Sigma^1_1$ formula range over hyperarithmetic sets only, and an existential quantifier over hyperarithmetic sets defines a $\Pi^1_1$ set, by a theorem of Kleene. Two disjoint $\Pi^1_1$ sets need not be separated by a hyperarithmetic set, and this is how $\Sigma^1_1$ separation fails in $\mathrm{HYP}$.

::::exercise{#ex-delta11-ca difficulty=1 objective="Derive Δ¹₁ comprehension from Σ¹₁ separation."}
**$\Delta^1_1$ comprehension** is the scheme: if a $\Sigma^1_1$ formula $\varphi(n)$ and a $\Pi^1_1$ formula $\psi(n)$ satisfy $\varphi(n) \leftrightarrow \psi(n)$ for every $n$, then $\{ n : \varphi(n) \}$ exists. Show that $\mathsf{ATR}_0$ proves $\Delta^1_1$ comprehension.

:::solution
The formula $\neg \psi(n)$ is equivalent to a $\Sigma^1_1$ formula, and $\varphi(n) \wedge \neg \psi(n)$ never holds. By :ref{#thm-atr-sigma11-separation}, there is $Z$ with $\varphi(n) \rightarrow n \in Z$ and $\neg \psi(n) \rightarrow n \notin Z$. If $n \in Z$, then $\psi(n)$, so $\varphi(n)$. Hence $Z = \{ n : \varphi(n) \}$.
:::
::::

## Notes and references

:ref{#thm-atr-sigma11-separation} is Simpson, Theorem V.5.1, and Dzhafarov–Mummert, Theorem 5.8.20 (proved in their Section 12.1.1). Simpson derives the forward direction from Lusin's separation theorem for Borel sets, Dzhafarov and Mummert from the existence of initial segments of Kleene's $\mathcal O$ in $\mathsf{ATR}_0$ and double descent trees. The proof given here, with products of trees and a single rank hierarchy, is a streamlined version of the latter; the converse follows Simpson. $\mathsf{ATR}_0$ is strictly stronger than $\Delta^1_1$ comprehension: $\mathrm{HYP}$ is the least ω-model of $\Delta^1_1\text{-}\mathsf{CA}_0$ (Simpson, Section VIII.4), and is not a model of $\mathsf{ATR}_0$.

- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Sections V.5 and VIII.4.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 5.8 and 12.1.

:::::exercises
::::exercise{#ex-separation-wkl difficulty=1 objective="See Σ¹₁ separation as the higher analogue of Σ⁰₁ separation, and recover WKL₀ from it."}
Show that $\Sigma^1_1$ separation implies $\Sigma^0_1$ separation, and deduce that $\mathsf{ATR}_0$ proves $\mathsf{WKL}_0$ without passing through $\mathsf{ACA}_0$.

:::solution
$\Sigma^0_1$ formulas are $\Sigma^1_1$, so $\Sigma^0_1$ separation is a special case of $\Sigma^1_1$ separation. By :ref{#thm-wkl-separation}, $\Sigma^0_1$ separation is equivalent to $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$.
:::
::::

::::exercise{#ex-product-tree difficulty=1 objective="Check the properties of products of trees used in the forward direction."}
Let $T, S \subseteq \nat^{<\nat}$ be trees. Show in $\mathsf{RCA}_0$ that $T \otimes S$ is a tree, that its paths correspond to the pairs of paths of $T$ and $S$, and that for a path $f$ of $T$, $\tau \mapsto (f \uh |\tau|) \otimes \tau$ satisfies $\rho(\tau \langle k \rangle) <_{\mathrm{KB}} \rho(\tau)$.

:::solution
A prefix of a sequence of pairs built from $\sigma \in T$ and $\tau \in S$ of length $k$ is built from the prefixes of $\sigma$ and $\tau$ of the same length, which are in $T$ and $S$: the product is a tree. A path $h$ of $T \otimes S$ has $h(i) = (a_i, b_i)$, and $i \mapsto a_i$, $i \mapsto b_i$ are paths of $T$ and $S$; conversely a pair of paths gives a path. Finally $(f \uh (k+1)) \otimes \tau \langle k' \rangle$ properly extends $(f \uh k) \otimes \tau$ for $|\tau| = k$, and a proper extension is smaller in the Kleene–Brouwer ordering.
:::
::::

::::exercise{#ex-rank-hierarchy-wf difficulty=2 objective="Use the rank hierarchy to compute the well-founded part of a sequence of trees ranked into a given well-ordering."}
Let $U$ be a well-ordering and $(S_n)$ a sequence of trees, and let $H$ and $G$ be as in the proof of :ref{#thm-atr-sigma11-separation}. Show in $\mathsf{ATR}_0$ that $(n, \tau) \in G$ if and only if there is a map $\rho$ from the subtree of $S_n$ above $\tau$ to $U$ that decreases strictly along proper extensions.

:::solution
If such a map $\rho$ exists, the arithmetic transfinite induction of the proof, applied to the nodes above $\tau$, shows that every node $\tau'$ above $\tau$ is in $H^{[\rho(\tau')]}$; in particular $(n, \tau) \in G$. Conversely, suppose $(n, \tau) \in G$. For $\tau' \succeq \tau$ in $S_n$ with $(n, \tau') \in G$, let $\rho(\tau')$ be the $\leq_U$-least $u$ with $(n, \tau') \in H^{[u]}$. If $(n, \tau') \in H^{[u]}$, every child is in some $H^{[v]}$ with $v <_U u$, so every child is in $G$ and has a smaller value. By induction on the length, every node above $\tau$ is in $G$, so $\rho$ is defined on the whole subtree above $\tau$; it exists by arithmetic comprehension and decreases strictly along proper extensions.
:::
::::
:::::
