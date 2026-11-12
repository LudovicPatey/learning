---
title: Cohesiveness and restricted reservoirs
summary: Mathias forcing with arbitrary computable reservoirs produces high sets; restricting the reservoirs to the Boolean combinations chosen along one path of decisions gives a notion of forcing with a Σ⁰₂ question, and cohesive sets that avoid a cone and a jump cone at once.
duration: 45
prerequisites: [sigma2-questions, ramsey-theorem/cohesiveness]
---

Computable Mathias forcing gives cohesive sets with a good control of the first jump (:ref{#thm-mathias-coh-preservation}), but its sufficiently generic sets are high (:ref{#prop-mathias-dominant}). Two diagnoses of the failure lead to the same remedy.

- **The reservoirs are too sparse.** The proof of :ref{#prop-mathias-dominant} thins the reservoir to a set whose elements grow faster than a given computable function. The construction of a cohesive set never needs such a thinning: it only splits the reservoir along one of the sets $R_n$, keeping a part that is infinite. If the reservoirs are only the Boolean combinations of the sets $R_n$, they cannot be thinned arbitrarily.
- **The partial order is too complex.** The lifted question quantifies over all extensions, hence over indices of infinite computable subsets of the reservoir, a $\Pi^0_2$ property (:ref{#ex-lifted-questions}). If the reservoir is determined by a finite amount of information, the quantification becomes a search over finite objects.

The remedy is to keep the reservoirs that the construction of a cohesive set needs and nothing else. Monin and Patey state it as a general principle: to obtain second-jump control, take a notion of forcing with a good first-jump control and restrict its partial order to the conditions that the construction actually uses. This lesson carries this out for cohesiveness. The choice of the Boolean combinations is made in advance, along a path through a tree of decisions; the path must be chosen so as not to help computing the set to be avoided.

## The tree of decisions

Fix a computable sequence of sets $\vec R = (R_n)$. For a string $\rho$, let
$$
R_\rho = \bigcap_{n < |\rho|,\ \rho(n) = 0} R_n \ \cap \bigcap_{n < |\rho|,\ \rho(n) = 1} \overline{R_n},
$$
with $R_\varepsilon = \nat$. A set $G$ is $\vec R$-cohesive (:ref{#def-cohesive}) if and only if it is infinite and for every $n$ there is $\rho$ of length $n$ with $G \subseteq^* R_\rho$: the string $\rho$ records on which side of each $R_i$, $i < n$, the set $G$ lies.

:::lemma{#lem-decision-tree}
Let $T$ be the set of strings $\rho$ such that $R_\rho$ has an element larger than $|\rho|$. Then $T$ is a c.e. tree, it has an infinite path, and $R_{P \uh n}$ is infinite for every path $P$ of $T$ and every $n$.
:::

:::proof{of=lem-decision-tree}
The relation "$x \in R_\rho$" is computable in $x$ and $\rho$, so $T$ is c.e. If $\rho' \preceq \rho$ and $\rho \in T$, an element $x > |\rho|$ of $R_\rho$ belongs to $R_{\rho'} \supseteq R_\rho$ and satisfies $x > |\rho'|$; so $T$ is a tree. Let $P$ be a path and $n \in \nat$. For every $m \geq n$, $R_{P \uh m}$ has an element larger than $m$, and $R_{P \uh m} \subseteq R_{P \uh n}$; so $R_{P \uh n}$ has arbitrarily large elements. Finally, if $R_\rho$ is infinite, then $R_{\rho 0} = R_\rho \cap R_{|\rho|}$ or $R_{\rho 1} = R_\rho \setminus R_{|\rho|}$ is infinite; starting from $R_\varepsilon = \nat$, this defines a sequence of strings with infinite sets $R_\rho$, which are in $T$, and whose union is a path.
:::

The tree $T$ is computable in $\emptyset'$, so its paths form a non-empty $\Pi^0_1(\emptyset')$ class. This is the class of decisions of :ref{to="ramsey-theorem/cohesiveness"}, presented through the sets $R_\rho$.

:::figure[The tree of decisions for a sequence $R_0, R_1, \dots$. A node $\rho$ is labeled by the set $R_\rho$ of numbers lying on the sides of $R_0, \dots, R_{|\rho| - 1}$ given by $\rho$; the nodes with $R_\rho$ finite are eventually outside the tree. A path $P$ is fixed in advance, and the conditions $(\sigma, n)$ use the reservoir $R_{P \uh n}$, which shrinks along $P$.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="The binary tree of decisions: each node rho is labeled by the set R_rho; a path P is drawn in the accent color, and the condition (sigma, n) uses the reservoir R of P restricted to n"><line x1="345.0" y1="36" x2="217.5" y2="72" class="accent-stroke" stroke-width="2"/><line x1="345.0" y1="36" x2="472.5" y2="72" class="muted-stroke" stroke-width="1"/><line x1="217.5" y1="94" x2="153.8" y2="130" class="muted-stroke" stroke-width="1"/><line x1="217.5" y1="94" x2="281.2" y2="130" class="accent-stroke" stroke-width="2"/><line x1="472.5" y1="94" x2="408.8" y2="130" class="muted-stroke" stroke-width="1"/><line x1="472.5" y1="94" x2="536.2" y2="130" class="muted-stroke" stroke-width="1"/><line x1="153.8" y1="152" x2="121.9" y2="188" class="muted-stroke" stroke-width="1"/><line x1="153.8" y1="152" x2="185.6" y2="188" class="muted-stroke" stroke-width="1"/><line x1="281.2" y1="152" x2="249.4" y2="188" class="muted-stroke" stroke-width="1"/><line x1="281.2" y1="152" x2="313.1" y2="188" class="accent-stroke" stroke-width="2"/><line x1="408.8" y1="152" x2="376.9" y2="188" class="muted-stroke" stroke-width="1"/><line x1="408.8" y1="152" x2="440.6" y2="188" class="muted-stroke" stroke-width="1"/><line x1="536.2" y1="152" x2="504.4" y2="188" class="muted-stroke" stroke-width="1"/><line x1="536.2" y1="152" x2="568.1" y2="188" class="muted-stroke" stroke-width="1"/><rect x="328.0" y="15" width="34" height="22" rx="4" class="head-cell"/><text x="345.0" y="31" text-anchor="middle" class="mrm" font-size="13">ℕ</text><rect x="196.5" y="73" width="42" height="22" rx="4" class="head-cell"/><text x="217.5" y="89" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">0</tspan></text><rect x="451.5" y="73" width="42" height="22" rx="4" class="cell"/><text x="472.5" y="89" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">1</tspan></text><rect x="128.8" y="131" width="50" height="22" rx="4" class="cell"/><text x="153.8" y="147" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">00</tspan></text><rect x="256.2" y="131" width="50" height="22" rx="4" class="head-cell"/><text x="281.2" y="147" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">01</tspan></text><rect x="383.8" y="131" width="50" height="22" rx="4" class="cell"/><text x="408.8" y="147" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">10</tspan></text><rect x="511.2" y="131" width="50" height="22" rx="4" class="cell"/><text x="536.2" y="147" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">11</tspan></text><rect x="92.9" y="189" width="58" height="22" rx="4" class="cell"/><text x="121.9" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">000</tspan></text><rect x="156.6" y="189" width="58" height="22" rx="4" class="cell"/><text x="185.6" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">001</tspan></text><rect x="220.4" y="189" width="58" height="22" rx="4" class="cell"/><text x="249.4" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">010</tspan></text><rect x="284.1" y="189" width="58" height="22" rx="4" class="head-cell"/><text x="313.1" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">011</tspan></text><rect x="347.9" y="189" width="58" height="22" rx="4" class="cell"/><text x="376.9" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">100</tspan></text><rect x="411.6" y="189" width="58" height="22" rx="4" class="cell"/><text x="440.6" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">101</tspan></text><rect x="475.4" y="189" width="58" height="22" rx="4" class="cell"/><text x="504.4" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">110</tspan></text><rect x="539.1" y="189" width="58" height="22" rx="4" class="cell"/><text x="568.1" y="205" text-anchor="middle" class="math" font-size="12">R<tspan class="mrm" font-size="9" dy="3">111</tspan></text><text x="20" y="31" class="label">level 0</text><text x="20" y="89" class="label">split by R₀</text><text x="20" y="147" class="label">by R₁</text><text x="20" y="205" class="label">by R₂</text><text x="300" y="240" text-anchor="middle" class="label">the path P = 011⋯ (highlighted); the condition (σ, 3) has reservoir R₀₁₁ = R₀ ∩ R₁ᶜ ∩ R₂ᶜ</text></svg>
:::

## Forcing along a path

:::definition{#def-path-forcing}
Let $P$ be a path of $T$. A **$P$-condition** is a pair $(\sigma, n)$ with $\sigma$ a string and $n \in \nat$. Its members are the sets $G$ with $\sigma \prec G$ and $G \setminus \sigma \subseteq R_{P \uh n}$, where $G \setminus \sigma$ denotes the set of elements of $G$ larger than or equal to $|\sigma|$. A $P$-condition $(\tau, m)$ **extends** $(\sigma, n)$ if $m \geq n$, $\sigma \preceq \tau$, and every $x$ with $|\sigma| \leq x < |\tau|$ and $\tau(x) = 1$ belongs to $R_{P \uh n}$.
:::

A $P$-condition $(\sigma, n)$ is the computable Mathias condition $(\sigma, R_{P \uh n} \setminus \{0, \dots, |\sigma| - 1\})$, with an infinite reservoir by :ref{#lem-decision-tree}. The members of an extension are members of the condition, since $R_{P \uh m} \subseteq R_{P \uh n}$. The class of members is closed and contains the finite set $\sigma$; the string $\sigma 0^k$ gives an extension $(\sigma 0^k, n)$ whose members have the prefix $\sigma 0^k$, so this is a notion of forcing in the sense of :ref{#def-forcing-notion}. A $P$-condition is a finite object, but deciding whether $(\tau, m)$ extends $(\sigma, n)$ requires the string $P \uh n$; the extension relation is computable in $P$.

:::lemma{#lem-path-questions}
For a $P$-condition $(\sigma, n)$ and a $\Sigma^0_1$ sentence $\varphi$, let $(\sigma, n) \mathrel{?{\vdash}} \varphi$ if some string $\tau$ with $(\tau, n) \leq (\sigma, n)$ satisfies $\varphi$. Then:

1. this is a forcing question for $\Sigma^0_1$ sentences; for each condition, the relation $\{ \vec m : (\sigma, n) \mathrel{?{\vdash}} \varphi(\vec m) \}$ is $\Sigma^0_1$; and a negative answer is witnessed by $(\sigma, n)$ itself, which forces $\neg\varphi$;
2. the lifted question (:ref{#def-lifted-question}) is a forcing question for $\Sigma^0_2$ sentences, and it is $\Sigma^0_1(\{ P \oplus \emptyset' \})$-preserving.
:::

:::proof{of=lem-path-questions}
1. If $\tau$ is as in the definition, $(\tau, n)$ is an extension all of whose members extend $\tau$, so they satisfy $\varphi$. If no such $\tau$ exists, a member $G$ of $(\sigma, n)$ with $\varphi(G)$, with use $u$, would give the string $\tau = G \uh \max(u, |\sigma|)$, with $(\tau, n) \leq (\sigma, n)$ and $\varphi$ satisfied by $\tau$. So $(\sigma, n)$ forces $\neg\varphi$. For a fixed condition, the search for $\tau$ involves the computable set $R_{P \uh n}$, given by the finite string $P \uh n$; so the relation is $\Sigma^0_1$. It is not uniform in the condition, since $P \uh n$ must be known.
2. Lemma :ref{#lem-lifted-question} gives the two properties. For the definability: $(\sigma, n) \mathrel{?{\vdash}} \exists y\ \psi(y)$ if and only if there are $\tau$, $m$ and $k$ such that $(\tau, m) \leq (\sigma, n)$ and $(\tau, m) \mathrel{?{\nvdash}} \neg\psi(k)$. The first clause is computable in $P$. By item 1, the second says that no string $\tau'$ with $(\tau', m) \leq (\tau, m)$ satisfies $\neg\psi(k)$; it is a $\Pi^0_1$ property of $\tau$, $k$ and the string $P \uh m$, uniformly, hence decided by $\emptyset'$ once $P \uh m$ is given. So the lifted question is $\Sigma^0_1(P \oplus \emptyset')$, for every condition.
:::

The point of item 2 is that the extensions $(\tau, m)$ are finite objects, enumerated with the oracle $P$; the complexity of the partial order is absorbed into the oracle $P \oplus \emptyset'$, instead of adding a quantifier.

:::quiz[forcing along a path]
In item 2 of :ref{#lem-path-questions}, why is the relation $(\tau, m) \mathrel{?{\nvdash}} \neg\psi(k)$ decided by $\emptyset'$ given $P \uh m$, although $m$ ranges over all numbers?

- [x] Because for each fixed string $\rho = P \uh m$, the property "no $\tau'$ compatible with $(\tau, R_\rho)$ satisfies $\neg\psi(k)$" is $\Pi^0_1$ uniformly in $\tau$, $k$ and $\rho$, and $P$ supplies $\rho$.
- [ ] Because $R_{P \uh m}$ is computable in $\emptyset'$ uniformly in $m$.

  It is computable in $P$ uniformly in $m$; $\emptyset'$ need not compute $P$.
- [ ] Because the question at level $1$ is merging.

  Merging plays no role in definability.

---

Why does the reservoir $R_{P \uh n}$ of a $P$-condition never become sparse?

- [x] Because extensions only replace $R_{P \uh n}$ by $R_{P \uh m}$ with $m \geq n$, a Boolean combination of the sets $R_i$; the construction has no means to thin the reservoir beyond what $\vec R$ prescribes.
- [ ] Because $R_{P \uh n}$ is infinite.

  The sparse reservoir of :ref{#prop-mathias-dominant} is infinite too.
- [ ] Because $P$ is a path of $T$.

  This makes the reservoirs infinite, not dense.
:::

## Cone avoidance and jump cone avoidance at once

:::theorem{#thm-coh-two-cones}
Let $\vec R$ be a computable sequence of sets, $C$ a non-computable set, and $D$ a set with $D \not\leq_T \emptyset'$. There is an $\vec R$-cohesive set $G$ with $C \not\leq_T G$ and $D \not\leq_T G'$.
:::

:::proof{of=thm-coh-two-cones}
By the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}) relativized to $\emptyset'$, applied to the non-empty $\Pi^0_1(\emptyset')$ class of paths of $T$ (:ref{#lem-decision-tree}), there is a path $P$ with $D \not\leq_T P \oplus \emptyset'$. Consider $P$-conditions, and let $G$ be sufficiently generic.

- By item 1 of :ref{#lem-path-questions}, the question for $\Sigma^0_1$ sentences is $\Sigma^0_1(\{ \emptyset \})$-preserving in the sense of :ref{#def-question-local}, so $C \not\leq_T G$ by :ref{#thm-local-cone-avoidance}.
- By item 2, the lifted question is $\Sigma^0_1(\{ P \oplus \emptyset' \})$-preserving, and $D$ is not computable in $P \oplus \emptyset'$, so $D \not\leq_T G'$ by :ref{#thm-local-jump-cone}.
- Given $(\sigma, n)$ and $k$, an element $x \geq \max(k, |\sigma|)$ of the infinite set $R_{P \uh n}$ gives the extension $(\tau, n)$, with $\tau$ of length $x + 1$ extending $\sigma$ by zeros and a $1$ at $x$, all of whose members have an element larger than or equal to $k$. So $G$ is infinite.
- Every condition $(\sigma, n)$ has the extension $(\sigma, n + 1)$, whose members $G$ satisfy $G \setminus \sigma \subseteq R_{P \uh (n + 1)}$, hence $G \subseteq^* R_n$ or $G \subseteq^* \overline{R_n}$. So $G$ is $\vec R$-cohesive.

The four families of dense sets are countable, so a single sufficiently generic $G$ has all the properties.
:::

The choice of $P$ is not a technicality. A sufficiently generic $G$ satisfies $G \subseteq^* R_{P \uh n}$ for every $n$, and for each $n$ the string $P \uh n$ is the only string $\rho$ of length $n$ with $G \subseteq^* R_\rho$, since the sets $R_\rho$ for distinct $\rho$ of the same length are disjoint. The relation "$G \subseteq^* R_\rho$" is $\Sigma^0_2(G)$, that is, $G'$-c.e., so $G'$ computes $P$: it enumerates the pairs $(\rho, n)$ with $G \subseteq^* R_\rho$ and $|\rho| = n$, and finds exactly one for each $n$. A path $P$ with $D \leq_T P \oplus \emptyset'$ would give $D \leq_T G'$. For the sequence of Jockusch and Stephan (:ref{#prop-coh-no-low}), every path of $T$ is PA relative to $\emptyset'$, and the cone avoidance basis theorem relative to $\emptyset'$ is exactly what is needed to keep the jump of $G$ away from $D$.

Compared with the weakly low basis of :ref{#thm-coh-weakly-low}, the theorem adds cone avoidance to jump cone avoidance. A cohesive set $G$ with $G' \leq_T Q$, for $Q$ PA relative to $\emptyset'$ with $D \not\leq_T Q$, satisfies $D \not\leq_T G'$, but its construction gives no control over a non-computable $C \leq_T \emptyset'$, which $Q$ computes.

:::quiz[the cohesive set]
Where is the hypothesis $D \not\leq_T \emptyset'$ used in the proof of :ref{#thm-coh-two-cones}?

- [x] To choose the path $P$ by the cone avoidance basis theorem relativized to $\emptyset'$, so that $D$ is not computable in $P \oplus \emptyset'$, the oracle relative to which the lifted question is $\Sigma^0_1$.
- [ ] To make $G$ infinite.

  Infinity comes from the infinity of the reservoirs $R_{P \uh n}$.
- [ ] To make the question for $\Sigma^0_1$ sentences preserving.

  That question is $\Sigma^0_1$ for each condition, whatever $D$ is.

---

Why does $G'$ compute the path $P$?

- [x] Because $P \uh n$ is the unique string $\rho$ of length $n$ with $G \subseteq^* R_\rho$, a $\Sigma^0_2(G)$ property; $G'$ enumerates the strings with this property and finds exactly one of each length.
- [ ] Because $G$ computes $P$.

  $G$ does not compute $P$ in general: $P$ may be PA relative to $\emptyset'$, and $G$ avoids the cone above any given non-computable set.
- [ ] Because $P$ is computable in $\emptyset'$.

  $P$ is a path of a $\emptyset'$-computable tree, not necessarily $\emptyset'$-computable.
:::

## Exercises

::::exercise{difficulty=2}
Let $f$ be a function hyperimmune relative to $P \oplus \emptyset'$. Show that $f$ is hyperimmune relative to $G'$ for every sufficiently generic $G$ for $P$-conditions.

:::solution
As in the second exercise of :ref{to="jump-cone-avoidance/sigma2-questions"}: write "$\Phi^{G'}_e(m)\converge$" as $\exists \langle k, y \rangle\ \psi_{m,k}(y)$, where $\exists y\ \psi_{m,k}(y)$ expresses "$\Phi^{G'}_e(m)\converge < k$". A positive answer of the lifted question for the first sentence, witnessed by an extension $(\tau, m')$ and $\langle k, y \rangle$, is a positive answer for "$\Phi^{G'}_e(m)\converge < k$" with the same witnesses. Given a condition $c$, the function $g(m)$, the first $k$ found with $c \mathrel{?{\vdash}} \Phi^{G'}_e(m)\converge < k$, is partial computable in $P \oplus \emptyset'$ by item 2 of :ref{#lem-path-questions}. If $g(m)$ is undefined, some extension forces $\Phi^{G'}_e(m)\diverge$; if $g$ is total, $f(m) > g(m)$ for some $m$, and some extension forces $\Phi^{G'}_e(m)\converge < f(m)$. These sets of conditions are dense, and :ref{#thm-forcing-truth} concludes.
:::
::::

::::exercise{difficulty=2}
Let $\vec R$ be the sequence of :ref{#prop-coh-no-low}, with $R_e = \{ s : \Phi^{\emptyset'_s}_e(e)[s]\converge = 0 \}$. Show that for every path $P$ of the tree $T$ of :ref{#lem-decision-tree}, the function $1 - P$ is $\{0,1\}$-valued and DNC relative to $\emptyset'$. Deduce, without using :ref{#prop-coh-no-low}, that the jump of every sufficiently generic set for $P$-conditions is PA relative to $\emptyset'$.

:::solution
By the proof of :ref{#prop-coh-no-low}, $R_e$ is cofinite if $\Phi^{\emptyset'}_e(e)\converge = 0$, and finite if $\Phi^{\emptyset'}_e(e)$ converges to another value. For a path $P$, the set $R_{P \uh (e+1)}$ is infinite by :ref{#lem-decision-tree}. If $\Phi^{\emptyset'}_e(e)\converge = 0$, then $\overline{R_e}$ is finite, so $P(e) = 0$ and $1 - P(e) = 1$. If $\Phi^{\emptyset'}_e(e)\converge = 1$, then $R_e$ is finite, so $P(e) = 1$ and $1 - P(e) = 0$. In both cases $1 - P(e) \neq \Phi^{\emptyset'}_e(e)$, so $1 - P$ is DNC relative to $\emptyset'$, and $P$ is PA relative to $\emptyset'$. A sufficiently generic $G$ satisfies $P \leq_T G'$, as shown after :ref{#thm-coh-two-cones}, and a set computing a set PA relative to $\emptyset'$ is PA relative to $\emptyset'$.
:::
::::

## Notes and references

The two diagnoses of the failure of Mathias forcing, the principle of restricting the partial order to the conditions used by the construction, the forcing along a path of the tree of decisions and :ref{#thm-coh-two-cones} follow the section *Cohesiveness principle* of the chapter *Jump cone avoidance* of Patey's monograph, where the definability of the lifted question is left as an exercise. The monograph also states, as an exercise attributed to Patey (2017), a notion of forcing that chooses the path and builds the cohesive set at the same time, combining $P$-conditions with Jockusch–Soare forcing relative to $\emptyset'$; Patey used such notions to control iterated jumps of cohesive sets. The class of decisions and its relation with the jumps of cohesive sets are due to Jockusch and Stephan (1993); see also Hirschfeldt, Section 6.5.

- L. Patey, *Controlling iterated jumps of solutions to combinatorial problems*, Computability 6 (2017), 47–78.
- C. G. Jockusch, Jr. and F. Stephan, *A cohesive set which is not high*, Mathematical Logic Quarterly 39 (1993), 515–530.
- D. R. Hirschfeldt, *Slicing the Truth*, World Scientific, 2014, Section 6.5.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump cone avoidance*, section *Cohesiveness principle*.
