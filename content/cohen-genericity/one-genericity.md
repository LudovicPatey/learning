---
title: 1-generic sets
summary: Forcing Σ⁰₁ and Π⁰₁ properties with strings; 1-generic sets decide them by a prefix; no 1-generic set is DNC; relativized cone avoidance; meager classes of degrees.
duration: 50
prerequisites: [weak-genericity, turing-degrees/low-and-high, immunity-growth/dnc-functions]
---

Weak genericity only asks a set to meet the dense c.e. sets of strings. **1-genericity**, introduced in the course on Turing degrees (:ref{#def-1-generic}), asks for more: for every c.e. set of strings $W$, the set either meets $W$, or has a prefix beyond which $W$ can no longer be met. This is exactly what is needed for every $\Sigma^0_1$ property of the set to be **decided** by a finite part of it. This lesson develops this point of view, and derives the main properties of 1-generic sets: they are generalized low, they compute no diagonally non-computable function, and they avoid every cone above a non-computable set relative to which they are generic.

## Forcing Σ⁰₁ properties

For a set of strings $W$, a string $\sigma$ **avoids** $W$ if no extension of $\sigma$ belongs to $W$; write $W^\perp$ for the set of strings avoiding $W$. The set $W \cup W^\perp$ is always dense: a string either has an extension in $W$, or avoids $W$. In these terms, :ref{#def-1-generic} says that $G$ is 1-generic if and only if $G$ meets $W \cup W^\perp$ for every c.e. set of strings $W$. If $W$ is dense, $W^\perp$ is empty, so every 1-generic set is weakly 1-generic.

:::figure[The two ways in which a 1-generic set $G$ deals with a c.e. set of strings $W$. Left: some prefix of $G$ belongs to $W$. Right: some prefix $\sigma$ of $G$ avoids $W$; the shaded subtree of the extensions of $\sigma$ contains no string of $W$, although $W$ has strings elsewhere.]
<svg class="fig" viewBox="0 0 600 250" width="600" role="img" aria-label="Two binary trees with the path of G. Left: a prefix of G belongs to W. Right: a prefix sigma of G has no extension in W; its subtree is shaded and contains no element of W"><line x1="150.0" y1="30" x2="85.0" y2="74" class="accent-stroke" stroke-width="2.2"/><line x1="150.0" y1="30" x2="215.0" y2="74" class="muted-stroke" stroke-width="1"/><line x1="85.0" y1="74" x2="52.5" y2="118" class="muted-stroke" stroke-width="1"/><line x1="85.0" y1="74" x2="117.5" y2="118" class="accent-stroke" stroke-width="2.2"/><line x1="215.0" y1="74" x2="182.5" y2="118" class="muted-stroke" stroke-width="1"/><line x1="215.0" y1="74" x2="247.5" y2="118" class="muted-stroke" stroke-width="1"/><line x1="52.5" y1="118" x2="36.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="52.5" y1="118" x2="68.8" y2="162" class="muted-stroke" stroke-width="1"/><line x1="117.5" y1="118" x2="101.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="117.5" y1="118" x2="133.8" y2="162" class="accent-stroke" stroke-width="2.2"/><line x1="182.5" y1="118" x2="166.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="182.5" y1="118" x2="198.8" y2="162" class="muted-stroke" stroke-width="1"/><line x1="247.5" y1="118" x2="231.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="247.5" y1="118" x2="263.8" y2="162" class="muted-stroke" stroke-width="1"/><line x1="36.2" y1="162" x2="28.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="36.2" y1="162" x2="44.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="68.8" y1="162" x2="60.6" y2="206" class="muted-stroke" stroke-width="1"/><line x1="68.8" y1="162" x2="76.9" y2="206" class="muted-stroke" stroke-width="1"/><line x1="101.2" y1="162" x2="93.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="101.2" y1="162" x2="109.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="133.8" y1="162" x2="125.6" y2="206" class="accent-stroke" stroke-width="2.2"/><line x1="133.8" y1="162" x2="141.9" y2="206" class="muted-stroke" stroke-width="1"/><line x1="166.2" y1="162" x2="158.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="166.2" y1="162" x2="174.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="198.8" y1="162" x2="190.6" y2="206" class="muted-stroke" stroke-width="1"/><line x1="198.8" y1="162" x2="206.9" y2="206" class="muted-stroke" stroke-width="1"/><line x1="231.2" y1="162" x2="223.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="231.2" y1="162" x2="239.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="263.8" y1="162" x2="255.6" y2="206" class="muted-stroke" stroke-width="1"/><line x1="263.8" y1="162" x2="271.9" y2="206" class="muted-stroke" stroke-width="1"/><circle cx="150.0" cy="30" r="3.5" class="accent-fill"/><circle cx="85.0" cy="74" r="3.5" class="accent-fill"/><circle cx="215.0" cy="74" r="2.5" class="muted-fill"/><circle cx="52.5" cy="118" r="2.5" class="muted-fill"/><circle cx="117.5" cy="118" r="3.5" class="accent-fill"/><circle cx="182.5" cy="118" r="5" class="ink-fill"/><circle cx="247.5" cy="118" r="2.5" class="muted-fill"/><circle cx="36.2" cy="162" r="2.5" class="muted-fill"/><circle cx="68.8" cy="162" r="2.5" class="muted-fill"/><circle cx="101.2" cy="162" r="2.5" class="muted-fill"/><circle cx="133.8" cy="162" r="5" class="ink-fill"/><circle cx="166.2" cy="162" r="2.5" class="muted-fill"/><circle cx="198.8" cy="162" r="2.5" class="muted-fill"/><circle cx="231.2" cy="162" r="2.5" class="muted-fill"/><circle cx="263.8" cy="162" r="2.5" class="muted-fill"/><circle cx="28.1" cy="206" r="2.5" class="muted-fill"/><circle cx="44.4" cy="206" r="2.5" class="muted-fill"/><circle cx="60.6" cy="206" r="5" class="ink-fill"/><circle cx="76.9" cy="206" r="2.5" class="muted-fill"/><circle cx="93.1" cy="206" r="2.5" class="muted-fill"/><circle cx="109.4" cy="206" r="2.5" class="muted-fill"/><circle cx="125.6" cy="206" r="3.5" class="accent-fill"/><circle cx="141.9" cy="206" r="2.5" class="muted-fill"/><circle cx="158.1" cy="206" r="2.5" class="muted-fill"/><circle cx="174.4" cy="206" r="2.5" class="muted-fill"/><circle cx="190.6" cy="206" r="2.5" class="muted-fill"/><circle cx="206.9" cy="206" r="2.5" class="muted-fill"/><circle cx="223.1" cy="206" r="2.5" class="muted-fill"/><circle cx="239.4" cy="206" r="5" class="ink-fill"/><circle cx="255.6" cy="206" r="2.5" class="muted-fill"/><circle cx="271.9" cy="206" r="2.5" class="muted-fill"/><text x="125.6" y="228" text-anchor="middle" class="math" font-size="15">G</text><text x="143.8" y="156" class="label">prefix in W</text><text x="150.0" y="16" text-anchor="middle" class="label">G meets W</text><path d="M417.5,110 L383.1,216 L451.9,216 z" class="soft-fill"/><line x1="450.0" y1="30" x2="385.0" y2="74" class="accent-stroke" stroke-width="2.2"/><line x1="450.0" y1="30" x2="515.0" y2="74" class="muted-stroke" stroke-width="1"/><line x1="385.0" y1="74" x2="352.5" y2="118" class="muted-stroke" stroke-width="1"/><line x1="385.0" y1="74" x2="417.5" y2="118" class="accent-stroke" stroke-width="2.2"/><line x1="515.0" y1="74" x2="482.5" y2="118" class="muted-stroke" stroke-width="1"/><line x1="515.0" y1="74" x2="547.5" y2="118" class="muted-stroke" stroke-width="1"/><line x1="352.5" y1="118" x2="336.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="352.5" y1="118" x2="368.8" y2="162" class="muted-stroke" stroke-width="1"/><line x1="417.5" y1="118" x2="401.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="417.5" y1="118" x2="433.8" y2="162" class="accent-stroke" stroke-width="2.2"/><line x1="482.5" y1="118" x2="466.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="482.5" y1="118" x2="498.8" y2="162" class="muted-stroke" stroke-width="1"/><line x1="547.5" y1="118" x2="531.2" y2="162" class="muted-stroke" stroke-width="1"/><line x1="547.5" y1="118" x2="563.8" y2="162" class="muted-stroke" stroke-width="1"/><line x1="336.2" y1="162" x2="328.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="336.2" y1="162" x2="344.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="368.8" y1="162" x2="360.6" y2="206" class="muted-stroke" stroke-width="1"/><line x1="368.8" y1="162" x2="376.9" y2="206" class="muted-stroke" stroke-width="1"/><line x1="401.2" y1="162" x2="393.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="401.2" y1="162" x2="409.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="433.8" y1="162" x2="425.6" y2="206" class="accent-stroke" stroke-width="2.2"/><line x1="433.8" y1="162" x2="441.9" y2="206" class="muted-stroke" stroke-width="1"/><line x1="466.2" y1="162" x2="458.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="466.2" y1="162" x2="474.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="498.8" y1="162" x2="490.6" y2="206" class="muted-stroke" stroke-width="1"/><line x1="498.8" y1="162" x2="506.9" y2="206" class="muted-stroke" stroke-width="1"/><line x1="531.2" y1="162" x2="523.1" y2="206" class="muted-stroke" stroke-width="1"/><line x1="531.2" y1="162" x2="539.4" y2="206" class="muted-stroke" stroke-width="1"/><line x1="563.8" y1="162" x2="555.6" y2="206" class="muted-stroke" stroke-width="1"/><line x1="563.8" y1="162" x2="571.9" y2="206" class="muted-stroke" stroke-width="1"/><circle cx="450.0" cy="30" r="3.5" class="accent-fill"/><circle cx="385.0" cy="74" r="3.5" class="accent-fill"/><circle cx="515.0" cy="74" r="2.5" class="muted-fill"/><circle cx="352.5" cy="118" r="2.5" class="muted-fill"/><circle cx="417.5" cy="118" r="3.5" class="accent-fill"/><circle cx="482.5" cy="118" r="5" class="ink-fill"/><circle cx="547.5" cy="118" r="2.5" class="muted-fill"/><circle cx="336.2" cy="162" r="2.5" class="muted-fill"/><circle cx="368.8" cy="162" r="2.5" class="muted-fill"/><circle cx="401.2" cy="162" r="2.5" class="muted-fill"/><circle cx="433.8" cy="162" r="3.5" class="accent-fill"/><circle cx="466.2" cy="162" r="2.5" class="muted-fill"/><circle cx="498.8" cy="162" r="2.5" class="muted-fill"/><circle cx="531.2" cy="162" r="2.5" class="muted-fill"/><circle cx="563.8" cy="162" r="5" class="ink-fill"/><circle cx="328.1" cy="206" r="2.5" class="muted-fill"/><circle cx="344.4" cy="206" r="5" class="ink-fill"/><circle cx="360.6" cy="206" r="2.5" class="muted-fill"/><circle cx="376.9" cy="206" r="5" class="ink-fill"/><circle cx="393.1" cy="206" r="2.5" class="muted-fill"/><circle cx="409.4" cy="206" r="2.5" class="muted-fill"/><circle cx="425.6" cy="206" r="3.5" class="accent-fill"/><circle cx="441.9" cy="206" r="2.5" class="muted-fill"/><circle cx="458.1" cy="206" r="2.5" class="muted-fill"/><circle cx="474.4" cy="206" r="2.5" class="muted-fill"/><circle cx="490.6" cy="206" r="2.5" class="muted-fill"/><circle cx="506.9" cy="206" r="2.5" class="muted-fill"/><circle cx="523.1" cy="206" r="2.5" class="muted-fill"/><circle cx="539.4" cy="206" r="2.5" class="muted-fill"/><circle cx="555.6" cy="206" r="2.5" class="muted-fill"/><circle cx="571.9" cy="206" r="2.5" class="muted-fill"/><text x="425.6" y="228" text-anchor="middle" class="math" font-size="15">G</text><text x="407.5" y="112" text-anchor="end" class="label">σ</text><text x="450.0" y="16" text-anchor="middle" class="label">a prefix σ of G avoids W</text><circle cx="190" cy="238" r="5" class="ink-fill"/><text x="200" y="242" class="label">strings of W</text><rect x="310" y="231" width="14" height="12" class="soft-fill"/><text x="330" y="242" class="label">extensions of σ: none in W</text></svg>
:::

The difference with weak genericity lies in the sets $W$ that are not dense. A weakly 1-generic set is only required to meet the dense set $W \cup W^\perp$ when this set is c.e.; but $W^\perp$ is co-c.e., and $W \cup W^\perp$ is in general not c.e. 1-genericity asks for it anyway.

:::definition{#def-relative-genericity}
Let $A$ be a set. A set $G$ is **1-generic relative to $A$** if it meets $W \cup W^\perp$ for every $A$-c.e. set of strings $W$. For $n \geq 1$, $G$ is **$n$-generic** if it is 1-generic relative to $\emptyset^{(n-1)}$, equivalently, by Post's theorem, if it meets $W \cup W^\perp$ for every $\Sigma^0_n$ set of strings $W$.
:::

:::example{#ex-relative-genericity}
1. Genericity relative to $A$ depends only on the degree of $A$, since the $A$-c.e. sets are the same for Turing equivalent oracles. If $A \leq_T B$, every set 1-generic relative to $B$ is 1-generic relative to $A$; in particular every $n$-generic set is $m$-generic for $m \leq n$.
2. No set $G$ is 1-generic relative to itself, nor relative to any $A \geq_T G$: the set $\{ \sigma : \sigma \not\prec G \}$ is $A$-computable and dense, and $G$ does not meet it. For instance, the 1-generic sets computable in $\emptyset'$ of :ref{#prop-1-generic} are not 2-generic.
:::

A **$\Sigma^0_1$ property** of sets is a property of the form "$\Phi^G_e(0)\converge$", and a **$\Pi^0_1$ property** is the negation of one. A string $\sigma$ **forces** such a property if every set extending $\sigma$ has it.

:::proposition{#prop-force-sigma1}
Let $P$ be the $\Sigma^0_1$ property "$\Phi^G_e(0)\converge$", and $W = \{ \sigma : \Phi^\sigma_e(0)\converge \}$, a c.e. set of strings.

1. Every string in $W$ forces $P$, and every string forcing $P$ has an extension in $W$.
2. A string forces $\neg P$ if and only if it avoids $W$.
:::

:::proof{of=prop-force-sigma1}
1. If $\Phi^\sigma_e(0)\converge$, every $X \succ \sigma$ has $\Phi^X_e(0)\converge$ (:ref{#prop-oracle-stages}). If $\sigma$ forces $P$, take any $X \succ \sigma$; then $\Phi^{X \uh k}_e(0)\converge$ for some $k \geq |\sigma|$, and $X \uh k$ is an extension of $\sigma$ in $W$.
2. If $\sigma$ avoids $W$ and $X \succ \sigma$ had $\Phi^X_e(0)\converge$, some prefix $X \uh k$ with $k \geq |\sigma|$ would be an extension of $\sigma$ in $W$. Conversely, if $\sigma$ has an extension $\tau \in W$, every $X \succ \tau$ satisfies $P$, so $\sigma$ does not force $\neg P$.
:::

:::theorem{#thm-1generic-decides}
Let $G$ be 1-generic. For every $\Sigma^0_1$ property $P$, $G$ has a prefix that forces $P$ or a prefix that forces $\neg P$; and $G$ satisfies $P$ if and only if some prefix of $G$ forces $P$.
:::

:::proof{of=thm-1generic-decides}
With $W$ as above, $G$ meets $W \cup W^\perp$. If a prefix of $G$ is in $W$, it forces $P$; if a prefix avoids $W$, it forces $\neg P$ by :ref{#prop-force-sigma1}. A property forced by a prefix of $G$ holds for $G$, so $G$ satisfies $P$ exactly in the first case.
:::

The theorem is the reason why 1-generic sets are **generalized low** (:ref{#thm-generic-low}): to decide whether $e \in G'$, it suffices to find a prefix of $G$ that belongs to $\{ \sigma : \Phi^\sigma_e(e)\converge \}$ or avoids it, and both relations are decided by $\emptyset'$, the first being c.e. and the second co-c.e. Soare calls this **forcing the jump**. The converse also holds: a set that decides every property "$\Phi^G_e(e)\converge$" by a prefix is 1-generic, since by the parameter theorem every c.e. set of strings $W$ can be turned into an index $e$ such that $\Phi^X_e(e)\converge$ if and only if $X$ meets $W$, for every set $X$; a prefix forcing the divergence of $\Phi^X_e(e)$ then avoids $W$ (Soare 2016, Theorem 6.3.2, credited to Jockusch and Posner).

:::quiz[forcing Σ⁰₁ properties]
Why does a string $\sigma$ that avoids $W = \{ \sigma : \Phi^\sigma_e(0)\converge \}$ force the divergence of $\Phi^G_e(0)$?

- [x] Because a convergent computation $\Phi^X_e(0)$ with $X \succ \sigma$ would converge already with some prefix of $X$ extending $\sigma$, which would be an extension of $\sigma$ in $W$.
- [ ] Because $\sigma \notin W$.

  Not being in $W$ only says that the computation does not converge with oracle $\sigma$ itself; longer prefixes might make it converge.
- [ ] Because $W$ is c.e.

  The complexity of $W$ plays no role in this implication.

---

Why is every 1-generic set weakly 1-generic?

- [x] If $W$ is dense, no string avoids it, so $W^\perp = \emptyset$, and meeting $W \cup W^\perp$ means meeting $W$.
- [ ] Because $W \cup W^\perp$ is contained in $W$.

  It is equal to $W$ only when $W^\perp$ is empty, that is, when $W$ is dense.
- [ ] Because every c.e. set of strings is dense.

  Many c.e. sets of strings are not dense, for instance the set of strings beginning with $0$.
:::

## 1-generic sets are not DNC

Recall from :ref{#def-dnc} that a total function $f$ is **diagonally non-computable**, or **DNC**, if $f(e) \neq \Phi_e(e)$ for every $e$ with $\Phi_e(e)\converge$. The PA sets of the course on $\Pi^0_1$ classes compute $\{0, 1\}$-valued DNC functions; $\emptyset'$ computes DNC functions.

The proof turns the 1-genericity of $G$ against a reduction $\Phi^G_i$ that would be DNC. For each string $\sigma$, a program $e_\sigma$ looks for an extension of $\sigma$ on which $\Phi_i$ converges at the argument $e_\sigma$, and copies the value found; the fixed point theorem lets the program know its own index. Along $G$, this search always succeeds, which prevents prefixes of $G$ from avoiding the strings found; and the strings found are never prefixes of $G$, since $\Phi^G_i$ must differ from the copied value $\Phi_{e_\sigma}(e_\sigma)$.

:::theorem[Demuth, Kučera]{#thm-generic-not-dnc}
No 1-generic set computes a DNC function.
:::

:::proof{of=thm-generic-not-dnc}
Let $G$ be 1-generic, and suppose that $\Phi^G_i$ is a total DNC function. For a string $\sigma$ and an index $e$, consider the program that searches for an extension $\tau \succeq \sigma$ with $\Phi^\tau_i(e)\converge$ and outputs the value of the first one found. By the fixed point theorem with parameters (:ref{#thm-fixed-point-parameters}), there is a computable function $\sigma \mapsto e_\sigma$ such that the program $e_\sigma$, on any input, searches for an extension $\tau_\sigma \succeq \sigma$ with $\Phi^{\tau_\sigma}_i(e_\sigma)\converge$, and outputs $\Phi^{\tau_\sigma}_i(e_\sigma)$. Let $W$ be the c.e. set of the strings $\tau_\sigma$ found in this way, for all $\sigma$.

*No prefix of $G$ belongs to $W$.* If $\tau_\sigma \prec G$, then $\sigma \prec G$ and $\Phi^G_i(e_\sigma) = \Phi^{\tau_\sigma}_i(e_\sigma) = \Phi_{e_\sigma}(e_\sigma)$, contradicting the fact that $\Phi^G_i$ is DNC.

*No prefix of $G$ avoids $W$.* If $\sigma \prec G$, the search of the program $e_\sigma$ succeeds, since $G$ itself makes $\Phi_i(e_\sigma)$ converge, and the string $\tau_\sigma$ it finds is an extension of $\sigma$ in $W$.

So $G$ does not meet $W \cup W^\perp$, contradicting its 1-genericity.
:::

:::corollary{#cor-generic-not-pa}
No 1-generic set is PA or computes $\emptyset'$.
:::

:::proof{of=cor-generic-not-pa}
PA sets and $\emptyset'$ compute DNC functions.
:::

The hypothesis of 1-genericity cannot be weakened to weak 1-genericity: every hyperimmune degree contains a weakly 1-generic set (Kurtz, admitted in the previous lesson), and the degree of $\emptyset'$ is hyperimmune, so some weakly 1-generic set computes $\emptyset'$.

:::quiz[the Demuth–Kučera theorem]
Why does the proof need the fixed point theorem?

- [x] So that the program $e_\sigma$ can search for a computation of $\Phi_i$ at its own index $e_\sigma$, and output its value, making its diagonal value $\Phi_{e_\sigma}(e_\sigma)$ agree with $\Phi^{\tau_\sigma}_i$.
- [ ] To make the function $\sigma \mapsto e_\sigma$ total.

  Any computable function of $\sigma$ is total; what the fixed point theorem provides is that the program $e_\sigma$ can refer to its own index.
- [ ] To show that $W$ is c.e.

  Once the indices are fixed, the enumeration of $W$ is an ordinary dovetailed search.
:::

## Genericity and cones

The cone avoidance theorem of the course on Turing degrees (:ref{#thm-cone-avoidance}) builds a set that does not compute a given non-computable set $C$. Its dense sets are not c.e., since they mention $C$; they are c.e. relative to $C$. Genericity relative to $C$ is therefore the right hypothesis, and the argument relativizes to an additional oracle $Z$.

:::theorem{#thm-generic-cone}
Let $C$ and $Z$ be sets with $C \not\leq_T Z$. If $G$ is 1-generic relative to $C \oplus Z$, then $C \not\leq_T G \oplus Z$. In particular, if $C$ is not computable and $G$ is 1-generic relative to $C$, then $C \not\leq_T G$.
:::

:::proof{of=thm-generic-cone}
Fix $e$. For a string $\sigma$, write $\sigma \oplus Z$ for the partial oracle that has the bits of $\sigma$ at the even positions below $2|\sigma|$ and the bits of $Z$ at the odd positions; a computation with this oracle is defined as long as it reads no even position $2k$ with $k \geq |\sigma|$. Let $W$ be the set of strings $\sigma$ such that $\Phi^{\sigma \oplus Z}_e(n)\converge \neq C(n)$ for some $n$; it is $(C \oplus Z)$-c.e. The set $G$ meets $W \cup W^\perp$.

If a prefix of $G$ is in $W$, then $\Phi^{G \oplus Z}_e(n)\converge \neq C(n)$ for some $n$. Otherwise some $\sigma \prec G$ avoids $W$: for every $\tau \succeq \sigma$ and every $n$, if $\Phi^{\tau \oplus Z}_e(n)\converge$ then its value is $C(n)$. If $\Phi^{G \oplus Z}_e$ were total, $C$ would then be $Z$-computable: to compute $C(n)$, search for $\tau \succeq \sigma$ with $\Phi^{\tau \oplus Z}_e(n)\converge$ — prefixes of $G$ provide one — and output the value. So $\Phi^{G \oplus Z}_e \neq C$, for every $e$.
:::

The genericity relative to $C$ cannot be replaced by plain 1-genericity: a 1-generic set $G$ computes the non-computable set $C = G$, and by :ref{#ex-relative-genericity} it is not 1-generic relative to $G$. The next lesson shows that, for every non-computable set $A$, some 1-generic set $G$ satisfies $A \oplus G \geq_T \emptyset'$: joined with $A$, a 1-generic set can compute much more than $A$ alone.

## Meager classes of degrees

The class of 1-generic sets relative to a fixed set is co-meager, so every property implied by such genericity holds for all sufficiently generic sets.

:::corollary{#cor-meager-degrees}
The following classes are meager:

1. for each non-computable $C$, the class of sets computing $C$;
2. the class of sets computing a DNC function, and in particular the class of PA sets;
3. the class of computably dominated sets;
4. the class of high sets.
:::

:::proof{of=cor-meager-degrees}
1. By :ref{#thm-generic-cone} with $Z = \emptyset$.
2. By :ref{#thm-generic-not-dnc}.
3. Weakly 1-generic sets are not computably dominated, by :ref{#cor-delta2-weak-generic}.
4. Let $G$ be 1-generic relative to $\emptyset''$. Then $G$ is 1-generic, so $G' \equiv_T G \oplus \emptyset'$ (:ref{#thm-generic-low} and the exercises of that lesson). By :ref{#thm-generic-cone} with $C = \emptyset''$ and $Z = \emptyset'$, since $\emptyset'' \not\leq_T \emptyset'$ and $G$ is 1-generic relative to $\emptyset'' \equiv_T \emptyset'' \oplus \emptyset'$, we get $\emptyset'' \not\leq_T G \oplus \emptyset' \equiv_T G'$. So $G$ is not high.
:::

Items 2 and 3 show that typical sets in the sense of category compute no DNC function and are not computably dominated. In the sense of measure, the situation is reversed for DNC functions: every Martin-Löf random sequence computes a DNC function, so the class of sets computing a DNC function has measure $1$ (:ref{to="martin-lof-randomness/random-dnc"}). The comparison of the typical degree in the sense of measure and in the sense of category is the subject of a paper of Barmpalias, Day and Lewis-Pye (2014).

## Exercises

::::exercise{difficulty=1}
Show directly that no 1-generic set is computable.

:::solution
Let $X$ be computable, and $W = \{ (X \uh n)\, (1 - X(n)) : n \in \nat \}$, a computable set of strings. No prefix of $X$ is in $W$, and every prefix $X \uh n$ has the extension $(X \uh n)(1 - X(n))$ in $W$, so no prefix of $X$ avoids $W$. So $X$ does not meet $W \cup W^\perp$.
:::
::::

::::exercise{difficulty=2}
Let $G = G_0 \oplus G_1$ be 1-generic. Show that $G_0 \not\leq_T G_1$ and $G_1 \not\leq_T G_0$.

:::solution
Suppose $\Phi^{G_1}_e = G_0$. For a string $\sigma$, write $\sigma_0$ and $\sigma_1$ for the strings of its bits at even and at odd positions. Let $W$ be the c.e. set of strings $\sigma$ such that $\Phi^{\sigma_1}_e(n)\converge \neq \sigma_0(n)$ for some $n < |\sigma_0|$. No prefix of $G$ is in $W$, since $\Phi^{G_1}_e = G_0$. Let $\sigma \prec G$. Take $n = |\sigma_0|$, and a prefix $\tau \prec G$ extending $\sigma$, long enough that $\Phi^{\tau_1}_e(n)\converge$ and $|\tau_0| > n$. Let $\tau'$ be $\tau$ with the even bit of index $n$ flipped. Then $\tau' \succeq \sigma$, its odd part is $\tau_1$, so $\Phi^{\tau'_1}_e(n)\converge = G_0(n) \neq \tau'_0(n)$, and $\tau' \in W$. So no prefix of $G$ avoids $W$, contradicting the 1-genericity of $G$. The other half is symmetric.
:::
::::

::::exercise{difficulty=2}
A set $X$ is **left-c.e.** if there is a computable sequence of finite sets $X_0, X_1, \dots$ such that each $X_{s+1}$ is lexicographically greater than $X_s$, as infinite binary sequences, and $X(n) = \lim_s X_s(n)$ for every $n$. Show that no left-c.e. set is 1-generic.

:::hint
Enumerate the strings $X_s \uh (n_s + 1)$, where $n_s$ is the first position at which $X_s$ and $X_{s+1}$ differ.
:::

:::solution
Since $X_s <_{\mathrm{lex}} X_{s+1}$, the first position $n_s$ at which they differ has $X_s(n_s) = 0$ and $X_{s+1}(n_s) = 1$. Let $W = \{ X_s \uh (n_s + 1) : s \in \nat \}$, a c.e. set of strings.

First, $X_t \leq_{\mathrm{lex}} X$ for every $t$. Otherwise $X$ and $X_t$ first differ at some $p$ with $X(p) = 0$ and $X_t(p) = 1$; for $u$ large enough, $X_u \uh (p + 1) = X \uh (p + 1)$, so $X_u <_{\mathrm{lex}} X_t$ with $u > t$, which is impossible. Hence $X \geq_{\mathrm{lex}} X_{s+1}$ for every $s$.

*No prefix of $X$ is in $W$.* If $X \uh (n_s + 1) = X_s \uh (n_s + 1)$, then $X$ and $X_{s+1}$ agree below $n_s$ and $X(n_s) = 0 < 1 = X_{s+1}(n_s)$, so $X <_{\mathrm{lex}} X_{s+1}$, a contradiction.

*No prefix of $X$ avoids $W$.* Let $k \in \nat$, and $s$ large enough that $X_s \uh k = X_{s+1} \uh k = X \uh k$. Then $n_s \geq k$, and $X_s \uh (n_s + 1) \in W$ extends $X \uh k$.

So $X$ does not meet $W \cup W^\perp$. The same proof shows that no set left-c.e. relative to $A$ is 1-generic relative to $A$. On the other hand, there are left-c.e. sets that are weakly 1-generic (Monin and Patey, chapter *Cohen forcing*, exercise after the comparison of weak and full genericity); this gives another separation of the two notions.
:::
::::

## Notes and references

1-generic sets were introduced by Jockusch (1980), who proved most of their basic properties; Soare (2016, §6.3) credits the characterization by forcing the jump to Jockusch and Posner. The theorem that 1-generic sets are not DNC is due to Demuth and Kučera (1987); the proof by the fixed point theorem given here is the one of Monin and Patey, while Downey and Hirschfeldt (2010, Theorem 2.24.5) give a proof through a co-c.e. set of strings. The meagerness of the high sets and of the computably dominated sets is classical. The exercise on left-c.e. sets is taken from Monin and Patey.

- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- O. Demuth and A. Kučera, *Remarks on 1-genericity, semigenericity and related concepts*, Commentationes Mathematicae Universitatis Carolinae 28 (1987), 85–94.
- G. Barmpalias, A. R. Day and A. E. M. Lewis-Pye, *The typical Turing degree*, Proceedings of the London Mathematical Society 109 (2014), 1–39.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §6.3.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, §2.24.
- B. Monin and L. Patey, *Computability theory*, chapter *Cohen forcing*, section *Effective genericity*.
