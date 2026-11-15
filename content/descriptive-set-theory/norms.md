---
title: Π¹₁ norms and stage comparison
summary: The rank of the normal-form tree as a stage at which an element enters a Π¹₁ set; comparison of ranks by strictly monotone maps; the stage comparison relations are Π¹₁, so the stage map is a Π¹₁ norm and the Π¹₁ sets have the prewellordering property.
duration: 45
prerequisites: [hyperarithmetic/kleene-theorem]
---

A c.e. set is enumerated in stages $0, 1, 2, \dots$, and two elements can be compared by the stage at which they appear. Many properties of c.e. sets follow from this. For instance, two c.e. sets $A$ and $B$ can be **reduced** to disjoint c.e. sets $A' \subseteq A$ and $B' \subseteq B$ with the same union: enumerate both sets simultaneously and put each element in the set where it appears first. The $\Pi^1_1$ sets are enumerated in the same way, along the computable ordinals instead of the natural numbers. By the normal form theorem, $n$ belongs to a $\Pi^1_1$ set exactly when a certain computable tree $T_n$ is well-founded, and the rank of $T_n$ measures how long it takes to see this; it is the **stage** at which $n$ enters the set.

The difficulty is that a stage is an ordinal, not a number, and that "$T_n$ has rank at most $\alpha$" is not an arithmetic statement. This lesson shows that two stages can nevertheless be compared in a $\Pi^1_1$ way, provided one of them is known to be an ordinal. The technique, **stage comparison**, is the main tool of the course: the next lesson uses it to prove the reduction property of $\Pi^1_1$ sets, the following one to select witnesses, and the course on higher randomness uses it to build universal tests.

## Ranks and strictly monotone maps

Throughout, trees are subsets of $\nat^{<\nat}$ closed under prefixes, and we only consider trees containing the empty sequence. Adding the empty sequence to a tree does not change whether it is well-founded, so the trees $T_n$ of the normal form theorem (:ref{#thm-pi11-normal-form}) may be assumed to contain it. For a tree $T$, let $\rho(T) = \mathrm{rk}(T)$ if $T$ is well-founded (:ref{#def-tree-rank}), and $\rho(T) = \infty$ otherwise, with $\alpha < \infty$ for every ordinal $\alpha$. For $\sigma \in T$, write $T_\sigma = \{ \tau : \sigma \tau \in T \}$ for the subtree above $\sigma$, and $\mathrm{rk}_T(\sigma) = \mathrm{rk}(T_\sigma)$ when it is well-founded. If $\sigma \subsetneq \tau$ are in a well-founded tree $T$, then $\mathrm{rk}_T(\tau) < \mathrm{rk}_T(\sigma)$, by induction on the length of $\tau$ from the definition of the rank. For example, the tree of all sequences of length at most $k$ has rank $k$, and a node of length $i$ in it has rank $k - i$.

To compare two ranks without computing them, one compares the trees directly. The rank of a well-founded tree measures how long one can keep descending in it, going from a node to one of its extensions, with the remaining ranks decreasing at each step. A tree $S$ has rank at most that of $T$ when every descent in $S$ can be imitated by a descent in $T$, step by step. A map that imitates descents is the following.

A map $g : S \to T$ between trees is **strictly monotone** if $\sigma \subsetneq \tau$ implies $g(\sigma) \subsetneq g(\tau)$.

The word "strictly" carries all the information: a map with $\sigma \subseteq \tau \Rightarrow g(\sigma) \subseteq g(\tau)$ always exists, for instance the map sending every node to the empty sequence.

:::lemma{#lem-rank-comparison}
For trees $S$ and $T$, $\rho(S) \leq \rho(T)$ if and only if there is a strictly monotone map $g : S \to T$.
:::

:::proof{of=lem-rank-comparison}
($\Leftarrow$) Let $g$ be strictly monotone. If $T$ is ill-founded, $\rho(T) = \infty$ and there is nothing to prove. Suppose $T$ well-founded. Then $S$ is well-founded: a path $f$ through $S$ would give a strictly increasing sequence $g(f \uh 0) \subsetneq g(f \uh 1) \subsetneq \cdots$ in $T$, hence a path. We show $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma))$ for every $\sigma \in S$, by induction along the well-founded relation "$\tau$ properly extends $\sigma$" on $S$. For every $n$ with $\sigma n \in S$, the induction hypothesis and $g(\sigma) \subsetneq g(\sigma n)$ give $\mathrm{rk}_S(\sigma n) \leq \mathrm{rk}_T(g(\sigma n)) < \mathrm{rk}_T(g(\sigma))$. Taking the supremum of $\mathrm{rk}_S(\sigma n) + 1$ gives $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma))$. For $\sigma$ empty, $\rho(S) \leq \mathrm{rk}_T(g(\emptyset)) \leq \rho(T)$.

($\Rightarrow$) If $T$ has a path $h$, let $g(\sigma) = h \uh |\sigma|$. Otherwise $T$ is well-founded, and so is $S$, since $\rho(S) \leq \rho(T) < \infty$. Define $g(\sigma)$ by induction on $|\sigma|$, maintaining $\mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma))$. Let $g(\emptyset) = \emptyset$. If $g(\sigma)$ is defined and $\sigma n \in S$, then
$$
\mathrm{rk}_S(\sigma n) < \mathrm{rk}_S(\sigma) \leq \mathrm{rk}_T(g(\sigma)) = \sup \{ \mathrm{rk}_T(g(\sigma) m) + 1 : g(\sigma) m \in T \},
$$
so there is $m$ with $g(\sigma) m \in T$ and $\mathrm{rk}_S(\sigma n) \leq \mathrm{rk}_T(g(\sigma) m)$; let $g(\sigma n) = g(\sigma) m$ for the least such $m$. The map is strictly monotone, since each step extends the image by one element.
:::

:::figure[A strictly monotone map $g : S \to T$, as in :ref{#lem-rank-comparison}. Each node is labeled with its rank. In general a strictly monotone map need not preserve lengths; the one drawn here does, like the map built in the proof of the direction ($\Rightarrow$). Each node of $S$ has rank at most that of its image.]
<svg class="fig" viewBox="0 0 600 300" width="600" role="img" aria-label="Two trees S and T with the ranks of their nodes, and a strictly monotone map from S to T drawn as dashed arrows"><defs><marker id="dst-rank-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="110" y1="40" x2="60" y2="110" class="ink-stroke" stroke-width="1.4"/><line x1="110" y1="40" x2="160" y2="110" class="ink-stroke" stroke-width="1.4"/><line x1="60" y1="110" x2="60" y2="180" class="ink-stroke" stroke-width="1.4"/><line x1="430" y1="40" x2="380" y2="110" class="ink-stroke" stroke-width="1.4"/><line x1="430" y1="40" x2="500" y2="110" class="ink-stroke" stroke-width="1.4"/><line x1="380" y1="110" x2="380" y2="180" class="ink-stroke" stroke-width="1.4"/><line x1="380" y1="180" x2="380" y2="250" class="ink-stroke" stroke-width="1.4"/><path d="M119,40 Q270.0,0.0 420,40" class="accent-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#dst-rank-arrow)"/><path d="M69,110 Q220.0,144.0 370,110" class="accent-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#dst-rank-arrow)"/><path d="M69,180 Q220.0,210.0 370,180" class="accent-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#dst-rank-arrow)"/><path d="M169,110 Q330.0,84.0 490,110" class="accent-stroke" stroke-width="1.2" stroke-dasharray="4 3" marker-end="url(#dst-rank-arrow)"/><circle cx="110" cy="40" r="6" class="node"/><text x="99" y="44" text-anchor="end" class="mrm" font-size="12">2</text><circle cx="60" cy="110" r="6" class="node"/><text x="49" y="114" text-anchor="end" class="mrm" font-size="12">1</text><circle cx="160" cy="110" r="6" class="node"/><text x="149" y="114" text-anchor="end" class="mrm" font-size="12">0</text><circle cx="60" cy="180" r="6" class="node"/><text x="49" y="184" text-anchor="end" class="mrm" font-size="12">0</text><circle cx="430" cy="40" r="6" class="node"/><text x="441" y="44" text-anchor="start" class="mrm" font-size="12">3</text><circle cx="380" cy="110" r="6" class="node"/><text x="391" y="114" text-anchor="start" class="mrm" font-size="12">2</text><circle cx="500" cy="110" r="6" class="node"/><text x="511" y="114" text-anchor="start" class="mrm" font-size="12">0</text><circle cx="380" cy="180" r="6" class="node"/><text x="391" y="184" text-anchor="start" class="mrm" font-size="12">1</text><circle cx="380" cy="250" r="6" class="node"/><text x="391" y="254" text-anchor="start" class="mrm" font-size="12">0</text><text x="110" y="20" text-anchor="middle" class="math" font-size="16">S</text><text x="430" y="20" text-anchor="middle" class="math" font-size="16">T</text><text x="270" y="50" text-anchor="middle" class="math" font-size="15">g</text><text x="20" y="286" class="label">numbers: the ranks of the nodes; ρ(S) = 2 ≤ ρ(T) = 3, and each node σ of S has rank at most that of g(σ)</text></svg>
:::

The existence of a strictly monotone map is expressed by an existential function quantifier followed by an arithmetic condition. So the relation $\rho(S) \leq \rho(T)$ between indices of computable trees is $\Sigma^1_1$. Strict comparison reduces to it, when the larger tree is well-founded:
$$
\text{if } T \text{ is well-founded:} \quad \rho(S) < \rho(T) \iff \exists n\ (\langle n \rangle \in T \wedge \rho(S) \leq \rho(T_{\langle n \rangle})),
$$
since $\rho(T)$ is the supremum of the ordinals $\rho(T_{\langle n \rangle}) + 1$. Without the hypothesis, the equivalence fails: if $S$ and $T$ are both ill-founded, a path of $T$ passes through some $\langle n \rangle$, so $T_{\langle n \rangle}$ is ill-founded and the right-hand side holds, while $\rho(S) < \rho(T)$ is the false inequality $\infty < \infty$.

## Stage comparison

Fix a $\Pi^1_1$ set $A$ and a uniformly computable sequence of trees $(T_n)$, containing the empty sequence, with $n \in A$ if and only if $T_n$ is well-founded.

:::definition{#def-pi11-stage}
The **stage** of $n$ with respect to $(T_n)$ is $\rho_n = \rho(T_n)$. The **stage comparison relations** are
$$
n \leq^* m \iff n \in A \wedge \rho_n \leq \rho_m, \qquad n <^* m \iff n \in A \wedge \rho_n < \rho_m.
$$
:::

For $n \in A$, the stage is a computable ordinal, since the Kleene–Brouwer ordering of $T_n$ is a computable well-ordering of type at least $\rho_n$ (:ref{#thm-kleene-brouwer}). For $n \notin A$, $\rho_n = \infty$. In words, $n \leq^* m$ says that $n$ has entered $A$, and that $m$ has not entered strictly before $n$; it does not require $m \in A$.

:::example{#ex-ce-stages}
Let $A$ be a c.e. set with a computable enumeration $(A_s)$, where $A_0 = \emptyset$, each $A_s$ is finite and $A_s \subseteq A_{s+1}$. Let $T_n = \{ \sigma \in \nat^{<\nat} : n \notin A_{|\sigma|} \}$. This is a tree containing the empty sequence, since the sets $A_s$ increase and $A_0 = \emptyset$, and it is computable uniformly in $n$. If $s$ is the least number with $n \in A_s$, then $T_n$ is the tree of sequences of length less than $s$, of rank $s - 1$. If $n \notin A$, then $T_n = \nat^{<\nat}$ is ill-founded. So the stage of $n$ is its stage of enumeration minus one, and the stage comparison relations compare enumeration stages: the notions of this lesson extend those of c.e. sets.
:::

The stages depend on the sequence $(T_n)$, not only on $A$. Replacing $T_n$ by $\{ \emptyset \} \cup \{ \langle 0 \rangle \sigma : \sigma \in T_n \}$ for even $n$ only, for instance, adds $1$ to the stages of the even numbers and can change the relative order of elements of $A$. The results below hold for every choice of the sequence.

The next theorem is the core of the lesson. To decide whether $n \leq^* m$, one needs a $\Pi^1_1$ formula. The lemma gives a $\Sigma^1_1$ formula for $\rho_n \leq \rho_m$, which has the wrong complexity. The way out is to write $\rho_n \leq \rho_m$ as the negation of $\rho_m < \rho_n$, which is $\Sigma^1_1$ by the display above, as long as $T_n$ is well-founded; and the well-foundedness of $T_n$ is exactly the $\Pi^1_1$ condition $n \in A$.

:::theorem{#thm-stage-comparison}
The relations
$$
n \leq^* m \iff n \in A \wedge \rho_n \leq \rho_m, \qquad n <^* m \iff n \in A \wedge \rho_n < \rho_m
$$
are $\Pi^1_1$.
:::

:::proof{of=thm-stage-comparison}
If $n \in A$, then $T_n$ is well-founded, and $\rho_n \leq \rho_m$ holds if and only if $\rho_m < \rho_n$ fails, that is, by the display above, if and only if there is no $k$ with $\langle k \rangle \in T_n$ and $\rho_m \leq \rho((T_n)_{\langle k \rangle})$. So
$$
n \leq^* m \iff n \in A \wedge \neg \exists k\ \big(\langle k \rangle \in T_n \wedge \rho(T_m) \leq \rho((T_n)_{\langle k \rangle})\big),
$$
the conjunction of a $\Pi^1_1$ formula and the negation of a $\Sigma^1_1$ formula, by :ref{#lem-rank-comparison}. Similarly, $n <^* m$ if and only if $n \in A$ and $\rho(T_m) \leq \rho(T_n)$ fails.
:::

If $m \notin A$, then $\rho_m = \infty$, and every $n \in A$ satisfies $n <^* m$. This is the analogue of the fact that an element enumerated into a c.e. set comes before every element that is never enumerated.

:::quiz[stage comparison]
In the proof of :ref{#thm-stage-comparison}, why is $n \leq^* m$ written as the negation of $\rho_m < \rho_n$, rather than directly as "there is a strictly monotone map from $T_n$ to $T_m$"?

- [x] Because the existence of a map is $\Sigma^1_1$, while $n \leq^* m$ must be $\Pi^1_1$; the negation of the $\Sigma^1_1$ relation $\rho_m < \rho_n$, available since $T_n$ is well-founded, has the right complexity.
- [ ] Because the map does not exist when $T_m$ is ill-founded.

  It does: every tree maps strictly monotonically into an ill-founded tree.
- [ ] Because ranks cannot be compared by maps.

  :ref{#lem-rank-comparison} shows that they can.

---

Why is the hypothesis $n \in A$ part of the definition of $n \leq^* m$?

- [x] Because the formula for $\rho_m < \rho_n$ by the subtrees $(T_n)_{\langle k \rangle}$ is only correct when $T_n$ is well-founded; when both trees are ill-founded, it would wrongly assert $\infty < \infty$.

  Without the hypothesis, the relation $\rho_n \leq \rho_m$ is not $\Pi^1_1$ in general: for a fixed $n_0 \notin A$, the set $\{ m : \rho_{n_0} \leq \rho_m \}$ is $\overline A$, which is $\Pi^1_1$ only if $A$ is $\Delta^1_1$.
- [ ] Because $\rho_n$ is not defined for $n \notin A$.

  It is defined, and equal to $\infty$.
- [ ] To make the relation $\Sigma^1_1$.

  Membership in $A$ is $\Pi^1_1$; it keeps the relation $\Pi^1_1$.
:::

Once an element $n \in A$ is fixed, the comparison with $n$ also has a $\Sigma^1_1$ definition: the elements that enter $A$ no later than $n$ form a hyperarithmetic set.

:::corollary{#cor-initial-segments}
For every $n \in A$, the set $\{ m : \rho_m \leq \rho_n \}$ is $\Delta^1_1$, hence hyperarithmetic, and included in $A$.
:::

:::proof{of=cor-initial-segments}
It is $\{ m : m \leq^* n \}$, which is $\Pi^1_1$ by :ref{#thm-stage-comparison}; and it is $\{ m : \rho(T_m) \leq \rho(T_n) \}$, which is $\Sigma^1_1$ by :ref{#lem-rank-comparison}. Its members have $\rho_m \leq \rho_n < \infty$, so they belong to $A$. By Kleene's theorem (:ref{#thm-kleene-delta11}), it is hyperarithmetic.
:::

This is the first instance of a pattern that recurs in higher computability: a $\Pi^1_1$ property becomes $\Delta^1_1$ once the ordinals involved are bounded, as in the proof of Kleene's theorem (:ref{#thm-kleene-delta11}).

Moschovakis isolated the properties of the stage map in an abstract notion, which applies to other classes of sets.

:::definition{#def-pi11-norm}
A **norm** on a set $A \subseteq \nat$ is a map $\varphi$ from $A$ to the ordinals, extended by $\varphi(n) = \infty$ for $n \notin A$. It is a **$\Pi^1_1$ norm** if the relations $n \in A \wedge \varphi(n) \leq \varphi(m)$ and $n \in A \wedge \varphi(n) < \varphi(m)$ are $\Pi^1_1$. A class of sets has the **prewellordering property** if every set of the class has a norm whose relations are in the class.
:::

By :ref{#thm-stage-comparison}, the map $n \mapsto \rho_n$ is a $\Pi^1_1$ norm on $A$, for every sequence of trees given by the normal form: **the $\Pi^1_1$ sets have the prewellordering property**. The name comes from the relation $\varphi(n) \leq \varphi(m)$ on $A$, which is a prewellordering: a total preorder without infinite strictly descending sequences.

::::exercise{#ex-wo-norm difficulty=2 objective="Build a $\Pi^1_1$ norm on $\mathrm{WO}$ directly from embeddings of well-orderings, without the normal form theorem."}
For an index $e$ of a computable linear order, let $\varphi(e) = |L_e|$ if $e \in \mathrm{WO}$, and $\varphi(e) = \infty$ otherwise. Show that $\varphi$ is a $\Pi^1_1$ norm on $\mathrm{WO}$, without using the normal form theorem.

:::solution
Use two facts on well-orderings. A linear order $L$ that embeds into a well-ordering $W$ is a well-ordering, of type at most that of $W$: otherwise $W$ would be isomorphic to a proper initial segment of $L$, by the comparison theorem, and composing gives a strictly increasing map from $L$ into one of its proper initial segments $L_{<a}$, which sends $a$ below $a$, contradicting :ref{#lem-wo-rigid}. And a well-ordering of type at most $\gamma$ embeds into every well-ordering of type $\gamma$, by the comparison theorem (:ref{#thm-wo-comparison}). Let $e \in \mathrm{WO}$ and let $d$ be any number.

- $\varphi(d) < \varphi(e)$ if and only if $L_d$ is a linear order that embeds into $\{ y : y <_{L_e} x \}$ for some $x$ in the field of $L_e$: the initial segments of $L_e$ below its elements have all the types smaller than $|L_e|$.
- $\varphi(d) \leq \varphi(e)$ if and only if $L_d$ is a linear order that embeds into $L_e$.

Both conditions are $\Sigma^1_1$: an existential quantifier over an embedding, in front of an arithmetic condition. Hence $e \in \mathrm{WO} \wedge \varphi(e) \leq \varphi(d)$ is equivalent to $e \in \mathrm{WO} \wedge \neg (\varphi(d) < \varphi(e))$, and $e \in \mathrm{WO} \wedge \varphi(e) < \varphi(d)$ to $e \in \mathrm{WO} \wedge \neg (\varphi(d) \leq \varphi(e))$. Both are conjunctions of a $\Pi^1_1$ condition and the negation of a $\Sigma^1_1$ condition, hence $\Pi^1_1$.
:::
::::

## Notes and references

Representing co-analytic sets by well-founded trees and assigning ordinals to their members goes back to Lusin and Sierpiński (1923), who introduced the ordering of sequences now called the Kleene–Brouwer ordering. In the effective setting, Kleene (1955) represented $\Pi^1_1$ sets by notations in $\mathcal O$, and Spector (1955) by computable well-orderings, in a form close to the one used here (Moschovakis, Section 4G, historical remarks 5–9). The prewellordering property was isolated explicitly by Moschovakis in 1964, in order to give common proofs for $\Pi^1_1$ and $\Sigma^1_2$; the form of the definition used here is due to Kechris (Moschovakis, *Descriptive Set Theory*, Section 4G, historical remark 12). Moschovakis proves that $\Pi^1_1$ is normed as Theorem 4B.2, from the representation of $\Pi^1_1$ sets by trees (Theorem 4A.3).

Monin and Patey present the analogy between $\Pi^1_1$ and c.e. sets differently: they write a $\Pi^1_1$ set as an increasing union of sets $A_\alpha$, each $\Sigma^0_{\alpha+1}$, for $\alpha < \omega_1^{\mathrm{CK}}$, using Kleene's $\mathcal O$ and the H-sets in place of trees and ranks.

- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009, Sections 4A–4B.
- A. S. Kechris, *Classical Descriptive Set Theory*, Springer, 1995, Sections 34–35 (co-analytic ranks and rank theory).
- B. Monin and L. Patey, *Computability theory*, chapter *Beyond hyperarithmetic*, sections *The Π¹₁ sets and the well-orders* and *Analogies between Π¹₁ sets and c.e. sets*.

:::::exercises
::::exercise{#ex-same-stage difficulty=1 objective="Apply stage comparison to the elements that enter a $\Pi^1_1$ set strictly before a given element, and to the relation of entering at the same stage."}
Show that for $n \in A$, the set $\{ m : \rho_m < \rho_n \}$ is $\Delta^1_1$, and that the relation $n \leq^* m \wedge m \leq^* n$ is $\Pi^1_1$ and an equivalence relation on $A$ whose classes are the sets of elements entering $A$ at the same stage.

:::solution
The set is $\{ m : m <^* n \}$, which is $\Pi^1_1$, and $\{ m : \exists k\ (\langle k \rangle \in T_n \wedge \rho(T_m) \leq \rho((T_n)_{\langle k \rangle})) \}$, which is $\Sigma^1_1$, by the display after :ref{#lem-rank-comparison}, since $T_n$ is well-founded. The relation is a conjunction of $\Pi^1_1$ relations. It holds exactly when $n, m \in A$ and $\rho_n = \rho_m$, which is an equivalence relation on $A$ with the stated classes.
:::
::::

::::exercise{#ex-rank-full-trees difficulty=1 objective="Compare the ranks of explicit trees by strictly monotone maps, and see that such maps never shorten nodes."}
For $k \in \nat$, let $F_k$ be the tree of all sequences of length at most $k$, and let
$$
G = \{ \emptyset \} \cup \{ \langle n \rangle \sigma : n \in \nat,\ |\sigma| \leq n \}.
$$

1. Show that every strictly monotone map $g : S \to T$ between trees satisfies $|g(\sigma)| \geq |\sigma|$ for every $\sigma \in S$. Deduce, without :ref{#lem-rank-comparison}, that there is a strictly monotone map from $F_j$ to $F_k$ if and only if $j \leq k$.
2. Show that $\rho(G) = \omega$, that every $F_k$ has a strictly monotone map into $G$, and that $G$ has none into any $F_k$.

:::solution
1. By induction on $|\sigma|$. For $\sigma = \emptyset$ there is nothing to prove. If $\sigma = \tau n$, then $g(\tau) \subsetneq g(\sigma)$, so $|g(\sigma)| \geq |g(\tau)| + 1 \geq |\tau| + 1 = |\sigma|$. If $j \leq k$, the inclusion of $F_j$ into $F_k$ is strictly monotone. Conversely, if $g : F_j \to F_k$ is strictly monotone, then $g(0^j)$ is a node of $F_k$ of length at least $j$, so $j \leq k$.
2. $G$ is a tree: the prefixes of $\langle n \rangle \sigma$ are $\emptyset$ and the sequences $\langle n \rangle \tau$ with $\tau \subseteq \sigma$. The subtree $G_{\langle n \rangle}$ is $F_n$, of rank $n$ (as observed at the beginning of the lesson), so $\mathrm{rk}(G) = \sup_n (n + 1) = \omega$ by :ref{#def-tree-rank}. The map $\sigma \mapsto \langle k \rangle \sigma$ sends $F_k$ into $G$, since $|\sigma| \leq k$, and it is strictly monotone. Finally, $G$ contains $\langle k \rangle 0^k$, of length $k + 1$; by item 1, its image under a strictly monotone map would have length at least $k + 1$, so $G$ has no strictly monotone map into $F_k$. Both facts agree with :ref{#lem-rank-comparison}, since $k < \omega$.
:::
::::

::::exercise{#ex-rank-comparison-complexity difficulty=1 objective="Locate the comparison relations $\rho(S) \leq \rho(T)$ and $\rho(S) < \rho(T)$ on computable trees exactly in the analytical hierarchy."}
Let $\mathrm{Tr}$ be the set of numbers $e$ such that $\Phi_e$ is total, $\{0, 1\}$-valued, and the characteristic function of a tree $T_e$ containing the empty sequence; it is an arithmetic set. Show that the set of pairs $(d, e) \in \mathrm{Tr}^2$ with $\rho(T_d) \leq \rho(T_e)$ is $\Sigma^1_1$ but not $\Pi^1_1$, and that the set of pairs $(d, e) \in \mathrm{Tr}^2$ with $\rho(T_d) < \rho(T_e)$ is $\Pi^1_1$ but not $\Sigma^1_1$.

:::solution
*Upper bounds.* By :ref{#lem-rank-comparison}, for $d, e \in \mathrm{Tr}$, $\rho(T_d) \leq \rho(T_e)$ if and only if some function $g$, defined on codes of sequences, maps $T_d$ into $T_e$ strictly monotonically. This condition on $d$, $e$ and $g$ is arithmetic, so the relation is $\Sigma^1_1$. For the strict relation: if $T_d$ is well-founded, then $\rho(T_d)$ is an ordinal, and $\rho(T_d) < \rho(T_e)$ holds if and only if $\rho(T_e) \leq \rho(T_d)$ fails; if $T_d$ is ill-founded, $\rho(T_d) = \infty$ and $\rho(T_d) < \rho(T_e)$ is false. So
$$
\rho(T_d) < \rho(T_e) \iff T_d \text{ is well-founded} \wedge \neg \big(\rho(T_e) \leq \rho(T_d)\big),
$$
the conjunction of a $\Pi^1_1$ condition and the negation of a $\Sigma^1_1$ condition.

*Lower bounds.* Let $\mathrm{WF}^+ = \{ d \in \mathrm{Tr} : T_d \text{ is well-founded} \}$. It is not $\Sigma^1_1$. Indeed, let $A$ be a $\Pi^1_1$ set that is not $\Sigma^1_1$ (:ref{#prop-pi11-not-sigma11}), and $(T'_n)$ uniformly computable trees containing the empty sequence with $n \in A$ if and only if $T'_n$ is well-founded (:ref{#thm-pi11-normal-form}). By the SMN theorem, there is a computable function $h$ with $h(n) \in \mathrm{Tr}$ and $T_{h(n)} = T'_n$ for every $n$. Then $n \in A$ if and only if $h(n) \in \mathrm{WF}^+$, so $A$ would be $\Sigma^1_1$ if $\mathrm{WF}^+$ were. Now fix $u \in \mathrm{Tr}$ with $T_u = \nat^{<\nat}$, so that $\rho(T_u) = \infty$. Then
$$
\begin{gathered}
\mathrm{WF}^+ = \{ d \in \mathrm{Tr} : \rho(T_d) < \rho(T_u) \}, \\
\mathrm{Tr} \setminus \mathrm{WF}^+ = \{ d \in \mathrm{Tr} : \rho(T_u) \leq \rho(T_d) \}.
\end{gathered}
$$
If the strict relation were $\Sigma^1_1$, so would be $\mathrm{WF}^+$. If the relation $\leq$ were $\Pi^1_1$, so would be $\mathrm{Tr} \setminus \mathrm{WF}^+$, and $\mathrm{WF}^+ = \mathrm{Tr} \setminus (\mathrm{Tr} \setminus \mathrm{WF}^+)$ would be $\Sigma^1_1$, since $\mathrm{Tr}$ is arithmetic. Both are impossible.
:::
::::

::::exercise{#ex-ce-stage-comparison difficulty=1 objective="Compute the stage comparison relations of a c.e. set from its enumeration, and check that they are c.e."}
Let $A$ be a c.e. set, with the enumeration $(A_s)$ and the trees $T_n$ of :ref{#ex-ce-stages}. Show that
$$
\begin{gathered}
n \leq^* m \iff \exists s \geq 1\ (n \in A_s \wedge m \notin A_{s-1}), \\
n <^* m \iff \exists s\ (n \in A_s \wedge m \notin A_s).
\end{gathered}
$$
Deduce that both relations are c.e., and that each of them is computable only if $A$ is.

:::solution
For each $n$, let $s_n$ be the least $s$ with $n \in A_s$, and $s_n = \infty$ if $n \notin A$. Since $A_0 = \emptyset$, $s_n \geq 1$, and by :ref{#ex-ce-stages}, $\rho_n = s_n - 1$ if $n \in A$ and $\rho_n = \infty$ otherwise. Since the sets $A_s$ increase, $n \in A_s$ if and only if $s_n \leq s$. So $n \leq^* m$ holds if and only if $s_n$ is finite and $s_n \leq s_m$, and $n <^* m$ if and only if $s_n$ is finite and $s_n < s_m$.

If $s_n$ is finite and $s_n \leq s_m$, then $s = s_n \geq 1$ satisfies $n \in A_s$, and $m \notin A_{s-1}$ since $s_m > s - 1$. Conversely, if $n \in A_s$ and $m \notin A_{s-1}$, then $s_n \leq s$ and $s_m > s - 1$, that is, $s_n \leq s \leq s_m$. Similarly, $s_n < s_m$ with $s_n$ finite holds if and only if some $s$ satisfies $s_n \leq s < s_m$, that is, $n \in A_s$ and $m \notin A_s$.

The relations "$n \in A_s$" and "$m \notin A_s$" are computable, so both relations are $\Sigma^0_1$. Finally, $n \leq^* n$ if and only if $n \in A$, so $A$ is computable if $\leq^*$ is. For $<^*$: if $A = \nat$, $A$ is computable; otherwise fix $m_0 \notin A$, and $n <^* m_0$ if and only if $n \in A$. This is the c.e. counterpart of :ref{#thm-stage-comparison}.
:::
::::

::::exercise{#ex-norm-min-max difficulty=2 objective="Combine stage comparison relations to build $\Pi^1_1$ norms on unions and intersections of $\Pi^1_1$ sets."}
Let $B$ and $C$ be $\Pi^1_1$ sets, let $A = \{ 2n : n \in B \} \cup \{ 2n + 1 : n \in C \}$, with stages $\rho_k$ given by a sequence of trees as in :ref{#def-pi11-stage}, and let
$$
\varphi(n) = \min(\rho_{2n}, \rho_{2n+1}), \qquad \psi(n) = \max(\rho_{2n}, \rho_{2n+1}),
$$
computed in the ordinals extended by $\infty$. Show that $\varphi$ is a $\Pi^1_1$ norm on $B \cup C$ and that $\psi$ is a $\Pi^1_1$ norm on $B \cap C$.

:::solution
First, $\varphi(n) = \infty$ if and only if $\rho_{2n} = \rho_{2n+1} = \infty$, that is, $n \notin B \cup C$; and $\psi(n) = \infty$ if and only if one of the two stages is $\infty$, that is, $n \notin B \cap C$. So $\varphi$ and $\psi$ are norms on $B \cup C$ and $B \cap C$ in the sense of :ref{#def-pi11-norm}. We write their comparison relations with the $\Pi^1_1$ relations $\leq^*$ and $<^*$ of :ref{#thm-stage-comparison}; finite conjunctions and disjunctions of $\Pi^1_1$ formulas are $\Pi^1_1$.

*The norm $\varphi$.* We claim
$$
n \in B \cup C \wedge \varphi(n) \leq \varphi(m) \iff \exists i < 2\ \big(2n + i \leq^* 2m \wedge 2n + i \leq^* 2m + 1\big).
$$
If $n \in B \cup C$, then $\varphi(n) = \rho_{2n+i}$ for some $i < 2$ with $\rho_{2n+i} < \infty$, so $2n + i \in A$; if moreover $\varphi(n) \leq \varphi(m)$, then $\rho_{2n+i}$ is at most both $\rho_{2m}$ and $\rho_{2m+1}$. Conversely, if $2n + i \leq^* 2m$ and $2n + i \leq^* 2m + 1$, then $2n + i \in A$, so $n \in B \cup C$, and $\varphi(n) \leq \rho_{2n+i} \leq \min(\rho_{2m}, \rho_{2m+1}) = \varphi(m)$. The same argument with $<$ and $<^*$ gives the strict relation.

*The norm $\psi$.* We claim
$$
n \in B \cap C \wedge \psi(n) \leq \psi(m) \iff \exists i < 2\ \big(2n \leq^* 2m + i \wedge 2n + 1 \leq^* 2m + i\big).
$$
If $n \in B \cap C$ and $\psi(n) \leq \psi(m)$, let $i < 2$ with $\psi(m) = \rho_{2m+i}$; then $2n, 2n + 1 \in A$ and both $\rho_{2n}$ and $\rho_{2n+1}$ are at most $\rho_{2m+i}$. Conversely, the right-hand side gives $2n, 2n + 1 \in A$, so $n \in B \cap C$, and $\psi(n) \leq \rho_{2m+i} \leq \psi(m)$. Again, the strict relation is obtained by replacing $\leq$ and $\leq^*$ by $<$ and $<^*$.
:::
::::

::::exercise{#ex-norm-initial-segments difficulty=2 objective="Extend the corollary on initial segments to an arbitrary $\Pi^1_1$ norm, and deduce that its values on a non-$\Delta^1_1$ set have no largest element."}
Let $\varphi$ be a $\Pi^1_1$ norm on a set $A$ (:ref{#def-pi11-norm}), and write $n \leq_\varphi m$ for $n \in A \wedge \varphi(n) \leq \varphi(m)$, and $n <_\varphi m$ for $n \in A \wedge \varphi(n) < \varphi(m)$.

1. Show that $A$ is $\Pi^1_1$, and that for every $n \in A$, the sets $\{ m : \varphi(m) \leq \varphi(n) \}$ and $\{ m : \varphi(m) < \varphi(n) \}$ are $\Delta^1_1$.
2. Show that if $A$ is not $\Delta^1_1$, then the set $\{ \varphi(n) : n \in A \}$ has no largest element.
3. Show that the relation $\leq_\varphi$ is $\Delta^1_1$ only if $A$ is.

:::solution
1. $n \in A$ if and only if $n \leq_\varphi n$, so $A$ is $\Pi^1_1$. Let $n \in A$, so that $\varphi(n)$ is an ordinal. A number $m$ with $\varphi(m) \leq \varphi(n)$ has $\varphi(m) < \infty$, so it belongs to $A$; hence $\{ m : \varphi(m) \leq \varphi(n) \} = \{ m : m \leq_\varphi n \}$, which is $\Pi^1_1$. Since the ordinals extended by $\infty$ are linearly ordered, $\varphi(m) \leq \varphi(n)$ holds if and only if $\varphi(n) < \varphi(m)$ fails, that is, since $n \in A$, if and only if $n <_\varphi m$ fails; so the set is also $\Sigma^1_1$. In the same way, $\{ m : \varphi(m) < \varphi(n) \}$ is $\{ m : m <_\varphi n \}$, which is $\Pi^1_1$, and $\{ m : \neg (n \leq_\varphi m) \}$, which is $\Sigma^1_1$.
2. If $\varphi(n_0)$ were the largest value of $\varphi$ on $A$, with $n_0 \in A$, then $A = \{ m : \varphi(m) \leq \varphi(n_0) \}$: members of $A$ satisfy the inequality by maximality, and numbers satisfying it belong to $A$ by item 1. So $A$ would be $\Delta^1_1$ by item 1.
3. If $\leq_\varphi$ is $\Sigma^1_1$, then so is $A = \{ n : n \leq_\varphi n \}$, which is then $\Delta^1_1$.

For the stage map, item 1 is :ref{#cor-initial-segments} and :ref{#ex-same-stage}. Item 2 says that a $\Pi^1_1$ set that is not $\Delta^1_1$ receives new elements at arbitrarily late values of the norm, which the lesson on uniformization makes precise for the stages.
:::
::::
:::::
