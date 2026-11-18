---
title: Degree spectra that are not possible
summary: No degree spectrum is a countable union of enumeration cones unless it is one of them (Knight and others); 2-generic presentations; a structure with c.e. existential types has a copy computing no member of any Π⁰₁ class without computable members (Andrews, Miller); a spectrum that is the upward closure of an F_σ set is an enumeration cone, so the PA, DNC and Martin-Löf random degrees are not spectra; low structures and the open low₅ problem for Boolean algebras.
duration: 45
prerequisites: [possible-spectra, pi01-classes/pa-degrees]
---

The previous lesson built spectra; this one rules some out. The method is the same throughout. Take a copy generic enough that whatever it computes, it computes for a structural reason. Then show that the shape of the spectrum forces a structural reason that is incompatible with the shape. The results answer natural questions: can a spectrum be the union of two cones, or the set of PA degrees? Both answers are negative.

## Unions of cones

:::theorem[Knight and others]{#thm-no-two-cones}
Let $Y_0, Y_1, \ldots$ be sets, and suppose that
$$
\mathrm{DgSp}(\mathcal A) = \bigcup_{n} \{ Z : Y_n \text{ is c.e. in } Z \}.
$$
Then $\mathrm{DgSp}(\mathcal A) = \{ Z : Y_n \text{ is c.e. in } Z \}$ for some $n$.
:::

:::proof{of=thm-no-two-cones}
Let $X = \bigoplus_n Y_n$, and let $\mathcal B$ be an $X$-generic presentation of $\mathcal A$ (:ref{#lem-generic-exists}). Since $D(\mathcal B)$ is in the spectrum, $Y_n$ is c.e. in $D(\mathcal B)$ for some $n$. As $Y_n \leq_T X$, the enumeration defining $\mathcal B$ is $Y_n$-generic, so $Y_n$ is c.e.-coded by $\mathcal A$ (:ref{#lem-generic-ce}). Then every set in the spectrum computes a copy, in which $Y_n$ is c.e., so the spectrum is contained in the enumeration cone of $Y_n$. The reverse inclusion is a hypothesis.
:::

Taking $Y_n \oplus \overline{Y_n}$ for $Y_n$ gives the same statement for upper cones. So a spectrum is never the union of finitely or countably many upper cones, unless it is one of them.

::::exercise{#ex-two-cones difficulty=1 objective="Apply the theorem on unions of cones to two incomparable degrees."}
Let $Y_0$ and $Y_1$ be Turing incomparable. Show that $\{ Z : Y_0 \leq_T Z \text{ or } Y_1 \leq_T Z \}$ is not a degree spectrum.

:::solution
Suppose it is the spectrum of $\mathcal A$. It is the union of the enumeration cones of $Y_0 \oplus \overline{Y_0}$ and $Y_1 \oplus \overline{Y_1}$, so by :ref{#thm-no-two-cones} it equals one of them, say the upper cone of $Y_0$. Then $Y_1$, which belongs to the union, belongs to the upper cone of $Y_0$: $Y_0 \leq_T Y_1$, a contradiction.
:::
::::

## Second-order genericity

The next results need copies that decide sets of tuples of one more quantifier.

:::definition{#def-2-generic-enumeration}
Let $X \subseteq \nat$. A relation $R \subseteq A^\star$ is **relatively intrinsically $\Sigma^0_2$ in $X$** if its image $R^{\mathcal C}$ is $\Sigma^0_2$ in $D(\mathcal C) \oplus X$ for every copy $(\mathcal C, R^{\mathcal C})$ of $(\mathcal A, R)$. An injective function $g : \nat \to A$ is a **2-generic enumeration of $\mathcal A$ relative to $X$** if every such $R$ is decided by an initial segment of $g$.
:::

As in :ref{#lem-generic-exists}, such an enumeration exists, onto $A$, and is computable in $(D(\mathcal A) \oplus X)''$. A 2-generic enumeration relative to $X$ is in particular $X$-generic, since every $X$-r.i.c.e. relation is relatively intrinsically $\Sigma^0_2$ in $X$.

Fix a Turing functional $\Phi$ that, given an oracle and a number $n$, outputs a string of length $n$; for a finite string $\sigma$, $\Phi^\sigma(n)$ is the computation with oracle $\sigma$ bounded by $|\sigma|$ steps. Let $T \subseteq \nat^{<\nat}$ be a tree. For an injective enumeration $g$ of $\mathcal A$ with pull-back $\mathcal B$, suppose that $\Phi^{D(\mathcal B)}$ is a path through $T$, that is, $\Phi^{D(\mathcal B)}(n) \in T$ has length $n$ and $\Phi^{D(\mathcal B)}(n) \preceq \Phi^{D(\mathcal B)}(n + 1)$ for every $n$. Consider the sets of tuples that would make this fail:
- $Q_0$, the tuples $\bar q \in A^\star$ such that $\Phi^{D_{\mathcal A}(\bar q)}(n)$ converges, for some $n$, to a string not in $T$;
- $Q_1$, the tuples $\bar q$ such that $\Phi^{D_{\mathcal A}(\bar q)}(n)$ and $\Phi^{D_{\mathcal A}(\bar q)}(n + 1)$ converge, for some $n$, to strings with the first not a prefix of the second;
- $Q_2$, the tuples $\bar p$ such that, for some $n$, no $\bar q \in A^\star$ extending $\bar p$ makes $\Phi^{D_{\mathcal A}(\bar q)}(n)$ converge.

The sets $Q_0$ and $Q_1$ are $T$-r.i.c.e., and $Q_2$ is relatively intrinsically $\Sigma^0_2$: in a copy, it is defined by an existential quantifier over $n$ followed by a universal quantifier over tuples, with a matrix computable in the diagram.

:::lemma{#lem-forcing-path}
Let $g$ be a 2-generic enumeration of $\mathcal A$ relative to $T$, onto $A$, with pull-back $\mathcal B$, and suppose that $\Phi^{D(\mathcal B)}$ is a path through $T$. Then there is an initial segment $\bar b$ of $g$ such that, for every tuple $\bar q \in A^\star$ extending $\bar b$ and every $n$:
1. if $\Phi^{D_{\mathcal A}(\bar q)}(n)$ converges, its value is in $T$;
2. if $\Phi^{D_{\mathcal A}(\bar q)}(n)$ and $\Phi^{D_{\mathcal A}(\bar q)}(n+1)$ converge, the first is a prefix of the second;
3. some extension $\bar q'' \in A^\star$ of $\bar q$ makes $\Phi^{D_{\mathcal A}(\bar q'')}(n)$ converge.
:::

:::proof{of=lem-forcing-path}
Each $Q_i$ is decided by an initial segment of $g$. No initial segment $g \uh k$ belongs to $Q_0$ or $Q_1$, since a convergent computation with oracle $D_{\mathcal A}(g \uh k)$, a part of $D(\mathcal B)$, is a computation of $\Phi^{D(\mathcal B)}$. No initial segment belongs to $Q_2$, since $\Phi^{D(\mathcal B)}(n)$ converges with oracle $D_{\mathcal A}(g \uh m)$ for some $m$, which can be taken beyond $k$. So for each $i$ there is an initial segment of $g$ with no extension in $Q_i$. The longest of the three is $\bar b$, and its extensions satisfy the three properties.
:::

## Π⁰₁ classes in the copies

:::theorem[Andrews, Miller]{#thm-andrews-miller}
Let $\mathcal A$ have c.e. existential types. Then $\mathcal A$ has a copy $\mathcal B$ such that, for every $\Pi^0_1$ class $\mathcal P \subseteq \nat^\nat$ without computable members, $D(\mathcal B)$ computes no member of $\mathcal P$.
:::

**Intuition.** If a generic copy computes a path through a computable tree, a finite piece $\bar b$ of the copy forces the computation to behave well (:ref{#lem-forcing-path}). The existential type of $\bar b$ then describes which values the computation can take. It is c.e., so the values can be searched for computably, and the search builds a computable path.

:::proof{of=thm-andrews-miller}
Let $\mathcal B$ be the pull-back of a 2-generic enumeration $g$ of $\mathcal A$, onto $A$. Suppose that $\Phi^{D(\mathcal B)}$ is a path through a computable tree $T$. A computable tree is decided by $\emptyset$, so $g$ is 2-generic relative to $T$. Let $\bar b$ be given by :ref{#lem-forcing-path}. We build a computable path $\sigma_0 \preceq \sigma_1 \preceq \cdots$ through $T$.

Let $\sigma_0$ be the empty string. Given $\sigma_n$, search for a finite atomic diagram $\delta$ of a tuple of length $|\bar b| + j$, and for a string $\sigma$, such that:
- the existential formula "there is a tuple $\bar x$ of length $j$, without repetitions and disjoint from $\bar b$, such that $\bar b \bar x$ has atomic diagram $\delta$" belongs to $\exists\text{-}\mathrm{tp}_{\mathcal A}(\bar b)$;
- $\Phi^\delta(n + 1)$ converges to $\sigma$, and $\sigma_n \preceq \sigma$.

Let $\sigma_{n+1}$ be the first $\sigma$ found. The search is computable, since the existential type of $\bar b$ is c.e.

*The search succeeds.* We show by induction that each $\sigma_n$ is the value $\Phi^{D_{\mathcal A}(\bar b \bar a)}(n)$ for some tuple $\bar a$ with $\bar b \bar a \in A^\star$. For $n = 0$, take $\bar a$ empty. Given such $\bar a$ for $\sigma_n$, property 3 gives an extension $\bar b \bar a'$ with $\Phi^{D_{\mathcal A}(\bar b \bar a')}(n + 1)$ convergent. The computation at $n$ still converges with the larger oracle, to $\sigma_n$, and by property 2 it is a prefix of the value at $n + 1$. So $\delta = D_{\mathcal A}(\bar b \bar a')$ is a candidate, and the search finds some candidate.

*The result is a path.* Every candidate $\delta$ is the diagram of an actual tuple $\bar b \bar x$ of $\mathcal A$, so by property 1 the value $\sigma_{n+1} = \Phi^\delta(n+1)$ is in $T$. It has length $n + 1$ and extends $\sigma_n$. So $\bigcup_n \sigma_n$ is a computable path through $T$.

Hence, if $\mathcal P = [T]$ has no computable member, $D(\mathcal B)$ computes no member of $\mathcal P$.
:::

:::quiz[the theorem of Andrews and Miller]
Where is the hypothesis that the existential types of $\mathcal A$ are c.e. used?

- [x] To make the search for $\sigma_{n+1}$ computable: the possible values of the computation beyond $\bar b$ are those $\Phi^\delta$ for which $\delta$ is realized over $\bar b$, a property listed in the existential type of $\bar b$.
- [ ] To build the 2-generic enumeration.

  Generic enumerations exist for every structure; they are built with the double jump of its diagram.
- [ ] To show that the values found lie in $T$.

  This is property 1 of :ref{#lem-forcing-path}, which comes from genericity; the existential type only certifies that the diagram $\delta$ is realized.

---

Why is genericity of the second order needed, and not only $T$-genericity?

- [x] The set $Q_2$, of tuples beyond which the computation diverges at some $n$, involves a universal quantifier over extensions; it is not r.i.c.e., and avoiding it is what guarantees that the search succeeds.
- [ ] Because $T$ is not computable.

  $T$ is computable here; the point is the quantifier complexity of $Q_2$, not the tree.
- [ ] To make the copy $\mathcal B$ computable in $\emptyset''$.

  The complexity of $\mathcal B$ plays no role in the conclusion.
:::

:::corollary[Andrews, Miller]{#cor-andrews-miller}
A structure with c.e. existential types, for instance a linear order, has a copy that computes no PA set, no DNC function, and no Martin-Löf random set.
:::

:::proof{of=cor-andrews-miller}
The $\{0, 1\}$-valued DNC functions, of PA degree (:ref{#def-pa-degree}), and the DNC functions form $\Pi^0_1$ classes without computable members. The Martin-Löf random sets form the union of the complements of the levels of a universal Martin-Löf test, each a $\Pi^0_1$ class without computable members. Apply :ref{#thm-andrews-miller}.
:::

## Upward closures of F_σ sets

A subset of $\nat^\nat$ is **$F_\sigma$** if it is a countable union of closed sets $[T_i]$, for arbitrary trees $T_i \subseteq \nat^{<\nat}$. The **Turing upward closure** of $\mathcal F \subseteq \nat^\nat$ is the set of $Z$ that compute a member of $\mathcal F$.

:::theorem[Andrews, Miller; Montalbán]{#thm-fsigma-spectra}
If the degree spectrum of $\mathcal A$ is the Turing upward closure of an $F_\sigma$ set, then $\mathcal A$ has an enumeration degree.
:::

:::proof{of=thm-fsigma-spectra}
Let the spectrum be the upward closure of $\bigcup_i [T_i]$, and let $\mathcal B$ be the pull-back of a 2-generic enumeration of $\mathcal A$ relative to $\bigoplus_i T_i$. Since $D(\mathcal B)$ is in the spectrum, there are $i$ and a functional $\Phi$ such that $\Phi^{D(\mathcal B)}$ is a path through $T_i$. Let $\bar b$ be given by :ref{#lem-forcing-path} for $T = T_i$, and let
$$
S = \{ \sigma : \sigma \preceq \Phi^{D_{\mathcal A}(\bar q)}(n) \text{ for some } n \text{ and some } \bar q \in A^\star \text{ extending } \bar b \}.
$$
The set $S$ is c.e.-coded by $\mathcal A$: in a copy $\mathcal C$, knowing the image of $\bar b$, enumerate the values of the computations along the tuples extending it. By property 1, $S \subseteq T_i$. It is a tree, closed under prefixes by definition, and it has no dead ends. Indeed, if $\sigma \preceq \Phi^{D_{\mathcal A}(\bar q)}(n)$, then by properties 3 and 2 some extension $\bar q'$ gives a value at $n + 1$ that strictly extends the value at $n$.

We claim that $\mathcal A$ has enumeration degree $S$. If $Z$ computes a copy, $S$ is c.e. in $Z$, since $S$ is c.e.-coded. Conversely, if $S$ is c.e. in $Z$, then $Z$ computes a path through $S$: starting from the empty string, search in the enumeration of $S$ for a one-element extension of the current string, which exists because $S$ has no dead ends. This path belongs to $[S] \subseteq [T_i]$, so $Z$ is in the upward closure, which is the spectrum.
:::

The theorem has a short consequence for the classes of degrees met in the course on $\Pi^0_1$ classes.

:::corollary[Andrews, Miller]{#cor-pa-not-spectrum}
The PA degrees, the DNC degrees and the Martin-Löf random degrees are not degree spectra.
:::

:::proof{of=cor-pa-not-spectrum}
Each of these sets of degrees is the upward closure of an $F_\sigma$ set: a $\Pi^0_1$ class for the first two, a countable union of $\Pi^0_1$ classes for the third. If one of them were a spectrum, it would be an enumeration cone $\{ Z : Y \text{ is c.e. in } Z \}$ by :ref{#thm-fsigma-spectra}. Then $Y$ would be c.e. in every member of a non-empty $\Pi^0_1$ class without computable members. Andrews and Miller proved that such a set $Y$ is c.e. (their Proposition 3.6, which we admit). Then the cone would contain the computable sets, which are neither PA, nor DNC, nor random.
:::

The F_σ theorem cannot be improved to say that the spectrum is an upper cone. Miller and Soskova showed that the enumeration cone of a non-total continuous degree is the upward closure of a closed set. McCarthy characterized the enumeration degrees whose cones are upward closures of closed sets: they are exactly the cototal degrees, studied in the track on enumeration degrees.

## Low structures

A structure is **low** if it has a copy of low degree. The question whether low structures have computable copies, the *low property*, depends on the class.
- **Boolean algebras.** Downey and Jockusch (1994) proved that every low Boolean algebra has a computable copy; Thurber extended this to low₂ (1995), and Knight and Stob to low₃ and low₄ (2000). Whether every low₅ Boolean algebra has a computable copy is open. Harris and Montalbán's analysis of the back-and-forth types of Boolean algebras shows that the next step is, in a precise sense, harder than the solved cases.
- **Linear orders.** Jockusch and Soare (1991) built a low linear order without a computable copy. The combinatorial core of their proof is a game in which one player copies a linear order built by the other, who can force a difference by choosing between $\omega$ and $m + \omega^*$ (Montalbán, Section X.6).

The low property matters for spectra. In a class with the low property, the spectrum of a structure is determined by the spectrum of its jump, a structure that adds the complete r.i.c.e. relation (Montalbán, Chapters IX and X).

## Notes and references

:ref{#thm-no-two-cones} is due to Knight and her students in the 1990s, here with Montalbán's proof (Theorem V.15). :ref{#thm-andrews-miller}, :ref{#cor-andrews-miller} and :ref{#cor-pa-not-spectrum} are from Andrews and Miller (2015), and the F_σ theorem :ref{#thm-fsigma-spectra} is Montalbán's generalization of their ideas (*Within the Arithmetic*, Section V.3, Theorems V.18 and V.20, Corollary V.22). We define 2-generic enumerations by sets that are relatively intrinsically $\Sigma^0_2$. Montalbán defines them as generic enumerations of the structure expanded by its complete r.i.c.e. relation, which comes to the same for the sets needed here. The status of the low₅ problem for Boolean algebras was checked in November 2026: it is still stated as open in recent papers.

- A. Montalbán, *Computable Structure Theory: Within the Arithmetic*, Sections V.3 and X.4–X.6.
- U. Andrews and J. S. Miller, *Spectra of theories and structures*, Proceedings of the AMS 143 (2015), 1283–1298.
- E. McCarthy, *Cototal enumeration degrees and the Turing degree spectra of minimal subshifts*, Proceedings of the AMS, doi:10.1090/proc/13783.
- R. Downey and C. G. Jockusch, *Every low Boolean algebra is isomorphic to a recursive one*, Proceedings of the AMS 122 (1994), 871–880.
- J. J. Thurber, *Every low₂ Boolean algebra has a recursive copy*, Proceedings of the AMS 123 (1995), 3859–3866.
- J. F. Knight and M. Stob, *Computable Boolean algebras*, Journal of Symbolic Logic 65 (2000), 1605–1623.
- K. Harris and A. Montalbán, *On the n-back-and-forth types of Boolean algebras*, Transactions of the AMS 364 (2012), 827–866.
- C. G. Jockusch and R. I. Soare, *Degrees of orderings not isomorphic to recursive linear orderings*, Annals of Pure and Applied Logic 52 (1991), 39–64.

:::::exercises
::::exercise{#ex-countable-upward-closure difficulty=1 objective="Recover the theorem on unions of upper cones from the F_σ theorem."}
Show that a countable subset of $\nat^\nat$ is $F_\sigma$. Deduce from :ref{#thm-fsigma-spectra} that if a spectrum is a countable union of upper cones, then the structure has an enumeration degree.

:::solution
A singleton $\{ f \}$ is closed: it is $[T]$ for the tree $T$ of prefixes of $f$. A countable set is a countable union of singletons, hence $F_\sigma$. The union of the upper cones of countably many sets $Y_n$ is the Turing upward closure of the countable set $\{ Y_n : n \in \nat \}$, so :ref{#thm-fsigma-spectra} applies.
:::
::::

::::exercise{#ex-no-pa-spectrum-contained difficulty=1 objective="Combine the theorem of Andrews and Miller with Richter's example of linear orders."}
Show that the spectrum of a linear order is never contained in the set of PA degrees.

:::solution
Linear orders have c.e. existential types (:ref{#ex-linear-orders-ce-types}). By :ref{#cor-andrews-miller}, a linear order $\mathcal L$ has a copy $\mathcal B$ that computes no PA set. The diagram of $\mathcal B$ is in the spectrum of $\mathcal L$, and it is not of PA degree.
:::
::::

::::exercise{#ex-spectrum-tree-c.e.-coded difficulty=2 objective="Check the step of the F_σ theorem that produces a tree without dead ends."}
In the proof of :ref{#thm-fsigma-spectra}, show in detail that if $\sigma \in S$, then $\sigma$ has a proper extension in $S$, using the three properties of :ref{#lem-forcing-path}.

:::solution
Let $\sigma \preceq \Phi^{D_{\mathcal A}(\bar q)}(n) = \rho$ with $\bar q$ extending $\bar b$; $\rho$ has length $n$. By property 3, applied to $\bar q$ and $n + 1$, there is an extension $\bar q'$ of $\bar q$ with $\Phi^{D_{\mathcal A}(\bar q')}(n + 1)$ convergent, to a string $\rho'$ of length $n + 1$. The computation $\Phi^{D_{\mathcal A}(\bar q)}(n)$ converges within $|\bar q|$ steps using only $D_{\mathcal A}(\bar q)$, which is part of $D_{\mathcal A}(\bar q')$, so $\Phi^{D_{\mathcal A}(\bar q')}(n) = \rho$. By property 2, $\rho \preceq \rho'$. So $\rho'$ is in $S$, and it properly extends $\sigma$, since $|\rho'| = n + 1 > n \geq |\sigma|$.
:::
::::
:::::
