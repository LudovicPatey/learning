---
title: Merging by duplication
summary: Two negative answers of product Mathias forcing are merged by duplicating the reservoirs, and the generic set has a jump that is not PA relative to ∅′; the theorem of Monin and Patey for Δ⁰₂ sets, and why a pair of stems with product reservoirs may have no valid side.
duration: 35
prerequisites: [product-mathias, jump-cone-avoidance/pigeonhole-forcing, lowness/cjs-theorem, ramsey-theorem/cone-avoidance]
---

The previous lesson defined product Mathias forcing and its question for $\Sigma^0_2$ sentences. This lesson proves that two negative answers can be merged, by keeping both classes on two copies of the reservoirs, and deduces with the three-case argument of :ref{#thm-jump-pa-merging} that the generic set has a jump that is not PA relative to $\emptyset'$. It then turns to the pigeonhole principle, the subject of the rest of the course, and shows on an example why product Mathias forcing with a pair of stems does not suffice.

## Merging by duplication

Two negative answers give two large classes $\mathcal A_{p, \varphi_0}$ and $\mathcal A_{p, \varphi_1}$ of possible tuples of reservoirs (:ref{#lem-product-question}), whose intersection need not be large. Instead of intersecting them, the extension keeps two copies of the reservoirs, and asks the first copy to range over the first class and the second copy over the second. A product of two large classes is large, so nothing is lost; the stem may later use both copies.

:::lemma{#lem-product-merging}
Let $p = (\sigma, \vec X, S)$ be a condition with index set $I$, and let $\varphi_0, \varphi_1$ be $\Sigma^0_2$ sentences with $p \mathrel{?{\nvdash}} \varphi_0$ and $p \mathrel{?{\nvdash}} \varphi_1$. There is an extension of $p$ with index set $I \cdot \{0, 1\}$ that promises $\neg\varphi_0$ and $\neg\varphi_1$.
:::

:::proof{of=lem-product-merging}
Let $\mathcal A_b = \mathcal A_{p, \varphi_b}$ for $b < 2$; both are large. Let $Y_{\nu b} = X_\nu$, and let $\mathcal C$ be the class of $(I \cdot \{0, 1\})$-tuples $\vec Z$ with $\vec Z^{(0)} \in \mathcal A_0$ and $\vec Z^{(1)} \in \mathcal A_1$. It is $\mathcal U^{I \cdot \{0, 1\}}_T$ for a $\Delta^0_2$ set $T$ computed from the sets of indices $S \cup E_0$ and $S \cup E_1$ of $\mathcal A_0$ and $\mathcal A_1$ (:ref{#lem-product-question}), translating each index into an index of the same class read on the corresponding slice. It is large, since for a cover one chooses $j$ on each slice separately, and it is contained in $\mathcal L_{\vec Y}$, since $\mathcal A_b \subseteq \mathcal L_{\vec X}$. So $q = (\sigma, \vec Y, T)$ is a condition. It extends $p$: its slices are in $\mathcal A_b \subseteq \mathcal U^I_S$. Let $\tau$ be compatible with $(\sigma, \bigcup \vec Y) = (\sigma, \bigcup \vec X)$, $m \in \nat$ and $\vec Z \in \mathcal C$. Then $\vec Z^{(0)} \in \mathcal A_0 \subseteq \mathcal V^I_{\tau, \neg\psi_0(m)}$, so $\vec Z \in \mathcal V^{I \cdot \{0, 1\}}_{\tau, \neg\psi_0(m)}$ as in the proof of :ref{#lem-product-promise}. So $q$ promises $\neg\varphi_0$, and similarly $\neg\varphi_1$.
:::

:::quiz[the merging lemma]
In the proof of :ref{#lem-product-merging}, why is $q$ not obtained by taking the intersection $\mathcal A_0 \cap \mathcal A_1$ with the same reservoirs?

- [x] Because $\mathcal A_0 \cap \mathcal A_1$ need not be large (:ref{#lem-no-two-sides}); the product of the two classes on two copies of the reservoirs is always large.
- [ ] Because $\mathcal A_0 \cap \mathcal A_1$ is not a $\Sigma^0_1(\mathcal M)$ class.

  It is $\mathcal U^I_{S \cup E_0 \cup E_1}$, with a $\Delta^0_2$ set of indices; definability is not the issue.
- [ ] Because the index set must grow at every extension.

  Extensions may keep the index set, as in :ref{#lem-product-question}.
:::

:::figure[Merging by duplication (:ref{#lem-product-merging}). The two negative answers give two large classes $\mathcal A_0$ and $\mathcal A_1$ of $I$-tuples, whose intersection need not be large. The extension duplicates the reservoirs: slice $0$ of the new tuple ranges over $\mathcal A_0$ and slice $1$ over $\mathcal A_1$, and the stem may use both.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Merging by duplication: a condition with index set I and two negative answers giving classes A_0 and A_1 is extended by a condition with index set I times 0,1 whose slice 0 ranges over A_0 and slice 1 over A_1, with the same stem and copied reservoirs"><defs><marker id="jca-pm-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="200" y="10" width="200" height="52" rx="6" class="state"/><text x="300.0" y="32.0" text-anchor="middle" class="label">p, reservoirs X, index set I</text><text x="300.0" y="48.0" text-anchor="middle" class="label">p ?⊬ φ₀ and p ?⊬ φ₁</text><rect x="20" y="100" width="200" height="44" rx="6" class="node"/><text x="120.0" y="126.0" text-anchor="middle" class="label">𝒜₀ = 𝒜(p, φ₀) large</text><rect x="380" y="100" width="200" height="44" rx="6" class="node"/><text x="480.0" y="126.0" text-anchor="middle" class="label">𝒜₁ = 𝒜(p, φ₁) large</text><rect x="130" y="186" width="340" height="52" rx="6" class="state"/><text x="300.0" y="208.0" text-anchor="middle" class="label">q: stem σ, reservoirs X copied twice, index set I·{0, 1}</text><text x="300.0" y="224.0" text-anchor="middle" class="label">slice 0 ∈ 𝒜₀, slice 1 ∈ 𝒜₁</text><line x1="250" y1="64" x2="140" y2="96" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><line x1="350" y1="64" x2="460" y2="96" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><line x1="140" y1="146" x2="230" y2="182" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><line x1="460" y1="146" x2="370" y2="182" class="ink-stroke" stroke-width="1.2" marker-end="url(#jca-pm-arr)"/><text x="300" y="132" text-anchor="middle" class="label">𝒜₀ ∩ 𝒜₁ need not be large</text></svg>
:::

The duplication is what a single class could not do (:ref{#lem-no-two-sides}): for the sentences "$G \cap R$ is finite" and "$G \setminus R$ is finite", slice $0$ can provide the elements of $R$ and slice $1$ those of $\overline R$ (first exercise below).

## The theorem

:::theorem{#thm-product-mathias}
There is a sequence of conditions $p_0 \geq p_1 \geq \cdots$ whose stems define an infinite set $G$, a member of every $p_s$, such that $G'$ is not PA relative to $\emptyset'$.
:::

:::proof{of=thm-product-mathias}
Start with $p_0 = (\varepsilon, \langle \nat \rangle, S_\infty)$, and handle in turn, each infinitely often, the following tasks: extend the stem, by item 1 of :ref{#lem-product-basic}; for a $\Pi^0_2$ sentence $\forall y\ \theta(y)$ and a number $m$, if the current condition promises it, pass to an extension forcing $\theta(m)$, by :ref{#lem-product-promise}; and for an index $e$, the requirement below. The stems are compatible, so they define a set $G$, infinite by the first task, and a member of every $p_s$. If $p_s$ promises $\forall y\ \theta(y)$, so do all later conditions, and the second task makes $G$ satisfy each $\theta(m)$.

*The requirement.* Let $p$ be the current condition, and $U$ the set of pairs $(x, v) \in \nat \times \{0, 1\}$ with $p \mathrel{?{\vdash}} \chi_{e, x, v}$, the sentence "$\Phi^{G'}_e(x)\converge = v$" (:ref{to="jump-compactness-avoidance/merging-level-two"}). It is $\Sigma^0_2$ by item 1 of :ref{#lem-product-question}. If $(x, J^{\emptyset'}(x)) \in U$ for some $x$ with $J^{\emptyset'}(x)$ defined, item 2 gives an extension all of whose members, $G$ among them, satisfy $\Phi^{G'}_e(x) = J^{\emptyset'}(x)$. If $(x, 0), (x, 1) \notin U$ for some $x$, :ref{#lem-product-merging} gives an extension promising $\neg\chi_{e, x, 0}$ and $\neg\chi_{e, x, 1}$, which $G$ then satisfies: $\Phi^{G'}_e(x)$ has no value in $\{0, 1\}$. Otherwise, as in the proof of :ref{#thm-jump-pa-merging}, $U$ yields a $\emptyset'$-computable $\{0, 1\}$-valued function DNC relative to $\emptyset'$, which does not exist. So no $\Phi^{G'}_e$ is $\mathrm{DNC}_2$ relative to $\emptyset'$.
:::

Unlike the forcing of :ref{#prop-one-reservoir-cohesive}, this one cannot always replace the reservoirs by their intersections with a set or with its complement, and by the theorem it builds no cohesive set for the sequence of :ref{#prop-coh-no-low}.

## The pigeonhole principle

:::theorem[Monin, Patey]{#thm-d22-jump-pa}
Let $D \leq_T Z$ be sets such that $Z'$ is not PA relative to $D'$, and let $A$ be a $\Delta^0_2(Z)$ set. There is an infinite set $H$, contained in $A$ or in $\overline A$, such that $(Z \oplus H)'$ is not PA relative to $D'$. So $\mathsf D^2_2$ admits jump PA avoidance.
:::

We write the proof for $Z = D = \emptyset$, so that $A$ is $\Delta^0_2$ and the conclusion is that $H'$ is not PA relative to $\emptyset'$; the general case is explained at the end of :ref{to="jump-compactness-avoidance/delta2-jump-pa"}, which completes the proof begun in :ref{to="jump-compactness-avoidance/meta-conditions"} and :ref{to="jump-compactness-avoidance/meta-questions"}. Write $A_0 = A$ and $A_1 = \overline A$. The plan follows the proof of :ref{#thm-d22-weakly-low} by Cholak, Jockusch and Slaman, and the forcing of Dzhafarov and Jockusch (:ref{#thm-dj-cone-avoidance}): conditions with two stems, $\sigma_0 \subseteq A_0$ and $\sigma_1 \subseteq A_1$, sharing their reservoirs. Here the reservoirs are those of product Mathias forcing. This section explains why a pair of stems does not suffice.

### Valid sides

Consider for a moment quadruples $(\sigma_0, \sigma_1, \vec X, S)$ such that $(\sigma_i, \vec X, S)$ is a condition of product Mathias forcing (:ref{#def-product-condition}) with $\sigma_i \subseteq A_i$, for $i < 2$. The reservoirs contain elements of both $A_0$ and $A_1$, and side $i$ is useful only if the class $\mathcal U^I_S$ allows reservoirs inside $A_i$. As in :ref{#def-valid-part}, call side $i$ **valid** if $\mathcal U^I_S \cap \mathcal L_{\langle X_\nu \cap A_i : \nu \in I \rangle}$ is large.

If $I$ is a singleton, some side is valid. By :ref{#lem-product-cover} applied to the cover $A_0, A_1$ of $\nat$, some $i$ makes $\mathcal U^I_S \cap \mathcal L_{\langle A_i \rangle}$ large, and since $\mathcal U^I_S \subseteq \mathcal L_{\vec X}$, :ref{#lem-product-intersection} makes $\mathcal U^I_S \cap \mathcal L_{\langle X \cap A_i \rangle}$ large. For two coordinates this fails, and merging is the cause. Let $A$ be computable, infinite and coinfinite, and apply the first exercise below with $R = A$ to the condition $(\varepsilon, \langle \nat \rangle, S_\infty)$. The extension has the reservoirs $(\nat, \nat)$, and the members $(Z_0, Z_1)$ of its class have $Z_0 \cap A$ and $Z_1 \setminus A$ infinite. Side $0$ is valid only if this class intersected with $\mathcal L_{(A, A)}$ is large. For the cover $A_0, A_1$ of $\nat$, the second coordinate of a pair of parts in the intersection would meet both $A$ and $\overline A$ infinitely often, which neither part does. So side $0$ is not valid, and symmetrically side $1$ is not valid: the stems can grow on neither side.

The cover lemma still says something for two coordinates: it gives $j : I \to 2$ such that $\mathcal U^I_S \cap \mathcal L_{\langle X_\nu \cap A_{j(\nu)} \rangle}$ is large. The function $j$ colors the coordinates. If two coordinates out of three have the same color $i$, the pair of these two coordinates has a valid side $i$. This suggests keeping, instead of one pair of stems for the whole tuple, one pair of stems for each sub-tuple in a family with a Ramsey property: every $2$-coloring of the coordinates makes some member of the family monochromatic. Weak merging, with three negative answers instead of two, provides such families; they are the subject of the next lesson.

## Exercises

::::exercise{difficulty=1}
Let $p = (\sigma, \vec X, S)$ be a condition and $R$ a computable set such that $\mathcal U^I_S \cap \mathcal L_{\langle R \rangle_\nu}$ and $\mathcal U^I_S \cap \mathcal L_{\langle \overline R \rangle_\nu}$ are both large, where $\langle R \rangle_\nu$ is the tuple with all coordinates $R$. Show that some extension of $p$ promises that $G \cap R$ and $G \setminus R$ are infinite.

:::solution
The sentence "$G \cap R$ is finite" is $\exists y\ \psi(y)$ with $\psi(y)$: no element $z \geq y$ of $G$ is in $R$. For $\tau$ compatible with $(\sigma, \bigcup \vec X)$, the class $\mathcal V^I_{\tau, \neg\psi(m)}$ contains every tuple $\vec Z$ such that $\bigcup \vec Z \cap R$ has an element larger than or equal to $\max(m, |\tau|)$. So $\mathcal A_{p, \varphi}$ contains $\mathcal U^I_S \cap \mathcal L_{\langle R \rangle_\nu}$, which is large, and $p \mathrel{?{\nvdash}} \varphi$. Similarly for "$G \setminus R$ is finite". Apply :ref{#lem-product-merging}.
:::
::::

## Notes and references

The merging lemma and the theorem follow the section *Product Mathias forcing* of the chapter *Jump compactness avoidance* of Patey's monograph, after Monin and Patey (2021), where the theorem is obtained from the abstract exercise on merging questions. :ref{#thm-d22-jump-pa} is the main theorem of Monin and Patey (2021); the discussion of valid sides follows the section *Pigeonhole principle* of the monograph. The forcing with two stems and one reservoir is that of Dzhafarov and Jockusch (2009).

- D. D. Dzhafarov and C. G. Jockusch, Jr., *Ramsey's theorem and cone avoidance*, Journal of Symbolic Logic 74 (2009), 557–578.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, sections *Product Mathias forcing* and *Pigeonhole principle*.
