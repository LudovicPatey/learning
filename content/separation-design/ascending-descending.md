---
title: Linear orders and dependent hyperimmunity
summary: The forcing for the ascending–descending sequence principle; its question over split pairs is answered negatively only when the condition already forces one of the two negations; dependent hyperimmunity of a pair of sets; ADS preserves it.
duration: 40
prerequisites: [chain-antichain]
---

The ascending–descending sequence principle $\mathsf{ADS}$ (defined in :ref{to="separation-design/erdos-moser-hyperimmunities"}) follows from $\mathsf{CAC}$: for a linear order $<_L$, the partial order with $x \prec y$ if $x < y$ and $x <_L y$ has the ascending sequences of $<_L$ as infinite chains and its descending sequences as infinite antichains (Hirschfeldt and Shore). Its notion of forcing is the forcing of the previous lesson without the antichain side. The two questions differ in one respect. For $\mathsf{CAC}$, a negative answer was turned into an extension forcing a negation by a case analysis that may pass to an extension. For $\mathsf{ADS}$, a negative answer means that the condition itself already forces one of the two negations, without knowing which; the question is **extremal**. Extremality allows the construction to control formulas with parameters ranging over finite sets, which leads to a property of pairs of sets, dependent hyperimmunity. This lesson proves that $\mathsf{ADS}$ preserves it; :ref{to="separation-design/separating-instances"} shows that $\mathsf{CAC}$ does not, even for stable partial orders.

## The forcing

Fix a set $Z$ and a $Z$-computable linear order $<_L$ on $\nat$. Ascending and descending finite or infinite sets are defined as for partial orders (:ref{to="separation-design/chain-antichain"}), and $\rho <_L y$ means $x <_L y$ for every $x \in \rho$. An **$\mathsf{ADS}$ condition** is a triple $(\sigma_0, \sigma_1, X)$ with $X$ infinite and $Z$-computable, $\min X \geq |\sigma_0|, |\sigma_1|$, such that $\sigma_0 \cup \{ x \}$ is ascending and $\sigma_1 \cup \{ x \}$ descending for every $x \in X$. Extension and forcing of $\varphi(G_i)$ and $\neg \varphi(G_i)$ are defined through the stems, as in :ref{#def-sd-cac-condition}.

If some infinite $Z$-computable set $X$ has no $x$ with infinitely many larger $y \in X$ with $x <_L y$, the greedy construction of the previous lesson gives a $Z$-computable descending sequence; symmetrically for ascending. In that case a $Z$-computable solution exists. Otherwise, as in :ref{#lem-sd-cac-extension}, each stem can be extended by an element beyond its length; we assume this from now on.

:::definition{#def-sd-split-pair}
A **split pair** for an $\mathsf{ADS}$ condition $c = (\sigma_0, \sigma_1, X)$ is a pair of strings $(\tau_0, \tau_1)$, each $\tau_i$ compatible with $(\sigma_i, X)$, whose sets of new elements $\rho_0$, $\rho_1$ are respectively ascending and descending, with $x <_L y$ for all $x \in \rho_0$ and $y \in \rho_1$. For $\Sigma^0_1$ sentences $\varphi_0, \varphi_1$, let $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$ hold if some split pair has $\tau_0$ satisfying $\varphi_0$ and $\tau_1$ satisfying $\varphi_1$.
:::

:::lemma{#lem-sd-ads-question}
Let $c$ be an $\mathsf{ADS}$ condition and $\varphi_0, \varphi_1$ be $\Sigma^0_1$ sentences.

1. If $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, some extension of $c$ forces $\varphi_i(G_i)$ for some $i < 2$.
2. (**Extremality**) If $c \mathrel{?{\nvdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, no extension of $c$ has stems $\tau_0$ satisfying $\varphi_0$ and $\tau_1$ satisfying $\varphi_1$.
3. The relation is $\Sigma^0_1(Z)$, uniformly in the parameters of the sentences.
:::

:::proof{of=lem-sd-ads-question}
Property 3 holds since being a split pair is decidable in $X \oplus Z$ and $X \leq_T Z$.

*Property 1.* Let $(\tau_0, \tau_1)$ be a witnessing split pair, and $Y \subseteq X$ infinite, $Z$-computable, above $|\tau_0|$ and $|\tau_1|$, such that each element of $\rho_0 \cup \rho_1$ is **small** (below every $y \in Y$) or **large** (above every $y \in Y$), by finitely many applications of the pigeonhole principle; since $<_L$ is linear, there is no third case. If some $x \in \rho_0$ is large, then every $z \in \rho_1$ has $y <_L x <_L z$ for $y \in Y$, so is large, and $(\sigma_0, \tau_1, Y)$ is a condition forcing $\varphi_1(G_1)$. Otherwise every element of $\rho_0$ is small, and $(\tau_0, \sigma_1, Y)$ is a condition forcing $\varphi_0(G_0)$.

*Property 2.* Let $(\tau_0, \tau_1, Y)$ be an extension of $c$ with $\tau_i$ satisfying $\varphi_i$. For $y \in Y$, $\tau_0 \cup \{ y \}$ is ascending and $\tau_1 \cup \{ y \}$ descending, so $\rho_0 <_L y <_L \rho_1$, and $(\tau_0, \tau_1)$ is a split pair for $c$ satisfying both sentences. So the answer is positive.
:::

In the language of the previous lesson, a negative answer says that $c$ forces "$\neg \varphi_0(G_0)$ or $\neg \varphi_1(G_1)$" in the strong sense that no extension decides both sentences positively. For $\mathsf{CAC}$ this fails: in Case 1 of the proof of :ref{#lem-sd-cac-question}, the extension forcing $\neg \varphi_2(G_2)$ was obtained by first adding blocks that satisfy $\varphi_0$ and $\varphi_1$. Extremality has a consequence on generic pairs: if $G_0, G_1$ are the unions of the stems along a sequence of conditions through $c$, and $c \mathrel{?{\nvdash}} \varphi_0(G_0) \vee \varphi_1(G_1)$, then $G_0$ fails $\varphi_0$ or $G_1$ fails $\varphi_1$. Indeed, if both held, with uses below $u$, a condition far enough in the sequence would have stems of length at least $u$ on both sides, both satisfying the sentences.

:::quiz[extremality]
Why does the proof of property 2 not need any case analysis?

- [x] Because any element of the reservoir of the extension separates the two blocks in the order, so the stems of the extension already form a split pair for $c$.
- [ ] Because $X$ is computable.

  Computability of $X$ is used for property 3.
- [ ] Because the order is stable.

  The order is arbitrary.
:::

## Dependent hyperimmunity

The extremality of the question lets the construction handle formulas whose parameters are finite sets chosen later. In what follows, $U$, $V$, $R$ and $S$ range over non-empty finite sets, given by canonical indices, and $R > x$ means $\min R > x$.

:::definition{#def-sd-dependent}
A formula $\varphi(U, V)$ is **essential** if for every $x$ there is $R > x$ such that for every $y$ there is $S > y$ with $\varphi(R, S)$. A pair of sets $(A_0, A_1)$ is **dependently hyperimmune relative to $W$** if for every essential $\Sigma^0_1(W)$ formula $\varphi(U, V)$, there are $R \subseteq \overline{A_0}$ and $S \subseteq \overline{A_1}$ with $\varphi(R, S)$. A problem $\mathsf P$ admits **preservation of dependent hyperimmunity** if for every $Z$, every pair dependently hyperimmune relative to $Z$ and every instance $X \leq_T Z$, there is a solution $Y$ such that the pair is dependently hyperimmune relative to $Z \oplus Y$.
:::

An essential formula describes a game in which finite sets $R$ and $S$ can be found arbitrarily far, $S$ depending on $R$. Dependent hyperimmunity says that such a formula can always be satisfied with $R$ outside $A_0$ and $S$ outside $A_1$: neither set can be approximated by blocks, even when the blocks for $A_1$ are chosen after those for $A_0$. For a fixed pair, the class of sets $W$ relative to which it is dependently hyperimmune is a weakness property.

:::example{#ex-sd-dependent}
Let $(A_0, A_1)$ be dependently hyperimmune, and $(F_n)$ a disjoint strong array of non-empty sets. The formula "$U = F_n$ for some $n$", with $V$ arbitrary, is $\Sigma^0_1$ and essential, since $\min F_n \to \infty$. So some $F_n$ is disjoint from $A_0$. Hence $A_0$, and symmetrically $A_1$, has no disjoint strong array of non-empty sets all meeting it: each is hyperimmune if infinite.
:::

:::theorem[Patey]{#thm-sd-ads-dependent}
$\mathsf{ADS}$ admits preservation of dependent hyperimmunity.
:::

:::proof{of=thm-sd-ads-dependent}
Let $(A_0, A_1)$ be dependently hyperimmune relative to $Z$ and $<_L$ a $Z$-computable linear order. If it has a $Z$-computable solution we are done; otherwise build a decreasing sequence of $\mathsf{ADS}$ conditions, handling infinitely often the growth of each side and, for each pair of $\Sigma^0_1$ formulas $\varphi_0(G, U, V)$ and $\varphi_1(G, U, V)$ with oracle $Z \oplus G$, the following task. Let $c$ be the current condition, and let $\psi(U, V)$ say that there are $U_0, U_1 \subseteq U$ and $V_0, V_1 \subseteq V$ with
$$
c \mathrel{?{\vdash}} \varphi_0(G_0, U_0, V_0) \vee \varphi_1(G_1, U_1, V_1).
$$
It is $\Sigma^0_1(Z)$ by property 3.

- If $\psi$ is essential, dependent hyperimmunity relative to $Z$ gives $R \subseteq \overline{A_0}$ and $S \subseteq \overline{A_1}$ with $\psi(R, S)$, witnessed by $U_i \subseteq R$ and $V_i \subseteq S$. Property 1 gives an extension forcing $\varphi_i(G_i, U_i, V_i)$ for some $i$, with $U_i \subseteq \overline{A_0}$ and $V_i \subseteq \overline{A_1}$.
- If $\psi$ is not essential, keep $c$.

Let $G_0, G_1$ be the unions of the stems: an ascending and a descending sequence. We claim that for each pair $(\varphi_0, \varphi_1)$, some side $i$ has $\varphi_i(G_i, U, V)$ not essential or satisfied by some $R \subseteq \overline{A_0}$ and $S \subseteq \overline{A_1}$. In the first case of the task this holds on side $i$. In the second case, $\psi$ is not essential: there is $x$ such that for every $R > x$ there is $y_R$ such that $\neg \psi(R, S)$ for every $S > y_R$. Suppose both $\varphi_i(G_i, U, V)$ essential. For each $i$, take $R_i > x$ such that for every $y$ some $S > y$ has $\varphi_i(G_i, R_i, S)$. Let $R = R_0 \cup R_1$, and for each $i$ take $S_i > y_R$ with $\varphi_i(G_i, R_i, S_i)$, and $S = S_0 \cup S_1$. By extremality and the remark after :ref{#lem-sd-ads-question}, $c \mathrel{?{\vdash}} \varphi_0(G_0, R_0, S_0) \vee \varphi_1(G_1, R_1, S_1)$, so $\psi(R, S)$ holds with $R > x$ and $S > y_R$, a contradiction.

By Lachlan's disjunction, some side $i$ satisfies this for every formula: if each side had a counterexample $\varphi_i$, the pair $(\varphi_0, \varphi_1)$ would contradict the claim. Then $(A_0, A_1)$ is dependently hyperimmune relative to $Z \oplus G_i$.
:::

:::quiz[dependent hyperimmunity]
In the second case of the proof, why is the question applied to the parameters $(R_0, S_0)$ and $(R_1, S_1)$ rather than to a single pair $(R, S)$?

- [x] Because each side has its own witnesses of essentiality, found from $G_0$ and $G_1$ separately; the formula $\psi$ quantifies over subsets of $U$ and $V$ precisely so that the two pairs of witnesses can be merged into $(R, S)$.
- [ ] Because $R_0$ and $R_1$ are disjoint.

  They need not be.
- [ ] Because the question is not compact.

  Compactness plays no role here; the point is the dependency of $S$ on $R$.

---

Where is extremality used, and why would the proof fail with the question of $\mathsf{CAC}$?

- [x] To conclude from "$G_0$ and $G_1$ satisfy the sentences" that the question at $c$ is positive; with $\mathsf{CAC}$, a negative answer only gives some extension forcing a negation, and the generic sets need not pass through it.
- [ ] To find $R \subseteq \overline{A_0}$.

  This uses dependent hyperimmunity relative to $Z$, in the first case.
- [ ] To make $G_0$ ascending.

  This comes from the definition of the conditions.
:::

The first case is the usual use of the question; the second case is new. The construction does not act on a non-essential $\psi$: it could not, since essentiality is a property of high arithmetic complexity, decided by no single extension. Extremality makes the condition $c$ itself responsible for the behavior of the generic pair, whatever extensions are chosen later.

## Exercises

::::exercise{difficulty=2}
Let $(A_0, A_1)$ be a pair with $A_0 \cup A_1 = \nat$, and $H$ an infinite set contained in $A_0$ or in $A_1$. Show that $(A_0, A_1)$ is not dependently hyperimmune relative to $H$. Deduce that if $A_0 \sqcup A_1 = \nat$ is a partition and $(A_0, A_1)$ is dependently hyperimmune, then $A_0$ and $A_1$ are both infinite.

:::solution
The formula "$U \cup V \subseteq H$" is $\Sigma^0_1(H)$, even decidable in $H$, and essential since $H$ is infinite: take $R = \{ h \}$ with $h \in H$, $h > x$, and $S = \{ h' \}$ with $h' \in H$, $h' > y$. If $H \subseteq A_0$, a set $R \subseteq H$ is contained in $A_0$, so not in $\overline{A_0}$ (it is non-empty). If $H \subseteq A_1$, the same holds for $S$. For the second statement, if $A_1$ were finite, $A_0$ would be cofinite, hence an infinite computable set; the first part with $H = A_0$ gives a $\Sigma^0_1$ formula, without oracle, witnessing that the pair is not dependently hyperimmune. The same holds if $A_0$ is finite.
:::
::::

## Notes and references

The notion of forcing, extremal questions, dependent hyperimmunity and :ref{#thm-sd-ads-dependent} are due to Patey (2018), and follow the section *Linear orders* of the chapter *Custom properties* of his monograph; the terminology "essential" comes from Lerman, Solomon and Towsner (2013), who first separated $\mathsf{ADS}$ from $\mathsf{CAC}$. The reduction of $\mathsf{ADS}$ to $\mathsf{CAC}$ is due to Hirschfeldt and Shore (2007; Hirschfeldt, *Slicing the Truth*, Exercise 9.3). The monograph also states an abstract version: a $\Sigma^0_1$-preserving extremal question preserves dependent hyperimmunity.

- L. Patey, *Partial orders and immunity in reverse mathematics*, Computability 7 (2018), 323–339.
- M. Lerman, R. Solomon and H. Towsner, *Separating principles below Ramsey's theorem for pairs*, Journal of Mathematical Logic 13 (2013), 1350007.
- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- L. Patey, *Lowness and avoidance*, chapter *Custom properties*, section *Linear orders*.
