---
title: DNC avoidance and the comparison of avoidances
summary: DNC avoidance and countably merging forcing questions; DNC avoidance implies cone avoidance; preservation of immunity; the relations between cone, PA, constant-bound trace and DNC avoidance.
duration: 30
prerequisites: [rwwkl-dnc, pa-avoidance-examples, immunity-growth/immune-sets]
---

The previous lesson showed that DNC functions are the weakest of the four levels of compactness met in the course, and that Ramsey's theorem for pairs reaches it. Avoiding DNC degrees is therefore a property that Ramsey's theorem for pairs lacks, but that weaker problems may have. This lesson defines DNC avoidance, identifies the property of forcing questions that proves it, countable merging, and shows that the same property preserves immunity. The last section compares the avoidance properties of the course.

## DNC avoidance

A function $f$ is **DNC relative to $D$** if $f(x) \neq \Phi^D_x(x)$ whenever $\Phi^D_x(x)$ converges, and a set is **DNC relative to $D$** if it computes such a function. As for PA, the class of these sets is closed upwards, contains $D'$, and contains no set computable in $D$.

:::definition{#def-dnc-avoidance}
A problem $\mathsf P$ admits **DNC avoidance** if for all sets $D \leq_T Z$ such that $Z$ is not DNC relative to $D$, every instance $X \leq_T Z$ has a solution $Y$ such that $Z \oplus Y$ is not DNC relative to $D$.
:::

A $\{0, 1\}$-valued DNC function is a DNC function, so DNC sets include PA sets. To avoid DNC degrees, the case analysis of :ref{#thm-local-pa-avoidance} must handle functionals with values in $\nat$: in the second case, a number $x$ for which no value $v$ can be forced, one needs an extension forcing all the infinitely many negations "$\Phi^{Z \oplus G}_e(x) \neq v$" at once.

:::definition{#def-countably-merging}
A forcing question is **countably merging** if for every condition $c$, every $\Sigma^0_1$ formula $\varphi(y)$ and every set $R \subseteq \nat$ such that $c \mathrel{?{\nvdash}} \varphi(m)$ for every $m \in R$, some extension of $c$ forces $\neg \varphi(m)$ for every $m \in R$.
:::

The questions of Cohen forcing, of computable Sacks forcing, of computable Mathias forcing and of the forcing of :ref{#thm-delta2-pa-avoidance} are countably merging: a negative answer means that no compatible string, or no node, satisfies the sentence, and then the condition itself forces all the negations. The case of Sacks forcing is :ref{#exr-sacks-dnc}. The question of Jockusch–Soare forcing is not, by the theorem below: below the condition $\mathrm{DNC}_2$, every generic set computes a DNC function. Nor does the measure argument of :ref{#thm-wwkl-strong-pa} extend to DNC functions: a positive measure of oracles may give each value with small probability, and removing infinitely many small classes can remove everything; indeed, random sequences compute DNC functions (:ref{#cor-random-dnc}).

:::theorem{#thm-countably-merging-dnc}
Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving countably merging forcing question, and $D$ a set such that no member of $\mathcal M$ is DNC relative to $D$. For every sufficiently generic set $G$, $Z \oplus G$ is not DNC relative to $D$.
:::

:::proof{of=thm-countably-merging-dnc}
Fix $e$, a condition $c$ and $X \in \mathcal M$ for $c$. The set
$$
U = \{ (x, v) \in \nat^2 : c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge = v \}
$$
is $\Sigma^0_1(X)$.

1. If $(x, \Phi^D_x(x)) \in U$ for some $x$ with $\Phi^D_x(x)\converge$, an extension forces $\Phi^{Z \oplus G}_e(x) = \Phi^D_x(x)$.
2. If for some $x$ no pair $(x, v)$ belongs to $U$, the question is countably merging, applied to the formula $\Phi^{Z \oplus G}_e(x)\converge = y$ and $R = \nat$: an extension forces $\Phi^{Z \oplus G}_e(x)\converge \neq v$ for every $v$, that is, $\Phi^{Z \oplus G}_e(x)\diverge$.
3. Otherwise, the first value $g(x)$ found for each $x$ in an enumeration of $U$ defines a total $X$-computable function with $g(x) \neq \Phi^D_x(x)$ whenever this converges: $X$ is DNC relative to $D$, which is excluded.

So the conditions forcing that $\Phi^{Z \oplus G}_e$ is not DNC relative to $D$ are dense.
:::

With computable Mathias forcing relative to $Z$, as in :ref{#thm-coh-pa-avoidance}, this shows that $\mathsf{COH}$ admits DNC avoidance; the unrelativized case is in :ref{#thm-mathias-coh-preservation}. The comparison with cone avoidance is the same as for PA degrees.

:::proposition{#prop-dnc-avoidance-cone}
If a problem admits DNC avoidance, it admits cone avoidance.
:::

:::proof{of=prop-dnc-avoidance-cone}
Repeat the proof of :ref{#thm-pa-implies-cone} with "DNC" in place of "PA": with $W = Z \oplus G$ given by the Posner–Robinson theorem, $W$ is not DNC relative to $W$, and $W'$ is DNC relative to $W$, since it computes $x \mapsto \Phi^W_x(x) + 1$ where this converges, and $0$ elsewhere.
:::

## Preservation of immunity

Countable merging gives a second preservation property. An infinite set $I$ is **immune relative to $Z$** if it has no infinite subset that is c.e. relative to $Z$, equivalently no infinite $Z$-computable subset (:ref{to="immunity-growth/immune-sets"}).

:::definition{#def-preserve-immunity}
A problem $\mathsf P$ admits **preservation of immunity** if for every set $Z$, every set $I$ immune relative to $Z$, and every instance $X \leq_T Z$, there is a solution $Y$ such that $I$ is immune relative to $Z \oplus Y$.
:::

:::theorem{#thm-countably-merging-immunity}
Let $\mathbb P$ have a $\Sigma^0_1(\mathcal M)$-preserving countably merging forcing question, and let $I$ be immune relative to every member of $\mathcal M$. For every sufficiently generic set $G$, $I$ is immune relative to $Z \oplus G$.
:::

:::proof{of=thm-countably-merging-immunity}
Fix $e$, a condition $c$ and $X \in \mathcal M$ for $c$, and let $U = \{ x : c \mathrel{?{\vdash}} x \in W^{Z \oplus G}_e \}$, a $\Sigma^0_1(X)$ set. If some $x \in U$ is not in $I$, an extension forces $x \in W^{Z \oplus G}_e$, so $W^{Z \oplus G}_e \not\subseteq I$. If $U$ is finite, countable merging with $R = \nat \setminus U$ gives an extension forcing $x \notin W^{Z \oplus G}_e$ for every $x \notin U$, so $W^{Z \oplus G}_e \subseteq U$ is finite. Otherwise $U$ is an infinite subset of $I$, c.e. relative to $X$, which is excluded. So for every sufficiently generic $G$, no $W^{Z \oplus G}_e$ is an infinite subset of $I$.
:::

The first two cases of this proof are the two ways a c.e. set can fail to be an infinite subset of $I$, and they need the same property of the question as DNC avoidance. This is not a coincidence: a DNC function relative to $Z$ computes a set that is effectively immune relative to $Z$, a strong form of immunity (:ref{#thm-dnc-effectively-immune}).

:::quiz[countable merging]
In the proof of :ref{#thm-countably-merging-dnc}, why does case 2 need countable merging, while the proof of :ref{#thm-local-pa-avoidance} only needs merging?

- [x] Because $\Phi^{Z \oplus G}_e(x)$ may take any value in $\nat$, so forcing it to diverge requires forcing the negations of infinitely many sentences, one for each $v$, at once.
- [ ] Because $U$ is a set of pairs of numbers rather than of pairs with $v < 2$.

  This is a consequence of the same fact, not its reason.
- [ ] Because $\Phi^D_x(x)$ may diverge.

  The divergence of $\Phi^D_x(x)$ is harmless in all cases.

---

In the proof of :ref{#thm-countably-merging-immunity}, which hypothesis on $I$ excludes the third case?

- [x] That $I$ has no infinite subset c.e. relative to $X$, for every $X \in \mathcal M$; the set $U$ is such a subset in the third case.
- [ ] That $I$ is infinite.

  Infinity of $I$ is not used; a finite set has no infinite subset at all.
- [ ] That $I$ is not computable.

  A non-computable set can have infinite computable subsets.
:::

## Comparing the avoidance properties

:::figure[Relations between the avoidance properties of the course. An arrow between avoidance properties is an implication proved in the course, and the label next to it names a problem for which the converse fails. The properties of forcing questions on the left give the avoidance properties they point to; countable merging implies finite merging, which implies merging for the sentences used in the proofs.]
<svg class="fig" viewBox="0 0 600 340" width="600" role="img" aria-label="Constant-bound trace avoidance implies PA avoidance, which implies cone avoidance; DNC avoidance implies cone avoidance. WWKL has PA avoidance but not c.b. trace avoidance; WKL has cone avoidance but not PA avoidance; RT22 has cone avoidance but not DNC avoidance. Finitely merging, merging and countably merging questions give c.b. trace, PA and DNC avoidance; countable merging also gives preservation of immunity"><defs><marker id="ca-cmp-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="105" y="18" text-anchor="middle" class="label muted">property of the question</text><text x="410" y="18" text-anchor="middle" class="label muted">avoidance property</text><rect x="20" y="30" width="170" height="40" rx="6" class="cell"/><text x="105.0" y="54.0" text-anchor="middle" class="label">finitely merging</text><rect x="20" y="130" width="170" height="40" rx="6" class="cell"/><text x="105.0" y="154.0" text-anchor="middle" class="label">merging</text><rect x="20" y="230" width="170" height="40" rx="6" class="cell"/><text x="105.0" y="254.0" text-anchor="middle" class="label">countably merging</text><rect x="330" y="30" width="160" height="40" rx="6" class="state"/><text x="410.0" y="54.0" text-anchor="middle" class="label">c.b. trace avoidance</text><rect x="330" y="130" width="160" height="40" rx="6" class="state"/><text x="410.0" y="154.0" text-anchor="middle" class="label">PA avoidance</text><rect x="330" y="230" width="160" height="40" rx="6" class="state"/><text x="410.0" y="254.0" text-anchor="middle" class="label">cone avoidance</text><rect x="510" y="130" width="80" height="40" rx="6" class="state"/><text x="550.0" y="146.0" text-anchor="middle" class="label">DNC</text><text x="550.0" y="162.0" text-anchor="middle" class="label">avoidance</text><line x1="192" y1="50" x2="326" y2="50" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="192" y1="150" x2="326" y2="150" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="410" y1="72" x2="410" y2="126" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="410" y1="172" x2="410" y2="226" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="530" y1="172" x2="472" y2="228" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><path d="M192,262 C300,330 610,320 584,176" class="ink-stroke" stroke-width="1.3" fill="none" marker-end="url(#ca-cmp-arr)"/><text x="418" y="104" class="label">converse fails: WWKL</text><text x="402" y="204" text-anchor="end" class="label">converse fails: WKL</text><text x="512" y="204" class="label">converse</text><text x="512" y="219" class="label">fails: RT²₂</text><text x="380" y="330" text-anchor="middle" class="label">countable merging also preserves immunity</text></svg>
:::

The following table summarizes what the course proves about the main problems.

| problem | cone | PA | c.b. trace | DNC |
| --- | --- | --- | --- | --- |
| $\mathsf{COH}$ | yes | yes | yes | yes |
| $\mathsf{WKL}$ | yes | no | no | no |
| $\mathsf{WWKL}$ | yes | yes | no | no |
| $\mathsf{RWKL}$ | yes | yes | yes (from $\mathsf{RT}^2_2$) | no |
| $\mathsf{RT}^2_2$ | yes | yes | yes (Liu, admitted) | no |
| $\mathsf{RT}^3_2$ | no | no | no | no |

The entries for $\mathsf{COH}$ come from :ref{#thm-coh-pa-avoidance} and its variants with finitely and countably merging questions; those for $\mathsf{WKL}$ from the class $\mathrm{DNC}_2$; those for $\mathsf{WWKL}$ from :ref{#thm-wwkl-strong-pa}, :ref{#prop-random-no-trace} and :ref{#cor-random-dnc}; those for $\mathsf{RWKL}$ and $\mathsf{RT}^2_2$ from Liu's theorems and :ref{#cor-rt22-dnc}; the cone avoidance entries from :ref{#thm-pa-implies-cone}. Constant-bound trace avoidance of $\mathsf{RWKL}$ follows from that of $\mathsf{RT}^2_2$ (:ref{#thm-liu-closed-classes}) by Flood's reduction (:ref{#prop-rwkl-reductions}): a $Z$-computable tree gives a $Z$-computable coloring whose homogeneous sets are solutions. The pattern is that of the properties of the forcing questions: merging for PA, finite merging for traces, countable merging for DNC functions. Ramsey's theorem for pairs has the avoidance property of the second level and not that of the third.

Some relations are not settled by the course. DNC avoidance and PA avoidance are both implied by countable merging, but the course does not decide whether DNC avoidance implies PA avoidance for problems: the hypothesis "$Z$ is not DNC relative to $D$" is stronger than "$Z$ is not PA relative to $D$", so the definitions are not directly comparable. Patey's monograph observes that some problems admit DNC avoidance but not preservation of immunity, and asks whether preservation of immunity implies DNC avoidance; we do not know of a published answer.

::::exercise{#ex-dnc-avoid-rwwkl difficulty=1 objective="Combine DNC avoidance with the characterization of DNC degrees to build ω-models without solutions to an instance of $\mathsf{RWWKL}$."}
Show that if a problem admits DNC avoidance, it does not imply $\mathsf{RWWKL}$ in ω-models: there is a Turing ideal satisfying it that is not closed under $\mathsf{RWWKL}$.

:::solution
The class of the sets that are not DNC is a weakness property, preserved by the problem (DNC avoidance with $D = \emptyset$). By :ref{#lem-preservation-ideal}, some Turing ideal satisfying the problem contains no DNC function. By :ref{#prop-rwwkl-dnc} (2 ⇒ 1), it contains no homogeneous set for the computable instance $\mathcal P$ of the proof, so it does not satisfy $\mathsf{RWWKL}$.
:::
::::

## Notes and references

DNC avoidance, countably merging questions and preservation of immunity follow the sections *DNC avoidance* and *Comparing avoidances* of the chapter *Compactness avoidance* of Patey's monograph, where countable merging is called countably $\Pi^0_1$-merging; the monograph states without reference that the ascending descending sequence principle admits DNC avoidance but not preservation of immunity, and asks whether preservation of immunity implies DNC avoidance. The c.b. trace avoidance of Ramsey's theorem for pairs is due to Liu (2015).

- L. Liu, *Cone avoiding closed sets*, Transactions of the American Mathematical Society 367 (2015), 1609–1630.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, sections *DNC avoidance* and *Comparing avoidances*.

:::::exercises
::::exercise[Inverting the jump while preserving immunity]{#ex-delta2-immune-dnc difficulty=2 objective="Apply the two theorems on countably merging questions to the forcing that makes an arbitrary set $\Delta^0_2$."}
Let $I$ be an immune set and $A$ an arbitrary set. Using the forcing of :ref{#thm-delta2-pa-avoidance}, show that there is a set $G$ with $A \leq_T G'$ such that $G$ computes no DNC function and $I$ is immune relative to $G$.

:::solution
The question of :ref{#thm-delta2-pa-avoidance} is $\Sigma^0_1(\{ \emptyset \})$-preserving with $Z = \emptyset$, and if $(\sigma, m) \mathrel{?{\nvdash}} \varphi(y)$ for every $y \in R$, then $(\sigma, m)$ itself forces every $\neg \varphi(y)$, $y \in R$, as shown in the proof of :ref{#thm-delta2-cone-avoidance}: it is countably merging. By :ref{#thm-countably-merging-dnc} with $D = \emptyset$ and :ref{#thm-countably-merging-immunity} with $\mathcal M = \{ \emptyset \}$, a sufficiently generic $G$ computes no DNC function and keeps $I$ immune. The density argument of that proof gives $A \leq_T G'$. The dense sets of the two theorems and those of the limit can be met by the same generic set, and countably many immune sets can be handled at once in the same way.
:::
::::

::::exercise[Immunity and cones]{#ex-immunity-implies-cone difficulty=1 objective="Show that preservation of immunity implies cone avoidance, with the set of codes of the prefixes of a set."}
Show that every problem that admits preservation of immunity admits cone avoidance.

:::solution
Let $C \not\leq_T Z$, $X \leq_T Z$ an instance, and $I = X_C$ the set of the codes of the prefixes of $C$, as in :ref{#ex-coding-reservoir}. If $W$ is an infinite subset of $I$, c.e. relative to $Z$, then $Z$ computes $C$: to compute $C \uh n$, enumerate $W$ until an element coding a string of length at least $n$ appears, which happens since $W$ is infinite and only finitely many numbers code shorter strings. So $I$ is immune relative to $Z$, and preservation of immunity gives a solution $Y$ with $I$ immune relative to $Z \oplus Y$. If $C \leq_T Z \oplus Y$, then $I$ is computable in $Z \oplus Y$ and is an infinite subset of itself, a contradiction. So $C \not\leq_T Z \oplus Y$.
:::
::::

::::exercise[Countable, finite and binary merging]{#ex-merging-hierarchy difficulty=1 objective="Compare countable merging, finite merging and merging, and check which form of merging the PA avoidance theorem uses."}
Show that a countably merging forcing question is finitely merging, and that a finitely merging question has the following property: for every condition $c$, every $\Sigma^0_1$ formula $\varphi(y)$ and all $m_0, m_1$ with $c \mathrel{?{\nvdash}} \varphi(m_0)$ and $c \mathrel{?{\nvdash}} \varphi(m_1)$, some extension of $c$ forces $\neg \varphi(m_0) \wedge \neg \varphi(m_1)$. Show that this property suffices for the proof of :ref{#thm-local-pa-avoidance}.

:::solution
A finite set $R$ is a set, so the definition of countable merging (:ref{#def-countably-merging}) applies to it, and gives the definition of finite merging. Applying finite merging to $R = \{ m_0, m_1 \}$ gives the property. In the proof of :ref{#thm-local-pa-avoidance}, merging is used in case 2 only, for the two sentences $\Phi^{Z \oplus G}_e(x)\converge = 0$ and $\Phi^{Z \oplus G}_e(x)\converge = 1$. They are the instances $\varphi(0)$ and $\varphi(1)$ of the formula $\varphi(y)$: "$\Phi^{Z \oplus G}_e(x)\converge = y$", with $x$ fixed. So the property, with $m_0 = 0$ and $m_1 = 1$, is what case 2 needs. This is the sense in which countable merging implies finite merging, which implies merging for the sentences used in the proofs, as in the figure.
:::
::::

::::exercise[Cohesiveness preserves immunity]{#ex-coh-preserves-immunity difficulty=1 objective="Apply the abstract theorem on immunity to computable Mathias forcing relative to $Z$."}
Show that $\mathsf{COH}$ admits preservation of immunity.

:::solution
Let $I$ be immune relative to $Z$ and $\vec R \leq_T Z$. Use Mathias forcing with $Z$-computable reservoirs and the question of :ref{#thm-coh-pa-avoidance}: some string compatible with $(\sigma, X)$ satisfies the sentence. It is $\Sigma^0_1(\mathcal M)$-preserving for the class $\mathcal M$ of the sets computable in $Z$, relative to each of which $I$ is immune. It is countably merging: if no compatible string satisfies $\varphi(m)$ for any $m \in R$, then $(\sigma, X)$ itself forces every $\neg \varphi(m)$, by the use principle. By :ref{#thm-countably-merging-immunity}, $I$ is immune relative to $Z \oplus G$ for every sufficiently generic $G$, and a sufficiently generic $G$ is $\vec R$-cohesive, by the density argument of :ref{#thm-coh-pa-avoidance}.
:::
::::

::::exercise[The pigeonhole principle does not strongly avoid DNC degrees]{#ex-rt12-not-strong-dnc difficulty=1 objective="Use the infinite subsets of a random set to show that DNC avoidance of the pigeonhole principle fails for arbitrary instances."}
Say that a problem admits **strong DNC avoidance** if :ref{#def-dnc-avoidance} holds for every instance, not only for the instances computable in $Z$. Show that $\mathsf{RT}^1_2$ admits DNC avoidance, but not strong DNC avoidance.

:::solution
A $Z$-computable set $A$ has the solution $A$ or $\overline A$, computable in $Z$, so $Z \oplus Y \equiv_T Z$: $\mathsf{RT}^1_2$ admits DNC avoidance. Let $A$ be Martin-Löf random. Its complement is random too, since flipping all bits maps every Martin-Löf test to a Martin-Löf test. By :ref{#ex-random-subsets-dnc}, every infinite subset of $A$ or of $\overline A$ computes a DNC function. So with $D = Z = \emptyset$, the instance $A$ has no solution $Y$ with $Z \oplus Y$ not DNC. By contrast, $\mathsf{RT}^1_2$ admits strong PA avoidance (:ref{#thm-rt12-strong-pa}): DNC avoidance is the place where randomness, and not only compactness, is detected.
:::
::::

::::exercise[Strong DNC avoidance and Δ⁰₂ instances]{#ex-dnc-delta2-strong difficulty=2 objective="Reduce strong DNC avoidance to instances computable in the jump, with the countably merging forcing that makes a set $\Delta^0_2$."}
With the notion of :ref{#ex-rt12-not-strong-dnc}, show that a problem $\mathsf P$ admits strong DNC avoidance if and only if for all $D \leq_T Z$ with $Z$ not DNC relative to $D$, every instance $X \leq_T Z'$ has a solution $Y$ with $Z \oplus Y$ not DNC relative to $D$.

:::solution
The forward direction is a special case. Conversely, let $D \leq_T Z$ with $Z$ not DNC relative to $D$, and $X$ an arbitrary instance. Use the forcing of :ref{#thm-delta2-pa-avoidance} with $A = X$. Its question is $\Sigma^0_1(\{ Z \})$-preserving, and countably merging, since a condition with a negative answer for every $\varphi(m)$, $m \in R$, forces all the negations, as in the proof of :ref{#thm-delta2-cone-avoidance}. By :ref{#thm-countably-merging-dnc} with $\mathcal M = \{ Z \}$, every sufficiently generic $G$ has $Z \oplus G$ not DNC relative to $D$, and the density argument gives $X \leq_T G' \leq_T (Z \oplus G)'$. Since $D \leq_T Z \oplus G$, the hypothesis applied to $Z \oplus G$ gives a solution $Y$ with $Z \oplus G \oplus Y$ not DNC relative to $D$, and $Z \oplus Y$ is not DNC relative to $D$ either, since the class of sets DNC relative to $D$ is closed upwards.
:::
::::
:::::
