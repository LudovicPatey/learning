---
title: The forcing question
summary: Forcing questions and their definability; a forcing question for tree forcings at every level; preservation of non-Σ⁰ₙ sets and cone avoidance for the iterated jumps.
duration: 25
prerequisites: [forcing-with-trees, cohen-forcing]
---

The preservation theorem for Cohen forcing (:ref{#thm-cohen-preservation}) used one fact about the forcing relation: for a condition $c$ and a $\Sigma^0_n$ formula $\varphi(x)$, the set of $m$ such that $c$ can be extended to force $\varphi(m)$ is $\Sigma^0_n$. For tree forcings the forcing relation is too complex for this (:ref{#prop-js-complexity}), but the proof of :ref{#thm-tree-gl2} used a substitute at level $2$: a $\Sigma^0_2$ question whose positive answer yields an extension forcing the sentence, and whose negative answer yields an extension forcing its negation.

A **forcing question** is such a substitute, at every level. It isolates what the density arguments of the previous lessons need, and leaves aside how the extensions are found. This lesson defines forcing questions, builds one for tree forcings, and proves that every notion of forcing with a $\Sigma^0_n$-preserving question preserves the non-$\Sigma^0_n$ sets, hence avoids the cones above the sets not computable in $\emptyset^{(n-1)}$. The next lesson adds two properties of questions, compactness and merging, which give the preservation of hyperimmunity and the avoidance of PA degrees. The method is due to Monin and Patey, and is used to prove that combinatorial principles admit computationally weak solutions.

## Forcing questions

:::definition{#def-forcing-question}
Let $\mathbb P$ be a notion of forcing. A **forcing question** is a relation $c \mathrel{?{\vdash}} \varphi$ between conditions and sentences of the form $\Sigma^0_n$, $n \geq 1$, such that for every condition $c$ and every such sentence $\varphi$:

1. if $c \mathrel{?{\vdash}} \varphi$, some extension of $c$ forces $\varphi$;
2. if $c \mathrel{?{\nvdash}} \varphi$, some extension of $c$ forces $\neg \varphi$.

The question is **$\Sigma^0_n$-preserving** if for every condition $c$ and every $\Sigma^0_n$ formula $\varphi(\vec x)$, the relation $\{ \vec m : c \mathrel{?{\vdash}} \varphi(\vec m) \}$ is $\Sigma^0_n$.
:::

The question does not decide whether $c$ forces $\varphi$; it tells which of $\varphi$ and $\neg \varphi$ can be forced below $c$, and may answer either way when both can. Every notion of forcing has a forcing question: let $c \mathrel{?{\vdash}} \varphi$ if some extension of $c$ forces $\varphi$; property 2 holds by :ref{#prop-forcing-basic}. The point is definability.

A forcing question may be given only for the $\Sigma^0_n$ sentences of some levels, for instance only for $\Sigma^0_1$ sentences, as for Mathias forcing in :ref{to="effective-forcing/mathias-forcing"}; the definitions and theorems below use a question only at the levels they mention. The later courses of the track, from :ref{to="avoidance/forcing-question-method"} on, use questions of this kind, with $\Sigma^0_1$-preservation relative to a set depending on the condition.

:::example{#ex-cohen-question}
For Cohen forcing, the relation "$\sigma \mathrel{?{\vdash}} \varphi$ if some $\tau \succeq \sigma$ forces $\varphi$" is a forcing question, and it is $\Sigma^0_n$-preserving for every $n$ by :ref{#thm-cohen-forcing-definable}. At level $1$, $\sigma \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if and only if $\Phi^\tau_e(\vec m)\converge$ for some $\tau \succeq \sigma$.
:::

::::exercise{#ex-question-needs-extensions difficulty=1 objective="See why a forcing question must refer to extensions of the condition, and not to the condition alone."}
For Cohen forcing, let $\sigma \mathrel{?{\vdash}} \varphi$ hold, for $\Sigma^0_1$ sentences $\varphi$, if $\sigma$ itself forces $\varphi$. This relation is $\Sigma^0_1$ by :ref{#thm-cohen-forcing-definable}. Show that it is not a forcing question.

:::solution
Property 1 holds, with the condition itself as extension. Property 2 fails. Let $\Phi_e$ be the functional that, on every input, searches for an element of its oracle, and $\varphi$ the sentence $\Phi^G_e(0)\converge$, "$G$ is non-empty". The empty string does not force $\varphi$, since its member $\emptyset$ does not satisfy it. But no string $\tau$ forces $\neg \varphi$, since $\tau 1 1 \cdots$ is a member of $\tau$ satisfying $\varphi$. So the empty string answers negatively, and no extension forces $\neg \varphi$. The question of :ref{#ex-cohen-question}, which asks whether some extension forces $\varphi$, answers positively here.
:::
::::

:::theorem{#thm-tree-question}
Jockusch–Soare forcing and computable Sacks forcing have forcing questions that are $\Sigma^0_n$-preserving for every $n \geq 1$.
:::

:::proof{of=thm-tree-question}
Conditions are given by indices. We define $c \mathrel{?{\vdash}} \varphi$ by induction on the level of $\varphi$, and prove properties 1 and 2 together with the following uniform form of preservation: for each $n$, there is a $\Sigma^0_n$ relation that agrees with "$c \mathrel{?{\vdash}} \varphi$" on indices $c$ of conditions and codes of $\Sigma^0_n$ sentences $\varphi$.

*Level $1$.* For Jockusch–Soare forcing, $\mathcal P \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if $\mathcal P$ forces it, a $\Sigma^0_1$ relation by :ref{#prop-js-complexity}. If not, the class $\mathcal P \cap \{ X : \Phi^X_e(\vec m)\diverge \}$ is non-empty and forces the negation. For Sacks forcing, $T \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if some node $T(\rho)$ has $\Phi^{T(\rho)}_e(\vec m)\converge$, a $\Sigma^0_1$ relation. If so, the full subtree above $T(\rho)$ forces the sentence; if not, $T$ forces its negation by :ref{#prop-sacks-complexity}.

*Level $2$.* Let $c \mathrel{?{\vdash}} \varphi$ if $c$ answers yes for $\varphi$ in the sense of :ref{#prop-tree-sigma2}, which gives properties 1 and 2 and the $\Sigma^0_2$ bound.

*Level $k + 1$, $k \geq 2$.* Let $\varphi = \exists y\ \psi(y)$, with $\psi$ a $\Pi^0_k$ formula. Let $c \mathrel{?{\vdash}} \varphi$ if there are a condition $d \leq c$ and a number $m$ with $d \mathrel{?{\nvdash}} \neg \psi(m)$.

1. If $c \mathrel{?{\vdash}} \varphi$, take $d$ and $m$; by property 2 at level $k$, some $e \leq d$ forces $\neg \neg \psi(m) = \psi(m)$, hence forces $\varphi$.
2. If $c \mathrel{?{\nvdash}} \varphi$, then $d \mathrel{?{\vdash}} \neg \psi(m)$ for every $d \leq c$ and every $m$. We show that $c$ forces $\neg \varphi = \forall y\ \neg \psi(y)$, that is, that no $d \leq c$ forces $\psi(m)$. If $d$ did, property 1 at level $k$ would give $e \leq d$ forcing $\neg \psi(m)$, while $e$ forces $\psi(m)$ by extension, contradicting consistency (:ref{#prop-forcing-basic}).
3. "$d$ is a condition" is $\Pi^0_1$ or $\Pi^0_2$, "$d \leq c$" is $\Pi^0_2$ or $\Pi^0_1$ (:ref{#prop-js-complexity}, :ref{#prop-sacks-complexity}), and "$d \mathrel{?{\nvdash}} \neg \psi(m)$" is $\Pi^0_k$ by the induction hypothesis. Since $k \geq 2$, the relation $\exists d\ \exists m\ (\Pi^0_k)$ is $\Sigma^0_{k+1}$.
:::

The step from level $k$ to level $k + 1$ uses only properties 1 and 2 at level $k$ and the fact that conditions and extension are $\Pi^0_2$. The real work is at levels $1$ and $2$, where each notion of forcing needs its own question.

## Preservation of the arithmetic hierarchy

The proof of :ref{#thm-cohen-preservation} carries over verbatim, with the forcing question in place of the search for an extension.

:::theorem{#thm-question-preservation}
Let $n \geq 1$, and let $\mathbb P$ be a notion of forcing with a $\Sigma^0_n$-preserving forcing question. If $A$ is not $\Sigma^0_n$, then $A$ is not $\Sigma^0_n(G)$ for every sufficiently generic set $G$.
:::

:::proof{of=thm-question-preservation}
For a $\Sigma^0_n$ formula $\varphi(x)$, let $E_\varphi$ be the set of conditions that force $\varphi(m)$ for some $m \notin A$, or force $\neg \varphi(m)$ for some $m \in A$. Given a condition $c$, the set $U = \{ m : c \mathrel{?{\vdash}} \varphi(m) \}$ is $\Sigma^0_n$, so $U \neq A$. If $m \in U \setminus A$, property 1 gives an extension forcing $\varphi(m)$; if $m \in A \setminus U$, property 2 gives an extension forcing $\neg \varphi(m)$. So $E_\varphi$ is dense. A set $G$ generic for the sets $E_\varphi$ and for the sets $D_\psi$, $\psi$ of level at most $n$, satisfies, for each $\varphi$, $G \models \varphi(m)$ for some $m \notin A$ or $G \models \neg \varphi(m)$ for some $m \in A$ (:ref{#thm-forcing-truth}). No $\Sigma^0_n$ formula defines $A$ with parameter $G$, so $A$ is not $\Sigma^0_n(G)$.
:::

:::figure[The density argument of :ref{#thm-question-preservation}, and of :ref{#thm-cohen-preservation}. The set $U$ of numbers $m$ for which the condition $c$ answers yes about $\varphi(m)$ is $\Sigma^0_n$, so it differs from $A$; an element of the difference gives an extension on which $\varphi$ and $A$ disagree.]
<svg class="fig" viewBox="0 0 600 214" width="600" role="img" aria-label="The density argument: the set U of numbers m such that c answers yes to the question about phi(m) differs from A; an element of the difference gives an extension forcing phi(m) with m outside A, or not phi(m) with m in A"><defs><marker id="ef-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="ink-fill"/></marker></defs><rect x="200" y="10" width="200" height="56" rx="6" class="state"/><text x="300.0" y="30" text-anchor="middle" class="label">condition c</text><text x="300.0" y="46" text-anchor="middle" class="label">U = { m : c ?⊢ φ(m) } is Σ⁰ₙ</text><rect x="20" y="128" width="240" height="56" rx="6" class="state"/><text x="140.0" y="148" text-anchor="middle" class="label">m ∈ U, m ∉ A</text><text x="140.0" y="164" text-anchor="middle" class="label">d ≤ c with d ⊩ φ(m)</text><rect x="340" y="128" width="240" height="56" rx="6" class="state"/><text x="460.0" y="148" text-anchor="middle" class="label">m ∈ A, m ∉ U</text><text x="460.0" y="164" text-anchor="middle" class="label">d ≤ c with d ⊩ ¬φ(m)</text><line x1="270" y1="68" x2="160" y2="124" class="ink-stroke" stroke-width="1.2" marker-end="url(#ef-arr)"/><line x1="330" y1="68" x2="440" y2="124" class="ink-stroke" stroke-width="1.2" marker-end="url(#ef-arr)"/><text x="300" y="104" text-anchor="middle" class="label">A is not Σ⁰ₙ, so U ≠ A</text><text x="300" y="206" text-anchor="middle" class="label">either way, φ does not define A from a generic set below d</text></svg>
:::

:::corollary{#cor-question-jump-cone}
Let $n \geq 0$, and let $\mathbb P$ be a notion of forcing with a $\Sigma^0_{n+1}$-preserving forcing question. If $A$ is not computable in $\emptyset^{(n)}$, then $A$ is not computable in $G^{(n)}$ for every sufficiently generic set $G$. In particular this holds for Jockusch–Soare and computable Sacks forcing, for every $n$.
:::

:::proof{of=cor-question-jump-cone}
As in :ref{#cor-cohen-jump-cone}: $A$ or its complement is not $\Sigma^0_{n+1}$, hence not $\Sigma^0_{n+1}(G)$, so $A$ is not computable in $G^{(n)}$ by Post's theorem relativized. The last statement is :ref{#thm-tree-question}.
:::

For Jockusch–Soare forcing and $n = 0$ this is the cone avoidance basis theorem (:ref{#thm-cone-avoidance-basis}); for $n = 1$, it gives a member of every non-empty $\Pi^0_1$ class whose jump does not compute a given set not computable in $\emptyset'$.

:::quiz[forcing questions]
Why does :ref{#def-forcing-question} not require that $c$ itself force $\varphi$ when $c \mathrel{?{\vdash}} \varphi$?

- [x] Because the density arguments only need an extension of $c$ with the required property, and requiring more would make the question as complex as the forcing relation.
- [ ] Because no condition forces a $\Sigma^0_n$ sentence.

  Conditions force many $\Sigma^0_n$ sentences; the question is about what can be reached below $c$.
- [ ] Because the answer would otherwise be undecidable.

  The issue is the level of definability, not decidability.

---

In the proof of :ref{#thm-tree-question}, where is it used that being a condition and extension are $\Pi^0_2$?

- [x] In the complexity bound at level $k + 1 \geq 3$: the quantifier over extensions $d \leq c$ adds a $\Pi^0_2$ conjunct, which is absorbed in $\Pi^0_k$ since $k \geq 2$.
- [ ] In properties 1 and 2 at level $k + 1$.

  Those follow from properties 1 and 2 at level $k$ and from consistency, for any notion of forcing.
- [ ] At level $1$.

  Level $1$ uses the specific descriptions of :ref{#prop-js-complexity} and :ref{#prop-sacks-complexity}.
:::

## Notes and references

The forcing question was introduced by Monin and Patey, and appears in several of their papers on the reverse mathematics of Ramsey-type theorems, for instance in *Pigeons do not jump high* (2019), where forcing relations and questions adapted to variants of Mathias forcing are designed to build solutions to the pigeonhole principle that are not high; Patey (2015, arXiv) had used forcing relations with the complexity of the formulas they force to control iterated jumps. The abstract definition and the preservation of the arithmetic hierarchy follow the chapter *Effective forcing* of Monin and Patey, section *Forcing question*, where questions are defined for $\Sigma^0_n$ and $\Pi^0_n$ sentences; the version here, for $\Sigma^0_n$ sentences only, suffices for all the applications of the course. The forcing question of Jockusch–Soare forcing at level $1$ is the over-approximation used in the proof of the cone avoidance basis theorem.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics (2019), doi:10.1016/j.aim.2019.06.026; arXiv:1803.09771.
- L. Patey, *Controlling iterated jumps of solutions to combinatorial problems*, arXiv:1509.05340 (2015).
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, sections *Computational complexity and forcing question* and *Forcing question*.

:::::exercises
::::exercise{#ex-js-naive-question difficulty=2 objective="See that the question &quot;some extension forces $\varphi$&quot; may fail to be $\Sigma^0_1$-preserving for Jockusch–Soare forcing."}
For Jockusch–Soare forcing, let $\mathcal P \mathrel{?{\vdash}} \varphi$ hold, for $\Sigma^0_1$ sentences, if some extension of $\mathcal P$ forces $\varphi$.

1. Show that $\mathcal P \mathrel{?{\vdash}} \Phi^G_e(\vec m)\converge$ if and only if some member $X$ of $\mathcal P$ satisfies $\Phi^X_e(\vec m)\converge$.
2. For a number $a$, let $C_a = \{ \langle a, t \rangle : t \in \nat \}$ be the $a$-th column. Show that $\mathcal P = \{ \emptyset \} \cup \{ C_a : a \notin \emptyset' \}$ is a non-empty $\Pi^0_1$ class.
3. Let $\Phi_e$ be the functional that, on input $m$, searches for $t$ with $\langle m, t \rangle \in G$. Show that $\{ m : \mathcal P \mathrel{?{\vdash}} \Phi^G_e(m)\converge \}$ is the complement of $\emptyset'$, so that this question is not $\Sigma^0_1$-preserving.

:::solution
1. If some $\mathcal Q \subseteq \mathcal P$ forces the sentence, any member of $\mathcal Q$ is a member of $\mathcal P$ satisfying it. Conversely, if $X \in \mathcal P$ satisfies $\Phi^X_e(\vec m)\converge$ with use $u$, then $\mathcal P \cap [X \uh u]$ is a non-empty $\Pi^0_1$ class contained in $\mathcal P$, and all its members satisfy the sentence by the use principle.
2. Let $T$ be the set of strings $\sigma$ that either have no $1$, or for which there is $a$ such that $\sigma(p) = 1$ exactly for the positions $p < |\sigma|$ of the form $\langle a, t \rangle$, and $a$ has not entered $\emptyset'$ by stage $|\sigma|$. The number $a$ is then unique, since it is read off any position where $\sigma$ is $1$, so $T$ is computable. It is closed under prefixes: a prefix of $\sigma$ has no $1$, or the same pattern for the same $a$, which has not entered $\emptyset'$ by an earlier stage either. A path of $T$ with no $1$ is $\emptyset$. A path with a $1$ at a position $\langle a, t \rangle$ has the pattern of $a$ on all its long prefixes, so it is $C_a$, and $a$ has not entered $\emptyset'$ at any stage, that is, $a \notin \emptyset'$. Conversely $\emptyset$, and $C_a$ for $a \notin \emptyset'$, are paths. So $\mathcal P = [T]$, which contains $\emptyset$.
3. By item 1, $\mathcal P \mathrel{?{\vdash}} \Phi^G_e(m)\converge$ if and only if some member of $\mathcal P$ meets the column of $m$. The member $\emptyset$ does not, and $C_a$ does if and only if $a = m$. So the answer is positive if and only if $C_m \in \mathcal P$, that is, $m \notin \emptyset'$. The complement of $\emptyset'$ is not c.e. By contrast, the question of :ref{#thm-tree-question} answers positively at $\mathcal P$ only if $\mathcal P$ itself forces the convergence, which never happens here, because of the member $\emptyset$.
:::
::::

::::exercise{#ex-question-iterated-cones difficulty=1 objective="Combine the cone avoidance results for iterated jumps into one basis theorem."}
Let $C_0, C_1, \dots$ be sets with $C_n \not\leq_T \emptyset^{(n)}$ for every $n$. Show that every non-empty $\Pi^0_1$ class has a member $G$ with $C_n \not\leq_T G^{(n)}$ for every $n$. Deduce that every non-empty $\Pi^0_1$ class has a member that is not high.

:::solution
By :ref{#thm-tree-question} and :ref{#cor-question-jump-cone}, for each $n$ there is a countable family $\mathcal D_n$ of dense sets of Jockusch–Soare forcing such that $C_n \not\leq_T G^{(n)}$ for every $\mathcal D_n$-generic set $G$. Let $\mathcal P$ be a non-empty $\Pi^0_1$ class. By :ref{#lem-rasiowa-sikorski}, some filter containing $\mathcal P$ is generic for the countable family $\bigcup_n \mathcal D_n$; its generic set $G$ is a member of $\mathcal P$, and $C_n \not\leq_T G^{(n)}$ for every $n$. For the last statement, take $C_1 = \emptyset''$, which is not computable in $\emptyset'$, and for instance $C_n = \emptyset^{(n+1)}$ for the other $n$; then $\emptyset'' \not\leq_T G'$.
:::
::::

::::exercise{#ex-question-pi-sentences difficulty=1 objective="Extend a forcing question from $\Sigma^0_n$ sentences to $\Pi^0_n$ sentences."}
Let $\mathbb P$ have a forcing question for $\Sigma^0_n$ sentences. For a $\Pi^0_n$ sentence $\psi$, let $c \mathrel{?{\vdash}} \psi$ hold if $c \mathrel{?{\nvdash}} \neg \psi$. Show that properties 1 and 2 of :ref{#def-forcing-question} hold for $\Pi^0_n$ sentences, and that if the question is $\Sigma^0_n$-preserving, then $\{ \vec m : c \mathrel{?{\vdash}} \psi(\vec m) \}$ is $\Pi^0_n$ for every condition $c$ and every $\Pi^0_n$ formula $\psi(\vec x)$.

:::solution
The sentence $\neg \psi$ is $\Sigma^0_n$, and $\neg \neg \psi = \psi$. If $c \mathrel{?{\vdash}} \psi$, then $c \mathrel{?{\nvdash}} \neg \psi$, and property 2 for $\neg \psi$ gives an extension forcing $\neg \neg \psi = \psi$. If $c \mathrel{?{\nvdash}} \psi$, then $c \mathrel{?{\vdash}} \neg \psi$, and property 1 for $\neg \psi$ gives an extension forcing $\neg \psi$. For the complexity, $\{ \vec m : c \mathrel{?{\vdash}} \psi(\vec m) \}$ is the complement of $\{ \vec m : c \mathrel{?{\vdash}} \neg \psi(\vec m) \}$, which is $\Sigma^0_n$ since $\neg \psi(\vec x)$ is a $\Sigma^0_n$ formula.
:::
::::

::::exercise{#ex-question-not-monotone difficulty=1 objective="Compare how forcing and the forcing question behave under extension."}
For the question of Cohen forcing of :ref{#ex-cohen-question}, find a $\Sigma^0_1$ sentence $\varphi$ and strings $\tau \preceq \sigma$ such that $\tau \mathrel{?{\vdash}} \varphi$ and $\sigma \mathrel{?{\nvdash}} \varphi$. Show that, on the contrary, a negative answer at $\tau$ remains negative at every $\sigma \succeq \tau$, and that a sentence forced by $\tau$ is forced by every $\sigma \succeq \tau$.

:::solution
Let $\varphi$ be the $\Sigma^0_1$ sentence expressing $G(0) = 1$, given by a functional that reads the bit $0$ of its oracle and converges if and only if it is $1$. The empty string answers positively, since its extension $1$ forces $\varphi$. The string $0$ answers negatively: all its extensions have $0$ at position $0$, so none forces $\varphi$.

If $\tau \mathrel{?{\nvdash}} \varphi$, no extension of $\tau$ forces $\varphi$; the extensions of $\sigma \succeq \tau$ are extensions of $\tau$, so none of them forces $\varphi$, and $\sigma \mathrel{?{\nvdash}} \varphi$. The last statement is the extension property of :ref{#prop-forcing-basic}. So the question records what can still be forced, which shrinks along a construction, while forcing records what has been forced, which grows.
:::
::::

::::exercise{#ex-question-relativized difficulty=1 objective="Relativize the preservation theorem at level $1$ to formulas with oracle $Z \oplus G$."}
Let $Z$ be a set, and consider the $\Sigma^0_1$ sentences with oracle $Z \oplus G$ (:ref{#ex-forcing-formulas}, item 4). Suppose that a notion of forcing has a forcing question for these sentences such that $\{ m : c \mathrel{?{\vdash}} \varphi(m) \}$ is $\Sigma^0_1(Z)$ for every condition $c$ and every such formula $\varphi(x)$. Show that if $A$ is not $\Sigma^0_1(Z)$, then $A$ is not $\Sigma^0_1(Z \oplus G)$ for every sufficiently generic set $G$, and that if $C \not\leq_T Z$, then $C \not\leq_T Z \oplus G$ for every sufficiently generic set $G$.

:::solution
For a formula $\varphi(x)$, let $E_\varphi$ be the set of conditions forcing $\varphi(m)$ for some $m \notin A$, or $\neg \varphi(m)$ for some $m \in A$. Given $c$, the set $U = \{ m : c \mathrel{?{\vdash}} \varphi(m) \}$ is $\Sigma^0_1(Z)$, so $U \neq A$, and properties 1 and 2 give an extension in $E_\varphi$, as in :ref{#thm-question-preservation}. Let $G$ be generic for the sets $E_\varphi$. For each $\varphi$, $G$ is a member of a condition in $E_\varphi$, and at level $1$ forcing is truth on all members; so $G$ satisfies $\varphi(m)$ for some $m \notin A$, or $\neg \varphi(m)$ for some $m \in A$. The $\Sigma^0_1(Z \oplus G)$ sets are the sets $\{ m : \Phi^{Z \oplus G}_e(m)\converge \}$, so $A$ is not one of them.

If $C \not\leq_T Z$, then $C$ or its complement is not $\Sigma^0_1(Z)$, since a set that is $\Sigma^0_1(Z)$ and $\Pi^0_1(Z)$ is $Z$-computable. By the first part, for every set generic for the corresponding family, $C$ or its complement is not $\Sigma^0_1(Z \oplus G)$, so $C \not\leq_T Z \oplus G$.
:::
::::
:::::
