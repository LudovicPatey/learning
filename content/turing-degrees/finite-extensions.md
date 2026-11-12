---
title: The finite extension method
summary: Constructions by finite extensions; the Kleene–Post theorem on incomparable degrees below 0′; avoiding the cone above a non-computable set; 1-generic sets.
duration: 55
prerequisites: [turing-jump, countability/requirements]
---

Many questions about the Turing degrees ask for a set that is neither too strong nor too weak: a set that does not compute some given set, but that is not computable either. Such sets are built by **finite extensions**: the set is determined by an increasing sequence of strings, and each requirement it must satisfy is secured by a finite piece of information. This method appeared in the course on countability (:ref{#lem-finite-extension}); here it is applied to requirements about oracle computations, where the use principle makes it work. The constructions answer the first questions about the structure of the degrees: the order is not linear, and there are degrees strictly between $\obf$ and $\obf'$.

## Dense sets of strings

Requirements are expressed through sets of strings.

:::definition{#def-dense}
A set $D \subseteq \bstr$ is **dense** if every string has an extension in $D$: for every $\sigma$ there is $\tau \succeq \sigma$ with $\tau \in D$. A set $X \in \cs$ **meets** $D$ if some prefix of $X$ belongs to $D$.
:::

The idea is that $D$ is the set of strings that **force** a requirement: every $X$ extending a string of $D$ satisfies it. Density says that the requirement can always be forced, whatever finite part of $X$ has already been fixed.

:::lemma{#lem-meet-dense}
Let $(D_n)_{n \in \nat}$ be a sequence of dense sets. Then some $X$ meets every $D_n$. Moreover, if there is a $Z$-computable function $h$ such that $h(n, \sigma) \succeq \sigma$ and $h(n, \sigma) \in D_n$ for all $n$ and $\sigma$, then such an $X$ can be taken $Z$-computable.
:::

:::proof{of=lem-meet-dense}
Let $h$ be any function with $h(n, \sigma) \succeq \sigma$ and $h(n, \sigma) \in D_n$ for all $n$ and $\sigma$; for the first statement, take $h(n, \sigma)$ to be the first extension of $\sigma$ in $D_n$, in a fixed computable enumeration of $\bstr$. Define $\sigma_0 = \varepsilon$ and $\sigma_{n+1} = h(n, \sigma_n)\, 0$. The strings $\sigma_0 \prec \sigma_1 \prec \cdots$ have strictly increasing lengths, and determine a unique $X$ with $\sigma_n \prec X$ for every $n$. Since $h(n, \sigma_n) \prec X$ belongs to $D_n$, $X$ meets $D_n$. If $h$ is $Z$-computable, so is the sequence $(\sigma_n)$, and $X(k)$ is the bit at position $k$ of $\sigma_{k+1}$, whose length exceeds $k$; so $X \leq_T Z$.
:::

The appended bit $0$ ensures that the lengths increase; it does no harm, since a string extending a member of $D_n$ still forces what that member forces. The lemma isolates the combinatorial core of the method; in each application below, the work consists in showing that the relevant sets of strings are dense, and in measuring how much oracle is needed to find extensions in them.

## Incomparable degrees

:::theorem[Kleene–Post]{#thm-kleene-post}
There are sets $A$ and $B$, both computable in $\emptyset'$, such that $A \not\leq_T B$ and $B \not\leq_T A$.
:::

:::proof{of=thm-kleene-post}
We build $A$ and $B$ together, by finite extensions of a pair of strings. The requirements are, for every $e$:
$$
\mathcal R_e : \Phi^A_e \neq B, \qquad \mathcal S_e : \Phi^B_e \neq A.
$$
If all are satisfied, then $A \not\leq_T B$ and $B \not\leq_T A$. Here $\Phi^A_e \neq B$ means that for some $x$, either $\Phi^A_e(x)\diverge$ or $\Phi^A_e(x)\converge \neq B(x)$.

We define pairs of strings $(\sigma_n, \tau_n)$ with $\sigma_n \preceq \sigma_{n+1}$ and $\tau_n \preceq \tau_{n+1}$, starting from $(\varepsilon, \varepsilon)$, and let $A$ and $B$ be the limits. At step $n = 2e$ we satisfy $\mathcal R_e$, at step $n = 2e + 1$ we satisfy $\mathcal S_e$, and at the end of each step we append the bit $0$ to both strings, so that the lengths tend to infinity.

*Satisfying $\mathcal R_e$.* Let $x = |\tau_n|$, the first position at which $B$ is not yet determined.

- If there is a string $\sigma \succeq \sigma_n$ with $\Phi^\sigma_e(x)\converge$, take the string $\sigma$ of the first pair $(\sigma, s)$, in a fixed computable enumeration of pairs, such that $\sigma \succeq \sigma_n$ and $\Phi^\sigma_e(x)[s]\converge$; let $i = \Phi^\sigma_e(x)$, and set $\sigma_{n+1} = \sigma$ and $\tau_{n+1} = \tau_n\, j$ with $j = 1 - i$ if $i \in \{0, 1\}$ and $j = 0$ otherwise. For every $A \succ \sigma$, the use principle gives $\Phi^A_e(x) = i \neq B(x)$.
- Otherwise, set $\sigma_{n+1} = \sigma_n$ and $\tau_{n+1} = \tau_n$. For every $A \succ \sigma_n$, $\Phi^A_e(x)\diverge$: a convergent computation would converge already with a prefix of $A$ extending $\sigma_n$ (:ref{#prop-oracle-stages}).

In both cases, $\mathcal R_e$ holds for every pair of sets extending $(\sigma_{n+1}, \tau_{n+1})$, and therefore for $(A, B)$. The requirements $\mathcal S_e$ are satisfied symmetrically.

:::figure[The first steps of the Kleene–Post construction, in the case where every search succeeds. At step $\mathcal R_0$, the string for $A$ is extended until $\Phi_0$ converges at the first free position $x$ of $B$, and $B(x)$ is set to the opposite value; at step $\mathcal S_0$ the roles are exchanged. Each step ends by appending $0$ to both strings.]
<svg class="fig" viewBox="0 0 520 200" width="520" role="img" aria-label="The first three steps of the Kleene–Post construction: each step extends one string by a search and the other by one diagonal bit"><defs><marker id="ah-kp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><text x="64" y="58" text-anchor="end" class="math" font-size="17">A</text><rect x="80" y="40" width="26" height="26" class="cell head-cell"/><rect x="106" y="40" width="26" height="26" class="cell head-cell"/><rect x="132" y="40" width="26" height="26" class="cell head-cell"/><rect x="158" y="40" width="26" height="26" class="cell head-cell"/><text x="132.0" y="30" text-anchor="middle" class="math muted" font-size="15">R<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="184" y="40" width="26" height="26" class="cell"/><text x="197.0" y="58" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="210" y="40" width="26" height="26" class="cell"/><rect x="214" y="44" width="18" height="18" class="accent-fill" opacity="0.85"/><text x="223.0" y="30" text-anchor="middle" class="math muted" font-size="15">S<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="236" y="40" width="26" height="26" class="cell"/><text x="249.0" y="58" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="262" y="40" width="26" height="26" class="cell head-cell"/><rect x="288" y="40" width="26" height="26" class="cell head-cell"/><rect x="314" y="40" width="26" height="26" class="cell head-cell"/><text x="301.0" y="30" text-anchor="middle" class="math muted" font-size="15">R<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="340" y="40" width="26" height="26" class="cell"/><text x="353.0" y="58" text-anchor="middle" class="mrm muted" font-size="14">0</text><text x="374" y="58" class="mrm muted" font-size="15">⋯</text><text x="64" y="138" text-anchor="end" class="math" font-size="17">B</text><rect x="80" y="120" width="26" height="26" class="cell"/><rect x="84" y="124" width="18" height="18" class="accent-fill" opacity="0.85"/><text x="93.0" y="166" text-anchor="middle" class="math muted" font-size="15">R<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="106" y="120" width="26" height="26" class="cell"/><text x="119.0" y="138" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="132" y="120" width="26" height="26" class="cell head-cell"/><rect x="158" y="120" width="26" height="26" class="cell head-cell"/><rect x="184" y="120" width="26" height="26" class="cell head-cell"/><rect x="210" y="120" width="26" height="26" class="cell head-cell"/><rect x="236" y="120" width="26" height="26" class="cell head-cell"/><text x="197.0" y="166" text-anchor="middle" class="math muted" font-size="15">S<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="262" y="120" width="26" height="26" class="cell"/><text x="275.0" y="138" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="288" y="120" width="26" height="26" class="cell"/><rect x="292" y="124" width="18" height="18" class="accent-fill" opacity="0.85"/><text x="301.0" y="166" text-anchor="middle" class="math muted" font-size="15">R<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="314" y="120" width="26" height="26" class="cell"/><text x="327.0" y="138" text-anchor="middle" class="mrm muted" font-size="14">0</text><text x="348" y="138" class="mrm muted" font-size="15">⋯</text><path d="M132.0,66 C132.0,96 93.0,90 93.0,118" class="ink-stroke" stroke-width="1.2" marker-end="url(#ah-kp)"/><path d="M197.0,118 C197.0,90 223.0,96 223.0,68" class="ink-stroke" stroke-width="1.2" marker-end="url(#ah-kp)"/><rect x="300" y="176" width="14" height="14" class="cell head-cell"/><text x="320" y="187" class="label">extension found by search</text><rect x="80" y="176" width="14" height="14" class="cell"/><rect x="83" y="179" width="8" height="8" class="accent-fill"/><text x="100" y="187" class="label">diagonal bit</text><text x="190" y="187" class="label">0: padding</text></svg>
:::

*Effectivity.* The only non-computable step is the case distinction, the question "is there $\sigma \succeq \sigma_n$ with $\Phi^\sigma_e(x)\converge$?". It is a c.e. question about $(e, x, \sigma_n)$, so $\emptyset'$ answers it; and in the first case, the string $\sigma$ is then found by a computable search. So the whole sequence of pairs is computable in $\emptyset'$, and so are $A$ and $B$.
:::

:::corollary{#cor-intermediate-degree}
The Turing degrees are not linearly ordered, and there is a degree $\abf$ with $\obf < \abf < \obf'$.
:::

:::proof{of=cor-intermediate-degree}
The first statement is the theorem. For the second, take $\abf = \deg_T(A)$. If $A$ were computable, then $A \leq_T B$. If $A \equiv_T \emptyset'$, then $B \leq_T \emptyset' \leq_T A$. Both are excluded, so $\obf < \abf < \obf'$.
:::

:::quiz[the Kleene–Post theorem]
In the satisfaction of $\mathcal R_e$, why is the position $x$ chosen as $|\tau_n|$?

- [x] Because $B(x)$ is not yet determined at this position, so it can be chosen to differ from the value of $\Phi^A_e(x)$.

  At positions below $|\tau_n|$, the bit of $B$ is already fixed, and $\Phi^A_e(x)$ may agree with it.
- [ ] Because $\Phi^A_e$ is only defined at $|\tau_n|$.

  $\Phi^A_e$ is a partial function defined on any inputs; the position is chosen because $B$ is still free there.
- [ ] To make the construction computable.

  The choice of $x$ is computable in any case; the point is the freedom on $B(x)$.

---

In the second case, why does $\Phi^A_e(x)$ diverge for every $A$ extending $\sigma_n$?

- [x] If it converged, it would converge with a finite prefix of $A$, which can be taken to extend $\sigma_n$, contradicting the case hypothesis.

  This is where the use principle enters: convergence is always witnessed by a string.
- [ ] Because $\Phi_e$ is partial.

  Partiality alone says nothing about this particular computation.
- [ ] Because $A$ is not yet determined.

  The statement concerns every possible completion of $\sigma_n$; the argument shows that none makes the computation converge.

---

Why are $A$ and $B$ computable in $\emptyset'$ and not merely in $\emptyset''$?

- [x] Each step asks only whether some string makes a computation converge, which is a c.e. question.

  Questions of the form "does every extension diverge?" are complements of c.e. questions, and are also answered by $\emptyset'$.
- [ ] Because each requirement concerns a single position $x$.

  The position is fixed, but the question ranges over all extensions of $\sigma_n$; what matters is that it is a c.e. question.
- [ ] Because $A$ and $B$ are c.e.

  They need not be c.e.: the construction fixes the bits of both sets, $0$ or $1$, in an order unrelated to any enumeration.
:::

## Avoiding a cone

In the Kleene–Post theorem both sets are built. The following result fixes one of them in advance: every non-computable set has a set incomparable with it. The upper cone $\{ X : C \leq_T X \}$ of a non-computable set $C$ is avoided by satisfying the requirements $\Phi^X_e \neq C$, and the hypothesis that $C$ is not computable is exactly what makes them dense.

:::theorem[Cone avoidance]{#thm-cone-avoidance}
Let $C$ be a non-computable set. For every $e$, the set
$$
D_e = \{ \tau : \exists x\ \Phi^\tau_e(x)\converge \neq C(x) \} \cup \{ \tau : \exists x\ \forall \rho \succeq \tau\ \ \Phi^\rho_e(x)\diverge \}
$$
is dense. Consequently, for every set $A$, there is a set $B$ with $C \not\leq_T B$ and $B \not\leq_T A$.
:::

:::proof{of=thm-cone-avoidance}
Every $X$ meeting $D_e$ satisfies $\Phi^X_e \neq C$: in the first case, $\Phi^X_e(x)\converge \neq C(x)$ by the use principle; in the second, $\Phi^X_e(x)\diverge$ by :ref{#prop-oracle-stages}.

Let $\sigma$ be a string, and suppose that no extension of $\sigma$ belongs to $D_e$. Then for every $x$ there is $\rho \succeq \sigma$ with $\Phi^\rho_e(x)\converge$, since otherwise $\sigma$ itself would be in the second part of $D_e$; and for every such $\rho$, $\Phi^\rho_e(x) = C(x)$, since otherwise $\rho$ would be in the first part. Then $C$ is computable: to compute $C(x)$, search for a string $\rho \succeq \sigma$ and a stage $s$ with $\Phi^\rho_e(x)[s]\converge$, and output its value. This contradicts the hypothesis on $C$. So $D_e$ is dense.

By :ref{#lem-meet-dense}, some $B$ meets every $D_e$, and then $C \not\leq_T B$. To ensure also $B \not\leq_T A$, add the dense sets $E_e = \{ \tau : \exists x < |\tau|\ \ \Phi^A_e(x)\converge \neq \tau(x) \} \cup \{ \tau : \exists x < |\tau|\ \ \Phi^A_e(x)\diverge \}$: given $\sigma$, let $x = |\sigma|$; if $\Phi^A_e(x)\converge = i$, the string $\sigma\, (1 - i)$ belongs to $E_e$ (with $1 - i$ replaced by $0$ if $i \notin \{0, 1\}$), and otherwise $\sigma 0$ does. A set meeting every $E_e$ is not computable in $A$.
:::

The hypothesis on $C$ cannot be dropped: if $C$ is computable, say $C = \Phi_e^X$ for every $X$ with a machine $e$ that ignores its oracle, then no string belongs to $D_e$, and every set computes $C$.

Taking $A = C$ gives a set $B$ incomparable with $C$. So every non-computable degree is incomparable with some degree; in particular no degree other than $\obf$ is comparable with all degrees.

:::quiz[cone avoidance]
Where is the hypothesis that $C$ is not computable used?

- [x] To show that $D_e$ is dense: if some $\sigma$ had no extension in $D_e$, the computations above $\sigma$ would all converge to $C$, and $C$ would be computable.
- [ ] To show that a set meeting $D_e$ satisfies $\Phi^X_e \neq C$.

  This holds for every $C$.
- [ ] To apply the lemma on dense sets.

  The lemma applies to any sequence of dense sets.

---

In the proof of density, why does the search "find $\rho \succeq \sigma$ with $\Phi^\rho_e(x)\converge$" always give the correct value $C(x)$?

- [x] Because a string $\rho \succeq \sigma$ with $\Phi^\rho_e(x)\converge \neq C(x)$ would belong to $D_e$, which is excluded.
- [ ] Because the search finds the first such $\rho$.

  Any such $\rho$ gives the correct value; the order of the search only matters for termination.
- [ ] Because $\Phi_e$ computes $C$.

  Nothing is assumed about $\Phi_e$; the conclusion that it would compute $C$ above $\sigma$ is what leads to a contradiction.
:::

## 1-generic sets

The sets built by the most general finite extension arguments share a common property, genericity, which can be defined once and for all.

:::definition{#def-1-generic}
A set $G$ is **1-generic** if for every c.e. set of strings $W$, there is a prefix $\sigma \prec G$ such that either $\sigma \in W$, or no extension of $\sigma$ belongs to $W$.
:::

In words: for every c.e. property of strings, $G$ either meets it, or has a prefix beyond which it can never be met. Equivalently, $G$ meets the dense set $W \cup \{ \sigma : \text{no extension of } \sigma \text{ is in } W \}$ for every c.e. $W$. The definition does not require $W$ to be dense; when $W$ is dense, the second alternative is impossible, and $G$ meets $W$.

:::example{#ex-1-generic}
For each $n$, the set $W_n$ of strings containing $n$ consecutive $1$s is computable and dense, so every 1-generic set contains $n$ consecutive integers, for every $n$. Likewise it contains $n$ consecutive non-elements. In particular the set of even numbers is not 1-generic, and neither is any set whose elements are spread out in a computable pattern. A 1-generic set looks typical from the point of view of c.e. properties of its prefixes.
:::

:::proposition{#prop-1-generic}
1. There is a 1-generic set computable in $\emptyset'$.
2. Every 1-generic set is non-computable; in fact it is neither c.e. nor co-c.e.
:::

:::proof{of=prop-1-generic}
1. Fix a computable enumeration $(W'_n)$ of the c.e. sets of strings, say $W'_n = \{ \tau : \text{the code of } \tau \text{ is in } W_n \}$. The sets $D_n = W'_n \cup \{ \sigma : \forall \tau \succeq \sigma\ \tau \notin W'_n \}$ are dense: a string either has an extension in $W'_n$, or belongs to the second part. The function $h(n, \sigma)$ which asks $\emptyset'$ whether some $\tau \succeq \sigma$ belongs to $W'_n$ — a c.e. question — and returns the first such $\tau$ found by enumerating $W'_n$ if so, and $\sigma$ otherwise, is computable in $\emptyset'$. Apply :ref{#lem-meet-dense}.
2. Let $G$ be 1-generic. First, $G$ is infinite: for each $m$, every string has an extension in the c.e. set $V_m = \{ \sigma : \exists x \geq m\ \sigma(x) = 1 \}$, so $G$ cannot have a prefix without extension in $V_m$, and therefore meets $V_m$; that is, $G$ has an element $x \geq m$. Symmetrically, $\nat \setminus G$ is infinite. Now suppose $G$ is c.e. The set $W = \{ \sigma : \exists x < |\sigma|\ (\sigma(x) = 0 \wedge x \in G) \}$ is c.e., and no prefix of $G$ belongs to it, since a prefix of $G$ has the bit $1$ at every element of $G$. So some $\sigma \prec G$ has no extension in $W$. But if $x \geq |\sigma|$ belongs to $G$, the string obtained by extending $\sigma$ with $0$s up to position $x$ included is in $W$. Hence $G$ has no element $x \geq |\sigma|$, contradicting its infiniteness. If $\nat \setminus G$ is c.e., the same argument applies to $W = \{ \sigma : \exists x < |\sigma|\ (\sigma(x) = 1 \wedge x \notin G) \}$, and shows that $\nat \setminus G$ is finite. In particular $G$ is not computable.
:::

In the lesson on low and high sets, 1-generic sets computable in $\emptyset'$ provide non-computable sets whose jump is as small as possible.

## Exercises

::::exercise{difficulty=1}
Show that every sequence $(\dbf_n)_{n \in \nat}$ of degrees has an upper bound.

:::solution
Choose representatives $X_n \in \dbf_n$, and let $Z = \bigoplus_n X_n$, defined by $Z(\langle n, m \rangle) = X_n(m)$ (:ref{#def-join}). Each $X_n$ is computable from $Z$, by $X_n(m) = Z(\langle n, m \rangle)$, so $\deg_T(Z)$ is an upper bound.
:::
::::

::::exercise{difficulty=2}
Show that there is a sequence $(A_n)_{n \in \nat}$ of sets, uniformly computable in $\emptyset'$, such that $A_n \not\leq_T A_m$ for all $n \neq m$.

:::solution
Build all the sets at once by finite extensions of finite tuples of strings: at step $t$, strings $\sigma_{0,t}, \dots, \sigma_{t,t}$ approximate $A_0, \dots, A_t$. Requirements: $\Phi^{A_m}_e \neq A_n$ for all $e$ and $n \neq m$; at step $t$, treat the requirement with $\langle e, n, m \rangle = t$, if $n \neq m$ (otherwise do nothing), which only involves sets already started, since $n, m \leq \langle e, n, m \rangle$. To satisfy $\Phi^{A_m}_e \neq A_n$, let $x = |\sigma_{n,t}|$; if some $\rho \succeq \sigma_{m,t}$ has $\Phi^\rho_e(x)\converge = i$, extend $\sigma_{m,t}$ to $\rho$ and $\sigma_{n,t}$ by the bit $1 - i$ (or $0$); otherwise do nothing. Then extend every string by one bit and start a new string for $A_{t+1}$. As in :ref{#thm-kleene-post}, the case distinction is a c.e. question and each step is computable in $\emptyset'$. Since every string grows at each step after it is started, $A_n(k)$ is computed with oracle $\emptyset'$ by running the construction until the string for $A_n$ has length greater than $k$, uniformly in $n$ and $k$.
:::
::::

::::exercise{difficulty=2}
Show that if $G$ is 1-generic, then $\nat \setminus G$ is 1-generic.

:::solution
Let $\bar\sigma$ be the string obtained from $\sigma$ by flipping all its bits; $\sigma \mapsto \bar\sigma$ is a computable bijection of $\bstr$ that preserves prefixes, and the prefixes of $\nat \setminus G$ are the strings $\bar\sigma$ for $\sigma \prec G$. If $W$ is a c.e. set of strings, so is $\bar W = \{ \bar\sigma : \sigma \in W \}$. Some $\sigma \prec G$ is in $\bar W$ or has no extension in $\bar W$; then $\bar\sigma \prec \nat \setminus G$ is in $W$ or has no extension in $W$.
:::
::::

## Notes and references

The incomparable degrees below $\obf'$ are due to Kleene and Post (1954), who introduced the finite extension method (Soare 2016, Theorem 6.1.1; Downey and Hirschfeldt 2010, Theorem 2.10.2; Nies 2009, §1.6). The cone avoidance theorem is folklore; Soare (2016, Theorem 6.2.6) gives the case $A = C$, with the additional bound $B \leq_T C'$. The density of the sets $D_e$ says that the upper cone of a non-computable set is meager, as the course on Cohen genericity explains; the cone is also null, by a theorem of Sacks (1963), which also follows from earlier work of de Leeuw, Moore, Shannon and Shapiro (1956) (Downey and Hirschfeldt 2010, §8.12). 1-generic sets were introduced by Jockusch (1980), following Feferman's adaptation of Cohen's forcing to arithmetic (1965); they are studied in the course on Cohen genericity (Soare 2016, §6.3; Downey and Hirschfeldt 2010, §2.24).

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- G. E. Sacks, *Degrees of Unsolvability*, Annals of Mathematics Studies 55, Princeton University Press, 1963.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §§6.1–6.3.
