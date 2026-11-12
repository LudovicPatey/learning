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

## Exercises

::::exercise{#ex-bi-immune difficulty=3}
Show that there is a set $Y$ such that neither $Y$ nor its complement contains an infinite computable set.

:::hint
For each infinite computable set $C$, the requirement is: $C \not\subseteq Y$ and $C \not\subseteq \nat \setminus Y$. Satisfy it by a finite extension.
:::

:::solution
The infinite computable sets form a countably infinite set, by :ref{#prop-countably-many-computable} and :ref{#cor-subset-countable} (it contains the sets $\nat \setminus \underline n$); let $C_0, C_1, \dots$ be an enumeration of them. Requirement $R_{2n}$: $Y(m) = 0$ for some $m \in C_n$; requirement $R_{2n+1}$: $Y(m) = 1$ for some $m \in C_n$. Given $\sigma$, since $C_n$ is infinite there is $m \in C_n$ with $m \geq |\sigma|$; extend $\sigma$ by zeros to length $m$, then append the required bit. Every $Y$ extending the result satisfies the requirement. By :ref{#lem-finite-extension}, some $Y$ satisfies all requirements: each infinite computable set meets both $Y$ and its complement, so it is contained in neither. Such a set is called **bi-immune**. The definition in the course on immunity (:ref{#def-immune}) uses infinite c.e. sets instead of infinite computable sets; the two versions are equivalent, since every infinite c.e. set has an infinite computable subset.
:::
::::


::::exercise{difficulty=1}
Show that a bi-immune set is not computable. Which step of the construction of the previous exercise is not effective?

:::solution
Let $Y$ be computable. Since $\nat = Y \cup (\nat \setminus Y)$ is infinite, one of $Y$ and $\nat \setminus Y$ is infinite, a union of two finite sets being finite. That set is computable, as $Y$ is, and it is contained in itself; so $Y$ is not bi-immune.

In the construction, the step from $\sigma$ to its extension is effective as soon as $C_n$ is given by an algorithm: search for the least $m \geq |\sigma|$ in $C_n$. What is not effective is the enumeration $C_0, C_1, \dots$ itself: by :ref{#ex-no-uniform-computable-sets}, no uniformly computable sequence contains all computable sets. Compare with :ref{#prop-infinitely-different}, where the list is uniformly computable and the resulting $Y$ is computable.
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
