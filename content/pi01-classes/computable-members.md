---
title: Computable members
summary: Isolated members of Π⁰₁ classes are computable; countable Π⁰₁ classes have computable members; a non-empty Π⁰₁ class without computable member is perfect; the class of DNC₂ functions.
duration: 45
prerequisites: [trees-and-classes]
---

A non-empty $\Pi^0_1$ class always has a member computable in $\emptyset'$: follow the leftmost extendible node, which $\emptyset'$ can recognize. Whether it has a computable member depends on the topology of the class. Isolated members are computable, so countable classes have computable members. But there are non-empty $\Pi^0_1$ classes without computable members, and these classes are necessarily large: they contain a copy of Cantor space.

## The leftmost path

:::proposition{#prop-leftmost-path}
Every non-empty $\Pi^0_1$ class has a member computable in $\emptyset'$, namely its leftmost member.
:::

:::proof{of=prop-leftmost-path}
Let $\mathcal P = [T]$ with $T$ computable. By :ref{#prop-pi01-emptiness}, the set of extendible nodes of $T$ is co-c.e., hence computable in $\emptyset'$. Define $X$ by induction: $X(n) = 0$ if $(X \uh n)\, 0$ is extendible, and $X(n) = 1$ otherwise. Since $X \uh n$ is extendible, one of its two successors is, so every $X \uh n$ is extendible, and $X \in [T]$. The construction asks finitely many questions to $\emptyset'$ at each step. The sequence $X$ is the leftmost path of $T$, that is, the least member of $\mathcal P$ in the lexicographic order.
:::

The proposition is the **Kreisel basis theorem**: the sets computable in $\emptyset'$ form a basis for the $\Pi^0_1$ classes, in the sense that every non-empty $\Pi^0_1$ class has a member among them. The next lesson improves it considerably. The leftmost member is in fact the limit of a computable sequence of approximations that only move to the right, since the leftmost node of $T$ at length $s$ moves right as $s$ grows; its degree is c.e. (Soare, Theorem 8.5.1(iii)).

## Isolated members

:::definition{#def-isolated}
A member $X$ of a class $\mathcal P$ is **isolated** if there is a string $\sigma \prec X$ with $[\sigma] \cap \mathcal P = \{ X \}$. A non-empty closed class without isolated members is **perfect**.
:::

:::example{#ex-isolated}
1. Every member of a finite class is isolated.
2. In the class $\{ 0^\infty \} \cup \{ 0^n 1 0^\infty : n \in \nat \}$, each $0^n 1 0^\infty$ is isolated by the string $0^n 1$, but $0^\infty$ is not: every prefix $0^k$ of it is also a prefix of $0^k 1 0^\infty$. The class is countable and closed, and it is a $\Pi^0_1$ class: a sequence is outside it if and only if it has a prefix with two ones.
3. $\cs$ is perfect, and so is the class $\{ X : X(2n) = 0 \text{ for all } n \}$.
4. The class $[0] \cup \{ 1 0^\infty \}$ is uncountable and has the isolated member $1 0^\infty$.
:::

An isolated member is the only path through the subtree above an isolating prefix. To compute it, one follows that subtree: at each step one of the two successors is not extendible, and by effective compactness this is eventually detected, while the other successor is never rejected.

:::proposition{#prop-isolated-computable}
Every isolated member of a $\Pi^0_1$ class is computable.
:::

:::proof{of=prop-isolated-computable}
Let $\mathcal P = [T]$ with $T$ computable, and $\sigma \prec X$ with $[\sigma] \cap \mathcal P = \{ X \}$. We compute $X(n)$ for $n \geq |\sigma|$ by induction, the bits below $|\sigma|$ being given by $\sigma$. Suppose $\tau = X \uh n$ is known, with $n \geq |\sigma|$. The two strings $\tau 0$ and $\tau 1$ extend $\sigma$; the one that is a prefix of $X$ is extendible, and the other one is not, since a path through it would be a second member of $[\sigma] \cap \mathcal P$. Non-extendibility is a $\Sigma^0_1$ property (:ref{#prop-pi01-emptiness}), so a search eventually finds which of $\tau 0$ and $\tau 1$ is not extendible, and never wrongly reports the other one. Set $X(n)$ to the other bit.
:::

:::theorem{#thm-perfect-continuum}
Let $\mathcal P$ be a perfect class. Then there is an injective map $Z \mapsto X_Z$ from $\cs$ into $\mathcal P$. In particular, $\mathcal P$ has the cardinality of the continuum.
:::

:::proof{of=thm-perfect-continuum}
The idea is to find a copy of the full binary tree inside $T$: above every node used so far, two members of $\mathcal P$ separate, which gives two incompatible extensions, and each of them is split again. Let $\mathcal P = [T]$, with $T$ the tree of prefixes of members of $\mathcal P$, so that every node of $T$ is extendible. We define strings $\sigma_\rho \in T$, for $\rho \in \bstr$, such that $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ are incompatible extensions of $\sigma_\rho$. Let $\sigma_\varepsilon = \varepsilon$. Given $\sigma_\rho \in T$, let $X$ be a member of $\mathcal P$ through $\sigma_\rho$. Since $X$ is not isolated, $[\sigma_\rho] \cap \mathcal P$ contains a member $Y \neq X$. If $n$ is the first position where they differ, the strings $X \uh (n+1)$ and $Y \uh (n+1)$ are incompatible extensions of $\sigma_\rho$ in $T$. Let $\sigma_{\rho 0}, \sigma_{\rho 1}$ be the first pair of incompatible extensions of $\sigma_\rho$ in $T$, in a fixed enumeration of pairs of strings; this avoids any arbitrary choice.

For $Z \in \cs$, the classes $[\sigma_{Z \uh k}] \cap \mathcal P$ form a decreasing sequence of non-empty closed classes, so their intersection is non-empty (:ref{#prop-cantor-compact}), and it contains a single sequence $X_Z$, since the lengths of the strings $\sigma_{Z \uh k}$ increase. If $Z \neq Z'$ first differ at position $k$, then $X_Z$ and $X_{Z'}$ extend the incompatible strings $\sigma_{(Z \uh k) 0}$ and $\sigma_{(Z \uh k) 1}$, so they are different.
:::

:::figure[The strings $\sigma_\rho$ of the proof of :ref{#thm-perfect-continuum}, for $|\rho| \leq 2$. The map $\rho \mapsto \sigma_\rho$ embeds the full binary tree into $T$, preserving the prefix order and incompatibility; a sequence $Z$ selects the branch $\sigma_{Z \uh 0} \prec \sigma_{Z \uh 1} \prec \cdots$, whose union is $X_Z$.]
<svg class="fig" viewBox="0 0 600 290" width="600" role="img" aria-label="Strings sigma_rho: each one has two incompatible extensions sigma_rho0 and sigma_rho1 in the tree"><line x1="300.0" y1="24" x2="160.0" y2="66" class="ink-stroke" stroke-width="1.3"/><line x1="160.0" y1="66" x2="90.0" y2="108" class="ink-stroke" stroke-width="1.3"/><line x1="160.0" y1="66" x2="230.0" y2="108" class="ink-stroke" stroke-width="1.3"/><line x1="90.0" y1="108" x2="55.0" y2="150" class="ink-stroke" stroke-width="1.3"/><line x1="90.0" y1="108" x2="125.0" y2="150" class="ink-stroke" stroke-width="1.3"/><line x1="230.0" y1="108" x2="265.0" y2="150" class="ink-stroke" stroke-width="1.3"/><line x1="125.0" y1="150" x2="142.5" y2="192" class="ink-stroke" stroke-width="1.3"/><line x1="265.0" y1="150" x2="247.5" y2="192" class="ink-stroke" stroke-width="1.3"/><line x1="265.0" y1="150" x2="282.5" y2="192" class="ink-stroke" stroke-width="1.3"/><line x1="247.5" y1="192" x2="238.8" y2="234" class="ink-stroke" stroke-width="1.3"/><line x1="55.0" y1="150" x2="48.0" y2="172" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="55.0" y1="150" x2="62.0" y2="172" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="55.0" y="190" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><line x1="142.5" y1="192" x2="135.5" y2="214" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="142.5" y1="192" x2="149.5" y2="214" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="142.5" y="232" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><line x1="238.8" y1="234" x2="231.8" y2="256" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="238.8" y1="234" x2="245.8" y2="256" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="238.8" y="274" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><line x1="282.5" y1="192" x2="275.5" y2="214" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="282.5" y1="192" x2="289.5" y2="214" class="muted-stroke" stroke-width="1.2" stroke-dasharray="3 3"/><text x="282.5" y="232" text-anchor="middle" class="mrm muted" font-size="12">⋮</text><circle cx="160.0" cy="66" r="2.5" class="ink-fill"/><circle cx="230.0" cy="108" r="2.5" class="ink-fill"/><circle cx="125.0" cy="150" r="2.5" class="ink-fill"/><circle cx="247.5" cy="192" r="2.5" class="ink-fill"/><circle cx="300.0" cy="24" r="5" class="accent-fill"/><text x="309.0" y="28" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">ε</tspan></text><circle cx="90.0" cy="108" r="5" class="accent-fill"/><text x="81.0" y="112" text-anchor="end" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><circle cx="265.0" cy="150" r="5" class="accent-fill"/><text x="274.0" y="154" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><circle cx="55.0" cy="150" r="5" class="accent-fill"/><text x="46.0" y="154" text-anchor="end" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">00</tspan></text><circle cx="142.5" cy="192" r="5" class="accent-fill"/><text x="151.5" y="196" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">01</tspan></text><circle cx="238.8" cy="234" r="5" class="accent-fill"/><text x="229.8" y="238" text-anchor="end" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">10</tspan></text><circle cx="282.5" cy="192" r="5" class="accent-fill"/><text x="291.5" y="196" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">11</tspan></text><circle cx="406" cy="70" r="5" class="accent-fill"/><text x="418" y="74" class="label">the strings σ<tspan font-size="9" dy="3">ρ</tspan></text><circle cx="406" cy="92" r="2.5" class="ink-fill"/><text x="418" y="96" class="label">other nodes of T</text></svg>
:::

The theorem is one half of the Cantor–Bendixson analysis of closed classes. Removing the isolated members of a closed class, and iterating this operation transfinitely, taking intersections at limit stages, ends with a class that is empty or perfect, the **perfect kernel**; the members removed along the way form a countable set. So a closed class is countable if and only if its perfect kernel is empty. The effective study of this iteration for $\Pi^0_1$ classes goes back to Kreisel (1959); see Cenzer and Remmel's survey.

:::corollary{#cor-countable-computable}
1. Every countable non-empty $\Pi^0_1$ class has a computable member; in particular, every member of a finite $\Pi^0_1$ class is computable.
2. A non-empty $\Pi^0_1$ class without computable member is perfect, and has the cardinality of the continuum.
:::

:::proof{of=cor-countable-computable}
1. A countable non-empty closed class is not perfect, by :ref{#thm-perfect-continuum}, so it has an isolated member, which is computable by :ref{#prop-isolated-computable}. In a finite class, every member is isolated.
2. If the class had an isolated member, this member would be computable. So the class is perfect, and :ref{#thm-perfect-continuum} applies.
:::

:::quiz[isolated members]
In the proof of :ref{#prop-isolated-computable}, why does the search for a non-extendible successor of $\tau = X \uh n$ always succeed?

- [x] Because one of the two successors is not extendible: otherwise $[\sigma] \cap \mathcal P$ would contain a member other than $X$, through the successor that is not a prefix of $X$.
- [ ] Because $T$ is computable.

  Computability of $T$ makes non-extendibility $\Sigma^0_1$; the existence of a non-extendible successor comes from isolation.
- [ ] Because $X$ is the leftmost path.

  An isolated member need not be the leftmost path.

---

Why does the proof of :ref{#thm-perfect-continuum} not apply to a class with an isolated member $X$?

- [x] Above a prefix isolating $X$, there is no pair of incompatible extendible extensions, so the splitting cannot continue there.

  The construction needs two different members through each node it uses.
- [ ] Because the class is then countable.

  A class with an isolated member can still be uncountable: the isolated member may be the only one in some cylinder, while others are perfect.
- [ ] Because the map would not be injective.

  Injectivity comes from the incompatibility of the strings chosen at each splitting; the problem is that the splitting cannot be found above an isolating prefix.
:::

## A Π⁰₁ class without computable members

:::theorem{#thm-dnc2-no-computable}
The class $\mathrm{DNC}_2 = \{ X \in \cs : X(e) \neq \Phi_e(e) \text{ for every } e \text{ with } \Phi_e(e)\converge \}$ is a non-empty $\Pi^0_1$ class without computable member. It is the class of sets separating $A = \{ e : \Phi_e(e)\converge = 0 \}$ from $B = \{ e : \Phi_e(e)\converge = 1 \}$.
:::

:::proof{of=thm-dnc2-no-computable}
A set $X$ satisfies $X(e) \neq \Phi_e(e)$ for all $e$ with $\Phi_e(e)\converge$ if and only if $X(e) = 1$ for $e \in A$ and $X(e) = 0$ for $e \in B$, since $X(e)$ can only equal $0$ or $1$; so $\mathrm{DNC}_2$ is the class of separating sets $\mathcal S(A, B)$, which is $\Pi^0_1$ by :ref{#ex-pi01-classes}. It is non-empty: $A$ itself separates $A$ from $B$.

Suppose $X \in \mathrm{DNC}_2$ is computable, and let $c$ be an index of its characteristic function, so that $\Phi_c$ is total with values in $\{0, 1\}$. Then $\Phi_c(c)\converge = X(c)$, contradicting $X(c) \neq \Phi_c(c)$.
:::

The proof is a diagonal argument in the sense of the course on countability: a computable member would have an index, and the member differs from the function of that index at that index. By :ref{#cor-countable-computable}, the class $\mathrm{DNC}_2$ is perfect and has continuum many members, none of them computable. The class plays a central role in the next lessons: its members are the $\{0, 1\}$-valued diagonally non-computable functions, and the sets that compute one of them are the sets of **PA degree** (:ref{#def-pa-degree}).

:::quiz[the class DNC₂]
Why is the class $\mathrm{DNC}_2$ non-empty, although none of its members is computable?

- [x] Because the c.e. set $A = \{ e : \Phi_e(e)\converge = 0 \}$ is a member: it has the value $1$ on $A$ and $0$ on $B$.

  A member may be c.e. without being computable; $A$ is c.e. and not computable.
- [ ] By weak König's lemma applied to a finite tree.

  Weak König's lemma applies to infinite trees; here an explicit member is available.
- [ ] Because every $\Pi^0_1$ class is non-empty.

  The empty class is a $\Pi^0_1$ class.
:::

## Exercises

::::exercise{difficulty=1}
Give a $\Pi^0_1$ class whose leftmost member is $\emptyset'$, and deduce that the leftmost member of a $\Pi^0_1$ class may compute $\emptyset'$.

:::solution
The class $\{ X : \emptyset' \subseteq X \}$ is $\Pi^0_1$: $X$ is outside it if and only if some $n$ enters $\emptyset'$ with $X(n) = 0$, a $\Sigma^0_1$ condition on prefixes. Its least member in the lexicographic order has the bit $0$ wherever possible, that is, outside $\emptyset'$, so it is $\emptyset'$.
:::
::::

::::exercise{difficulty=2}
Let $(T_e)$ be an enumeration of the computable trees, given by indices. Show that the set of $e$ such that $[T_e]$ has a computable member is $\Sigma^0_3$.

:::solution
$[T_e]$ has a computable member if and only if there is $i$ such that $\Phi_i$ is total with values in $\{0, 1\}$, and every prefix of the sequence $\Phi_i$ belongs to $T_e$. The first condition is $\Pi^0_2$. Given it, the second is equivalent to "for all $n$ and $s$, if $\Phi_i(0), \dots, \Phi_i(n-1)$ converge at stage $s$, the string they form belongs to $T_e$". Membership of a string in $T_e$ is decidable, but as a relation in $e$ it is $\Sigma^0_1$ (some computation of the characteristic function of $T_e$ outputs $1$), so this condition is $\Pi^0_2$. So the condition on $(e, i)$ is $\Pi^0_2$, and its projection over $i$ is $\Sigma^0_3$.
:::
::::

## Notes and references

The basis theorem for $\emptyset'$ is credited to Kreisel (1953) by Cenzer and Remmel and by Hirschfeldt; Kreisel proved it for trees given by primitive recursive predicates, in a paper on the foundations of arithmetic (Dean and Walsh, Section 4.1). Monin and Patey credit it to Kreisel (1959). The analysis of $\Pi^0_1$ classes by the Cantor–Bendixson derivative, and the computability of a member of every countable $\Pi^0_1$ class, go back to Kreisel (1959); the members of countable $\Pi^0_1$ classes were studied in detail by Cenzer, Clote, Smith, Soare and Wainer (1986). Kleene (1952) gave the first computable infinite binary tree without computable path, the tree of consistent extensions of an essentially undecidable theory, in a study of the fan theorem of intuitionistic analysis (Dean and Walsh, Section 4.2); Hirschfeldt (Corollary 3.7) credits the same fact to Kreisel (1953).

Soare's *Turing Computability* proves the Kreisel basis theorem, the computability of isolated paths and the existence of a $\Pi^0_1$ class without computable member in Theorem 8.5.1 and Theorem 9.3.2; Nies proves them as Facts 1.8.31, 1.8.33 and 1.8.36.

- G. Kreisel, *A variant to Hilbert's theory of the foundations of arithmetic*, British Journal for the Philosophy of Science 4 (1953), 107–129.
- G. Kreisel, *Analysis of the Cantor–Bendixson theorem by means of the analytic hierarchy*, Bulletin de l'Académie Polonaise des Sciences, Série des Sciences Mathématiques, Astronomiques et Physiques 7 (1959), 621–626.
- S. C. Kleene, *Recursive functions and intuitionistic mathematics*, in *Proceedings of the International Congress of Mathematicians, Cambridge, Massachusetts, 1950*, Volume 1, American Mathematical Society, 1952, 679–685.
- W. Dean and S. Walsh, *The prehistory of the subsystems of second-order arithmetic*, arXiv:1612.06219, 2016, Section 4.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 8.5 and 9.3.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 1.8.
- D. R. Hirschfeldt, *Slicing the Truth*, Lecture Notes Series of the Institute for Mathematical Sciences, National University of Singapore, 28, World Scientific, 2015, Section 3.1.
- D. Cenzer, P. Clote, R. L. Smith, R. I. Soare and S. S. Wainer, *Members of countable Π⁰₁ classes*, Annals of Pure and Applied Logic 31 (1986), 145–163.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. Cenzer and J. B. Remmel, *Π⁰₁ classes in mathematics*, in *Handbook of Recursive Mathematics*, Volume 2, Studies in Logic 139, North-Holland, 1998, 623–821.
