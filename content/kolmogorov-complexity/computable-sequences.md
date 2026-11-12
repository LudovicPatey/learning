---
title: Chaitin's characterization of computable sequences
summary: A string has few descriptions of length close to its complexity; a sequence is computable if and only if the complexity of its initial segments is at most that of their length, up to a constant.
duration: 40
prerequisites: [initial-segments]
---

By :ref{#prop-computable-segments}, the initial segments of a computable sequence are as simple as their lengths. Chaitin proved the converse: minimal complexity of the initial segments characterizes the computable sequences. The statement is natural, but the proof is not immediate, since the hypothesis bounds the complexity of each initial segment separately and does not obviously yield a single algorithm. This lesson proves the theorem. Its two ingredients, a counting lemma for descriptions and the passage from a c.e. tree of bounded width to a computable tree with the same paths, reappear in the study of the K-trivial sequences.

## The theorem

:::theorem[Chaitin]{#thm-chaitin-computable}
For a sequence $X$, the following are equivalent:

1. $X$ is computable;
2. $C(X \uh n) \leq^+ C(n)$;
3. $C(X \uh n) \leq^+ \log n$, for $n \geq 1$.
:::

The implications (1 ⇒ 2 ⇒ 3) follow from :ref{#prop-computable-segments} and $C(n) \leq^+ \log n$. The proof of (3 ⇒ 1) has two parts. The first is a counting lemma: a string has few descriptions of length close to its complexity, and as a consequence, few strings of length $n$ have complexity close to $C(n)$. The second converts this into computability. The sequences satisfying 3 with a fixed constant are the paths of a c.e. tree, which by the counting lemma has few nodes at infinitely many levels. Such a tree has finitely many paths, and a c.e. tree can be replaced by a computable tree with the same paths. A computable tree with finitely many paths has only computable paths.

## Counting descriptions

:::lemma[Chaitin]{#lem-description-count}
For every machine $M$ there is a constant $c$ such that, for every string $\sigma$ and every $d$, fewer than $(d + 1)^2\, 2^{d + c}$ strings $\tau$ satisfy $M(\tau) = \sigma$ and $|\tau| \leq C(\sigma) + d$.
:::

The idea is that a string with many short $M$-descriptions belongs to a small c.e. set, and can be described by its position in an enumeration of that set, which is shorter than its complexity.

:::proof{of=lem-description-count}
For numbers $m$ and $k$, let $L_{m,k}$ be the set of strings having at least $2^m$ $M$-descriptions of length at most $k$. The sets $L_{m,k}$ are c.e., uniformly in $m$ and $k$. Distinct strings have disjoint sets of descriptions, and there are $2^{k+1} - 1$ strings of length at most $k$, so $|L_{m,k}|\, 2^m < 2^{k+1}$, that is, $|L_{m,k}| < 2^{k + 1 - m}$; in particular $L_{m,k}$ is empty if $m > k$.

Let $N$ be the machine that, on an input of the form $\bar\rho\, 01\, \alpha$, with $\bar\rho$ the string $\rho$ with each bit doubled, lets $m$ be the number associated with $\rho$ and $k = |\alpha| + m - 1$, reads $\alpha$ as a binary representation of a number $i$ (leading zeros allowed), and outputs the $i$-th element, counting from $0$, of a fixed enumeration of $L_{m,k}$. An element of $L_{m,k}$, with $m \leq k$, has a position $i < 2^{k + 1 - m}$, which is written with exactly $k + 1 - m$ bits. So $C_N(\sigma) \leq 2|\rho| + 2 + k + 1 - m$ for $\sigma \in L_{m,k}$, and by optimality there is a constant $c_0$ with
$$
C(\sigma) \leq k - m + 2 \log(m + 1) + c_0 \quad \text{for every } \sigma \in L_{m,k}.
$$
Let $c$ be such that $c \geq 2 \log(c + 3) + c_0 + 2$. Fix $\sigma$ and $d$, and let $k = C(\sigma) + d$ and $m = d + c + 2\lfloor \log(d + 1) \rfloor$. Suppose that $\sigma \in L_{m,k}$. Then
$$
C(\sigma) \leq C(\sigma) - c - 2 \lfloor \log(d + 1) \rfloor + 2 \log(m + 1) + c_0.
$$
Since $m + 1 \leq (d + 1) + c + 2(d + 1) \leq (d + 1)(c + 3)$, we have $\log(m + 1) \leq \log(d + 1) + \log(c + 3) < \lfloor \log(d + 1) \rfloor + 1 + \log(c + 3)$, and the inequality gives $c < 2 \log(c + 3) + c_0 + 2$, contrary to the choice of $c$. So $\sigma \notin L_{m,k}$: $\sigma$ has fewer than $2^m \leq (d + 1)^2\, 2^{d + c}$ $M$-descriptions of length at most $C(\sigma) + d$.
:::

:::lemma[Chaitin]{#lem-few-segments}
There is a constant $c$ such that, for all $n$ and $d$, fewer than $(d + 1)^2\, 2^{d + c}$ strings $\sigma$ of length $n$ satisfy $C(\sigma) \leq C(n) + d$.
:::

:::proof{of=lem-few-segments}
Let $M$ be the machine $\tau \mapsto |U(\tau)|$, which outputs the string associated with the length of $U(\tau)$, and let $c$ be given by :ref{#lem-description-count} for $M$. For each string $\sigma$ of length $n$ with $C(\sigma) \leq C(n) + d$, a shortest $U$-description $\tau_\sigma$ of $\sigma$ is an $M$-description of $n$ of length at most $C(n) + d$, and distinct strings $\sigma$ have distinct descriptions $\tau_\sigma$. By :ref{#lem-description-count} applied to the string $n$, there are fewer than $(d + 1)^2\, 2^{d + c}$ of them.
:::

The bound does not depend on $n$: although there are $2^n$ strings of length $n$, only a bounded number of them are as simple as their length. Both lemmas are instances of the counting argument of :ref{#prop-incompressible-count}, applied to a cleverly chosen c.e. set.

## Proof of Chaitin's theorem

:::proof{of=thm-chaitin-computable}
It remains to prove (3 ⇒ 1). Let $e$ be such that $C(X \uh n) \leq \log n + e$ for every $n \geq 1$. Let
$$
T = \{ \sigma : C(\sigma \uh m) \leq \log m + e \text{ for every } m \text{ with } 1 \leq m \leq |\sigma| \}.
$$
It is a tree (closed under prefixes) and every initial segment of $X$ belongs to it. It is c.e.: with the approximation $C_s$ of :ref{#thm-c-not-computable}, the sets $T_s$ defined in the same way with $C_s$ in place of $C$ are computable, uniformly in $s$, closed under prefixes, increasing in $s$, and their union is $T$.

*Few nodes at infinitely many levels.* For $\ell \geq 1$, let $I_\ell$ be the set of numbers $n$ with $2^\ell - 1 \leq n \leq 2^{\ell + 1} - 2$, those whose associated string has length $\ell$. By :ref{#prop-incompressible-count}, some $n \in I_\ell$ satisfies $C(n) \geq \ell$. Since $n < 2^{\ell + 1}$, every $\sigma \in T$ of length $n$ satisfies $C(\sigma) \leq \log n + e < \ell + 1 + e \leq C(n) + e + 1$. By :ref{#lem-few-segments}, $T$ has fewer than $b = (e + 2)^2\, 2^{e + 1 + c}$ nodes at the level $n$. So the number $a_\ell$, the least number of nodes of $T$ at a level of $I_\ell$, satisfies $a_\ell < b$ for every $\ell \geq 1$.

Let $a$ be the largest number such that $a_\ell = a$ for infinitely many $\ell$, and let $\ell^* \geq 1$ be such that $a_\ell \leq a$ for every $\ell \geq \ell^*$. The numbers $a$ and $\ell^*$ are used as fixed information in the algorithm below; they are not computed.

*$T$ has at most $a$ paths.* If $P_1, \dots, P_p$ are distinct paths of $T$, they have pairwise distinct initial segments of some length $L$, so $T$ has at least $p$ nodes at every level $n \geq L$. Taking $\ell$ large with $a_\ell = a$ gives $p \leq a$.

*A computable tree with the same paths.* Define computable sequences $\ell_0 < \ell_1 < \cdots$ and $s_0, s_1, \dots$ as follows. At step $i$, search for $\ell \geq \ell^*$, with $\ell > \ell_{i-1}$ if $i > 0$, and a stage $s$ such that $T_s$ has at least $a$ nodes at every level of $I_\ell$, and let $(\ell_i, s_i)$ be the first pair found. The search terminates: for the infinitely many $\ell$ with $a_\ell = a$, $T$ has at least $a$ nodes at each of the finitely many levels of $I_\ell$, and they all appear in some $T_s$. Let $m_i = 2^{\ell_i} - 1$, the least element of $I_{\ell_i}$.

We claim that $P \uh m_i \in T_{s_i}$ for every path $P$ of $T$ and every $i$. Otherwise, since $T_{s_i}$ is closed under prefixes, $P \uh n \notin T_{s_i}$ for every $n \in I_{\ell_i}$. At each such level, $T$ contains the at least $a$ nodes of $T_{s_i}$ and the node $P \uh n$, so $a_{\ell_i} \geq a + 1$, contradicting $\ell_i \geq \ell^*$.

Let $S$ be the set of strings $\sigma$ such that $\sigma \uh m_i \in T_{s_i}$ for every $i$ with $m_i \leq |\sigma|$. It is a computable tree, since the sequence $(m_i)$ is computable and increasing. By the claim, every path of $T$ is a path of $S$. Conversely, if $P$ is a path of $S$, then $P \uh m_i \in T_{s_i} \subseteq T$ for every $i$, so every initial segment of $P$ is in $T$. So $S$ and $T$ have the same paths, at most $a$ of them, and $X$ is one of them.

*Paths of $S$ are computable.* Let $L$ be a length such that no path of $S$ other than $X$ extends $X \uh L$. A node $\rho \in S$ that lies on no path has no extension in $S$ beyond some level: if $\rho$ had extensions in $S$ of every length, then so would $\rho 0$ or $\rho 1$, and iterating would build a path through $\rho$ (this is König's lemma for binary trees). To compute $X \uh n$ for $n \geq L$, search for a level $N \geq n$ such that exactly one string of length $n$ extending $X \uh L$ has an extension of length $N$ in $S$, and output that string. The search terminates and is correct: $X \uh n$ has extensions of every length, and each of the finitely many other strings of length $n$ extending $X \uh L$ lies on no path, hence has no extension beyond some level. So $X$ is computable.
:::

The proof is non-uniform: it uses the numbers $a$ and $\ell^*$ and the string $X \uh L$, which cannot be found effectively from $e$. The argument is an instance of a general technique. A condition that holds on all initial segments defines a tree, the tree is c.e. because complexity is approximable from above, and a bound on its width at infinitely many levels limits its paths. In the course on $\Pi^0_1$ classes, the last step is the statement that isolated paths of computable trees are computable (:ref{to="pi01-classes/computable-members"}).

:::quiz[Chaitin's theorem]
In the proof of :ref{#thm-chaitin-computable}, why are incompressible numbers $n \in I_\ell$ used to bound the width of $T$?

- [x] Because the hypothesis bounds $C(X \uh n)$ by $\log n + e$, while :ref{#lem-few-segments} counts the strings with complexity at most $C(n) + d$; the two bounds agree up to a constant exactly when $C(n)$ is close to $\log n$.
- [ ] Because $T$ has few nodes at every level.

  The proof only bounds the width at one level of each interval $I_\ell$; at a level $n$ with $C(n)$ small, the bound $\log n + e$ may allow many strings.
- [ ] Because incompressible numbers are computable from $\ell$.

  They are not: no algorithm finds them, which is why the proof searches for stages at which every level of $I_\ell$ has enough nodes.

---

Why does the claim $P \uh m_i \in T_{s_i}$ use the fact that $a_\ell \leq a$ for $\ell \geq \ell^*$?

- [x] If $P \uh m_i$ appeared after stage $s_i$, every level of $I_{\ell_i}$ would contain one more node than the $a$ nodes already present at stage $s_i$, so $a_{\ell_i}$ would exceed $a$.
- [ ] To ensure that the search for $\ell_i$ and $s_i$ terminates.

  Termination uses the infinitely many $\ell$ with $a_\ell = a$, not the upper bound.
- [ ] To show that $S$ is computable.

  $S$ is computable for any computable sequences $(m_i)$ and $(s_i)$.
:::

The bound $\log n$ in (3) cannot be replaced by $2 \log n$: an exercise of the previous lesson shows that the characteristic sequence of every c.e. set $A$ satisfies $C(A \uh n) \leq^+ 2 \log n$, and non-computable c.e. sets exist.

## Exercises

::::exercise{difficulty=2}
Show that for every $d$ there are only finitely many sequences $X$ with $C(X \uh n) \leq C(n) + d$ for every $n$, and bound their number in terms of $d$.

:::solution
Such sequences are paths of the tree $T' = \{ \sigma : C(\sigma \uh m) \leq C(m) + d \text{ for every } m \leq |\sigma| \}$. By :ref{#lem-few-segments}, $T'$ has fewer than $(d + 1)^2\, 2^{d + c}$ nodes at every level. Distinct paths have distinct initial segments of some common length, so there are fewer than $(d + 1)^2\, 2^{d + c}$ such sequences.
:::
::::

## Notes and references

The theorem and the two counting lemmas are from Chaitin's 1976 paper; Downey and Hirschfeldt (Section 3.4, Lemmas 3.4.2–3.4.3 and Theorem 3.4.4) and Monin and Patey present the same proof, with the bound $O(2^d)$ in place of $(d + 1)^2\, 2^{d + c}$ in the counting lemmas; any bound depending only on $d$ suffices for the theorem. Monin and Patey also credit the theorem to Zvonkin and Levin and to Meyer. A form with conditional complexity, $C(X \uh n \mid n) = O(1)$, is due to Loveland (1969) (Downey–Hirschfeldt, Theorem 3.4.1). The analogous statement for prefix-free complexity fails: the sequences with $K(X \uh n) \leq^+ K(n)$, the K-trivial sequences, include non-computable ones.

- G. J. Chaitin, *Information-theoretic characterizations of recursive infinite strings*, Theoretical Computer Science 2 (1976), 45–48.
- D. W. Loveland, *A variant of the Kolmogorov concept of complexity*, Information and Control 15 (1969), 510–526.
- A. K. Zvonkin and L. A. Levin, *The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms*, Russian Mathematical Surveys 25 (1970), 83–124.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 3.4.
- B. Monin and L. Patey, *Computability theory*, chapter "Kolmogorov complexity and random numbers", section "Chaitin's theorem".
