---
title: The Erdős–Moser theorem and several hyperimmunities
summary: Reservoirs in a Scott ideal; the Erdős–Moser theorem avoids cones and preserves countably many hyperimmunities, Ramsey's theorem for pairs does not preserve two; RT²₂ is EM plus ADS.
duration: 45
prerequisites: [erdos-moser-design, avoidance/hyperimmunities, turing-degrees/limit-computability]
---

This lesson completes the design of the previous one with its third step, the choice of the reservoirs, and separates $\mathsf{EM}$ from Ramsey's theorem for pairs. The separating property is read off one feature of the question: it is not disjunctive. A construction for Ramsey's theorem for pairs satisfies each requirement on one of two sides that it does not choose, so two families of requirements may end up satisfied on different sides; a construction for $\mathsf{EM}$ satisfies every requirement on the set it builds.

## Step 3: computational properties

The three-case argument of :ref{to="avoidance/forcing-question-method"} compares the answers of the question with the property to be preserved; since they are $\Sigma^0_1(X \oplus Z)$, the reservoirs $X$ must themselves be weak. The operations performed on reservoirs are restrictions computable in $X \oplus Z$ (:ref{#lem-sd-em-extension} and property 1 of the question), and the choice of a member of a non-empty $\Pi^0_1(X \oplus Z)$ class, followed by a restriction computable from it (property 2). So the reservoirs can be taken in any Scott ideal $\mathcal M$ containing $Z$, and if a weakness property $\mathcal W$ is preserved by $\mathsf{WKL}$, there is such an ideal inside $\mathcal W$ (:ref{#lem-scott-preservation}). The pigeonhole principle used in the restrictions is computably true and imposes nothing. As in most designs, the reservoirs must have the property the solution should have, with closure conditions given by the list of operations.

:::theorem{#thm-sd-em-cone}
Let $Z$ be a set and $C \not\leq_T Z$. Every $Z$-computable tournament $T$ has an infinite transitive set $G$ with $C \not\leq_T Z \oplus G$. So $\mathsf{EM}$ admits cone avoidance.
:::

:::proof{of=thm-sd-em-cone}
Let $\mathcal M$ be a Scott ideal containing $Z$ and not $C$ (:ref{#lem-scott-cone}), and use $\mathsf{EM}$ conditions with reservoirs in $\mathcal M$. Starting from $(\varepsilon, \nat)$, build a decreasing sequence $c_0 \geq c_1 \geq \cdots$, handling infinitely often each of the following tasks.

- *Growth.* Pass from $(\sigma, X)$ to the extension of :ref{#lem-sd-em-extension} for $x = \min X$; its reservoir is computable in $X \oplus Z$, hence in $\mathcal M$.
- *Requirement $e$.* For the current condition $c = (\sigma, X)$, let $U$ be the set of pairs $(x, v)$ with $v < 2$ and $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge = v$, a $\Sigma^0_1(X \oplus Z)$ set. If $(x, 1 - C(x)) \in U$ for some $x$, property 1 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\converge = 1 - C(x)$. If $(x, C(x)) \notin U$ for some $x$, property 2 gives an extension forcing that $\Phi^{Z \oplus G}_e(x)$ does not converge to $C(x)$. Otherwise $U$ is the graph of $C$, and $C \leq_T X \oplus Z \in \mathcal M$, which is excluded.

Let $G$ be the union of the stems. It is infinite by the growth task, and transitive since every finite subset lies in a stem. It is a member of every $c_s$: it extends the stem of $c_s$, and its later elements come from later reservoirs, contained in that of $c_s$. So $\Phi^{Z \oplus G}_e \neq C$ for every $e$.
:::

This is the argument of :ref{#thm-local-cone-avoidance} along a sequence of conditions; the abstract theorem does not apply verbatim, since $\mathsf{EM}$ conditions lack the refinement property of :ref{#def-forcing-notion} (:ref{#ex-sd-em-block}).

## Several hyperimmunities

:::definition{#def-sd-k-hyperimmunities}
Let $1 \leq k \leq \omega$. A problem $\mathsf P$ admits **preservation of $k$ hyperimmunities** if for every set $Z$, every sequence $(h_i)_{i < k}$ of $Z$-hyperimmune functions and every instance $X \leq_T Z$, there is a solution $Y$ such that every $h_i$ is $(Z \oplus Y)$-hyperimmune.
:::

For $k = 1$ this is :ref{#def-preserve-hyperimmunity}. For a fixed sequence $(h_i)$, the class $\mathcal W_{\vec h}$ of sets $W$ such that every $h_i$ is $W$-hyperimmune is a weakness property, and preservation of $k$ hyperimmunities is the preservation of all these classes. $\mathsf{WKL}$ preserves them for $k = \omega$ (first exercise). By :ref{#thm-hyperimmunity-examples}, $\mathsf{RT}^2_2$ admits preservation of one hyperimmunity. The proof uses a disjunctive question: for a pair of indices, some side $G_i$ satisfies "$\Phi^{Z \oplus G_i}_{e_i}$ does not dominate $h$", and Lachlan's disjunction gives one side satisfying all the requirements. With two functions $h_0$ and $h_1$, the requirements for $h_0$ may be satisfied on side $0$ and those for $h_1$ on side $1$, and nothing forces a common side. For $\mathsf{EM}$ the question is not disjunctive.

:::lemma{#lem-sd-em-compact}
Let $\mathcal M$ be a Scott ideal containing $Z$. The question of :ref{#lem-sd-em-question} is compact: if $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge$, there is $k$ with $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge < k$.
:::

:::proof{of=lem-sd-em-compact}
In the proof of :ref{#lem-sd-em-question}, a positive answer gives a bound $\ell$ such that for every string $\beta$ of length $\ell$ there is a witness $(i, \tau)$ with $|\tau| \leq \ell$ and $\Phi^{Z \oplus \tau}_e(x)[\ell]\converge$. There are finitely many such pairs; let $k$ exceed all the values $\Phi^{Z \oplus \tau}_e(x)[\ell]$. For every set $B$, the witness for $B \uh \ell$ is a witness for the sentence $\Phi^{Z \oplus G}_e(x)\converge < k$.
:::

:::theorem[Patey]{#thm-sd-em-hyperimmunities}
$\mathsf{EM}$ admits preservation of $\omega$ hyperimmunities: for every set $Z$, every sequence $(h_i)_{i \in \nat}$ of $Z$-hyperimmune functions and every $Z$-computable tournament $T$, there is an infinite transitive set $G$ such that every $h_i$ is $(Z \oplus G)$-hyperimmune.
:::

:::proof{of=thm-sd-em-hyperimmunities}
By the first exercise and :ref{#lem-scott-preservation}, there is a Scott ideal $\mathcal M$ containing $Z$ such that every $h_i$ is $X$-hyperimmune for every $X \in \mathcal M$. Build a sequence of $\mathsf{EM}$ conditions with reservoirs in $\mathcal M$ as in :ref{#thm-sd-em-cone}, with the growth task and, for each pair $(e, i)$, the following task. Let $c = (\sigma, X)$ be the current condition.

- If $c \mathrel{?{\nvdash}} \Phi^{Z \oplus G}_e(x)\converge$ for some $x$, property 2 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\diverge$.
- Otherwise, by :ref{#lem-sd-em-compact}, for every $x$ there is $k$ with $c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge < k$. Let $g(x)$ be the first such $k$ found in an enumeration of these pairs computable in $X \oplus Z$; $g$ is total and $(X \oplus Z)$-computable. Since $X \oplus Z \in \mathcal M$, $h_i$ is $(X \oplus Z)$-hyperimmune, so $g(x) < h_i(x)$ for some $x$, and property 1 gives an extension forcing $\Phi^{Z \oplus G}_e(x)\converge < g(x)$.

In both cases every member $G$ of the extension has $\Phi^{Z \oplus G}_e$ partial or below $h_i$ at some point, so $\Phi^{Z \oplus G}_e$ does not dominate $h_i$. The union $G$ of the stems is an infinite transitive set and a member of every condition of the sequence, so no $\Phi^{Z \oplus G}_e$ dominates any $h_i$.
:::

:::quiz[several hyperimmunities]
Why can the requirements for all the functions $h_i$ be satisfied by the same set $G$?

- [x] Because each extension given by the question acts on the set being built, not on a side chosen by the question; the requirements are conjunctive, and a sequence of conditions can handle them all.
- [ ] Because the functions $h_i$ are hyperimmune relative to a common Scott ideal.

  This is needed for each requirement; for $\mathsf{RT}^2_2$ such an ideal exists too.
- [ ] Because the question is compact.

  The Seetapun question is compact too.

---

Where is the Scott ideal used in the proof of :ref{#thm-sd-em-hyperimmunities}?

- [x] In property 2 of the question, for a partition in $\mathcal M$ witnessing a negative answer; and in the second case, to know that $h_i$ is hyperimmune relative to $X \oplus Z$.
- [ ] To make $g$ total.

  Totality comes from the positive answers for every $x$.
- [ ] Only in the growth task.

  The growth task only needs closure under computability in $X \oplus Z$.
:::

## Ramsey's theorem for pairs does not preserve two hyperimmunities

The separating instance comes from a $\Delta^0_2$ partition of $\nat$ into two hyperimmune sets, through a stable coloring.

:::lemma{#lem-sd-bihyperimmune}
There is a $\Delta^0_2$ set $A$ such that $A$ and $\overline A$ are hyperimmune.
:::

:::proof{of=lem-sd-bihyperimmune}
Write $A^0 = A$ and $A^1 = \overline A$. We build $A$ by finite extensions with oracle $\emptyset'$, satisfying for each $e$ and $i < 2$ the requirement: if $\Phi_e$ is a disjoint strong array $(F_n)$, then $F_n \cap A^i = \emptyset$ for some $n$. Given the current string $\sigma$, ask $\emptyset'$ whether there is $n$ with $\Phi_e(n)\converge$ and $F_n$ empty or $\min F_n \geq |\sigma|$, a $\Sigma^0_1$ question. If so, extend $\sigma$ so that the elements of $F_n$ are outside $A^i$, the positions in between being set to $0$. If not, $\Phi_e$ is not a disjoint strong array: a total sequence of pairwise disjoint finite sets has only finitely many members meeting $[0, |\sigma|)$. Then add one element to $A$ and one to $\overline A$. The construction is computable in $\emptyset'$, so $A$ is $\Delta^0_2$; $A$ and $\overline A$ are infinite, and every requirement is satisfied.
:::

:::proposition{#prop-sd-rt22-two}
There are two hyperimmune functions $h_0, h_1$ and a computable stable coloring $f : [\nat]^2 \to 2$ such that, for each $i < 2$, $h_i$ is not $H$-hyperimmune for any infinite set $H$ homogeneous for $f$ with color $i$. So $\mathsf{RT}^2_2$, and even its restriction $\mathsf{SRT}^2_2$ to stable colorings, does not admit preservation of $2$ hyperimmunities.
:::

:::proof{of=prop-sd-rt22-two}
Let $A$ be as in :ref{#lem-sd-bihyperimmune}, with a computable approximation $(A_s)$ (:ref{#thm-limit-lemma}), and let $f(\{ x, y \}) = A_y(x)$ for $x < y$. It is computable and stable, with limit $\lim_y f(\{ x, y \}) = A(x)$. Let $h_1 = p_A$ and $h_0 = p_{\overline A}$, the principal functions; they are hyperimmune by :ref{#thm-hyperimmune-principal}. If $H$ is infinite and homogeneous with color $1$, every $x \in H$ has $f(\{ x, y \}) = 1$ for the infinitely many $y > x$ in $H$, so $A(x) = 1$: $H \subseteq A$. Then $p_H(n) \geq p_A(n)$ for every $n$, and $p_H$, computable in $H$, dominates $h_1$. The case of color $0$ is symmetric.
:::

:::corollary[Lerman, Solomon, Towsner]{#cor-sd-em-not-srt22}
$\mathsf{SRT}^2_2 \not\leq_\omega \mathsf{EM}$: there is an ω-model of $\mathsf{RCA}_0 + \mathsf{EM}$ that is not a model of $\mathsf{SRT}^2_2$, hence not of $\mathsf{RT}^2_2$.
:::

:::proof{of=cor-sd-em-not-srt22}
Let $h_0, h_1$ be as in :ref{#prop-sd-rt22-two} and $\mathcal W$ the class of sets $W$ such that $h_0$ and $h_1$ are $W$-hyperimmune. By :ref{#thm-sd-em-hyperimmunities}, $\mathsf{EM}$ preserves $\mathcal W$. The set $\emptyset$ belongs to $\mathcal W$ and computes the stable coloring $f$, every solution $H$ of which has $H \notin \mathcal W$. So $\mathsf{SRT}^2_2$ does not preserve $\mathcal W$, and :ref{#thm-preservation-separation} applies.
:::

Cone avoidance, PA avoidance and preservation of one hyperimmunity, which both problems admit, do not see this separation; it only uses that the question of $\mathsf{RT}^2_2$ chooses its side.

## Ramsey's theorem as a conjunction

Let $\mathcal L = (\nat, <_{\mathcal L})$ be a linear order. As in :ref{to="lowness/weak-preservation"}, an **ascending sequence** is an infinite set on which $<_{\mathcal L}$ agrees with the order of $\nat$, and a **descending sequence** an infinite set on which it agrees with the reverse order. The **ascending–descending sequence principle** $\mathsf{ADS}$ is the problem whose instances are the linear orders on $\nat$ and whose solutions are their ascending and descending sequences; it is studied in :ref{to="separation-design/ascending-descending"}.

:::proposition{#prop-sd-rt22-em-ads}
A Turing ideal satisfies $\mathsf{RT}^2_2$ if and only if it satisfies $\mathsf{EM}$ and $\mathsf{ADS}$.
:::

:::proof{of=prop-sd-rt22-em-ads}
($\Rightarrow$) By :ref{#prop-sd-em-rt22}, and since a linear order $\mathcal L$ computes the coloring with $f(\{ x, y \}) = 1$ if and only if $x <_{\mathcal L} y$, for $x < y$, whose homogeneous sets are ascending (color $1$) or descending (color $0$). ($\Leftarrow$) Let $f$ be a coloring in the ideal, and $T$ the tournament with $T(x, y)$ if and only if $f(\{ x, y \}) = 1$, for $x < y$. Let $H$ be an infinite transitive set in the ideal, $h$ its enumeration in increasing order, and $\mathcal L$ the linear order on $\nat$ with $m <_{\mathcal L} n$ if and only if $T(h(m), h(n))$; it belongs to the ideal. Let $S$ be an ascending or descending sequence of $\mathcal L$ in the ideal. If $S$ is ascending, then for $m < n$ in $S$, $T(h(m), h(n))$ with $h(m) < h(n)$, so $f(\{ h(m), h(n) \}) = 1$; so $h[S]$ is homogeneous with color $1$. If $S$ is descending, $h[S]$ is homogeneous with color $0$.
:::

:::corollary[Lerman, Solomon, Towsner]{#cor-sd-ads-not-em}
$\mathsf{ADS} \not\leq_\omega \mathsf{EM}$.
:::

:::proof{of=cor-sd-ads-not-em}
Otherwise every Turing ideal satisfying $\mathsf{EM}$ would satisfy $\mathsf{ADS}$, hence $\mathsf{RT}^2_2$ by :ref{#prop-sd-rt22-em-ads}, contradicting :ref{#cor-sd-em-not-srt22}.
:::

So Ramsey's theorem for pairs splits into a part about transitivity and a part about orders. The first has the compactness of $\mathsf{RT}^2_2$: $\mathsf{EM}$ implies the Ramsey-type weak König lemma, by a theorem of Bienvenu, Patey and Shafer, and of Flood and Towsner, which we admit. The second has none, as :ref{to="separation-design/ascending-descending"} shows.

## Exercises

::::exercise{difficulty=1}
Let $(h_i)_{i \in \nat}$ be functions that are $Z$-hyperimmune. Show that every infinite $Z$-computable binary tree has a path $P$ such that every $h_i$ is $(Z \oplus P)$-hyperimmune. Deduce that $\mathsf{WKL}$ preserves $\mathcal W_{\vec h}$.

:::solution
By the computably dominated basis theorem (:ref{#thm-dominated-basis}) relativized to $Z$, the tree has a path $P$ such that every $(Z \oplus P)$-computable function is dominated by a $Z$-computable function. If a $(Z \oplus P)$-computable function $g$ dominated $h_i$, a $Z$-computable function dominating $g$ would dominate $h_i$. Given $W \in \mathcal W_{\vec h}$ and a $W$-computable tree, apply this with $Z = W$.
:::
::::

## Notes and references

The separation of $\mathsf{EM}$ from $\mathsf{RT}^2_2$ through preservation of hyperimmunities follows the section *Erdős–Moser theorem* of the chapter *Custom properties* of Patey's monograph, and Patey (2017), who proves :ref{#thm-sd-em-hyperimmunities} and :ref{#prop-sd-rt22-two}; the question with partitions is the one of the monograph's chapter *Custom properties*. The separation itself is due to Lerman, Solomon and Towsner (2013), with an iterated forcing; their result gives an ω-model of $\mathsf{EM}$ that is not a model of $\mathsf{SRT}^2_2$ (Hirschfeldt, *Slicing the Truth*, Theorem 9.31). The decomposition $\mathsf{RT}^2_2 \leftrightarrow \mathsf{EM} \wedge \mathsf{ADS}$ over $\mathsf{RCA}_0$ is Exercise 9.30 of Hirschfeldt, "noted by several people", and is attributed to Montalbán by Bovykin and Weiermann (2017). That $\mathsf{EM}$ implies $\mathsf{RWKL}$ is due to Bienvenu, Patey and Shafer (2017), and independently to Flood and Towsner (2016).

- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- M. Lerman, R. Solomon and H. Towsner, *Separating principles below Ramsey's theorem for pairs*, Journal of Mathematical Logic 13 (2013), 1350007.
- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71.
- S. Flood and H. Towsner, *Separating principles below WKL₀*, Mathematical Logic Quarterly 62 (2016).
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Section 9.2.
- L. Patey, *Lowness and avoidance*, chapters *Custom properties* and *Forcing design*.
