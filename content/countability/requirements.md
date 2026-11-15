---
title: Diagonalization by requirements
summary: Constructions by finite extensions; requirements that can always be secured; sequences differing infinitely often from every member of a list; bi-immune sets.
duration: 35
prerequisites: [diagonalization-and-computation]
---

The diagonal argument builds a sequence $Y$ that differs from each member of a list, by fixing one bit for each member. Most constructions of computability theory have the same structure, with more complicated conditions in place of "$Y \neq X_n$": a list of **requirements**, and a construction of $Y$ by finite pieces in which each requirement is taken care of at its turn. This lesson isolates the simplest version, the **finite extension method**, in which every requirement can be secured by a finite piece of $Y$, whatever was decided before. It is the method of the Kleene–Post theorem in the course on Turing degrees, and the simplest form of forcing.

## Requirements and finite extensions

In the diagonal argument, the sequence $Y$ is built to satisfy infinitely many conditions, $Y \neq X_n$ for each $n$, each of which can be secured by fixing a single bit. Constructions in computability theory are usually organized in this way: one lists **requirements** $R_0, R_1, R_2, \dots$, and builds the desired object by finite approximations, ensuring each requirement at its turn.

For strings $\sigma, \tau \in 2^{<\nat}$, write $\sigma \preceq \tau$ if $\sigma$ is a prefix of $\tau$, and $\sigma \prec X$ if $\sigma$ is a prefix of $X \in \cs$. A requirement is a property of elements of $\cs$, that is, a subset $R \subseteq \cs$. A string $\tau$ **secures** $R$ if every $X \succ \tau$ satisfies $R$: once $\tau$ is an initial segment of the sequence under construction, $R$ holds whatever the remaining bits are. For instance, the string $\tau = 01$ secures the requirement "$Y \neq X$" for every $X$ with $X(1) = 0$.

The construction maintains a finite string, the part of $Y$ decided so far. At step $e$, it extends this string to one that secures $R_e$. A requirement secured at some step stays secured at every later step, since later strings extend the earlier ones. The only hypothesis needed is that every requirement can be secured, starting from any string.

:::lemma[Finite extension]{#lem-finite-extension}
Let $(R_e)_{e \in \nat}$ be a sequence of requirements such that for every $e$ and every $\sigma \in 2^{<\nat}$, there is $\tau \succeq \sigma$ such that every $X \succ \tau$ satisfies $R_e$. Then there is $Y \in \cs$ satisfying every $R_e$.
:::

:::proof{of=lem-finite-extension}
Fix an enumeration $\rho_0, \rho_1, \dots$ of $2^{<\nat}$, given by :ref{#prop-strings-countable}. If $\tau$ is as in the hypothesis, so is every extension of $\tau$; in particular there is such a $\tau$ with $|\tau| > |\sigma|$. Define $\sigma_0$ as the empty string and $\sigma_{e+1}$ as the first $\rho_i$ such that $\rho_i \succeq \sigma_e$, $|\rho_i| > |\sigma_e|$, and every $X \succ \rho_i$ satisfies $R_e$. The strings $\sigma_0 \preceq \sigma_1 \preceq \cdots$ have strictly increasing lengths, so there is a unique $Y \in \cs$ with $\sigma_e \prec Y$ for every $e$: its $n$-th bit is the $n$-th bit of any $\sigma_e$ of length greater than $n$. Since $\sigma_{e+1} \prec Y$, $Y$ satisfies $R_e$.
:::

Choosing $\sigma_{e+1}$ as the first suitable string in a fixed enumeration avoids any use of the axiom of choice, and makes the construction explicit.

:::figure[The first stages of a construction by finite extensions. Each string $\sigma_{e+1}$ keeps $\sigma_e$ (muted) and appends a finite block (shaded) after which $R_e$ is secured. The sequence $Y$ extends every $\sigma_e$.]
<svg class="fig" viewBox="0 0 520 210" width="520" role="img" aria-label="Successive strings of a finite extension construction, each extending the previous one by a block"><text x="34" y="37" text-anchor="middle" class="mrm" font-size="16">σ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="70" y="18" width="28" height="28" class="cell head-cell"/><text x="84.0" y="37" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="98" y="18" width="28" height="28" class="cell head-cell"/><text x="112.0" y="37" text-anchor="middle" class="mrm" font-size="14">1</text><text x="138" y="37" class="label">secures</text><text x="192" y="37" text-anchor="start" class="math" font-size="15">R<tspan class="mrm" font-size="10" dy="4">0</tspan></text><text x="34" y="77" text-anchor="middle" class="mrm" font-size="16">σ<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="70" y="58" width="28" height="28" class="cell"/><text x="84.0" y="77" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="98" y="58" width="28" height="28" class="cell"/><text x="112.0" y="77" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="126" y="58" width="28" height="28" class="cell head-cell"/><text x="140.0" y="77" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="154" y="58" width="28" height="28" class="cell head-cell"/><text x="168.0" y="77" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="182" y="58" width="28" height="28" class="cell head-cell"/><text x="196.0" y="77" text-anchor="middle" class="mrm" font-size="14">0</text><text x="222" y="77" class="label">secures</text><text x="276" y="77" text-anchor="start" class="math" font-size="15">R<tspan class="mrm" font-size="10" dy="4">1</tspan></text><text x="34" y="117" text-anchor="middle" class="mrm" font-size="16">σ<tspan class="mrm" font-size="10" dy="4">3</tspan></text><rect x="70" y="98" width="28" height="28" class="cell"/><text x="84.0" y="117" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="98" y="98" width="28" height="28" class="cell"/><text x="112.0" y="117" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="126" y="98" width="28" height="28" class="cell"/><text x="140.0" y="117" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="154" y="98" width="28" height="28" class="cell"/><text x="168.0" y="117" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="182" y="98" width="28" height="28" class="cell"/><text x="196.0" y="117" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="210" y="98" width="28" height="28" class="cell head-cell"/><text x="224.0" y="117" text-anchor="middle" class="mrm" font-size="14">1</text><text x="250" y="117" class="label">secures</text><text x="304" y="117" text-anchor="start" class="math" font-size="15">R<tspan class="mrm" font-size="10" dy="4">2</tspan></text><text x="34" y="157" text-anchor="middle" class="mrm" font-size="16">σ<tspan class="mrm" font-size="10" dy="4">4</tspan></text><rect x="70" y="138" width="28" height="28" class="cell"/><text x="84.0" y="157" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="98" y="138" width="28" height="28" class="cell"/><text x="112.0" y="157" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="126" y="138" width="28" height="28" class="cell"/><text x="140.0" y="157" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="154" y="138" width="28" height="28" class="cell"/><text x="168.0" y="157" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="182" y="138" width="28" height="28" class="cell"/><text x="196.0" y="157" text-anchor="middle" class="mrm muted" font-size="14">0</text><rect x="210" y="138" width="28" height="28" class="cell"/><text x="224.0" y="157" text-anchor="middle" class="mrm muted" font-size="14">1</text><rect x="238" y="138" width="28" height="28" class="cell head-cell"/><text x="252.0" y="157" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="266" y="138" width="28" height="28" class="cell head-cell"/><text x="280.0" y="157" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="294" y="138" width="28" height="28" class="cell head-cell"/><text x="308.0" y="157" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="322" y="138" width="28" height="28" class="cell head-cell"/><text x="336.0" y="157" text-anchor="middle" class="mrm" font-size="14">0</text><text x="362" y="157" class="label">secures</text><text x="416" y="157" text-anchor="start" class="math" font-size="15">R<tspan class="mrm" font-size="10" dy="4">3</tspan></text><text x="34" y="197" text-anchor="middle" class="math" font-size="16">Y</text><rect x="70" y="178" width="28" height="28" class="cell"/><text x="84.0" y="197" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="98" y="178" width="28" height="28" class="cell"/><text x="112.0" y="197" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="126" y="178" width="28" height="28" class="cell"/><text x="140.0" y="197" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="154" y="178" width="28" height="28" class="cell"/><text x="168.0" y="197" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="182" y="178" width="28" height="28" class="cell"/><text x="196.0" y="197" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="210" y="178" width="28" height="28" class="cell"/><text x="224.0" y="197" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="238" y="178" width="28" height="28" class="cell"/><text x="252.0" y="197" text-anchor="middle" class="mrm" font-size="14">0</text><rect x="266" y="178" width="28" height="28" class="cell"/><text x="280.0" y="197" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="294" y="178" width="28" height="28" class="cell"/><text x="308.0" y="197" text-anchor="middle" class="mrm" font-size="14">1</text><rect x="322" y="178" width="28" height="28" class="cell"/><text x="336.0" y="197" text-anchor="middle" class="mrm" font-size="14">0</text><text x="360" y="197" class="mrm muted" font-size="15">⋯</text></svg>
:::

The hypothesis of the lemma cannot be dropped. The requirement "$Y$ has infinitely many ones" is secured by no string, since every $\tau$ has the extension $\tau 000 \cdots$; and the two requirements "$Y(0) = 0$" and "$Y(0) = 1$" cannot both be satisfied, the second being secured by no extension of the string $0$. In the first case the remedy is to split the requirement into the infinitely many requirements "$Y(m) = 1$ for some $m \geq k$", for $k \in \nat$, each of which can be secured. The proposition below uses the same device.

:::example{#ex-finite-extension-diagonal}
Let $(X_n)$ be a sequence in $\cs$, and $R_n = \{ Y : Y \neq X_n \}$. Given $\sigma$, the string $\tau = \sigma \, i$ with $i = 1 - X_n(|\sigma|)$ satisfies the hypothesis: every $Y \succ \tau$ differs from $X_n$ at position $|\sigma|$. This is the diagonal argument, except that the position at which $X_n$ is defeated is now chosen by the construction rather than fixed in advance.
:::

## Differing infinitely often

The diagonal argument defeats each $X_n$ at one position. A stronger requirement asks that $Y$ differ from $X_n$ at infinitely many positions, so that no finite modification of $X_n$ equals $Y$. As explained above, this is not a requirement that a finite string can secure, but it splits into infinitely many requirements that can.

:::proposition{#prop-infinitely-different}
For every sequence $(X_n)$ in $\cs$, there is $Y \in \cs$ that differs from every $X_n$ at infinitely many positions. If $(X_n)$ is uniformly computable, $Y$ can be taken computable.
:::

:::proof{of=prop-infinitely-different}
For $e = \langle n, k \rangle$, let $R_e$ be the requirement "$Y(m) \neq X_n(m)$ for some $m \geq k$". Given $\sigma$, extend it by zeros to a string $\sigma'$ of length at least $k$, and let $\tau = \sigma' i$ with $i = 1 - X_n(|\sigma'|)$; every $Y \succ \tau$ differs from $X_n$ at the position $|\sigma'| \geq k$. By :ref{#lem-finite-extension}, some $Y$ satisfies all $R_{\langle n, k \rangle}$, that is, differs from each $X_n$ beyond every $k$.

If $(X_n)$ is uniformly computable, use the explicit extension above instead of a search in an enumeration: $\sigma_{e+1}$ is obtained from $\sigma_e$ by padding with zeros to length $\max(k, |\sigma_e|)$ and appending the bit $1 - X_n(\ell)$, where $\ell = \max(k, |\sigma_e|)$; both steps are computable from $\sigma_e$ and $e = \langle n, k \rangle$. Then $e \mapsto \sigma_e$ is computable, and so is $Y$, since $Y(m)$ is the $m$-th bit of $\sigma_{m+1}$, which has length at least $m + 1$.
:::

The requirements of this proposition never interfere: once a requirement is satisfied, it remains satisfied whatever is done afterwards. Requirements of this kind can be handled one after the other, by finite extensions. The method was introduced by Kleene and Post to build Turing degrees with prescribed properties (:ref{to="turing-degrees/finite-extensions"}), and it is the elementary case of **forcing**: the set of strings that secure $R_e$ is what that lesson calls a dense set. When requirements conflict, so that satisfying one may later injure another, one needs the **priority method**, which is the main technique of the theory of computably enumerable sets.

:::quiz[the finite extension lemma]
Why does the proof of :ref{#lem-finite-extension} require $|\sigma_{e+1}| > |\sigma_e|$?

- [x] To ensure that the lengths tend to infinity, so that the strings $\sigma_e$ determine a whole infinite sequence $Y$.

  Without it, the construction could stall on a single finite string, which determines no element of $\cs$.
- [ ] To ensure that $\sigma_{e+1}$ extends $\sigma_e$.

  This is required separately, by $\rho_i \succeq \sigma_e$.
- [ ] To ensure that $Y$ satisfies $R_e$.

  That is ensured by the choice of $\sigma_{e+1}$ among the strings all of whose extensions satisfy $R_e$.

---

In the computable part of :ref{#prop-infinitely-different}, why is the explicit extension used rather than the search of the lemma?

- [x] The search tests the condition "every $X \succ \rho_i$ satisfies $R_e$", a property of infinitely many sequences, which is not in general decidable.

  The explicit extension computes a suitable string directly, so the whole construction is an algorithm.
- [ ] Because the lemma uses the axiom of choice.

  It does not: it uses a fixed enumeration of strings.
- [ ] Because the search may not terminate.

  It always terminates, by the hypothesis of the lemma; the problem is that its steps may not be computable.
:::

::::exercise{#ex-bi-immune difficulty=3 objective="Apply the finite extension method to build a set such that neither it nor its complement contains an infinite computable set."}
Show that there is a set $Y$ such that neither $Y$ nor its complement contains an infinite computable set.

:::hint
For each infinite computable set $C$, the requirement is: $C \not\subseteq Y$ and $C \not\subseteq \nat \setminus Y$. Satisfy it by a finite extension.
:::

:::solution
The infinite computable sets form a countably infinite set, by :ref{#prop-countably-many-computable} and :ref{#cor-subset-countable} (it contains the sets $\nat \setminus \underline n$); let $C_0, C_1, \dots$ be an enumeration of them. Requirement $R_{2n}$: $Y(m) = 0$ for some $m \in C_n$; requirement $R_{2n+1}$: $Y(m) = 1$ for some $m \in C_n$. Given $\sigma$, since $C_n$ is infinite there is $m \in C_n$ with $m \geq |\sigma|$; extend $\sigma$ by zeros to length $m$, then append the required bit. Every $Y$ extending the result satisfies the requirement. By :ref{#lem-finite-extension}, some $Y$ satisfies all requirements: each infinite computable set meets both $Y$ and its complement, so it is contained in neither. Such a set is called **bi-immune**. The definition in the course on immunity and growth uses infinite c.e. sets instead of infinite computable sets; the two versions are equivalent, since every infinite c.e. set has an infinite computable subset.
:::
::::

::::exercise{#ex-bi-immune-not-computable difficulty=1 objective="See that a bi-immune set is not computable, and locate the non-effective step of its construction."}
Show that a bi-immune set is not computable. Which step of the construction of :ref{#ex-bi-immune} is not effective?

:::solution
Let $Y$ be computable. Since $\nat = Y \cup (\nat \setminus Y)$ is infinite, one of $Y$ and $\nat \setminus Y$ is infinite, a union of two finite sets being finite. That set is computable, as $Y$ is, and it is contained in itself; so $Y$ is not bi-immune.

In the construction, the step from $\sigma$ to its extension is effective as soon as $C_n$ is given by an algorithm: search for the least $m \geq |\sigma|$ in $C_n$. What is not effective is the enumeration $C_0, C_1, \dots$ itself: by :ref{#ex-no-uniform-computable-sets}, no uniformly computable sequence contains all computable sets, and hence none contains all infinite computable sets: interleaving such a sequence with the uniformly computable sequence of all finite sets, the $k$-th of which is $\{ n : \text{the } n\text{-th binary digit of } k \text{ is } 1 \}$, would give one. Compare with :ref{#prop-infinitely-different}, where the list is uniformly computable and the resulting $Y$ is computable.
:::
::::

## Notes and references

The finite extension method is due to Kleene and Post (1954), who used it to build Turing degrees below $\mathbf 0'$ that are incomparable; Soare (§6.1) and Monin and Patey (chapter *Turing degrees*, section *Finite extensions method*) present it in this setting. The priority method is due to Friedberg (1957) and Muchnik (1956). Bi-immune sets were studied by Jockusch, who showed that some Turing degrees contain no bi-immune set.

- S. C. Kleene and E. L. Post, *The upper semi-lattice of degrees of recursive unsolvability*, Annals of Mathematics 59 (1954), 379–407.
- R. M. Friedberg, *Two recursively enumerable sets of incomparable degrees of unsolvability*, Proceedings of the National Academy of Sciences 43 (1957), 236–238.
- A. A. Muchnik, *On the unsolvability of the problem of reducibility in the theory of algorithms*, Doklady Akademii Nauk SSSR 108 (1956), 194–197 (in Russian).
- C. G. Jockusch, Jr., *The degrees of bi-immune sets*, Zeitschrift für Mathematische Logik und Grundlagen der Mathematik 15 (1969), 135–140.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, §6.1.
- B. Monin and L. Patey, *Computability theory*, chapter *Turing degrees*.

:::::exercises
::::exercise{#ex-secures difficulty=1 objective="Determine which strings secure a given requirement, and which requirements meet the hypothesis of the finite extension lemma."}
For each of the following requirements, describe the strings $\tau$ that secure it: (a) $Y(3) = 1$; (b) $Y(m) = 1$ for some $m < 5$; (c) $Y \neq 000\cdots$; (d) $Y$ has infinitely many ones; (e) $Y$ is not computable. Which of them, taken as a constant sequence $R_e = R$, satisfy the hypothesis of :ref{#lem-finite-extension}?

:::solution
In each case, compare with the extension $\tau 000 \cdots$ of $\tau$.

(a) $\tau$ secures the requirement if and only if $|\tau| \geq 4$ and $\tau(3) = 1$: then every extension has bit $3$ equal to $1$, while if $|\tau| \leq 3$ the extension $\tau 000 \cdots$ has bit $3$ equal to $0$, and if $\tau(3) = 0$ no extension works.

(b) $\tau$ secures it if and only if $\tau(m) = 1$ for some $m < \min(5, |\tau|)$: otherwise $\tau 000 \cdots$ has no $1$ below position $5$.

(c) $\tau$ secures it if and only if $\tau$ contains a $1$: otherwise $\tau 000 \cdots = 000 \cdots$.

(d) No string secures it, since $\tau 000 \cdots$ has finitely many ones.

(e) No string secures it, since $\tau 000 \cdots$ is computable: it is a finite set.

The hypothesis of the lemma asks for a securing extension of *every* string $\sigma$. Only (c) satisfies it, with the extension $\sigma 1$. For (a), the string $0000$ has no securing extension, and for (b) the string $00000$ has none. Requirement (e) can nevertheless be met, after splitting it into the requirements $Y \neq X_n$ for an enumeration $(X_n)$ of the computable sets, as in :ref{#ex-finite-extension-diagonal}.
:::
::::

::::exercise{#ex-three-requirements difficulty=1 objective="Interleave several families of requirements in one construction by finite extensions."}
Let $(X_n)$ be a sequence in $\cs$. Use :ref{#lem-finite-extension} to build a set $Y$ that is infinite, has an infinite complement, and differs from every $X_n$.

:::solution
Every $e$ is $3k + i$ for exactly one $k \in \nat$ and one $i < 3$. Let $R_{3k}$ be "$Y(m) = 1$ for some $m \geq k$", $R_{3k+1}$ be "$Y(m) = 0$ for some $m \geq k$", and $R_{3k+2}$ be "$Y \neq X_k$". Given $\sigma$, extend it by zeros to a string $\sigma'$ of length at least $k$, and let $\tau = \sigma' 1$ for $R_{3k}$ and $\tau = \sigma' 0$ for $R_{3k+1}$; every extension of $\tau$ has the required bit at position $|\sigma'| \geq k$. For $R_{3k+2}$, let $\tau = \sigma\, i$ with $i = 1 - X_k(|\sigma|)$, as in :ref{#ex-finite-extension-diagonal}. By the lemma, some $Y$ satisfies all the requirements. Then $Y$ has a one beyond every $k$, hence infinitely many ones, and likewise infinitely many zeros; and $Y \neq X_k$ for every $k$.
:::
::::

::::exercise{#ex-many-solutions difficulty=2 objective="Branch a construction by finite extensions to obtain continuum many solutions."}
Let $(R_e)$ satisfy the hypothesis of :ref{#lem-finite-extension}. Show that the set of $Y \in \cs$ satisfying every $R_e$ has the cardinality of the continuum.

:::solution
Fix an enumeration $\rho_0, \rho_1, \dots$ of $2^{<\nat}$. For $X \in \cs$, define strings $\sigma^X_e$ by $\sigma^X_0 = \varepsilon$, and let $\sigma^X_{e+1}$ be the first $\rho_i$ that extends the string $\sigma^X_e X(e)$, obtained by appending the bit $X(e)$, and secures $R_e$; it exists by the hypothesis applied to $\sigma^X_e X(e)$. The lengths increase strictly, so there is a unique $Y_X$ extending every $\sigma^X_e$, and $Y_X$ satisfies every $R_e$, as in the proof of the lemma.

The map $X \mapsto Y_X$ is injective. Let $X \neq X'$, and let $e$ be the least position where they differ. The string $\sigma^X_{e'+1}$ depends only on $\sigma^X_{e'}$ and $X(e')$, so by induction $\sigma^X_{e'} = \sigma^{X'}_{e'}$ for $e' \leq e$. Let $\ell = |\sigma^X_e|$. Then $Y_X(\ell) = X(e)$ and $Y_{X'}(\ell) = X'(e)$, since $\sigma^X_{e+1}$ extends $\sigma^X_e X(e)$; so $Y_X \neq Y_{X'}$.

So $\cs$ injects into the set of solutions, which is a subset of $\cs$; by :ref{#thm-cantor-bernstein}, it is equipotent to $\cs$, hence has the cardinality of the continuum (:ref{#thm-continuum}). The same branching, with requirements on pairs of branches, is used in Soare 2016, Exercise 6.1.7, to build continuum many pairwise incomparable Turing degrees.
:::
::::

::::exercise{#ex-bi-immune-splits difficulty=1 objective="Reformulate bi-immunity in terms of intersections with infinite computable sets."}
Show that a set $Y$ is bi-immune, in the sense of :ref{#ex-bi-immune}, if and only if, for every infinite computable set $C$, both $C \cap Y$ and $C \setminus Y$ are infinite.

:::solution
If both sets are infinite for every infinite computable $C$, then no such $C$ is contained in $Y$, since $C \setminus Y \neq \emptyset$, or in $\nat \setminus Y$, since $C \cap Y \neq \emptyset$. So $Y$ is bi-immune.

Conversely, let $Y$ be bi-immune and $C$ infinite computable. If $F = C \cap Y$ were finite, then $C \setminus F = C \setminus Y$ would be infinite, by :ref{#ex-remove-finite}, and computable: to decide $m \in C \setminus F$, decide $m \in C$ and compare $m$ with the finitely many elements of $F$, which the algorithm can list. It would be an infinite computable subset of $\nat \setminus Y$, a contradiction. Symmetrically, if $C \setminus Y$ were finite, then $C \cap Y$ would be an infinite computable subset of $Y$.
:::
::::

::::exercise{#ex-effective-finite-extension difficulty=2 objective="Effectivize the finite extension lemma when securing extensions can be computed."}
Let $(R_e)$ be a sequence of requirements, and let $s$ be a total computable function, defined on pairs $(e, \sigma)$ with $e \in \nat$ and $\sigma \in 2^{<\nat}$ (strings being coded by integers), such that $s(e, \sigma) \succeq \sigma$, $|s(e, \sigma)| > |\sigma|$, and $s(e, \sigma)$ secures $R_e$. Show that some computable $Y$ satisfies every $R_e$. Apply this to a uniformly computable sequence $(X_n)$ and the requirements $Y \neq X_n$, and compare the resulting $Y$ with the diagonal sequence of :ref{#ex-no-uniform-computable-sets}.

:::solution
Let $\sigma_0 = \varepsilon$ and $\sigma_{e+1} = s(e, \sigma_e)$. Then $e \mapsto \sigma_e$ is computable, by iterating $s$, and $|\sigma_e| \geq e$. Let $Y$ be the unique sequence extending every $\sigma_e$; then $Y(m)$ is the $m$-th bit of $\sigma_{m+1}$, which has length at least $m + 1$, so $Y$ is computable. Since $\sigma_{e+1} \prec Y$ and $\sigma_{e+1}$ secures $R_e$, $Y$ satisfies $R_e$.

For $R_n$: $Y \neq X_n$, let $s(n, \sigma) = \sigma\, i$ with $i = 1 - X_n(|\sigma|)$; it is computable since $(n, m) \mapsto X_n(m)$ is. Then $|\sigma_n| = n$ for every $n$, and $\sigma_{n+1}$ appends the bit $1 - X_n(n)$. So $Y(n) = 1 - X_n(n)$: the construction is exactly the diagonal argument of :ref{#ex-no-uniform-computable-sets}.
:::
::::

::::exercise{#ex-avoid-pr-sets difficulty=2 objective="Apply the computable form of the construction to a uniformly computable list of all primitive recursive sets."}
A set is **primitive recursive** if its characteristic function is. Using that the primitive recursive functions form a uniformly computable sequence $(f_e)$, as recalled in the previous lesson, show that there is a computable set $Y$ such that $Y \mathbin{\triangle} P$ is infinite for every primitive recursive set $P$. Deduce that no finite modification of $Y$ is primitive recursive.

:::solution
Let $X_e = \{ m : f_e(m) \geq 1 \}$. Then $(e, m) \mapsto X_e(m) = \min(f_e(m), 1)$ is computable, so $(X_e)$ is uniformly computable. Every primitive recursive set $P$ occurs in it: its characteristic function is some $f_e$, and then $X_e = P$. By :ref{#prop-infinitely-different}, there is a computable $Y$ that differs from every $X_e$ at infinitely many positions, that is, $Y \mathbin{\triangle} X_e$ is infinite for every $e$. If a finite modification $Y \mathbin{\triangle} F$ of $Y$, with $F$ finite, were a primitive recursive set $P$, then $Y \mathbin{\triangle} P = F$ would be finite, a contradiction.
:::
::::
:::::
