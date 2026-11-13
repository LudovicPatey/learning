---
title: Product Mathias forcing
summary: Mathias conditions with a tuple of reservoirs in a low Scott ideal and a large Δ⁰₂ class of tuples; promises for Π⁰₂ sentences; a Σ⁰₂ question whose negative answers are merged by duplicating the reservoirs; the jump of the generic set is not PA relative to ∅′.
duration: 45
prerequisites: [product-largeness, lowness/coded-ideals, jump-cone-avoidance/pigeons-non-high]
---

This lesson builds a notion of forcing of Mathias type with a merging, $\Sigma^0_2$-preserving question for $\Sigma^0_2$ sentences. A condition has a stem, a tuple of reservoirs, and a large class of tuples, the possible future reservoirs; two negative answers are merged by duplicating the reservoirs. The resulting theorem is weak, since low sets have its conclusion; its interest is the notion of forcing, which the next lessons adapt to the pigeonhole principle.

Throughout, $\mathcal M$ is a Scott ideal with a **low** code $M = \bigoplus_i Z_i$ (:ref{#cor-scott-codes}), and the classes $\mathcal U^I_S$ are as in :ref{to="jump-compactness-avoidance/product-largeness"}. Strings are identified with finite sets, and a string $\tau$ is **compatible** with $(\sigma, X)$ if $\sigma \preceq \tau$ and every $x$ with $|\sigma| \leq x < |\tau|$ and $\tau(x) = 1$ is in $X$, as in :ref{to="jump-cone-avoidance/pigeonhole-forcing"}.

## Conditions

For index sets $I$ and $K$, let $I \cdot K = \{ \nu\kappa : \nu \in I, \kappa \in K \}$, the concatenations. For an $(I \cdot K)$-tuple $\vec Z$ and $\kappa \in K$, the **slice** $\vec Z^{(\kappa)}$ is the $I$-tuple $\langle Z_{\nu\kappa} : \nu \in I \rangle$. With $K = \{ \varepsilon \}$, $I \cdot K = I$.

:::definition{#def-product-condition}
A **condition** is a triple $p = (\sigma, \vec X, S)$ where, for an index set $I$:

1. $\sigma$ is a string and $\vec X$ an $I$-tuple of members of $\mathcal M$ with $\min X_\nu \geq |\sigma|$;
2. $S \subseteq \nat^2$ is $\Delta^0_2$, and $\mathcal U^I_S$ is a large subclass of $\mathcal L_{\vec X}$.

A **member** of $p$ is a set $G$ with $\sigma \prec G$ whose elements larger than or equal to $|\sigma|$ are in $\bigcup \vec X$. A condition $(\tau, \vec Y, T)$ with index set $J$ **extends** $p$ if $J = I \cdot K$ for some index set $K$, $Y_{\nu\kappa} \subseteq X_\nu$ for all $\nu$ and $\kappa$, $\tau$ is compatible with $(\sigma, \bigcup \vec X)$, and $\vec Z^{(\kappa)} \in \mathcal U^I_S$ for every $\vec Z \in \mathcal U^J_T$ and every $\kappa \in K$.
:::

A member of an extension is a member of $p$. The relation is transitive: slices of slices are slices, and compatibility composes. The class $\mathcal U^I_S$ is a class of possible future tuples of reservoirs; since it is contained in $\mathcal L_{\vec X}$, it is non-trivial, and all $X_\nu$ are infinite. By the last statement of :ref{#lem-product-intersection}, applied to $\mathcal U^I_S = \mathcal U^I_S \cap \mathcal L_{\vec X}$, the tuple $\vec X$ itself belongs to $\mathcal U^I_S$. The triple $(\varepsilon, \langle \nat \rangle, S_\infty)$, with $I = \{ \varepsilon \}$ and $\mathcal U^I_{S_\infty}$ the class of infinite sets, is a condition.

:::lemma{#lem-product-basic}
Let $p = (\sigma, \vec X, S)$ be a condition.

1. For $x \in \bigcup \vec X$, the triple $(\sigma \cup \{ x \}, \langle X_\nu \setminus \{0, \dots, x\} \rangle, S)$ is a condition extending $p$, where $\sigma \cup \{ x \}$ is the string of length $x + 1$.
2. For a $\Sigma^0_1$ sentence $\theta$: if some string compatible with $(\sigma, \bigcup \vec X)$ satisfies $\theta$, an extension of the form of item 1, with a longer stem, forces $\theta$; otherwise $p$ forces $\neg\theta$.
:::

:::proof{of=lem-product-basic}
1. The new reservoirs are in $\mathcal M$ and differ from $X_\nu$ by finitely many elements, so $\mathcal L$ of the new tuple is $\mathcal L_{\vec X}$; the class and its index set do not change. The stem is compatible with $(\sigma, \bigcup \vec X)$, since $x \geq \min X_\nu \geq |\sigma|$.
2. If $\tau$ satisfies $\theta$, take $\tau$ as stem and truncate the reservoirs above $|\tau|$; every member extends $\tau$ and satisfies $\theta$ by the use principle. Otherwise, a member satisfying $\theta$ would have a prefix of length at least $|\sigma|$, compatible with $(\sigma, \bigcup \vec X)$, satisfying $\theta$.
:::

## Promises

For an $I$-tuple, a string $\tau$ and a $\Sigma^0_1$ sentence $\theta$, let $\mathcal V^I_{\tau, \theta}$ be the class of $I$-tuples $\vec Z$ such that some string compatible with $(\tau, \bigcup \vec Z)$ satisfies $\theta$. It is an upward closed $\Sigma^0_1$ class with an index computable from $\tau$, $\theta$ and $I$, hence a $\Sigma^0_1(\mathcal M)$ class.

:::definition{#def-product-promise}
A condition $(\sigma, \vec X, S)$ **promises** a $\Pi^0_2$ sentence $\forall y\ \theta(y)$, with $\theta$ a $\Sigma^0_1$ formula, if $\mathcal U^I_S \subseteq \mathcal V^I_{\tau, \theta(m)}$ for every $m$ and every string $\tau$ compatible with $(\sigma, \bigcup \vec X)$.
:::

A promise is the syntactic forcing relation of the monograph, named as in :ref{#def-pigeon-pi2}.

:::lemma{#lem-product-promise}
Let $p = (\sigma, \vec X, S)$ promise $\forall y\ \theta(y)$.

1. Every extension of $p$ promises $\forall y\ \theta(y)$.
2. For every $m$, some extension of $p$ of the form of item 1 of :ref{#lem-product-basic} forces $\theta(m)$.
:::

:::proof{of=lem-product-promise}
1. Let $q = (\tau, \vec Y, T)$ extend $p$, with $J = I \cdot K$. Let $\rho$ be compatible with $(\tau, \bigcup \vec Y)$ and $\vec Z \in \mathcal U^J_T$. Since $\tau$ is compatible with $(\sigma, \bigcup \vec X)$ and $\bigcup \vec Y \subseteq \bigcup \vec X$, $\rho$ is compatible with $(\sigma, \bigcup \vec X)$. Take $\kappa \in K$: $\vec Z^{(\kappa)} \in \mathcal U^I_S \subseteq \mathcal V^I_{\rho, \theta(m)}$, so some string compatible with $(\rho, \bigcup \vec Z^{(\kappa)})$ satisfies $\theta(m)$, and $\bigcup \vec Z^{(\kappa)} \subseteq \bigcup \vec Z$. So $\vec Z \in \mathcal V^J_{\rho, \theta(m)}$.
2. Since $\vec X \in \mathcal U^I_S \subseteq \mathcal V^I_{\sigma, \theta(m)}$, some string compatible with $(\sigma, \bigcup \vec X)$ satisfies $\theta(m)$; apply item 2 of :ref{#lem-product-basic}.
:::

So a promise is kept by all later conditions of a construction, even when the class shrinks and the index set grows, and each of its instances can be forced later.

## The question for Σ⁰₂ sentences

:::definition{#def-product-question}
Let $p = (\sigma, \vec X, S)$ be a condition and $\varphi = \exists y\ \psi(y)$ a $\Sigma^0_2$ sentence, with $\psi$ a $\Pi^0_1$ formula. Let $\mathcal A_{p, \varphi}$ be the class
$$
\mathcal U^I_S \cap \bigcap \{ \mathcal V^I_{\tau, \neg\psi(m)} : m \in \nat,\ \tau \text{ compatible with } (\sigma, \textstyle\bigcup \vec X) \}.
$$
Let $p \mathrel{?{\vdash}} \varphi$ if $\mathcal A_{p, \varphi}$ is not large.
:::

:::lemma{#lem-product-question}
Let $p = (\sigma, \vec X, S)$ be a condition and $\varphi = \exists y\ \psi(y)$.

1. The relation $\{ \vec n : p \mathrel{?{\vdash}} \varphi(\vec n) \}$ is $\Sigma^0_2$.
2. If $p \mathrel{?{\vdash}} \varphi$, some extension of $p$ with the same index set forces $\varphi$: all its members satisfy $\psi(m)$ for some $m$.
3. If $p \mathrel{?{\nvdash}} \varphi$, then $(\sigma, \vec X, S \cup E)$ is a condition extending $p$ that promises $\neg\varphi$, where $E$ is the set of indices of the classes $\mathcal V^I_{\tau, \neg\psi(m)}$ in the definition.
:::

:::proof{of=lem-product-question}
1. The set $E$ is computable in $\bigcup \vec X$, uniformly in the parameters $\vec n$, and $\bigcup \vec X \leq_T M$. So $S \cup E$ is $\Delta^0_2$, and by item 2 of :ref{#prop-product-complexity}, "$\mathcal A_{p, \varphi}$ is large" is $\Pi^0_1((S \cup E) \oplus M')$, hence $\Pi^0_1(\emptyset')$ since $M$ is low and $S$ is $\Delta^0_2$. The question is its negation, $\Sigma^0_1(\emptyset')$, that is, $\Sigma^0_2$.
2. By item 2 of :ref{#prop-product-complexity}, some finite part of the intersection is not large: there are a finite $F \subseteq S$ and finitely many pairs $(m_s, \tau_s)$, $s < l$, such that $\mathcal B = \mathcal U^I_F \cap \bigcap_{s < l} \mathcal V^I_{\tau_s, \neg\psi(m_s)}$ is not large. It is a $\Sigma^0_1(\mathcal M)$ class, so by item 3 there is a $k$-partition $Y_0, \dots, Y_{k-1}$ of $\nat$ in $\mathcal M$ with $\vec Y_j \notin \mathcal B$ for every $j$. By :ref{#lem-product-cover}, some $j$ makes $\mathcal U^I_S \cap \mathcal L_{\vec Y_j}$ large; then $\vec Y_j \in \mathcal U^I_S \subseteq \mathcal U^I_F$ by :ref{#lem-product-intersection}, so $\vec Y_j \notin \mathcal V^I_{\tau_s, \neg\psi(m_s)}$ for some $s$. Let $W_\nu = X_\nu \cap Y_{j(\nu)}$. By :ref{#lem-product-intersection}, since $\mathcal U^I_S \subseteq \mathcal L_{\vec X}$, the class $\mathcal U^I_S \cap \mathcal L_{\vec W}$ is large; it is $\mathcal U^I_T$ for $T = S \cup E'$ with $E'$ computable, a $\Delta^0_2$ set. Let $q = (\tau_s, \langle W_\nu \setminus \{0, \dots, |\tau_s|\} \rangle, T)$. It is a condition: the reservoirs are in $\mathcal M$, and finite changes do not affect $\mathcal L$. It extends $p$ with $K = \{ \varepsilon \}$, since $\mathcal U^I_T \subseteq \mathcal U^I_S$. A member $G$ of $q$ extends $\tau_s$ and its later elements are in $\bigcup \vec Y_j$. If $G$ satisfied $\neg\psi(m_s)$, a prefix of $G$ of length at least $|\tau_s|$ would be compatible with $(\tau_s, \bigcup \vec Y_j)$ and satisfy $\neg\psi(m_s)$, so $\vec Y_j \in \mathcal V^I_{\tau_s, \neg\psi(m_s)}$. So $G$ satisfies $\psi(m_s)$.
3. $\mathcal U^I_{S \cup E} = \mathcal A_{p, \varphi}$ is large and contained in $\mathcal U^I_S$, and $S \cup E$ is $\Delta^0_2$; so the triple is a condition extending $p$. It promises $\forall y\ \neg\psi(y)$ by definition of $\mathcal A_{p, \varphi}$.
:::

A positive answer thus gives an extension all of whose members satisfy $\varphi$, and a negative answer a promise of $\neg\varphi$, which becomes truth along a construction that handles its instances.

:::quiz[the Σ⁰₂ question]
In item 2 of :ref{#lem-product-question}, why is the partition $Y_0, \dots, Y_{k-1}$ taken in $\mathcal M$?

- [x] Because the new reservoirs $X_\nu \cap Y_{j(\nu)}$ must belong to $\mathcal M$; item 3 of :ref{#prop-product-complexity} provides a witness of non-largeness in $\mathcal M$.
- [ ] Because $\mathcal U^I_S$ only contains members of $\mathcal M$.

  It contains many tuples outside $\mathcal M$.
- [ ] Because otherwise $\vec Y_j$ would not be in $\mathcal U^I_S$.

  Membership comes from the cover lemma and the intersection lemma.


## Merging by duplication

:::lemma{#lem-product-merging}
Let $p = (\sigma, \vec X, S)$ be a condition with index set $I$, and let $\varphi_0, \varphi_1$ be $\Sigma^0_2$ sentences with $p \mathrel{?{\nvdash}} \varphi_0$ and $p \mathrel{?{\nvdash}} \varphi_1$. There is an extension of $p$ with index set $I \cdot \{0, 1\}$ that promises $\neg\varphi_0$ and $\neg\varphi_1$.
:::

:::proof{of=lem-product-merging}
Let $\mathcal A_b = \mathcal A_{p, \varphi_b}$ for $b < 2$; both are large. Let $Y_{\nu b} = X_\nu$, and let $\mathcal C$ be the class of $(I \cdot \{0, 1\})$-tuples $\vec Z$ with $\vec Z^{(0)} \in \mathcal A_0$ and $\vec Z^{(1)} \in \mathcal A_1$. It is $\mathcal U^{I \cdot \{0, 1\}}_T$ for a $\Delta^0_2$ set $T$ computed from the index sets of $\mathcal A_0$ and $\mathcal A_1$, translating each index to the corresponding slice. It is large, since for a cover one chooses $j$ on each slice separately, and it is contained in $\mathcal L_{\vec Y}$, since $\mathcal A_b \subseteq \mathcal L_{\vec X}$. So $q = (\sigma, \vec Y, T)$ is a condition. It extends $p$: its slices are in $\mathcal A_b \subseteq \mathcal U^I_S$. Let $\tau$ be compatible with $(\sigma, \bigcup \vec Y) = (\sigma, \bigcup \vec X)$, $m \in \nat$ and $\vec Z \in \mathcal C$. Then $\vec Z^{(0)} \in \mathcal A_0 \subseteq \mathcal V^I_{\tau, \neg\psi_0(m)}$, so $\vec Z \in \mathcal V^{I \cdot \{0, 1\}}_{\tau, \neg\psi_0(m)}$ as in the proof of :ref{#lem-product-promise}. So $q$ promises $\neg\varphi_0$, and similarly $\neg\varphi_1$.
:::

:::figure[Merging by duplication (:ref{#lem-product-merging}). The two negative answers give two large classes $\mathcal A_0$ and $\mathcal A_1$ of $I$-tuples, whose intersection need not be large. The extension duplicates the reservoirs: slice $0$ of the new tuple ranges over $\mathcal A_0$ and slice $1$ over $\mathcal A_1$, and the stem may use both.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Merging by duplication: a condition with index set I and two negative answers giving classes A_0 and A_1 is extended by a condition with index set I times 0,1 whose slice 0 ranges over A_0 and slice 1 over A_1, with the same stem and copied reservoirs"><defs><marker id="jca-pm-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="200" y="10" width="200" height="52" rx="6" class="state"/><text x="300.0" y="32.0" text-anchor="middle" class="label">p = (σ, X⃗, S), index set I</text><text x="300.0" y="48.0" text-anchor="middle" class="label">p ?⊬ φ₀ and p ?⊬ φ₁</text><rect x="20" y="100" width="200" height="44" rx="6" class="node"/><text x="120.0" y="126.0" text-anchor="middle" class="label">𝒜₀ = 𝒜(p, φ₀) large</text><rect x="380" y="100" width="200" height="44" rx="6" class="node"/><text x="480.0" y="126.0" text-anchor="middle" class="label">𝒜₁ = 𝒜(p, φ₁) large</text><rect x="130" y="186" width="340" height="52" rx="6" class="state"/><text x="300.0" y="208.0" text-anchor="middle" class="label">q = (σ, X⃗ duplicated, T), index set I·{0, 1}</text><text x="300.0" y="224.0" text-anchor="middle" class="label">slice 0 ∈ 𝒜₀, slice 1 ∈ 𝒜₁</text><line x1="250" y1="64" x2="140" y2="96" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><line x1="350" y1="64" x2="460" y2="96" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><line x1="140" y1="146" x2="230" y2="182" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><line x1="460" y1="146" x2="370" y2="182" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><text x="300" y="132" text-anchor="middle" class="label">𝒜₀ ∩ 𝒜₁ need not be large</text></svg>
:::

The duplication is what a single class could not do (:ref{#lem-no-two-sides}): for the sentences "$G \cap R$ is finite" and "$G \setminus R$ is finite", slice $0$ can provide the elements of $R$ and slice $1$ those of $\overline R$ (first exercise).

## The theorem

:::theorem{#thm-product-mathias}
There is a sequence of conditions $p_0 \geq p_1 \geq \cdots$ whose stems define an infinite set $G$, a member of every $p_s$, such that $G'$ is not PA relative to $\emptyset'$.
:::

:::proof{of=thm-product-mathias}
Start with $p_0 = (\varepsilon, \langle \nat \rangle, S_\infty)$, and handle in turn, each infinitely often, the following tasks: extend the stem, by item 1 of :ref{#lem-product-basic}; for a $\Pi^0_2$ sentence $\forall y\ \theta(y)$ and a number $m$, if the current condition promises it, pass to an extension forcing $\theta(m)$, by :ref{#lem-product-promise}; and for an index $e$, the requirement below. The stems are compatible, so they define a set $G$, infinite by the first task, and a member of every $p_s$. If $p_s$ promises $\forall y\ \theta(y)$, so do all later conditions, and the second task makes $G$ satisfy each $\theta(m)$.

*The requirement.* Let $p$ be the current condition, and $U$ the set of pairs $(x, v) \in \nat \times \{0, 1\}$ with $p \mathrel{?{\vdash}} \chi_{e, x, v}$, the sentence "$\Phi^{G'}_e(x)\converge = v$" (:ref{to="jump-compactness-avoidance/jump-pa-avoidance"}). It is $\Sigma^0_2$ by item 1 of :ref{#lem-product-question}. If $(x, J^{\emptyset'}(x)) \in U$ for some $x$ with $J^{\emptyset'}(x)$ defined, item 2 gives an extension all of whose members, $G$ among them, satisfy $\Phi^{G'}_e(x) = J^{\emptyset'}(x)$. If $(x, 0), (x, 1) \notin U$ for some $x$, :ref{#lem-product-merging} gives an extension promising $\neg\chi_{e, x, 0}$ and $\neg\chi_{e, x, 1}$, which $G$ then satisfies: $\Phi^{G'}_e(x)$ has no value in $\{0, 1\}$. Otherwise, as in the proof of :ref{#thm-jump-pa-merging}, $U$ yields a $\emptyset'$-computable $\{0, 1\}$-valued function DNC relative to $\emptyset'$, which does not exist. So no $\Phi^{G'}_e$ is $\mathrm{DNC}_2$ relative to $\emptyset'$.
:::

Unlike the forcing of :ref{#prop-one-reservoir-cohesive}, this notion of forcing does not allow one to replace the reservoirs by their intersections with a set or with its complement, and by the theorem it cannot build a cohesive set for the sequence of :ref{#prop-coh-no-low}.

## Exercises

::::exercise{difficulty=1}
Let $p = (\sigma, \vec X, S)$ be a condition and $R$ a computable set such that $\mathcal U^I_S \cap \mathcal L_{\langle R \rangle_\nu}$ and $\mathcal U^I_S \cap \mathcal L_{\langle \overline R \rangle_\nu}$ are both large, where $\langle R \rangle_\nu$ is the tuple with all coordinates $R$. Show that some extension of $p$ promises that $G \cap R$ and $G \setminus R$ are infinite.

:::solution
The sentence "$G \cap R$ is finite" is $\exists y\ \psi(y)$ with $\psi(y)$: no element $z \geq y$ of $G$ is in $R$. For $\tau$ compatible with $(\sigma, \bigcup \vec X)$, the class $\mathcal V^I_{\tau, \neg\psi(m)}$ is the class of tuples $\vec Z$ such that $\bigcup \vec Z \cap R$ has an element larger than or equal to $\max(m, |\tau|)$. So $\mathcal A_{p, \varphi}$ contains $\mathcal U^I_S \cap \mathcal L_{\langle R \rangle_\nu}$, which is large, and $p \mathrel{?{\nvdash}} \varphi$. Similarly for "$G \setminus R$ is finite". Apply :ref{#lem-product-merging}.
:::
::::

## Notes and references

Product Mathias forcing, its question for $\Sigma^0_2$ sentences and the merging lemma follow the section *Product Mathias forcing* of the chapter *Jump compactness avoidance* of Patey's monograph, after Monin and Patey (2021). Extensions are defined here with slices, which replace the monograph's projections; in the negative case of the question, the extension has the index set $S \cup E$ (the monograph writes the old one).

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Product Mathias forcing*.
