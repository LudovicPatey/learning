---
title: Forcing the jump effectively
summary: Conditions represented by codes; a notion of forcing decides the jump effectively relative to an oracle A if A finds extensions deciding each Σ⁰₁ sentence; then an A-computable generic sequence yields a set whose jump is computable in A; Cohen, Jockusch–Soare and computable Mathias forcing; the low basis theorem with lowness indices.
duration: 45
prerequisites: [low-bases, effective-forcing/cohen-forcing, effective-forcing/mathias-forcing, arithmetic-hierarchy/codes, pi01-classes/basis-theorems]
---

A set built by a sufficiently generic filter can be anything: for every countable family of sets, the generic set avoids it. To obtain a low set, the genericity must be restricted to what can be achieved with the oracle $\emptyset'$, and the construction must record, along the way, the answers to the questions "does $\Phi^G_e(e)$ converge?". This lesson isolates the two ingredients. First, the conditions must be represented by finite **codes**, so that an oracle can manipulate them. Second, the oracle must be able to find, from the code of a condition, an extension that **decides** the next question about the jump, and to say which way it is decided. When both hold, the jump of the generic set is computed by the oracle, by reading the decisions off the construction. This is **forcing the jump**, already met for Cohen forcing (:ref{#thm-generic-low}) and in the low basis theorem (:ref{#ex-low-basis-forcing}); here it becomes a method, applied with oracles other than $\emptyset'$ in the rest of the course.

## Codes of conditions

:::definition{#def-coded-forcing}
A **coding** of a notion of forcing $\mathbb P$ is a partial map from $\nat$ onto $\mathbb P$. The numbers in its domain are the **codes** of conditions. A family of dense sets $D_0, D_1, \dots$ is **uniformly $A$-effectively dense** if some partial $A$-computable function maps every code of a condition $c$ and every $i$ to a code of an extension of $c$ in $D_i$.
:::

This is the setting of :ref{#thm-effective-generic}. A coding is a choice, and the choice matters: it determines what an oracle can compute about a condition from its code.

1. **Cohen forcing.** A string is coded by a number in the usual way. Everything about a string can be computed from its code.
2. **Jockusch–Soare forcing.** A non-empty $\Pi^0_1$ class is coded by an index of a computable tree whose paths are its members. From the code one cannot decide whether the class is non-empty, but $\emptyset'$ can (:ref{#prop-pi01-emptiness}).
3. **Computable Mathias forcing.** A condition $(\sigma, X)$ is coded by a pair $\langle \sigma, b \rangle$ where $b$ is a $\Delta^0_1$ index of $X$ (:ref{#def-indices}). Membership in $X$ is decided from the code, but whether $X$ is infinite, or whether $X \cap R$ is infinite for a computable set $R$, are $\Pi^0_2$ questions about $b$.

The set of codes need not be simple: the set of $\Delta^0_1$ indices of infinite sets is $\Pi^0_2$-complete (exercises of :ref{to="arithmetic-hierarchy/codes"}). This is harmless, since a construction applies its procedures only to numbers that it has itself produced as codes.

## Deciding the jump

At level $1$, a condition forces a sentence when all its members satisfy it (:ref{#def-forcing-relation}).

:::definition{#def-jump-decision}
Let $\mathbb P$ be a coded notion of forcing and $A$ a set. $\mathbb P$ **decides the jump $A$-effectively** if there is a partial $A$-computable function that maps every code of a condition $c$ and every $e$ to a pair formed of a code of an extension $d \leq c$ and a bit $b$ such that
- if $b = 1$, every member $G$ of $d$ satisfies $\Phi^G_e(e)\converge$;
- if $b = 0$, every member $G$ of $d$ satisfies $\Phi^G_e(e)\diverge$.
:::

A forcing question at level $1$ (:ref{#def-forcing-question}) gives such a function when its answers can be decided by $A$ from the codes, and the extensions given by its two properties can be found by $A$ from the codes. For the questions of the previous course, the first condition holds with $A = \emptyset'$ as soon as the question is $\Sigma^0_1$ uniformly in the codes. The second condition is an additional requirement: the definition of a forcing question only asserts that the extensions exist.

:::theorem{#thm-jump-control}
Let $\mathbb P$ be a coded notion of forcing that decides the jump $A$-effectively, and let $D_0, D_1, \dots$ be uniformly $A$-effectively dense sets including the sets $S_n$ of conditions whose members have a common prefix of length $n$. For every condition $c$, there is an $A$-computable sequence of codes of conditions $c = c_0 \geq c_1 \geq \cdots$ whose filter $F$ meets every $D_i$, and the set $G = G_F$ satisfies $G' \leq_T A$.
:::

:::proof{of=thm-jump-control}
Let $h$ witness the uniform effective density, and $j$ the decision of the jump. Define the codes by $c_{2i+1} = h(c_{2i}, i)$ and $(c_{2i+2}, b_i) = j(c_{2i+1}, i)$. Each step applies a partial $A$-computable function to a code of a condition, so it is defined and gives a code of a condition; the sequence of codes and the sequence of bits are $A$-computable, and the sequence of conditions is decreasing. Its filter $F$ meets every $D_i$, in particular every $S_n$, so $G_F$ is defined, and it is a member of every condition of $F$ (:ref{#lem-generic-set}). If $b_e = 1$, then $G_F$ is a member of $c_{2e+2}$, so $\Phi^{G_F}_e(e)\converge$; if $b_e = 0$, then $\Phi^{G_F}_e(e)\diverge$. Hence $G_F' = \{ e : b_e = 1 \}$, which is computable in $A$.
:::

:::figure[The construction of :ref{#thm-jump-control}. The oracle computes each code from the previous one, alternating between dense sets, which include the sets $S_n$ that determine prefixes of the generic set, and decisions of the jump. The bits recorded at the decisions form the jump of the generic set.]
<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="A decreasing sequence of codes of conditions computed by the oracle A; the steps alternate between prefixes of the generic set, decisions of the jump and dense sets; the decisions are recorded as bits"><defs><marker id="lw-js-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker></defs><rect x="18" y="40" width="66" height="40" rx="6" class="cell"/><text x="51.0" y="65" text-anchor="middle" class="math" font-size="16">c₀</text><text x="51.0" y="100" text-anchor="middle" class="label">start</text><rect x="100" y="40" width="66" height="40" rx="6" class="cell"/><text x="133.0" y="65" text-anchor="middle" class="math" font-size="16">c₁</text><text x="133.0" y="100" text-anchor="middle" class="label">prefix</text><line x1="86" y1="60" x2="98" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><rect x="182" y="40" width="66" height="40" rx="6" class="head-cell"/><text x="215.0" y="65" text-anchor="middle" class="math" font-size="16">c₂</text><text x="215.0" y="100" text-anchor="middle" class="label">decide e = 0</text><line x1="168" y1="60" x2="180" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><line x1="215.0" y1="108" x2="215.0" y2="140" class="accent-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><text x="215.0" y="158" text-anchor="middle" class="label">bit b = 1</text><rect x="264" y="40" width="66" height="40" rx="6" class="cell"/><text x="297.0" y="65" text-anchor="middle" class="math" font-size="16">c₃</text><text x="297.0" y="100" text-anchor="middle" class="label">dense set D₀</text><line x1="250" y1="60" x2="262" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><rect x="346" y="40" width="66" height="40" rx="6" class="cell"/><text x="379.0" y="65" text-anchor="middle" class="math" font-size="16">c₄</text><text x="379.0" y="100" text-anchor="middle" class="label">prefix</text><line x1="332" y1="60" x2="344" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><rect x="428" y="40" width="66" height="40" rx="6" class="head-cell"/><text x="461.0" y="65" text-anchor="middle" class="math" font-size="16">c₅</text><text x="461.0" y="100" text-anchor="middle" class="label">decide e = 1</text><line x1="414" y1="60" x2="426" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><line x1="461.0" y1="108" x2="461.0" y2="140" class="accent-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><text x="461.0" y="158" text-anchor="middle" class="label">bit b = 0</text><rect x="510" y="40" width="66" height="40" rx="6" class="cell"/><text x="543.0" y="65" text-anchor="middle" class="math" font-size="16">c₆</text><text x="543.0" y="100" text-anchor="middle" class="label">dense set D₁</text><line x1="496" y1="60" x2="508" y2="60" class="muted-stroke" stroke-width="1.2" marker-end="url(#lw-js-arr)"/><text x="300" y="24" text-anchor="middle" class="label">each code is computed by A from the previous one</text><text x="300" y="188" text-anchor="middle" class="label">G′(e) = the bit recorded at the step deciding e: so G′ ≤ A</text><text x="300" y="206" text-anchor="middle" class="label muted">c₀ ≥ c₁ ≥ c₂ ≥ ⋯, and G is the member of all of them</text></svg>
:::

The proof does not use the genericity of $F$ beyond the sets $D_i$ and the decisions: the set $G$ is determined by countably many effective choices, and its jump is read from the record of the construction. The theorem is uniform: from a code of $c$ and indices of $h$ and $j$, one computes an index $k$ with $\Phi^A_k = G'$. For $A = \emptyset'$ this is a lowness index of $G$ (:ref{to="arithmetic-hierarchy/codes"}).

:::quiz[forcing the jump effectively]
In the proof of :ref{#thm-jump-control}, why is the bit $b_e$ needed, rather than only the extension $c_{2e+2}$?

- [x] Because the oracle must know which way the extension decides $\Phi^G_e(e)$; knowing that some decision is forced is useless if the oracle cannot tell which one.

  For instance, the oracle may be unable to decide whether all members of a given $\Pi^0_1$ class make a computation converge from the code alone.
- [ ] Because the extension might not decide the sentence.

  The definition requires that it does.
- [ ] Because $G$ is not computable in $A$.

  It is, since $G \leq_T G' \leq_T A$; the bit is what makes $G'$ computable in $A$.

---

Where is it used that the sets $S_n$ are among the dense sets?

- [x] To ensure that the filter determines a set $G_F$ that is a member of all its conditions, so that the decisions forced by the conditions hold for $G_F$.
- [ ] To ensure that $G_F$ is infinite.

  The sets $S_n$ fix prefixes of the characteristic sequence; they say nothing about the number of elements.
- [ ] To compute the bits $b_e$.

  The bits come from the decision of the jump, not from the sets $S_n$.
:::

## Three notions of forcing

:::proposition{#prop-jump-decision-examples}
Cohen forcing, Jockusch–Soare forcing and computable Mathias forcing, with the codings above, decide the jump $\emptyset'$-effectively, and their sets $S_n$ are uniformly $\emptyset'$-effectively dense.
:::

:::proof{of=prop-jump-decision-examples}
*Cohen forcing.* Given $\sigma$ and $e$, the oracle $\emptyset'$ decides whether $\Phi^\tau_e(e)\converge$ for some $\tau \succeq \sigma$, a $\Sigma^0_1$ question. If so, a search finds such a $\tau$, and $(\tau, 1)$ is returned: every $G \succ \tau$ satisfies $\Phi^G_e(e)\converge$ by the use principle. If not, $(\sigma, 0)$ is returned: every $G \succ \sigma$ satisfies $\Phi^G_e(e)\diverge$, since a convergent computation would converge on a prefix of $G$ extending $\sigma$. The sets $S_n$ are computably dense: extend $\sigma$ by zeros.

*Jockusch–Soare forcing.* Given a code of $\mathcal P$, let $\mathcal Q = \mathcal P \cap \{ X : \Phi^X_e(e)\diverge \}$, whose code is computable. The oracle $\emptyset'$ decides whether $\mathcal Q$ is empty (:ref{#prop-pi01-emptiness}). If not, return $(\mathcal Q, 0)$. If so, every member of $\mathcal P$ satisfies $\Phi^X_e(e)\converge$: return $(\mathcal P, 1)$. For $S_n$, $\emptyset'$ finds a string $\sigma$ of length $n$ with $\mathcal P \cap [\sigma] \neq \emptyset$, and returns a code of $\mathcal P \cap [\sigma]$.

*Computable Mathias forcing.* Given a code $\langle \sigma, b \rangle$ of $(\sigma, X)$, the relation "some string $\tau$ compatible with $(\sigma, X)$ has $\Phi^\tau_e(e)\converge$" is $\Sigma^0_1$ in $(\sigma, b, e)$: since $\Phi_b$ is total, compatibility of a given $\tau$ is decided by running $\Phi_b$ on the positions below $|\tau|$. The oracle $\emptyset'$ decides it. If it holds, a search finds $\tau$, and a $\Delta^0_1$ index $b'$ of $X \setminus \{0, \dots, |\tau|\}$ is computed from $b$ and $|\tau|$; return $(\langle \tau, b' \rangle, 1)$. If not, return $(\langle \sigma, b \rangle, 0)$: by property 2 of :ref{#prop-mathias-question}, every member satisfies $\Phi^G_e(e)\diverge$. For $S_n$, extend $\sigma$ by zeros up to length $n$, and remove from $X$ the numbers below $n$; this is computable.
:::

With :ref{#thm-jump-control}, the first two cases give a low 1-generic set, a second proof of :ref{#cor-low-exists}, and the low basis theorem, with the proof of :ref{#thm-low-basis}. For Jockusch–Soare forcing the decision is made **on all members** of the given class, without search for an extension; for Cohen and Mathias forcing, a positive decision requires a search, which succeeds because $\emptyset'$ has answered that the object searched for exists. Both forms fit the definition.

For computable Mathias forcing, the sets of conditions $(\sigma, X)$ with $\sigma$ containing at least $n$ elements are also computably dense, given a code, since a search through $X$ finds new elements. :ref{#thm-jump-control} then gives an infinite low set. This is not interesting by itself, since every infinite computable set is low, but it locates the obstacle to building low cohesive sets. For a computable sequence of sets $(R_i)$, the dense sets of conditions $(\sigma, X)$ with $X \subseteq R_i$ or $X \subseteq \overline{R_i}$ are uniformly $\emptyset''$-effectively dense, and no better in general: if they were uniformly $\emptyset'$-effectively dense, :ref{#thm-jump-control} would produce a low cohesive set, which does not always exist (:ref{#prop-coh-no-low}). The jump of a Mathias generic set is easy to decide; the difficulty is to choose the reservoir. Lesson 5 shows that the choice requires an oracle PA relative to $\emptyset'$, and no more.

:::quiz[the three examples]
In the proof of :ref{#prop-jump-decision-examples} for Mathias forcing, where is it used that the code contains a $\Delta^0_1$ index of the reservoir rather than a $\Sigma^0_1$ index?

- [x] To make the question "is there a compatible string with a convergent computation" a $\Sigma^0_1$ property of the code: compatibility requires knowing which numbers are outside the reservoir.
- [ ] To compute the index of $X \setminus \{0, \dots, |\tau|\}$.

  That index can be computed from a $\Sigma^0_1$ index too.
- [ ] To decide whether $X$ is infinite.

  Neither kind of index allows this computably.

---

Why does the Jockusch–Soare decision return the class $\mathcal P$ itself when $\mathcal Q$ is empty?

- [x] Because emptiness of $\mathcal Q$ means that every member of $\mathcal P$ makes the computation converge, so $\mathcal P$ already decides it.
- [ ] Because $\mathcal P$ has no extension.

  It has many; none is needed.
- [ ] Because $\emptyset'$ cannot compute a code of an extension.

  It can compute codes of many extensions; the point is that none is needed.
:::

## The low basis theorem with lowness indices

The construction of :ref{#thm-low-basis} relativizes, and the relativized construction is uniform in a way that matters for iterations. Recall that a **lowness index** of a low set $Z$ is a number $\ell$ with $\Phi^{\emptyset'}_\ell = Z'$ (:ref{to="arithmetic-hierarchy/codes"}), and that by :ref{#prop-no-lowness-index}, a lowness index cannot in general be computed from a $\Delta^0_2$ index.

:::proposition[Jockusch, Soare]{#prop-uniform-low-basis}
There is a total computable function $u$ with the following property. Let $\ell$ be a lowness index of a low set $Z$, and $t$ such that $\Phi^Z_t$ is the characteristic function of an infinite binary tree $T$. Then $u(\ell, t)$ is a lowness index of $Z \oplus X$ for some path $X$ of $T$.
:::

:::proof{of=prop-uniform-low-basis}
We describe a procedure with oracle $\emptyset'$, uniform in $\ell$ and $t$, that computes $(Z \oplus X)'$ for some path $X$; its index $u(\ell, t)$ is computable by the parameter form of SMN. Let $\mathcal P_0 = [T]$, a non-empty $\Pi^0_1(Z)$ class. Given a non-empty $\Pi^0_1(Z)$ class $\mathcal P_e$, by an index, let $\mathcal Q_e = \mathcal P_e \cap \{ X : \Phi^{Z \oplus X}_e(e)\diverge \}$. Emptiness of $\mathcal Q_e$ is a $\Sigma^0_1(Z)$ property of its index, by :ref{#prop-pi01-emptiness} relativized; by item 2 of :ref{#thm-jump}, there is a computable $g$, independent of $Z$, such that $\mathcal Q_e$ is empty if and only if $g(\text{index}) \in Z'$. The procedure evaluates $Z'(g(\text{index}))$ as $\Phi^{\emptyset'}_\ell(g(\text{index}))$. If $\mathcal Q_e \neq \emptyset$, let $\mathcal P_{e+1} = \mathcal Q_e$ and $J(e) = 0$; otherwise $\mathcal P_{e+1} = \mathcal P_e$ and $J(e) = 1$. As in :ref{#thm-low-basis}, every $X$ in the non-empty intersection of the classes $\mathcal P_e$ satisfies $(Z \oplus X)' = J$, and $J = \Phi^{\emptyset'}_{u(\ell, t)}$.
:::

The function $u$ is total even when its arguments are not what the proposition assumes; its output is then meaningless. This is how lowness indices are used: a construction with oracle $\emptyset'$ manipulates lowness indices of the sets it has built, and the correctness of each index is proved by induction. For instance, starting from a lowness index of $\emptyset$ and applying $u$ to the trees of $\{0, 1\}$-valued functions DNC relative to the current set gives a $\emptyset'$-computable sequence of lowness indices of sets $Z_0 \leq_T Z_1 \leq_T \cdots$, each PA relative to the previous one: the proof of :ref{#thm-low-scott}, made uniform. Uniformity of the indices does not make the join $\bigoplus_n Z_n$ low: a computation with this oracle may query infinitely many columns, and the jumps of the $Z_n$ say nothing about it. Lesson 4 obtains low codes of whole ideals by a single application of the low basis theorem.

:::quiz[lowness indices]
In the proof of :ref{#prop-uniform-low-basis}, why is a lowness index of $Z$ needed, rather than a $\Delta^0_2$ index of $Z$?

- [x] Because the questions asked are $\Sigma^0_1(Z)$, that is, questions about $Z'$; a $\Delta^0_2$ index gives $Z$ but not $Z'$, and :ref{#prop-no-lowness-index} shows that $Z'$ cannot be recovered uniformly from it.
- [ ] Because $Z$ is not computable in $\emptyset'$.

  It is, since $Z$ is low.
- [ ] Because the tree $T$ is computable in $Z'$.

  It is computable in $Z$, by hypothesis.
:::

## Exercises

::::exercise{difficulty=1}
Show that there is a computable function $v$ such that if $\ell$ is a lowness index of $Z$ and $\Phi^Z_e$ is the characteristic function of a set $Y$, then $v(\ell, e)$ is a lowness index of $Y$.

:::solution
The set $Y'$ is $Y$-c.e., hence $Z$-c.e., uniformly in $e$: $x \in Y'$ if and only if $\Phi^{\Phi^Z_e}_x(x)$ converges, where the inner oracle is simulated by $\Phi^Z_e$. By item 2 of :ref{#thm-jump}, there is a computable injective $f$, depending computably on $e$ and not on $Z$, with $x \in Y' \iff f(e, x) \in Z'$. The procedure $x \mapsto \Phi^{\emptyset'}_\ell(f(e, x))$ computes $Y'$; its index $v(\ell, e)$ is given by SMN.
:::
::::

::::exercise{difficulty=2}
Use :ref{#thm-jump-control} with Cohen forcing to build a low infinite set $G$ whose principal function $p_G$ is hyperimmune (:ref{#def-hyperimmune-fn}).

:::solution
Count the elements of a set from $0$, so that $p_G(k)$ is its $k$-th element. Let $D_{2e}$ be the set of strings $\tau$ such that $\Phi_e(k)\diverge$ for some $k$, or $\tau$ has a $k$-th element larger than $\Phi_e(k)$ for some $k$; and let $D_{2e+1}$ be the set of strings with at least $e$ elements. Given $\sigma$ and $e$, let $k$ be the number of elements of $\sigma$. The oracle $\emptyset'$ decides whether $\Phi_e(k)\converge$. If not, $\sigma \in D_{2e}$. If so, let $\tau = \sigma 0^m 1$ with $|\sigma| + m > \Phi_e(k)$: the $k$-th element of $\tau$ is $|\sigma| + m$, so $\tau \in D_{2e}$. The sets $D_{2e+1}$ and $S_n$ are computably dense. By :ref{#prop-jump-decision-examples} and :ref{#thm-jump-control}, there is a low set $G$ whose filter of prefixes meets all these sets. It is infinite, and for every total computable function $\Phi_e$, some prefix of $G$ has a $k$-th element larger than $\Phi_e(k)$, so $p_G(k) > \Phi_e(k)$. No computable function dominates $p_G$.
:::
::::

::::exercise{difficulty=2}
Show that computable Sacks forcing, with conditions coded by indices of computable f-trees (:ref{#def-function-tree}), decides the jump $\emptyset'$-effectively. Deduce that every computable f-tree has a low path that is not computable.

:::solution
Given an index of an f-tree $T$ and $e$, the oracle $\emptyset'$ decides whether some node $T(\rho)$ has $\Phi^{T(\rho)}_e(e)\converge$. If so, the subtree of the nodes above $T(\rho)$ has an index computable from $\rho$, and all its paths make the computation converge; return it with $b = 1$. If not, every path $X$ of $T$ has $\Phi^X_e(e)\diverge$, since a convergent computation would converge on some node; return $T$ with $b = 0$. The sets $S_n$ are computably dense: the full subtree above a node of length at least $n$ is an extension. To make $G$ non-computable, add the dense sets $E_e$ of trees no path of which is equal to $\Phi_e$. Given $T$ and $e$, let $n$ be the first position at which the incomparable nodes $T(0)$ and $T(1)$ differ. The oracle $\emptyset'$ decides whether $\Phi_e(n)\converge$. If so, choose $i$ with $T(i)(n) \neq \Phi_e(n)$, and take the subtree above $T(i)$: none of its paths is equal to $\Phi_e$. If not, $\Phi_e$ is partial, and $T$ is already in $E_e$. These sets are uniformly $\emptyset'$-effectively dense, and :ref{#thm-jump-control} gives a low path that is not computable.
:::
::::

## Notes and references

The effectivization of forcing constructions with codes of conditions follows the sections *Indices* and *Basic constructions* of the chapter *Lowness* of Patey's monograph. Effective genericity is presented by Hirschfeldt (Section 2.3, Proposition 2.7) and by Dzhafarov and Mummert (Theorem 7.5.6); the decision of the jump of Mathias generic sets with $\emptyset'$ is Claim 1 in the proof of their Lemma 8.5.11, and Hirschfeldt's proof of Theorem 6.44. The low basis theorem is due to Jockusch and Soare (1972), who observed that it is uniform; the version with lowness indices of :ref{#prop-uniform-low-basis} is Exercise 3.12 of Hirschfeldt, for low trees.

- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Sections 2.3, 3.1 and 6.5.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Sections 7.5 and 8.5.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, sections *Indices* and *Basic constructions*.
