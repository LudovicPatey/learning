---
title: Quasi-minimal degrees
summary: The enumeration degree of a 1-generic set is quasi-minimal, nonzero and bounding no nonzero total degree, so the enumeration degrees properly extend the Turing degrees (Medvedev); the proof forces disjointness of two enumerations; no minimal degrees (Gutteridge) and embeddings of partial orders below every nonzero degree (stated).
duration: 20
prerequisites: [selman-theorem]
---

Are all enumeration degrees total, that is, images of Turing degrees? Medvedev showed in 1955 that they are not, in a strong form: some nonzero enumeration degree bounds no nonzero total degree. Such a degree is called quasi-minimal. This lesson proves that the enumeration degree of every 1-generic set is quasi-minimal. The proof is a forcing argument with Cohen conditions, in which an enumeration operator can only see the positive part of a condition. The lesson ends with the main structural differences between the enumeration degrees and the Turing degrees: there are no minimal enumeration degrees, and every countable partial order embeds below every nonzero degree.

## Quasi-minimality

:::definition{#def-quasi-minimal}
A nonzero enumeration degree $\mathbf a$ is **quasi-minimal** if the only total degree below $\mathbf a$ is $\mathbf 0_e$.
:::

A quasi-minimal degree is not total, since it would be a nonzero total degree below itself. So the existence of quasi-minimal degrees implies that the total degrees, the image of the Turing degrees, are a proper part of $\mathcal D_e$.

For a binary string $\sigma$, let $P_\sigma = \{ x < |\sigma| : \sigma(x) = 1 \}$ be its **positive part**. If $\sigma$ is a prefix of $G$, then $P_\sigma \subseteq G$. An enumeration operator applied to $G$ only uses finite subsets of $G$, hence positive parts of prefixes: $\Gamma(G) = \bigcup_{\sigma \prec G} \Gamma(P_\sigma)$. Recall that $G$ is 1-generic if for every c.e. set of strings $S$, some prefix of $G$ either belongs to $S$ or has no extension in $S$ (:ref{#def-1-generic}).

:::theorem[Medvedev]{#thm-generic-quasi-minimal}
If $G$ is 1-generic, then $\deg_e(G)$ is quasi-minimal.
:::

**Intuition.** Suppose that a total set $T$ is enumeration reducible to $G$. Then $T$ and its complement are both enumerated from $G$, by operators $\Gamma$ and $\Gamma'$. Genericity provides a prefix $\sigma$ of $G$ beyond which no extension makes $\Gamma$ and $\Gamma'$ enumerate a common number: otherwise $G$ itself would make them overlap. Beyond $\sigma$, whatever $\Gamma$ enumerates from any extension is correct, because an extension and $G$ can be merged into a single extension, which positive information cannot distinguish. So $T$ is enumerated by searching through all extensions of $\sigma$, a c.e. procedure.

:::proof{of=thm-generic-quasi-minimal}
By :ref{#prop-1-generic}, $G$ is not c.e., so $\deg_e(G) \neq \mathbf 0_e$.

Let $T$ be a total set with $T \leq_e G$; we show that $T$ is computable, so that $\deg_e(T) = \mathbf 0_e$. Since $\overline T \leq_e T$, composition gives operators $\Gamma$ and $\Gamma'$ with $T = \Gamma(G)$ and $\overline T = \Gamma'(G)$. Let
$$
S = \{ \sigma : \Gamma(P_\sigma) \cap \Gamma'(P_\sigma) \neq \emptyset \},
$$
a c.e. set of strings. No prefix of $G$ is in $S$, since $\Gamma(P_\sigma) \cap \Gamma'(P_\sigma) \subseteq T \cap \overline T = \emptyset$ for $\sigma \prec G$. By 1-genericity, some prefix $\sigma \prec G$ has no extension in $S$. We claim that
$$
T = \{ n : n \in \Gamma(P_\tau) \text{ for some } \tau \supseteq \sigma \},
$$
which shows that $T$ is c.e.; the same argument with $\Gamma'$ shows that $\overline T$ is c.e., and $T$ is computable.

If $n \in T = \Gamma(G)$, then $n \in \Gamma(P_\tau)$ for a long enough prefix $\tau$ of $G$, which extends $\sigma$. Conversely, let $\tau \supseteq \sigma$ with $n \in \Gamma(P_\tau)$, and suppose that $n \notin T$. Then $n \in \overline T = \Gamma'(G)$, so $n \in \Gamma'(E)$ for a finite set $E \subseteq G$. Let $\rho$ be the string of length $\max(|\tau|, \max E + 1)$ that agrees with $\sigma$ on $|\sigma|$ and takes the value $1$ at every other position. It extends $\sigma$. Its positive part contains $P_\tau$: the positions below $|\sigma|$ where $\tau$ is $1$ are those where $\sigma$ is $1$, and all other positions are $1$ in $\rho$. It contains $E$: an element of $E$ below $|\sigma|$ is in $G$, so $\sigma$, a prefix of $G$, is $1$ there. By monotonicity, $n \in \Gamma(P_\rho) \cap \Gamma'(P_\rho)$, so $\rho \in S$, an extension of $\sigma$ in $S$: a contradiction. So $n \in T$.
:::

The argument uses a special feature of enumeration operators: making a condition larger, by changing $0$s into $1$s outside the part fixed by $\sigma$, can only enlarge what they enumerate. Turing functionals do not have this property: they may use the $0$s of a condition, and the argument has no analogue for $G \oplus \overline G$, which is total.

:::quiz[the quasi-minimality of 1-generic sets]
In the proof, why is the string $\rho$ allowed to be $1$ at every position beyond $\sigma$?

- [x] It only needs to extend $\sigma$ and to have a positive part containing $P_\tau$ and $E$; enumeration operators are monotone, so adding elements to the positive part keeps $n$ in both outputs.
- [ ] Because $G$ is $1$ at these positions.

  $G$ may be $0$ at many of them; $\rho$ is not a prefix of $G$, only an extension of $\sigma$.
- [ ] Because $\rho$ must be a prefix of $G$.

  If $\rho$ were a prefix of $G$, the contradiction would be immediate; the point is that $\rho$ need not be.

---

Where is it used that $T$ is total?

- [x] To get an operator $\Gamma'$ enumerating the complement of $T$ from $G$, which makes the overlap of the two outputs a forbidden event that genericity can avoid.
- [ ] To show that $\deg_e(G)$ is nonzero.

  That uses only that $G$ is not c.e.
- [ ] To show that the set $S$ is c.e.

  $S$ is c.e. for any two operators.
:::

So the image of the Turing degrees is a proper part of the enumeration degrees, and there are nonzero degrees whose only total lower bound is $\mathbf 0_e$. By :ref{#prop-1-generic}, there is a 1-generic set computable in $\emptyset'$; its enumeration degree is a quasi-minimal degree below $\mathbf 0'_e$, since $G \leq_e G \oplus \overline G \leq_e \overline K$ when $G \leq_T K$.

## The structure of the enumeration degrees

Two classical results show how differently the enumeration degrees behave from the Turing degrees, where minimal degrees exist (course on the structure of the Turing degrees).

:::theorem[Gutteridge]{#thm-gutteridge}
There is no minimal enumeration degree: every nonzero enumeration degree bounds a strictly smaller nonzero degree.
:::

We admit the theorem (Gutteridge, 1971). Slaman and Sorbi (2014) strengthened it: every countable partial order embeds below every nonzero enumeration degree. Cooper (1990) showed on the other hand that the enumeration degrees are not dense, and Kent, Lewis-Pye and Sorbi (2012) that there are **strong minimal covers**: degrees $\mathbf a < \mathbf b$ such that every degree below $\mathbf b$ is below $\mathbf a$. These results already decide the existential theory of $\mathcal D_e$: it is decidable, since every finite partial order embeds (Soskova's survey, Section 2).

::::exercise{#ex-generic-total-cover difficulty=1 objective="Locate a 1-generic set and its complement with respect to the image of its Turing degree."}
Let $G$ be 1-generic. Show that $\deg_e(G) < \iota(\deg_T(G))$, and that $\deg_e(G)$ and $\deg_e(\overline G)$ are incomparable. (The complement of a 1-generic set is 1-generic, :ref{#ex-complement-generic}.)

:::solution
$G \leq_e G \oplus \overline G$. If the converse held, $\deg_e(G)$ would bound the total degree $\iota(\deg_T(G))$, which is nonzero since $G$ is not computable, contradicting :ref{#thm-generic-quasi-minimal}. If $G \leq_e \overline G$, then $G \oplus \overline G \leq_e \overline G$, and $\deg_e(\overline G)$, which is quasi-minimal since $\overline G$ is 1-generic, would bound a nonzero total degree. Symmetrically $\overline G \not\leq_e G$.
:::
::::

## Notes and references

Medvedev (1955) proved the existence of quasi-minimal enumeration degrees, in the language of partial degrees; the proof through 1-generic sets is now standard. :ref{#thm-gutteridge} is from Gutteridge's thesis (1971). The embedding results are Lagemann (1972), Bianchini (2000), Soskov and Soskova (2012) and Slaman and Sorbi (2014), as described in Soskova's survey, Section 2.1.

- Yu. T. Medvedev, *Degrees of difficulty of the mass problem*, Doklady Akademii Nauk SSSR 104 (1955), 501–504.
- L. Gutteridge, *Some Results on Enumeration Reducibility*, PhD thesis, Simon Fraser University, 1971.
- T. A. Slaman and A. Sorbi, *A note on initial segments of the enumeration degrees*, Journal of Symbolic Logic 79 (2014), 633–643.
- M. I. Soskova, *The theory of the enumeration degrees, definability, and automorphisms*, College Publications, 2020, Sections 1–2.

:::::exercises
::::exercise{#ex-complement-generic difficulty=1 objective="Apply quasi-minimality to the complement of a generic set and to the pair it forms with the set."}
Let $G$ be 1-generic. Show that $\overline G$ is 1-generic, that $\deg_e(\overline G)$ is quasi-minimal, and that $\deg_e(G) \vee \deg_e(\overline G)$ is total.

:::solution
The map exchanging $0$ and $1$ in strings is a computable bijection of strings preserving extension; if $S$ is c.e., so is its image $\overline S$, and a prefix of $G$ meets or avoids $\overline S$ exactly when the corresponding prefix of $\overline G$ meets or avoids $S$. So $\overline G$ is 1-generic, and its degree is quasi-minimal by :ref{#thm-generic-quasi-minimal}. The join is the degree of $G \oplus \overline G$, which is total. So two quasi-minimal degrees can join to a total degree.
:::
::::

::::exercise{#ex-quasi-minimal-not-total-below difficulty=2 objective="Distinguish quasi-minimality from minimality using Gutteridge's theorem."}
Let $\mathbf a$ be quasi-minimal. Using :ref{#thm-gutteridge}, show that there is a nonzero degree $\mathbf b < \mathbf a$, and that every such $\mathbf b$ is quasi-minimal.

:::solution
By :ref{#thm-gutteridge}, $\mathbf a$ bounds a nonzero degree $\mathbf b < \mathbf a$. A total degree below $\mathbf b$ is below $\mathbf a$, hence equal to $\mathbf 0_e$; so $\mathbf b$, which is nonzero, is quasi-minimal.
:::
::::
:::::
