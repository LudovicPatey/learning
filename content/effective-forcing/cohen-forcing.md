---
title: Definability of forcing for Cohen forcing
summary: For Cohen forcing, forcing a Σ⁰ₙ formula is a Σ⁰ₙ relation; n-generic filters and n-generic sets; the jumps of generic sets; generic sets preserve the non-Σ⁰ₙ sets and avoid the cones above sets not computable in the n-th jump.
duration: 45
prerequisites: [forcing-relation, generic-sets, cohen-genericity/n-genericity]
---

The forcing relation of the previous lesson is defined for every notion of forcing, but its usefulness in computability theory depends on its complexity. If the relation "$c \Vdash \varphi$" is not much more complex than $\varphi$ itself, then questions about a generic set can be answered from questions about conditions, with a known oracle. Cohen forcing is the model case: the conditions are strings, the extension relation is computable, and forcing a $\Sigma^0_n$ sentence is a $\Sigma^0_n$ property of the string. This lesson proves this fact and derives three consequences: the $n$-generic sets of :ref{#def-relative-genericity} are exactly the sets whose filters are $n$-generic in the sense of the previous lesson; their $n$-th jump is computable from $G \oplus \emptyset^{(n)}$; and sufficiently generic sets do not help to define or compute any set that is not already $\Sigma^0_n$ or computable in $\emptyset^{(n)}$. The last argument is the template for the forcing question (:ref{to="effective-forcing/forcing-question"}).

## The complexity of forcing

Recall that sentences are coded by numbers, and that from the code of a formula $\psi(y)$ and a number $m$ one computes the code of $\psi(m)$.

:::theorem{#thm-cohen-forcing-definable}
For Cohen forcing and $n \geq 1$, the relation "$\sigma \Vdash \varphi$", for strings $\sigma$ and $\Sigma^0_n$ sentences $\varphi$, is $\Sigma^0_n$; for $\Pi^0_n$ sentences it is $\Pi^0_n$.
:::

:::proof{of=thm-cohen-forcing-definable}
By induction on $n$.

*Level $1$, $\Sigma^0_1$.* Let $\varphi$ be $\Phi^G_e(\vec m)\converge$. We show that $\sigma \Vdash \varphi$ if and only if there is $\ell \geq |\sigma|$ such that $\Phi^\tau_e(\vec m)[\ell]\converge$ for every $\tau \succeq \sigma$ of length $\ell$. This is $\Sigma^0_1$, since the inner condition is decidable (:ref{#prop-oracle-stages}) and involves finitely many strings. If such an $\ell$ exists, every $X \succ \sigma$ extends one of these strings $\tau$, and $\Phi^X_e(\vec m)\converge$ by monotonicity. Conversely, suppose $\sigma \Vdash \varphi$, and let $B$ be the set of strings $\tau$ comparable with $\sigma$ such that $\Phi^\tau_e(\vec m)[|\tau|]\diverge$. By monotonicity, $B$ is closed under prefixes. If $B$ were infinite, it would have a path $X$ by weak König's lemma (:ref{#lem-weak-konig}); $X$ extends $\sigma$, so $\Phi^X_e(\vec m)\converge$, with a prefix $X \uh u$ at some stage $s$, and then $\Phi^{X \uh \ell}_e(\vec m)[\ell]\converge$ for $\ell \geq \max(u, s)$, so $X \uh \ell \notin B$. Hence $B$ is finite, and every $\ell$ larger than the lengths of its elements, with $\ell \geq |\sigma|$, works.

*Level $1$, $\Pi^0_1$.* By :ref{#prop-force-sigma1}, $\sigma \Vdash \Phi^G_e(\vec m)\diverge$ if and only if $\Phi^\tau_e(\vec m)[s]\diverge$ for every $\tau \succeq \sigma$ and every $s$, a $\Pi^0_1$ condition.

*Level $n + 1$.* If $\varphi = \exists y\ \psi(y)$, then $\sigma \Vdash \varphi$ if and only if $\exists m\ \sigma \Vdash \psi(m)$, a projection of a $\Pi^0_n$ relation by the induction hypothesis, hence $\Sigma^0_{n+1}$. If $\varphi = \forall y\ \psi(y)$, then $\sigma \Vdash \varphi$ if and only if
$$
\forall \tau\ \forall m\ \big(\tau \succeq \sigma \rightarrow \neg\, (\tau \Vdash \neg \psi(m))\big).
$$
The relation $\tau \Vdash \neg \psi(m)$ is $\Pi^0_n$ by the induction hypothesis, since $\neg \psi(m)$ is $\Pi^0_n$, so its negation is $\Sigma^0_n$; the relation $\tau \succeq \sigma$ is decidable. So the whole is $\Pi^0_{n+1}$.
:::

Two features of Cohen forcing are used. At level $1$, forcing has the complexity of the sentence, by compactness of the cylinders. At higher levels, the universal clause quantifies over the extensions of $\sigma$, and "$\tau \succeq \sigma$" is decidable. For the notions of forcing of the next lesson, both features fail, and the complexity of forcing grows faster than the level of the sentence.

:::quiz[the complexity of Cohen forcing]
In the proof of :ref{#thm-cohen-forcing-definable}, where is weak König's lemma used?

- [x] To show that if all extensions of $\sigma$ make the computation converge, they do so by a common length $\ell$, so that forcing a $\Sigma^0_1$ sentence is $\Sigma^0_1$.
- [ ] To show that forcing a $\Pi^0_1$ sentence is $\Pi^0_1$.

  This case only needs the use principle: a convergent computation on an extension would converge on a string extending $\sigma$.
- [ ] To show that the universal clause gives a $\Pi^0_{n+1}$ relation.

  That step only counts quantifiers.

---

For $\Pi^0_2$ sentences, what would the proof give if the extension relation were only $\Pi^0_2$, as for some notions of forcing of the next lesson?

- [x] A $\Pi^0_3$ bound: "$\tau$ extends $\sigma$" appears negatively in an implication under the universal quantifiers, so it contributes a $\Sigma^0_2$ disjunct to the matrix.
- [ ] The same $\Pi^0_2$ bound.

  The matrix would contain a $\Sigma^0_2$ disjunct, which a $\Pi^0_2$ bound cannot absorb.
- [ ] No bound, since the forcing relation would no longer satisfy extension.

  Extension holds for every notion of forcing (:ref{#prop-forcing-basic}); only the complexity changes.
:::

::::exercise{#ex-cohen-totality-pi2 difficulty=1 objective="Unfold the forcing of a $\Pi^0_2$ sentence for Cohen forcing and count its quantifiers."}
Show directly from the definition that a string $\sigma$ forces "$\Phi^G_e$ is total" if and only if for every $\tau \succeq \sigma$ and every $x$ there is $\rho \succeq \tau$ with $\Phi^\rho_e(x)\converge$, and check that this is a $\Pi^0_2$ property of $(\sigma, e)$.

:::solution
By the universal clause, $\sigma$ forces the sentence if and only if no $\tau \succeq \sigma$ forces $\Phi^G_e(x)\diverge$ for any $x$. By :ref{#prop-force-sigma1}, $\tau$ forces $\Phi^G_e(x)\diverge$ if and only if no $\rho \succeq \tau$ has $\Phi^\rho_e(x)\converge$. So $\sigma$ forces the sentence if and only if for every $\tau \succeq \sigma$ and $x$ some $\rho \succeq \tau$ has $\Phi^\rho_e(x)\converge$. The relation $\Phi^\rho_e(x)\converge$ is $\Sigma^0_1$, so the condition has the form $\forall \tau\ \forall x\ \exists \rho\ \exists s$ (decidable), which is $\Pi^0_2$.
:::
::::

## n-generic sets

For Cohen forcing, a filter meeting the sets $S_k$ is the set of prefixes of $G_F$. The two notions of $n$-genericity, for sets in :ref{#def-relative-genericity} and for filters in :ref{#def-n-generic-notion}, coincide.

:::theorem{#thm-cohen-n-generic}
Let $n \geq 1$. A set $G$ is $n$-generic, that is, meets or avoids every $\Sigma^0_n$ set of strings, if and only if its filter of prefixes is $n$-generic for Cohen forcing.
:::

:::proof{of=thm-cohen-n-generic}
Suppose $G$ is $n$-generic, and let $\varphi$ be a $\Sigma^0_k$ sentence with $1 \leq k \leq n$. The set $W = \{ \sigma : \sigma \Vdash \varphi \}$ is $\Sigma^0_k$ by :ref{#thm-cohen-forcing-definable}, hence $\Sigma^0_n$. If a prefix of $G$ belongs to $W$, it forces $\varphi$. If a prefix $\sigma$ of $G$ avoids $W$, no extension of $\sigma$ forces $\varphi$, so $\sigma \Vdash \neg \varphi$ by :ref{#prop-forcing-basic}. So the filter meets $D_\varphi = D_{\neg \varphi}$, for every sentence of level at most $n$.

Conversely, suppose the filter $F$ of prefixes of $G$ is $n$-generic, and let $W$ be a $\Sigma^0_n$ set of strings, say $W = \{ \sigma : \exists y_1\ \forall y_2 \cdots R(\sigma, \vec y) \}$ with $R$ computable. The property "some prefix of $G$ belongs to $W$" is $\Sigma^0_n(G)$, uniformly in $G$, so it is expressed by a $\Sigma^0_n$ sentence $\varphi_W$ (see the previous lesson). Some prefix $\sigma$ of $G$ decides $\varphi_W$. If $\sigma \Vdash \varphi_W$, then $G \models \varphi_W$ by :ref{#thm-forcing-truth}, and $G$ meets $W$. If $\sigma \Vdash \neg \varphi_W$, then $\sigma$ avoids $W$: if some $\tau \succeq \sigma$ belonged to $W$, an $n$-generic filter $H$ containing $\tau$ (:ref{#lem-rasiowa-sikorski}) would determine a set $G_H \succ \tau$ meeting $W$, so $G_H \models \varphi_W$; but $H$ contains $\sigma$, which forces $\neg \varphi_W$, so $G_H \models \neg \varphi_W$ by :ref{#thm-forcing-truth}.
:::

By :ref{#thm-cohen-forcing-definable}, the sets $D_\varphi$ for the sentences of level at most $n$, and the sets $S_k$, are uniformly $\emptyset^{(n)}$-effectively dense: given a string $\sigma$ and a $\Sigma^0_k$ sentence $\varphi$ with $k \leq n$, the oracle $\emptyset^{(n)}$ decides whether some extension of $\sigma$ forces $\varphi$, and finds one if so; otherwise $\sigma$ forces $\neg \varphi$. By :ref{#thm-effective-generic}, there is an $n$-generic set computable in $\emptyset^{(n)}$, which is a second proof of :ref{#thm-low-generic-exists}.

The theorem explains the form of :ref{#thm-n-generic-decides}, where a prefix of an $n$-generic set decides a $\Sigma^0_n$ property for the $(n-1)$-generic extensions of the prefix only: a string that forces a $\Sigma^0_n$ sentence guarantees it for generic sets, not for all its members.

## The jumps of generic sets

The following is a second proof of :ref{#thm-generic-jumps}, by forcing.

:::corollary{#cor-cohen-jumps}
If $G$ is $n$-generic, then $G^{(n)} \leq_T G \oplus \emptyset^{(n)}$.
:::

:::proof{of=cor-cohen-jumps}
Let $\theta_n(x)$ be the $\Sigma^0_n$ formula with $m \in X^{(n)} \iff X \models \theta_n(m)$ for every $X$ (previous lesson). Given $m$, search for a prefix $\sigma$ of $G$ that forces $\theta_n(m)$ or forces $\neg \theta_n(m)$, and answer accordingly. The search uses $G$ to list its prefixes and $\emptyset^{(n)}$ to decide the two relations, which are $\Sigma^0_n$ and $\Pi^0_n$ by :ref{#thm-cohen-forcing-definable}. It terminates by :ref{#thm-cohen-n-generic}, and the answer is correct by :ref{#thm-forcing-truth}.
:::

## Preservation of the arithmetic hierarchy

If a set $A$ is not $\Sigma^0_n$, can it become $\Sigma^0_n$ relative to a generic set? The answer is no, for every sufficiently generic set. The proof compares $A$ with the set of numbers $m$ for which some extension of the current condition forces $\varphi(m)$, a $\Sigma^0_n$ set by the definability of forcing.

:::theorem{#thm-cohen-preservation}
Let $n \geq 1$ and let $A$ be a set that is not $\Sigma^0_n$. For every sufficiently generic set $G$ for Cohen forcing, $A$ is not $\Sigma^0_n(G)$.
:::

:::proof{of=thm-cohen-preservation}
For a $\Sigma^0_n$ formula $\varphi(x)$, let $E_\varphi$ be the set of strings $\tau$ such that $\tau \Vdash \varphi(m)$ for some $m \notin A$, or $\tau \Vdash \neg \varphi(m)$ for some $m \in A$. We show that $E_\varphi$ is dense. Let $\sigma$ be a string, and
$$
U = \{ m : \exists \tau \succeq \sigma\ \ \tau \Vdash \varphi(m) \}.
$$
By :ref{#thm-cohen-forcing-definable}, $U$ is $\Sigma^0_n$, so $U \neq A$. If $m \in U \setminus A$, some $\tau \succeq \sigma$ forces $\varphi(m)$, with $m \notin A$. If $m \in A \setminus U$, no extension of $\sigma$ forces $\varphi(m)$, so $\sigma \Vdash \neg \varphi(m)$ by :ref{#prop-forcing-basic}, with $m \in A$. In both cases $\sigma$ has an extension in $E_\varphi$.

Let $G$ be generic for the countable family of the sets $E_\varphi$ and $D_\psi$, for all $\Sigma^0_n$ formulas $\varphi(x)$ and all sentences $\psi$ of level at most $n$. For each $\varphi$, a prefix of $G$ belongs to $E_\varphi$, so by :ref{#thm-forcing-truth}, $G \models \varphi(m)$ for some $m \notin A$ or $G \models \neg \varphi(m)$ for some $m \in A$. So no $\Sigma^0_n$ formula defines $A$ with the parameter $G$, and $A$ is not $\Sigma^0_n(G)$.
:::

:::corollary{#cor-cohen-jump-cone}
Let $n \geq 0$ and let $A$ be a set not computable in $\emptyset^{(n)}$. For every sufficiently generic set $G$ for Cohen forcing, $A$ is not computable in $G^{(n)}$.
:::

:::proof{of=cor-cohen-jump-cone}
By Post's theorem (:ref{#thm-post}), $A$ is not $\Delta^0_{n+1}$, so $A$ or its complement is not $\Sigma^0_{n+1}$. By :ref{#thm-cohen-preservation}, for every sufficiently generic $G$, $A$ or its complement is not $\Sigma^0_{n+1}(G)$, so $A$ is not $\Delta^0_{n+1}(G)$, and by Post's theorem relativized to $G$, $A$ is not computable in $G^{(n)}$.
:::

For $n = 0$ this is cone avoidance (:ref{#thm-cone-avoidance}). For $n = 1$ and $A = \emptyset''$, it says that sufficiently generic sets are not high.

:::quiz[preservation of the arithmetic hierarchy]
In the proof of :ref{#thm-cohen-preservation}, why is it enough that $U \neq A$, without knowing which elements are in the difference?

- [x] Because both kinds of disagreement give an extension in $E_\varphi$: an $m \in U \setminus A$ gives an extension forcing $\varphi(m)$, an $m \in A \setminus U$ shows that $\sigma$ itself forces $\neg \varphi(m)$.
- [ ] Because $U \subseteq A$.

  Nothing prevents $U$ from containing elements outside $A$; this case is handled by the first kind of extension.
- [ ] Because the construction is effective.

  The construction is not effective: finding an element of $U \setminus A$ or $A \setminus U$ needs $A$.

---

Which property of Cohen forcing makes $U$ a $\Sigma^0_n$ set?

- [x] The definability of forcing, :ref{#thm-cohen-forcing-definable}, together with the decidability of the extension relation.
- [ ] The fact that $A$ is not $\Sigma^0_n$.

  That is the hypothesis used after the complexity of $U$ is known.
- [ ] The theorem on forcing and truth.

  That theorem is used at the end, to transfer the decisions to the generic set.
:::

::::exercise{#ex-cohen-relative-preservation difficulty=2 objective="Find how much genericity the preservation theorem needs at level $1$."}
Show that in :ref{#thm-cohen-preservation}, for $n = 1$, it suffices that $G$ be 1-generic relative to $A$.

:::solution
For a $\Sigma^0_1$ formula $\varphi(x) = \Phi^G_e(x)\converge$, the set $W_\varphi = \{ \tau : \exists m \notin A\ \ \Phi^\tau_e(m)\converge \}$ is $A$-c.e. If $G$ meets $W_\varphi$, then $\Phi^G_e(m)\converge$ for some $m \notin A$. Otherwise some prefix $\sigma$ of $G$ avoids $W_\varphi$: no extension of $\sigma$ makes $\Phi_e$ converge at an $m \notin A$. If $\Phi_e^G$ converged exactly on $A$, then $A = \{ m : \exists \tau \succeq \sigma\ \Phi^\tau_e(m)\converge \}$: an $m \in A$ converges with a prefix of $G$ extending $\sigma$, and an $m$ in the right-hand side is in $A$ since $\sigma$ avoids $W_\varphi$. The right-hand side is $\Sigma^0_1$, contradicting the hypothesis. So $\varphi$ does not define $A$ with the parameter $G$.
:::
::::

## Notes and references

The definability of the forcing relation for Cohen forcing, and its consequences for the jumps of $n$-generic sets, are due to Jockusch (1980), building on Feferman (1965); Dzhafarov and Mummert present them as Lemma 7.5.10 and Propositions 7.5.11 and 7.5.12. The equivalence between the two definitions of $n$-genericity is credited by Downey and Hirschfeldt to Jockusch and Posner (Section 2.24). The preservation theorem and its corollary are stated for Cohen forcing in the chapter on Cohen genericity of Monin and Patey, and for every notion of forcing with a suitable forcing question in their chapter *Effective forcing*; :ref{to="effective-forcing/forcing-question"} gives the general form.

- S. Feferman, *Some applications of the notions of forcing and generic sets*, Fundamenta Mathematicae 56 (1965), 325–345.
- C. G. Jockusch, *Degrees of generic sets*, in *Recursion Theory: its Generalisations and Applications*, London Mathematical Society Lecture Note Series 45, Cambridge University Press, 1980, 110–139.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 2.24.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 7.5.
- B. Monin and L. Patey, *Computability theory*, chapters *Cohen genericity* and *Effective forcing*.

:::::exercises
::::exercise{#ex-cohen-not-high difficulty=2 objective="Apply the preservation theorem for Cohen forcing to the double jump."}
Let $G$ be sufficiently generic for Cohen forcing. Show that the complement of $\emptyset''$ is not $\Sigma^0_2(G)$, that $G$ is not high, and that $\emptyset' \not\leq_T G$.

:::solution
The complement of $\emptyset''$ is not $\Sigma^0_2$: otherwise $\emptyset''$ would be $\Delta^0_2$, hence computable in $\emptyset'$ by Post's theorem, which contradicts :ref{#cor-hierarchy-strict}. By :ref{#thm-cohen-preservation} with $n = 2$, it is not $\Sigma^0_2(G)$. If $G$ were high, $\emptyset'' \leq_T G'$, and $\emptyset''$ and its complement would be $\Delta^0_2(G)$ by Post's theorem relativized; so $G$ is not high. Finally $\emptyset' \not\leq_T G$ is :ref{#cor-cohen-jump-cone} with $n = 0$ and $A = \emptyset'$.
:::
::::

::::exercise{#ex-oracle-free-forcing difficulty=2 objective="Show that the bounds of the definability theorem for Cohen forcing cannot be improved."}
Call a sentence **oracle-free** if none of its functionals queries the oracle, so that its truth does not depend on the set interpreting $G$.

1. Show that for every notion of forcing, a condition forces an oracle-free sentence if and only if the sentence is true.
2. Let $n \geq 1$ and let $A \subseteq \nat$ be $\Sigma^0_n$. Show that there is a computable sequence $(\varphi_a)$ of oracle-free $\Sigma^0_n$ sentences such that $a \in A$ if and only if the empty string forces $\varphi_a$, for Cohen forcing.
3. Deduce that the relation of :ref{#thm-cohen-forcing-definable}, for $\Sigma^0_n$ sentences, is not $\Pi^0_n$, and for $\Pi^0_n$ sentences, is not $\Sigma^0_n$.

:::solution
1. By induction on the level, for all conditions at once. At level $1$, $c$ forces $\varphi$ if every member satisfies it; all sets agree on $\varphi$, and $[c]$ is non-empty, so this holds if and only if $\varphi$ is true. If $\varphi = \exists y\ \psi(y)$, then $c \Vdash \varphi$ if and only if $c \Vdash \psi(m)$ for some $m$, if and only if $\psi(m)$ is true for some $m$, by the induction hypothesis. If $\varphi = \forall y\ \psi(y)$, then $c \Vdash \varphi$ if and only if there are no $d \leq c$ and $m$ with $d \Vdash \neg \psi(m)$. By the induction hypothesis, $d \Vdash \neg \psi(m)$ if and only if $\neg \psi(m)$ is true, whatever $d$ is, and $c$ itself is an extension of $c$. So $c \Vdash \varphi$ if and only if $\neg \psi(m)$ is false for every $m$, that is, $\varphi$ is true.
2. By :ref{#def-arithmetic-hierarchy}, there is a computable relation $R$ with $a \in A \iff \exists y_1\ \forall y_2 \cdots Q y_n\ R(a, y_1, \dots, y_n)$. If $Q = \exists$, let $\Phi_e$ be the functional that, on input $(a, y_1, \dots, y_{n-1})$, ignores its oracle and searches for $y_n$ with $R(a, \vec y)$; then $\exists y_n\ R(a, \vec y)$ holds if and only if $\Phi_e(a, y_1, \dots, y_{n-1})\converge$, a $\Sigma^0_1$ formula. If $Q = \forall$, let $\Phi_e$ search for $y_n$ with $\neg R(a, \vec y)$; then $\forall y_n\ R(a, \vec y)$ holds if and only if $\Phi_e(a, y_1, \dots, y_{n-1})\diverge$, a $\Pi^0_1$ formula. Adding the quantifiers $\exists y_1\ \forall y_2 \cdots$ over $y_1, \dots, y_{n-1}$ gives a $\Sigma^0_n$ formula $\varphi(x)$ in the sense of :ref{#def-forcing-formula}, oracle-free, and $\varphi_a = \varphi(a)$ is true if and only if $a \in A$. By item 1, the empty string forces $\varphi_a$ if and only if $a \in A$. The code of $\varphi_a$ is computed from $a$.
3. Take for $A$ a $\Sigma^0_n$ set that is not $\Pi^0_n$, which exists by :ref{#cor-hierarchy-strict}. If the relation "$\sigma \Vdash \varphi$" on $\Sigma^0_n$ sentences were $\Pi^0_n$, then $A = \{ a : \varepsilon \Vdash \varphi_a \}$, the preimage of a $\Pi^0_n$ relation by a computable function, would be $\Pi^0_n$. For $\Pi^0_n$ sentences, apply item 2 to the complement of a $\Pi^0_n$ set that is not $\Sigma^0_n$: its negations $\neg \varphi_a$ are oracle-free $\Pi^0_n$ sentences, true exactly on that set.
:::
::::

::::exercise{#ex-cohen-jump-inversion-n difficulty=3 objective="Code a set into an $n$-generic set while deciding the sentences of level $n$, to invert the $n$-th jump."}
Let $n \geq 1$ and let $A$ be a set with $\emptyset^{(n)} \leq_T A$. Show that there is an $n$-generic set $G$ with $G^{(n)} \equiv_T G \oplus \emptyset^{(n)} \equiv_T A$. For $n = 1$ this is Friedberg's jump inversion theorem, in the form proved in the course on Cohen genericity.

:::solution
Fix a computable enumeration $\varphi_0, \varphi_1, \dots$ of the $\Sigma^0_k$ sentences, $1 \leq k \leq n$. Build strings $\sigma_0 \preceq \sigma_1 \preceq \cdots$ with $\sigma_0 = \varepsilon$.

- *Step $2s$.* Let $\varphi_s$ be $\Sigma^0_k$. The relation "some $\tau \succeq \sigma$ forces $\varphi$" is $\Sigma^0_k$, by :ref{#thm-cohen-forcing-definable} and the decidability of $\succeq$, so $\emptyset^{(n)}$ decides it, uniformly. If it holds for $\sigma_{2s}$ and $\varphi_s$, let $\sigma_{2s+1}$ be the first $\tau \succeq \sigma_{2s}$, in a fixed enumeration of the strings, that forces $\varphi_s$, each test being decided by $\emptyset^{(n)}$. Otherwise let $\sigma_{2s+1} = \sigma_{2s}$, which forces $\neg \varphi_s$ by :ref{#prop-forcing-basic}, item 3.
- *Step $2s + 1$.* Let $\sigma_{2s+2} = \sigma_{2s+1}\, A(s)$.

Let $G = \bigcup_s \sigma_s$, a set since $|\sigma_{2s+2}| \geq s + 1$. Its filter of prefixes meets every $S_k$ and every $D_{\varphi_s}$, and $D_\psi = D_{\neg \psi}$, so it is $n$-generic in the sense of :ref{#def-n-generic-notion}, and $G$ is $n$-generic by :ref{#thm-cohen-n-generic}.

The construction is computable in $A \oplus \emptyset^{(n)} \equiv_T A$, so $G \leq_T A$, and $G \oplus \emptyset^{(n)} \leq_T A$. Conversely, $G \oplus \emptyset^{(n)}$ computes the sequence $(\sigma_s)$: step $2s$ uses only $\emptyset^{(n)}$, and at step $2s + 1$, $A(s) = G(|\sigma_{2s+1}|)$, so $\sigma_{2s+2} = G \uh (|\sigma_{2s+1}| + 1)$. This also computes $A$, so $A \leq_T G \oplus \emptyset^{(n)}$. Finally $G^{(n)} \leq_T G \oplus \emptyset^{(n)}$ by :ref{#cor-cohen-jumps}, and $G \oplus \emptyset^{(n)} \leq_T G^{(n)}$ for every set. So $G^{(n)} \equiv_T G \oplus \emptyset^{(n)} \equiv_T A$.
:::
::::

::::exercise{#ex-preservation-quantifiers difficulty=1 objective="See why the family of dense sets in the preservation theorem must depend on the set to be preserved."}
Show that a set $G$ has the property "every set that is not c.e. is not c.e. relative to $G$" if and only if $G$ is computable. Explain why this does not contradict :ref{#thm-cohen-preservation} for $n = 1$.

:::solution
If $G$ is computable, the $G$-c.e. sets are the c.e. sets, and the property holds. If $G$ is not computable, then $G$ or its complement is not c.e., since a set that is c.e. and co-c.e. is computable. Both $G$ and its complement are computable in $G$, hence c.e. relative to $G$; so one of them is a set that is not c.e. and becomes c.e. relative to $G$.

The theorem says: for each set $A$ that is not $\Sigma^0_1$, there is a countable family $\mathcal D_A$ of dense sets, the sets $E_\varphi$ of its proof, which depend on $A$, such that $A$ is not $\Sigma^0_1(G)$ for every $\mathcal D_A$-generic set $G$. The quantifiers are in the order "for every $A$, for every sufficiently generic $G$". The property of the exercise would require a set generic for the families $\mathcal D_A$ of all the uncountably many sets $A$ that are not c.e., and by the first part only computable sets have it, while sufficiently generic sets are not computable.
:::
::::

::::exercise{#ex-cohen-arithmetical-preservation difficulty=1 objective="Combine countably many applications of the preservation theorem."}
Let $A$ be a set that is not arithmetical. Show that for every sufficiently generic set $G$ for Cohen forcing, $A$ is not arithmetical relative to $G$, that is, $A$ is not $\Sigma^0_n(G)$ for any $n$.

:::solution
For each $n \geq 1$, $A$ is not $\Sigma^0_n$, so :ref{#thm-cohen-preservation} gives a countable family $\mathcal D_n$ of dense sets such that $A$ is not $\Sigma^0_n(G)$ for every $\mathcal D_n$-generic set $G$. The family $\bigcup_n \mathcal D_n$ is countable, and a set generic for it is $\mathcal D_n$-generic for every $n$, so $A$ is not $\Sigma^0_n(G)$ for any $n$.
:::
::::
:::::
