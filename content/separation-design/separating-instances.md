---
title: Building the separating instances
summary: A Δ⁰₂ constant-bound immune set meeting every DNC degree, so that CAC implies neither DNC nor RT²₂; a stable partial order defeating dependent hyperimmunity, so that ADS does not imply SCAC.
duration: 45
prerequisites: [chain-antichain, ascending-descending, immunity-growth/dnc-functions, turing-degrees/limit-computability]
---

A separation by preservation has two halves (:ref{to="separation-design/custom-properties"}); the two previous lessons gave the preservation theorems for $\mathsf{CAC}$ and $\mathsf{ADS}$. This lesson builds the separating instances, by two independent finite injury arguments.

## A constant-bound immune set for DNC functions

The problem $\mathsf{DNC}$ has the sets $X$ as instances, with the functions DNC relative to $X$ as solutions. A DNC function escapes every c.e. set of known size (:ref{#thm-dnc-effectively-immune}): it computes $h$ with $h(e, n) \notin W_e$ whenever $|W_e| \leq n$. So a DNC function can meet a set whose complement is c.e. and small in a known way, while c.b.-immunity requires the complement to meet every computable array of bounded blocks. Columns reconcile the two demands.

Let $X_i = \{ \langle i, k \rangle : k \in \nat \}$, the $i$-th column, and call $k$ the **height** of $\langle i, k \rangle$. Let $\mu(i)$ be the least $s > i$ with $\emptyset'_s \uh i = \emptyset' \uh i$, for the standard enumeration of $\emptyset'$. It dominates the modulus of :ref{#cor-complete-domination}, so a function dominating $\mu$ computes $\emptyset'$. It is **left-c.e.**: for $y > i$, $\mu(i) > y$ holds if and only if some element below $i$ enters $\emptyset'$ after stage $y$, so the set $\{ (i, y) : y < \mu(i) \}$ is c.e. Let $F_i$ be the set of elements of $X_i$ of height less than $\mu(i)$.

:::theorem[Patey]{#thm-sd-dnc-cb}
There is a $\Delta^0_2$ c.b.-immune set $A$ such that every DNC function computes an infinite subset of $A$.
:::

:::figure[The set $A$ of :ref{#thm-sd-dnc-cb}. Each column $X_i$ is cut at height $\mu(i)$, a left-c.e. bound; the elements kept form the sets $F_i$ (filled). The c.e. set $W$ removes at most $i$ elements from column $i$ (holes). A DNC function finds in each column an element outside $W$; if it finds infinitely many below the cut, they form a subset of $A$, and otherwise its heights dominate $\mu$.]
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Columns X0 to X5; each column is filled up to the height mu(i), with a few holes for the elements of W; the elements above the cut are not in A"><rect x="110" y="198" width="52" height="22" class="cell head-cell"/><rect x="110" y="176" width="52" height="22" class="cell head-cell"/><rect x="110" y="154" width="52" height="22" class="cell"/><rect x="110" y="132" width="52" height="22" class="cell"/><rect x="110" y="110" width="52" height="22" class="cell"/><rect x="110" y="88" width="52" height="22" class="cell"/><rect x="110" y="66" width="52" height="22" class="cell"/><rect x="110" y="44" width="52" height="22" class="cell"/><line x1="106" y1="176" x2="166" y2="176" class="accent-stroke" stroke-width="2"/><text x="136.0" y="242" text-anchor="middle" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3">0</tspan></text><rect x="176" y="198" width="52" height="22" class="cell head-cell"/><rect x="176" y="176" width="52" height="22" class="cell"/><rect x="176" y="154" width="52" height="22" class="cell head-cell"/><rect x="176" y="132" width="52" height="22" class="cell"/><rect x="176" y="110" width="52" height="22" class="cell"/><rect x="176" y="88" width="52" height="22" class="cell"/><rect x="176" y="66" width="52" height="22" class="cell"/><rect x="176" y="44" width="52" height="22" class="cell"/><line x1="172" y1="154" x2="232" y2="154" class="accent-stroke" stroke-width="2"/><text x="202.0" y="242" text-anchor="middle" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3">1</tspan></text><rect x="242" y="198" width="52" height="22" class="cell"/><rect x="242" y="176" width="52" height="22" class="cell head-cell"/><rect x="242" y="154" width="52" height="22" class="cell head-cell"/><rect x="242" y="132" width="52" height="22" class="cell"/><rect x="242" y="110" width="52" height="22" class="cell head-cell"/><rect x="242" y="88" width="52" height="22" class="cell"/><rect x="242" y="66" width="52" height="22" class="cell"/><rect x="242" y="44" width="52" height="22" class="cell"/><line x1="238" y1="110" x2="298" y2="110" class="accent-stroke" stroke-width="2"/><text x="268.0" y="242" text-anchor="middle" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3">2</tspan></text><rect x="308" y="198" width="52" height="22" class="cell head-cell"/><rect x="308" y="176" width="52" height="22" class="cell head-cell"/><rect x="308" y="154" width="52" height="22" class="cell head-cell"/><rect x="308" y="132" width="52" height="22" class="cell head-cell"/><rect x="308" y="110" width="52" height="22" class="cell"/><rect x="308" y="88" width="52" height="22" class="cell"/><rect x="308" y="66" width="52" height="22" class="cell"/><rect x="308" y="44" width="52" height="22" class="cell"/><line x1="304" y1="132" x2="364" y2="132" class="accent-stroke" stroke-width="2"/><text x="334.0" y="242" text-anchor="middle" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3">3</tspan></text><rect x="374" y="198" width="52" height="22" class="cell head-cell"/><rect x="374" y="176" width="52" height="22" class="cell head-cell"/><rect x="374" y="154" width="52" height="22" class="cell"/><rect x="374" y="132" width="52" height="22" class="cell head-cell"/><rect x="374" y="110" width="52" height="22" class="cell head-cell"/><rect x="374" y="88" width="52" height="22" class="cell"/><rect x="374" y="66" width="52" height="22" class="cell head-cell"/><rect x="374" y="44" width="52" height="22" class="cell"/><line x1="370" y1="66" x2="430" y2="66" class="accent-stroke" stroke-width="2"/><text x="400.0" y="242" text-anchor="middle" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3">4</tspan></text><rect x="440" y="198" width="52" height="22" class="cell head-cell"/><rect x="440" y="176" width="52" height="22" class="cell"/><rect x="440" y="154" width="52" height="22" class="cell head-cell"/><rect x="440" y="132" width="52" height="22" class="cell head-cell"/><rect x="440" y="110" width="52" height="22" class="cell head-cell"/><rect x="440" y="88" width="52" height="22" class="cell head-cell"/><rect x="440" y="66" width="52" height="22" class="cell"/><rect x="440" y="44" width="52" height="22" class="cell"/><line x1="436" y1="88" x2="496" y2="88" class="accent-stroke" stroke-width="2"/><text x="466.0" y="242" text-anchor="middle" class="math" font-size="14">X<tspan class="mrm" font-size="10" dy="3">5</tspan></text><text x="98" y="216" text-anchor="end" class="label">height 0</text><text x="98" y="58" text-anchor="end" class="label">height 7</text><rect x="110" y="262" width="12" height="12" class="cell head-cell"/><text x="128" y="272" class="label">element of A</text><line x1="240" y1="268" x2="266" y2="268" class="accent-stroke" stroke-width="2"/><text x="272" y="272" class="label">cut at μ(i)</text><text x="370" y="272" class="label">empty below the cut: element of W</text></svg>
:::

:::proof{of=thm-sd-dnc-cb}
We build a c.e. set $W$ with $|W \cap X_i| \leq i$ for every $i$, and let $A = \bigcup_i F_i \setminus W$. Since $|F_i| = \mu(i) > i$, each $F_i \setminus W$ is non-empty, so $A$ is infinite; and $A \leq_T \emptyset'$, since $\mu \leq_T \emptyset'$.

*DNC functions.* Let $f$ be DNC and $h \leq_T f$ as above. For each $i$, let $e(i)$ be an index, computable from $i$, of the c.e. set of heights $\{ k : \langle i, k \rangle \in W \}$, which has at most $i$ elements; let $k_i = h(e(i), i)$, so that $n_i = \langle i, k_i \rangle \in X_i \setminus W$. Then $(n_i)$ is computable in $f$, and $n_i \in A$ if and only if $k_i < \mu(i)$.

1. If $k_i < \mu(i)$ for infinitely many $i$, the set of these $i$ is c.e. relative to $f$, since $\mu$ is left-c.e., and infinite; it has an infinite $f$-computable subset $I$, and $\{ n_i : i \in I \}$ is an infinite $f$-computable subset of $A$, its elements lying in distinct columns.
2. Otherwise $i \mapsto k_i$ dominates $\mu$ from some point on, and a finite modification of it, computable in $f$, dominates $\mu$. So $f$ computes $\emptyset'$, hence $A$, an infinite subset of itself.

*Requirements.* By :ref{#exr-sd-min-arrays}, it suffices to defeat, for each $k$, the computable sequences of sets of size at most $k$ with $\min F_n > n$; let $\Psi_{e,k}$ be the partial computable functions of :ref{#def-sd-preserve-cb} without oracle. The requirements are, for all $e$ and $k$:

$R_{e,k}$: if $\Psi_{e,k}$ is total and meets each column $X_j$ only finitely often, that is, $\{ n : \Psi_{e,k}(n) \cap X_j \neq \emptyset \}$ is finite for every $j$, then $\Psi_{e,k}(n) \subseteq W$ for some $n$.

*Construction.* Order the pairs $(e, k)$ by codes, and let $i_{e,k} = \sum_{\langle e', k' \rangle \leq \langle e, k \rangle} k'$. At stage $s$, each $R_{e,k}$ with $\langle e, k \rangle < s$ that has not acted yet **acts** if there is $n < s$ with $\Psi_{e,k}(n)[s]\converge = F$ and $F \subseteq \bigcup_{j \geq i_{e,k}} X_j$: it enumerates $F$ into $W$, and never acts again.

*Verification.* Each $R_{e,k}$ acts at most once and enumerates at most $k$ elements, all in columns $j \geq i_{e,k}$. The elements of $W \cap X_i$ come from requirements with $i_{e,k} \leq i$; since $i_{e,k}$ is non-decreasing in $\langle e, k \rangle$, these form an initial segment of the pairs, ending at some $\langle e^*, k^* \rangle$, and they enumerate at most $\sum_{\langle e', k' \rangle \leq \langle e^*, k^* \rangle} k' = i_{e^*, k^*} \leq i$ elements. So $|W \cap X_i| \leq i$. If the hypothesis of $R_{e,k}$ holds, only finitely many $n$ have $\Psi_{e,k}(n)$ meeting a column $X_j$ with $j < i_{e,k}$, so $R_{e,k}$ eventually acts, putting some $\Psi_{e,k}(n')$ into $W$. So every requirement is satisfied.

*c.b.-immunity.* We show by induction on $k \geq 0$ that every total $\Psi_{e,k}$ has a member disjoint from $A$. For $k = 0$ there is nothing to prove: the members of $\Psi_{e,0}$ would be empty sets with $\min F > n$, so $\Psi_{e,0}$ is nowhere defined. Let $k \geq 1$, and suppose that $\Psi_{e,k}$ is total with every member meeting $A$. No member is contained in $W$, which is disjoint from $A$, so by $R_{e,k}$ some column $X_j$ meets $\Psi_{e,k}(n)$ for infinitely many $n$. The set of these $n$ is computable; let $n_0 < n_1 < \cdots$ be a computable enumeration of those with $n > \max F_j$. Since $\min \Psi_{e,k}(n_m) > n_m > \max F_j$ and $A \cap X_j \subseteq F_j$, the elements of $\Psi_{e,k}(n_m)$ in $X_j$ are not in $A$. Let $E_m = \Psi_{e,k}(n_m) \setminus X_j$. Then $E_m$ meets $A$, $|E_m| \leq k - 1$, $\min E_m > n_m \geq m$, and $(E_m)$ is computable: a contradiction with the induction hypothesis for $k - 1$, applied to an index of $(E_m)$.
:::

:::quiz[the DNC construction]
In the case analysis for a DNC function, why is it essential that $\mu$ is left-c.e.?

- [x] To enumerate, with oracle $f$, the columns $i$ in which $n_i$ lies below the cut, and hence in $A$; with a cut that could only be approximated from above, membership of $n_i$ in $F_i$ would not be detectable.
- [ ] To make $A$ a $\Delta^0_2$ set.

  Any $\emptyset'$-computable cut would.
- [ ] To make $|W \cap X_i| \leq i$.

  The bound on $W$ comes from the thresholds $i_{e,k}$.

:::

:::corollary[Hirschfeldt, Shore]{#cor-sd-cac-not-dnc}
$\mathsf{DNC} \not\leq_\omega \mathsf{CAC}$. Consequently $\mathsf{RT}^2_2 \not\leq_\omega \mathsf{CAC}$ and $\mathsf{EM} \not\leq_\omega \mathsf{CAC}$.
:::

:::proof{of=cor-sd-cac-not-dnc}
Let $A$ be as in :ref{#thm-sd-dnc-cb}, and $\mathcal W$ the class of sets relative to which $A$ is c.b.-immune; $\emptyset \in \mathcal W$. By :ref{#thm-sd-cac-cb}, $\mathsf{CAC}$ preserves $\mathcal W$. For the instance $\emptyset$ of $\mathsf{DNC}$, every solution $f$ computes an infinite subset of $A$, so $A$ is not even immune relative to $f$. So $\mathsf{DNC}$ does not preserve $\mathcal W$, and :ref{#thm-preservation-separation} applies. Every Turing ideal satisfying $\mathsf{RT}^2_2$ contains, relative to each of its members, a DNC function, by :ref{#cor-rt22-dnc} relativized; so $\mathsf{DNC} \leq_\omega \mathsf{RT}^2_2$, and $\mathsf{RT}^2_2 \not\leq_\omega \mathsf{CAC}$. For $\mathsf{EM}$, use the theorem of Bienvenu, Patey and Shafer that $\mathsf{EM}$ implies $\mathsf{RWKL}$, admitted in :ref{to="separation-design/erdos-moser-separation"}, and :ref{#cor-rt22-dnc} for $\mathsf{RWKL}$.
:::

Hirschfeldt and Shore proved the first statement through the avoidance of DNC degrees.

## A stable partial order for dependent hyperimmunity

Let $<_P$ be a partial order on $\nat$. An element $x$ is **small** if $x <_P y$ for almost every $y$, and **isolated** if $x \mid_P y$ for almost every $y$. The order is **stable** if every element is small or isolated, or every element is large or isolated (defined symmetrically); $\mathsf{SCAC}$ is $\mathsf{CAC}$ for stable orders (Hirschfeldt and Shore). If every element is small or isolated, an infinite chain $H$ consists of small elements, since an isolated element is incomparable with almost every element of $H$; and an infinite antichain consists of isolated elements.

:::theorem[Patey]{#thm-sd-stable-order}
There is a computable partial order $<_P$ on $\nat$ and a $\Delta^0_2$ partition $\nat = B \sqcup I$ into its small elements $B$ and its isolated elements $I$, such that the pair $(I, B)$ is dependently hyperimmune.
:::

:::proof{of=thm-sd-stable-order}
Fix an enumeration $(\varphi_e)$ of the $\Sigma^0_1$ formulas $\varphi(U, V)$, with $\varphi_e(U, V)[s]$ its approximation at stage $s$. We build $<_P$ and approximations $B_s \sqcup I_s = [0, s)$ of $B$ and $I$, satisfying:

$R_e$: if $\varphi_e$ is essential, then $\varphi_e(R, S)$ for some $R \subseteq B$ and $S \subseteq I$.

This is dependent hyperimmunity of $(I, B)$, since $\overline I = B$. Each $R_e$ has a **marker** $m_e$, initially $0$, and may be **satisfied**.

*Stage $s$.* First decide the relation between $s$ and every $x < s$: let $x <_P s$ if $x \in B_s$, and $x \mid_P s$ otherwise. Then $R_e$ with $e < s$ **requires attention** if it is not satisfied and there are $R, S \subseteq (m_e, s]$ with $\max R < \min S$ and $\varphi_e(R, S)[s]$. If some $R_e$ requires attention, let $e$ be the least one, with witnesses $R$ and $S$: move the elements of $(m_e, \min S)$ to $B_{s+1}$ and those of $[\min S, s]$ to $I_{s+1}$, the others keeping their side. Declare $R_e$ satisfied, and for every $e' > e$, set $m_{e'} = s + 1$ and declare $R_{e'}$ not satisfied. If no requirement requires attention, put $s$ into $I_{s+1}$.

*Partial order.* The relation $<_P$ is computable, and $x <_P y$ implies $x < y$, so it is irreflexive. For transitivity, let $x < y < z$ with $x <_P y$ and $y <_P z$, that is, $x \in B_y$ and $y \in B_z$, and suppose $x \in I_z$. Let $s < z$ be the last stage with $x \in B_s$; then $s \geq y$, and at stage $s$ some $R_e$ acts and moves $x$ into $I$, hence moves all of $[x, s]$, which contains $y$. Since $y \in B_z$, some $R_{e'}$ acts at a stage $t$ with $s < t < z$ and moves $y$ back to $B$, so $m_{e'} < y$ at stage $t$. After stage $s$, the requirements $e'' > e$ have markers above $s \geq y$, and $R_e$, satisfied, acts again only after a reset raising its marker above $s$; so $e' < e$, and $m_{e'}$ has not changed since stage $s$, so $m_{e'} \leq m_e < x$, the markers being non-decreasing in the index. Then $R_{e'}$ moves an interval $(m_{e'}, \min S')$ containing $y$, hence $x$, into $B$ at stage $t$: $x \in B_{t+1}$ with $s < t + 1 \leq z$, contradicting the choice of $s$ or the assumption $x \in I_z$.

*Limits.* An element $x$ moved by $R_e$ at stage $s$ can afterwards only be moved by requirements of higher priority than $e$: the others have markers above $s$. So $x$ moves at most $e + 1$ more times, and $B = \lim_s B_s$ and $I = \lim_s I_s$ exist; they partition $\nat$, and are $\Delta^0_2$. If $x \in B$, then $x \in B_s$ and $x <_P s$ for almost every $s$, so $x$ is small; if $x \in I$, $x$ is isolated. So the order is stable, with $B$ and $I$ as stated.

*Requirements.* By induction, each $R_e$ acts finitely often: after the last action of the requirements of higher priority, at some stage $s_0$, its marker no longer changes, and it acts at most once more. If $\varphi_e$ is essential, there are $R > m_e$ and $S > \max R$ with $\varphi_e(R, S)$, and if $R_e$ is not satisfied after $s_0$, it requires attention at a large stage and acts. When it last acts, with sets $R$ and $S$ at stage $s$, it puts $R \subseteq (m_e, \min S)$ into $B$ and $S \subseteq [\min S, s]$ into $I$. These elements are never moved again: the requirements of higher priority do not act, those of lower priority have markers above $s$, and $R_e$ is not reset. So $R \subseteq B$ and $S \subseteq I$.
:::

:::corollary[Lerman, Solomon, Towsner]{#cor-sd-ads-not-scac}
$\mathsf{SCAC} \not\leq_\omega \mathsf{ADS}$, hence $\mathsf{CAC} \not\leq_\omega \mathsf{ADS}$.
:::

:::proof{of=cor-sd-ads-not-scac}
Let $<_P$, $B$, $I$ be as in :ref{#thm-sd-stable-order}, and $\mathcal W$ the class of sets relative to which $(I, B)$ is dependently hyperimmune; $\emptyset \in \mathcal W$. By :ref{#thm-sd-ads-dependent}, $\mathsf{ADS}$ preserves $\mathcal W$. Let $H$ be an infinite chain or antichain of $<_P$. Then $H \subseteq B$ or $H \subseteq I$, and by the exercise of :ref{to="separation-design/ascending-descending"}, $H \notin \mathcal W$. So $\mathsf{SCAC}$ does not preserve $\mathcal W$, and :ref{#thm-preservation-separation} applies.
:::

:::quiz[the stable partial order]
Why does a strategy move to $B$ the whole interval $(m_e, \min S)$, and to $I$ the whole interval $[\min S, s]$, rather than just $R$ and $S$?

- [x] To keep $<_P$ transitive: the relation of each element with the later ones is decided by its current side, and moving intervals ensures that when an element goes back to $B$, every element between the marker and it goes back as well, which is what the transitivity argument uses.
- [ ] To make the requirement satisfied.

  Moving $R$ and $S$ alone would do.
- [ ] To make $B$ and $I$ infinite.

  This follows from the requirements.
:::

## Exercises

::::exercise{difficulty=2}
Show that the order of :ref{#thm-sd-stable-order} has no infinite descending sequence, and that $B$ and $I$ are infinite. Deduce from :ref{#thm-sd-stable-order} that $B$ and $I$ are hyperimmune.

:::solution
If $x <_P y$ then $x < y$, so no pair $x < y$ has $y <_P x$. Since $\nat = B \sqcup I$ and $(I, B)$ is dependently hyperimmune, both sets are infinite by the exercise of :ref{to="separation-design/ascending-descending"}. By :ref{#ex-sd-dependent}, with $A_0 = I$, no disjoint strong array of non-empty sets has all its members meeting $I$, so $I$ is hyperimmune. For $B = A_1$, the same argument applies to the essential formula "$V = F_n$ for some $n$", with $U$ arbitrary: it gives some $F_n \subseteq \overline B$.
:::
::::

## Notes and references

:ref{#thm-sd-dnc-cb} and :ref{#thm-sd-stable-order} are due to Patey (2018), and follow the sections *Partial orders* and *Linear orders* of the chapter *Custom properties* of his monograph. The separations are due to Hirschfeldt and Shore (2007), who also introduced $\mathsf{SCAC}$, and to Lerman, Solomon and Towsner (2013; Hirschfeldt, *Slicing the Truth*, Theorem 9.29).

- L. Patey, *Partial orders and immunity in reverse mathematics*, Computability 7 (2018), 323–339.
- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- M. Lerman, R. Solomon and H. Towsner, *Separating principles below Ramsey's theorem for pairs*, Journal of Mathematical Logic 13 (2013), 1350007.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2015, Sections 9.1–9.2.
- L. Patey, *Lowness and avoidance*, chapter *Custom properties*.
