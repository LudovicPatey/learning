---
title: The forcing question as a method
summary: The three-case argument behind every proof of cone avoidance; the forcing question as a dividing line between conditions; forcing questions whose answers are Σ⁰₁ relative to the condition, and the cone avoidance theorem for them.
duration: 40
prerequisites: [avoidance-properties, effective-forcing/mathias-forcing]
---

The proofs of cone avoidance met so far share one argument. For Cohen forcing (:ref{#thm-cone-avoidance}), for the construction of a high set avoiding a cone (:ref{#thm-high-cone-avoidance}), for Mathias forcing and cohesiveness (:ref{#thm-coh-cone-avoidance}), and in the abstract form of :ref{#cor-question-jump-cone}, a condition $c$ and a functional $\Phi_e$ being given, one considers the set $U$ of pairs $(x, v)$ such that "$\Phi^G_e(x)$ converges to $v$" can be forced below $c$, and distinguishes three cases.

1. $U$ contains a wrong pair $(x, 1 - C(x))$: an extension forces $\Phi^G_e(x) \neq C(x)$ by convergence to the wrong value.
2. $U$ misses a right pair $(x, C(x))$: an extension forces that $\Phi^G_e(x)$ does not converge to $C(x)$.
3. Otherwise $U$ is the graph of $C$, so $C$ is as simple as $U$, which contradicts the hypothesis on $C$.

We call it the **three-case argument**. The first two cases are about forcing and hold for every notion of forcing; only the third depends on the complexity of $U$. This lesson isolates the part that varies, the **forcing question**, in a form adapted to problems, where the complexity of $U$ depends on the condition. The next lesson applies it to strong cone avoidance.

Throughout, a set $Z$ is fixed, and formulas are built with functionals of the oracle $Z \oplus G$ (:ref{#ex-forcing-formulas}, item 4). For a functional $\Phi_e$, a number $x$ and a value $v$, "$\Phi^{Z \oplus G}_e(x)\converge = v$" is a $\Sigma^0_1$ sentence, as "$\Phi^G_e(m)\converge < k$" in :ref{to="effective-forcing/compactness-merging"}: it is $\Phi^{Z \oplus G}_{a}(x, v)\converge$ for an index $a$ computable from $e$. Its negation says that $\Phi^{Z \oplus G}_e(x)$ diverges or converges to another value.

## The forcing question as a dividing line

Recall that a forcing question (:ref{#def-forcing-question}) answers, for a condition $c$ and a sentence $\varphi$, whether an extension forcing $\varphi$ or an extension forcing $\neg \varphi$ is to be sought: a positive answer guarantees the first, a negative answer the second. For a fixed $\Sigma^0_1$ sentence $\varphi$, the conditions fall into three classes: those forcing $\varphi$, those forcing $\neg \varphi$, and those forcing neither, which have extensions of both kinds (by :ref{#prop-forcing-basic}, item 3, a condition none of whose extensions forces $\varphi$ forces $\neg \varphi$). On the first class a forcing question must answer yes, on the second it must answer no; on the third it may answer either way.

:::figure[A forcing question as a dividing line, for a fixed $\Sigma^0_1$ sentence $\varphi$. A condition forcing $\varphi$ must get the answer yes, and a condition forcing $\neg \varphi$ the answer no; on the conditions forcing neither, the question chooses. The question of Jockusch–Soare forcing (:ref{#thm-tree-question}) answers yes only when $c$ already forces $\varphi$; the question of Cohen forcing (:ref{#ex-cohen-question}) answers yes as soon as some extension forces $\varphi$. Both positions are legitimate; each notion of forcing chooses the one with the right definability.]
<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="The conditions are divided into those forcing phi, those forcing its negation, and those deciding neither; the Jockusch-Soare question answers yes only on the first part, the Cohen question on the first two parts"><defs><marker id="av-dl-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><rect x="40" y="70" width="160" height="36" class="cell head-cell"/><rect x="200" y="70" width="200" height="36" class="cell"/><rect x="400" y="70" width="160" height="36" class="state"/><text x="120.0" y="93" text-anchor="middle" class="label">c ⊩ φ</text><text x="300.0" y="93" text-anchor="middle" class="label">c forces neither φ nor ¬φ</text><text x="480.0" y="93" text-anchor="middle" class="label">c ⊩ ¬φ</text><line x1="200" y1="48" x2="200" y2="128" class="ink-stroke" stroke-width="1.4" stroke-dasharray="5 4"/><text x="200" y="38" text-anchor="middle" class="label">Jockusch–Soare question</text><line x1="400" y1="48" x2="400" y2="128" class="ink-stroke" stroke-width="1.4" stroke-dasharray="5 4"/><text x="400" y="38" text-anchor="middle" class="label">Cohen question</text><line x1="40" y1="156" x2="200" y2="156" class="accent-stroke" stroke-width="2" marker-start="url(#av-dl-arr)" marker-end="url(#av-dl-arr)"/><text x="120.0" y="149" text-anchor="middle" class="label">Jockusch–Soare: yes</text><text x="380.0" y="149" text-anchor="middle" class="label muted">no</text><line x1="40" y1="196" x2="400" y2="196" class="accent-stroke" stroke-width="2" marker-start="url(#av-dl-arr)" marker-end="url(#av-dl-arr)"/><text x="220.0" y="189" text-anchor="middle" class="label">Cohen: yes</text><text x="480.0" y="189" text-anchor="middle" class="label muted">no</text><text x="300" y="228" text-anchor="middle" class="label">conditions, for a fixed Σ⁰₁ sentence φ</text></svg>
:::

The two extreme positions correspond to two definitions. "Some extension of $c$ forces $\varphi$" is always a forcing question, but its complexity is that of searching through the extensions. "The condition $c$ forces $\varphi$" has the complexity of the forcing relation, and is a forcing question only when every condition forcing neither $\varphi$ nor $\neg \varphi$ can be extended to force $\neg \varphi$ (second exercise). For Jockusch–Soare forcing the first definition is $\Sigma^0_2$: an extension forcing a convergence exists as soon as one member makes the computation converge, and membership is $\Pi^0_1$. The second is $\Sigma^0_1$ by compactness: a $\Pi^0_1$ class forces a convergence if and only if all the nodes of some level of its tree make the computation converge. This is the first instance of a recurring technique, the **over-approximation**: when the natural question is too complex, one asks a question with a stronger positive answer, chosen so that compactness brings it down to $\Sigma^0_1$. The Dzhafarov–Jockusch argument (:ref{#thm-dj-cone-avoidance}) is the second: it asks about all partitions of $\nat$ instead of the given one.

## Questions relative to the condition

In applications to problems, the conditions carry infinite objects, such as the reservoirs of Mathias conditions, and the answers to the question are computable from these objects, not computable outright. What the third case needs is that each condition comes with an oracle that is weak in the relevant sense.

:::definition{#def-question-local}
Let $\mathcal M$ be a class of sets. A forcing question for $\Sigma^0_1$ sentences is **$\Sigma^0_1(\mathcal M)$-preserving** if for every condition $c$ there is $X \in \mathcal M$ such that, for every $\Sigma^0_1$ formula $\varphi(\vec x)$, the relation $\{ \vec m : c \mathrel{?{\vdash}} \varphi(\vec m) \}$ is $\Sigma^0_1(X)$.
:::

For $\mathcal M = \{ \emptyset \}$ this is $\Sigma^0_1$-preservation (:ref{#def-forcing-question}). Two other cases are used in the next lessons: computable Mathias forcing relative to $Z$, with $\mathcal M = \{ Z \oplus X : X \text{ a } Z\text{-computable reservoir} \}$, which consists of sets computable in $Z$; and Mathias forcing whose reservoirs $X$ satisfy $C \not\leq_T Z \oplus X$, with $\mathcal M$ the class of these sets $Z \oplus X$.

:::theorem{#thm-local-cone-avoidance}
Let $\mathbb P$ be a notion of forcing with a $\Sigma^0_1(\mathcal M)$-preserving forcing question, and let $C$ be a set that is computable in no member of $\mathcal M$. For every sufficiently generic set $G$, $C \not\leq_T Z \oplus G$.
:::

:::proof{of=thm-local-cone-avoidance}
For each $e$, let $E_e$ be the set of conditions $d$ for which there is $x$ such that $d \Vdash \Phi^{Z \oplus G}_e(x)\converge = 1 - C(x)$ or $d \Vdash \neg (\Phi^{Z \oplus G}_e(x)\converge = C(x))$. Every member of a condition of $E_e$ satisfies $\Phi^{Z \oplus G}_e \neq C$, since forcing at level $1$ means truth on all members. We show that $E_e$ is dense.

Let $c$ be a condition, and $X \in \mathcal M$ as in :ref{#def-question-local}. The set
$$
U = \{ (x, v) \in \nat \times \{ 0, 1 \} : c \mathrel{?{\vdash}} \Phi^{Z \oplus G}_e(x)\converge = v \}
$$
is $\Sigma^0_1(X)$.

1. If $(x, 1 - C(x)) \in U$ for some $x$, property 1 of the question gives an extension forcing $\Phi^{Z \oplus G}_e(x)\converge = 1 - C(x)$.
2. If $(x, C(x)) \notin U$ for some $x$, property 2 gives an extension forcing $\neg (\Phi^{Z \oplus G}_e(x)\converge = C(x))$.
3. Otherwise, for every $x$, $(x, C(x)) \in U$ and $(x, 1 - C(x)) \notin U$. Then $C(x)$ is the unique $v < 2$ with $(x, v) \in U$, found by enumerating $U$ with oracle $X$; so $C \leq_T X$, which is excluded.

Let $G$ be generic for the sets $E_e$ (and the sets $S_n$ of :ref{#lem-generic-set}). For each $e$, the filter contains a condition of $E_e$, of which $G$ is a member (:ref{#lem-generic-set}); so $\Phi^{Z \oplus G}_e \neq C$ for every $e$.
:::

The proof is the one of :ref{#thm-question-preservation} at level $1$, with two differences: the oracle $X$ depends on the condition, and the set compared with the $\Sigma^0_1(X)$ set $U$ is the graph of $C$, so that the hypothesis is on $C$ rather than on $C$ or its complement. Since the conclusion holds for all $e$ at once, the theorem gives more than cone avoidance for one set: the same family of dense sets can be built for countably many sets $C$ at once, and every sufficiently generic set avoids all their cones.

For Cohen forcing relative to $Z$ and $\mathcal M = \{ Z \}$, the set $U$ is the set of pairs $(x, v)$ such that $\Phi^{Z \oplus \tau}_e(x)\converge = v$ for some $\tau \succeq \sigma$, and the theorem is :ref{#thm-cone-avoidance} relativized. The hypothesis on $\mathcal M$ cannot be dropped, as the following example shows.

:::example{#ex-coding-reservoir}
Let $C$ be a non-computable set, and let $X_C$ be the set of the codes of the prefixes $C \uh n$, $n \in \nat$, for a computable coding of strings by numbers. Every infinite subset $H$ of $X_C$ computes $C$: to compute $C \uh n$, search for an element of $H$ coding a string of length at least $n$, which exists since only finitely many numbers code shorter strings, and take its prefix of length $n$. Consider Mathias forcing with arbitrary infinite reservoirs, and the question of :ref{#prop-mathias-question} relative to $Z = \emptyset$. As in the next lesson, it is a forcing question, and its answers at $(\sigma, X)$ are $\Sigma^0_1(X)$; so it is $\Sigma^0_1(\mathcal M)$-preserving for the class $\mathcal M$ of all sets. The members of the condition $(\varepsilon, X_C)$ are the subsets of $X_C$, and every sufficiently generic set whose filter contains this condition is an infinite subset of $X_C$, hence computes $C$. The proof of :ref{#thm-local-cone-avoidance} breaks down in case 3 at this condition: for the index $e$ of the reduction just described, which only reads finite subsets of $X_C$ and never outputs a wrong value, the set $U$ is the graph of $C$, and it is $\Sigma^0_1(X_C)$ with $C \leq_T X_C$.
:::

This is why the constructions of the following lessons restrict the reservoirs to a class of sets that do not compute $C$: computable in $Z$, avoiding the cone above $C$ together with $Z$, or members of a Scott ideal that does not contain $C$.

:::quiz[the three-case argument]
In the proof of :ref{#thm-local-cone-avoidance}, which hypothesis does each case use?

- [x] Cases 1 and 2 use only the two properties of a forcing question; case 3 uses that $U$ is $\Sigma^0_1(X)$ for some $X \in \mathcal M$, and that $C$ is not computable in $X$.
- [ ] Case 1 uses that $C$ is not computable.

  Case 1 uses property 1 of the question; it holds whatever $C$ is.
- [ ] Case 3 uses property 2 of the question.

  Case 3 is a contradiction obtained from the complexity of $U$; no extension is built.

---

Why does the argument compare $U$ with the graph of $C$ rather than with $C$ itself?

- [x] Because a set whose graph is $\Sigma^0_1(X)$ is computable in $X$, whereas a set that is $\Sigma^0_1(X)$ need not be; the graph contains both the positive and the negative information about $C$.
- [ ] Because $\Phi_e$ may take values other than $0$ and $1$.

  Values other than $0$ and $1$ never belong to $U$, which only contains pairs with $v < 2$.
- [ ] Because $U$ is a set of pairs.

  Pairs can be coded by numbers, so this is only a matter of presentation; what matters is that $U$ records both values, and a $\Sigma^0_1(X)$ set of numbers compared with $C$ itself is the subject of :ref{to="avoidance/non-sigma1-definitions"}.
:::

## Exercises

::::exercise{difficulty=1}
Show that every forcing question satisfies: if $c \Vdash \varphi$ then $c \mathrel{?{\vdash}} \varphi$, and if $c \Vdash \neg \varphi$ then $c \mathrel{?{\nvdash}} \varphi$.

:::solution
If $c \Vdash \varphi$ and $c \mathrel{?{\nvdash}} \varphi$, property 2 gives $d \leq c$ forcing $\neg \varphi$; but $d$ forces $\varphi$ by extension (:ref{#prop-forcing-basic}), contradicting consistency. The second statement is symmetric, with property 1.
:::
::::

::::exercise{#exr-question-converse difficulty=2}
For Cohen forcing, let $\sigma \mathrel{R} \varphi$ hold if $\sigma \Vdash \varphi$, for $\Sigma^0_1$ sentences $\varphi$. Show that $R$ satisfies the two properties of the previous exercise, but is not a forcing question. Show that $R$ is a forcing question for Jockusch–Soare forcing at level $1$, and explain the difference.

:::solution
The two properties hold since forcing is consistent. Let $\varphi$ say that $G$ has an element $n \geq |\sigma|$: it is $\Phi^G_a\converge$ for the functional searching for such an element. The condition $\sigma$ does not force it, since $\sigma 0 0 \cdots$ is a member. But no extension $\tau$ of $\sigma$ forces $\neg \varphi$, since $\tau 1 1 \cdots$ is a member of $\tau$. So property 2 fails. For Jockusch–Soare forcing, if $\mathcal P$ does not force $\Phi^G_e(\vec m)\converge$, some member makes it diverge, and $\mathcal P \cap \{ X : \Phi^X_e(\vec m)\diverge \}$ is a non-empty $\Pi^0_1$ class forcing the divergence. The difference is that a $\Pi^0_1$ class can be cut down to the members satisfying a $\Pi^0_1$ property, while a Cohen condition cannot exclude a single member without fixing a longer string.
:::
::::

## Notes and references

The three-case argument and the forcing question as its abstraction follow the chapter *Cone avoidance* of Patey's monograph (sections *First examples* and *Forcing question*), where the dividing line between conditions is drawn as in the figure; the forcing question was introduced by Monin and Patey (2019, Lemma 2.4 for the abstract cone avoidance theorem). The monograph states as an exercise that the two properties of the first exercise characterize forcing questions; :ref{#exr-question-converse} shows that they are necessary but not sufficient in the framework of this course. :ref{#def-question-local} is introduced here to state in one theorem the variants with reservoirs computable in $Z$, avoiding a cone, or belonging to a Scott ideal. The example of reservoirs that code $C$ shows why the class $\mathcal M$ must avoid the cone; it is the reason for the restrictions on reservoirs in all later constructions.

- B. Monin and L. Patey, *Pigeons do not jump high*, Advances in Mathematics 352 (2019), 1066–1095; arXiv:1803.09771.
- L. Patey, *Lowness and avoidance*, chapter *Cone avoidance*, sections *First examples* and *Forcing question*.
