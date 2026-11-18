---
title: Disjunction and compactness
summary: Two measures of the strength of a problem, read off from the weakness properties it preserves; the number of hyperimmunities preserved measures disjunction (SRT²₂ and SADS do not preserve two, EM preserves countably many); preservation of constant-bound immunity measures the absence of compactness (DNR, the weakest form of compactness, does not preserve it, while CAC, ADS and COH do); a table of the principles of the course and the separations it gives.
duration: 35
prerequisites: [ads-dnr, reducibilities/preservation]
---

The previous lesson separated $\mathsf{ADS}$ from $\mathsf{DNR}$ by preserving a property built for the purpose: computing no DNC function. Research on the zoo has shown that a few families of weakness properties suffice for most separations, and that each family measures one feature of a problem. This lesson presents two of them. **Hyperimmunities** measure how *disjunctive* a problem is: whether a solution must choose one of several sides of the instance. **Constant-bound immunity** measures how much *compactness* a problem carries: whether its solutions can make a bounded choice in infinitely many places at once, as paths through trees do. The hard preservation theorems are proved in the courses on lowness and avoidance and on separation design; here we state them, derive the rest, and read the separations of the course off a single table.

## Preservation along reductions

Recall that a weakness property is a class $\mathcal W$ closed downwards under Turing reducibility, and that a problem preserves $\mathcal W$ if every instance computable in some $Z \in \mathcal W$ has a solution $Y$ with $Z \oplus Y \in \mathcal W$ (:ref{#def-weakness}). If $\mathsf Q$ preserves $\mathcal W$ and $\mathsf P$ does not, then $\mathsf Q$ does not imply $\mathsf P$ in ω-models (:ref{#thm-preservation-separation}). A problem $\mathsf P$ is **computably reducible** to $\mathsf Q$, written $\mathsf P \leq_c \mathsf Q$, if every instance $X$ of $\mathsf P$ computes an instance $\hat X$ of $\mathsf Q$ such that every solution of $\hat X$ computes, together with $X$, a solution of $X$.

:::lemma{#lem-preservation-reduction}
If $\mathsf P \leq_c \mathsf Q$ and $\mathsf Q$ preserves a weakness property $\mathcal W$, then $\mathsf P$ preserves $\mathcal W$.
:::

:::proof{of=lem-preservation-reduction}
Let $Z \in \mathcal W$ and $X \leq_T Z$ an instance of $\mathsf P$. Then $\hat X \leq_T X \leq_T Z$, so $\hat X$ has a solution $\hat Y$ with $Z \oplus \hat Y \in \mathcal W$. Some solution $Y$ of $X$ is computable in $X \oplus \hat Y \leq_T Z \oplus \hat Y$. So $Z \oplus Y \leq_T Z \oplus \hat Y$, and $Z \oplus Y \in \mathcal W$ by downward closure.
:::

The implications proved in this course are computable reductions: their proofs build, from an instance of the weaker principle, an instance of the stronger one whose solutions give solutions. For instance $\mathsf{ADS} \leq_c \mathsf{CAC} \leq_c \mathsf{RT}^2_2$ (:ref{#prop-rt22-cac-ads}), $\mathsf{COH} \leq_c \mathsf{ADS}$ (:ref{#thm-ads-coh}), $\mathsf{SADS} \leq_c \mathsf{SCAC} \leq_c \mathsf{CAC}$, $\mathsf{EM} \leq_c \mathsf{RT}^2_2$, $\mathsf{WWKL} \leq_c \mathsf{WKL}$ and $\mathsf{DNR} \leq_c \mathsf{WWKL}$ (:ref{#thm-wwkl-dnr}). So preservation results propagate downwards along the zoo, and failures of preservation propagate upwards.

## Disjunction and hyperimmunities

An instance of the pigeonhole principle splits $\nat$ into parts, and a solution must lie inside one of them. If every part is hyperimmune, a solution inside a part $A$ is sparse, and its principal function dominates that of $A$: it reveals the sparseness of the part it chose. The instance cannot prevent the solution from choosing, but it can make every choice costly. This is measured as follows (:ref{#def-sd-k-hyperimmunities}): a problem **preserves $k$ hyperimmunities** if for every set $Z$, all $Z$-hyperimmune functions $h_0, \ldots, h_{k-1}$ and every instance $X \leq_T Z$, some solution $Y$ leaves every $h_i$ hyperimmune relative to $Z \oplus Y$. For each $k$, the class of sets $W$ relative to which given functions $h_0, \ldots, h_{k-1}$ are hyperimmune is a weakness property, so these notions fit the method of preservation.

:::proposition{#prop-srt-two-hyperimmunities}
$\mathsf{SRT}^2_2$, and even $\mathsf D^2_2$, does not preserve $2$ hyperimmunities.
:::

:::proof{of=prop-srt-two-hyperimmunities}
There is a $\Delta^0_2$ set $A$ such that $A$ and $\overline A$ are hyperimmune (:ref{#lem-sd-bihyperimmune}, built by finite extensions with oracle $\emptyset'$). Let $f$ be a computable stable coloring with limit set $A$, given by a computable approximation, and $h_1 = p_A$, $h_0 = p_{\overline A}$ the principal functions, which are hyperimmune (:ref{#thm-hyperimmune-principal}). Take $Z = \emptyset$. A solution $H$ is an infinite subset of $A$ or of $\overline A$ (:ref{#prop-srt-d22}). If $H \subseteq A$, then $p_H(n) \geq p_A(n)$ for every $n$, and $p_H \leq_T H$ dominates $h_1$; if $H \subseteq \overline A$, $p_H$ dominates $h_0$. Either way, one of the two hyperimmunities is lost.
:::

Two sides of a disjunction defeat two hyperimmunities. One hyperimmunity, on the other hand, can be preserved: $\mathsf{RT}^2_2$ preserves $1$ hyperimmunity (:ref{#thm-hyperimmunity-examples}), and even $2$ among $3$, in the sense that from three given hyperimmunities a solution can keep two (:ref{#exr-rt22-two-among-three}). The number of hyperimmunities a problem preserves thus counts, roughly, how many sides its instances can force the solution to choose between.

The Erdős–Moser theorem is the opposite case. A transitive subtournament is not a choice between sides: the solution decides, element by element, how to extend a single order, and its forcing question involves no disjunction. Patey proved that $\mathsf{EM}$ preserves countably many hyperimmunities (:ref{#thm-sd-em-hyperimmunities}). So does $\mathsf{WKL}$: by the computably dominated basis theorem relativized to $Z$, a $Z$-computable binary tree has a path $Y$ such that every $(Z \oplus Y)$-computable function is dominated by a $Z$-computable one, and then every $Z$-hyperimmune function stays $(Z \oplus Y)$-hyperimmune (:ref{#exr-wkl-hyperimmunities}). Compactness, in other words, is not disjunction.

The order principles of the course sit with Ramsey's theorem on this scale. They are below $\mathsf{RT}^2_2$, so they preserve one hyperimmunity, by :ref{#lem-preservation-reduction}. The stable part of $\mathsf{ADS}$ already defeats two.

:::proposition[Patey]{#prop-sads-two-hyperimmunities}
$\mathsf{SADS}$ does not preserve $2$ hyperimmunities.
:::

**Intuition.** Restrict the bi-hyperimmune stable coloring of :ref{#prop-srt-two-hyperimmunities} to a transitive set given by $\mathsf{EM}$, which keeps both hyperimmunities. On a transitive set, the coloring is a stable linear order, whose two parts are the two sides of the coloring: the disjunction of the coloring has become the disjunction between ascending and descending sequences.

:::proof{of=prop-sads-two-hyperimmunities}
Let $A$, $f$, $h_0$, $h_1$ be as in the previous proof, and $T$ the tournament with $T(x, y) \iff f(\{ x, y \}) = 1$ for $x < y$. By :ref{#thm-sd-em-hyperimmunities}, with $Z = \emptyset$, there is an infinite transitive set $G$ such that $h_0$ and $h_1$ are $G$-hyperimmune. Let $g$ list $G$ in increasing order, and let $m <_L n$ if $T(g(m), g(n))$; this is a $G$-computable linear order. It is stable: if $g(m) \in A$, then $f(\{ g(m), y \}) = 1$ for almost every $y$, so $m <_L n$ for almost every $n$; if $g(m) \notin A$, then $n <_L m$ for almost every $n$. Let $S$ be an ascending sequence of $L$. For $m < n$ in $S$, $T(g(m), g(n))$, so $g[S]$ is homogeneous for $f$ with color $1$, hence contained in $A$ by :ref{#prop-srt-d22}, and $p_{g[S]} \leq_T G \oplus S$ dominates $h_1$. A descending sequence gives in the same way a subset of $\overline A$, which dominates $h_0$. So, with $Z = G$ and the instance $L \leq_T G$, every solution destroys one of the two $G$-hyperimmunities.
:::

By :ref{#lem-preservation-reduction}, neither $\mathsf{ADS}$, $\mathsf{SCAC}$, $\mathsf{CAC}$, $\mathsf{SRT}^2_2$ nor $\mathsf{RT}^2_2$ preserves $2$ hyperimmunities. Since $\mathsf{EM}$ preserves them, $\mathsf{EM}$ implies none of these principles in ω-models: this is the separation of Lerman, Solomon and Towsner, now read as a difference of disjunctiveness. The finer relation between $\mathsf{ADS}$ and $\mathsf{CAC}$ needs a property that couples two sets, dependent hyperimmunity, which $\mathsf{ADS}$ preserves and $\mathsf{SCAC}$ does not (:ref{#thm-sd-ads-dependent}, :ref{#cor-sd-ads-not-scac}).

:::quiz[disjunction and hyperimmunities]
In the proof of :ref{#prop-srt-two-hyperimmunities}, why does a solution inside $A$ destroy the hyperimmunity of $p_A$?

- [x] Because an infinite subset $H$ of $A$ is sparser than $A$: its $n$-th element is at least the $n$-th element of $A$, so $p_H$, which $H$ computes, dominates $p_A$.
- [ ] Because $H$ computes $A$.

  An infinite subset of $A$ need not compute $A$; it only computes a function dominating $p_A$.
- [ ] Because $A$ is $\Delta^0_2$.

  The complexity of $A$ makes the coloring computable; the domination comes from $H \subseteq A$.

---

Why does $\mathsf{WKL}$ preserve countably many hyperimmunities, although it is much stronger than $\mathsf{SADS}$ in other respects?

- [x] Because its solutions can be chosen computably dominated relative to the instance, and such a solution computes no function that grows faster than the oracle can bound; the strength of $\mathsf{WKL}$ is compactness, not disjunction.
- [ ] Because $\mathsf{WKL}$ is weaker than $\mathsf{SADS}$.

  $\mathsf{WKL}_0$ and $\mathsf{SADS}$ are incomparable: neither implies the other.
- [ ] Because binary trees have only two sides.

  A path through a binary tree makes infinitely many binary choices, but none of them is forced by the instance to cost a hyperimmunity.
:::

## Compactness and constant-bound immunity

Compactness comes in levels, studied in the course on compactness avoidance: computing a member of every non-empty $\Pi^0_1$ class ($\mathsf{WKL}$, PA degrees), of every $\Pi^0_1$ class of positive measure ($\mathsf{WWKL}$, random sequences), and computing homogeneous sets for every $\Pi^0_1$ class of positive measure, the Ramsey-type weak weak König lemma $\mathsf{RWWKL}$. The last one is equivalent to the existence of DNC functions (:ref{#prop-rwwkl-dnc}). So $\mathsf{DNR}$ is the weakest form of compactness: a DNC function makes, for each $e$, a choice that avoids one value predicted by a computation, in infinitely many places at once.

The property that detects this choice is immunity against arrays of bounded size. An infinite set $A$ is **constant-bound immune**, or c.b.-immune, if for every $k$ and every computable disjoint array $(F_n)$ of sets with at most $k$ elements each, some $F_n$ misses $A$ (:ref{#def-sd-cb-immune}). It lies between immunity and hyperimmunity: a hyperimmune set is c.b.-immune, a c.b.-immune set is immune. A compactness principle can pick, among the at most $k$ candidates of each $F_n$, one that is in $A$; a principle without compactness cannot.

:::fact[Patey]{#fact-dnc-cb-immune}
There is a $\Delta^0_2$ c.b.-immune set $A$ such that every DNC function computes an infinite subset of $A$ (:ref{#thm-sd-dnc-cb}). So $\mathsf{DNR}$ does not preserve c.b.-immunity. Neither does any principle $\mathsf P$ that implies $\mathsf{DNR}$ in ω-models: otherwise a Turing ideal satisfying $\mathsf P$ inside the weakness class would contain a DNC function, hence an infinite subset of $A$ (:ref{#lem-preservation-ideal}). This applies to $\mathsf{WWKL}$, $\mathsf{WKL}$, $\mathsf{SRT}^2_2$, $\mathsf{RT}^2_2$, and $\mathsf{EM}$, which implies $\mathsf{DNR}$ through the Ramsey-type weak König lemma.
:::

On the other side, Patey proved that $\mathsf{CAC}$ preserves c.b.-immunity (:ref{#thm-sd-cac-cb}), by forcing with an ascending, a descending and an antichain stem at once. By :ref{#lem-preservation-reduction}, so do $\mathsf{SCAC}$, $\mathsf{ADS}$, $\mathsf{SADS}$ and $\mathsf{COH}$. These principles carry no compactness at all, and the separation of :ref{#cor-ads-not-dnr} becomes a one-line consequence: $\mathsf{CAC}$ preserves c.b.-immunity and $\mathsf{DNR}$ does not, so $\mathsf{CAC}$ does not imply $\mathsf{DNR}$ in ω-models (:ref{#cor-sd-cac-not-dnc}). The proof of the previous lesson, which preserved non-DNC degrees directly, is the special case where the weakness property is tailored to $\mathsf{DNR}$; c.b.-immunity explains why it works.

Between $\mathsf{DNR}$ and $\mathsf{WWKL}$, compactness can be measured more finely, by the traces of closed classes: Liu proved that $\mathsf{RT}^2_2$ admits constant-bound trace avoidance and $\mathsf{WWKL}$ does not, so that $\mathsf{RT}^2_2$ has the compactness of DNC functions but not that of random sequences (:ref{#thm-liu-closed-classes}, :ref{#cor-rt22-not-wwkl}).

## The table of the course

| Principle | Hyperimmunities preserved | c.b.-immunity preserved | Source |
| --- | --- | --- | --- |
| $\mathsf{WKL}$, $\mathsf{WWKL}$, $\mathsf{DNR}$ | countably many | no | dominated basis; :ref{#fact-dnc-cb-immune} |
| $\mathsf{EM}$ | countably many | no | :ref{#thm-sd-em-hyperimmunities}; :ref{#fact-dnc-cb-immune} |
| $\mathsf{RT}^2_2$, $\mathsf{SRT}^2_2$ | one, not two | no | :ref{#thm-hyperimmunity-examples}; :ref{#prop-srt-two-hyperimmunities} |
| $\mathsf{CAC}$, $\mathsf{SCAC}$, $\mathsf{ADS}$, $\mathsf{SADS}$ | one, not two | yes | reduction to $\mathsf{RT}^2_2$; :ref{#prop-sads-two-hyperimmunities}; :ref{#thm-sd-cac-cb} |
| $\mathsf{COH}$ | at least one | yes | :ref{#thm-hyperimmunity-examples}; reduction to $\mathsf{ADS}$ |

The two columns are independent measures. Principles strong in compactness may be weak in disjunction ($\mathsf{WKL}$, $\mathsf{EM}$), and principles with disjunction may have no compactness (the order principles). Ramsey's theorem for pairs has both, which is why it implies the principles of both kinds, and why it splits into $\mathsf{EM}$, which carries its compactness, and $\mathsf{ADS}$, which carries its disjunction (:ref{#thm-rt22-em-ads}).

:::quiz[reading the table]
Which column separates $\mathsf{EM}$ from $\mathsf{SADS}$, and in which direction?

- [x] The hyperimmunity column: $\mathsf{EM}$ preserves two hyperimmunities and $\mathsf{SADS}$ does not, so $\mathsf{EM}$ does not imply $\mathsf{SADS}$.
- [ ] The c.b.-immunity column: $\mathsf{SADS}$ preserves c.b.-immunity and $\mathsf{EM}$ does not, so $\mathsf{EM}$ does not imply $\mathsf{SADS}$.

  This column gives the other direction: $\mathsf{SADS}$ does not imply $\mathsf{EM}$, since a principle that preserves a property cannot imply one that does not.
- [ ] Neither: the two principles are not separated by the table.

  Each column separates them in one direction, so they are incomparable.
:::

::::exercise{#ex-read-two-columns difficulty=1 objective="Derive separations from the two columns of the table, choosing the weakness property that matches the principles."}
Using the table and :ref{#thm-preservation-separation}, show that in ω-models: $\mathsf{WKL}$ does not imply $\mathsf{SADS}$; $\mathsf{SADS}$ does not imply $\mathsf{WWKL}$; $\mathsf{COH}$ does not imply $\mathsf{EM}$; $\mathsf{EM}$ does not imply $\mathsf{ADS}$. Say in each case whether the separation comes from disjunction or from compactness.

:::solution
- $\mathsf{WKL}$ preserves two hyperimmunities and $\mathsf{SADS}$ does not: disjunction. (Compare the proof by computably dominated sets in :ref{#ex-sads-hyperimmune}.)
- $\mathsf{SADS}$ preserves c.b.-immunity and $\mathsf{WWKL}$ does not: compactness.
- $\mathsf{COH}$ preserves c.b.-immunity and $\mathsf{EM}$ does not: compactness.
- $\mathsf{EM}$ preserves two hyperimmunities and $\mathsf{ADS}$ does not: disjunction.

In each case, the principle that preserves the property has a Turing ideal inside the corresponding weakness class satisfying it (:ref{#lem-preservation-ideal}), and the instance witnessing the failure of preservation for the other principle lies in that ideal without a solution there.
:::
::::

## Notes and references

The use of hyperimmunities to measure disjunction is due to Patey, who proved :ref{#prop-sads-two-hyperimmunities} and the preservation of countably many hyperimmunities by $\mathsf{EM}$ (Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, 2017; Dzhafarov–Mummert, Theorem 9.5.4). Constant-bound immunity and its preservation by $\mathsf{CAC}$ are also due to Patey, who used it to give the modern proof of the theorem of Hirschfeldt and Shore that $\mathsf{CAC}$ does not imply $\mathsf{DNR}$. The equivalence of $\mathsf{DNR}$ with $\mathsf{RWWKL}$ is due to Bienvenu, Patey and Shafer. The proofs of the preservation theorems are in the courses on separation design and compactness avoidance; the proof of :ref{#prop-sads-two-hyperimmunities} given here, through a transitive set, follows the solution of :ref{#ex-sads-not-em}.

- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221.
- L. Patey, *The weakness of being cohesive, thin or free in reverse mathematics*, Israel Journal of Mathematics 216 (2016), 905–955.
- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 9.1, 9.5 and 9.11.

:::::exercises
::::exercise{#ex-dk-hyperimmunities difficulty=2 objective="Count the hyperimmunities defeated by a disjunction with k sides."}
Let $\mathsf D^2_k$ be the statement that for every $\Delta^0_2$ partition of $\nat$ into $k$ parts, given by a computable approximation, some part has an infinite subset. Show that $\mathsf D^2_k$ does not preserve $k$ hyperimmunities.

:::solution
Build with oracle $\emptyset'$ a partition $\nat = A_0 \sqcup \cdots \sqcup A_{k-1}$ into hyperimmune parts, by finite extensions: a finite partial partition is extended to meet, for each $e$ and $i < k$, the requirement that if $\Phi_e$ is a disjoint strong array, some block of it misses $A_i$. Given the current finite partition, defined on $[0, m)$, ask $\emptyset'$ whether some $\Phi_e(n)$ converges to the canonical index of a block contained in $[m, \infty)$, a $\Sigma^0_1$ question; if $\Phi_e$ is a disjoint strong array, the answer is yes, since only finitely many of its disjoint blocks meet $[0, m)$. If so, put all the elements of that block, and the numbers below its maximum not yet placed, into $A_{i+1 \bmod k}$; then add $m$ to each part in turn, so that every part is infinite. The resulting partition is $\Delta^0_2$, and each $A_i$ is hyperimmune: every disjoint strong array has infinitely many blocks beyond any bound, and one of them was put outside $A_i$. The principal functions $h_i = p_{A_i}$ are hyperimmune. A solution $H$ is an infinite subset of some $A_i$, and $p_H \leq_T H$ dominates $h_i$. So with $Z = \emptyset$, no solution keeps all $k$ hyperimmunities. For $k = 2$ this is :ref{#prop-srt-two-hyperimmunities}.
:::
::::

::::exercise{#ex-cb-between difficulty=1 objective="Place constant-bound immunity between immunity and hyperimmunity."}
Show that a hyperimmune set is c.b.-immune, and that a c.b.-immune set is immune.

:::solution
A $k$-array is a disjoint strong array, so a hyperimmune set misses one of its blocks: it is $k$-immune for every $k$. If $A$ is not immune, it has an infinite computable subset $\{ a_0 < a_1 < \cdots \}$, and the $1$-array $F_n = \{ a_n \}$ meets $A$ at every $n$: $A$ is not $1$-immune, hence not c.b.-immune.
:::
::::

::::exercise{#ex-coh-cb-reduction difficulty=1 objective="Use the reduction lemma to transfer preservation of c.b.-immunity from ADS to COH."}
Check that the proof of :ref{#thm-ads-coh} gives $\mathsf{COH} \leq_c \mathsf{ADS}$, and deduce from :ref{#thm-sd-cac-cb} that $\mathsf{COH}$ preserves c.b.-immunity.

:::solution
Given a sequence $\vec R$, the linear order $x \leq_L y \iff \sigma_x \leq_{\mathrm{lex}} \sigma_y$ is computable in $\vec R$, and every ascending or descending sequence of it is $\vec R$-cohesive, by :ref{#thm-ads-coh}: the solution of the $\mathsf{ADS}$ instance is itself a solution of the $\mathsf{COH}$ instance. So $\mathsf{COH} \leq_c \mathsf{ADS}$. Similarly $\mathsf{ADS} \leq_c \mathsf{CAC}$ by :ref{#prop-rt22-cac-ads}. Since $\mathsf{CAC}$ preserves c.b.-immunity (:ref{#thm-sd-cac-cb}), two applications of :ref{#lem-preservation-reduction} show that $\mathsf{ADS}$, then $\mathsf{COH}$, preserve it. For each fixed set $A$, the class of sets $W$ relative to which $A$ is c.b.-immune is a weakness property, so the lemma applies.
:::
::::
:::::
