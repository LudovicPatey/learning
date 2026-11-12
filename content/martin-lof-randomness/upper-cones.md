---
title: Upper cones are null
summary: Relative measure and the Lebesgue density lemma; Sacks's theorem that the upper cone of a non-computable set is null, by the majority vote technique.
duration: 35
prerequisites: [levin-schnorr]
---

Random sequences are typical with respect to measure, and one may ask what they can compute. This lesson and the next prove two results that point in opposite directions. Sacks's theorem says that a non-computable set is computed by a null class of oracles only: a sequence chosen at random computes it with probability $0$. The Kučera–Gács theorem, in the next lesson, says that every set is nevertheless computed by some Martin-Löf random sequence. Both proofs rest on the relative measure of a class in a cylinder, which this lesson introduces first.

For a string $\tau$, $\Phi^\tau_e(n)\converge = i$ means that the computation of $\Phi_e$ on input $n$ with oracle $\tau$ halts with output $i$ and only queries the oracle below $|\tau|$; by :ref{#prop-oracle-stages}, it then holds with every oracle extending $\tau$.

## Relative measure and density

For a Borel class $\mathcal B$ and a string $\sigma$, the **relative measure** of $\mathcal B$ in $[\sigma]$ is
$$
\lambda(\mathcal B \mid \sigma) = \frac{\lambda(\mathcal B \cap [\sigma])}{\lambda([\sigma])} = 2^{|\sigma|}\, \lambda(\mathcal B \cap [\sigma]).
$$
It is the proportion of $[\sigma]$ occupied by $\mathcal B$. Since $[\sigma]$ is the disjoint union of $[\sigma 0]$ and $[\sigma 1]$, $\lambda(\mathcal B \mid \sigma)$ is the average of $\lambda(\mathcal B \mid \sigma 0)$ and $\lambda(\mathcal B \mid \sigma 1)$; more generally, it is the average of $\lambda(\mathcal B \mid \tau)$ over the $2^k$ extensions $\tau$ of $\sigma$ of length $|\sigma| + k$.

For example, let $\mathcal B$ be the class of the sequences $X$ with $X(0) = X(1)$. Then $\lambda(\mathcal B \mid \varepsilon) = \lambda(\mathcal B \mid 0) = \lambda(\mathcal B \mid 1) = \frac12$, while $\lambda(\mathcal B \mid \sigma)$ is $1$ for $\sigma \succeq 00$ or $\sigma \succeq 11$, and $0$ for $\sigma \succeq 01$ or $\sigma \succeq 10$. The relative measure in a cylinder depends on the cylinder, and long cylinders can be almost filled by a class of measure $\frac12$.

A class of positive measure cannot be spread thinly over every cylinder: some cylinder is almost filled by it.

:::lemma[Lebesgue density lemma]{#lem-density}
Let $\mathcal B$ be a Borel class with $\lambda(\mathcal B) > 0$. For every $\varepsilon > 0$, there is a string $\sigma$ with $\lambda(\mathcal B \mid \sigma) > 1 - \varepsilon$.
:::

:::proof{of=lem-density}
If $\varepsilon \geq 1$, the empty string works, since $\lambda(\mathcal B) > 0$; so assume $\varepsilon < 1$. By outer regularity, there is an open class $\mathcal U \supseteq \mathcal B$ with $\lambda(\mathcal U) < \lambda(\mathcal B) / (1 - \varepsilon)$, a number larger than $\lambda(\mathcal B)$. Write $\mathcal U = [W]^{\prec}$ with $W$ prefix-free. The classes $\mathcal B \cap [\sigma]$, $\sigma \in W$, are pairwise disjoint with union $\mathcal B$. If $\lambda(\mathcal B \mid \sigma) \leq 1 - \varepsilon$ for every $\sigma \in W$, then
$$
\lambda(\mathcal B) = \sum_{\sigma \in W} \lambda(\mathcal B \cap [\sigma]) \leq (1 - \varepsilon) \sum_{\sigma \in W} 2^{-|\sigma|} = (1 - \varepsilon)\, \lambda(\mathcal U) < \lambda(\mathcal B),
$$
a contradiction. So some $\sigma \in W$ satisfies $\lambda(\mathcal B \mid \sigma) > 1 - \varepsilon$.
:::

:::quiz[the density lemma]
In the proof of :ref{#lem-density}, where is the hypothesis $\lambda(\mathcal B) > 0$ used?

- [x] To choose $\mathcal U$ with $\lambda(\mathcal U) < \lambda(\mathcal B) / (1 - \varepsilon)$, a number larger than $\lambda(\mathcal B)$, and to obtain the strict inequality at the end.
- [ ] To ensure that $W$ is finite.

  $W$ may be infinite; the sums are countable.
- [ ] It is not needed: the lemma holds for null classes as well.

  For $\mathcal B = \emptyset$, every relative measure is $0$, and the conclusion fails.

---

Why is the generator $W$ of $\mathcal U$ taken prefix-free?

- [x] So that the classes $\mathcal B \cap [\sigma]$, $\sigma \in W$, are disjoint, and the measure of $\mathcal B$ is the sum of their measures.
- [ ] So that $\mathcal U$ is a Σ⁰₁ class.

  No effectivity is involved in this proof; $\mathcal B$ is an arbitrary Borel class.
- [ ] So that $W$ is finite.

  Prefix-free sets can be infinite, for example $\{ 0^n 1 : n \in \nat \}$.
:::

Lebesgue proved a stronger statement, the **density theorem**: for almost every $X \in \mathcal B$, $\lambda(\mathcal B \mid X \uh n)$ tends to $1$ (Downey–Hirschfeldt, Theorem 1.2.3). The lemma suffices for this course; it is the case of Nies, Theorem 1.9.4, for the uniform measure.

## Upper cones are null

If many oracles compute $Y$ by the same procedure $\Phi_e$, one can compute $Y$ without an oracle by a vote: run $\Phi_e$ on all oracles at once and output the value supported by the largest measure of oracles. The difficulty is that $\Phi_e$ may also compute wrong values on many oracles; the density lemma provides a cylinder in which the correct oracles form a majority. The argument is called the **majority vote** technique.

:::theorem[Sacks]{#thm-sacks}
If $Y$ is not computable, then $\lambda(\{ X : Y \leq_T X \}) = 0$.
:::

:::proof{of=thm-sacks}
The class $\{ X : Y \leq_T X \}$ is the union over $e$ of the classes $\mathcal C_e = \{ X : \Phi^X_e = Y \}$. Each $\mathcal C_e$ is Borel: $X \in \mathcal C_e$ if and only if for every $n$ there is a prefix $\tau$ of $X$ with $\Phi^\tau_e(n)\converge = Y(n)$. By subadditivity, it suffices to show that each $\mathcal C_e$ is null.

Suppose that $\lambda(\mathcal C_e) > 0$. By the density lemma (:ref{#lem-density}), there is a string $\sigma$ with $\lambda(\mathcal C_e \mid \sigma) > \frac12$. For $n \in \nat$ and $i \in \{0, 1\}$, let $\mathcal U_{n,i}$ be the open class generated by the strings $\tau \succeq \sigma$ with $\Phi^\tau_e(n)\converge = i$; these classes are uniformly $\Sigma^0_1$.

- $\mathcal C_e \cap [\sigma] \subseteq \mathcal U_{n, Y(n)}$, so $\lambda(\mathcal U_{n, Y(n)} \mid \sigma) > \frac12$.
- $\mathcal U_{n,0}$ and $\mathcal U_{n,1}$ are disjoint: a sequence in both would have prefixes $\tau, \tau'$ with $\Phi^\tau_e(n)\converge = 0$ and $\Phi^{\tau'}_e(n)\converge = 1$, and by monotonicity the longer of the two would give both outputs. So $\lambda(\mathcal U_{n, 1 - Y(n)} \mid \sigma) < \frac12$.

To compute $Y(n)$, enumerate $\mathcal U_{n,0}$ and $\mathcal U_{n,1}$ until the measure of the finite part of one of them inside $[\sigma]$ exceeds $2^{-|\sigma| - 1}$, and output the corresponding $i$. The search terminates by the first item, since the measure of $\mathcal U_{n, Y(n)} \cap [\sigma]$ is approached from below, and its output is $Y(n)$ by the second. This computes $Y$, a contradiction.
:::

Sacks's theorem is the measure-theoretic analogue of the fact that upper cones of non-computable sets are meager.

:::quiz[Sacks's theorem]
In the proof of :ref{#thm-sacks}, why is the density lemma needed, rather than the hypothesis $\lambda(\mathcal C_e) > 0$ alone?

- [x] Because the vote must be won by a majority: on a cylinder where $\mathcal C_e$ has relative measure above $\frac12$, the correct value has more than half of the measure and the incorrect one less than half.
- [ ] Because $\mathcal C_e$ might not be measurable.

  It is Borel, as shown at the beginning of the proof.
- [ ] Because the density lemma makes $\mathcal C_e$ open.

  $\mathcal C_e$ is not open in general; the lemma only finds a cylinder where it is dense.

---

Why are the classes $\mathcal U_{n,0}$ and $\mathcal U_{n,1}$ disjoint?

- [x] Because a computation with an oracle string is preserved by extending the string, so two prefixes of the same sequence cannot produce different outputs on the same input.
- [ ] Because $Y(n)$ has only one value.

  The classes are defined without reference to $Y$; disjointness comes from the oracle machine.
- [ ] Because $\Phi_e$ is total.

  $\Phi^X_e$ may be partial for many $X$; disjointness concerns the oracles on which it converges.
:::

:::corollary{#cor-random-cone}
For every non-computable $Y$, almost every sequence fails to compute $Y$. In particular the class of sequences computing $\emptyset'$ is null.
:::

This class nevertheless contains random sequences, such as $\Omega$ (:ref{#cor-omega-random}). Martin-Löf tests capture only effectively null classes, and the null class $\{ X : \emptyset' \leq_T X \}$, which is $\Sigma^0_4$, is not contained in any of them.

## Exercises

::::exercise{difficulty=1}
Relativize :ref{#thm-sacks}: show that if $\lambda(\{ X : Y \leq_T A \oplus X \}) > 0$, then $Y \leq_T A$.

:::solution
The proof of :ref{#thm-sacks} relativizes: replace $\Phi_e^X$ by $\Phi_e^{A \oplus X}$, and the classes $\mathcal U_{n,i}$ by the classes generated by the strings $\tau \succeq \sigma$ such that $\Phi_e^{A \oplus \tau}(n)\converge = i$, which are $\Sigma^0_1$ relative to $A$, uniformly in $n$ and $i$. The vote is then computable in $A$, and computes $Y$.
:::
::::

::::exercise{difficulty=2}
Let $A \subseteq \nat$ and $e \in \nat$ be such that the class $\mathcal C = \{ X : W^X_e = A \}$ has positive measure. Show that $A$ is c.e.

:::solution
By :ref{#lem-density}, there is $\sigma$ with $\lambda(\mathcal C \mid \sigma) > \frac12$. For each $n$, let $\mathcal E_n$ be the open class generated by the strings $\tau \succeq \sigma$ such that $n$ is enumerated into $W_e^\tau$ by a computation that only queries the oracle below $|\tau|$; the classes $\mathcal E_n$ are uniformly $\Sigma^0_1$. If $n \in A$, then $\mathcal C \cap [\sigma] \subseteq \mathcal E_n$, so $\lambda(\mathcal E_n \mid \sigma) > \frac12$. If $n \notin A$, then $\mathcal E_n$ is disjoint from $\mathcal C \cap [\sigma]$, so $\lambda(\mathcal E_n \mid \sigma) < \frac12$. Hence $n \in A$ if and only if $\lambda(\mathcal E_n \cap [\sigma]) > 2^{-|\sigma| - 1}$. The measure of $\mathcal E_n \cap [\sigma]$ is left-c.e., uniformly in $n$ (:ref{#prop-measure-effective}), so this condition is $\Sigma^0_1$, and $A$ is c.e. This is the theorem of de Leeuw, Moore, Shannon and Shapiro.
:::
::::

## Notes and references

Sacks's theorem is from his monograph *Degrees of Unsolvability* (1963). De Leeuw, Moore, Shannon and Shapiro (1956) had proved, in the language of probabilistic machines, that a set enumerated by a positive measure of oracles is c.e. (second exercise), from which Sacks's theorem follows by applying it to the set and to its complement (Downey–Hirschfeldt, Theorem 8.12.1 and Corollary 8.12.2; Nies, Theorem 5.1.12). The density theorem is due to Lebesgue, in dimension one as a consequence of his differentiation theorem (1904), and in general in 1910 (Downey–Hirschfeldt, Theorem 1.2.3, prove the version for Cantor space).

- G. E. Sacks, *Degrees of Unsolvability*, Annals of Mathematics Studies 55, Princeton University Press, 1963.
- K. de Leeuw, E. F. Moore, C. E. Shannon and N. Shapiro, *Computability by probabilistic machines*, in: Automata Studies, Annals of Mathematics Studies 34, Princeton University Press, 1956, 183–212.
- H. Lebesgue, *Leçons sur l'intégration et la recherche des fonctions primitives*, Gauthier-Villars, 1904.
- H. Lebesgue, *Sur l'intégration des fonctions discontinues*, Annales scientifiques de l'École Normale Supérieure 27 (1910), 361–450.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 1.2 and 8.12.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Sections 1.9 and 5.1.
