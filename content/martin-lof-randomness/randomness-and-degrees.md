---
title: The Kučera–Gács theorem
summary: Kučera's branching lemma; every set is computable, by a weak truth-table reduction, from a member of any Π⁰₁ class of positive measure, hence from a Martin-Löf random sequence; every degree above 0′ contains a random sequence.
duration: 30
prerequisites: [upper-cones]
---

By :ref{#thm-sacks}, a non-computable set is computed by a null class of oracles only. Martin-Löf tests capture only effectively null classes, and this lesson shows that the null class of oracles computing a given set always contains random sequences: every set is computable from a random sequence. The proof codes the set into a member of a $\Pi^0_1$ class of random sequences, using a lower bound on relative measure.

## Kučera's branching lemma

Recall from :ref{to="martin-lof-randomness/upper-cones"} that the relative measure $\lambda(\mathcal B \mid \sigma)$ is the average of the relative measures $\lambda(\mathcal B \mid \tau)$ over the extensions $\tau$ of $\sigma$ of any fixed length. The density lemma used this average to find a cylinder that is almost filled; here it is used to find two cylinders that are not too empty. If a class fills a proportion $2^{-k}$ of a cylinder, then at least two of the extensions of the cylinder by $k + 1$ bits are filled in proportion at least $2^{-k-1}$: a single extension, even completely filled, contributes only $2^{-k-1}$ to the average. This **branching lemma** of Kučera is what the coding of the Kučera–Gács theorem needs.

:::lemma[Kučera]{#lem-kucera-branching}
Let $\mathcal B$ be a Borel class, $\sigma$ a string and $k \in \nat$ with $\lambda(\mathcal B \mid \sigma) \geq 2^{-k}$. Then there are at least two strings $\tau \succeq \sigma$ of length $|\sigma| + k + 1$ with $\lambda(\mathcal B \mid \tau) \geq 2^{-k-1}$.
:::

:::proof{of=lem-kucera-branching}
$\lambda(\mathcal B \mid \sigma)$ is the average of $\lambda(\mathcal B \mid \tau)$ over the $2^{k+1}$ strings $\tau \succeq \sigma$ of length $|\sigma| + k + 1$. If at most one of them had relative measure at least $2^{-k-1}$, this one being at most $1$ and the others less than $2^{-k-1}$, the average would be less than
$$
2^{-k-1} \left( 1 + (2^{k+1} - 1)\, 2^{-k-1} \right) = 2^{-k-1} + 2^{-k-1} - 2^{-2k-2} < 2^{-k},
$$
a contradiction.
:::

## Every set is computable from a random sequence

A computable tree in which every node has two incomparable extensions has members of every Turing degree above its own: a set $X$ is coded by following, at the $n$-th branching, the left or the right extension according to $X(n)$. The tree of a $\Pi^0_1$ class may have dead ends, and one cannot tell effectively which nodes branch. When the class has positive measure, :ref{#lem-kucera-branching} says where to look for branchings: among the extensions of a fixed length, those in which the class keeps a large relative measure. Deciding which extensions these are requires $\emptyset'$, so the coding is not effective; the decoding is effective, because the coded bit is determined by the position of the chosen extension among the good ones, leftmost or rightmost, and the bad extensions eventually reveal themselves. :ref{#fig-kucera-gacs} shows two steps.

:::figure[Two steps of the coding of :ref{#thm-kucera-gacs}. The extensions of $\sigma_n$ of length $m_{n+1}$ are drawn in lexicographic order, those of the set $A_n(\sigma_n)$, in which $\mathcal P$ has large relative measure, being highlighted; there are at least two of them by :ref{#lem-kucera-branching}. The next string $\sigma_{n+1}$ is the leftmost one if $X(n) = 0$, and the rightmost one if $X(n) = 1$.]{#fig-kucera-gacs}
<svg class="fig" viewBox="0 0 600 320" width="600" role="img" aria-label="Two steps of the Kučera–Gács coding: among the extensions of sigma_n of the next length, those of large relative measure are marked; sigma_n+1 is the leftmost of them if X(n) is 0 and the rightmost if X(n) is 1"><defs><marker id="mlr-kg-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" class="accent-fill"/></marker></defs><circle cx="300" cy="22" r="5" class="node"/><text x="312.0" y="27.0" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><line x1="300.0" y1="27" x2="104.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="160.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="216.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="272.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="328.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="384.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="440.0" y2="70" class="muted-stroke" stroke-width="0.8"/><line x1="300.0" y1="27" x2="496.0" y2="70" class="muted-stroke" stroke-width="0.8"/><rect x="79.0" y="70" width="50" height="24" class="cell"/><rect x="135.0" y="70" width="50" height="24" class="head-cell"/><rect x="191.0" y="70" width="50" height="24" class="cell"/><rect x="247.0" y="70" width="50" height="24" class="cell"/><rect x="303.0" y="70" width="50" height="24" class="head-cell"/><rect x="359.0" y="70" width="50" height="24" class="cell"/><rect x="415.0" y="70" width="50" height="24" class="head-cell"/><rect x="471.0" y="70" width="50" height="24" class="cell"/><text x="160.0" y="110" text-anchor="middle" class="label">leftmost</text><text x="440.0" y="110" text-anchor="middle" class="label">rightmost</text><line x1="440.0" y1="116" x2="440.0" y2="134" class="accent-stroke" stroke-width="1.6" marker-end="url(#mlr-kg-arrow)"/><text x="448.0" y="132.0" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><text x="529.0" y="86" class="label">X(0) = 1</text><line x1="440.0" y1="145" x2="104.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="160.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="216.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="272.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="328.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="384.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="440.0" y2="210" class="muted-stroke" stroke-width="0.8"/><line x1="440.0" y1="145" x2="496.0" y2="210" class="muted-stroke" stroke-width="0.8"/><rect x="79.0" y="210" width="50" height="24" class="cell"/><rect x="135.0" y="210" width="50" height="24" class="cell"/><rect x="191.0" y="210" width="50" height="24" class="head-cell"/><rect x="247.0" y="210" width="50" height="24" class="head-cell"/><rect x="303.0" y="210" width="50" height="24" class="cell"/><rect x="359.0" y="210" width="50" height="24" class="cell"/><rect x="415.0" y="210" width="50" height="24" class="cell"/><rect x="471.0" y="210" width="50" height="24" class="head-cell"/><text x="496.0" y="250" text-anchor="middle" class="label">rightmost</text><text x="216.0" y="250" text-anchor="middle" class="label">leftmost</text><line x1="216.0" y1="256" x2="216.0" y2="274" class="accent-stroke" stroke-width="1.6" marker-end="url(#mlr-kg-arrow)"/><text x="224.0" y="272.0" text-anchor="start" class="math" font-size="15">σ<tspan class="mrm" font-size="10" dy="4">2</tspan></text><text x="529.0" y="226" class="label">X(1) = 0</text><rect x="79.0" y="302" width="22" height="14" class="head-cell"/><text x="107.0" y="313" class="label">extensions τ with large relative measure: the set A</text></svg>
:::

:::theorem[Kučera, Gács]{#thm-kucera-gacs}
Let $\mathcal P$ be a $\Pi^0_1$ class of positive measure. For every set $X$, there is $Z \in \mathcal P$ with $X \leq_T Z$ and $Z \leq_T X \oplus \emptyset'$. In particular, every set is computable from a Martin-Löf random sequence, and every Turing degree above $\obf'$ contains a random sequence.
:::

:::proof{of=thm-kucera-gacs}
Let $\mathcal P = [T]$ with $T$ computable, and let $c$ be such that $\lambda(\mathcal P) \geq 2^{-c}$. Let $m_0 = 0$ and $m_{n+1} = m_n + c + n + 1$. For a string $\sigma$ of length $m_n$, let $A_n(\sigma)$ be the set of strings $\tau \succeq \sigma$ of length $m_{n+1}$ with $\lambda(\mathcal P \mid \tau) \geq 2^{-c-n-1}$. By :ref{#lem-kucera-branching} with $k = c + n$, if $\lambda(\mathcal P \mid \sigma) \geq 2^{-c-n}$, then $A_n(\sigma)$ has at least two elements.

*Construction.* Let $\sigma_0$ be the empty string; $\lambda(\mathcal P \mid \sigma_0) = \lambda(\mathcal P) \geq 2^{-c}$. Given $\sigma_n$ of length $m_n$ with $\lambda(\mathcal P \mid \sigma_n) \geq 2^{-c-n}$, let $\sigma_{n+1}$ be the leftmost element of $A_n(\sigma_n)$ if $X(n) = 0$, and the rightmost one if $X(n) = 1$, for the lexicographic order. It satisfies $\lambda(\mathcal P \mid \sigma_{n+1}) \geq 2^{-c-n-1}$. Let $Z = \bigcup_n \sigma_n$. Each $[\sigma_n]$ meets $\mathcal P$, since it has positive relative measure, so every prefix of $Z$ is extendible in $T$ and $Z \in \mathcal P$.

*$Z \leq_T X \oplus \emptyset'$.* By :ref{#prop-measure-effective} (2) applied to the $\Pi^0_1$ class $\mathcal P \cap [\tau]$, the relative measure $\lambda(\mathcal P \mid \tau)$ is right-c.e., uniformly in $\tau$. So the condition $\lambda(\mathcal P \mid \tau) \geq q$, for a rational $q$, is $\Pi^0_1$: it fails if and only if some approximation from above falls below $q$. With $\emptyset'$, one computes $A_n(\sigma_n)$ from $\sigma_n$, and with $X$ one chooses $\sigma_{n+1}$.

*$X \leq_T Z$.* The sets $A_n(\sigma)$ are co-c.e. uniformly in $n$ and $\sigma$: there are finite sets $A_{n,s}(\sigma)$, computable from $n$, $\sigma$, $s$, decreasing in $s$, with intersection $A_n(\sigma)$. To compute $X(n)$, let $\sigma = Z \uh m_n = \sigma_n$ and $\tau = Z \uh m_{n+1} = \sigma_{n+1}$, and search for a stage $s$ at which $\tau$ is the leftmost or the rightmost element of $A_{n,s}(\sigma)$; output $0$ in the first case and $1$ in the second. Suppose $X(n) = 0$, so that $\tau$ is the leftmost element of $A_n(\sigma)$. The finitely many strings of length $m_{n+1}$ to the left of $\tau$ are not in $A_n(\sigma)$, so they leave $A_{n,s}(\sigma)$ at some stage, and $\tau$ becomes leftmost. On the other hand, $A_n(\sigma)$ has an element to the right of $\tau$, which belongs to every $A_{n,s}(\sigma)$, so $\tau$ is never the rightmost element. The search therefore returns $0$. The case $X(n) = 1$ is symmetric.

For the last statements, take for $\mathcal P$ the $\Pi^0_1$ class of random sequences of :ref{#cor-mlr-structure} (2), of measure at least $\frac12$. If $X \geq_T \emptyset'$, then $Z \leq_T X \oplus \emptyset' \equiv_T X$, so $Z \equiv_T X$.
:::

The reduction of $X$ to $Z$ reads only $Z \uh m_{n+1}$ to compute $X(n)$, a computable bound on the use: it is a **weak truth-table** reduction. The use $m_{n+1}$ grows quadratically in $n$; much better bounds are known (see the notes). The encoding is not computable, since recognizing the nodes $\tau$ with large relative measure requires $\emptyset'$, but the decoding is: the decoder waits for the competitors of $\tau$ to reveal that they have small relative measure.

:::quiz[the Kučera–Gács theorem]
In the decoding procedure of :ref{#thm-kucera-gacs}, why can the search not return the wrong bit?

- [x] Because $A_n(\sigma)$ has at least two elements: if $\tau$ is its leftmost element, another element lies to its right and stays in every approximation, so $\tau$ never appears as the rightmost one.
- [ ] Because the approximations $A_{n,s}(\sigma)$ are computable.

  Computability makes the search effective; correctness comes from the second element of $A_n(\sigma)$.
- [ ] Because $\tau$ belongs to $\mathcal P$.

  $\tau$ is a string; what matters is its position among the strings of $A_n(\sigma)$.

---

Why are the lengths chosen with $m_{n+1} - m_n = c + n + 1$, growing with $n$?

- [x] Because the relative measure guaranteed for $\sigma_n$ is only $2^{-c-n}$, halved at each step, and :ref{#lem-kucera-branching} finds two branching extensions at depth $c + n + 1$ for such a relative measure.
- [ ] Because $X(n)$ must be encoded with $n$ bits.

  Each bit of $X$ is encoded by a binary choice; the extra length is the price of finding a branching.
- [ ] To make $Z$ random.

  $Z$ is random because it lies in $\mathcal P$, whatever the lengths.
:::

## Exercises

::::exercise{difficulty=1}
Show that for every $n \geq 1$ there is a random sequence $Z \equiv_T \emptyset^{(n)}$, and that the class of such sequences is null.

:::solution
Apply :ref{#thm-kucera-gacs} to $X = \emptyset^{(n)}$, which computes $\emptyset'$: the random sequence $Z$ obtained satisfies $Z \equiv_T \emptyset^{(n)}$. The class of sequences computing $\emptyset^{(n)}$ is null by :ref{#thm-sacks}, and contains the class considered.
:::
::::

::::exercise{difficulty=1}
Let $\mathcal P$ be a $\Pi^0_1$ class of positive measure. Show that $\mathcal P$ has a member in every Turing degree above $\obf'$, and a member that is not computably dominated. Compare with the computably dominated basis theorem.

:::solution
For $X \geq_T \emptyset'$, :ref{#thm-kucera-gacs} gives $Z \in \mathcal P$ with $X \leq_T Z \leq_T X \oplus \emptyset' \equiv_T X$. With $X = \emptyset'$, the member $Z \equiv_T \emptyset'$ is $\Delta^0_2$ and not computable, hence not computably dominated (:ref{#def-computably-dominated}). By :ref{#thm-dominated-basis}, $\mathcal P$ also has a computably dominated member: a $\Pi^0_1$ class of positive measure has members of both kinds.
:::
::::

## Notes and references

The Kučera–Gács theorem was proved independently by Kučera (1985) and Gács (1986). The branching lemma and the coding by leftmost and rightmost extensions follow Nies (Lemma 3.3.1 and Theorem 3.3.2); Downey and Hirschfeldt (Theorem 8.3.2) give a proof with martingales, which are the subject of the next course of the track (:ref{to="martingales/betting-strategies"}). The use of the reduction can be made much smaller than in the proof above: Gács obtained a use of $n + O(\sqrt{n} \log n)$, Merkle and Mihailović (2002) simplified his construction, and Barmpalias and Lewis-Pye (2018) showed that a use of $n + g(n)$ can be achieved for every computable non-decreasing $g$ with $\sum_n 2^{-g(n)} < \infty$; by work of Barmpalias, Lewis-Pye and Teutsch (2016), this condition cannot be dropped.

- A. Kučera, *Measure, Π⁰₁-classes and complete extensions of PA*, in: Recursion Theory Week, Lecture Notes in Mathematics 1141, Springer, 1985, 245–259.
- P. Gács, *Every sequence is reducible to a random one*, Information and Control 70 (1986), 186–192.
- W. Merkle and N. Mihailović, *On the construction of effective random sets*, in: Mathematical Foundations of Computer Science 2002, Lecture Notes in Computer Science 2420, Springer, 2002, 568–580.
- G. Barmpalias and A. Lewis-Pye, *Optimal redundancy in computations from random oracles*, Journal of Computer and System Sciences (2018), doi:10.1016/j.jcss.2017.06.009.
- G. Barmpalias, A. Lewis-Pye and J. Teutsch, *Lower bounds on the redundancy in computations from random oracles via betting strategies with restricted wagers*, Information and Computation 251 (2016), 287–300.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Section 8.3.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 3.3.
