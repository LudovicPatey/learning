---
title: Product Mathias forcing
summary: Mathias conditions with a tuple of reservoirs in a low Scott ideal and a large Δ⁰₂ class of tuples, extended through slices; promises for Π⁰₂ sentences; a Σ⁰₂ question whose positive answers are forced and whose negative answers are promised.
duration: 40
prerequisites: [product-largeness, lowness/coded-ideals, jump-cone-avoidance/pigeons-non-high, jump-cone-avoidance/pigeon-questions]
---

This lesson and the next build a forcing of Mathias type with a merging, $\Sigma^0_2$-preserving question for $\Sigma^0_2$ sentences. A condition has a stem, a tuple of reservoirs and a large class of possible future tuples. This lesson defines the conditions, the promises that replace the forcing of $\Pi^0_2$ sentences, and the question; the next one merges two negative answers by duplicating the reservoirs. The theorem obtained is weak, since low sets satisfy it; the notion of forcing is what the rest of the course adapts to the pigeonhole principle.

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

:::example{#ex-product-extension}
Let $p = (\sigma, \langle \nat \rangle, S_\infty)$, and let $E$ and $O$ be the sets of even and odd numbers larger than or equal to $|\sigma|$. Let $q = (\sigma, \langle E, O \rangle, T)$ with index set $\{0, 1\} = \{\varepsilon\} \cdot \{0, 1\}$ and $\mathcal U^{\{0, 1\}}_T = \mathcal L_E \times \mathcal L_O$, which is large by :ref{#ex-product-large}. Both slices of a member of this class are infinite sets, so $q$ extends $p$. The two conditions have the same members, since $E \cup O$ contains every number above $|\sigma|$. What $q$ adds is information on the future: every later tuple of reservoirs will keep infinitely many even numbers in its first coordinate and infinitely many odd numbers in its second. A forcing with one reservoir can only record one of the two, by passing to $E$ or to $O$, and then loses the other.
:::

:::lemma{#lem-product-basic}
Let $p = (\sigma, \vec X, S)$ be a condition.

1. For $x \in \bigcup \vec X$, the triple $(\sigma \cup \{ x \}, \langle X_\nu \setminus \{0, \dots, x\} \rangle, S)$ is a condition extending $p$, where $\sigma \cup \{ x \}$ is the string of length $x + 1$.
2. For a $\Sigma^0_1$ sentence $\theta$: if a string $\tau$ compatible with $(\sigma, \bigcup \vec X)$ satisfies $\theta$, the condition $(\tau, \langle X_\nu \setminus \{0, \dots, |\tau|\} \rangle, S)$ extends $p$ and all its members satisfy $\theta$; otherwise all members of $p$ satisfy $\neg\theta$.
:::

:::proof{of=lem-product-basic}
1. The new reservoirs are in $\mathcal M$ and differ from $X_\nu$ by finitely many elements, so $\mathcal L$ of the new tuple is $\mathcal L_{\vec X}$; the class and its index set do not change. The stem is compatible with $(\sigma, \bigcup \vec X)$, since $x \geq \min X_\nu \geq |\sigma|$.
2. The triple is a condition extending $p$ as in item 1, and every member extends $\tau$, so it satisfies $\theta$ by the use principle. Otherwise, a member satisfying $\theta$ would have a prefix of length at least $|\sigma|$, compatible with $(\sigma, \bigcup \vec X)$, satisfying $\theta$.
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

So a promise survives the shrinking of the class and the growth of the index set, and each of its instances can be forced later.

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
:::

## Exercises

::::exercise{difficulty=1}
Show that the extension relation of :ref{#def-product-condition} is transitive.

:::solution
Let $p = (\sigma, \vec X, S)$ with index set $I$, $q = (\tau, \vec Y, T)$ extending $p$ with index set $I \cdot K$, and $r = (\rho, \vec W, R)$ extending $q$ with index set $(I \cdot K) \cdot K' = I \cdot (K \cdot K')$; the set $K \cdot K'$ is an index set, since its strings have the same length. For $\nu \in I$, $\kappa \in K$ and $\kappa' \in K'$, $W_{\nu\kappa\kappa'} \subseteq Y_{\nu\kappa} \subseteq X_\nu$. The stem $\rho$ is compatible with $(\tau, \bigcup \vec Y)$, $\tau$ is compatible with $(\sigma, \bigcup \vec X)$ and $\bigcup \vec Y \subseteq \bigcup \vec X$, so $\rho$ is compatible with $(\sigma, \bigcup \vec X)$. For $\vec Z \in \mathcal U^{I \cdot K \cdot K'}_R$, the slice $\vec Z^{(\kappa')}$ is in $\mathcal U^{I \cdot K}_T$, and its slice $\kappa$ is $\langle Z_{\nu\kappa\kappa'} : \nu \in I \rangle = \vec Z^{(\kappa\kappa')}$, which is therefore in $\mathcal U^I_S$.
:::
::::

## Notes and references

Product Mathias forcing and its question for $\Sigma^0_2$ sentences follow the section *Product Mathias forcing* of the chapter *Jump compactness avoidance* of Patey's monograph, after Monin and Patey (2021). Extensions are defined here with slices, which replace the monograph's projections; in the negative case of the question, the extension has the index set $S \cup E$ (the monograph writes the old one). The transitivity of extension is an exercise of the monograph, stated there for its order on classes of tuples.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Product Mathias forcing*.
