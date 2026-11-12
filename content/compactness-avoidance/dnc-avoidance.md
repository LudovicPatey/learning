---
title: DNC functions and the comparison of avoidances
summary: DNC degrees are the degrees that compute homogeneous sets for all Π⁰₁ classes of positive measure, so Ramsey's theorem for pairs computes DNC functions; DNC avoidance and countably merging forcing questions; preservation of immunity; the relations between cone, PA, constant-bound trace and DNC avoidance.
duration: 45
prerequisites: [measure-and-closed-classes, immunity-growth/dnc-functions, martin-lof-randomness/random-dnc]
---

The previous lessons separated three levels of compactness: full compactness ($\mathsf{WKL}$, PA degrees), its probabilistic restriction ($\mathsf{WWKL}$, random sequences), and the Ramsey-type weak König lemma, which Ramsey's theorem for pairs implies. A fourth level is the weakest: the existence of diagonally non-computable functions (:ref{#def-dnc}). A DNC function escapes every c.e. set whose size is known in advance (:ref{#thm-dnc-effectively-immune}), which is a weak form of choosing a member of a large class. This lesson shows that DNC degrees are exactly the degrees of homogeneous sets for $\Pi^0_1$ classes of positive measure, so that Ramsey's theorem for pairs computes DNC functions; it then develops the corresponding avoidance property, and compares all the avoidance properties of the course.

## The Ramsey-type weak weak König lemma

The **Ramsey-type weak weak König lemma** $\mathsf{RWWKL}$ is the restriction of $\mathsf{RWKL}$ to the infinite binary trees $T$ with $\lambda([T]) > 0$. For a finite set $F$, let $\mathcal Q_F = \{ X \in \cs : F \subseteq X \}$, a clopen class of measure $2^{-|F|}$, and $\mathcal Q_n = \mathcal Q_{\{ n \}}$.

:::proposition[Bienvenu, Patey, Shafer]{#prop-rwwkl-dnc}
For every set $X$, the following are equivalent:

1. $X$ computes a DNC function;
2. for every $\Pi^0_1$ class $\mathcal P \subseteq \cs$ of positive measure, $X$ computes an infinite set homogeneous for $\mathcal P$, that is, for a computable tree $T$ with $[T] = \mathcal P$.
:::

For the first direction, the idea is to build a homogeneous set of color $1$ by adding elements one at a time, keeping a lower bound on the measure of the members of $\mathcal P$ that contain the finite set built so far. Few numbers make this measure drop sharply, and they form a c.e. set of known size, which a DNC function can escape.

:::proof{of=prop-rwwkl-dnc}
(1 ⇒ 2) We first prove a counting fact. *Let $\mathcal C$ be a measurable class with $\lambda(\mathcal C) \geq 2^{-d}$, $d \geq 3$. Fewer than $2d$ numbers $n$ satisfy $\lambda(\mathcal C \cap \mathcal Q_n) < 2^{-2d}$.* Otherwise let $E$ be a set of $2d$ such numbers. Every $X$ either contains an element of $E$ or is disjoint from $E$, so
$$
2^{-d} \leq \lambda(\mathcal C) \leq \lambda(\{ X : X \cap E = \emptyset \}) + \sum_{n \in E} \lambda(\mathcal C \cap \mathcal Q_n) < 2^{-2d} + 2d \cdot 2^{-2d} = (2d + 1)\, 2^{-2d},
$$
that is, $2^d < 2d + 1$, which fails for $d \geq 3$.

Let $\mathcal P$ be a $\Pi^0_1$ class with $\lambda(\mathcal P) \geq 2^{-c}$, $c \geq 3$. Call a finite set $F$ **valid** if $\lambda(\mathcal P \cap \mathcal Q_F) \geq 2^{-c \cdot 2^{|F|}}$. The empty set is valid. A valid set $F$ is contained in some member of $\mathcal P$, since $\mathcal P \cap \mathcal Q_F$ has positive measure. The class $\mathcal P \cap \mathcal Q_F$ is $\Pi^0_1$, so its measure is right-c.e., uniformly in $F$ (:ref{#prop-measure-effective}), and "$F$ is not valid" is a $\Sigma^0_1$ property of $F$. By SMN, there is a computable function $a$ such that
$$
W_{a(F)} = \{ n : n \leq \max F \} \cup \{ n : F \cup \{ n \} \text{ is not valid} \},
$$
with $\{ n : n \leq \max F \} = \emptyset$ for $F = \emptyset$. If $F$ is valid, apply the counting fact to $\mathcal C = \mathcal P \cap \mathcal Q_F$ and $d = c \cdot 2^{|F|} \geq 3$: the numbers $n$ with $F \cup \{ n \}$ not valid satisfy $\lambda(\mathcal C \cap \mathcal Q_n) < 2^{-c \cdot 2^{|F| + 1}} = 2^{-2d}$, so there are fewer than $2d$ of them, and $|W_{a(F)}| \leq b(F)$, where $b(F) = \max F + 1 + 2c \cdot 2^{|F|}$ (with $\max \emptyset + 1 = 0$).

Let $h \leq_T X$ be the function of :ref{#thm-dnc-effectively-immune} (2), with $h(e, m) \notin W_e$ whenever $|W_e| \leq m$. Define $F_0 = \emptyset$ and $F_{j+1} = F_j \cup \{ n_j \}$ with $n_j = h(a(F_j), b(F_j))$. By induction, each $F_j$ is valid and $n_j > \max F_j$: since $|W_{a(F_j)}| \leq b(F_j)$, $n_j \notin W_{a(F_j)}$. The set $H = \{ n_0 < n_1 < \cdots \}$ is infinite and computable in $X$. Every finite subset of $H$ is contained in some $F_j$, hence in a member of $\mathcal P$: $H$ is homogeneous for $\mathcal P$ with color $1$.

(2 ⇒ 1) For each $e$, let $\mathcal P_e$ be the class of the sets $X$ such that, if $\Phi_e(e)$ converges to the code of a tuple $(x_0, \dots, x_{e+2})$ of $e + 3$ distinct numbers, then $X$ is not constant on $\{ x_0, \dots, x_{e+2} \}$. Its complement is $\Sigma^0_1$, uniformly in $e$, and has measure at most $2 \cdot 2^{-(e+3)}$. So $\mathcal P = \bigcap_e \mathcal P_e$ is a $\Pi^0_1$ class with
$$
\lambda(\mathcal P) \geq 1 - \sum_e 2^{-(e+2)} = \tfrac12.
$$
Let $H = \{ y_0 < y_1 < \cdots \}$ be an infinite set computable in $X$ and homogeneous for $\mathcal P$, say with color $i$, and let $f(e)$ be the code of $(y_0, \dots, y_{e+2})$; then $f \leq_T X$. If $\Phi_e(e)\converge = f(e)$, then by :ref{#prop-homogeneous-member} some $X' \in \mathcal P$ has $\{ y_0, \dots, y_{e+2} \} \subseteq X'^{-1}(i)$, so $X'$ is constant on these $e + 3$ distinct numbers, and $X' \notin \mathcal P_e$, a contradiction. So $f$ is DNC.
:::

The proof of (2 ⇒ 1) uses a single class $\mathcal P$: a homogeneous set for it computes a DNC function. Together with Flood's reduction, this gives a lower bound for Ramsey's theorem for pairs.

:::corollary{#cor-rt22-dnc}
There is a computable coloring $f : [\nat]^2 \to 2$ all of whose infinite homogeneous sets compute a DNC function. So $\mathsf{RT}^2_2$ and $\mathsf{RWKL}$ do not admit the avoidance of DNC degrees defined below, and every Turing ideal satisfying $\mathsf{RT}^2_2$ contains a DNC function.
:::

:::proof{of=cor-rt22-dnc}
Let $T$ be a computable tree with $[T] = \mathcal P$, the class of the proof of (2 ⇒ 1). Flood's coloring for $T$ (:ref{#prop-rwkl-reductions}) is computable, and its infinite homogeneous sets are homogeneous for $T$, so they compute a DNC function by the proof of (2 ⇒ 1).
:::

So the four levels form a chain: $\mathsf{WKL}$ implies $\mathsf{WWKL}$ and $\mathsf{RWKL}$, each of which implies $\mathsf{RWWKL}$, which is equivalent to the existence of DNC functions. Ramsey's theorem for pairs implies $\mathsf{RWKL}$ but neither $\mathsf{WKL}$ (Liu, 2012) nor $\mathsf{WWKL}$ (Liu, 2015), and Bienvenu, Patey and Shafer showed that $\mathsf{RWKL}$ is strictly stronger than the existence of DNC functions. In the other direction, a random sequence computes a DNC function (:ref{#cor-random-dnc}), so $\mathsf{WWKL}$ implies $\mathsf{RWWKL}$ also by this route, while some DNC functions compute no random sequence.

:::quiz[DNC functions and homogeneous sets]
In (1 ⇒ 2), why does the c.e. set $W_{a(F)}$ contain all the numbers up to $\max F$?

- [x] To make the new element larger than the elements already chosen, so that $H$ is infinite and enumerated in increasing order; the bound $b(F)$ accounts for these numbers.
- [ ] Because the numbers below $\max F$ make $F$ invalid.

  They may well keep $F$ valid; they are excluded for another reason.
- [ ] To make $W_{a(F)}$ finite.

  It is finite anyway when $F$ is valid, by the counting fact.

---

In (2 ⇒ 1), why must the $e + 3$ numbers be distinct?

- [x] So that the class of the $X$ constant on them has measure $2 \cdot 2^{-(e+3)}$; with repetitions the class would be larger, and the bound on $\lambda(\mathcal P)$ would fail.
- [ ] So that $f$ is injective.

  Injectivity of $f$ is not needed.
- [ ] Because $H$ is infinite.

  The elements of $H$ are distinct anyway; the condition concerns the values of $\Phi_e(e)$.
:::

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

The two cases of this proof are the two ways a c.e. set can fail to be an infinite subset of $I$, and they need the same property of the question as DNC avoidance. This is not a coincidence: a DNC function relative to $Z$ computes a set that is effectively immune relative to $Z$, a strong form of immunity (:ref{#thm-dnc-effectively-immune}).

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
<svg class="fig" viewBox="0 0 600 330" width="600" role="img" aria-label="Constant-bound trace avoidance implies PA avoidance, which implies cone avoidance; DNC avoidance implies cone avoidance. WWKL has PA avoidance but not c.b. trace avoidance; WKL has cone avoidance but not PA avoidance; RT22 has c.b. trace avoidance but not DNC avoidance. Finitely merging, merging and countably merging questions give c.b. trace, PA and DNC avoidance and preservation of immunity"><defs><marker id="ca-cmp-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="330" y="20" width="160" height="40" rx="6" class="state"/><text x="410.0" y="44.0" text-anchor="middle" class="label">c.b. trace avoidance</text><rect x="330" y="120" width="160" height="40" rx="6" class="state"/><text x="410.0" y="144.0" text-anchor="middle" class="label">PA avoidance</text><rect x="330" y="220" width="160" height="40" rx="6" class="state"/><text x="410.0" y="244.0" text-anchor="middle" class="label">cone avoidance</text><rect x="510" y="120" width="80" height="40" rx="6" class="state"/><text x="550.0" y="136.0" text-anchor="middle" class="label">DNC</text><text x="550.0" y="152.0" text-anchor="middle" class="label">avoidance</text><rect x="20" y="20" width="170" height="40" rx="6" class="cell"/><text x="105.0" y="44.0" text-anchor="middle" class="label">finitely merging</text><rect x="20" y="120" width="170" height="40" rx="6" class="cell"/><text x="105.0" y="144.0" text-anchor="middle" class="label">merging</text><rect x="20" y="220" width="170" height="40" rx="6" class="cell"/><text x="105.0" y="244.0" text-anchor="middle" class="label">countably merging</text><line x1="410" y1="62" x2="410" y2="116" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="410" y1="162" x2="410" y2="216" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="550" y1="162" x2="470" y2="216" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="192" y1="40" x2="326" y2="40" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><line x1="192" y1="140" x2="326" y2="140" class="ink-stroke" stroke-width="1.3" marker-end="url(#ca-cmp-arr)"/><path d="M192,248 C300,300 520,300 550,164" class="ink-stroke" stroke-width="1.3" fill="none" marker-end="url(#ca-cmp-arr)"/><text x="418" y="94" class="label">converse fails: WWKL</text><text x="402" y="194" text-anchor="end" class="label">converse fails: WKL</text><text x="250" y="312" class="label">also preservation of immunity</text><text x="20" y="106" class="label muted">questions (sufficient conditions)</text><text x="310" y="80" class="label muted" text-anchor="end">RT²₂: c.b. trace yes, DNC no</text></svg>
:::

The following table summarizes what the course proves about the main problems.

| problem | cone | PA | c.b. trace | DNC |
| --- | --- | --- | --- | --- |
| $\mathsf{COH}$ | yes | yes | yes | yes |
| $\mathsf{WKL}$ | yes | no | no | no |
| $\mathsf{WWKL}$ | yes | yes | no | no |
| $\mathsf{RWKL}$ | yes | yes | yes (Liu, admitted) | no |
| $\mathsf{RT}^2_2$ | yes | yes | yes (Liu, admitted) | no |
| $\mathsf{RT}^3_2$ | no | no | no | no |

The entries for $\mathsf{COH}$ come from :ref{#thm-coh-pa-avoidance} and its variants with finitely and countably merging questions; those for $\mathsf{WKL}$ from the class $\mathrm{DNC}_2$; those for $\mathsf{WWKL}$ from :ref{#thm-wwkl-strong-pa}, :ref{#prop-random-no-trace} and :ref{#cor-random-dnc}; those for $\mathsf{RWKL}$ and $\mathsf{RT}^2_2$ from Liu's theorems and :ref{#cor-rt22-dnc}; the cone avoidance entries from :ref{#thm-pa-implies-cone}. Constant-bound trace avoidance of $\mathsf{RWKL}$ is proved by Liu (2015) with the forcing of :ref{to="compactness-avoidance/partition-forcing"}, blocks replacing valuations. The pattern is that of the properties of the forcing questions: merging for PA, finite merging for traces, countable merging for DNC functions. Ramsey's theorem for pairs has the second property and not the third.

Some relations are not settled by the course. DNC avoidance and PA avoidance are both implied by countable merging, but the course does not decide whether DNC avoidance implies PA avoidance for problems: the hypothesis "$Z$ is not DNC relative to $D$" is stronger than "$Z$ is not PA relative to $D$", so the definitions are not directly comparable. Patey's monograph observes that some problems admit DNC avoidance but not preservation of immunity, and asks whether preservation of immunity implies DNC avoidance; we do not know of a published answer.

## Exercises

::::exercise{difficulty=1}
Show that if a problem admits DNC avoidance, it does not imply $\mathsf{RWWKL}$ in ω-models: there is a Turing ideal satisfying it that is not closed under $\mathsf{RWWKL}$.

:::solution
The class of the sets that are not DNC is a weakness property, preserved by the problem (DNC avoidance with $D = \emptyset$). By :ref{#lem-preservation-ideal}, some Turing ideal satisfying the problem contains no DNC function. By :ref{#prop-rwwkl-dnc} (2 ⇒ 1), it contains no homogeneous set for the computable instance $\mathcal P$ of the proof, so it does not satisfy $\mathsf{RWWKL}$.
:::
::::

::::exercise{difficulty=2}
Let $I$ be an immune set and $A$ an arbitrary set. Using the forcing of :ref{#thm-delta2-pa-avoidance}, show that there is a set $G$ with $A \leq_T G'$ such that $G$ computes no DNC function and $I$ is immune relative to $G$.

:::solution
The question of :ref{#thm-delta2-pa-avoidance} is $\Sigma^0_1(\{ \emptyset \})$-preserving with $Z = \emptyset$, and if $(\sigma, m) \mathrel{?{\nvdash}} \varphi(y)$ for every $y \in R$, then $(\sigma, m)$ itself forces every $\neg \varphi(y)$, $y \in R$, as shown in the proof of :ref{#thm-delta2-cone-avoidance}: it is countably merging. By :ref{#thm-countably-merging-dnc} with $D = \emptyset$ and :ref{#thm-countably-merging-immunity} with $\mathcal M = \{ \emptyset \}$, a sufficiently generic $G$ computes no DNC function and keeps $I$ immune. The density argument of that proof gives $A \leq_T G'$. The dense sets of the two theorems and those of the limit can be met by the same generic set, and countably many immune sets can be handled at once in the same way.
:::
::::

## Notes and references

The equivalence between DNC degrees and homogeneous sets for $\Pi^0_1$ classes of positive measure is due to Bienvenu, Patey and Shafer (2017), who introduced $\mathsf{RWWKL}$, proved its equivalence with the existence of DNC functions over $\mathsf{RCA}_0$, and showed that $\mathsf{RWKL}$ is strictly stronger; Flood and Towsner (2016) separated $\mathsf{RWKL}$ from the existence of DNC functions independently. Flood (2012) had shown that $\mathsf{RWKL}$ implies the existence of DNC functions. The proof given here follows the chapter *Compactness avoidance* of Patey's monograph, section *DNC and compactness*, with the tuples of length $e + 3$ in the second direction; it uses the characterization of DNC degrees by escaping functions (:ref{#thm-dnc-effectively-immune}), which the monograph attributes to Bienvenu, Patey and Shafer and which is also proved by Monin and Patey in the chapter *Immunity and function growth*. DNC avoidance, countably merging questions and preservation of immunity follow the sections *DNC avoidance* and *Comparing avoidances* of the monograph, where countable merging is called countably $\Pi^0_1$-merging. That a random sequence computes a DNC function, and that some DNC functions compute no random sequence, are in the course on Martin-Löf randomness.

- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71; arXiv:1411.5874.
- S. Flood, *Reverse mathematics and a Ramsey-type König's lemma*, Journal of Symbolic Logic 77 (2012), 1272–1280.
- S. Flood and H. Towsner, *Separating principles below WKL₀*, Mathematical Logic Quarterly 62 (2016), 507–529; arXiv:1410.4068.
- L. Liu, *Cone avoiding closed sets*, Transactions of the American Mathematical Society 367 (2015), 1609–1630.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, sections *DNC and compactness*, *DNC avoidance* and *Comparing avoidances*.
