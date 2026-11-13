---
title: DNC functions and homogeneous sets
summary: A set computes a DNC function if and only if it computes homogeneous sets for all Π⁰₁ classes of positive measure (Bienvenu, Patey, Shafer); a computable coloring of pairs all of whose homogeneous sets compute DNC functions; the chain of four levels of compactness.
duration: 30
prerequisites: [closed-classes, immunity-growth/dnc-functions, martin-lof-randomness/random-dnc]
---

The previous lessons separated three levels of compactness: full compactness ($\mathsf{WKL}$, PA degrees), its probabilistic restriction ($\mathsf{WWKL}$, random sequences), and the Ramsey-type weak König lemma, which Ramsey's theorem for pairs implies. A fourth level is the weakest: the existence of diagonally non-computable functions (:ref{#def-dnc}). A DNC function escapes every c.e. set whose size is known in advance (:ref{#thm-dnc-effectively-immune}), which is a weak form of choosing a member of a large class. This lesson shows that DNC degrees are exactly the degrees of homogeneous sets for $\Pi^0_1$ classes of positive measure, so that Ramsey's theorem for pairs computes DNC functions. The next lesson develops the corresponding avoidance property and compares all the avoidance properties of the course.

## The Ramsey-type weak weak König lemma

The **Ramsey-type weak weak König lemma** $\mathsf{RWWKL}$ is the restriction of $\mathsf{RWKL}$ to the infinite binary trees $T$ with $\lambda([T]) > 0$. For a finite set $F$, let $\mathcal Q_F = \{ X \in \cs : F \subseteq X \}$, a clopen class of measure $2^{-|F|}$, and $\mathcal Q_n = \mathcal Q_{\{ n \}}$.

:::proposition[Bienvenu, Patey, Shafer]{#prop-rwwkl-dnc}
For every set $X$, the following are equivalent:

1. $X$ computes a DNC function;
2. for every $\Pi^0_1$ class $\mathcal P \subseteq \cs$ of positive measure, $X$ computes an infinite set homogeneous for $\mathcal P$, that is, for a computable tree $T$ with $[T] = \mathcal P$.
:::

For the first direction, the idea is to build a homogeneous set of color $1$ by adding elements one at a time, keeping a lower bound on the measure of the members of $\mathcal P$ that contain the finite set built so far. Few numbers make this measure drop sharply, and they form a c.e. set of known size, which a DNC function can escape.

:::proof{of=prop-rwwkl-dnc}
(1 ⇒ 2) We first prove a counting fact. *Let $\mathcal C$ be a measurable class with $\lambda(\mathcal C) \geq 2^{-d}$, $d \geq 3$. Fewer than $2d$ numbers $n$ satisfy $\lambda(\mathcal C \cap \mathcal Q_n) < 2^{-2d}$.* Otherwise let $E$ be a set of $2d$ such numbers. Every $X$ either contains an element of $E$ or is disjoint from $E$, so
$$
2^{-d} \leq \lambda(\mathcal C) \leq \lambda(\{ X : X \cap E = \emptyset \}) + \sum_{n \in E} \lambda(\mathcal C \cap \mathcal Q_n) < 2^{-2d} + 2d \cdot 2^{-2d} = (2d + 1)\, 2^{-2d},
$$
that is, $2^d < 2d + 1$, which fails for $d \geq 3$.

Let $\mathcal P$ be a $\Pi^0_1$ class with $\lambda(\mathcal P) \geq 2^{-c}$, $c \geq 3$. Call a finite set $F$ **valid** if $\lambda(\mathcal P \cap \mathcal Q_F) \geq 2^{-c \cdot 2^{|F|}}$. The empty set is valid. A valid set $F$ is contained in some member of $\mathcal P$, since $\mathcal P \cap \mathcal Q_F$ has positive measure. The class $\mathcal P \cap \mathcal Q_F$ is $\Pi^0_1$, so its measure is right-c.e., uniformly in $F$ (:ref{#prop-measure-effective}), and "$F$ is not valid" is a $\Sigma^0_1$ property of $F$. By SMN, there is a computable function $a$ such that
$$
W_{a(F)} = \{ n : n \leq \max F \} \cup \{ n : F \cup \{ n \} \text{ is not valid} \},
$$
with $\{ n : n \leq \max F \} = \emptyset$ for $F = \emptyset$. If $F$ is valid, apply the counting fact to $\mathcal C = \mathcal P \cap \mathcal Q_F$ and $d = c \cdot 2^{|F|} \geq 3$: the numbers $n$ with $F \cup \{ n \}$ not valid satisfy $\lambda(\mathcal C \cap \mathcal Q_n) < 2^{-c \cdot 2^{|F| + 1}} = 2^{-2d}$, so there are fewer than $2d$ of them, and $|W_{a(F)}| \leq b(F)$, where $b(F) = \max F + 1 + 2c \cdot 2^{|F|}$ (with $\max \emptyset + 1 = 0$).

Let $h \leq_T X$ be the function of :ref{#thm-dnc-effectively-immune} (2), with $h(e, m) \notin W_e$ whenever $|W_e| \leq m$. Define $F_0 = \emptyset$ and $F_{j+1} = F_j \cup \{ n_j \}$ with $n_j = h(a(F_j), b(F_j))$. By induction, each $F_j$ is valid and $n_j > \max F_j$: since $|W_{a(F_j)}| \leq b(F_j)$, $n_j \notin W_{a(F_j)}$. The set $H = \{ n_0 < n_1 < \cdots \}$ is infinite and computable in $X$. Every finite subset of $H$ is contained in some $F_j$, hence in a member of $\mathcal P$: $H$ is homogeneous for $\mathcal P$ with color $1$.

(2 ⇒ 1) For each $e$, let $\mathcal P_e$ be the class of the sets $X$ such that, if $\Phi_e(e)$ converges to the code of a tuple $(x_0, \dots, x_{e+2})$ of $e + 3$ distinct numbers, then $X$ is not constant on $\{ x_0, \dots, x_{e+2} \}$. Its complement is $\Sigma^0_1$, uniformly in $e$, and has measure at most $2 \cdot 2^{-(e+3)}$. So $\mathcal P = \bigcap_e \mathcal P_e$ is a $\Pi^0_1$ class with
$$
\lambda(\mathcal P) \geq 1 - \sum_e 2^{-(e+2)} = \tfrac12.
$$
Let $H = \{ y_0 < y_1 < \cdots \}$ be an infinite set computable in $X$ and homogeneous for $\mathcal P$, say with color $i$, and let $f(e)$ be the code of $(y_0, \dots, y_{e+2})$; then $f \leq_T X$. If $\Phi_e(e)\converge = f(e)$, then by :ref{#prop-homogeneous-member} some $X' \in \mathcal P$ has $\{ y_0, \dots, y_{e+2} \} \subseteq X'^{-1}(i)$, so $X'$ is constant on these $e + 3$ distinct numbers, and $X' \notin \mathcal P_e$, a contradiction. So $f$ is DNC.
:::

The proof of (2 ⇒ 1) uses a single class $\mathcal P$: a homogeneous set for it computes a DNC function. Together with Flood's reduction, this gives a lower bound for Ramsey's theorem for pairs.

:::corollary{#cor-rt22-dnc}
There is a computable coloring $f : [\nat]^2 \to 2$ all of whose infinite homogeneous sets compute a DNC function. So $\mathsf{RT}^2_2$ and $\mathsf{RWKL}$ do not admit the avoidance of DNC degrees defined below, and every Turing ideal satisfying $\mathsf{RT}^2_2$ contains a DNC function.
:::

:::proof{of=cor-rt22-dnc}
Let $T$ be a computable tree with $[T] = \mathcal P$, the class of the proof of (2 ⇒ 1). Flood's coloring for $T$ (:ref{#prop-rwkl-reductions}) is computable, and its infinite homogeneous sets are homogeneous for $T$, so they compute a DNC function by the proof of (2 ⇒ 1).
:::

So the four levels form a chain: $\mathsf{WKL}$ implies $\mathsf{WWKL}$ and $\mathsf{RWKL}$, each of which implies $\mathsf{RWWKL}$, which is equivalent to the existence of DNC functions. Ramsey's theorem for pairs implies $\mathsf{RWKL}$ but neither $\mathsf{WKL}$ (Liu, 2012) nor $\mathsf{WWKL}$ (Liu, 2015), and Bienvenu, Patey and Shafer showed that $\mathsf{RWKL}$ is strictly stronger than the existence of DNC functions. In the other direction, a random sequence computes a DNC function (:ref{#cor-random-dnc}), so $\mathsf{WWKL}$ implies $\mathsf{RWWKL}$ also by this route, while some DNC functions compute no random sequence.

:::quiz[DNC functions and homogeneous sets]
In (1 ⇒ 2), why does the c.e. set $W_{a(F)}$ contain all the numbers up to $\max F$?

- [x] To make the new element larger than the elements already chosen, so that $H$ is infinite and enumerated in increasing order; the bound $b(F)$ accounts for these numbers.
- [ ] Because the numbers below $\max F$ make $F$ invalid.

  They may well keep $F$ valid; they are excluded for another reason.
- [ ] To make $W_{a(F)}$ finite.

  It is finite anyway when $F$ is valid, by the counting fact.

---

In (2 ⇒ 1), why must the $e + 3$ numbers be distinct?

- [x] So that the class of the $X$ constant on them has measure $2 \cdot 2^{-(e+3)}$; with repetitions the class would be larger, and the bound on $\lambda(\mathcal P)$ would fail.
- [ ] So that $f$ is injective.

  Injectivity of $f$ is not needed.
- [ ] Because $H$ is infinite.

  The elements of $H$ are distinct anyway; the condition concerns the values of $\Phi_e(e)$.
:::

## Exercises

::::exercise{difficulty=1}
In the proof of (2 ⇒ 1) of :ref{#prop-rwwkl-dnc}, the $e$-th requirement uses tuples of $\ell(e) = e + 3$ distinct numbers. Show that the argument works for every computable function $\ell$ such that $\sum_e 2^{1 - \ell(e)} < 1$, and that it gives no information for $\ell(e) = e + 2$.

:::solution
The class of the sets constant on $\ell(e)$ given distinct numbers has measure $2 \cdot 2^{-\ell(e)}$, so the complement of $\mathcal P_e$ has measure at most $2^{1 - \ell(e)}$, and $\lambda(\mathcal P) \geq 1 - \sum_e 2^{1 - \ell(e)}$. If this sum is less than $1$, $\mathcal P$ is a $\Pi^0_1$ class of positive measure, and the rest of the proof is unchanged, with $f(e)$ the code of the first $\ell(e)$ elements of $H$. For $\ell(e) = e + 2$, the sum is $\sum_e 2^{-(e+1)} = 1$, and the estimate only gives $\lambda(\mathcal P) \geq 0$: the class could be null, and then it is not an instance of $\mathsf{RWWKL}$.
:::
::::

## Notes and references

The equivalence between DNC degrees and homogeneous sets for $\Pi^0_1$ classes of positive measure is due to Bienvenu, Patey and Shafer (2017), who introduced $\mathsf{RWWKL}$, proved its equivalence with the existence of DNC functions over $\mathsf{RCA}_0$, and showed that $\mathsf{RWKL}$ is strictly stronger; Flood and Towsner (2016) separated $\mathsf{RWKL}$ from the existence of DNC functions independently. Flood (2012) had shown that $\mathsf{RWKL}$ implies the existence of DNC functions. The proof given here follows the chapter *Compactness avoidance* of Patey's monograph, section *DNC and compactness*, with tuples of length $e + 3$ in the second direction, where the monograph's $e + 2$ does not give a class of positive measure (exercise above). It uses the characterization of DNC degrees by escaping functions (:ref{#thm-dnc-effectively-immune}), which the monograph attributes to Bienvenu, Patey and Shafer. That a random sequence computes a DNC function, and that some DNC functions compute no random sequence, are in the course on Martin-Löf randomness.

- L. Bienvenu, L. Patey and P. Shafer, *On the logical strengths of partial solutions to mathematical problems*, Transactions of the London Mathematical Society 4 (2017), 30–71; arXiv:1411.5874.
- S. Flood, *Reverse mathematics and a Ramsey-type König's lemma*, Journal of Symbolic Logic 77 (2012), 1272–1280.
- S. Flood and H. Towsner, *Separating principles below WKL₀*, Mathematical Logic Quarterly 62 (2016), 507–529; arXiv:1410.4068.
- L. Patey, *Lowness and avoidance*, chapter *Compactness avoidance*, section *DNC and compactness*.
