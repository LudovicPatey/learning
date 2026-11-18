---
title: PA relative to an enumeration oracle
summary: The relation "⟨B⟩ is PA relative to ⟨A⟩" extends PA relative to a Turing oracle; total degrees are PA bounded; codable sets and the continuous degrees; no continuous degree is PA relative to itself, while self-PA degrees exist (Miller, Soskova); the continuous degrees are exactly the PA bounded degrees (Goh, Kalimullin, Miller, Soskova); universal classes, low for PA degrees and open questions.
duration: 20
prerequisites: [relative-classes, pi01-classes/basis-theorems]
---

A Turing oracle $B$ is PA relative to $X$ if $B$ computes a member of every nonempty $\Pi^0_1(X)$ class. Two properties of this relation are basic in the Turing degrees: if $B$ is PA relative to $X$, then $B$ computes $X$, since $\{ X \}$ is a $\Pi^0_1(X)$ class; and no set is PA relative to itself, by Kreisel's theorem relativized: the class of $\{0, 1\}$-valued functions that are diagonally noncomputable relative to $X$ has no $X$-computable member. Extending the relation to enumeration oracles, both properties can fail, and the degrees on which they hold turn out to be natural classes, among them the continuous degrees.

## The relation

:::definition[Goh, Kalimullin, Miller, Soskova]{#def-relative-pa}
$\langle B \rangle$ is **PA relative to** $\langle A \rangle$ if every nonempty $\Pi^0_1\langle A \rangle$ class contains a sequence $X$ with $X \oplus \overline X \leq_e B$. A set $A$ is **$\langle$self$\rangle$-PA** if $\langle A \rangle$ is PA relative to $\langle A \rangle$, and **PA bounded** if $A \leq_e B$ whenever $\langle B \rangle$ is PA relative to $\langle A \rangle$.
:::

Members of a class are total objects, so they are required to be enumerated together with their complements. The relation is invariant under enumeration equivalence of $A$ and of $B$, and, by :ref{#prop-relative-classes-total}, for total oracles it is the Turing relation: $\langle Y \oplus \overline Y \rangle$ is PA relative to $\langle X \oplus \overline X \rangle$ if and only if $Y$ is PA relative to $X$.

:::proposition{#prop-total-pa-bounded}
Every total set is PA bounded, and no total set is $\langle$self$\rangle$-PA.
:::

:::proof{of=prop-total-pa-bounded}
Let $A = X \oplus \overline X$ (every total set is enumeration equivalent to one). By :ref{#prop-relative-classes-total}, $\{ X \}$ is a nonempty $\Pi^0_1\langle A \rangle$ class; if $\langle B \rangle$ is PA relative to $\langle A \rangle$, then $X \oplus \overline X \leq_e B$, that is, $A \leq_e B$. If $A$ were $\langle$self$\rangle$-PA, then $X$ would be PA relative to $X$ in the Turing sense, contradicting Kreisel's theorem relativized to $X$.
:::

## Codable sets and the continuous degrees

:::definition{#def-codable}
A set $A$ is **codable** if there is a nonempty $\Pi^0_1\langle A \rangle$ class $\mathcal U$ and a uniform procedure that, given any member $X$ of $\mathcal U$, enumerates $A$ from $X$: $A$ is uniformly c.e. in the members of $\mathcal U$.
:::

A total set $X \oplus \overline X$ is codable, with the class $\{ X \}$. The following characterization of Andrews, Igusa, Miller and Soskova is admitted.

:::theorem[Andrews, Igusa, Miller, Soskova]{#thm-codable-continuous}
An enumeration degree is continuous if and only if it contains a codable set.
:::

:::proposition{#prop-continuous-not-self-pa}
No set of continuous degree is $\langle$self$\rangle$-PA.
:::

:::proof{of=prop-continuous-not-self-pa}
The relation is invariant under enumeration equivalence, so by :ref{#thm-codable-continuous} we may assume that $A$ is codable, with class $\mathcal U$. Suppose that $\langle A \rangle$ is PA relative to $\langle A \rangle$. Then some $X \in \mathcal U$ satisfies $X \oplus \overline X \leq_e A$. Since $A$ is c.e. in $X$, $A \leq_e X \oplus \overline X$ (:ref{#prop-ce-in-e}). So $A \equiv_e X \oplus \overline X$ is total, and $\langle X \oplus \overline X \rangle$ is PA relative to itself, which :ref{#prop-total-pa-bounded} excludes.
:::

So the continuous degrees, like the total ones, satisfy the analogue of Kreisel's theorem. This is not the case for all degrees.

:::theorem[Miller, Soskova]{#thm-self-pa}
There are $\langle$self$\rangle$-PA enumeration degrees. The total degrees below a $\langle$self$\rangle$-PA degree form a Scott set, every countable Scott set is the set of total degrees below some $\langle$self$\rangle$-PA degree, and for sets $X$ and $Y$, $X$ is PA relative to $Y$ if and only if $Y \oplus \overline Y <_e A <_e X \oplus \overline X$ for some $\langle$self$\rangle$-PA set $A$.
:::

We admit the theorem. It parallels Miller's theorem on the nontotal continuous degrees: the total degrees below a nontotal continuous degree form a Scott set, every countable Scott set arises in this way, and $X$ is PA relative to $Y$ if and only if a nontotal continuous degree lies strictly between the images of their degrees (:ref{#thm-nontotal-continuous} and the remarks after it). Goh, Kalimullin, Miller and Soskova proved that some $\langle$self$\rangle$-PA set is not of cototal degree, while every $\Sigma^0_2$ degree is cototal, so $\langle$self$\rangle$-PA degrees exist on both sides of cototality.

:::quiz[continuous degrees and self-PA]
In the proof of :ref{#prop-continuous-not-self-pa}, where is codability used?

- [x] To get $A \leq_e X \oplus \overline X$ for the member $X$ of the class that $A$ enumerates, which makes $A$ total and reduces the question to Kreisel's theorem.
- [ ] To show that the class $\mathcal U$ is nonempty.

  Nonemptiness is part of the definition; the uniform enumeration of $A$ from members of $\mathcal U$ is what is used.
- [ ] To show that the relation is invariant under enumeration equivalence.

  Invariance holds for all sets; codability is used once a member of the class is enumerated.
:::

## The classification

Ganchev, Kalimullin, Miller and Soskova proved that every PA bounded degree is cototal, and that the continuous degrees are exactly the degrees that are PA bounded and have a **universal class**: a nonempty $\Pi^0_1\langle A \rangle$ class $\mathcal P$ such that for every nonempty $\Pi^0_1\langle A \rangle$ class $\mathcal Q$, a single Turing functional maps every member of $\mathcal P$ to a member of $\mathcal Q$. Goh, Kalimullin, Miller and Soskova removed the second condition.

:::theorem[Goh, Kalimullin, Miller, Soskova]{#thm-pa-bounded-continuous}
An enumeration degree is PA bounded if and only if it is continuous.
:::

We admit the theorem. The same authors introduced the **low for PA** degrees, those $\mathbf a$ such that every nonempty $\Pi^0_1\langle A \rangle$ class has a nonempty $\Pi^0_1$ subclass, so that $\mathbf a$ adds nothing to PA computations; the degrees of 1-generic sets and the halves of nontrivial K-pairs are low for PA, and the low for PA degrees are disjoint from the continuous degrees, although both have universal classes. They compared all these classes with the classes of Kalimullin and Puzarenko, defined by properties of descriptive set theory (reduction, separation, extension), and showed that three of the latter are the analogues of their own, with $\Pi^0_1\langle A \rangle$ classes restricted to separating classes. The resulting picture of the relative positions of all these classes is complete; among the open questions they list is the exact role of uniformity in the definition of a universal class.

::::exercise{#ex-relative-pa-monotone difficulty=1 objective="Check the monotonicity of the relation PA relative to an enumeration oracle in both arguments."}
Show that if $\langle B \rangle$ is PA relative to $\langle A \rangle$, $A' \leq_e A$ and $B \leq_e B'$, then $\langle B' \rangle$ is PA relative to $\langle A' \rangle$.

:::solution
By :ref{#prop-relative-classes-total}, item 2, every $\Pi^0_1\langle A' \rangle$ class is a $\Pi^0_1\langle A \rangle$ class. If it is nonempty, it has a member $X$ with $X \oplus \overline X \leq_e B \leq_e B'$.
:::
::::

## Notes and references

:ref{#def-relative-pa}, :ref{#prop-total-pa-bounded}, :ref{#prop-continuous-not-self-pa} and :ref{#thm-pa-bounded-continuous} are from Goh, Kalimullin, Miller and Soskova (2022), who also recall :ref{#thm-self-pa} from unpublished work of Miller and Soskova, and the results of Ganchev, Kalimullin, Miller and Soskova. :ref{#thm-codable-continuous} is Andrews, Igusa, Miller and Soskova (2019).

- J. L. Goh, I. Sh. Kalimullin, J. S. Miller and M. I. Soskova, *PA relative to an enumeration oracle*, Journal of Symbolic Logic, published online 2022, doi:10.1017/jsl.2022.55.
- U. Andrews, G. Igusa, J. S. Miller and M. I. Soskova, *Characterizing the continuous degrees*, Israel Journal of Mathematics 234 (2019), 743–767.
- H. A. Ganchev, I. Sh. Kalimullin, J. S. Miller and M. I. Soskova, *A structural dichotomy in the enumeration degrees*, Journal of Symbolic Logic.
- I. Sh. Kalimullin and V. G. Puzarenko, *Computability principles on admissible sets*, Matematicheskie Trudy 7 (2004), 35–71.

:::::exercises
::::exercise{#ex-pa-bounded-scott difficulty=1 objective="Separate the self-PA degrees from the continuous and the PA bounded degrees."}
Show that no $\langle$self$\rangle$-PA degree is continuous, and deduce from :ref{#thm-pa-bounded-continuous} that no $\langle$self$\rangle$-PA set is PA bounded.

:::solution
The first statement is :ref{#prop-continuous-not-self-pa}. By :ref{#thm-pa-bounded-continuous}, the PA bounded degrees are the continuous ones, so a $\langle$self$\rangle$-PA set, which does not have continuous degree, is not PA bounded.
:::
::::

::::exercise{#ex-relative-pa-total difficulty=1 objective="Check that the relation extends PA relative to a Turing oracle."}
Show that $\langle Y \oplus \overline Y \rangle$ is PA relative to $\langle X \oplus \overline X \rangle$ if and only if $Y$ is PA relative to $X$.

:::solution
By :ref{#prop-relative-classes-total}, the $\Pi^0_1\langle X \oplus \overline X \rangle$ classes are the $\Pi^0_1(X)$ classes. For a member $Z$, $Z \oplus \overline Z \leq_e Y \oplus \overline Y$ if and only if $Z \leq_T Y$, by :ref{#prop-ce-in-e}. So both relations say that $Y$ computes a member of every nonempty $\Pi^0_1(X)$ class.
:::
::::

:::::
