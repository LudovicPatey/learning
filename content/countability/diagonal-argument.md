---
title: The diagonal argument
summary: Uncountability of 2^ℕ and Cantor's theorem on power sets, by diagonalization.
duration: 15
prerequisites: [countable-sets]
---

In 1891 Cantor showed that no sequence of infinite binary sequences can enumerate all of them. The argument, known as diagonalization, recurs throughout computability theory: in the undecidability of the halting problem, in the fixed point theorem, and in most constructions of non-computable sets.

We write $\cs$ for the set of infinite binary sequences $X = X(0)\,X(1)\,X(2)\cdots$. Identifying a set $A \subseteq \nat$ with its characteristic sequence, $\cs$ is also the set of all subsets of $\nat$.

:::theorem[Cantor]{#thm-cantor-diagonal}
The set $\cs$ is uncountable: for every sequence $X_0, X_1, X_2, \dots$ of elements of $\cs$, there is a $Y \in \cs$ different from every $X_n$.
:::

:::proof{of=thm-cantor-diagonal}
Arrange the sequences as the rows of an infinite table, and walk down the diagonal, flipping each bit:
$$
Y(n) = 1 - X_n(n).
$$
For every $n$, the sequences $Y$ and $X_n$ differ at position $n$. So $Y$ is none of the $X_n$.
:::

:::figure[The diagonal sequence differs from row $n$ at column $n$.]
<svg viewBox="0 0 330 200" width="330" role="img" aria-label="Binary table with highlighted diagonal" style="font-family: ui-monospace, monospace; font-size: 15px">
<g fill="currentColor"><text x="10" y="38">X₀</text><text x="10" y="68">X₁</text><text x="10" y="98">X₂</text><text x="10" y="128">X₃</text><text x="14" y="152">⋮</text><text x="10" y="188" font-weight="700">Y</text></g>
<g fill="currentColor"><text x="60" y="38">0</text><text x="95" y="38">1</text><text x="130" y="38">1</text><text x="165" y="38">0</text><text x="200" y="38">…</text><text x="60" y="68">1</text><text x="95" y="68">1</text><text x="130" y="68">0</text><text x="165" y="68">1</text><text x="200" y="68">…</text><text x="60" y="98">0</text><text x="95" y="98">0</text><text x="130" y="98">0</text><text x="165" y="98">0</text><text x="200" y="98">…</text><text x="60" y="128">1</text><text x="95" y="128">0</text><text x="130" y="128">1</text><text x="165" y="128">1</text><text x="200" y="128">…</text></g>
<g fill="none" stroke="#4f46e5" stroke-width="2"><rect x="52" y="20" width="24" height="26" rx="5"/><rect x="87" y="50" width="24" height="26" rx="5"/><rect x="122" y="80" width="24" height="26" rx="5"/><rect x="157" y="110" width="24" height="26" rx="5"/></g>
<g fill="#4f46e5" font-weight="700"><text x="60" y="188">1</text><text x="95" y="188">0</text><text x="130" y="188">1</text><text x="165" y="188">0</text><text x="200" y="188">…</text></g>
</svg>
:::

:::quiz
Why is it important that $Y$ is changed **at position $n$** to differ from $X_n$, and not at some other position?

- [x] Each row needs its own position where $Y$ is forced to differ; using the diagonal guarantees that different rows use different positions, so the requirements never conflict.

  Two rows assigned the same position might demand opposite bits there.
- [ ] Because the diagonal is the only place where the table is defined.
- [ ] It is not important; any fixed position $k$ would do for all rows.

  A single bit $Y(k)$ can only differ from $X_n(k)$ for rows with the same value at $k$ — it cannot defeat both a row starting with $0$ and a row starting with $1$ at $k$.

---

Could we fix the argument's "flaw" by simply adding $Y$ to the list, say as $X'_0 = Y$, $X'_{n+1} = X_n$?

- [x] No: the theorem applies to the new list too, producing a new sequence $Y'$ missing from it.

  The argument works against **every** list, so no repair is possible.
- [ ] Yes, and this shows that $\cs$ is countable after all.
- [ ] Only if $Y$ happens to equal one of the $X_n$.

  By construction it never does.
:::

## Every set is smaller than its power set

The same idea works for any set, with no table at all.

:::theorem{#thm-cantor-powerset}
For every set $A$, there is no surjection from $A$ onto its power set $\mathcal P(A)$. Hence $|A| < |\mathcal P(A)|$.
:::

:::proof{of=thm-cantor-powerset}
Let $f : A \to \mathcal P(A)$. Consider
$$
D = \{ a \in A : a \notin f(a) \}.
$$
If $D = f(d)$ for some $d \in A$, then $d \in D \iff d \notin f(d) = D$, a contradiction. So $D$ is not in the image of $f$. Finally $a \mapsto \{a\}$ is an injection $A \to \mathcal P(A)$, so $|A| \leq |\mathcal P(A)|$, and the inequality is strict.
:::

:::quiz
How is this proof the "same" as the previous one, when $A = \nat$?

- [x] $f(n)$ plays the role of the row $X_n$, and $n \in D$ iff $n \notin f(n)$ is exactly "flip the $n$-th bit of the $n$-th row".
- [ ] $D$ corresponds to the first row of the table.
- [ ] They are unrelated; the second proof uses the axiom of choice.

  Neither proof uses choice.
:::

Iterating, $\nat$, $\mathcal P(\nat)$, $\mathcal P(\mathcal P(\nat))$, … are infinite sets of strictly increasing size: there is no largest infinity.

## Looking ahead

Since there are countably many programs and uncountably many sets of integers, some sets are not computable. This cardinality argument is not constructive. Diagonalizing against the enumeration $\Phi_0, \Phi_1, \Phi_2, \dots$ of partial computable functions yields an explicit non-computable set, the halting problem, studied in the course on fundamentals.
