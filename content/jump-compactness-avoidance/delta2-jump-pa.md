---
title: The pigeonhole principle and jump PA avoidance
summary: Forcing a requirement on a part of a meta-condition with Liu's valuations one jump up; the number of branches where a requirement is not forced decreases, or becomes zero at the next level; a construction by tasks, a path of valid parts by König's lemma, and the proof that every Δ⁰₂ set has an infinite subset of itself or of its complement whose jump is not PA relative to ∅′.
duration: 40
prerequisites: [meta-questions]
---

This lesson completes the proof of :ref{#thm-d22-jump-pa}. The setting of the two previous lessons is fixed. The construction is a decreasing sequence of meta-conditions, whose level grows from time to time. Each requirement is forced on every part of some meta-condition, by the three-case argument with Liu's valuations, one jump up. The set $H$ is read along a path of valid parts, found at the end by König's lemma.

## Forcing a requirement on a part

For a finite valuation $h$ (:ref{#def-valuation}) and an index $e$, the sentence "$\Phi^{G'}_e$ is incompatible with $h$", that is, $\Phi^{G'}_e(x)\converge = 1 - h(x)$ for some $x \in \mathrm{dom}\, h$, is equivalent to a $\Sigma^0_2$ sentence $\varphi_{e, h} = \exists y\ \psi_{e, h}(y)$, uniformly in $e$ and the code of $h$: it is the disjunction of the sentences $\chi_{e, x, 1 - h(x)}$ of :ref{to="jump-compactness-avoidance/jump-pa-avoidance"}, written with one existential quantifier. Its negation $\neg\varphi_{e, h}$ says that $\Phi^{G'}_e$ is compatible with $h$. Correctness of valuations is relative to $\emptyset'$: $h$ is correct if $J^{\emptyset'}(x)$ is defined and differs from $h(x)$ for every $x \in \mathrm{dom}\, h$.

:::definition{#def-meta-requirement}
A meta-condition $c$ **forces the requirement $e$** on its part $(I, i)$ if

1. there is a valuation $h$ correct relative to $\emptyset'$ such that every member of $(I, i)$ satisfies $\varphi_{e, h}$; or
2. there are two incompatible valuations $h, h'$ such that $c$ promises $\neg\varphi_{e, h}$ and $\neg\varphi_{e, h'}$ on $(I, i)$.
:::

In the first case, $\Phi^{G'}_e(x) = J^{\emptyset'}(x)$ for some $x$, for every member $G$. In the second, if the promises become true, $\Phi^{G'}_e$ is undefined at a number where $h$ and $h'$ differ. In both cases $\Phi^{G'}_e$ is not a total $\{0, 1\}$-valued function DNC relative to $\emptyset'$. If $c$ forces the requirement $e$ on $(I, i)$ and $d$ of level $m$ extends $c$, then $d$ forces it on every part $(J, i)$ with $J \upharpoonright n = I$: members of $(J, i)$ are members of $(I, i)$, and promises are inherited by :ref{#lem-meta-promise}.

For a meta-condition $c$ of level $n$, $i < 2$ and $e$, let $N_e(c, i)$ be the set of branches $I$ of $\mathbb I_n$ such that $c$ does not force the requirement $e$ on $(I, i)$.

:::lemma{#lem-meta-requirement}
1. Let $c$ be a meta-condition, $i < 2$ and $e$ an index with $N_e(c, i) \neq \emptyset$. There is an extension $d$ of $c$ such that either $d$ has the same level as $c$ and $|N_e(d, i)| < |N_e(c, i)|$, or $N_e(d, i) = \emptyset$.
2. For every meta-condition $c$ and every $e$, there is an extension $d$ of $c$ that forces the requirement $e$ on all its parts.
:::

:::proof{of=lem-meta-requirement}
1. Let $n$ be the level of $c$ and $H = N_e(c, i)$. Let $U$ be the set of finite valuations $h$ with $c \mathrel{?{\vdash}}_{H, i} \varphi_{e, h}$. By item 1 of :ref{#lem-meta-question}, $U$ is $\Sigma^0_2$, that is, $\Sigma^0_1(\emptyset')$. Apply :ref{#lem-liu-valuations} with $W = \emptyset'$ and $\emptyset'$ in place of $D$; its hypothesis holds, since no set computable in $\emptyset'$ is PA relative to $\emptyset'$.
   - If $U$ contains a correct valuation $h$, item 2 of :ref{#lem-meta-question} gives an extension $d$ of level $n$ and $I \in H$ such that all members of $(I, i)$ in $d$ satisfy $\varphi_{e, h}$: $d$ forces the requirement on $(I, i)$. Since the level is the same, every branch is its own ancestor, and $d$ still forces the requirement on the parts outside $H$. So $N_e(d, i) \subseteq H \setminus \{ I \}$.
   - Otherwise, choose $l$ with $2^l \geq 2u_n + 1$: there are $2u_n + 1$ pairwise incompatible valuations $h_0, \dots, h_{2u_n}$ outside $U$. By :ref{#lem-meta-merging}, some $d$ of level $n + 1$ extends $c$ and promises $\neg\varphi_{e, h_a}$ and $\neg\varphi_{e, h_b}$ on $(I \cdot \{a, b\}, i)$ for every $I \in H$ and $a < b$: it forces the requirement there. The other branches of $\mathbb I_{n+1}$ have their ancestor outside $H$, where $c$ forced the requirement. So $N_e(d, i) = \emptyset$.
2. Apply item 1 repeatedly with $i = 0$. Each application either decreases $|N_e(\cdot, 0)|$ or makes it empty, so after finitely many steps $N_e(d_0, 0) = \emptyset$. Then apply it with $i = 1$ to get $d_1$ extending $d_0$. Forcing on the parts with $i = 0$ is inherited by $d_1$, so $N_e(d_1, 0) = N_e(d_1, 1) = \emptyset$.
:::

The lemma is the three-case argument of :ref{#thm-weak-merging-pa}, with $\emptyset'$ in the role of the oracle, and the number of branches as a measure of progress. A positive answer settles one branch without changing the level. A negative answer settles all branches at once, at the next level, where the count starts again from zero. The third case is empty: Liu's lemma says that one of the first two always applies, because $\emptyset'$ is not PA relative to itself.

:::quiz[forcing the requirements]
In item 1 of :ref{#lem-meta-requirement}, why does a positive answer not give $N_e(d, i) = \emptyset$?

- [x] Because a positive answer of $\mathrel{?{\vdash}}_{H, i}$ forces $\varphi_{e, h}$ on one branch of $H$ only, chosen by the witness of non-largeness; the other branches of $H$ remain to be handled.
- [ ] Because a positive answer increases the level.

  It keeps the level, which is why the count can decrease.
- [ ] Because $h$ is correct on one branch only.

  Correctness of $h$ is a property of $h$ and $\emptyset'$, not of branches.

---

Why does the iteration in item 2 terminate?

- [x] Because each application either decreases the finite number $|N_e(\cdot, i)|$ at the same level, or makes it $0$; a strictly decreasing sequence of natural numbers is finite.
- [ ] Because the level is bounded.

  The level can grow, but only in the second case, which ends the iteration.
- [ ] Because there are finitely many valuations.

  There are infinitely many finite valuations.
:::

## The construction

Fix an enumeration of tasks in which every task occurs infinitely often:

- **(R)** for an index $e$: pass to an extension given by item 2 of :ref{#lem-meta-requirement};
- **(L)** for every valid part of the current meta-condition in turn, extend its stem by item 4 of :ref{#lem-meta-valid};
- **(P)** for a $\Pi^0_2$ sentence $\forall y\ \theta(y)$ and a number $m$: for every valid part $(I, i)$ of the current meta-condition in turn, if it promises $\forall y\ \theta(y)$ on $(I, i)$, pass to an extension given by item 2 of :ref{#lem-meta-promise}.

Start with the meta-condition $c_0$ of level $0$ and let $c_{s+1}$ be obtained from $c_s$ by the $s$-th task; let $n_s$ be the level of $c_s$. The steps inside a task (L) or (P) keep the level, the index set and, up to finite changes, the reservoirs, so by item 3 of :ref{#lem-meta-valid} they keep the valid parts: a part valid at the end of the task was valid throughout, and its stem was extended, or its promise used, during the task.

Let $V_s$ be the finite set of valid parts of $c_s$. It is non-empty, by item 1 of :ref{#lem-meta-valid}. By item 2, if $(J, i) \in V_{s+1}$, then $(J \upharpoonright n_s, i) \in V_s$. So the sets $V_s$ form a finitely branching infinite tree, whose nodes at height $s$ are the elements of $V_s$ and the parent of $(J, i) \in V_{s+1}$ is $(J \upharpoonright n_s, i)$. By König's lemma, there is a sequence $(I_s, i_s)$ with $(I_s, i_s) \in V_s$ and $I_{s+1} \upharpoonright n_s = I_s$, $i_{s+1} = i_s$. Let $i$ be the common value of $i_s$ and
$$
G = \bigcup_s \sigma^{I_s}_i(c_s),
$$
where $\sigma^{I_s}_i(c_s)$ is the stem of the part $(I_s, i)$ of $c_s$.

:::proof{of=thm-d22-jump-pa}
We prove the case $Z = D = \emptyset$. By item 2 of :ref{#def-meta-extension}, each stem $\sigma^{I_{s+1}}_i(c_{s+1})$ is compatible with $(\sigma^{I_s}_i(c_s), \bigcup_{\nu \in I_s} X_\nu(c_s))$; so the stems form an increasing sequence of strings, $G$ is a member of the part $(I_s, i)$ of $c_s$ for every $s$, and $G \subseteq A_i$, since every stem is.

*$G$ is infinite.* At a step $s$ with a task (L), the part $(I_{s+1}, i)$ is valid in $c_{s+1}$, at the same level as $c_s$, so it was valid throughout the task and its stem was extended.

*Promises are kept.* Suppose $c_s$ promises $\forall y\ \theta(y)$ on $(I_s, i)$. By item 1 of :ref{#lem-meta-promise} and induction, $c_t$ promises it on $(I_t, i)$ for every $t \geq s$. Let $m \in \nat$, and $t \geq s$ a step with the task (P) for $\forall y\ \theta(y)$ and $m$. The part $(I_{t+1}, i) = (I_t, i)$ is valid throughout the task, so the task made all members of this part satisfy $\theta(m)$; $G$ is one of them. So $G$ satisfies $\forall y\ \theta(y)$.

*Requirements.* Let $e$ and $s$ be such that the task at step $s$ is (R) for $e$. Then $c_{s+1}$ forces the requirement $e$ on $(I_{s+1}, i)$. In the first case of :ref{#def-meta-requirement}, $G$ is a member of this part, so $\Phi^{G'}_e(x) = J^{\emptyset'}(x)$ for some $x$. In the second case, $G$ satisfies the two promises, so $\Phi^{G'}_e$ is undefined at some $x$. In both cases $\Phi^{G'}_e$ is not a $\{0, 1\}$-valued function DNC relative to $\emptyset'$.

So $H = G$ is an infinite subset of $A_i$ and $H'$ is not PA relative to $\emptyset'$.

*The general case.* Let $D \leq_T Z$ with $Z'$ not PA relative to $D'$, and $A$ a $\Delta^0_2(Z)$ set. Take a Scott ideal $\mathcal M$ containing $Z$ with a code $M$ such that $M' \leq_T Z'$ (:ref{#cor-scott-codes}), and use sentences about $Z \oplus G$: the classes $\mathcal V^I_{\tau, \theta}$ become $\Sigma^0_1(Z)$ classes, which are $\Sigma^0_1(\mathcal M)$ classes since $Z \in \mathcal M$; index sets $S$ are $\Delta^0_2(Z)$. The questions become $\Sigma^0_1(Z')$, and :ref{#lem-liu-valuations} is applied with $W = Z'$ and $D'$ in place of $D$, which is legitimate since $D' \leq_T Z'$ and $Z'$ is not PA relative to $D'$. Correctness of valuations is relative to $D'$, and the result is an infinite $H \subseteq A_i$ with $(Z \oplus H)'$ not PA relative to $D'$.
:::

:::figure[The tree of valid parts along the construction. Column $s$ lists the valid parts of $c_s$, and each valid part of $c_{s+1}$ is joined to its ancestor in $c_s$. Some parts lose their validity and their descendants disappear; the level grows when a requirement is forced by weak merging. König's lemma gives an infinite path, along which the stems define $H$.]
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="Columns of valid parts of the meta-conditions c_0 to c_4, each part joined to its ancestor; some parts lose validity and have no descendants; a path through the columns is drawn in the accent color"><text x="60" y="22" text-anchor="middle" class="label">c₀</text><text x="180" y="22" text-anchor="middle" class="label">c₁</text><text x="300" y="22" text-anchor="middle" class="label">c₂</text><text x="420" y="22" text-anchor="middle" class="label">c₃</text><text x="540" y="22" text-anchor="middle" class="label">c₄</text><line x1="104" y1="50" x2="136" y2="50" class="muted-stroke" stroke-width="1"/><line x1="104" y1="100" x2="136" y2="100" class="accent-stroke" stroke-width="2"/><line x1="224" y1="50" x2="256" y2="50" class="muted-stroke" stroke-width="1"/><line x1="224" y1="100" x2="256" y2="100" class="accent-stroke" stroke-width="2"/><line x1="224" y1="100" x2="256" y2="150" class="muted-stroke" stroke-width="1"/><line x1="344" y1="100" x2="376" y2="50" class="accent-stroke" stroke-width="2"/><line x1="344" y1="150" x2="376" y2="100" class="muted-stroke" stroke-width="1"/><line x1="464" y1="50" x2="496" y2="50" class="accent-stroke" stroke-width="2"/><rect x="16" y="36" width="88" height="28" rx="6" class="state"/><text x="60.0" y="54.0" text-anchor="middle" class="label">({ε}, 0)</text><rect x="16" y="86" width="88" height="28" rx="6" class="node"/><text x="60.0" y="104.0" text-anchor="middle" class="label">({ε}, 1)</text><rect x="136" y="36" width="88" height="28" rx="6" class="state"/><text x="180.0" y="54.0" text-anchor="middle" class="label">({ε}, 0)</text><rect x="136" y="86" width="88" height="28" rx="6" class="node"/><text x="180.0" y="104.0" text-anchor="middle" class="label">({ε}, 1)</text><rect x="256" y="36" width="88" height="28" rx="6" class="state"/><text x="300.0" y="54.0" text-anchor="middle" class="label">({0,1}, 0)</text><rect x="256" y="86" width="88" height="28" rx="6" class="node"/><text x="300.0" y="104.0" text-anchor="middle" class="label">({0,2}, 1)</text><rect x="256" y="136" width="88" height="28" rx="6" class="state"/><text x="300.0" y="154.0" text-anchor="middle" class="label">({1,2}, 1)</text><rect x="376" y="36" width="88" height="28" rx="6" class="node"/><text x="420.0" y="54.0" text-anchor="middle" class="label">({0,2}, 1)</text><rect x="376" y="86" width="88" height="28" rx="6" class="state"/><text x="420.0" y="104.0" text-anchor="middle" class="label">({1,2}, 1)</text><rect x="496" y="36" width="88" height="28" rx="6" class="node"/><text x="540.0" y="54.0" text-anchor="middle" class="label">({0,2}, 1)</text><text x="300" y="212" text-anchor="middle" class="label">level 0 for c₀, c₁; level 1 from c₂ on, after a weak merging step</text></svg>
:::

:::quiz[the construction]
Why is the path of valid parts chosen at the end, by König's lemma, rather than during the construction?

- [x] Because a part valid at one step may lose its validity at a later step; only parts valid forever turn their promises into truth, and König's lemma provides such a sequence of parts whatever happens.
- [ ] Because the construction does not know $A$.

  The construction uses $A$, through the stems and the questions.
- [ ] Because the level of the meta-conditions is bounded.

  The level may grow without bound.

---

Where in the proof is the hypothesis that $\emptyset'$ is not PA relative to $\emptyset'$ hidden in the unrelativized case?

- [x] In :ref{#lem-meta-requirement}, through :ref{#lem-liu-valuations}: the set $U$ of valuations is $\Sigma^0_1(\emptyset')$, and Liu's lemma needs that its oracle is not PA relative to $\emptyset'$.
- [ ] In the choice of the low code $M$.

  Low codes exist for every Scott ideal construction; no PA hypothesis is used.
- [ ] In item 1 of :ref{#lem-meta-valid}.

  Validity uses only the cover lemma and the Ramsey property of branches.
:::

## Exercises

::::exercise{difficulty=2}
Show that the proof still works if $N_e(c, i)$ is replaced by the set $N^{\mathrm{v}}_e(c, i)$ of the branches $I$ such that $(I, i)$ is valid in $c$ and $c$ does not force the requirement $e$ on $(I, i)$.

:::solution
Item 1 of :ref{#lem-meta-requirement} holds with $H = N^{\mathrm v}_e(c, i)$. In the first case, $d$ has the same level, the branch $I$ is now forced, and by item 2 of :ref{#lem-meta-valid} a part valid in $d$ was valid in $c$; so $N^{\mathrm v}_e(d, i) \subseteq H \setminus \{I\}$. In the second case, a valid part $(J, i)$ of $d$ has a valid ancestor $(J \upharpoonright n, i)$, which is either in $H$, and then $(J, i)$ is forced by the merging, or forced in $c$, and then $(J, i)$ is forced by inheritance; so $N^{\mathrm v}_e(d, i) = \emptyset$. The iteration terminates as before, and the resulting meta-condition forces the requirement on all its valid parts, which is all that the proof of the theorem uses, since the path consists of valid parts.
:::
::::

::::exercise{difficulty=1}
Show that while the level of $c_s$ is $0$, the branch $I_s$ is $\{\varepsilon\}$, and that if $A$ is finite, the path has $i = 1$.

:::solution
At level $0$ there is one branch, so $I_s = \{\varepsilon\}$ while $n_s = 0$. If $A$ is finite, no part $(I, 0)$ is valid (second exercise of :ref{to="jump-compactness-avoidance/meta-conditions"}), and the path consists of valid parts, so $i = 1$.
:::
::::

## Notes and references

The notion of forcing a requirement on a branch, the counting argument and the conclusion along a path are due to Monin and Patey (2021); the presentation follows the section *Pigeonhole principle* of the chapter *Jump compactness avoidance* of Patey's monograph. The monograph builds a sufficiently generic filter and defines paths through it; here the construction is a sequence of meta-conditions with tasks, as in :ref{to="jump-cone-avoidance/pigeons-non-high"}, and the path is given by König's lemma on the finite sets of valid parts. Liu's lemma is from Liu (2012); its relativization to $\emptyset'$ is immediate from :ref{#lem-liu-valuations}.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Pigeonhole principle*.
