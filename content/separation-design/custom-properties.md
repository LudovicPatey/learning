---
title: Custom properties and immunity
summary: Separations between Ramsey-type problems need weakness properties designed for the pair of problems; solutions closed under subsets are immune; hyperimmunity, constant-bound immunity and effective immunity as strengthenings of immunity; the property preserved by weak König's lemma read off its forcing question.
duration: 40
prerequisites: [avoidance/hyperimmunities, compactness-avoidance/dnc-avoidance, immunity-growth/dnc-functions, pi01-classes/finitely-branching-trees]
---

The previous courses of the track separate problems by a few classical weakness properties: avoiding a cone, not being PA, preserving a hyperimmune function, being low. They do not separate the Ramsey-type problems below Ramsey's theorem for pairs: the Erdős–Moser theorem, the chain–antichain principle and the ascending–descending sequence principle avoid cones, avoid PA degrees and preserve one hyperimmune function, as $\mathsf{RT}^2_2$ does. To separate them, one designs a weakness property for the pair of problems at hand. This course shows how such properties are found, and how a notion of forcing is designed for a problem. This lesson sets up the method and the properties used throughout: the variants of immunity.

## The method

Recall the framework of :ref{to="reducibilities/preservation"}. A weakness property is a class $\mathcal W$ closed downwards under $\leq_T$; a problem $\mathsf Q$ preserves $\mathcal W$ if for every $Z \in \mathcal W$, every instance $X \leq_T Z$ has a solution $Y$ with $Z \oplus Y \in \mathcal W$ (:ref{#def-weakness}). If $\mathsf Q$ preserves $\mathcal W$ and $\mathsf P$ does not, then $\mathsf P \not\leq_\omega \mathsf Q$ (:ref{#thm-preservation-separation}), which gives an ω-model of $\mathsf{RCA}_0 + \mathsf Q$ that is not a model of $\mathsf P$. A separation of $\mathsf P$ from $\mathsf Q$ thus has two halves:

1. a **preservation theorem**: $\mathsf Q$ preserves $\mathcal W$, usually proved with a notion of forcing for $\mathsf Q$;
2. a **separating instance**: some $Z \in \mathcal W$ computes an instance of $\mathsf P$ all of whose solutions $Y$ have $Z \oplus Y \notin \mathcal W$, usually built by a priority argument or a limit construction.

The two halves pull in opposite directions: $\mathcal W$ must be large enough to be preserved by $\mathsf Q$, and small enough not to be preserved by $\mathsf P$. The method of the course is to read $\mathcal W$ off the forcing for $\mathsf Q$: one tries to preserve a coarse property with the three-case argument of :ref{to="avoidance/forcing-question-method"}; the argument fails in its third case, which shows what the answers of the forcing question can compute; and the property is strengthened just enough to make this computation impossible.

## Solutions closed under subsets are immune

For all the problems of this course, every infinite subset of a solution is again a solution: homogeneous sets, transitive subtournaments, chains, antichains.

:::proposition{#prop-sd-subset-immune}
Let $\mathsf P$ be a problem whose solutions are infinite sets, and $X$ an instance whose solutions are closed under infinite subsets. Let $Z$ be a set such that no solution to $X$ is computable in $Z$. Then every solution to $X$ is immune relative to $Z$.
:::

:::proof{of=prop-sd-subset-immune}
If a solution $Y$ had an infinite subset c.e. relative to $Z$, it would have an infinite subset computable in $Z$ (:ref{to="immunity-growth/immune-sets"}), which would be a solution computable in $Z$.
:::

So the coarsest invariant for a separation is immunity. If $X \leq_T Z$ is an instance of $\mathsf P$ without $Z$-computable solution, and $A$ is any solution, then $A$ is immune relative to $Z$, and the class $\mathcal W_A = \{ W : A \text{ is immune relative to } W \}$ is a weakness property containing $Z$. Keeping such sets immune is the **preservation of immunity** of :ref{#def-preserve-immunity}. It is too strong for problems with any amount of compactness, as the analysis of weak König's lemma below shows; the useful properties are strengthenings of immunity, easier to preserve.

## Strong forms of immunity

Recall that an infinite set $A$ is hyperimmune if for every disjoint strong array $(F_n)$ some $F_n$ is disjoint from $A$ (:ref{#def-hyperimmune-set}), and that a hyperimmune set is immune. Immunity forbids computable lists of elements of $A$; hyperimmunity forbids computable lists of finite blocks each containing an element of $A$. Between the two, one can bound the size of the blocks.

:::definition{#def-sd-cb-immune}
Let $k \geq 1$. A **$k$-array** is a disjoint strong array $(F_n)$ with $|F_n| \leq k$ for every $n$. An infinite set $A$ is **$k$-immune** if for every $k$-array $(F_n)$ there is $n$ with $F_n \cap A = \emptyset$, and **constant-bound immune**, or **c.b.-immune**, if it is $k$-immune for every $k$. Relative to a set $W$, the arrays are computable in $W$, and one speaks of $k$-immunity and c.b.-immunity relative to $W$.
:::

A $1$-array is a computable sequence of distinct singletons, so the $1$-immune sets are the immune sets. A $k$-array is a disjoint strong array, so hyperimmune sets are c.b.-immune. For a fixed set $A$, the classes of sets $W$ relative to which $A$ is immune, $k$-immune, c.b.-immune or hyperimmune are weakness properties: an array computable in $V \leq_T W$ is computable in $W$.

::::exercise{#exr-sd-min-arrays difficulty=2 objective="Replace disjointness by the condition $\min F_n > n$ in the definition of $k$-immunity."}
Show that the requirement "$\min F_n > n$" may replace disjointness in :ref{#def-sd-cb-immune}: an infinite set $A$ is $k$-immune if and only if for every computable sequence $(F_n)$ of finite sets, given by canonical indices, with $|F_n| \leq k$ and $\min F_n > n$, some $F_n$ is disjoint from $A$.

:::solution
Let $(F_n)$ be a $k$-array each member of which meets $A$; its members are non-empty and pairwise disjoint, so only finitely many of them meet each interval $[0, m]$. Let $s(n)$ be the least $s$ with $\min F_s > n$; it is computable, and $F'_n = F_{s(n)}$ is a computable sequence with $|F'_n| \leq k$, $\min F'_n > n$, and each $F'_n$ meeting $A$. Conversely, from a sequence with $\min F_n > n$, define $n_0 = 0$ and $n_{j+1} = \max F_{n_j}$; the sets $F_{n_j}$ are pairwise disjoint, since $\min F_{n_{j+1}} > n_{j+1} = \max F_{n_j}$, and form a $k$-array, computable whenever the sequence is.
:::
::::

On co-c.e. sets the hierarchy collapses at its lower end.

:::proposition{#prop-sd-coce-cb}
A co-c.e. set is immune if and only if it is c.b.-immune.
:::

:::proof{of=prop-sd-coce-cb}
A c.b.-immune set is immune. Conversely, let $A$ be co-c.e. and immune, and suppose that $A$ is not c.b.-immune. Let $k$ be least such that some $k$-array $(F_n)$ has $F_n \cap A \neq \emptyset$ for every $n$. Since $A$ is immune, $k \geq 2$. The set $N = \{ n : F_n \not\subseteq A \}$ is c.e., since $\overline A$ is c.e. and the sets $F_n$ are given by canonical indices.

- If $N$ is finite, then $\bigcup_{n > \max N} F_n$ is an infinite c.e. subset of $A$ (infinite since the $F_n$ are disjoint and non-empty), contradicting immunity.
- If $N$ is infinite, let $n_0 < n_1 < \cdots$ be an infinite computable subset of $N$. For each $j$, wait for the first element $a_j$ of $F_{n_j}$ enumerated into $\overline A$, and let $F'_j = F_{n_j} \setminus \{ a_j \}$. Then $(F'_j)$ is a $(k-1)$-array, and $F'_j \cap A = F_{n_j} \cap A \neq \emptyset$ since $a_j \notin A$. This contradicts the minimality of $k$.
:::

By :ref{#ex-post-not-hypersimple}, the complement $A$ of Post's simple set satisfies $p_A(n) \leq 2n$, so it is not hyperimmune; by the proposition it is c.b.-immune. So c.b.-immunity is strictly weaker than hyperimmunity. Concretely, at least $n + 1$ of the numbers $0, \dots, 2n$ belong to $A$, and at most $n$ of them are below $n$, so every interval $[n, 2n]$ with $n \geq 1$ meets $A$. With $m_0 = 1$ and $m_{j+1} = 2m_j + 1$, the intervals $I_j = [m_j, 2m_j]$ form a disjoint strong array each of whose blocks meets $A$; their sizes grow, as they must.

:::quiz[immunity of co-c.e. sets]
In the proof of :ref{#prop-sd-coce-cb}, where is it used that $A$ is co-c.e.?

- [x] To find, for infinitely many blocks, an element outside $A$ effectively, and remove it; this lowers the size bound from $k$ to $k - 1$ while keeping each block meeting $A$.
- [ ] To show that the blocks with $F_n \subseteq A$ are finitely many.

  That is the case distinction itself; in the first case the conclusion uses only immunity.
- [ ] To show that $k \geq 2$.

  This uses only that $A$ is immune and that $1$-arrays are sequences of singletons.
:::

The last notion of the family is **effective immunity** (:ref{#def-effectively-immune}): a c.e. subset $W_e$ of $A$ has at most $q(e)$ elements, for a computable $q$. It is a property of a different kind, an upper bound on the c.e. subsets rather than a restriction on arrays, and it characterizes the DNC degrees (:ref{#thm-dnc-effectively-immune}). It is the property that the separating instance of :ref{to="separation-design/separating-instances"} exploits.

## Reading the property off a forcing question

We apply the method to weak König's lemma. Fix a set $A$ immune relative to $Z$ and a $Z$-computable infinite binary tree, and try to build a path $G$ keeping $A$ immune relative to $Z \oplus G$, with Jockusch–Soare forcing inside the paths of the tree, relativized to $Z$. Its question (:ref{#thm-tree-question}) asks whether every member of a $\Pi^0_1(Z)$ class $\mathcal P$ satisfies a $\Sigma^0_1$ sentence; by compactness, this holds if and only if every node of some level $\ell$ of a tree for $\mathcal P$ satisfies it within $\ell$ steps. The requirement for $e$ is that $W^{Z \oplus G}_e$ is not an infinite subset of $A$. Given $\mathcal P$, ask for each $n$ whether "$W^{Z \oplus G}_e$ has an element larger than $n$".

1. If the answer is negative for some $n$, an extension forces $W^{Z \oplus G}_e \subseteq [0, n]$.
2. If the answer is positive for every $n$, the level $\ell$ that witnesses it gives a finite set $F_n$: the elements larger than $n$ enumerated within $\ell$ steps by the nodes of level $\ell$. Every member of $\mathcal P$ enumerates an element of $F_n$. If some $F_n$ is disjoint from $A$, the condition itself forces $W^{Z \oplus G}_e \not\subseteq A$.
3. Otherwise every $F_n$ meets $A$, and $n \mapsto F_n$ is computable in $Z$.

In the third case nothing contradicts immunity: one only knows a $Z$-computable sequence of blocks, each meeting $A$. With hyperimmunity the third case is impossible, since $\min F_n > n$ lets one extract a $Z$-computable disjoint subsequence ($n_{j+1} = \max F_{n_j}$), a disjoint strong array relative to $Z$ meeting $A$ everywhere. So the property that the forcing question of $\mathsf{WKL}$ can preserve is hyperimmunity, and indeed $\mathsf{WKL}$ preserves it (:ref{#thm-hyperimmunity-examples}, with :ref{#thm-hyperimmune-principal} relativized to pass between sets and principal functions). The blocks $F_n$ are the trace of compactness: a positive answer does not say on which branch the element is produced. The failure is genuine.

:::proposition{#prop-sd-wkl-immunity}
$\mathsf{WKL}$ does not admit preservation of immunity: there are a co-c.e. immune set $A$ and a computable infinite binary tree every path of which computes an infinite subset of $A$.
:::

:::proof{of=prop-sd-wkl-immunity}
Let $A$ be the complement of Post's simple set, and $I_j$ the intervals above, which all meet $A$. The tree $S$ of finite sequences $(x_0, \dots, x_{j-1})$ with $x_i \in I_i$ and no $x_i$ enumerated into $\overline A$ within $j$ steps is computable and computably bounded (by $x_i \leq 2m_i$). Its paths are the sequences with $x_i \in I_i \cap A$ for every $i$, since $\overline A$ is c.e.; there is one, since every $I_i$ meets $A$. By :ref{#cor-bounded-pa}, every PA set computes a path, and a path $(x_i)$ computes the infinite subset $\{ x_i : i \in \nat \}$ of $A$, infinite since the intervals are disjoint. Let $T$ be a computable infinite binary tree whose paths are PA, for instance the tree of $\{0,1\}$-valued DNC functions (:ref{#thm-pa-characterization}). Then $A$ is immune, relative to $Z = \emptyset$, but not relative to any path of $T$.
:::

:::quiz[the property preserved by weak König's lemma]
In the analysis above, why does a positive answer give a finite set $F_n$ rather than one element?

- [x] Because the question of Jockusch–Soare forcing answers positively when all the nodes of some level make the enumeration produce an element; different nodes may produce different elements, and only the finite set of their outputs is known.
- [ ] Because $W^{Z \oplus G}_e$ is finite.

  It may be infinite; the blocks come from the bounded search.
- [ ] Because $A$ is co-c.e.

  The analysis holds for every set $A$; co-c.e. sets appear only in the counterexample.
:::

## The separations of the course

For each pair of problems, the course gives a forcing for the weaker one, the immunity property read off its question, and an instance of the stronger one defeating it.

| Problem | Property | Defeated by |
| --- | --- | --- |
| $\mathsf{EM}$ (Erdős–Moser) | countably many hyperimmunities | $\mathsf{RT}^2_2$: two hyperimmunities |
| $\mathsf{CAC}$ (chains and antichains) | c.b.-immunity | $\mathsf{DNC}$, hence $\mathsf{RT}^2_2$ and $\mathsf{EM}$ |
| $\mathsf{ADS}$ (ascending and descending sequences) | dependent hyperimmunity | $\mathsf{CAC}$, even for stable orders |

The question of $\mathsf{EM}$ is not disjunctive, so it preserves several properties at once; the question of $\mathsf{CAC}$ bounds the blocks of its positive answers by a constant; the question of $\mathsf{ADS}$ is answered negatively only when the condition already forces the negation. Before these separations, the next lesson explains where the notions of forcing come from.

## Notes and references

The use of custom weakness properties for separations below Ramsey's theorem for pairs, and the analysis of weak König's lemma through its forcing question, follow the chapter *Custom properties* of Patey's monograph (sections *Separation framework*, *Immunity and variants*, *Hyperimmunity and WKL*). Constant-bound immunity was introduced by Patey (2018), who also notes that it coincides with immunity on co-c.e. sets; the proof of :ref{#prop-sd-coce-cb} given here is a direct induction on the bound. Preservation of hyperimmunity by $\mathsf{WKL}$ is the computably dominated basis theorem of Jockusch and Soare (1972). The first separations of the problems in the table are due to Lerman, Solomon and Towsner (2013) for $\mathsf{EM}$ and $\mathsf{ADS}$, and Hirschfeldt and Shore (2007) for $\mathsf{CAC}$; the proofs by custom immunity properties are due to Patey (2017, 2018).

- L. Patey, *Lowness and avoidance*, chapter *Custom properties*.
- L. Patey, *Partial orders and immunity in reverse mathematics*, Computability 7 (2018), 323–339.
- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), 209–221; arXiv:1501.07709.
- M. Lerman, R. Solomon and H. Towsner, *Separating principles below Ramsey's theorem for pairs*, Journal of Mathematical Logic 13 (2013), 1350007.
- D. R. Hirschfeldt and R. A. Shore, *Combinatorial principles weaker than Ramsey's theorem for pairs*, Journal of Symbolic Logic 72 (2007), 171–206.
- C. G. Jockusch, Jr. and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.

:::::exercises
::::exercise{#ex-sd-immune-not-2-immune difficulty=2 objective="Separate immunity from $2$-immunity with a set that picks one number in each pair $\{2n, 2n+1\}$."}
A set $X$ is **bi-immune** if $X$ and $\overline X$ are both immune.

1. Let $X$ be bi-immune and $B = \{ 2n + X(n) : n \in \nat \}$. Show that $B$ is immune but not $2$-immune.
2. Show that there is a bi-immune set computable in $\emptyset'$.

:::solution
1. The set $B$ contains exactly one of $2n$ and $2n + 1$ for each $n$, so it is infinite, and the sets $F_n = \{ 2n, 2n + 1 \}$ form a $2$-array each member of which meets $B$: $B$ is not $2$-immune. Suppose that $R \subseteq B$ is infinite and computable. The sets $N_0 = \{ n : 2n \in R \}$ and $N_1 = \{ n : 2n + 1 \in R \}$ are computable. Since $2n \in B$ if and only if $X(n) = 0$, and $2n + 1 \in B$ if and only if $X(n) = 1$, we have $N_0 \subseteq \overline X$ and $N_1 \subseteq X$. Every element of $R$ is $2n$ or $2n + 1$ for some $n \in N_0 \cup N_1$, so one of $N_0$, $N_1$ is infinite, and it is an infinite computable subset of $\overline X$ or of $X$. This contradicts bi-immunity, so $B$ has no infinite computable subset, hence no infinite c.e. subset (:ref{#def-immune}).

2. Build $X$ by finite extensions $\sigma_0 \preceq \sigma_1 \preceq \cdots$ with oracle $\emptyset'$. At step $e$, with current string $\sigma$, ask $\emptyset'$ whether $W_e$ has two elements $a < b$ with $a \geq |\sigma|$, a $\Sigma^0_1$ question. If so, find such $a, b$ and extend $\sigma$ by zeros up to position $b$, with the bit $1$ at position $b$: then $a \notin X$ and $b \in X$. In both cases, then append the bits $1$ and $0$. The construction is computable in $\emptyset'$. The set $X$ and its complement are infinite, by the last clause. If $W_e$ is infinite, the question at step $e$ has a positive answer, so $W_e$ meets both $X$ and $\overline X$, and is contained in neither. So no infinite c.e. set is contained in $X$ or in $\overline X$.
:::
::::

::::exercise{#ex-sd-cb-finite-change difficulty=1 objective="Check that $k$-immunity passes to infinite subsets and survives the addition of finitely many elements."}
Let $k \geq 1$, $W$ a set, and $A$ a set $k$-immune relative to $W$. Show that every infinite subset of $A$ is $k$-immune relative to $W$, and that so is $A \cup E$ for every finite set $E$.

:::solution
If $B \subseteq A$ is infinite and a $W$-computable $k$-array $(F_n)$ has every member meeting $B$, every member meets $A$, which is impossible. Now let $E$ be finite, and suppose that a $W$-computable $k$-array $(F_n)$ has every member meeting $A \cup E$. Its members are pairwise disjoint, so only finitely many of them meet $E$; let $n_0$ be larger than their indices. Then $(F_{n_0 + n})_{n \in \nat}$ is a $W$-computable $k$-array every member of which meets $A$, a contradiction. The set $A \cup E$ is infinite since $A$ is.
:::
::::

::::exercise{#ex-sd-subset-closure difficulty=1 objective="See why closure of the solutions under infinite subsets is needed for solutions to be immune."}
Give a problem $\mathsf P$ and an instance $X$ of $\mathsf P$ with no computable solution, such that some solution to $X$ is not immune. Which hypothesis of :ref{#prop-sd-subset-immune} fails?

:::solution
Let the instances of $\mathsf P$ be all sets, and let the only solution to $X$ be $X \oplus \nat = \{ 2n : n \in X \} \cup \{ 2n + 1 : n \in \nat \}$, an infinite set. If $X$ is not computable, neither is $X \oplus \nat$, since $n \in X$ if and only if $2n \in X \oplus \nat$; so $X$ has no computable solution. But $X \oplus \nat$ contains the infinite computable set of odd numbers, so it is not immune. The solutions to $X$ are not closed under infinite subsets: the set of odd numbers is an infinite subset of the solution and is not a solution. This is the hypothesis used in the proof of :ref{#prop-sd-subset-immune}, where an infinite computable subset of a solution would itself be a solution.
:::
::::

::::exercise{#ex-sd-pa-coce difficulty=2 objective="Characterize the co-c.e. sets of which every PA set computes an infinite subset, through hyperimmunity."}
Let $A$ be an infinite co-c.e. set. Show that every PA set computes an infinite subset of $A$ if and only if $A$ is not hyperimmune. Show that the direction from left to right holds for every infinite set $A$.

:::solution
Suppose that $A$ is not hyperimmune: some disjoint strong array $(F_n)$ has every member meeting $A$. Let $S$ be the set of finite sequences $(x_0, \dots, x_{j-1})$ such that $x_i \in F_i$ for every $i < j$ and no $x_i$ is enumerated into $\overline A$ within $j$ steps. It is closed under prefixes, computable, and computably bounded, since $x_i \leq \max F_i$. An infinite sequence $(x_i)$ is a path through $S$ if and only if $x_i \in F_i \cap A$ for every $i$: if some $x_i$ is in $\overline A$, it is enumerated at some stage $s$, and the prefixes of length larger than $\max(i, s)$ are not in $S$. Since every $F_i$ meets $A$, $S$ has a path, so it is infinite. By :ref{#cor-bounded-pa}, every PA set computes a path $(x_i)$, and $\{ x_i : i \in \nat \}$ is an infinite subset of $A$, the sets $F_i$ being disjoint. This is the general form of :ref{#prop-sd-wkl-immunity}, whose set is co-c.e. and not hyperimmune.

Conversely, let $A$ be any infinite hyperimmune set. The $\{0,1\}$-valued DNC functions form a non-empty $\Pi^0_1$ class whose members are PA (:ref{#thm-pa-characterization}). By :ref{#thm-dominated-basis}, it has a computably dominated member $P$. If $P$ computed an infinite set $H \subseteq A$, the function $p_H$ would be dominated by a computable function $g$, and $p_A(n) \leq p_H(n) \leq g(n)$ for every $n$, since $H \subseteq A$; so $p_A$ would not be hyperimmune, contradicting :ref{#thm-hyperimmune-principal}.
:::
::::
:::::
