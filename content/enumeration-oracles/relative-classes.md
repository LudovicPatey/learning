---
title: Relativizing to an enumeration oracle
summary: Σ⁰₁ and Π⁰₁ classes relative to an enumeration oracle; for total oracles they are the usual relativized classes; genericity relative to an enumeration oracle, and strong quasi-minimal covers above every enumeration degree.
duration: 20
prerequisites: [enumeration-definability/continuous-degrees]
---

To relativize a notion of computability to a Turing oracle $X$, one replaces "c.e." by "c.e. in $X$". To relativize it to an enumeration oracle $A$, one replaces "c.e." by "enumeration reducible to $A$". By Selman's theorem, this amounts to relativizing to all the Turing oracles that enumerate $A$ at once. The method gives a systematic way to extend relations between Turing degrees to the enumeration degrees, and to locate the degrees on which the extension behaves as in the Turing case. This lesson defines the relativized $\Pi^0_1$ classes and the relativized generic sets, and uses the latter to show that every enumeration degree has a cover of a special kind.

We write $\langle A \rangle$ when a set $A$ is used as an enumeration oracle.

## Classes relative to an enumeration oracle

For a string $\sigma$, $[\sigma]$ is the class of infinite binary sequences extending $\sigma$, and for a set $W$ of strings, $[W] = \bigcup_{\sigma \in W} [\sigma]$.

:::definition[Miller, Soskova]{#def-relative-pi01}
A class $\mathcal U \subseteq 2^\nat$ is a **$\Sigma^0_1\langle A \rangle$ class** if $\mathcal U = [W]$ for some set of strings $W \leq_e A$. A class is a **$\Pi^0_1\langle A \rangle$ class** if its complement is a $\Sigma^0_1\langle A \rangle$ class.
:::

The members of a $\Pi^0_1\langle A \rangle$ class are total objects, sequences of bits; only the description of the class is restricted to positive information about $A$.

:::proposition{#prop-relative-classes-total}
1. For a set $X$, the $\Pi^0_1\langle X \oplus \overline X \rangle$ classes are the $\Pi^0_1(X)$ classes.
2. If $A \leq_e B$, every $\Pi^0_1\langle A \rangle$ class is a $\Pi^0_1\langle B \rangle$ class.
3. For every set $X$, the singleton $\{ X \}$ is a $\Pi^0_1\langle X \oplus \overline X \rangle$ class.
:::

:::proof{of=prop-relative-classes-total}
1. By :ref{#prop-ce-in-e}, the sets of strings enumeration reducible to $X \oplus \overline X$ are those c.e. in $X$, and a $\Pi^0_1(X)$ class is the complement of $[W]$ for a set of strings $W$ c.e. in $X$. 2 follows from transitivity. 3. The complement of $\{ X \}$ is $[W]$ for the set $W$ of strings incompatible with $X$; a string $\sigma$ is incompatible with $X$ if and only if $\sigma(n) = 1$ and $n \notin X$, or $\sigma(n) = 0$ and $n \in X$, for some $n < |\sigma|$, which is enumerated from $X \oplus \overline X$.
:::

## Genericity relative to an enumeration oracle

:::definition{#def-relative-generic}
A set $G$ is **$\langle A \rangle$-generic** if for every set of strings $W \leq_e A$, some prefix of $G$ is in $W$ or has no extension in $W$.
:::

There are countably many sets of strings enumeration reducible to $A$, so $\langle A \rangle$-generic sets exist, by the finite extension method: meet or avoid each of them in turn. For a total oracle $X \oplus \overline X$, this is 1-genericity relative to $X$.

:::definition{#def-strong-quasi-minimal-cover}
A degree $\mathbf b$ is a **strong quasi-minimal cover** of $\mathbf a$ if $\mathbf a < \mathbf b$ and every total degree below $\mathbf b$ is below $\mathbf a$.
:::

:::theorem{#thm-strong-qm-cover}
Let $A$ be a set and $G$ an $\langle A \rangle$-generic set. Then $\deg_e(A \oplus G)$ is a strong quasi-minimal cover of $\deg_e(A)$. In particular, every enumeration degree has a strong quasi-minimal cover.
:::

The proof is that of :ref{#thm-generic-quasi-minimal}, relativized to the enumeration oracle $\langle A \rangle$. For a string $\sigma$, $P_\sigma$ is its positive part.

:::proof{of=thm-strong-qm-cover}
*$G \not\leq_e A$.* If $G = \Gamma(A)$, let $W$ be the set of strings $\sigma$ such that $\sigma(n) = 0$ for some $n \in \Gamma(A)$. Then $W \leq_e A$. No prefix of $G$ is in $W$, since $\Gamma(A) = G$. A prefix $\sigma$ of $G$ with no extension in $W$ is impossible: $G$ is infinite (it meets the set of strings with a $1$ beyond any given length, which is computable), so some $n \geq |\sigma|$ is in $\Gamma(A)$, and $\sigma$ extended by $0$ at $n$ is in $W$. So $A <_e A \oplus G$.

*Total degrees below.* Let $T$ be total with $T \leq_e A \oplus G$. As in :ref{#thm-generic-quasi-minimal}, there are operators with $T = \Gamma(A \oplus G)$ and $\overline T = \Gamma'(A \oplus G)$. Let
$$
S = \{ \sigma : \Gamma(A \oplus P_\sigma) \cap \Gamma'(A \oplus P_\sigma) \neq \emptyset \},
$$
which is enumeration reducible to $A$: the condition only asks for finitely many elements of $A$ and of $P_\sigma$. No prefix of $G$ is in $S$, since $T \cap \overline T = \emptyset$. By genericity, a prefix $\sigma$ of $G$ has no extension in $S$. Then
$$
T = \{ n : n \in \Gamma(A \oplus P_\tau) \text{ for some } \tau \supseteq \sigma \},
$$
by the argument of :ref{#thm-generic-quasi-minimal}: a wrong $\tau$ would merge with a finite part of $G$ into an extension of $\sigma$ in $S$. So $T \leq_e A$, and similarly $\overline T \leq_e A$. Every total degree below $\deg_e(A \oplus G)$ is below $\deg_e(A)$.
:::

:::quiz[strong quasi-minimal covers]
In the proof of :ref{#thm-strong-qm-cover}, why is the set $S$ enumeration reducible to $A$, and not only c.e. in $A$?

- [x] Membership of $\sigma$ in $S$ is witnessed by finitely many axioms using finitely many elements of $A$ and of the finite set $P_\sigma$: positive information about $A$ only.
- [ ] Because $S$ is c.e.

  $S$ depends on $A$; what matters is that it only uses positive information about $A$.
- [ ] Because $T$ is total.

  Totality of $T$ gives the operator $\Gamma'$; the complexity of $S$ comes from the form of its definition.

---

Why does the theorem need genericity relative to $\langle A \rangle$, and not plain 1-genericity?

- [x] The forcing argument must meet or avoid the set $S$, which depends on $A$; a 1-generic set only handles c.e. sets of strings.
- [ ] Because a 1-generic set is enumeration reducible to $A$.

  A 1-generic set may or may not be; the point is which sets of strings it decides.
- [ ] To make $A \oplus G$ total.

  The cover $A \oplus G$ is in general not total; it bounds only the total degrees below $\mathbf a$.
:::

For $A = \emptyset$, the theorem is the quasi-minimality of 1-generic sets. For a total oracle $X \oplus \overline X$, it gives, above every Turing degree, an enumeration degree whose total predecessors are exactly those of the Turing degree. The method of relativizing to $\langle A \rangle$ is the basis of the next lesson, on the relation "PA relative to".

::::exercise{#ex-relative-generic-total difficulty=1 objective="Recognize relative genericity for total oracles."}
Let $X$ be a set. Show that a set $G$ is $\langle X \oplus \overline X \rangle$-generic if and only if it is 1-generic relative to $X$.

:::solution
By :ref{#prop-ce-in-e}, the sets of strings enumeration reducible to $X \oplus \overline X$ are exactly the sets of strings c.e. in $X$. So the two definitions quantify over the same sets of strings and impose the same condition.
:::
::::

## Notes and references

$\Pi^0_1\langle A \rangle$ classes were introduced by Miller and Soskova, and the systematic relativization to enumeration oracles is developed by Goh, Kalimullin, Miller and Soskova, who observe :ref{#thm-strong-qm-cover} as the relativization of the quasi-minimality of 1-generic sets.

- J. L. Goh, I. Sh. Kalimullin, J. S. Miller and M. I. Soskova, *PA relative to an enumeration oracle*, Journal of Symbolic Logic, published online 2022, doi:10.1017/jsl.2022.55, Sections 1–2.

:::::exercises
::::exercise{#ex-relative-pi01-monotone difficulty=1 objective="Compare relative Π⁰₁ classes along enumeration reducibility."}
Show that if $A$ is c.e., the $\Pi^0_1\langle A \rangle$ classes are exactly the $\Pi^0_1$ classes.

:::solution
If $A$ is c.e., the sets of strings enumeration reducible to $A$ are the c.e. sets of strings, so the $\Sigma^0_1\langle A \rangle$ classes are the $\Sigma^0_1$ classes, and their complements are the $\Pi^0_1$ classes.
:::
::::

::::exercise{#ex-relative-generic-exist difficulty=1 objective="Build relative generic sets by finite extensions."}
Show that for every set $A$ there is an $\langle A \rangle$-generic set.

:::solution
List the sets of strings $W_0, W_1, \ldots$ enumeration reducible to $A$; there are countably many. Build strings $\sigma_0 \subseteq \sigma_1 \subseteq \cdots$: given $\sigma_e$, let $\sigma_{e+1}$ be an extension of $\sigma_e$ in $W_e$ if there is one, and $\sigma_{e+1} = \sigma_e 0$ otherwise. Then $G = \bigcup_e \sigma_e$ meets $W_e$ or has the prefix $\sigma_e$ with no extension in $W_e$.
:::
::::

::::exercise{#ex-strong-cover-not-total difficulty=1 objective="See that a strong quasi-minimal cover is never total."}
Let $G$ be $\langle A \rangle$-generic. Show that $\deg_e(A \oplus G)$ is not total.

:::solution
If it were total, it would be a total degree below itself, hence below $\deg_e(A)$ by :ref{#thm-strong-qm-cover}; but $A <_e A \oplus G$.
:::
::::

:::::
