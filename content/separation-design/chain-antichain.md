---
title: Partial orders and constant-bound immunity
summary: The chain–antichain principle; forcing with an ascending, a descending and an antichain stem over a computable reservoir; split triples; preservation of constant-bound immunity.
duration: 40
prerequisites: [erdos-moser-hyperimmunities, avoidance/disjunctive-question]
---

The chain–antichain principle is a consequence of Ramsey's theorem for pairs without any compactness. Its notion of forcing has computable reservoirs, and its forcing question has a feature that the questions of $\mathsf{WKL}$, $\mathsf{RT}^2_2$ and $\mathsf{EM}$ lack: a positive answer about an existential sentence is witnessed by one value on each of three sides. By the method of :ref{to="separation-design/custom-properties"}, this feature becomes a property, constant-bound immunity, which $\mathsf{CAC}$ preserves; :ref{to="separation-design/separating-instances"} shows that $\mathsf{DNC}$, hence $\mathsf{RT}^2_2$, does not.

## Partial orders

A **partial order** on $\nat$ is a relation $<_P$ that is irreflexive and transitive. Elements $x, y$ are **comparable** if $x <_P y$ or $y <_P x$, and **incomparable**, written $x \mid_P y$, otherwise. A set is a **chain** if any two of its elements are comparable, and an **antichain** if any two distinct elements are incomparable. A set $S$, finite or infinite, is **ascending** if $x <_P y$ for all $x < y$ in $S$, and **descending** if $y <_P x$ for all $x < y$ in $S$; ascending and descending sets are chains. The **chain–antichain principle** $\mathsf{CAC}$ is the problem whose instances are the partial orders on $\nat$, and whose solutions are their infinite chains and antichains.

Coloring pairs by comparability gives $\mathsf{CAC} \leq_{sc} \mathsf{RT}^2_2$. Building a chain directly is awkward, since the comparabilities of a block with the future are unordered; building an ascending sequence, a descending sequence and an antichain at once is better behaved.

Fix a set $Z$ and a $Z$-computable partial order $<_P$. We write $\rho <_P y$ if $x <_P y$ for every $x \in \rho$, and similarly $y <_P \rho$ and $\rho \mid_P y$. Strings are identified with finite sets, and compatibility with a pair $(\sigma, X)$ is defined as in :ref{to="separation-design/erdos-moser-design"}. Side $0$ builds an ascending set, side $1$ a descending set, side $2$ an antichain.

:::definition{#def-sd-cac-condition}
A **$\mathsf{CAC}$ condition** is a tuple $c = (\sigma_0, \sigma_1, \sigma_2, X)$ with $X$ infinite and $Z$-computable, $\min X \geq |\sigma_i|$ for each $i$, such that for every $x \in X$, the sets $\sigma_0 \cup \{ x \}$, $\sigma_1 \cup \{ x \}$ and $\sigma_2 \cup \{ x \}$ are respectively ascending, descending and an antichain. A condition $(\tau_0, \tau_1, \tau_2, Y)$ **extends** $c$ if $Y \subseteq X$ and each $\tau_i$ is compatible with $(\sigma_i, X)$. For a $\Sigma^0_1$ sentence $\varphi$, $c$ **forces $\varphi(G_i)$** if $\sigma_i$ satisfies $\varphi$, and **forces $\neg \varphi(G_i)$** if no extension of $c$ has a stem on side $i$ satisfying $\varphi$.
:::

Forcing is defined through the stems, since the negative answers below are not witnessed by a restriction of the reservoir. Along a decreasing sequence of conditions whose stems grow, let $G_i$ be the union of the stems on side $i$. If $c_s$ forces $\varphi(G_i)$, $G_i$ satisfies $\varphi$ by the use principle. If $c_s$ forces $\neg \varphi(G_i)$ and $G_i$ satisfied $\varphi$ with use $u$, the stem on side $i$ of some later $c_t$, of length at least $u$, would satisfy $\varphi$. So $G_i$ satisfies what is forced.

If $\rho \subseteq X$ is ascending, so is $\sigma_0 \cup \rho$, since each $\sigma_0 \cup \{ y \}$ is; similarly on the other sides.

## Extendibility

Say that $x < y$ are in the **relation of side $i$** if $x <_P y$ ($i = 0$), $y <_P x$ ($i = 1$) or $x \mid_P y$ ($i = 2$). We assume:

(H) for every infinite $Z$-computable set $X$ and every $i < 3$, some $x \in X$ has infinitely many $y > x$ in $X$ in the relation of side $i$.

If (H) fails for $X$ and $i$, each $x \in X$ is in the relation of side $i$ with finitely many larger elements of $X$, and choosing greedily $y_{n+1}$, the least element of $X$ above $y_n$ in that relation with no $y_j$, gives an infinite $Z$-computable $Y \subseteq X$ without pairs of type $i$; the construction restarts inside $Y$ without side $i$ (:ref{#ex-cac-degenerate}).

:::lemma{#lem-sd-cac-extension}
Assume (H). For every condition $c = (\sigma_0, \sigma_1, \sigma_2, X)$ and $i < 3$, there is an extension of $c$ whose stem on side $i$ has an element beyond $|\sigma_i|$.
:::

:::proof{of=lem-sd-cac-extension}
Say $i = 0$. By (H), some $x \in X$ has infinitely many $y > x$ in $X$ with $x <_P y$; let $Y$ be the set of these $y$, which is $Z$-computable. Then $\sigma_0 \cup \{ x \}$ is ascending, and for $y \in Y$, $\sigma_0 \cup \{ x, y \}$ is ascending, since $\sigma_0 \cup \{ y \}$ is and $x <_P y$ with $x < y$. The other sides are unchanged and $Y \subseteq X$. Sides $1$ and $2$ are symmetric.
:::

## Split triples

A block added on side $0$ must stay below all future elements, on side $1$ above them, on side $2$ incomparable with them, and the future is unknown. The question asks for three blocks related so that, whatever the future, one of them can be added.

:::definition{#def-sd-split-triple}
Let $c = (\sigma_0, \sigma_1, \sigma_2, X)$ be a condition. A **split triple** for $c$ is a triple of strings $(\tau_0, \tau_1, \tau_2)$, each $\tau_i$ compatible with $(\sigma_i, X)$, whose sets of new elements $\rho_0, \rho_1, \rho_2$ are respectively ascending, descending and an antichain, and satisfy $x <_P z <_P y$ for all $x \in \rho_0$, $z \in \rho_2$ and $y \in \rho_1$. For $\Sigma^0_1$ sentences $\varphi_0, \varphi_1, \varphi_2$, let $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1) \vee \varphi_2(G_2)$ hold if some split triple $(\tau_0, \tau_1, \tau_2)$ has $\tau_i$ satisfying $\varphi_i$ for every $i < 3$.
:::

:::figure[A split triple. The new block $\rho_0$ of the ascending side lies below the antichain block $\rho_2$, which lies below the descending block $\rho_1$. After the reservoir is thinned, each element of $\rho_2$ is below, above or incomparable with all of it. If an element of $\rho_2$ is below the reservoir, so is all of $\rho_0$; if one is above, so is all of $\rho_1$; otherwise $\rho_2$ is incomparable with the reservoir.]
<svg class="fig" viewBox="0 0 600 270" width="600" role="img" aria-label="A split triple: an ascending block at the bottom, an antichain block in the middle, a descending block at the top; every element of a lower block is below every element of a higher block in the partial order"><text x="60" y="225" text-anchor="middle" class="math" font-size="14">ρ<tspan class="mrm" font-size="10" dy="3">0</tspan></text><text x="420" y="225" class="label">ascending</text><text x="60" y="145" text-anchor="middle" class="math" font-size="14">ρ<tspan class="mrm" font-size="10" dy="3">2</tspan></text><text x="420" y="145" class="label">antichain</text><text x="60" y="65" text-anchor="middle" class="math" font-size="14">ρ<tspan class="mrm" font-size="10" dy="3">1</tspan></text><text x="420" y="65" class="label">descending</text><line x1="150" y1="211" x2="130" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="150" y1="211" x2="210" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="150" y1="211" x2="290" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="150" y1="211" x2="370" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="230" y1="211" x2="130" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="230" y1="211" x2="210" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="230" y1="211" x2="290" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="230" y1="211" x2="370" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="310" y1="211" x2="130" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="310" y1="211" x2="210" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="310" y1="211" x2="290" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="310" y1="211" x2="370" y2="149" class="muted-stroke" stroke-width="0.8"/><line x1="130" y1="131" x2="170" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="130" y1="131" x2="250" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="130" y1="131" x2="330" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="210" y1="131" x2="170" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="210" y1="131" x2="250" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="210" y1="131" x2="330" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="290" y1="131" x2="170" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="290" y1="131" x2="250" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="290" y1="131" x2="330" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="370" y1="131" x2="170" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="370" y1="131" x2="250" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="370" y1="131" x2="330" y2="69" class="muted-stroke" stroke-width="0.8"/><line x1="159" y1="220" x2="221" y2="220" class="accent-stroke" stroke-width="1.6"/><line x1="239" y1="220" x2="301" y2="220" class="accent-stroke" stroke-width="1.6"/><line x1="179" y1="60" x2="241" y2="60" class="accent-stroke" stroke-width="1.6"/><line x1="259" y1="60" x2="321" y2="60" class="accent-stroke" stroke-width="1.6"/><circle cx="150" cy="220" r="8" class="state"/><circle cx="230" cy="220" r="8" class="state"/><circle cx="310" cy="220" r="8" class="state"/><circle cx="130" cy="140" r="8" class="state"/><circle cx="210" cy="140" r="8" class="state"/><circle cx="290" cy="140" r="8" class="state"/><circle cx="370" cy="140" r="8" class="state"/><circle cx="170" cy="60" r="8" class="state"/><circle cx="250" cy="60" r="8" class="state"/><circle cx="330" cy="60" r="8" class="state"/><text x="60" y="258" class="label">lines: the order of P between blocks (lower is smaller); thick lines: comparabilities inside a block</text></svg>
:::

A positive answer requires all three sentences and yields one of them: a disjunctive question as in :ref{#def-disjunctive-notion}, with three sides.

:::lemma{#lem-sd-cac-question}
Let $c = (\sigma_0, \sigma_1, \sigma_2, X)$ be a condition and $\varphi_0, \varphi_1, \varphi_2$ be $\Sigma^0_1$ sentences.

1. If $c \mathrel{?{\vdash}} \varphi_0(G_0) \vee \varphi_1(G_1) \vee \varphi_2(G_2)$, some extension of $c$ forces $\varphi_i(G_i)$ for some $i < 3$.
2. Otherwise, some extension of $c$ forces $\neg \varphi_i(G_i)$ for some $i < 3$.
3. The relation is $\Sigma^0_1(Z)$, uniformly in the parameters of the sentences.
:::

:::proof{of=lem-sd-cac-question}
*Property 3.* Being a split triple is decidable in $X \oplus Z$, and $X \leq_T Z$.

*Property 1.* Let $(\tau_0, \tau_1, \tau_2)$ be a split triple witnessing the answer, $F = \rho_0 \cup \rho_1 \cup \rho_2$ and $m = \max_i |\tau_i|$. By finitely many applications of the pigeonhole principle with three colors, there is an infinite $Z$-computable $Y \subseteq X \setminus [0, m)$ such that each $x \in F$ is **small** ($x <_P y$ for all $y \in Y$), **large** ($y <_P x$ for all $y \in Y$) or **isolated** ($x \mid_P y$ for all $y \in Y$).

- If every element of $\rho_2$ is isolated, $(\sigma_0, \sigma_1, \tau_2, Y)$ is a condition: for $y \in Y$, $\tau_2 \cup \{ y \}$ is an antichain, since $\sigma_2 \cup \rho_2$ is one, $\sigma_2 \cup \{ y \}$ is one, and $\rho_2 \mid_P y$. It forces $\varphi_2(G_2)$. This includes the case $\rho_2 = \emptyset$.
- If some $z \in \rho_2$ is small, every $x \in \rho_0$ has $x <_P z <_P y$ for $y \in Y$, so is small, and $(\tau_0, \sigma_1, \sigma_2, Y)$ is a condition: $\tau_0 \cup \{ y \}$ is ascending for $y \in Y$. It forces $\varphi_0(G_0)$.
- If some $z \in \rho_2$ is large, every element of $\rho_1$ is large in the same way, and $(\sigma_0, \tau_1, \sigma_2, Y)$ forces $\varphi_1(G_1)$.

*Property 2.* Suppose the answer is negative. **Case 1**: some extension $d = (\tau_0, \tau_1, \tau_2', Y)$ of $c$ has $\tau_0$ satisfying $\varphi_0$ and $\tau_1$ satisfying $\varphi_1$. Then $d' = (\tau_0, \tau_1, \sigma_2, Y)$ is a condition extending $c$, and it forces $\neg \varphi_2(G_2)$. Indeed, let an extension of $d'$ have a stem $\tau_2$ on side $2$ satisfying $\varphi_2$, with new elements $\rho_2 \subseteq Y$. Each $z \in \rho_2$ is in $Y$, so $\tau_0 \cup \{ z \}$ is ascending and $\tau_1 \cup \{ z \}$ descending: $\rho_0 <_P z <_P \rho_1$. And $\rho_0 <_P \rho_1$, by any element of $Y$. So $(\tau_0, \tau_1, \tau_2)$ is a split triple for $c$ satisfying the three sentences, contradicting the negative answer. **Case 2**: no extension of $c$ has stems on sides $0$ and $1$ satisfying $\varphi_0$ and $\varphi_1$. If no extension has a stem on side $0$ satisfying $\varphi_0$, then $c$ forces $\neg \varphi_0(G_0)$. Otherwise let $d \leq c$ have such a stem; every extension of $d$ keeps it, so no extension of $d$ has a stem on side $1$ satisfying $\varphi_1$, and $d$ forces $\neg \varphi_1(G_1)$.
:::

:::quiz[split triples]
In property 1, why does a small element of $\rho_2$ make all of $\rho_0$ small?

- [x] Because every element of $\rho_0$ is below every element of $\rho_2$, by the definition of a split triple, and $<_P$ is transitive.
- [ ] Because $\rho_0$ is ascending.

  Ascending is a property of $\rho_0$ alone; it says nothing about the reservoir.
- [ ] Because the reservoir was thinned for $\rho_0$.

  The thinning gives each element of $\rho_0$ some behavior, not necessarily small.

:::

## Constant-bound compactness

Let $\varphi_i(n) = \exists v\ \psi_i(v, n)$, with $\psi_i$ a $\Sigma^0_1$ formula. If the answer is positive for $\varphi_0(G_0) \vee \varphi_1(G_1) \vee \varphi_2(G_2)$, the witnessing split triple has $\tau_i$ satisfying $\psi_i(v_i)$ for some value $v_i$, for each $i$; so the answer is also positive for $\psi_0(v_0)(G_0) \vee \psi_1(v_1)(G_1) \vee \psi_2(v_2)(G_2)$, with one value per side. The questions of $\mathsf{WKL}$ and $\mathsf{EM}$ only give finite sets of values of unbounded size. This is **constant-bound compactness**.

:::definition{#def-sd-preserve-cb}
A problem $\mathsf P$ admits **preservation of c.b.-immunity** if for every set $Z$, every set $A$ c.b.-immune relative to $Z$ (:ref{#def-sd-cb-immune}) and every instance $X \leq_T Z$, there is a solution $Y$ such that $A$ is c.b.-immune relative to $Z \oplus Y$.
:::

By :ref{#exr-sd-min-arrays} relativized, the arrays may be replaced by $W$-computable sequences of sets $F_n$ with $|F_n| \leq k$ and $\min F_n > n$. For indices $e$ and $k$, let $\Psi^W_{e,k}(n)$ be $\Phi^W_e(n)$ if this is the canonical index of a non-empty set $F$ with $|F| \leq k$ and $\min F > n$, and undefined otherwise.

:::theorem[Patey]{#thm-sd-cac-cb}
$\mathsf{CAC}$ admits preservation of c.b.-immunity. More precisely, for every $Z$, every set $A$ c.b.-immune relative to $Z$ and every $Z$-computable partial order, there is an infinite ascending sequence, descending sequence or antichain $G$ such that $A$ is c.b.-immune relative to $Z \oplus G$.
:::

:::proof{of=thm-sd-cac-cb}
Assume (H); the other case is :ref{#ex-cac-degenerate}. Build a decreasing sequence of $\mathsf{CAC}$ conditions from $(\varepsilon, \varepsilon, \varepsilon, \nat)$, handling infinitely often the growth of each side (:ref{#lem-sd-cac-extension}) and, for every triple of pairs $((e_0, k_0), (e_1, k_1), (e_2, k_2))$, the following task. Let $k = \max_i k_i$ and $c$ the current condition.

- If for some $n$ the answer to $\Psi^{Z \oplus G}_{e_0, k_0}(n)\converge(G_0) \vee \Psi^{Z \oplus G}_{e_1, k_1}(n)\converge(G_1) \vee \Psi^{Z \oplus G}_{e_2, k_2}(n)\converge(G_2)$ is negative, property 2 gives an extension forcing $\Psi^{Z \oplus G}_{e_i, k_i}(n)\diverge$ on some side $i$.
- Otherwise, for each $n$, search with oracle $Z$ for a witnessing split triple, and let $F_i$ be the set computed on side $i$, and $E_n = F_0 \cup F_1 \cup F_2$. Then $|E_n| \leq 3k$, $\min E_n > n$, and $n \mapsto E_n$ is $Z$-computable. By c.b.-immunity relative to $Z$, some $E_n$ is disjoint from $A$. The same split triple witnesses a positive answer for the sentences "$\Psi^{Z \oplus G}_{e_i, k_i}(n)\converge \subseteq E_n$", and property 1 gives an extension forcing, on some side $i$, that $\Psi^{Z \oplus G}_{e_i, k_i}(n)$ is a set disjoint from $A$.

Let $G_0, G_1, G_2$ be the unions of the stems. They are infinite, respectively ascending, descending and an antichain, and they satisfy what is forced. For every triple of pairs, some side $i$ has $\Psi^{Z \oplus G_i}_{e_i, k_i}$ partial or with a member disjoint from $A$. If for each $i$ some pair $(e_i, k_i)$ had $\Psi^{Z \oplus G_i}_{e_i, k_i}$ total with all members meeting $A$, the triple of these pairs would contradict this. So some $G_i$ has no such pair, and $A$ is c.b.-immune relative to $Z \oplus G_i$.
:::

The reservoirs stay $Z$-computable: negative answers are handled by a case analysis on extensions, not by a member of a $\Pi^0_1$ class. First-jump control with computable reservoirs is a sign that the problem involves no compactness.

::::exercise{#ex-cac-wkl difficulty=1 objective="Separate weak König's lemma from the chain–antichain principle with constant-bound immunity." lessons="custom-properties"}
Show that $\mathsf{WKL} \not\leq_\omega \mathsf{CAC}$.

:::solution
Let $A$ be the complement of Post's simple set. It is co-c.e. and immune, hence c.b.-immune by :ref{#prop-sd-coce-cb}. Let $\mathcal W$ be the class of sets relative to which $A$ is c.b.-immune; $\emptyset \in \mathcal W$. By :ref{#thm-sd-cac-cb}, $\mathsf{CAC}$ preserves $\mathcal W$. By :ref{#prop-sd-wkl-immunity}, some computable infinite binary tree has all its paths $P$ computing an infinite subset of $A$; listing it in increasing order as singletons gives a $P$-computable $1$-array all of whose members meet $A$, so $P \notin \mathcal W$. So $\mathsf{WKL}$ does not preserve $\mathcal W$, and :ref{#thm-preservation-separation} applies.
:::
::::

## Notes and references

The notion of forcing, the split triples and :ref{#thm-sd-cac-cb} are due to Patey (2018), and follow the section *Partial orders* of the chapter *Custom properties* of his monograph, which leaves the case where (H) fails to the reader. In the monograph's proof of property 2, Case 1 should require that the stems on sides $0$ and $1$ satisfy $\varphi_0$ and $\varphi_1$, as here. $\mathsf{CAC}$ was introduced in reverse mathematics by Hirschfeldt and Shore (2007).

- L. Patey, *Partial orders and immunity in reverse mathematics*, Computability 7 (2018), 323–339.
- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Sections 9.1 and 9.2.1.
- L. Patey, *Lowness and avoidance*, chapter *Custom properties*, section *Partial orders*.

:::::exercises
::::exercise{#ex-cac-degenerate difficulty=2 objective="Complete the preservation of constant-bound immunity by $\mathsf{CAC}$ when some side cannot be extended."}
Complete the proof of :ref{#thm-sd-cac-cb} when (H) fails.

:::solution
For a set $I$ of sides and an infinite $Z$-computable set $Y$, say that **(H) holds for $(I, Y)$** if for every infinite $Z$-computable $X \subseteq Y$ and every $i \in I$, some $x \in X$ has infinitely many $y > x$ in $X$ in the relation of side $i$. Start with $I = \{ 0, 1, 2 \}$ and $Y = \nat$. While (H) fails for $(I, Y)$, witnessed by $X \subseteq Y$ and $i \in I$, replace $Y$ by the infinite $Z$-computable set $Y' \subseteq X$ given by the greedy construction of the text, which has no pair in the relation of side $i$, and $I$ by $I \setminus \{ i \}$. Every pair of elements of $Y$ is in the relation of some side, and no pair is in the relation of a side outside $I$, so $I$ never becomes empty. If $I$ becomes a singleton $\{ j \}$, every pair of $Y$ is in the relation of side $j$, so $Y$ is a $Z$-computable infinite ascending sequence, descending sequence or antichain, and $A$ is c.b.-immune relative to $Z \oplus Y$. Otherwise the procedure stops with $|I| = 2$ and (H) holding for $(I, Y)$.

Use conditions with stems on the sides of $I$ and reservoirs $X \subseteq Y$; :ref{#lem-sd-cac-extension} holds for the sides of $I$ with the same proof. Split pairs are defined by the order constraints of the split triples restricted to $I$: for $I = \{ 0, 1 \}$, $\rho_0$ ascending, $\rho_1$ descending and $\rho_0 <_P \rho_1$; for $I = \{ 0, 2 \}$, $\rho_0 <_P \rho_2$; for $I = \{ 1, 2 \}$, $\rho_2 <_P \rho_1$. Property 3 holds as before. In property 1, after thinning the reservoir to $Y'' \subseteq Y$, an element $x$ of the blocks cannot behave towards $Y''$ as a missing side would: if $x$ were small for $I = \{ 1, 2 \}$, the pairs $\{ x, y \}$, $y \in Y''$, would be in the relation of side $0$, and $x, y \in Y$; similarly large elements do not occur for $I = \{ 0, 2 \}$, and isolated ones for $I = \{ 0, 1 \}$.

- $I = \{ 0, 1 \}$: every element is small or large. If some $x \in \rho_0$ is large, every element of $\rho_1$ is above $x$, hence large, and the extension of side $1$ forces $\varphi_1$. Otherwise $\rho_0$ is small and the extension of side $0$ forces $\varphi_0$.
- $I = \{ 0, 2 \}$: every element is small or isolated. If some $z \in \rho_2$ is small, $\rho_0$ is small, and side $0$ is extended; otherwise $\rho_2$ is isolated, and side $2$ is extended.
- $I = \{ 1, 2 \}$: symmetric, with large elements.

For property 2 with sides $j < j'$ of $I$: if no extension has a stem on side $j$ satisfying $\varphi_j$, the condition forces $\neg \varphi_j(G_j)$. Otherwise let $d = (\ldots, Y_d)$ be an extension whose stem $\tau_j$ on side $j$ satisfies $\varphi_j$, and $d'$ the condition with the stem $\tau_j$ on side $j$, the original stem on side $j'$, and reservoir $Y_d$. It forces $\neg \varphi_{j'}(G_{j'})$: the new elements of a stem on side $j'$ of an extension of $d'$ lie in $Y_d$, and each element $y \in Y_d$ satisfies the constraint of the split pair with $\rho_j$ (for instance $\rho_0 <_P y$, since $\tau_0 \cup \{ y \}$ is ascending), so such a stem satisfying $\varphi_{j'}$ would give a split pair satisfying both sentences. The proof of :ref{#thm-sd-cac-cb} then goes through with pairs instead of triples, sets $E_n$ of size at most $2k$, and Lachlan's disjunction over the two sides of $I$.
:::
::::

::::exercise{#ex-cac-cone difficulty=2 objective="Prove cone avoidance for $\mathsf{CAC}$ with the disjunctive question over split triples."}
Show with the $\mathsf{CAC}$ conditions and :ref{#lem-sd-cac-question} that every $Z$-computable partial order satisfying (H) has an infinite ascending sequence, descending sequence or antichain $G$ with $C \not\leq_T Z \oplus G$, for every $C \not\leq_T Z$.

:::solution
Build a decreasing sequence of conditions from $(\varepsilon, \varepsilon, \varepsilon, \nat)$, with the growth tasks of :ref{#lem-sd-cac-extension} and, for each triple $(e_0, e_1, e_2)$, the following task. Let $c$ be the current condition and $U$ the set of pairs $(x, v)$ with $v < 2$ such that
$$
c \mathrel{?{\vdash}} (\Phi^{Z \oplus G}_{e_0}(x)\converge = v)(G_0) \vee (\Phi^{Z \oplus G}_{e_1}(x)\converge = v)(G_1) \vee (\Phi^{Z \oplus G}_{e_2}(x)\converge = v)(G_2),
$$
a $\Sigma^0_1(Z)$ set by property 3. If $(x, 1 - C(x)) \in U$ for some $x$, property 1 gives an extension forcing $\Phi^{Z \oplus G_i}_{e_i}(x) = 1 - C(x)$ on some side $i$. If $(x, C(x)) \notin U$ for some $x$, property 2 gives an extension forcing, on some side $i$, that $\Phi^{Z \oplus G_i}_{e_i}(x)$ does not converge to $C(x)$. Otherwise, for every $x$, $C(x)$ is the only $v$ with $(x, v) \in U$, and $C \leq_T Z$, which is excluded. The unions $G_0, G_1, G_2$ of the stems are infinite and satisfy what is forced, so for every triple some side $i$ has $\Phi^{Z \oplus G_i}_{e_i} \neq C$. If every side $i$ had an index $e_i$ with $\Phi^{Z \oplus G_i}_{e_i} = C$, the triple $(e_0, e_1, e_2)$ would contradict this. So $C \not\leq_T Z \oplus G_i$ for some $i$. When (H) fails, one argues with fewer sides as in :ref{#ex-cac-degenerate}.
:::
::::

::::exercise{#ex-cac-3k difficulty=2 objective="Extract from the proof for $\mathsf{CAC}$ a quantitative statement: $3k$-immunity yields $k$-immunity."}
Let $k \geq 1$, $A$ a set $3k$-immune relative to $Z$, and $<_P$ a $Z$-computable partial order satisfying (H). Show that there is an infinite ascending sequence, descending sequence or antichain $G$ such that $A$ is $k$-immune relative to $Z \oplus G$.

:::solution
Run the construction of :ref{#thm-sd-cac-cb} with only the triples of pairs $((e_0, k), (e_1, k), (e_2, k))$. In the second case of the task, the sets $E_n$ have at most $3k$ elements, $\min E_n > n$, and $n \mapsto E_n$ is $Z$-computable; by :ref{#exr-sd-min-arrays} for $3k$, relativized to $Z$, some $E_n$ is disjoint from $A$. The end of the proof gives a side $i$ such that, for every $e$, $\Psi^{Z \oplus G_i}_{e,k}$ is partial or has a member disjoint from $A$. A $(Z \oplus G_i)$-computable sequence of sets $F_n$ with $|F_n| \leq k$ and $\min F_n > n$, all meeting $A$, would be $\Psi^{Z \oplus G_i}_{e,k}$ for an index $e$ of it, since its members are non-empty. So there is none, and $A$ is $k$-immune relative to $Z \oplus G_i$ by :ref{#exr-sd-min-arrays} relativized.
:::
::::

::::exercise{#ex-cac-h-needed difficulty=1 objective="See on a linear order why the assumption (H) is needed to extend the stems."}
Let $x <_P y$ if and only if $x < y$. Show that $(\varepsilon, \varepsilon, \varepsilon, \nat)$ is a $\mathsf{CAC}$ condition with no extension whose stem on side $2$ or on side $1$ is non-empty, and that (H) fails. Follow the procedure of :ref{#ex-cac-degenerate} on this order.

:::solution
The stems are empty, so the condition is valid. An extension with a stem on side $2$ containing some $x$ would have an infinite reservoir $Y$ with $\{ x, y \}$ an antichain for every $y \in Y$; but any two elements are comparable. An extension with a stem on side $1$ containing $x$ would have $y <_P x$ for the elements $y > x$ of its reservoir, which never holds. For $X = \nat$ and side $2$, no $x$ has a larger element in the relation of side $2$, so (H) fails. The procedure removes side $2$ with $Y = \nat$, which has no incomparable pair, then side $1$, still with $Y = \nat$; it ends with $I = \{ 0 \}$, and $\nat$ is a computable ascending sequence.
:::
::::

::::exercise{#ex-cac-split-cases difficulty=1 objective="Check the case distinction and the conditions obtained in property 1 of the question over split triples."}
In the proof of property 1 of :ref{#lem-sd-cac-question}:

1. show that $\rho_2$ cannot contain both a small and a large element;
2. show in detail that if some $z \in \rho_2$ is small, $(\tau_0, \sigma_1, \sigma_2, Y)$ is a condition extending $c$.

:::solution
1. If $z \in \rho_2$ is small and $z' \in \rho_2$ is large, take $y \in Y$: $z <_P y <_P z'$, so $z <_P z'$ by transitivity, while $\rho_2$ is an antichain.
2. $Y$ is infinite, $Z$-computable, contained in $X$ and above $m \geq |\tau_0|, |\sigma_1|, |\sigma_2|$; $\tau_0$ is compatible with $(\sigma_0, X)$, and the other stems are unchanged. For $y \in Y \subseteq X$, $\sigma_1 \cup \{ y \}$ is descending and $\sigma_2 \cup \{ y \}$ an antichain, by the condition $c$. It remains that $\tau_0 \cup \{ y \} = \sigma_0 \cup \rho_0 \cup \{ y \}$ is ascending. The set $\sigma_0 \cup \rho_0$ is ascending, since $\rho_0 \subseteq X$ is (remark after :ref{#def-sd-cac-condition}). For $a \in \sigma_0$, $a <_P y$ since $\sigma_0 \cup \{ y \}$ is ascending. For $x \in \rho_0$, $x <_P z$ by the definition of a split triple and $z <_P y$ since $z$ is small, so $x <_P y$. All these elements are below $y$ in the order of $\nat$, so the set is ascending.
:::
::::
:::::
