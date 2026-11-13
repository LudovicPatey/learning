---
title: Questions on meta-conditions
summary: Promises for Π⁰₂ sentences on the parts of a meta-condition, kept by descendants and made true on valid parts; a Σ⁰₂ question about a set of branches, which uses that the instance is Δ⁰₂; its positive answers are witnessed on one branch at the same level, its negative answers by promises on all branches; weak merging of two answers out of 2uₙ + 1 by triplication of the index set.
duration: 45
prerequisites: [meta-conditions]
---

The setting of the previous lesson is fixed: a $\Delta^0_2$ set $A$ with $A_0 = A$ and $A_1 = \overline A$, a Scott ideal $\mathcal M$ with a low code $M$, the index sets $\mathbb I_n$ and their branches, and the meta-conditions $c = (\vec \sigma, \vec X, S)$ of :ref{#def-meta-condition}. This lesson adapts to meta-conditions the promises and the question of product Mathias forcing (:ref{to="jump-compactness-avoidance/product-mathias"}). Two features are new. The stems of a part $(I, i)$ must stay inside $A_i$, so that the question quantifies over strings compatible with $(\sigma^I_i, A_i \cap \bigcup_{\nu \in I} X_\nu)$; this is where the instance must be $\Delta^0_2$. And merging is replaced by weak merging: the extension of a negative answer is witnessed on many branches at once, and two answers can only be merged on each branch of the next level.

For a branch $I$ of $\mathbb I_n$, a string $\tau$ and a $\Sigma^0_1$ sentence $\theta$, let $\mathcal V^{I}_{\tau, \theta}$ be the class of $\mathbb I_n$-tuples $\vec Z$ such that some string compatible with $(\tau, \bigcup_{\nu \in I} Z_\nu)$ satisfies $\theta$. It is an upward closed $\Sigma^0_1$ class with an index computable from $I$, $\tau$ and $\theta$, and it depends only on the coordinates in $I$.

## Promises

:::definition{#def-meta-promise}
A meta-condition $c = (\vec \sigma, \vec X, S)$ of level $n$ **promises** a $\Pi^0_2$ sentence $\forall y\ \theta(y)$, with $\theta$ a $\Sigma^0_1$ formula, on its part $(I, i)$ if $\mathcal U^{\mathbb I_n}_S \subseteq \mathcal V^I_{\tau, \theta(m)}$ for every $m$ and every string $\tau$ compatible with $(\sigma^I_i, A_i \cap \bigcup_{\nu \in I} X_\nu)$.
:::

Compared with :ref{#def-product-promise}, the stems $\tau$ range over the extensions inside $A_i$, the only ones the part $(I, i)$ can take, while the continuations witnessing $\theta(m)$ may leave $A_i$. This is why a promise becomes truth only on a valid part.

:::lemma{#lem-meta-promise}
Let $c = (\vec \sigma, \vec X, S)$ of level $n$ promise $\forall y\ \theta(y)$ on $(I, i)$.

1. If $d$ of level $m$ extends $c$, then $d$ promises $\forall y\ \theta(y)$ on every part $(J, i)$ with $J \upharpoonright n = I$.
2. If $(I, i)$ is valid, then for every $m$ there is an extension of $c$ as in item 3 of :ref{#lem-meta-valid}, differing from $c$ only by the stem of $(I, i)$ and by the reservoirs, all of whose members of the part $(I, i)$ satisfy $\theta(m)$.
:::

:::proof{of=lem-meta-promise}
1. Let $d = (\vec \tau, \vec Y, T)$ and $J = I \cdot K$; fix $\kappa \in K$. Let $\rho$ be compatible with $(\tau^J_i, A_i \cap \bigcup_{\mu \in J} Y_\mu)$. Since $\tau^J_i \subseteq A_i$ is compatible with $(\sigma^I_i, \bigcup_{\nu \in I} X_\nu)$ and $\bigcup_{\mu \in J} Y_\mu \subseteq \bigcup_{\nu \in I} X_\nu$, the string $\rho$ is compatible with $(\sigma^I_i, A_i \cap \bigcup_{\nu \in I} X_\nu)$. For $\vec Z \in \mathcal U^{\mathbb I_m}_T$, the slice $\vec Z^{(\kappa)}$ is in $\mathcal U^{\mathbb I_n}_S \subseteq \mathcal V^I_{\rho, \theta(m)}$: some string compatible with $(\rho, \bigcup_{\nu \in I} Z_{\nu\kappa})$ satisfies $\theta(m)$, and $\bigcup_{\nu \in I} Z_{\nu\kappa} \subseteq \bigcup_{\mu \in J} Z_\mu$. So $\vec Z \in \mathcal V^J_{\rho, \theta(m)}$.
2. By validity and :ref{#lem-product-intersection}, $\vec X^{I, i} \in \mathcal U^{\mathbb I_n}_S \subseteq \mathcal V^I_{\sigma^I_i, \theta(m)}$. So some string $\rho$ compatible with $(\sigma^I_i, \bigcup_{\nu \in I} (X_\nu \cap A_i))$ satisfies $\theta(m)$, and $\rho \subseteq A_i$. Replace $\sigma^I_i$ by $\rho$ and each $X_\mu$ by $X_\mu \setminus \{0, \dots, |\rho|\}$. The result is a meta-condition extending $c$ as in item 3 of :ref{#lem-meta-valid}; its members of the part $(I, i)$ extend $\rho$, and satisfy $\theta(m)$ by the use principle.
:::

Validity is used in item 2 exactly once: to place the tuple of the reservoirs restricted to $A_i$ in the class $\mathcal U^{\mathbb I_n}_S$, so that the promise applies to it. On a part that is not valid, the strings witnessing $\theta(m)$ may all leave $A_i$, and the promise is useless.

## The question

:::definition{#def-meta-question}
Let $c = (\vec \sigma, \vec X, S)$ be a meta-condition of level $n$, $H$ a non-empty set of branches of $\mathbb I_n$, $i < 2$, and $\varphi = \exists y\ \psi(y)$ a $\Sigma^0_2$ sentence with $\psi$ a $\Pi^0_1$ formula. Let $\mathcal A^{H, i}_{c, \varphi}$ be the class
$$
\mathcal U^{\mathbb I_n}_S \cap \bigcap \{ \mathcal V^I_{\tau, \neg\psi(m)} : I \in H,\ m \in \nat,\ \tau \text{ compatible with } (\sigma^I_i, A_i \cap \textstyle\bigcup_{\nu \in I} X_\nu) \},
$$
and let $c \mathrel{?{\vdash}}_{H, i} \varphi$ if $\mathcal A^{H, i}_{c, \varphi}$ is not large.
:::

The question asks about the parts $(I, i)$ for all $I \in H$ at once. A negative answer promises $\neg\varphi$ on all of them. A positive answer gives $\varphi$ on one of them, chosen by the witness of non-largeness, not by us.

:::lemma{#lem-meta-question}
Let $c$, $H$, $i$ and $\varphi$ be as in the definition.

1. The relation $\{ \vec n : c \mathrel{?{\vdash}}_{H, i} \varphi(\vec n) \}$ is $\Sigma^0_2$.
2. If $c \mathrel{?{\vdash}}_{H, i} \varphi$, there are an extension $d$ of $c$ of level $n$ and a branch $I \in H$ such that every member of the part $(I, i)$ of $d$ satisfies $\varphi$.
3. If $c \mathrel{?{\nvdash}}_{H, i} \varphi$, then $(\vec \sigma, \vec X, S \cup E)$ is an extension of $c$ that promises $\neg\varphi$ on every part $(I, i)$ with $I \in H$, where $E$ is the set of indices of the classes $\mathcal V^I_{\tau, \neg\psi(m)}$ in the definition.
:::

:::proof{of=lem-meta-question}
1. The set $E$ is computable in $A \oplus \bigcup \vec X$, uniformly in the parameters $\vec n$, hence $\Delta^0_2$, since $A$ is $\Delta^0_2$ and $\bigcup \vec X \leq_T M$. By item 2 of :ref{#prop-product-complexity}, largeness of $\mathcal A^{H, i}_{c, \varphi} = \mathcal U^{\mathbb I_n}_{S \cup E}$ is $\Pi^0_1((S \cup E) \oplus M')$, hence $\Pi^0_1(\emptyset')$. Its negation is $\Sigma^0_2$.
2. As in item 2 of :ref{#lem-product-question}: there are a finite $F \subseteq S$ and finitely many triples $(I_s, m_s, \tau_s)$, $s < l$, such that $\mathcal B = \mathcal U^{\mathbb I_n}_F \cap \bigcap_{s < l} \mathcal V^{I_s}_{\tau_s, \neg\psi(m_s)}$ is not large; a $k$-partition $Y_0, \dots, Y_{k-1}$ of $\nat$ in $\mathcal M$ has $\vec Y_j \notin \mathcal B$ for all $j$; some $j$ makes $\mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\vec Y_j}$ large, so $\vec Y_j \in \mathcal U^{\mathbb I_n}_S \subseteq \mathcal U^{\mathbb I_n}_F$, and $\vec Y_j \notin \mathcal V^{I_s}_{\tau_s, \neg\psi(m_s)}$ for some $s$. Let $I = I_s$, $W_\nu = X_\nu \cap Y_{j(\nu)}$, and $T$ a $\Delta^0_2$ set with $\mathcal U^{\mathbb I_n}_T = \mathcal U^{\mathbb I_n}_S \cap \mathcal L_{\vec W}$, which is large by :ref{#lem-product-intersection}. Let $d$ have the stem $\tau_s$ on the part $(I, i)$, the stems of $c$ elsewhere, the reservoirs $W_\nu \setminus \{0, \dots, |\tau_s|\}$, and the index set $T$. Since $\tau_s$ is compatible with $(\sigma^I_i, A_i \cap \bigcup_{\nu \in I} X_\nu)$, it is a subset of $A_i$, and $d$ is a meta-condition extending $c$. A member $G$ of the part $(I, i)$ of $d$ extends $\tau_s$ with later elements in $\bigcup_{\nu \in I} Y_{j(\nu)}$; if it satisfied $\neg\psi(m_s)$, a prefix of $G$ would witness $\vec Y_j \in \mathcal V^I_{\tau_s, \neg\psi(m_s)}$. So $G$ satisfies $\psi(m_s)$.
3. The class $\mathcal U^{\mathbb I_n}_{S \cup E}$ is large, contained in $\mathcal U^{\mathbb I_n}_S$, and $S \cup E$ is $\Delta^0_2$; the promise is the definition.
:::

:::quiz[the question on meta-conditions]
Where is it used that $A$ is $\Delta^0_2$?

- [x] In item 1: the classes in the intersection are indexed by strings compatible with $(\sigma^I_i, A_i \cap \bigcup_{\nu \in I} X_\nu)$, so the set of their indices is computable in $A \oplus \bigcup \vec X$, and must be $\Delta^0_2$ for the question to be $\Sigma^0_2$.
- [ ] In item 2, to take the partition in $\mathcal M$.

  The partition is given by the Scott property of $\mathcal M$, whatever $A$ is.
- [ ] To show that some part is valid.

  :ref{#lem-meta-valid} holds for every set $A$.

---

Why does item 2 not require any part to be valid?

- [x] Because the extension forces $\varphi$ on all members of the part $(I, i)$ through its reservoirs $W_\nu \subseteq Y_{j(\nu)}$; validity is only needed to turn promises into truth.
- [ ] Because $\vec Y_j \in \mathcal U^{\mathbb I_n}_S$ makes the part $(I, i)$ valid.

  The partition does not depend on $A$, and says nothing about validity.
- [ ] Because item 2 is only applied to valid parts.

  It is applied to all branches of $H$, valid or not.
:::

## Weak merging

Two negative answers cannot be merged at the same level: duplicating the reservoirs, as in :ref{#lem-product-merging}, doubles every branch, and the duplicated branches are not branches. The index sets $\mathbb I_n$ are designed for the following form of merging.

:::lemma{#lem-meta-merging}
Let $c = (\vec \sigma, \vec X, S)$ be a meta-condition of level $n$, $H$ a non-empty set of branches of $\mathbb I_n$ and $i < 2$. Let $\varphi_0, \dots, \varphi_{2u_n}$ be $\Sigma^0_2$ sentences with $c \mathrel{?{\nvdash}}_{H, i} \varphi_a$ for every $a \leq 2u_n$. There is an extension $d$ of $c$ of level $n + 1$ such that for every $I \in H$ and all $a < b \leq 2u_n$, $d$ promises $\neg\varphi_a$ and $\neg\varphi_b$ on the part $(I \cdot \{a, b\}, i)$.
:::

:::proof{of=lem-meta-merging}
Let $\mathcal A_a = \mathcal A^{H, i}_{c, \varphi_a}$, a large class. Let $d = (\vec \tau, \vec Y, T)$ with $Y_{\nu a} = X_\nu$, stems $\tau^{I \cdot \{a, b\}}_k = \sigma^I_k$ for every branch $I$ of $\mathbb I_n$, $a < b$ and $k < 2$, and $\mathcal U^{\mathbb I_{n+1}}_T$ the class of tuples $\vec Z$ with $\vec Z^{(a)} \in \mathcal A_a$ for every $a \leq 2u_n$. As in the proof of :ref{#lem-product-merging}, $T$ is $\Delta^0_2$, the class is large and contained in $\mathcal L_{\vec Y}$, and $d$ is a meta-condition extending $c$. Let $I \in H$, $J = I \cdot \{a, b\}$, $\rho$ compatible with $(\sigma^I_i, A_i \cap \bigcup_{\mu \in J} Y_\mu) = (\sigma^I_i, A_i \cap \bigcup_{\nu \in I} X_\nu)$, $m \in \nat$, and $\vec Z \in \mathcal U^{\mathbb I_{n+1}}_T$. Then $\vec Z^{(a)} \in \mathcal A_a \subseteq \mathcal V^I_{\rho, \neg\psi_a(m)}$, so some string compatible with $(\rho, \bigcup_{\nu \in I} Z_{\nu a})$ satisfies $\neg\psi_a(m)$, and $\vec Z \in \mathcal V^J_{\rho, \neg\psi_a(m)}$. So $d$ promises $\neg\varphi_a$ on $(J, i)$, and similarly $\neg\varphi_b$.
:::

:::figure[Weak merging (:ref{#lem-meta-merging}) at level $0$, where $2u_0 + 1 = 3$. Three negative answers give three large classes $\mathcal A_0, \mathcal A_1, \mathcal A_2$. The extension triplicates the reservoir; slice $a$ ranges over $\mathcal A_a$. Each branch $\{a, b\}$ of $\mathbb I_1$ carries the stems of the old branch and the promises of $\neg\varphi_a$ and $\neg\varphi_b$.]
<svg class="fig" viewBox="0 0 600 240" width="600" role="img" aria-label="Weak merging at level 0: three negative answers give classes A_0, A_1, A_2; the extension has three copies of the reservoir, slice a ranging over A_a, and each branch a, b of I_1 promises the negations of phi_a and phi_b"><defs><marker id="jca-wm-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="170" y="10" width="260" height="44" rx="6" class="state"/><text x="300.0" y="36.0" text-anchor="middle" class="label">c of level 0: c ?⊬ φ₀, φ₁, φ₂</text><rect x="40" y="84" width="140" height="36" rx="6" class="node"/><text x="110.0" y="106.0" text-anchor="middle" class="label">𝒜₀ large</text><line x1="300" y1="56" x2="110" y2="80" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><rect x="230" y="84" width="140" height="36" rx="6" class="node"/><text x="300.0" y="106.0" text-anchor="middle" class="label">𝒜₁ large</text><line x1="300" y1="56" x2="300" y2="80" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><rect x="420" y="84" width="140" height="36" rx="6" class="node"/><text x="490.0" y="106.0" text-anchor="middle" class="label">𝒜₂ large</text><line x1="300" y1="56" x2="490" y2="80" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><rect x="40" y="170" width="140" height="52" rx="6" class="state"/><text x="110.0" y="192.0" text-anchor="middle" class="label">branch {0, 1}</text><text x="110.0" y="208.0" text-anchor="middle" class="label">promises ¬φ₀, ¬φ₁</text><line x1="110" y1="122" x2="90" y2="166" class="muted-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><line x1="300" y1="122" x2="130" y2="166" class="muted-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><rect x="230" y="170" width="140" height="52" rx="6" class="state"/><text x="300.0" y="192.0" text-anchor="middle" class="label">branch {0, 2}</text><text x="300.0" y="208.0" text-anchor="middle" class="label">promises ¬φ₀, ¬φ₂</text><line x1="110" y1="122" x2="280" y2="166" class="muted-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><line x1="490" y1="122" x2="320" y2="166" class="muted-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><rect x="420" y="170" width="140" height="52" rx="6" class="state"/><text x="490.0" y="192.0" text-anchor="middle" class="label">branch {1, 2}</text><text x="490.0" y="208.0" text-anchor="middle" class="label">promises ¬φ₁, ¬φ₂</text><line x1="300" y1="122" x2="470" y2="166" class="muted-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/><line x1="490" y1="122" x2="510" y2="166" class="muted-stroke" stroke-width="1.2" marker-end="url(#jca-wm-arr)"/></svg>
:::

The lemma is a form of weak merging (:ref{#def-weakly-merging}) with $k = 2u_n + 1$: out of $2u_n + 1$ negative answers, each descendant part receives two. The price is the growth of the level, and with it the number of branches, which the next lesson controls by counting the branches on which a requirement is not yet forced.

:::quiz[weak merging]
Why can the lemma not be applied with two negative answers only, at level $n + 1 = 1$, with $\mathbb I_1 = \{0, 1\}$?

- [x] Because with two copies, $\{0, 1\}$ would be the only branch, and a coloring of the two coordinates by the two sides need not make it monochromatic; :ref{#lem-meta-valid} would fail.
- [ ] Because the class of tuples whose slices lie in $\mathcal A_0$ and $\mathcal A_1$ would not be large.

  It would be large; the problem is the existence of a valid part.
- [ ] Because two negative answers are always merged at level $n$.

  They are not; this is the failure of merging for products.

---

In the proof of :ref{#lem-meta-merging}, why are the stems of all branches $I$, not only those in $H$, copied?

- [x] Because $d$ must have a pair of stems on every branch of $\mathbb I_{n+1}$, and copying them makes every part of $d$ extend its ancestor; promises and forcing on branches outside $H$ are then kept by :ref{#lem-meta-promise}.
- [ ] Because the branches outside $H$ are valid.

  Validity plays no role in the lemma.
- [ ] Because the question was asked for all branches.

  It was asked for those in $H$ only.
:::

## Exercises

::::exercise{difficulty=2}
Let $c$ be a meta-condition of level $n$ and $H \subseteq H'$ non-empty sets of branches. Show that $c \mathrel{?{\vdash}}_{H, i} \varphi$ implies $c \mathrel{?{\vdash}}_{H', i} \varphi$, and give an interpretation.

:::solution
The class $\mathcal A^{H', i}_{c, \varphi}$ is an intersection over more classes than $\mathcal A^{H, i}_{c, \varphi}$, so it is contained in it; a subclass of a non-large class is not large. A negative answer for $H'$ promises $\neg\varphi$ on more parts, which is harder; a positive answer for $H'$ only gives $\varphi$ on some branch of $H'$, which is weaker.
:::
::::

::::exercise{difficulty=2}
Show that for $n = 0$, a meta-condition is a pair of product Mathias conditions $(\sigma_0, \vec X, S)$ and $(\sigma_1, \vec X, S)$ with $I = \{\varepsilon\}$, and that the question $\mathrel{?{\vdash}}_{\{\{\varepsilon\}\}, i}$ differs from that of :ref{#def-product-question} only by the restriction of the stems to $A_i$.

:::solution
$\mathbb I_0 = \{\varepsilon\}$ has one branch, so $\vec\sigma$ is a pair $(\sigma_0, \sigma_1)$ and $\vec X$ a single reservoir. The class $\mathcal A^{H, i}_{c, \varphi}$ is the intersection of $\mathcal U_S$ with the classes $\mathcal V_{\tau, \neg\psi(m)}$ for $\tau$ compatible with $(\sigma_i, A_i \cap X)$, while $\mathcal A_{p, \varphi}$ uses all $\tau$ compatible with $(\sigma_i, X)$.
:::
::::

## Notes and references

The syntactic forcing relation (here: promises) on meta-conditions, the question $\mathrel{?{\vdash}}_H$ and its weak merging are due to Monin and Patey (2021); the presentation follows the section *Pigeonhole principle* of the chapter *Jump compactness avoidance* of Patey's monograph. The monograph states the lemma on promises for the branches seen as conditions with two stems, with an exercise for closure under extension; it is proved here for meta-conditions directly, with slices. In the positive case of the question, the monograph writes $D \subseteq C$ for the new index set where $D \supseteq C$ is meant.

- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, section *Pigeonhole principle*.
