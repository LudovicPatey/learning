---
title: Possible degree spectra
summary: Structures coding countable families of sets, whose spectra are the sets of oracles that can enumerate the family; every enumeration cone and every upper cone is a spectrum; the Slaman–Wehner structure, with no computable copy but a copy computable in every non-computable set; the non-Δ⁰₂ degrees (Kalimullin) and the non-arithmetic degrees (Harrison-Trainor, 2025) are spectra, while the non-Δ⁰ₙ degrees for n ≥ 3 are not.
duration: 35
prerequisites: [generic-presentations, fundamentals/fixed-point]
---

Which sets of Turing degrees are degree spectra? This lesson builds spectra. A single device does most of the work: a structure that codes a countable family of sets has as spectrum the set of oracles that can list the family. With it we obtain all upper cones and enumeration cones. We also obtain the theorem of Slaman and Wehner: a structure can be presentable in every non-computable degree without being computably presentable. The last section describes where the question stands.

## Structures coding families of sets

:::definition{#def-enumerate-family}
Let $\mathcal S$ be a countable family of subsets of $\nat$. A set $X$ **enumerates** $\mathcal S$ if there is a set $W$, c.e. in $X$, such that $\mathcal S = \{ W^{[n]} : n \in \nat \}$, where $W^{[n]} = \{ m : \langle n, m \rangle \in W \}$ is the $n$-th column. Columns may repeat.
:::

To code a family into a structure, use three sorts: numbers, names of sets, and membership facts. Let $\tau$ consist of unary relations $N$, $S$, $C$, a binary relation $E$ and constants $c_0, c_1, \ldots$.

:::definition{#def-family-structure}
Let $\mathcal S$ be a non-empty countable family. The structure $\mathcal A_{\mathcal S}$ has three disjoint sorts:
- $N$, consisting of the constants $c_n$ for $n \in \nat$;
- $S$, consisting of elements $s_{Y, i}$ for $Y \in \mathcal S$ and $i \in \nat$, so that each set is named infinitely often;
- $C$, consisting of elements $e_{Y, i, n}$ for $Y \in \mathcal S$, $i \in \nat$ and $n \in Y$.

The relation $E$ holds between $e_{Y, i, n}$ and $s_{Y, i}$, and between $e_{Y, i, n}$ and $c_n$, symmetrically, and nowhere else.
:::

So $n \in Y$ is witnessed by an element of $C$ joining $c_n$ to a name of $Y$. Each name $s$ of a set determines its **content** $\{ n : \exists e \in C\, (E(e, s) \wedge E(e, c_n)) \}$.

:::proposition{#prop-family-spectrum}
For every set $X$: $X$ computes a copy of $\mathcal A_{\mathcal S}$ if and only if $X$ enumerates $\mathcal S$.
:::

:::proof{of=prop-family-spectrum}
($\Rightarrow$) Let $\mathcal B$ be a copy computable in $X$. Its sort $S$ is an infinite set computable in $X$; list it as $b_0 < b_1 < \cdots$. Let $W$ be the set of pairs $\langle k, n \rangle$ such that some element $e$ of $C$ satisfies $E(e, b_k)$ and $E(e, c_n)$. It is c.e. in $X$, since the constants and relations of $\mathcal B$ are computable in $X$. Its $k$-th column is the content of $b_k$, which is the set named by $b_k$. Every set of $\mathcal S$ is named, so the columns of $W$ are exactly the sets of $\mathcal S$.

($\Leftarrow$) Let $W$ be c.e. in $X$ with columns forming $\mathcal S$, and fix an $X$-computable enumeration of $W$. Build a copy by stages, computably in $X$, deciding all relations on an element when it is created. At stage $s$, create the constant $c_s$, and a name $s_{k, i}$ for the pair $(k, i)$ with $\langle k, i \rangle = s$; the name $s_{k, i}$ is meant to name the column $W^{[k]}$. Then, for each pair $\langle k, n \rangle$ enumerated into $W$ by stage $s$ and each name $s_{k, i}$ already created, if no element of $C$ joins them yet, create one joined to $s_{k, i}$ and $c_n$. Each element is created with its sort and its $E$-relations, and these never change afterwards, so the copy is computable in $X$. The content of $s_{k, i}$ is $W^{[k]}$. Every column, hence every set of $\mathcal S$, has infinitely many names. So the structure is isomorphic to $\mathcal A_{\mathcal S}$. We use the elements in order of creation as $0, 1, 2, \ldots$, so that the domain is $\nat$.
:::

:::corollary{#cor-cones-spectra}
Every enumeration cone $\{ X : Y \text{ is c.e. in } X \}$ is a degree spectrum, and so is every upper cone $\{ X : Y \leq_T X \}$.
:::

:::proof{of=cor-cones-spectra}
A set $X$ enumerates the family $\{ Y \}$ if and only if $Y$ is c.e. in $X$: if $W$ is c.e. in $X$ and every column is $Y$, then $Y = W^{[0]}$ is c.e. in $X$, and conversely $W = \nat \times Y$ works. So $\mathcal A_{\{ Y \}}$ has enumeration degree $Y$. For upper cones, use $Y \oplus \overline Y$, which is c.e. in $X$ if and only if $Y \leq_T X$.
:::

The structures $\mathcal A_{\mathcal S}$ use infinitely many constants. A structure in a finite vocabulary does the same work: replace each constant $c_n$ by an element attached to a chain of length $n$. Graphs work too (Montalbán, Observation V.25).

## The Slaman–Wehner theorem

:::theorem[Slaman; Wehner]{#thm-slaman-wehner}
There is a structure whose degree spectrum is the set of non-computable sets.
:::

Write $F \oplus \{ n \} = \{ 2m : m \in F \} \cup \{ 2n + 1 \}$. The structure is $\mathcal A_{\mathcal F}$ for the family
$$
\mathcal F = \{ F \oplus \{ n \} : n \in \nat,\ F \subseteq \nat \text{ finite},\ F \neq W_n \}.
$$
By :ref{#prop-family-spectrum}, it suffices to show that a set enumerates $\mathcal F$ if and only if it is not computable.

**Intuition.** The family "knows" for each $n$ a finite set different from $W_n$. A computable listing of the family would give a computable way to find, from $n$, a c.e. set different from $W_n$, which the recursion theorem forbids. A non-computable oracle can list the family. It proposes all finite sets $F$. Whenever a proposed set looks equal to $W_n$, it adds a new element taken from $X \oplus \overline X$. If this happened infinitely often, $W_n$ would differ from $X \oplus \overline X$ by finitely many elements, and $X$ would be computable.

:::proof{of=thm-slaman-wehner}
*No computable set enumerates $\mathcal F$.* Suppose $W$ is c.e. with columns forming $\mathcal F$. Every member of $\mathcal F$ contains exactly one odd number. Given $n$, enumerate $W$ until some pair $\langle k, 2n + 1 \rangle$ appears. Such a pair exists, because $\emptyset \oplus \{ n \}$ or $\{ 0 \} \oplus \{ n \}$ is in $\mathcal F$: at least one of $\emptyset$ and $\{ 0 \}$ differs from $W_n$. The column $W^{[k]}$ is then $F \oplus \{ n \}$ for a finite set $F \neq W_n$. By the s-m-n theorem, there is a total computable function $h$ with $W_{h(n)} = \{ m : \langle k, 2m \rangle \in W \} = F$, where $k$ is the first column found for $n$. Then $W_{h(n)} \neq W_n$ for every $n$. This contradicts the fixed point theorem (:ref{#thm-fixed-point}), which gives $n$ with $\Phi_n = \Phi_{h(n)}$, hence $W_n = W_{h(n)}$, the sets $W_e$ being the domains of the functions $\Phi_e$.

*Every non-computable set enumerates $\mathcal F$.* Let $X$ be non-computable and $Y = X \oplus \overline X$, which is not c.e. Fix $n$. We enumerate, uniformly in $n$ and computably in $X$, the family $\mathcal F_n = \{ F : F \text{ finite},\ F \neq W_n \}$, as the family of sets $R_{F, s}$ for finite $F$ and $s \in \nat$. Each $R_{F, s}$ is the union of an increasing sequence $R_{F, s}[t]$. Let $R_{F, s}[t] = F$ for $t \leq s$. At stage $t + 1 > s$, if $R_{F, s}[t] = W_n[t]$, call it a *threat*, and let $R_{F, s}[t + 1]$ be $R_{F, s}[t]$ together with the least element of $Y$ not in it. Otherwise $R_{F, s}[t + 1] = R_{F, s}[t]$.

*Each $R_{F, s}$ belongs to $\mathcal F_n$.* Suppose there were infinitely many threats. Then $R_{F, s}$ would be infinite, equal to $F \cup Y$, since the elements of $Y$ are added in increasing order. At each threat stage, $R_{F, s}[t] = W_n[t] \subseteq W_n$, so $R_{F, s} \subseteq W_n$. Every element of $W_n$ is in $W_n[t]$ for large $t$, and at the next threat stage this equals $R_{F, s}[t] \subseteq R_{F, s}$; so $W_n \subseteq R_{F, s}$. Then $W_n = F \cup Y$, and $Y$ would be c.e., as a finite modification of a c.e. set. So there are finitely many threats, and $R_{F, s}$ is finite. If $R_{F, s} = W_n$, then for all large $t$, $W_n[t] = W_n = R_{F, s} = R_{F, s}[t]$, a threat, and a new element would be added. So $R_{F, s} \neq W_n$.

*Each member of $\mathcal F_n$ is some $R_{F, s}$.* Let $F$ be finite with $F \neq W_n$. If $W_n[t] = F$ for infinitely many $t$, then, the approximation being increasing, $W_n[t] = F$ for all large $t$, and $W_n = F$, which is excluded. So there is $s$ with $W_n[t] \neq F$ for all $t > s$. For this $s$, there is never a threat, and $R_{F, s} = F$.

The sets $R_{F, s}$ are enumerated uniformly in $(n, F, s)$, computably in $X$. Listing the sets $R_{F, s} \oplus \{ n \}$ for all triples $(n, F, s)$ is an enumeration of $\mathcal F$ computable in $X$.
:::

:::quiz[the Slaman–Wehner construction]
Why does the construction add elements of $X \oplus \overline X$, and not of $X$?

- [x] The argument needs a set that is not c.e. If there were infinitely many threats, $W_n$ would be a finite modification of the added set, hence that set would be c.e. A non-computable $X$ may be c.e., but $X \oplus \overline X$ is never c.e. when $X$ is not computable.
- [ ] Because $X$ might be finite.

  A finite set is computable and excluded by hypothesis; the issue is that a non-computable set may still be c.e.
- [ ] To make the sets $R_{F, s}$ finite.

  Finiteness follows from the finiteness of the number of threats, which is what the choice of the added set guarantees.

---

In the first part, where is it used that every member of $\mathcal F$ contains exactly one odd number?

- [x] To read off $n$ and $F$ from a column containing $2n + 1$: the column is then $F \oplus \{ n \}$ with $F \neq W_n$, and the even part gives a c.e. index for $F$.
- [ ] To show that $\mathcal F$ is non-empty.

  Non-emptiness comes from $\emptyset$ or $\{ 0 \}$ being different from $W_n$.
- [ ] To show that the columns are finite.

  Finiteness of the columns plays no role in the first part.
:::

The structure $\mathcal A_{\mathcal F}$ has no Turing degree and no enumeration degree. If its spectrum were the enumeration cone of $Y$, then $Y$ would be c.e. in every non-computable set. The next exercise shows that $Y$ would then be c.e. So the cone would contain $\emptyset$, which is computable.

::::exercise{#ex-sw-no-degree difficulty=2 objective="Use generic sets to show that a set c.e. in every non-computable set is c.e." lessons="cohen-genericity/one-genericity"}
Show that a set $Y$ that is c.e. in every non-computable set is c.e. Deduce that the Slaman–Wehner structure has no enumeration degree.

:::solution
Let $G$ be 1-generic relative to $Y$ (:ref{#def-relative-genericity}). It is not computable, so $Y$ is c.e. in $G$, say $Y = W_e^G$. Let $Q$ be the set of strings $\sigma$ such that some $n \in W_e^\sigma$ satisfies $n \notin Y$. It is c.e. in $Y$, so some prefix $\tau$ of $G$ either belongs to $Q$ or has no extension in $Q$. No prefix of $G$ belongs to $Q$, since $W_e^G = Y$. So $\tau$ has no extension in $Q$, and
$$
Y = \{ n : \text{some string } \sigma \succeq \tau \text{ satisfies } n \in W_e^\sigma \}.
$$
Indeed, an element of $Y$ is enumerated along a long enough prefix of $G$, which extends $\tau$; conversely, an extension of $\tau$ enumerating some $n \notin Y$ would belong to $Q$. The right-hand side is c.e., so $Y$ is c.e. If the Slaman–Wehner structure had enumeration degree $Y$, then $Y$ would be c.e. in every non-computable set, hence c.e., and every set, $\emptyset$ included, would be in the spectrum. This contradicts :ref{#thm-slaman-wehner}.
:::
::::

## What is known

The Slaman–Wehner theorem opened the study of spectra of the form "all degrees except a small class". The results are as follows; the proofs use the true-stage method or, for the last two, the theory of later courses.
- **Non-$\Delta^0_2$ degrees** (Kalimullin, 2008). There is a structure whose spectrum is the set of non-$\Delta^0_2$ degrees. Montalbán gave a variant of the Slaman–Wehner family that proves it (Exercise VII.22 of his book).
- **Non-$\Delta^0_n$ degrees, $n \geq 3$** (Andrews, Cai, Kalimullin, Lempp, Miller, Montalbán, 2016). For $n \geq 3$, the set of non-$\Delta^0_n$ degrees is not a spectrum.
- **Non-hyperarithmetic degrees** (Greenberg, Montalbán, Slaman). There is a structure, in fact a linear order, with no hyperarithmetic copy but with a copy computable in every non-hyperarithmetic set.
- **Non-arithmetic degrees** (Harrison-Trainor, preprint, 2025). There is a structure with no arithmetic copy but with a copy computable in every non-arithmetic set: the non-arithmetic degrees form a spectrum. This had been an open question for some time, stated as open in Montalbán's book. The proof introduces *unfriendly jump inversions*: an $n$-th unfriendly jump inversion of a structure behaves like an $n$-th jump inversion for isomorphism types, but like a $2n$-th jump inversion for presentations.

The question of which upward-closed sets of degrees are spectra remains open. The next lesson gives the known necessary conditions.

## Notes and references

The coding of families follows Montalbán, *Within the Arithmetic*, Section V.4 (Definition V.24, Observation V.25, Exercise V.27, Theorem V.26), whose proof of the Slaman–Wehner theorem we follow. Here the threats add the least element of $X \oplus \overline X$ outside the current set, and the limit set, in case of infinitely many threats, is $F \cup (X \oplus \overline X)$. The theorem is due independently to Slaman and to Wehner (1998). Kalimullin's paper is in Russian (Matematicheskii Sbornik). The status of the non-arithmetic case was checked in November 2026 against Harrison-Trainor's preprint, which is not yet refereed.

- T. A. Slaman, *Relative to any nonrecursive set*, Proceedings of the AMS 126 (1998), 2117–2122.
- S. Wehner, *Enumerations, countable structures and Turing degrees*, Proceedings of the AMS 126 (1998), 2131–2139.
- I. Sh. Kalimullin, *Almost computably enumerable families of sets*, Matematicheskii Sbornik 199(10) (2008), 33–40.
- U. Andrews, M. Cai, I. Kalimullin, S. Lempp, J. S. Miller and A. Montalbán, *The complements of lower cones of degrees and the degree spectra of structures*, Journal of Symbolic Logic 81 (2016), doi:10.1017/jsl.2015.59.
- N. Greenberg, A. Montalbán and T. A. Slaman, *Relative to any non-hyperarithmetic set*, Journal of Mathematical Logic, doi:10.1142/S0219061312500079.
- M. Harrison-Trainor, *Unfriendly jump inversions* (first circulated as *Relative to any non-arithmetic set*), arXiv:2505.23613, 2025.
- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Section V.4.

:::::exercises
::::exercise{#ex-family-union difficulty=1 objective="Compute the spectrum of a structure coding a family with two members."}
Let $Y_0$ and $Y_1$ be sets. Show that the spectrum of $\mathcal A_{\{ Y_0, Y_1 \}}$ is the intersection of the enumeration cones of $Y_0$ and of $Y_1$.

:::solution
By :ref{#prop-family-spectrum}, the spectrum is the set of $X$ that enumerate $\{ Y_0, Y_1 \}$. If $W$ is c.e. in $X$ with columns $Y_0$ and $Y_1$, each column is c.e. in $X$, so $X$ is in both cones. Conversely, if $Y_0$ and $Y_1$ are c.e. in $X$, the set $W$ whose even columns are $Y_0$ and odd columns $Y_1$ is c.e. in $X$ and enumerates the family.
:::
::::

::::exercise{#ex-family-noncomputable-member difficulty=1 objective="See why the Slaman–Wehner family lists all finite sets different from W_n, rather than one chosen set."}
For each $n$, let $F_n$ be $\emptyset$ if $W_n \neq \emptyset$, and $\{ 0 \}$ otherwise, so that $F_n \neq W_n$. Show that the family $\{ F_n \oplus \{ n \} : n \in \nat \}$ is enumerated by $\emptyset'$, and that no computable set enumerates it. Why does the construction of :ref{#thm-slaman-wehner} use all finite sets different from $W_n$, and not only $F_n$?

:::solution
Whether $W_n$ is empty is decided by $\emptyset'$, so $\emptyset'$ computes $n \mapsto F_n$, and the set of pairs $\langle n, m \rangle$ with $m \in F_n \oplus \{ n \}$ is computable in $\emptyset'$; it enumerates the family. A computable enumeration is impossible by the first part of the proof of :ref{#thm-slaman-wehner}, which applies to every family containing, for each $n$, at least one set $F \oplus \{ n \}$ with $F$ finite and $F \neq W_n$, and only such sets: it would give a computable function $h$ with $W_{h(n)} \neq W_n$ for all $n$. A non-computable oracle below $\emptyset'$ cannot in general decide whether $W_n$ is empty, so it cannot compute $F_n$. It does not know which finite sets differ from $W_n$, so it lists all finite sets and corrects a listed set when it threatens to equal $W_n$; the corrections stop because the oracle is not computable.
:::
::::

::::exercise{#ex-spectrum-join difficulty=2 objective="Combine two coded families to realize the intersection of two spectra." lessons="generic-presentations"}
Let $\mathcal S$ and $\mathcal T$ be countable families. Show that the intersection of the spectra of $\mathcal A_{\mathcal S}$ and $\mathcal A_{\mathcal T}$ is a spectrum. Deduce that the set of non-computable sets that compute a given set $Y$ is a degree spectrum.

:::solution
For a set $Z$, let $Z + 2 = \{ m + 2 : m \in Z \}$, and code the members of $\mathcal S$ and of $\mathcal T$ by
$$
c_0(Z) = \{ 0 \} \cup (Z + 2), \qquad c_1(Z) = \{ 1 \} \cup (Z + 2).
$$
Let $\mathcal U = \{ c_0(Z) : Z \in \mathcal S \} \cup \{ c_1(Z) : Z \in \mathcal T \}$. Each member of $\mathcal U$ contains exactly one of $0$ and $1$, which tells from which family it comes. By :ref{#prop-family-spectrum}, it suffices to show that $X$ enumerates $\mathcal U$ if and only if it enumerates $\mathcal S$ and $\mathcal T$.

If $W$ and $V$ are c.e. in $X$ and enumerate $\mathcal S$ and $\mathcal T$, the set whose $2k$-th column is $c_0(W^{[k]})$ and whose $(2k+1)$-th column is $c_1(V^{[k]})$ is c.e. in $X$ and enumerates $\mathcal U$.

Conversely, let $U$ be c.e. in $X$ and enumerate $\mathcal U$. The set $K_0$ of $k$ such that $0 \in U^{[k]}$ is c.e. in $X$, and non-empty because $\mathcal S$ is non-empty. So there is a total function $f \leq_T X$ whose range is $K_0$. The set whose $j$-th column is $\{ m : m + 2 \in U^{[f(j)]} \}$ is c.e. in $X$, and its columns are exactly the members of $\mathcal S$. The same argument with $1$ gives $\mathcal T$.

For the second statement, the set of non-computable sets that compute $Y$ is the intersection of the spectrum of :ref{#thm-slaman-wehner} with the upper cone of $Y$, the spectrum of $\mathcal A_{\{ Y \oplus \overline Y \}}$ (:ref{#cor-cones-spectra}). Both are spectra of structures of the form $\mathcal A_{\mathcal S}$.
:::
::::
:::::
