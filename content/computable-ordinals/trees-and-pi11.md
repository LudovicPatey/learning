---
title: Π¹₁ sets and Kleene's O
summary: The analytic sets Π¹₁ and Σ¹₁, Kleene's normal form by well-founded trees, and the Π¹₁-completeness of well-foundedness, of well-ordering and of Kleene's O.
duration: 45
prerequisites: [well-founded-trees, markwald]
---

The arithmetic hierarchy classifies sets defined by quantifiers over numbers. Quantifying over sets or functions gives the **analytic** hierarchy, whose first level, the $\Pi^1_1$ sets, is the central object of higher computability. This lesson shows that the $\Pi^1_1$ sets are exactly the sets $\{ n : T_n \text{ is well-founded} \}$ for uniformly computable sequences of trees $(T_n)$, so that well-foundedness, well-ordering and membership in Kleene's $\mathcal O$ are complete $\Pi^1_1$ properties. The next lesson separates $\Pi^1_1$ from $\Sigma^1_1$. The proofs combine the normal form of arithmetic formulas, the Kleene–Brouwer ordering of the previous lesson, and effective transfinite recursion on trees.

## Π¹₁ sets and their normal form

:::definition{#def-pi11-set}
A set $A \subseteq \nat$ is **$\Pi^1_1$** if there is an arithmetic formula $\varphi(n, X)$ such that $n \in A \iff \forall X \subseteq \nat\ \varphi(n, X)$. It is **$\Sigma^1_1$** if its complement is $\Pi^1_1$, and **$\Delta^1_1$** if it is both.
:::

Quantifiers over functions $f \in \nat^\nat$ can be used instead of quantifiers over sets, by coding a function by its graph; the class is the same. Every arithmetic set is $\Delta^1_1$. Relativized to an oracle $Y$, one obtains the $\Pi^1_1(Y)$ sets. The set $\mathrm{WO}$ of :ref{#def-wo} is $\Pi^1_1$: $e \in \mathrm{WO}$ if and only if $e$ is an index of a computable linear order, an arithmetic condition, and every function $f$ fails to be a descending sequence of $L_e$.

:::theorem[Kleene normal form]{#thm-pi11-normal-form}
A set $A$ is $\Pi^1_1$ if and only if there is a uniformly computable sequence of trees $(T_n)$ such that $n \in A$ if and only if $T_n$ is well-founded.
:::

:::proof{of=thm-pi11-normal-form}
($\Leftarrow$) $T_n$ is well-founded if and only if $\forall f\ \exists m\ f \uh m \notin T_n$, a $\Pi^1_1$ formula.

($\Rightarrow$) Write $n \in A \iff \forall f\, \varphi(n, f)$ with $\varphi$ arithmetic in prenex form. We first show, by induction on the number of number quantifiers, that every prenex arithmetic formula $\psi(f)$ is equivalent to a formula $\forall h\ \exists y\ \theta(f, h, y)$ with $\theta$ bounded.

- A bounded formula $\theta$ is equivalent to $\forall h\, \exists y\, \theta$, with dummy variables.
- If $\psi \equiv \forall x\, \chi(x)$ and $\chi(x) \equiv \forall h\, \exists y\, \theta(x, h, y)$, then $\psi \equiv \forall h'\, \exists y\, \theta(h'(0), h'', y)$, where $h''(i) = h'(i+1)$: the single function $h'$ codes both $x$ and $h$.
- If $\psi \equiv \exists x\, \chi(x)$ and $\chi(x) \equiv \forall h\, \exists y\, \theta(x, h, y)$, then $\psi \equiv \forall H\, \exists x\, \exists y\, \theta(x, H^{[x]}, y)$, where $H^{[x]}(i) = H(\langle x, i \rangle)$. Indeed, if $x_0$ witnesses $\psi$, then $\chi(x_0)$ applies to $H^{[x_0]}$. Conversely, if $\psi$ fails, choose for each $x$ a function $h_x$ with $\neg \exists y\, \theta(x, h_x, y)$, and let $H^{[x]} = h_x$; then $\exists x\, \exists y\, \theta(x, H^{[x]}, y)$ fails. The two existential quantifiers merge into one.

So $n \in A \iff \forall g\, \exists y\, \theta(n, g, y)$, where $g$ codes $f$ and the auxiliary function, and $\theta$ is bounded. The evaluation of the bounded formula $\theta(n, g, y)$ queries $g$ at finitely many arguments only. Let $R(n, \sigma)$ hold if for some $y < |\sigma|$, the evaluation of $\theta(n, g, y)$ with $\sigma$ in place of $g$ queries only arguments below $|\sigma|$ and returns true. Then $R$ is computable, and $\exists y\, \theta(n, g, y) \iff \exists m\, R(n, g \uh m)$: from left to right, take $m$ larger than $y$ and than every argument queried; from right to left, $g$ and $g \uh m$ agree on the queried arguments. Let $T_n = \{ \sigma : \neg R(n, \tau) \text{ for every } \tau \preceq \sigma \}$. Then $T_n$ is a tree, uniformly computable, and it has a path $g$ if and only if $\exists y\, \theta(n, g, y)$ fails for $g$, that is, if and only if $n \notin A$.
:::

The proof uses the axiom of choice in the third case, a countable choice of functions; this is harmless in the metatheory.

:::corollary{#cor-pi11-complete}
Let $\mathrm{WF}$ be the set of indices of computable trees that are well-founded, and $\mathrm{WO}$ the set of indices of computable linear orders that are well-orderings. Both are $\Pi^1_1$, and every $\Pi^1_1$ set is many-one reducible to each of them.
:::

:::proof{of=cor-pi11-complete}
Both definitions are $\Pi^1_1$: "for every $f$, $f$ is not a path", and "for every $f$, $f$ is not a descending sequence", together with the arithmetic conditions of being a tree or a linear order. If $A$ is $\Pi^1_1$, the normal form gives a computable function $n \mapsto$ an index of $T_n$, reducing $A$ to $\mathrm{WF}$. Composing with the computable map sending an index of a tree to an index of its Kleene–Brouwer ordering reduces $A$ to $\mathrm{WO}$, by :ref{#thm-kleene-brouwer}.
:::

## Kleene's O is Π¹₁-complete

Since $\mathcal O$ is defined as the least set closed under rules, membership in $\mathcal O$ is a universal statement over sets: a number is a notation if it belongs to every set closed under the rules. This is the general reason why inductive definitions produce $\Pi^1_1$ sets.

:::proposition{#prop-o-pi11}
The set $\mathcal O$ is $\Pi^1_1$.
:::

:::proof{of=prop-o-pi11}
Call a pair $(X, Y)$, with $X \subseteq \nat$ and $Y \subseteq \nat \times \nat$, **closed** if $1 \in X$; if $x \in X$, then $2^x \in X$, $(x, 2^x) \in Y$, and $(z, 2^x) \in Y$ whenever $(z, x) \in Y$; and if $\Phi_e$ is total, $\Phi_e(n) \in X$ and $(\Phi_e(n), \Phi_e(n+1)) \in Y$ for every $n$, then $3 \cdot 5^e \in X$ and $(z, 3 \cdot 5^e) \in Y$ whenever $(z, \Phi_e(n)) \in Y$ for some $n$. Being closed is an arithmetic property of $(X, Y)$. We show that $a \in \mathcal O$ if and only if $a \in X$ for every closed pair $(X, Y)$, a $\Pi^1_1$ condition.

The pair $(\mathcal O, <_{\mathcal O})$ is closed, which gives the direction from right to left. Conversely, let $(X, Y)$ be closed, and let $\mathcal O'$ be the set of $a \in \mathcal O$ such that $a \in X$ and $(b, a) \in Y$ for every $b <_{\mathcal O} a$. Then $\mathcal O'$ satisfies the rules of :ref{#def-kleene-o}: for the limit rule, if all $\Phi_e(n)$ are in $\mathcal O'$ and $\Phi_e(n) <_{\mathcal O} \Phi_e(n+1)$, then $(\Phi_e(n), \Phi_e(n+1)) \in Y$, so $3 \cdot 5^e \in X$; and every $b <_{\mathcal O} 3 \cdot 5^e$ satisfies $b <_{\mathcal O} \Phi_e(n)$ for some $n$, so $(b, \Phi_e(n)) \in Y$ and $(b, 3 \cdot 5^e) \in Y$. The successor rule is similar. By minimality, $\mathcal O \subseteq \mathcal O' \subseteq X$.
:::

Conversely, every $\Pi^1_1$ set reduces to $\mathcal O$. By the normal form theorem it suffices to send a computable tree $T$ to a number that is a notation exactly when $T$ is well-founded. The natural idea is to assign to each node $\sigma$ a notation above the notations of its immediate successors $\sigma m \in T$, by effective transfinite recursion on the tree, as in the proof of :ref{#thm-markwald}. Two points need care. The notations of the successors must be combined into an increasing sequence, as required by the limit rule; and when $T$ has a path, the number assigned to the root must fail to be a notation. Both are handled by building the notation of the subtree above $\sigma m$ **on top of** the notations already used for $\sigma 0, \dots, \sigma (m - 1)$: the sequence is then increasing by construction, and a notation for the root can be decomposed, by :ref{#lem-o-inversion}, into notations for the nodes along any path, with decreasing ordinals.

:::theorem[Kleene]{#thm-o-complete}
The set $\mathcal O$ is $\Pi^1_1$-complete: for every $\Pi^1_1$ set $A$, there is a total computable function $f$ such that $n \in A$ if and only if $f(n) \in \mathcal O$.
:::

:::proof{of=thm-o-complete}
By :ref{#thm-pi11-normal-form}, let $(T_n)$ be a uniformly computable sequence of trees with $n \in A$ if and only if $T_n$ is well-founded. By the recursion theorem (:ref{#cor-self-reference}) and the SMN theorem, there is a total computable function $F(n, b, \sigma)$, of a number $n$, a number $b$ and a sequence $\sigma$, such that $F(n, b, \sigma) = 3 \cdot 5^{j}$, where $j$ is an index, computed from $n$, $b$, $\sigma$ and an index of $F$, of the function $m \mapsto c_m$ defined by
$$
c_0 = 2^b, \qquad c_{m+1} = \begin{cases} 2^{F(n, c_m, \sigma m)} & \text{if } \sigma m \in T_n, \\ 2^{c_m} & \text{otherwise.} \end{cases}
$$
The function $F$ is total, since it only computes an index, and the function $m \mapsto c_m$ is then total as well. Let $f(n) = F(n, 1, \langle \rangle)$. Fix $n$ and write $T = T_n$ and $F(b, \sigma) = F(n, b, \sigma)$.

*Claim 1. If $T_\sigma$ is well-founded, then for every $b \in \mathcal O$, $F(b, \sigma) \in \mathcal O$ and $b <_{\mathcal O} F(b, \sigma)$.* By induction on $\mathrm{rk}(T_\sigma)$, for all $b$ at once. Let $(c_m)$ be the sequence of $F(b, \sigma) = 3 \cdot 5^j$. We show by induction on $m$ that $c_m \in \mathcal O$ and $c_m <_{\mathcal O} c_{m+1}$. First, $c_0 = 2^b \in \mathcal O$. If $\sigma m \in T$, then $T_{\sigma m}$ has rank less than $\mathrm{rk}(T_\sigma)$, and the induction hypothesis applied to the base $c_m$ gives $F(c_m, \sigma m) \in \mathcal O$ with $c_m <_{\mathcal O} F(c_m, \sigma m) <_{\mathcal O} c_{m+1}$. Otherwise $c_{m+1} = 2^{c_m}$ and $c_m <_{\mathcal O} c_{m+1}$. So $3 \cdot 5^j \in \mathcal O$, and $b <_{\mathcal O} c_0 <_{\mathcal O} 3 \cdot 5^j$.

*Claim 2. If $F(b, \sigma) \in \mathcal O$ and $\sigma m \in T$, then $F(b', \sigma m) \in \mathcal O$ and $|F(b', \sigma m)| < |F(b, \sigma)|$ for some $b'$.* Let $F(b, \sigma) = 3 \cdot 5^j$ with sequence $(c_m)$. By :ref{#lem-o-inversion}, every $c_k$ is in $\mathcal O$ and $c_{m+1} <_{\mathcal O} 3 \cdot 5^j$. Now $c_{m+1} = 2^{F(c_m, \sigma m)}$ with $F(c_m, \sigma m) \neq 0$, so $F(c_m, \sigma m) \in \mathcal O$ by inversion again, and $F(c_m, \sigma m) <_{\mathcal O} c_{m+1} <_{\mathcal O} 3 \cdot 5^j$. Take $b' = c_m$.

If $n \in A$, then $T$ is well-founded, and $f(n) \in \mathcal O$ by Claim 1 with $b = 1$ and $\sigma = \langle \rangle$. If $n \notin A$, let $g$ be a path of $T$, and suppose $f(n) \in \mathcal O$. Applying Claim 2 along $g$, with $b'$ given explicitly by its proof, defines numbers $b_0 = 1, b_1, b_2, \dots$ such that $F(b_k, g \uh k) \in \mathcal O$ and $|F(b_{k+1}, g \uh (k+1))| < |F(b_k, g \uh k)|$ for every $k$: an infinite descending sequence of ordinals, which is impossible. So $f(n) \notin \mathcal O$.
:::

:::figure[The notation $F(b, \sigma)$ of the proof. The chain $c_0, c_1, c_2, \dots$ starts just above $b$; when $\sigma k \in T$, the notation of the subtree above $\sigma k$ is built on top of $c_k$, and $c_{k+1}$ is its successor. The limit of the chain is $F(b, \sigma)$.]
<svg class="fig" viewBox="0 0 600 222" width="600" role="img" aria-label="The notation F(b, sigma) is the limit of a chain c0, c1, c2 starting above b; each step builds the notation of a subtree on top of the previous element of the chain"><defs><marker id="co-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="muted-fill"/></marker><marker id="co-red-acc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><line x1="46" y1="120" x2="103" y2="120" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-red)"/><line x1="116" y1="120" x2="243" y2="120" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-red)"/><line x1="256" y1="120" x2="383" y2="120" class="ink-stroke" stroke-width="1.3" marker-end="url(#co-red)"/><line x1="396" y1="120" x2="460" y2="120" class="ink-stroke" stroke-width="1.3" stroke-dasharray="4 3"/><circle cx="40" cy="120" r="4.5" class="ink-fill"/><text x="40.0" y="146.0" text-anchor="middle" class="math" font-size="16">b</text><circle cx="110" cy="120" r="4.5" class="ink-fill"/><text x="110.0" y="146.0" text-anchor="middle" class="math" font-size="16"><tspan class="math">c</tspan><tspan class="math" font-size="11" dy="4">0</tspan></text><circle cx="250" cy="120" r="4.5" class="ink-fill"/><text x="250.0" y="146.0" text-anchor="middle" class="math" font-size="16"><tspan class="math">c</tspan><tspan class="math" font-size="11" dy="4">1</tspan></text><circle cx="390" cy="120" r="4.5" class="ink-fill"/><text x="390.0" y="146.0" text-anchor="middle" class="math" font-size="16"><tspan class="math">c</tspan><tspan class="math" font-size="11" dy="4">2</tspan></text><circle cx="540" cy="120" r="5.5" class="accent-fill"/><text x="540.0" y="146.0" text-anchor="middle" class="math" font-size="16">F(b, σ)</text><text x="500.0" y="125.0" text-anchor="middle" class="mrm muted" font-size="16">⋯</text><path d="M114,112 Q150.0,50 174.0,62" class="accent-stroke" stroke-width="1.3" marker-end="url(#co-red-acc)"/><circle cx="180.0" cy="64" r="4" class="accent-fill"/><path d="M186.0,66 Q220.0,80 244,111" class="muted-stroke" stroke-width="1.2" marker-end="url(#co-red)"/><text x="180.0" y="50" text-anchor="middle" font-size="14"><tspan class="math">F</tspan><tspan class="mrm">(</tspan><tspan class="math">c</tspan><tspan class="math" font-size="9" dy="4">0</tspan><tspan class="mrm" dy="-4">, </tspan><tspan class="math">σ</tspan><tspan class="mrm">0)</tspan></text><path d="M254,112 Q290.0,50 314.0,62" class="accent-stroke" stroke-width="1.3" marker-end="url(#co-red-acc)"/><circle cx="320.0" cy="64" r="4" class="accent-fill"/><path d="M326.0,66 Q360.0,80 384,111" class="muted-stroke" stroke-width="1.2" marker-end="url(#co-red)"/><text x="320.0" y="50" text-anchor="middle" font-size="14"><tspan class="math">F</tspan><tspan class="mrm">(</tspan><tspan class="math">c</tspan><tspan class="math" font-size="9" dy="4">1</tspan><tspan class="mrm" dy="-4">, </tspan><tspan class="math">σ</tspan><tspan class="mrm">1)</tspan></text><text x="40.0" y="186.0" text-anchor="start" class="label" font-size="12">For σk ∈ T, the notation of the subtree above σk is built on top of c<tspan font-size="9" dy="3">k</tspan><tspan dy="-3"> </tspan>, and c<tspan font-size="9" dy="3">k+1</tspan><tspan dy="-3"> </tspan> is its successor;</text><text x="40.0" y="204.0" text-anchor="start" class="label" font-size="12">for σk ∉ T, c<tspan font-size="9" dy="3">k+1</tspan><tspan dy="-3"> </tspan> is the successor of c<tspan font-size="9" dy="3">k</tspan><tspan dy="-3"> </tspan>.</text></svg>
:::

:::quiz[the reduction to O]
Why is the notation of the subtree above $\sigma m$ built on top of $c_m$, instead of being computed independently and added to $c_m$ with $+_{\mathcal O}$?

- [x] Because then $c_m <_{\mathcal O} c_{m+1}$ follows from Claim 1, and in the ill-founded case $F(c_m, \sigma m)$ is recovered from $c_{m+1}$ by inversion alone. With a sum, one would need to show that $a +_{\mathcal O} x \in \mathcal O$ implies $x \in \mathcal O$, which does not follow from :ref{#lem-notation-sum}.
- [ ] Because $+_{\mathcal O}$ is not computable.

  It is total computable (:ref{#lem-notation-sum}).
- [ ] Because otherwise the function $F$ would not be total.

  Totality holds in both versions: $F$ only computes an index.

---

In the ill-founded case, where is the path $g$ used?

- [x] To choose, at each node $g \uh k$, the successor $g \uh (k+1) \in T$ to which Claim 2 applies; following it forever gives the descending sequence of ordinals.
- [ ] To show that $F$ is total.

  Totality does not depend on the tree.
- [ ] To compute $f(n)$.

  $f(n) = F(n, 1, \langle \rangle)$ does not depend on the paths of $T_n$.
:::

The theorem relativizes uniformly: $\mathcal O^X$ is $\Pi^1_1(X)$-complete for every $X$. Together with :ref{#cor-pi11-complete}, it shows that $\mathrm{WF}$, $\mathrm{WO}$ and $\mathcal O$ are many-one reducible to one another: they are three presentations of the same complete $\Pi^1_1$ set. In the course on hyperarithmetic sets, $\mathcal O$ plays for $\Pi^1_1$ sets the role that $\emptyset'$ plays for c.e. sets.

::::exercise{#ex-pi11-reducible difficulty=1 objective="Characterize the $\Pi^1_1$ sets as the sets many-one reducible to $\mathcal O$, to $\mathrm{WO}$ or to $\mathrm{WF}$."}
Show that a set $A \subseteq \nat$ is $\Pi^1_1$ if and only if $A \leq_m \mathcal O$, and that the same holds with $\mathrm{WO}$ or $\mathrm{WF}$ in place of $\mathcal O$.

:::solution
If $A \leq_m \mathcal O$ by a computable $f$, then $n \in A \iff f(n) \in \mathcal O$, and substituting $f(n)$ into the $\Pi^1_1$ definition of $\mathcal O$ (:ref{#prop-o-pi11}) gives a $\Pi^1_1$ definition of $A$, since "$m = f(n)$" is arithmetic. The converse is :ref{#thm-o-complete}. The same argument applies to $\mathrm{WO}$ and $\mathrm{WF}$, which are $\Pi^1_1$, with :ref{#cor-pi11-complete} for the converse.
:::
::::

## Notes and references

Kleene (1955) introduced the analytic hierarchy and proved the normal form theorem; the $\Pi^1_1$-completeness of $\mathcal O$ is also due to Kleene (1955, second paper on the forms of predicates). Simpson proves the normal form theorem in Lemma V.1.4 and the reduction of $\Pi^1_1$ formulas to well-orderings in Lemma V.1.8. Monin and Patey prove that $\mathcal O^X$ is $\Pi^1_1(X)$ and $\Pi^1_1(X)$-complete in the section *The Π¹₁ sets and the well-orders* of their chapter *Beyond hyperarithmetic*; their reduction composes the Kleene–Brouwer ordering with the Markwald–Kleene map, and leaves to the reader the verification that an ill-founded tree is sent outside $\mathcal O$. The reduction given here builds notations on top of one another to make that verification immediate. Nies states the $\Pi^1_1$-completeness of $\mathcal O$ in Section 9.1. Moschovakis's *Descriptive Set Theory* presents the effective theory in the general setting of Polish spaces.

- S. C. Kleene, *Arithmetical predicates and function quantifiers*, Transactions of the American Mathematical Society 79 (1955), 312–340.
- S. C. Kleene, *On the forms of the predicates in the theory of constructive ordinals (second paper)*, American Journal of Mathematics 77 (1955), 405–428.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section V.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Beyond hyperarithmetic*, section *The Π¹₁ sets and the well-orders*.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 9.1.
- Y. N. Moschovakis, *Descriptive Set Theory*, 2nd edition, American Mathematical Society, 2009.

:::::exercises
::::exercise{#ex-ill-founded-complete difficulty=1 objective="Transfer the completeness results for $\Pi^1_1$ to complements, and obtain complete $\Sigma^1_1$ sets."}
Let $\mathrm{IF}$ be the set of indices of computable trees that are ill-founded, and $\mathrm{NWO}$ the set of indices of computable linear orders that are not well-orderings. Show that both are $\Sigma^1_1$, and that every $\Sigma^1_1$ set is many-one reducible to each of them.

:::solution
Being an index of a computable tree, or of a computable linear order, is arithmetic, and "some function is a path", or "some function is a descending sequence", is $\Sigma^1_1$; so $\mathrm{IF}$ and $\mathrm{NWO}$ are $\Sigma^1_1$.

Let $A$ be $\Sigma^1_1$. Its complement is $\Pi^1_1$, and the proof of :ref{#cor-pi11-complete} gives a total computable $f$ such that $f(n)$ is an index of the computable tree $T_n$ of :ref{#thm-pi11-normal-form} for every $n$, and $n \notin A$ if and only if $T_n$ is well-founded. Since $f(n)$ is always an index of a tree, $n \in A$ if and only if $f(n) \in \mathrm{IF}$. Composing $f$ with the map that sends an index of a tree to an index of its Kleene–Brouwer ordering, which is always an index of a computable linear order, gives a reduction of $A$ to $\mathrm{NWO}$, by :ref{#thm-kleene-brouwer}.
:::
::::

::::exercise{#ex-pi11-number-quantifiers difficulty=2 objective="Combine sequences of trees into a single tree to show that $\Pi^1_1$ sets are closed under number quantifiers."}
Let $(T_{n,m})$ be a uniformly computable family of trees. Construct uniformly computable sequences of trees $(S_n)$ and $(S'_n)$ such that $S_n$ is well-founded if and only if $T_{n,m}$ is well-founded for every $m$, and $S'_n$ is well-founded if and only if $T_{n,m}$ is well-founded for some $m$. Deduce that if $B \subseteq \nat$ is $\Pi^1_1$, then so are $\{ n : \forall m\ \langle n, m \rangle \in B \}$ and $\{ n : \exists m\ \langle n, m \rangle \in B \}$.

:::solution
*Universal quantifier.* Let $S_n = \{ \langle \rangle \} \cup \{ m\tau : \tau \in T_{n,m} \}$, the trees $T_{n,m}$ placed side by side above the root. It is closed under prefixes and computable, uniformly in $n$. A path of $S_n$ has the form $m g$ with $g$ a path of $T_{n,m}$, and conversely. So $S_n$ is ill-founded if and only if some $T_{n,m}$ is, that is, $S_n$ is well-founded if and only if all the $T_{n,m}$ are.

*Existential quantifier.* Fix a bijective pairing $\langle m, i \rangle$ that is increasing in each argument, such as Cantor's, so that $\langle m, i \rangle \geq m$. For a sequence $\sigma$ and a number $m$, let $\sigma^{[m]}$ be the sequence $(\sigma(\langle m, 0 \rangle), \dots, \sigma(\langle m, i - 1 \rangle))$, where $i$ is least with $\langle m, i \rangle \geq |\sigma|$. Let
$$
S'_n = \{ \sigma : \sigma^{[m]} \in T_{n,m} \text{ for every } m < |\sigma| \}.
$$
It is computable, uniformly in $n$. It is a tree: if $\rho$ is a prefix of $\sigma \in S'_n$ and $m < |\rho|$, then $\rho^{[m]}$ is a prefix of $\sigma^{[m]}$, since the pairing is increasing in $i$, so $\rho^{[m]} \in T_{n,m}$.

If $g$ is a path of $S'_n$, let $g^{[m]}(i) = g(\langle m, i \rangle)$. Each prefix of $g^{[m]}$ is $(g \uh l)^{[m]}$ for a large enough $l > m$, so it is in $T_{n,m}$: every $T_{n,m}$ has the path $g^{[m]}$. Conversely, if every $T_{n,m}$ has a path $f_m$, let $g(\langle m, i \rangle) = f_m(i)$; then $(g \uh l)^{[m]}$ is a prefix of $f_m$ for all $l$ and $m$, so $g$ is a path of $S'_n$. Hence $S'_n$ is ill-founded if and only if all the $T_{n,m}$ are, and well-founded if and only if some $T_{n,m}$ is. The converse direction chooses a path $f_m$ for each $m$, a countable choice, as in the proof of :ref{#thm-pi11-normal-form}.

If $B$ is $\Pi^1_1$, :ref{#thm-pi11-normal-form} gives a uniformly computable sequence of trees $(T_k)$ with $k \in B$ if and only if $T_k$ is well-founded. Apply the constructions to $T_{n,m} = T_{\langle n, m \rangle}$: $\forall m\ \langle n, m \rangle \in B$ if and only if $S_n$ is well-founded, and $\exists m\ \langle n, m \rangle \in B$ if and only if $S'_n$ is well-founded. Both sets are $\Pi^1_1$ by the easy direction of :ref{#thm-pi11-normal-form}.
:::
::::

::::exercise{#ex-wf-part-inductive difficulty=2 objective="Describe the well-founded part of a tree as the least set closed under a rule, and derive its $\Pi^1_1$ definition as for $\mathcal O$."}
Let $T$ be a computable tree, and let $W$ be the set of $\sigma \in T$ such that $T_\sigma$ is well-founded. Call a set $X \subseteq \nat^{<\nat}$ **closed** if every $\sigma \in T$ all of whose immediate successors $\sigma m \in T$ belong to $X$ is itself in $X$. Show that $W$ is the least closed set, and deduce, as in :ref{#prop-o-pi11}, that $W$ is $\Pi^1_1$.

:::solution
$W$ is closed: if $\sigma \in T$ and $T_\sigma$ has a path $f$, then $\sigma f(0) \in T$ and $T_{\sigma f(0)}$ has the path $n \mapsto f(n + 1)$, so $\sigma f(0) \notin W$. Contrapositively, if all the $\sigma m \in T$ are in $W$, then $\sigma \in W$.

$W$ is contained in every closed set $X$: we show $\sigma \in X$ for $\sigma \in W$ by induction on $\mathrm{rk}(T_\sigma)$. Every $\sigma m \in T$ has $T_{\sigma m}$ well-founded, of smaller rank, so $\sigma m \in X$ by the induction hypothesis; since $X$ is closed and $\sigma \in T$, $\sigma \in X$.

Hence $\sigma \in W$ if and only if $\sigma \in X$ for every closed $X$. Being closed is the arithmetic condition $\forall \sigma\, [\sigma \in T \wedge \forall m\, (\sigma m \in T \rightarrow \sigma m \in X) \rightarrow \sigma \in X]$, since $T$ is computable, so $W$ is $\Pi^1_1$. This agrees with the direct definition: $\sigma \in W$ if and only if $\sigma \in T$ and for every $f$ there is $m$ with $\sigma (f \uh m) \notin T$. The proof of :ref{#prop-o-pi11} follows the same pattern, with the three rules of $\mathcal O$ in place of the single rule here.
:::
::::

::::exercise{#ex-no-computable-descending difficulty=2 objective="Combine the $\Pi^1_1$-completeness of $\mathrm{WO}$ with the arithmetic hierarchy theorem to show that ill-foundedness is not always witnessed computably."}
Show that some computable linear order that is not a well-ordering has no computable descending sequence. Use :ref{#cor-pi11-complete} and the fact that the arithmetic hierarchy is proper.

:::solution
Let $\mathrm{LO}$ be the set of indices of computable linear orders, a $\Pi^0_2$ set. Suppose that every computable linear order that is not a well-ordering has a computable descending sequence. Then for $e \in \mathrm{LO}$,
$$
e \notin \mathrm{WO} \iff \exists i\, \big[\Phi_i \text{ is total} \wedge \forall n\ \Phi_i(n + 1) <_{L_e} \Phi_i(n)\big],
$$
since a computable descending sequence is a total $\Phi_i$. The bracket is $\Pi^0_2$: totality is $\Pi^0_2$, and $\forall n\, \exists s$ (both values converge at stage $s$ and are compared by $\Phi_e$, which is total) is $\Pi^0_2$. So $\mathrm{LO} \setminus \mathrm{WO}$ is the intersection of $\mathrm{LO}$ with a $\Sigma^0_3$ set, and $\mathrm{WO} = \mathrm{LO} \cap \{ e : \neg \exists i \cdots \}$ is $\Pi^0_3$.

By :ref{#cor-pi11-complete}, every $\Pi^1_1$ set would then be many-one reducible to a $\Pi^0_3$ set, hence $\Pi^0_3$. But $\emptyset'''$ is arithmetic, hence $\Pi^1_1$, and it is $\Sigma^0_3$-complete, hence not $\Pi^0_3$: otherwise every $\Sigma^0_3$ set would be $\Pi^0_3$, contradicting the hierarchy theorem. This contradiction shows that some ill-founded computable linear order has no computable descending sequence.

The next lesson strengthens this: some such order has no arithmetic descending sequence.
:::
::::

::::exercise{#ex-reduction-rank difficulty=2 objective="Follow the ordinals through the reduction of a tree to a notation, and bound the rank of the tree by the ordinal of the notation."}
Let $F$ and $f$ be as in the proof of :ref{#thm-o-complete}, for a fixed $n$ with $T = T_n$ well-founded. Show by induction on $\mathrm{rk}(T_\sigma)$ that $|F(n, b, \sigma)| \geq |b| + \mathrm{rk}(T_\sigma)$ for every $b \in \mathcal O$ and every $\sigma$ with $T_\sigma$ well-founded. Deduce that $\mathrm{rk}(T_n) \leq |f(n)| < \omega_1^{\mathrm{CK}}$.

:::solution
Write $F(b, \sigma)$ for $F(n, b, \sigma)$, and let $(c_m)$ be the sequence of $F(b, \sigma)$. By the proof of Claim 1, all the $c_m$ are notations, $<_{\mathcal O}$-increasing, $c_0 = 2^b$, and $|F(b, \sigma)| = \sup_m |c_m|$. In particular $|c_m| > |b|$ for every $m$. If $\sigma$ has no immediate successor in $T$, then $\mathrm{rk}(T_\sigma) = 0$ and $|F(b, \sigma)| > |b|$. Otherwise, for each $m$ with $\sigma m \in T$, the induction hypothesis applied to $\sigma m$ and the base $c_m$ gives
$$
|c_{m+1}| = |F(c_m, \sigma m)| + 1 \geq |c_m| + \mathrm{rk}(T_{\sigma m}) + 1 \geq |b| + \rho_m,
$$
where $\rho_m = \mathrm{rk}(T_{\sigma m}) + 1$, using that $\alpha \leq \alpha'$ implies $\alpha + \beta \leq \alpha' + \beta$ (by induction on $\beta$). So $|F(b, \sigma)| \geq \sup_m (|b| + \rho_m)$, the supremum being over the $m$ with $\sigma m \in T$. By definition, $\mathrm{rk}(T_\sigma) = \sup_m \rho_m$. If this supremum is attained, at $\rho_{m_0}$, then $\sup_m (|b| + \rho_m) \geq |b| + \rho_{m_0} = |b| + \mathrm{rk}(T_\sigma)$. Otherwise $\mathrm{rk}(T_\sigma)$ is a limit $\lambda$, the $\rho_m$ are cofinal in $\lambda$, and $|b| + \lambda = \sup_{\delta < \lambda} (|b| + \delta) = \sup_m (|b| + \rho_m)$, since addition is non-decreasing in its right argument. In both cases $|F(b, \sigma)| \geq |b| + \mathrm{rk}(T_\sigma)$.

With $b = 1$ and $\sigma = \langle \rangle$: $|f(n)| \geq 0 + \mathrm{rk}(T_n) = \mathrm{rk}(T_n)$, and $|f(n)| < \omega_1^{\mathrm{CK}}$ since $f(n) \in \mathcal O$ (:ref{#cor-constructive-computable}). The construction of $F$ applies to any uniformly computable sequence of trees, in particular to a constant sequence; this gives a second proof that the rank of a computable well-founded tree is a computable ordinal (:ref{#prop-rank-computable}).
:::
::::
:::::
