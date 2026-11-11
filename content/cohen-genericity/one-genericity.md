---
title: 1-generic sets
summary: Forcing Σ⁰₁ and Π⁰₁ properties with strings; 1-generic sets decide them by a prefix; no 1-generic set is DNC; relativized cone avoidance; meager classes of degrees.
duration: 45
prerequisites: [weak-genericity, turing-degrees/low-and-high]
---

Weak genericity only asks a set to meet the dense c.e. sets of strings. **1-genericity**, introduced in the course on Turing degrees (:ref{#def-1-generic}), asks for more: for every c.e. set of strings $W$, the set either meets $W$, or has a prefix beyond which $W$ can no longer be met. This is exactly what is needed for every $\Sigma^0_1$ property of the set to be **decided** by a finite part of it. This lesson develops this point of view, and derives the main properties of 1-generic sets: they are generalized low, they compute no diagonally non-computable function, and they avoid every cone above a non-computable set relative to which they are generic.

## Forcing Σ⁰₁ properties

For a set of strings $W$, a string $\sigma$ **avoids** $W$ if no extension of $\sigma$ belongs to $W$; write $W^\perp$ for the set of strings avoiding $W$. The set $W \cup W^\perp$ is always dense: a string either has an extension in $W$, or avoids $W$. In these terms, :ref{#def-1-generic} says that $G$ is 1-generic if and only if $G$ meets $W \cup W^\perp$ for every c.e. set of strings $W$. If $W$ is dense, $W^\perp$ is empty, so every 1-generic set is weakly 1-generic.

:::definition{#def-relative-genericity}
Let $A$ be a set. A set $G$ is **1-generic relative to $A$** if it meets $W \cup W^\perp$ for every $A$-c.e. set of strings $W$. For $n \geq 1$, $G$ is **$n$-generic** if it is 1-generic relative to $\emptyset^{(n-1)}$, equivalently, by Post's theorem, if it meets $W \cup W^\perp$ for every $\Sigma^0_n$ set of strings $W$.
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

The theorem is the reason why 1-generic sets are **generalized low** (:ref{#thm-generic-low}): to decide whether $e \in G'$, it suffices to find a prefix of $G$ that belongs to $\{ \sigma : \Phi^\sigma_e(e)\converge \}$ or avoids it, and both relations are decided by $\emptyset'$, the first being c.e. and the second co-c.e.

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

A function $f$ is **diagonally non-computable**, or **DNC**, if $f(e) \neq \Phi_e(e)$ for every $e$ with $\Phi_e(e)\converge$. The PA sets of the course on $\Pi^0_1$ classes compute $\{0, 1\}$-valued DNC functions; $\emptyset'$ computes DNC functions.

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

:::quiz[the Demuth–Kučera theorem]
Why does the proof need the fixed point theorem?

- [x] So that the program $e_\sigma$ can search for a computation of $\Phi_i$ at its own index $e_\sigma$, and output its value, making its diagonal value $\Phi_{e_\sigma}(e_\sigma)$ agree with $\Phi^{\tau_\sigma}_i$.
- [ ] To make the function $\sigma \mapsto e_\sigma$ total.

  Any computable function of $\sigma$ is total; what the fixed point theorem provides is that the program $e_\sigma$ can refer to its own index.
- [ ] To show that $W$ is c.e.

  Once the indices are fixed, the enumeration of $W$ is an ordinary dovetailed search.
:::

## Genericity and cones

:::theorem{#thm-generic-cone}
Let $C$ and $Z$ be sets with $C \not\leq_T Z$. If $G$ is 1-generic relative to $C \oplus Z$, then $C \not\leq_T G \oplus Z$. In particular, if $C$ is not computable and $G$ is 1-generic relative to $C$, then $C \not\leq_T G$.
:::

:::proof{of=thm-generic-cone}
Fix $e$. For a string $\sigma$, write $\sigma \oplus Z$ for the partial oracle that has the bits of $\sigma$ at the even positions below $2|\sigma|$ and the bits of $Z$ at the odd positions; a computation with this oracle is defined as long as it reads no even position $2k$ with $k \geq |\sigma|$. Let $W$ be the set of strings $\sigma$ such that $\Phi^{\sigma \oplus Z}_e(n)\converge \neq C(n)$ for some $n$; it is $(C \oplus Z)$-c.e. The set $G$ meets $W \cup W^\perp$.

If a prefix of $G$ is in $W$, then $\Phi^{G \oplus Z}_e(n)\converge \neq C(n)$ for some $n$. Otherwise some $\sigma \prec G$ avoids $W$: for every $\tau \succeq \sigma$ and every $n$, if $\Phi^{\tau \oplus Z}_e(n)\converge$ then its value is $C(n)$. If $\Phi^{G \oplus Z}_e$ were total, $C$ would then be $Z$-computable: to compute $C(n)$, search for $\tau \succeq \sigma$ with $\Phi^{\tau \oplus Z}_e(n)\converge$ — prefixes of $G$ provide one — and output the value. So $\Phi^{G \oplus Z}_e \neq C$, for every $e$.
:::

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

Items 2 and 3 show that typical sets in the sense of category compute no DNC function and are not computably dominated. In the sense of measure the situation is different: in the course on algorithmic randomness, almost every set in the sense of measure is shown to compute a DNC function.

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

## Notes and references

1-generic sets were introduced by Jockusch (1980), who proved most of their basic properties. The theorem that 1-generic sets are not DNC is due to Demuth and Kučera (1987). The meagerness of the high sets and of the computably dominated sets is classical; Downey and Hirschfeldt's book presents these results in the setting of algorithmic randomness.

- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- O. Demuth and A. Kučera, *Remarks on 1-genericity, semigenericity and related concepts*, Commentationes Mathematicae Universitatis Carolinae 28 (1987), 85–94.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010.
