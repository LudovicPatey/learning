---
title: Martin's domination theorem
summary: A set is high if and only if it computes a function that eventually dominates every computable function, if and only if it computes a uniform list of exactly the computable sets.
duration: 40
prerequisites: [computably-dominated, turing-degrees/low-and-high, arithmetic-hierarchy/index-sets, arithmetic-hierarchy/post-theorem]
---

Hyperimmune functions escape every computable function infinitely often. A stronger growth property asks a function to be above every computable function from some point on. No function is above every computable function everywhere, since the constant functions are computable; but a function can **eventually dominate** each of them. Martin showed that the sets computing such a function are exactly the **high** sets, the sets whose jump computes $\emptyset''$. Highness is defined through the jump; Martin's theorem turns it into a property of growth, which is how it is used in most constructions.

This lesson proves Martin's theorem and Jockusch's characterization of the high sets as the sets that can list the computable sets uniformly. Applications to maximal sets and to DNC functions are given in :ref{to="immunity-growth/high-or-dnc"}.

We write $\forall^\infty n$ for "for all but finitely many $n$" and $\exists^\infty n$ for "for infinitely many $n$".

:::definition{#def-dominant}
A function $g$ **eventually dominates** $f$ if $\forall^\infty n\ f(n) \leq g(n)$. A function is **dominant** if it eventually dominates every computable function.
:::

:::figure[Two growth properties, relative to one computable function $g$. Left: a hyperimmune function exceeds $g$ at infinitely many points, and may be small elsewhere. Right: a dominant function exceeds $g$ at all points from some $n_0$ on, where $n_0$ depends on $g$.]
<svg class="fig" viewBox="0 0 600 230" width="600" role="img" aria-label="Left: a hyperimmune function exceeds a computable function g at infinitely many points but may stay small elsewhere. Right: a dominant function is above g from some point n0 on"><line x1="30" y1="180" x2="288" y2="180" class="axis"/><line x1="30" y1="180" x2="30" y2="22" class="axis"/><text x="292" y="184" class="math" font-size="13">n</text><text x="155.0" y="14" text-anchor="middle" class="label">hyperimmune: above g infinitely often</text><polyline points="30.0,165.0 42.5,160.5 55.0,156.0 67.5,151.5 80.0,147.0 92.5,142.5 105.0,138.0 117.5,133.5 130.0,129.0 142.5,124.5 155.0,120.0 167.5,115.5 180.0,111.0 192.5,106.5 205.0,102.0 217.5,97.5 230.0,93.0 242.5,88.5 255.0,84.0 267.5,79.5 280.0,75.0" class="ink-stroke" stroke-width="1.3"/><polyline points="30.0,175.0 42.5,170.0 55.0,175.0 67.5,170.0 80.0,135.0 92.5,170.0 105.0,175.0 117.5,165.0 130.0,170.0 142.5,170.0 155.0,165.0 167.5,95.0 180.0,165.0 192.5,170.0 205.0,160.0 217.5,165.0 230.0,165.0 242.5,165.0 255.0,160.0 267.5,35.0 280.0,160.0" class="accent-stroke" stroke-width="1.8"/><circle cx="80.0" cy="135.0" r="3" class="accent-fill"/><circle cx="167.5" cy="95.0" r="3" class="accent-fill"/><circle cx="267.5" cy="35.0" r="3" class="accent-fill"/><line x1="330" y1="180" x2="588" y2="180" class="axis"/><line x1="330" y1="180" x2="330" y2="22" class="axis"/><text x="592" y="184" class="math" font-size="13">n</text><text x="455.0" y="14" text-anchor="middle" class="label">dominant: above g from some point on</text><polyline points="330.0,165.0 342.5,160.5 355.0,156.0 367.5,151.5 380.0,147.0 392.5,142.5 405.0,138.0 417.5,133.5 430.0,129.0 442.5,124.5 455.0,120.0 467.5,115.5 480.0,111.0 492.5,106.5 505.0,102.0 517.5,97.5 530.0,93.0 542.5,88.5 555.0,84.0 567.5,79.5 580.0,75.0" class="ink-stroke" stroke-width="1.3"/><polyline points="330.0,177.5 342.5,177.0 355.0,175.0 367.5,173.0 380.0,170.0 392.5,165.0 405.0,157.5 417.5,150.0 430.0,140.0 442.5,130.0 455.0,120.0 467.5,110.0 480.0,100.0 492.5,90.0 505.0,80.0 517.5,70.0 530.0,60.0 542.5,52.5 555.0,45.0 567.5,37.5 580.0,32.5" class="accent-stroke" stroke-width="1.8"/><circle cx="467.5" cy="110.0" r="3" class="accent-fill"/><circle cx="480.0" cy="100.0" r="3" class="accent-fill"/><circle cx="492.5" cy="90.0" r="3" class="accent-fill"/><circle cx="505.0" cy="80.0" r="3" class="accent-fill"/><circle cx="517.5" cy="70.0" r="3" class="accent-fill"/><circle cx="530.0" cy="60.0" r="3" class="accent-fill"/><circle cx="542.5" cy="52.5" r="3" class="accent-fill"/><circle cx="555.0" cy="45.0" r="3" class="accent-fill"/><circle cx="567.5" cy="37.5" r="3" class="accent-fill"/><circle cx="580.0" cy="32.5" r="3" class="accent-fill"/><line x1="455.0" y1="180" x2="455.0" y2="40" class="muted-stroke" stroke-dasharray="3 3"/><text x="455.0" y="196" text-anchor="middle" class="math" font-size="13">n<tspan class="mrm" font-size="9" dy="3">0</tspan></text><line x1="150" y1="222" x2="170" y2="222" class="ink-stroke" stroke-width="1.3"/><text x="176" y="226" class="label">a computable function g</text><line x1="340" y1="222" x2="360" y2="222" class="accent-stroke" stroke-width="1.8"/><text x="366" y="226" class="label">the function f</text></svg>
:::

A dominant function is hyperimmune: a computable $g$ dominating it everywhere would be eventually dominated by it, and so would $g + 1$, which is impossible. Recall from :ref{#def-high} that $A$ is **high** if $A' \geq_T \emptyset''$, and from :ref{#thm-tot-complete} that $\mathrm{Tot} = \{ e : \Phi_e \text{ is total} \}$ is $\Pi^0_2$-complete, so $\mathrm{Tot} \equiv_T \emptyset''$.

## Martin's theorem

Both directions of the theorem rest on the set $\mathrm{Tot}$. For ($\Rightarrow$), a high set approximates $\mathrm{Tot}$ in the limit, and can therefore wait for the computations $\Phi_e(x)$ of the total functions $\Phi_e$ without waiting forever on the partial ones, from some point on. For ($\Leftarrow$), a dominant function bounds the running time of every total $\Phi_e$ from some point on, which turns totality into a $\Sigma^0_2(A)$ property.

:::theorem[Martin]{#thm-martin-domination}
A set $A$ is high if and only if it computes a dominant function.
:::

:::proof{of=thm-martin-domination}
($\Rightarrow$) Since $A$ is high, $\mathrm{Tot} \leq_T \emptyset'' \leq_T A'$. By the limit lemma relative to $A$ (:ref{#thm-limit-lemma}), there is an $A$-computable function $a(e, s)$ with $\lim_s a(e, s) = \mathrm{Tot}(e)$ for every $e$. Define $g(x)$ as follows. For each $e \leq x$, search for the least $s \geq x$ such that $\Phi_e(x)[s]\converge$ or $a(e, s) = 0$. The search terminates: if $\Phi_e$ is total, $\Phi_e(x)$ converges at some stage; otherwise $a(e, s) = 0$ for all large $s$. Let $v_e = \Phi_e(x)$ if the search ended with $\Phi_e(x)[s]\converge$, and $v_e = 0$ otherwise. Let $g(x) = \sum_{e \leq x} v_e$. It is $A$-computable.

Let $\Phi_e$ be total. Let $s_0$ be such that $a(e, s) = 1$ for all $s \geq s_0$. For $x \geq \max(e, s_0)$, the search for $e$ starts at $s \geq x \geq s_0$, never meets $a(e, s) = 0$, and ends with the convergence of $\Phi_e(x)$; so $v_e = \Phi_e(x)$ and $g(x) \geq \Phi_e(x)$. Hence $g$ eventually dominates $\Phi_e$.

($\Leftarrow$) Let $g \leq_T A$ be dominant. If $\Phi_e$ is total, the function $t_e(x)$, the least $s$ with $\Phi_e(x)[s]\converge$, is computable, so $\forall^\infty x\ t_e(x) \leq g(x)$. Hence
$$
e \in \mathrm{Tot} \iff \exists k\ \big[\ \forall x \geq k\ \ \Phi_e(x)[g(x)]\converge \ \text{ and } \ \forall x < k\ \ \Phi_e(x)\converge\ \big].
$$
If $e \in \mathrm{Tot}$, take $k$ such that $t_e(x) \leq g(x)$ for $x \geq k$. Conversely, the right-hand side states that $\Phi_e$ converges on every input. Inside the brackets, the first condition is $\Pi^0_1(A)$ and the second is $\Sigma^0_1$, so $\mathrm{Tot}$ is $\Sigma^0_2(A)$. It is also $\Pi^0_2$, hence $\Pi^0_2(A)$. So $\mathrm{Tot}$ is $\Delta^0_2(A)$, that is, computable in $A'$ by Post's theorem relative to $A$ (:ref{#thm-post}). Hence $\emptyset'' \leq_T A'$.
:::

:::corollary{#cor-high-hyperimmune}
Every high set has hyperimmune degree. No computably dominated set is high.
:::

The corollary follows from the remark that dominant functions are hyperimmune. Combined with :ref{#cor-ce-hyperimmune}, it shows that hyperimmunity is much weaker than highness: every non-zero c.e. degree is hyperimmune, while low c.e. sets are not high.

:::quiz[Martin's theorem]
In ($\Rightarrow$), why does the search for $e$ start at $s \geq x$, and not at $s = 0$?

- [x] So that, for large $x$, the search only looks at stages where the approximation $a(e, s)$ has already settled, and cannot stop on an early wrong value $0$.
- [ ] To make the search terminate.

  The search terminates whatever its starting point.
- [ ] To make $g$ increasing.

  $g$ need not be increasing, and this plays no role.

---

In ($\Leftarrow$), why is the clause "$\forall x < k\ \Phi_e(x)\converge$" needed?

- [x] Because the bound $g(x)$ only controls the computations from $k$ on; without the clause, a function diverging on a small input would satisfy the condition.
- [ ] Because $g$ may take the value $0$.

  The values of $g$ play no role below $k$.
- [ ] To make the condition $\Sigma^0_2(A)$.

  The clause is $\Sigma^0_1$; it is needed for correctness, and it keeps the condition $\Sigma^0_2(A)$.
:::

## Lists of computable sets

The computable sets cannot be listed computably: a uniformly computable sequence $(X_n)$ of sets misses the computable set $\{ n : n \notin X_n \}$. A dominant function makes such a list possible. The idea is to run each program $\Phi_e$ with a time bound given by the dominant function; the bound is eventually sufficient for the total programs, and the finitely many early inputs are handled by a parameter. Jockusch showed that this ability characterizes the high sets.

:::theorem[Jockusch]{#thm-jockusch-lists}
A set $A$ is high if and only if there is a uniformly $A$-computable sequence of sets $(X_n)$ whose members are exactly the computable sets.
:::

:::proof{of=thm-jockusch-lists}
($\Rightarrow$) Let $g \leq_T A$ be dominant, by :ref{#thm-martin-domination}. For $e, i \in \nat$ and every $x$, let
$$
X_{\langle e, i \rangle}(x) = \begin{cases} \Phi_e(x) & \text{if } \Phi_e(y)[i + g(y)]\converge \in \{0, 1\} \text{ for every } y \leq x, \\ 0 & \text{otherwise.} \end{cases}
$$
The sequence is uniformly $A$-computable. Each $X_{\langle e, i \rangle}$ is computable: either the condition holds for every $x$, and $X_{\langle e, i \rangle} = \Phi_e$ is a total computable $\{0, 1\}$-valued function; or it fails for a least $x_0$, hence for every $x \geq x_0$, and $X_{\langle e, i \rangle}$ is finite. Conversely, let $X = \Phi_e$ be computable, and let $t(y)$ be the least $s$ with $\Phi_e(y)[s]\converge$, a computable function. There is $y_0$ with $t(y) \leq g(y)$ for $y \geq y_0$; let $i = \max_{y < y_0} t(y)$. Then $t(y) \leq i + g(y)$ for every $y$, so $X_{\langle e, i \rangle} = X$.

($\Leftarrow$) Let $(X_j)$ be such a sequence. We show that $\mathrm{Tot}$ is $\Sigma^0_2(A)$. For each $e$, let $\psi_e$ be the partial computable $\{0, 1\}$-valued function defined by the following procedure, uniformly in $e$. At stage $t$, for each $n \leq t$ such that $\psi_e(n)$ is not yet defined:

- if $\Phi_n(n)[t]\converge$, let $\psi_e(n) = 1$ if $\Phi_n(n) = 0$, and $\psi_e(n) = 0$ otherwise;
- otherwise, if $\Phi_e(k)[t]\converge$ for every $k \leq n$, let $\psi_e(n) = 0$.

If $e \in \mathrm{Tot}$, every $n$ eventually satisfies the second clause, so $\psi_e$ is total; it is then a computable set, equal to some $X_j$. If $e \notin \mathrm{Tot}$, let $k_0$ be such that $\Phi_e(k_0)\diverge$. For $n \geq k_0$, the second clause never applies, so $\psi_e(n)$ is defined exactly when $\Phi_n(n)\converge$, and then $\psi_e(n) \neq \Phi_n(n)$. No computable set $X$ extends $\psi_e$: an index $n \geq k_0$ of $X$ exists by the padding lemma, and $\psi_e(n)$ is then defined and different from $\Phi_n(n) = X(n)$. So
$$
e \in \mathrm{Tot} \iff \exists j\ \forall n\ \forall t\ \big[\ \psi_e(n)[t]\converge \ \Rightarrow\ X_j(n) = \psi_e(n)\ \big],
$$
which is $\Sigma^0_2(A)$, since the sequence $(X_j)$ is uniformly $A$-computable. As $\mathrm{Tot}$ is also $\Pi^0_2$, it is $\Delta^0_2(A)$, hence computable in $A'$ by :ref{#thm-post}, and $\emptyset'' \equiv_T \mathrm{Tot} \leq_T A'$.
:::

The function $\psi_e$ of ($\Leftarrow$) uses the same diagonal as the class $\mathrm{DNC}_2$ (:ref{#thm-dnc2-no-computable}): a partial computable $\{0, 1\}$-valued function, here the restriction of $\psi_e$ to the inputs $n \geq k_0$, that has no computable completion. Totality of $\Phi_e$ fills its gaps with zeros; partiality leaves the diagonal alone, and the list, which contains only computable sets, cannot follow it.

:::quiz[lists of computable sets]
In ($\Rightarrow$), why is the parameter $i$ needed in the time bound $i + g(y)$?

- [x] Because $g$ bounds the running time $t$ of a total $\Phi_e$ only from some $y_0$ on; $i$ covers the finitely many inputs below $y_0$.
- [ ] Because $g$ may not be computable.

  $g$ is $A$-computable, which is all the construction needs; the parameter is about the inputs where $g$ is too small.
- [ ] To make the sets $X_{\langle e, i \rangle}$ computable.

  They are computable for every $i$; the parameter ensures that every computable set appears.

---

In ($\Leftarrow$), when $\Phi_e$ is partial, the second clause may define $\psi_e(n) = 0$ for some $n < k_0$. Why does no computable set extend $\psi_e$ nevertheless?

- [x] Because every computable set has an index $n \geq k_0$, by the padding lemma, and at such an index $\psi_e$ disagrees with the diagonal; the values below $k_0$ play no role.
- [ ] Because $\psi_e$ is undefined at every $n < k_0$.

  The second clause may apply below $k_0$, since $\Phi_e(k)$ may converge for every $k \leq n < k_0$.
- [ ] Because a computable set is total, and $\psi_e$ is partial.

  A total function may extend a partial one; the obstruction is the disagreement with the diagonal.
:::

## Exercises

::::exercise{difficulty=1}
Show that the following are equivalent for a set $A$: (1) $A$ computes a dominant function; (2) there is a uniformly $A$-computable sequence of total functions containing every computable function.

:::solution
(1 ⇒ 2) Let $g \leq_T A$ be dominant. As in the proof of :ref{#thm-jockusch-lists}, let $f_{\langle e, i \rangle}(x) = \Phi_e(x)$ if $\Phi_e(y)[i + g(y)]\converge$ for every $y \leq x$, and $f_{\langle e, i \rangle}(x) = 0$ otherwise. These functions are total and uniformly $A$-computable, and every total computable function $\Phi_e$ is equal to $f_{\langle e, i \rangle}$ for a suitable $i$.

(2 ⇒ 1) Let $(f_i)$ be the sequence and $g(n) = \sum_{i \leq n} f_i(n)$; it is $A$-computable. A computable function is some $f_i$, and $g(n) \geq f_i(n)$ for every $n \geq i$.
:::
::::

::::exercise{difficulty=2}
Show that a set $A$ is high if and only if $A$ computes a function $g$ such that, for every total computable function $\Phi_e$, $\forall^\infty x\ \Phi_e(x)[g(x)]\converge$.

:::solution
If $A$ is high, a dominant $g \leq_T A$ eventually dominates the computable function $t_e$, the convergence time of $\Phi_e$, so $\Phi_e(x)[g(x)]\converge$ for almost every $x$. Conversely, given such a $g$, the function $\hat g(x) = \max_{e \leq x} \Phi_e(x)[g(x)]$, where divergent computations count as $0$, is $A$-computable. For a total computable $f = \Phi_e$, $\Phi_e(x)[g(x)]\converge$ for almost every $x$, so $\hat g(x) \geq f(x)$ for almost every $x \geq e$. So $\hat g$ is dominant and $A$ is high by :ref{#thm-martin-domination}.
:::
::::

## Notes and references

Martin (1966) proved the domination theorem; Soare calls it the high domination theorem (Soare 2016, Theorem 4.5.6). The characterization by lists of computable sets is due to Jockusch (1972); Soare (2016, Theorem 4.8.2) proves it together with the version for functions of the first exercise, and our proof of ($\Rightarrow$) follows his. Monin and Patey prove both theorems in the section *Martin's domination theorem* of their chapter *Immunity and function growth*; our proof of ($\Leftarrow$) in :ref{#thm-jockusch-lists} is a variant of theirs. Relativized to a set $X \leq_T \emptyset'$, Martin's theorem characterizes the sets that are low₂ by domination (Soare 2016, Theorem 4.6.1).

- D. A. Martin, *Classes of recursively enumerable sets and degrees of unsolvability*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 12 (1966), 295–310.
- C. G. Jockusch, *Degrees in which the recursive sets are uniformly recursive*, Canadian Journal of Mathematics 24 (1972), 1092–1099.
- R. I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016, Sections 4.5, 4.6 and 4.8.
- B. Monin and L. Patey, *Computability theory*, chapter *Immunity and function growth*.
