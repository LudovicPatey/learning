---
title: The forcing relation
summary: The forcing relation of a notion of forcing; extension, consistency and density; forcing implies truth for generic sets; n-generic filters; forcing as density.
duration: 40
prerequisites: [generic-sets, arithmetic-hierarchy/post-theorem, cohen-genericity/one-genericity]
---

In the previous lesson each property of generic sets came from an ad hoc dense set. The **forcing relation** gives such dense sets for all arithmetic properties at once. A condition $c$ forces $\varphi$, written $c \Vdash \varphi$, if $c$ guarantees $\varphi$ for the set built, provided the construction continues generically. For formulas with one unbounded quantifier this can be required of all members of $c$; for more complex ones it cannot: no string has only infinite sets as members, yet every sufficiently generic Cohen set is infinite. So $c$ forces a universal statement if no extension of $c$ forces a counterexample. The theorem that forcing implies truth for generic sets justifies this choice.

## The forcing relation

Formulas, sentences and negations are those of :ref{#def-forcing-formula}.

:::definition{#def-forcing-relation}
Let $(\mathbb P, \leq, [\cdot])$ be a notion of forcing. The relation $c \Vdash \varphi$, read "$c$ **forces** $\varphi$", between conditions and sentences of level at least $1$ is defined by induction on the level.

1. If $\varphi$ is $\Sigma^0_1$ or $\Pi^0_1$, then $c \Vdash \varphi$ if every member of $c$ satisfies $\varphi$.
2. If $\varphi = \exists y\ \psi(y)$ is $\Sigma^0_{n+1}$, then $c \Vdash \varphi$ if $c \Vdash \psi(m)$ for some $m$.
3. If $\varphi = \forall y\ \psi(y)$ is $\Pi^0_{n+1}$, then $c \Vdash \varphi$ if there are no $d \leq c$ and $m$ with $d \Vdash \neg \psi(m)$.

A condition **decides** $\varphi$ if it forces $\varphi$ or $\neg \varphi$.
:::

At level $1$ this is the forcing of :ref{#prop-force-sigma1}: truth on all members. The existential clause asks for an explicit witness. Only the universal clause refers to extensions: however the construction continues below $c$, it never reaches a condition forcing a counterexample.

:::example{#ex-forcing-relation}
1. **Cohen forcing.** Every string $\sigma$ forces "$G$ is infinite", $\forall x\ \Phi^G_a(x)\converge$ in the notation of :ref{#ex-forcing-formulas}. Indeed $\tau \Vdash \Phi^G_a(m)\diverge$ would mean that no member of $\tau$ has an element above $m$, which fails for the member $\tau 1 1 \cdots$. But the finite set $\sigma 0 0 \cdots$ is a member of $\sigma$: forcing a $\Pi^0_2$ sentence does not make it true for all members.
2. **Jockusch–Soare forcing.** A class $\mathcal P$ forces "$\Phi^G_e$ is total" if and only if $\Phi^X_e$ is total for every $X \in \mathcal P$. If $\Phi^X_e(m)\diverge$ for some $X \in \mathcal P$, the non-empty $\Pi^0_1$ class $\mathcal P \cap \{ X : \Phi^X_e(m)\diverge \}$ is an extension forcing $\Phi^G_e(m)\diverge$. Conversely, an extension forcing $\Phi^G_e(m)\diverge$ has a member, which is a member of $\mathcal P$.
3. **Computable Sacks forcing.** Let $T$ be a computable f-tree, $L = \bigcup_k T(0^k)$ its leftmost path, and $\Phi_e$ the functional such that $\Phi^X_e(x)$ searches for $k$ with $X \uh |T(0^k)| \neq T(0^k)$. Then $\Phi^X_e$ is total if and only if $X \neq L$. No subtree $S$ of $T$ forces $\Phi^G_e(m)\diverge$, since $S$ has paths other than $L$; so $T$ forces "$\Phi^G_e$ is total", although $L$ is a member of $T$ for which it fails. Unlike Jockusch–Soare forcing, a computable perfect tree cannot remove a single path.
:::

:::proposition{#prop-forcing-basic}
Let $c$ be a condition and $\varphi$ a sentence of level $n \geq 1$.

1. (**Extension**) If $c \Vdash \varphi$ and $d \leq c$, then $d \Vdash \varphi$.
2. (**Consistency**) $c$ does not force both $\varphi$ and $\neg \varphi$.
3. If $\varphi$ is $\Sigma^0_n$ and no extension of $c$ forces $\varphi$, then $c \Vdash \neg \varphi$.
4. (**Density**) The set $D_\varphi$ of conditions that decide $\varphi$ is dense.
:::

:::proof{of=prop-forcing-basic}
1. By induction on $n$. At level $1$, $[d] \subseteq [c]$. If $c \Vdash \psi(m)$, then $d \Vdash \psi(m)$ by induction. If no extension of $c$ forces $\neg \psi(m)$, then neither does any extension of $d$, which is an extension of $c$.
2. At level $1$, a member of $c$ satisfies exactly one of $\varphi$ and $\neg \varphi$. At level $n + 1$, the two sentences are $\exists y\ \psi(y)$ and $\forall y\ \neg \psi(y)$. If $c \Vdash \psi(m)$, then $d = c$ forces $\neg \neg \psi(m) = \psi(m)$, so $c$ does not force $\forall y\ \neg \psi(y)$.
3. At level $1$, $\varphi$ is $\Phi^G_e(\vec m)\converge$. Suppose some member $X$ of $c$ satisfies $\varphi$, with use $u$. By refinement there is $d \leq c$ with $[d] \subseteq [X \uh u]$, and by the use principle (:ref{#thm-use-principle}) every member of $d$ satisfies $\varphi$; this contradicts the hypothesis. So every member satisfies $\neg \varphi$. At level $n + 1$, $\varphi = \exists y\ \psi(y)$. If some $d \leq c$ forced $\neg \neg \psi(m) = \psi(m)$, it would force $\varphi$. So $c \Vdash \forall y\ \neg \psi(y) = \neg \varphi$.
4. Since $D_\varphi = D_{\neg \varphi}$, we may assume that $\varphi$ is $\Sigma^0_n$. Given $c$, either some extension of $c$ forces $\varphi$, or $c$ forces $\neg \varphi$ by item 3.
:::

Item 3 fails for $\Pi^0_n$ sentences: a condition none of whose extensions forces a $\Pi^0_n$ sentence need not force its negation, which is existential and requires a witness (:ref{#exr-weak-forcing}).

:::quiz[the basic properties of forcing]
In item 3 of :ref{#prop-forcing-basic}, at level $1$, where is the refinement property of the notion of forcing used?

- [x] To pass from one member $X$ of $c$ on which the computation converges to an extension all of whose members extend $X \uh u$, and on which the computation therefore converges.
- [ ] To show that $c$ has a member.

  Conditions have members by definition.
- [ ] To show that the use $u$ exists.

  The use exists because the computation converges.

---

Why does consistency at level $n + 1$ follow from the case $d = c$ in the universal clause?

- [x] Because $\forall y\ \neg \psi(y)$ forbids every extension of $c$, including $c$ itself, from forcing $\psi(m)$; and $c \Vdash \exists y\ \psi(y)$ provides such an $m$.
- [ ] Because $c$ has no extensions.

  Every condition extends itself, and usually has many other extensions.
- [ ] By consistency at level $1$ applied to $\psi(m)$.

  The argument does not need the induction hypothesis.
:::

::::exercise{#ex-cohen-sigma2-witness difficulty=1 objective="See on an example that forcing a $\Sigma^0_2$ sentence requires an explicit witness."}
In Cohen forcing, let $\varphi$ be the $\Sigma^0_2$ sentence $\exists y\ \psi(y)$, where $\psi(y)$ is a $\Pi^0_1$ formula expressing "$G(0) = y$". Show that the empty string does not force $\varphi$, although every string of length $1$ does. Conclude that the set of conditions forcing a $\Sigma^0_2$ sentence may be dense below a condition that does not force it.

:::solution
The members of the empty string are all sets, and both values of $G(0)$ occur, so the empty string forces no $\psi(m)$, hence not $\varphi$. The string $i$ forces $\psi(i)$, since all its members have $G(0) = i$; so it forces $\varphi$. Every string has an extension of length at least $1$, so the set of conditions forcing $\varphi$ is dense below the empty string.
:::
::::

## Forcing and truth

A generic filter decides every sentence, and the decisions it makes are correct for the set it determines.

:::definition{#def-n-generic-notion}
Let $n \geq 1$. A filter is **$n$-generic** (for $\mathbb P$) if it meets the sets $S_k$ of :ref{#lem-generic-set} and the sets $D_\varphi$ for all sentences $\varphi$ of level at most $n$. A set is $n$-generic for $\mathbb P$ if it is $G_F$ for an $n$-generic filter $F$.
:::

There are countably many sentences, so by :ref{#lem-rasiowa-sikorski} every condition belongs to an $n$-generic filter, and to a filter that is $n$-generic for every $n$. For Cohen forcing, the next lesson shows that this notion coincides with the $n$-genericity of :ref{#def-relative-genericity}.

:::theorem[Forcing and truth]{#thm-forcing-truth}
Let $F$ be an $n$-generic filter and $\varphi$ a sentence of level $k \leq n$.

1. If some $c \in F$ forces $\varphi$, then $G_F \models \varphi$.
2. $G_F \models \varphi$ if and only if some $c \in F$ forces $\varphi$.
:::

:::proof{of=thm-forcing-truth}
1. By induction on $k$, for all sentences of level $k$ at once. At level $1$, $G_F$ is a member of $c$ by :ref{#lem-generic-set}, so it satisfies $\varphi$. If $\varphi = \exists y\ \psi(y)$, then $c \Vdash \psi(m)$ for some $m$, and $G_F \models \psi(m)$ by the induction hypothesis. Let $\varphi = \forall y\ \psi(y)$ and $m \in \nat$. The sentence $\psi(m)$ has level $k - 1 \leq n$, so $F$ contains a condition $d$ deciding it, and a common extension $e \in F$ of $c$ and $d$, which decides $\psi(m)$ by extension. It does not force $\neg \psi(m)$, since $e \leq c$ and $c \Vdash \varphi$. So $e \Vdash \psi(m)$, and $G_F \models \psi(m)$ by the induction hypothesis. Hence $G_F \models \varphi$.
2. One direction is item 1. Conversely, $F$ contains a condition $c$ deciding $\varphi$. If $c \Vdash \neg \varphi$, item 1 applied to $\neg \varphi$, of the same level, gives $G_F \models \neg \varphi$. So if $G_F \models \varphi$, then $c \Vdash \varphi$.
:::

Genericity is used only in the universal clause: no generic filter through a condition forcing $\forall y\ \psi(y)$ can choose a counterexample, since it would pass through a condition forcing it.

:::quiz[forcing and truth]
In the proof of :ref{#thm-forcing-truth}, why is the condition $e$ taken as a common extension of $c$ and $d$, rather than $d$ itself?

- [x] Because the hypothesis $c \Vdash \forall y\ \psi(y)$ only constrains extensions of $c$, and $d$ need not extend $c$.
- [ ] Because $d$ might not belong to $F$.

  $d$ is chosen in $F$; the point is its relation to $c$.
- [ ] Because $d$ might not decide $\psi(m)$.

  $d$ is chosen in $D_{\psi(m)}$, so it decides $\psi(m)$.

---

Which property of the generic set $G_F$ does the theorem give for a $2$-generic filter of Cohen forcing?

- [x] $G_F$ is infinite, since every string forces "$G$ is infinite", a $\Pi^0_2$ sentence.
- [ ] $G_F$ is finite.

  No string forces "$G$ is finite", since every string forces its negation.
- [ ] Nothing, since some members of every string are finite.

  The theorem concerns the generic set, not all members of a condition.
:::

Forcing can also be characterized by density, without reference to the syntax.

:::corollary{#cor-forcing-density}
Let $c$ be a condition and $\varphi$ a sentence of level $n$. The following are equivalent:

1. $G_F \models \varphi$ for every $n$-generic filter $F$ containing $c$;
2. the set of conditions forcing $\varphi$ is dense below $c$.
:::

:::proof{of=cor-forcing-density}
(2 ⇒ 1) Let $F$ be $n$-generic with $c \in F$. It contains a condition $d$ deciding $\varphi$, and a common extension $e$ of $c$ and $d$, which decides $\varphi$. If $e \Vdash \neg \varphi$, then by extension no extension of $e$ forces $\varphi$, contradicting the density below $c$. So $e \Vdash \varphi$, and $G_F \models \varphi$ by :ref{#thm-forcing-truth}.

(1 ⇒ 2) Let $d \leq c$. By density, some $e \leq d$ decides $\varphi$. If $e \Vdash \neg \varphi$, an $n$-generic filter containing $e$ contains $c$, since filters are closed upward, and its set satisfies $\neg \varphi$, contradicting 1. So $e \Vdash \varphi$.
:::

Condition 1 depends only on the class $\{ X : X \models \varphi \}$: two formulas of level $n$ defining the same class may be forced by different conditions, but are forced densely below the same conditions. In this sense the syntactic definition is harmless.

::::exercise{#exr-weak-forcing difficulty=2 objective="Compare the strong forcing relation with weak forcing, and locate where they differ."}
Say that $c$ **weakly forces** $\varphi$ if the set of conditions forcing $\varphi$ is dense below $c$. Show that forcing implies weak forcing, and that for a $\Pi^0_n$ sentence $\varphi$, $n \geq 1$, weak forcing implies forcing. Deduce, with :ref{#ex-cohen-sigma2-witness}, that item 3 of :ref{#prop-forcing-basic} fails for $\Pi^0_2$ sentences.

:::solution
If $c \Vdash \varphi$, every extension forces $\varphi$, so the set is dense below $c$.

Let $\varphi$ be $\Pi^0_n$ and suppose $c$ weakly forces it. For $n = 1$, let $\varphi = \Phi^G_e(\vec m)\diverge$, and suppose a member $X$ of $c$ has $\Phi^X_e(\vec m)\converge$ with use $u$. By refinement some $d \leq c$ has all its members extending $X \uh u$, so they all satisfy $\neg \varphi$; an extension of $d$ forcing $\varphi$ would have a member satisfying $\varphi$, in $[d]$. This is a contradiction, so $c \Vdash \varphi$. For $n \geq 2$, let $\varphi = \forall y\ \psi(y)$ and suppose $d \leq c$ forces $\neg \psi(m)$. Some $e \leq d$ forces $\varphi$; it also forces $\neg \psi(m)$ by extension, while $e \Vdash \varphi$ forbids $e$ itself from forcing $\neg \psi(m)$. So $c \Vdash \varphi$.

In :ref{#ex-cohen-sigma2-witness}, the $\Pi^0_2$ sentence $\neg \varphi$ is forced by no string: a non-empty string extends a string of length $1$, so it forces $\varphi$, and not $\neg \varphi$ by consistency; the empty string does not force $\neg \varphi$, since its extension $0$ forces $\psi(0) = \neg \neg \psi(0)$. But the empty string does not force $\neg \neg \varphi = \varphi$ either.
:::
::::

## Notes and references

The forcing relation for arithmetic is due to Feferman (1965), with atomic formulas $n \in G$ at the base and a negation clause; Downey and Hirschfeldt recall it for Cohen forcing (Section 2.24, footnote to Definition 2.24.1), and Dzhafarov and Mummert (Definition 7.4.1, Proposition 7.4.2, Theorem 7.4.6) treat arbitrary notions of forcing. The version used here, with truth on all members at level $1$, is the syntactic forcing relation of Monin and Patey (chapter *Effective forcing*, section *Forcing relation*), suited to conditions that are classes. It is a **strong forcing**; the weak forcing of :ref{#exr-weak-forcing} is the version common in set theory.

- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.24.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 7.4.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Forcing relation*.

:::::exercises
::::exercise{#ex-truth-needs-genericity difficulty=1 objective="See why genericity is needed in the theorem on forcing and truth."}
For Cohen forcing, let $F$ be the set of prefixes of the set $\emptyset$, that is, of the strings $0^k$. Show that $F$ is a filter meeting every $S_n$, that it contains a condition forcing the $\Pi^0_2$ sentence "$G$ is infinite" of :ref{#ex-forcing-formulas}, and that $G_F$ is finite. Find a $\Sigma^0_1$ sentence $\varphi$ such that $F$ does not meet $D_\varphi$.

:::solution
The strings $0^k$ are pairwise comparable, the set is closed upward ($\tau \preceq 0^k$ implies $\tau = 0^j$), and it contains $0^n \in S_n$. So $F$ is a filter meeting every $S_n$, and $G_F = \emptyset$, since $\emptyset$ is a member of every $0^k$. By :ref{#ex-forcing-relation}, item 1, every string, in particular the empty string, forces "$G$ is infinite". But $\emptyset$ is finite.

Let $\varphi$ be $\Phi^G_a(0)\converge$, with $\Phi_a$ the functional of :ref{#ex-forcing-formulas} that searches for an element above its input. A string forces $\varphi$ if and only if it has a $1$ at some position $y \geq 1$: otherwise its member $\sigma 0 0 \cdots$ has no element above $0$. No string forces $\neg \varphi$, since $\sigma 1 1 \cdots$ is a member with an element above $0$. So $D_\varphi$ is the set of strings with a $1$ at a position $y \geq 1$, which contains no $0^k$. The filter $F$ is not $1$-generic, and :ref{#thm-forcing-truth} does not apply to it.
:::
::::

::::exercise{#ex-sacks-totality-local difficulty=2 objective="See that for computable Sacks forcing, forcing totality is not a property of the nodes of the tree."}
Let $T$ be a computable f-tree and $\Phi_e$ a functional.

1. Show that if $T$ forces "$\Phi^G_e$ is total", then for every node $\sigma$ of $T$ and every $x$, some node $\tau \succeq \sigma$ of $T$ satisfies $\Phi^\tau_e(x)\converge$.
2. Let $T$ be the identity tree, and let $\Phi^X_e(x)$ search for an odd number $p$ with $X(p) = 1$, for every $x$. Show that the property of item 1 holds, but that $T$ does not force "$\Phi^G_e$ is total".

:::solution
1. Suppose that some node $\sigma = T(\rho)$ and some $x$ have no node $\tau \succeq \sigma$ of $T$ with $\Phi^\tau_e(x)\converge$. Let $S$ be the full subtree above $\sigma$. If a path $X$ of $S$ had $\Phi^X_e(x)\converge$ with use $u$, a node of $S$ that is a prefix of $X$ of length at least $u$, which exists since the nodes along a path have unbounded lengths, would make the computation converge; it is a node of $T$ extending $\sigma$. So every member of $S$ satisfies $\Phi^G_e(x)\diverge$, that is, $S \Vdash \Phi^G_e(x)\diverge$, and $T$ does not force totality, by the universal clause of :ref{#def-forcing-relation}.
2. Every string $\sigma$ is a node of $T$, and $\tau = \sigma 1 1$ has a $1$ at an odd position, $|\sigma|$ or $|\sigma| + 1$; so $\Phi^\tau_e(x)\converge$ for every $x$. Now let $R(\rho) = \hat\rho$, the string obtained by inserting a $0$ after each bit of $\rho$. It is a computable f-tree, as in :ref{#ex-tree-compatibility}, and a subtree of $T$. Its nodes are $0$ at every odd position, so its paths are $0$ at every odd position, and $\Phi^X_e(0)\diverge$ for every path $X$ of $R$. So $R \Vdash \Phi^G_e(0)\diverge$, with $R \leq T$, and $T$ does not force "$\Phi^G_e$ is total". In :ref{#ex-forcing-relation}, item 3, the subtrees could not avoid the leftmost path; here a subtree can avoid all the escape nodes at once.
:::
::::

::::exercise{#ex-infinite-four-notions difficulty=1 objective="Compute the conditions forcing a $\Pi^0_2$ sentence in each of the four notions of forcing."}
For each of Cohen, Jockusch–Soare, computable Sacks and computable Mathias forcing, determine which conditions force "$G$ is infinite", the sentence $\forall x\ \Phi^G_a(x)\converge$ of :ref{#ex-forcing-formulas}. In which of them can a condition force it while having a finite member?

:::solution
By the universal clause, $c$ forces the sentence if and only if no extension of $c$ forces $\Phi^G_a(m)\diverge$ for any $m$, that is, no extension has all its members contained in $\{0, \dots, m\}$.

- *Cohen.* Every string forces it (:ref{#ex-forcing-relation}, item 1), and every string has a finite member.
- *Jockusch–Soare.* By the argument of :ref{#ex-forcing-relation}, item 2, $\mathcal P$ forces it if and only if every member of $\mathcal P$ is infinite. For instance $\{ \emptyset \}$ does not force it.
- *Computable Sacks.* Every condition $T$ forces it. Let $S \leq T$ and $m \in \nat$. For each $k$, the sets $\bigcup_j S(\rho 0^j)$, for the $2^k$ strings $\rho$ of length $k$, are paths of $S$, and they are distinct since the nodes $S(\rho)$ are pairwise incompatible. So $S$ has infinitely many paths, while only $2^{m+1}$ sets are contained in $\{0, \dots, m\}$; hence $S$ does not force $\Phi^G_a(m)\diverge$. The identity tree has finite paths.
- *Computable Mathias.* Every condition forces it. An extension $(\tau, Y)$ has the member whose bits below $|\tau|$ are those of $\tau$ and whose elements from $|\tau|$ on are those of $Y$; it is infinite, so $(\tau, Y)$ does not force $\Phi^G_a(m)\diverge$. The member $\sigma 0 0 \cdots$ of $(\sigma, X)$ is finite.

So a condition may force the sentence while having a finite member in every notion except Jockusch–Soare forcing, where forcing this sentence is truth on all members.
:::
::::

::::exercise{#ex-cohen-pi2-comeager difficulty=2 objective="Interpret the forcing of a $\Pi^0_2$ sentence by a string in terms of Baire category."}
For Cohen forcing, let $\sigma$ be a string and $\varphi = \forall y\ \Phi^G_e(y)\converge$ a $\Pi^0_2$ sentence. Show that $\sigma \Vdash \varphi$ if and only if the class of members of $\sigma$ that do not satisfy $\varphi$ is meager.

:::solution
By the universal clause, $\sigma \Vdash \varphi$ if and only if no $\tau \succeq \sigma$ forces $\Phi^G_e(m)\diverge$ for any $m$. By :ref{#prop-force-sigma1}, $\tau$ forces $\Phi^G_e(m)\diverge$ if and only if no $\rho \succeq \tau$ satisfies $\Phi^\rho_e(m)\converge$. So $\sigma \Vdash \varphi$ if and only if for every $m$ and every $\tau \succeq \sigma$ there is $\rho \succeq \tau$ with $\Phi^\rho_e(m)\converge$.

Suppose $\sigma \Vdash \varphi$. For each $m$, let $\mathcal C_m = [\sigma] \cap \{ X : \Phi^X_e(m)\diverge \}$. It is nowhere dense: given a string $\tau$, if $\tau$ is incompatible with $\sigma$, then $[\tau]$ is disjoint from $\mathcal C_m$; otherwise let $\tau'$ be the longer of $\tau$ and $\sigma$, and $\rho \succeq \tau'$ with $\Phi^\rho_e(m)\converge$; then $[\rho] \subseteq [\tau]$ and $[\rho]$ is disjoint from $\mathcal C_m$ by the use principle. The members of $\sigma$ that do not satisfy $\varphi$ form $\bigcup_m \mathcal C_m$, a meager class (:ref{#def-meager}).

Conversely, suppose that $\sigma$ does not force $\varphi$: some $\tau \succeq \sigma$ and $m$ have no $\rho \succeq \tau$ with $\Phi^\rho_e(m)\converge$. Then no member of $\tau$ satisfies $\Phi^G_e(m)\converge$, by the use principle, so the cylinder $[\tau]$ is contained in the class of members of $\sigma$ that do not satisfy $\varphi$. A cylinder is not meager (:ref{#thm-baire-category}), and a subclass of a meager class is meager, so this class is not meager.
:::
::::
:::::
