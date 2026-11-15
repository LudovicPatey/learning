---
title: α-large sets and fast-growing functions
summary: Ordinals below ε₀ in Cantor normal form and their fundamental sequences; α-large finite sets, which generalize relative largeness; the decomposition of (β + γ)-large sets; the least y such that [x, y) is ω^k-large is F_k(x), and ω^α-largeness defines the Schwichtenberg–Wainer hierarchy; IΣ₁ does not prove that every interval contains an ω^ω-large one; the theorems of Ketonen–Solovay and Schwichtenberg–Wainer are stated.
duration: 40
prerequisites: [ph-unprovable, computable-ordinals/ordinals]
---

Relative largeness, $|A| > \min A$, is one step of a scale of largeness notions indexed by ordinals, introduced by Ketonen and Solovay. A set is $\alpha$-large when one can descend from $\alpha$ to $0$ by reading its elements in increasing order, each element $a$ allowing one step $\beta \mapsto \beta[a]$ down a fundamental sequence. For finite $\alpha = n$, this means having $n$ elements; for $\alpha = \omega$ it is relative largeness. The scale measures the growth of the functions met in this course exactly: the least $y$ such that $[x, y)$ is $\omega^k$-large is $F_k(x)$, so lessons 1–3 were about $\omega^k$-large intervals, and the Paris–Harrington function of lesson 7 lives at the level $\varepsilon_0$.

## Ordinals below ε₀

We use the ordinal arithmetic of :ref{to="computable-ordinals/ordinals"}. Every ordinal $\alpha > 0$ has a unique **Cantor normal form**
$$
\alpha = \omega^{\gamma_1} + \omega^{\gamma_2} + \cdots + \omega^{\gamma_r}, \qquad \gamma_1 \geq \gamma_2 \geq \cdots \geq \gamma_r .
$$
Let $\omega_0 = 1$ and $\omega_{n+1} = \omega^{\omega_n}$, so that $\omega_1 = \omega$, $\omega_2 = \omega^\omega$; $\varepsilon_0 = \sup_n \omega_n$ is the least ordinal with $\omega^{\varepsilon_0} = \varepsilon_0$. Below $\varepsilon_0$ the exponents are smaller than the ordinal, so the normal form can be iterated on the exponents, and these ordinals have finite notations; their comparison and arithmetic are primitive recursive on the notations (Hájek and Pudlák, Chapter II, Section 3(a), carry this out in $\mathrm I\Sigma_1$). We write $\beta + \gamma$ **in normal form** when the last exponent of $\beta$ is at least the first exponent of $\gamma$; then the normal form of $\beta + \gamma$ is the concatenation of those of $\beta$ and $\gamma$.

:::definition{#def-fundamental-sequence}
For $\alpha < \varepsilon_0$ and $x \in \nat$, the ordinal $\{ \alpha \}(x)$ is defined as follows: $\{ 0 \}(x) = 0$; $\{ \beta + 1 \}(x) = \beta$; and if $\alpha = \beta + \omega^\gamma$ in normal form with $\gamma > 0$,
$$
\{ \alpha \}(x) = \begin{cases} \beta + \omega^\delta \cdot x & \text{if } \gamma = \delta + 1, \\ \beta + \omega^{\{ \gamma \}(x)} & \text{if } \gamma \text{ is a limit.} \end{cases}
$$
For a limit $\lambda$, the sequence $\lambda[x] = \{ \lambda \}(x)$ is the **fundamental sequence** of $\lambda$.
:::

For instance $\{ \omega \}(x) = x$, $\{ \omega \cdot 2 \}(x) = \omega + x$, $\{ \omega^2 \}(x) = \omega \cdot x$, $\{ \omega^\omega \}(x) = \omega^x$ and $\{ \varepsilon_0 \}(x) = \omega_x$ if one sets $\varepsilon_0[x] = \omega_x$. For a limit $\lambda$, $\lambda[x] < \lambda$ and $\lambda = \sup_x \lambda[x]$; and if $\beta + \gamma$ is in normal form with $\gamma > 0$, then $\{ \beta + \gamma \}(x) = \beta + \{ \gamma \}(x)$, by inspection of the definition.

## α-large sets

:::definition[Ketonen, Solovay]{#def-alpha-large}
Let $A = \{ a_0 < a_1 < \cdots < a_q \}$ be a finite set and $\alpha < \varepsilon_0$. Put $\alpha_0 = \alpha$ and $\alpha_{i+1} = \{ \alpha_i \}(a_i)$. $A$ is **$\alpha$-large** if $\alpha_{q+1} = 0$.
:::

Since $\{ 0 \}(x) = 0$, a set that is $\alpha$-large remains $\alpha$-large when elements are added above its maximum.

:::example{#ex-alpha-large}
1. For finite $\alpha = n$, each element lowers the ordinal by one: $A$ is $n$-large if and only if $|A| \geq n$.
2. $A$ is $\omega$-large if and only if $\{ a_1, \dots, a_q \}$ is $a_0$-large, that is $q \geq a_0$: if and only if $|A| > \min A$. So $\omega$-large is **relatively large** (:ref{#def-relatively-large}).
3. $\{ \omega^2 \}(a_0) = \omega \cdot a_0$, so $A$ is $\omega^2$-large if and only if $A \setminus \{ a_0 \}$ is $\omega \cdot a_0$-large; by the next lemma, this means that $A \setminus \{ a_0 \}$ contains $a_0$ consecutive relatively large blocks. For instance, with $a_0 = 3$, the set $\{ 3 \} \cup [4, 8] \cup [9, 18] \cup [19, 38] = [3, 39)$ is $\omega^2$-large and no proper initial segment of it is; in accordance with the next theorem, $F_2(3) = 39$ (:ref{#ex-fgh-values}).
:::

:::figure[An $\omega^2$-large set with least element $3$: after $3$, three consecutive relatively large blocks, with $5 > 4$, $10 > 9$ and $20 > 19$ elements (the last block is drawn abridged).]
<svg class="fig" viewBox="0 0 600 140" width="600" role="img" aria-label="An omega squared large set with least element 3: after the first element, the set splits into three consecutive omega-large blocks, each with more elements than its least element"><line x1="20.0" y1="70.0" x2="580.0" y2="70.0" class="muted-stroke" stroke-width="1.0"/><circle cx="30.0" cy="70.0" r="4" class="ink-fill"/><text x="30.0" y="56.0" text-anchor="middle" class="math" font-size="13">3</text><circle cx="56.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="82.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="108.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="134.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="160.0" cy="70.0" r="3.5" class="accent-fill"/><path d="M51,82 L51,88 L165,88 L165,82" class="muted-stroke" stroke-width="1.2" fill="none"/><circle cx="186.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="212.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="238.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="264.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="290.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="316.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="342.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="368.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="394.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="420.0" cy="70.0" r="3.5" class="accent-fill"/><path d="M181,82 L181,88 L425,88 L425,82" class="muted-stroke" stroke-width="1.2" fill="none"/><circle cx="446.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="472.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="498.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="524.0" cy="70.0" r="3.5" class="accent-fill"/><circle cx="550.0" cy="70.0" r="3.5" class="accent-fill"/><path d="M441,82 L441,88 L555,88 L555,82" class="muted-stroke" stroke-width="1.2" fill="none"/><text x="108.0" y="106.0" text-anchor="middle" class="label">5 &gt; 4</text><text x="303.0" y="106.0" text-anchor="middle" class="label">10 &gt; 9</text><text x="518.0" y="106.0" text-anchor="middle" class="label">20 &gt; 19 (continues)</text><text x="56.0" y="56.0" text-anchor="middle" class="math" font-size="13">4</text><text x="186.0" y="56.0" text-anchor="middle" class="math" font-size="13">9</text><text x="446.0" y="56.0" text-anchor="middle" class="math" font-size="13">19</text><text x="580.0" y="20.0" text-anchor="end" class="label">three ω-large blocks after the least element 3</text></svg>
:::

:::lemma[Ketonen, Solovay]{#lem-large-sum}
Let $\beta + \gamma$ be in normal form, with $\gamma > 0$, and $A$ a finite set. Then $A$ is $(\beta + \gamma)$-large if and only if some initial segment of $A$ is $\gamma$-large and, for the shortest such initial segment $B$, the set $A \setminus B$ is $\beta$-large.
:::

:::proof{of=lem-large-sum}
Run the definition on $A = \{ a_0 < \cdots < a_q \}$ for $\gamma$ and for $\beta + \gamma$, with ordinals $\gamma_i$ and $\alpha_i$. As long as $\gamma_i \neq 0$, $\alpha_i = \beta + \gamma_i$ in normal form: this holds for $i = 0$, and if it holds for $i$ with $\gamma_i \neq 0$, then $\alpha_{i+1} = \{ \beta + \gamma_i \}(a_i) = \beta + \{ \gamma_i \}(a_i) = \beta + \gamma_{i+1}$, and $\beta + \gamma_{i+1}$ is again in normal form, since the exponents of $\gamma_{i+1}$ are at most those of $\gamma_i$. If $\gamma_i \neq 0$ for all $i \leq q + 1$, then $\alpha_{q+1} = \beta + \gamma_{q+1} \neq 0$, and no initial segment of $A$ is $\gamma$-large. Otherwise let $p$ be least with $\gamma_p = 0$; $B = \{ a_0, \dots, a_{p-1} \}$ is the shortest $\gamma$-large initial segment, $\alpha_p = \beta$, and the run continues on $A \setminus B$ from $\beta$. So $A$ is $(\beta + \gamma)$-large if and only if $A \setminus B$ is $\beta$-large.
:::

:::quiz[the decomposition of large sets]
In the proof of :ref{#lem-large-sum}, where is it used that $\beta + \gamma$ is in normal form?

- [x] To compute $\{ \beta + \gamma_i \}(x) = \beta + \{ \gamma_i \}(x)$: the step only acts on the last term of the normal form, which belongs to $\gamma_i$ when the concatenation is the normal form.
- [ ] To ensure that $\gamma$ is a limit.

  $\gamma$ may be a successor; the lemma holds for every $\gamma > 0$.
- [ ] To ensure that $A$ is finite.

  $A$ is finite by hypothesis.

---

Why does the lemma speak of the *shortest* $\gamma$-large initial segment?

- [x] Once the $\gamma$-part reaches $0$, the next elements already work on $\beta$; longer $\gamma$-large initial segments exist, but their extra elements were used by $\beta$.
- [ ] Because $\gamma$-large sets have a unique initial segment.

  Every extension of a $\gamma$-large initial segment within $A$ is again $\gamma$-large.
- [ ] Because $\beta$-large sets must be short.

  No length restriction is involved.
:::

## Largeness and growth

For $\alpha < \varepsilon_0$ and $x \in \nat$, let $L_\alpha(x)$ be the least $y$ such that the interval $[x, y) = \{ x, \dots, y - 1 \}$ is $\alpha$-large. It exists, since the run on $[x, \infty)$ is a decreasing sequence of ordinals until it reaches $0$, and ordinals are well-ordered. Reading off the first element gives the recursion
$$
L_0(x) = x, \qquad L_{\alpha + 1}(x) = L_\alpha(x + 1), \qquad L_\lambda(x) = L_{\lambda[x]}(x + 1) \text{ for limit } \lambda,
$$
and :ref{#lem-large-sum} gives $L_{\beta + \gamma}(x) = L_\beta(L_\gamma(x))$ when $\beta + \gamma$ is in normal form with $\gamma > 0$: the shortest $\gamma$-large initial segment of $[x, y)$ is $[x, L_\gamma(x))$ when $y \geq L_\gamma(x)$.

:::theorem{#thm-large-fgh}
For every $k \in \nat$ and every $x$, $L_{\omega^k}(x) = F_k(x)$: $F_k(x)$ is the least $y$ such that $[x, y)$ is $\omega^k$-large.
:::

:::proof{of=thm-large-fgh}
For $k = 0$, $L_1(x) = L_0(x + 1) = x + 1 = F_0(x)$. For the induction step, $\omega^{k+1}$ is a limit with $\{ \omega^{k+1} \}(x) = \omega^k \cdot x$, so $L_{\omega^{k+1}}(x) = L_{\omega^k \cdot x}(x + 1)$. Since $\omega^k \cdot (t + 1) = \omega^k \cdot t + \omega^k$ in normal form, the composition rule gives $L_{\omega^k \cdot t} = L_{\omega^k}^{(t)}$ by induction on $t$. So $L_{\omega^{k+1}}(x) = L_{\omega^k}^{(x)}(x + 1) = F_k^{(x)}(x + 1) = F_{k+1}(x)$.
:::

The same computation, for all $\alpha < \varepsilon_0$, shows that $F_\alpha = L_{\omega^\alpha}$ satisfies
$$
F_0(x) = x + 1, \qquad F_{\alpha+1}(x) = F_\alpha^{(x)}(x + 1), \qquad F_\lambda(x) = F_{\lambda[x]}(x + 1),
$$
since $\{ \omega^\lambda \}(x) = \omega^{\lambda[x]}$. This is the version of the **Schwichtenberg–Wainer hierarchy** used by Hájek and Pudlák (II.3.22 and Theorem II.3.30). For instance $F_\omega(x) = F_x(x + 1)$, the diagonal of the hierarchy of lesson 1.

:::corollary{#cor-omega-omega-large}
The sentence "for every $x$ there is $y$ such that $[x, y)$ is $\omega^\omega$-large" is true and not provable in $\mathrm I\Sigma_1$.
:::

:::proof{of=cor-omega-omega-large}
The relation "$[x, y)$ is $\omega^\omega$-large" is primitive recursive: the ordinals that occur are below $\omega^\omega$, given by finite sequences of coefficients, and the run has $y - x$ steps. By :ref{#thm-pr-provably-total}, it has a $\Delta_1$ definition in $\mathrm I\Sigma_1$ that defines it in $\nat$. If $\mathrm I\Sigma_1$ proved the sentence, the function $x \mapsto$ least $y$ would be provably total, hence bounded by some $F_n(x) + n$ (:ref{#thm-isigma1-envelope}). This function is $L_{\omega^\omega}(x) = F_\omega(x) = F_x(x + 1) \geq F_x(x)$, and $F_x(x) > F_n(x) + n$ for $x \geq n + 1$, as in the proof of :ref{#cor-pr-fgh-bound}. The sentence is true since $L_{\omega^\omega}$ is total.
:::

For each standard $k$, by contrast, $\mathrm I\Sigma_1$ proves that every interval $[x, \infty)$ contains an $\omega^k$-large interval, by a formalization of :ref{#thm-large-fgh} (Hájek and Pudlák, Theorem II.3.32 and Fact II.3.34) and :ref{#lem-fgh-isigma1}. On the scale of $\alpha$-largeness, the strength of $\mathrm I\Sigma_1$ is thus located at the level $\omega^\omega = \omega_2$: it proves the existence of $\omega^k$-large intervals for each $k < \omega$, and not of $\omega^\omega$-large ones.

## The theorems of Ketonen–Solovay and Schwichtenberg–Wainer

The same picture holds at every level of the hierarchy of fragments. We state the results and do not prove them.

:::theorem[Schwichtenberg; Wainer]{#thm-schwichtenberg-wainer}
A function is provably total in $\mathrm{PA}$ if and only if it is primitive recursive in $F_\alpha$ for some $\alpha < \varepsilon_0$; for $k \geq 1$, it is provably total in $\mathrm I\Sigma_k$ if and only if it is primitive recursive in $F_\alpha$ for some $\alpha < \omega_k$.
:::

Hájek and Pudlák prove this by indicators (Theorem IV.3.5 with Lemma IV.3.4): the functions $x \mapsto L_{\omega_n}(x)$, $n \in \nat$, form an envelope for $\mathrm{PA}$, with similar envelopes for $\mathrm I\Sigma_k$, the indicators being built from $\alpha$-largeness and "Paris sequences of the second kind" (Section IV.3(d)). For $k = 1$, $\omega_1 = \omega$, and the functions primitive recursive in some $F_n$ are the primitive recursive functions, in accordance with :ref{#thm-isigma1-envelope}; in terms of largeness, the ordinals $\omega^\alpha$ with $\alpha < \omega$ are those below $\omega^\omega = \omega_2$. Consequently $\mathrm{PA}$ does not prove that $F_{\varepsilon_0}$ is total, with $F_{\varepsilon_0}(x) = F_{\omega_x}(x + 1)$; equivalently, it does not prove that every interval $[x, \infty)$ contains an $\omega^{\varepsilon_0} = \varepsilon_0$-large interval.

Ketonen and Solovay (1981) related the two notions of largeness directly, by finite combinatorics. They showed that relatively large homogeneous sets for colorings of $(k+1)$-sets exist in every interval that is $\alpha$-large for an ordinal $\alpha$ of the order of $\omega_{k+d}$, with a small constant $d$ (Hájek and Pudlák quote the precise statement, which also involves the number of colors, in the comment after Theorem II.3.36), and computed the growth of the corresponding Paris–Harrington functions, which is that of the hierarchy at the level $\omega_k$. As a consequence, the function $g$ of :ref{#cor-ph-envelope} grows at the level $\varepsilon_0$, and the unprovability of $\mathrm{PH}$ in $\mathrm{PA}$ also follows from the Schwichtenberg–Wainer theorem. Hájek and Pudlák ask for a simple proof of these relations in $\mathrm I\Sigma_1$ (Problem II.3.37).

## Exercises

::::exercise{#ex-alpha-large-compute difficulty=1 objective="Compute the functions $L_\alpha$ for small ordinals from the recursion and the composition rule."}
Compute $L_\omega(x)$, $L_{\omega \cdot 2}(x)$ and $L_{\omega^2}(1)$, and check the last value with :ref{#ex-fgh-values}.

:::solution
$L_\omega(x) = L_x(x + 1) = 2x + 1$. By the composition rule, $L_{\omega \cdot 2}(x) = L_\omega(L_\omega(x)) = 4x + 3$. $L_{\omega^2}(1) = L_{\omega \cdot 1}(2) = 5 = F_2(1)$.
:::
::::

## Notes and references

$\alpha$-large sets were introduced by Ketonen and Solovay (1981) in their combinatorial analysis of the Paris–Harrington principle. The presentation follows Hájek and Pudlák, Chapter II, Section 3: ordinals below $\varepsilon_0$ (3(a)), fundamental sequences (Theorem 3.12), $\alpha$-large sets (Definition 3.19, Remark 3.20, Theorem 3.21), and the hierarchy $f_\alpha$ with $f_\alpha(x)$ the least $y$ such that $[x, y)$ is $\omega^\alpha$-large (3.22 and Theorem 3.30). :ref{#lem-large-sum} is their Theorem II.3.21 (3), here with a proof by running the definition; :ref{#cor-omega-omega-large} is an instance of Corollary IV.3.8. The characterization of the provably total functions of $\mathrm{PA}$ is due to Schwichtenberg (1971) and Wainer (1970), first by proof theory.

Recent applications of $\alpha$-large sets to Ramsey's theorem for pairs are listed in the notes of :ref{to="independence/paris-harrington"}.

- J. Ketonen and R. Solovay, *Rapidly growing Ramsey functions*, Annals of Mathematics 113 (1981), 267–314.
- H. Schwichtenberg, *Eine Klassifikation der ε₀-rekursiven Funktionen*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 17 (1971), 61–74.
- S. S. Wainer, *A classification of the ordinal recursive functions*, Archiv für mathematische Logik und Grundlagenforschung 13 (1970), 136–153.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter II, Section 3, and Chapter IV, Section 3(d).

:::::exercises
::::exercise{#ex-alpha-large-omega-omega difficulty=2 objective="Unfold one step of the definition at $\omega^\omega$ and identify the resulting function with the diagonal of the hierarchy."}
Show that $[x, y)$ is $\omega^\omega$-large if and only if $[x + 1, y)$ is $\omega^x$-large, and deduce from :ref{#thm-large-fgh} that $L_{\omega^\omega}(x) = F_x(x + 1)$. Compute $L_{\omega^\omega}(1)$.

:::solution
$\{ \omega^\omega \}(x) = \omega^{\{ \omega \}(x)} = \omega^x$, so the run on $[x, y)$ continues from $\omega^x$ on $[x + 1, y)$. Hence $L_{\omega^\omega}(x) = L_{\omega^x}(x + 1) = F_x(x + 1)$. For $x = 1$: $F_1(2) = 5$.
:::
::::

::::exercise{#ex-alpha-large-omega-plus-n difficulty=1 objective="Apply the decomposition lemma to $(\omega + n)$-large sets, and check it against the definition on an example."}
Show that a finite set $A$ is $(\omega + n)$-large if and only if $|A| \geq n$ and $A$ without its $n$ least elements is relatively large. Compute $L_{\omega + n}(x)$, and check with the definition that $\{ 2, 3, 5, 6, 7 \}$ is $(\omega + 1)$-large.

:::solution
$\omega + n$ is in normal form, the last exponent of $\omega$ being $1 \geq 0$. For $n = 0$ the claim is :ref{#ex-alpha-large}, item 2. For $n \geq 1$, the shortest $n$-large initial segment of $A$, if any, consists of its $n$ least elements (item 1 of :ref{#ex-alpha-large}), and it exists if and only if $|A| \geq n$; :ref{#lem-large-sum} gives the claim, with item 2 of :ref{#ex-alpha-large}. By the composition rule, $L_{\omega + n}(x) = L_\omega(L_n(x)) = L_\omega(x + n) = 2x + 2n + 1$.

For $A = \{ 2, 3, 5, 6, 7 \}$: $\alpha_0 = \omega + 1$, $\alpha_1 = \{ \omega + 1 \}(2) = \omega$, $\alpha_2 = \{ \omega \}(3) = 3$, and the elements $5, 6, 7$ lower $3$ to $0$. So $\alpha_5 = 0$, and $A$ is $(\omega + 1)$-large; accordingly $\{ 3, 5, 6, 7 \}$ is relatively large.
:::
::::

::::exercise{#ex-alpha-large-ordinal-order difficulty=1 objective="See that $\alpha$-largeness is not monotone in the ordinal $\alpha$."}
Find a finite set that is $\omega$-large and not $3$-large, although $3 < \omega$. Show that every $\omega$-large set with least element at least $n$ is $n$-large.

:::solution
$\{ 1, 2 \}$ has $2 > 1$ elements, so it is $\omega$-large, and it is not $3$-large since it has fewer than $3$ elements (item 1 of :ref{#ex-alpha-large}). If $A$ is $\omega$-large and $\min A \geq n$, then $|A| > \min A \geq n$, so $A$ is $n$-large. The step $\{ \omega \}(a_0) = a_0$ depends on the least element, which is why a smaller ordinal can require more elements.
:::
::::

::::exercise{#ex-alpha-large-normal-form difficulty=1 objective="See why the decomposition lemma requires the sum to be in normal form, with a counterexample."}
Show that the conclusion of :ref{#lem-large-sum} fails for $\beta = 1$ and $\gamma = \omega$.

:::solution
Here $\beta + \gamma = 1 + \omega = \omega$, and the sum is not in normal form: the last exponent of $\beta = \omega^0$ is $0$, below the exponent $1$ of $\gamma$. Let $A = \{ 1, 2 \}$, which is $\omega$-large. Its shortest $\omega$-large initial segment is $A$ itself, since $\{ 1 \}$ is not relatively large, and $A \setminus A = \emptyset$ is not $1$-large. So $A$ is $(\beta + \gamma)$-large while the right side of the equivalence fails. In the proof, the step $\{ 1 + \gamma_i \}(x) = 1 + \{ \gamma_i \}(x)$ fails for $\gamma_0 = \omega$: the left side is $\{ \omega \}(x) = x$, the right side $1 + x$.
:::
::::

::::exercise{#ex-alpha-large-towers difficulty=1 objective="Compute least large intervals for ordinals beyond $\omega^\omega$ by unfolding fundamental sequences and applying the composition rule."}
Compute $L_{\omega_3}(1)$, where $\omega_3 = \omega^{\omega^\omega}$, and $L_{\omega^\omega \cdot 2}(1)$, the latter in terms of the functions $F_k$.

:::solution
$\{ \omega^{\omega^\omega} \}(1) = \omega^{\{ \omega^\omega \}(1)} = \omega^{\omega^1} = \omega^\omega$, so $L_{\omega_3}(1) = L_{\omega^\omega}(2) = F_2(3) = 39$, by :ref{#ex-alpha-large-omega-omega} and :ref{#ex-fgh-values}.

$\omega^\omega \cdot 2 = \omega^\omega + \omega^\omega$ is in normal form, so $L_{\omega^\omega \cdot 2}(1) = L_{\omega^\omega}(L_{\omega^\omega}(1)) = L_{\omega^\omega}(F_1(2)) = L_{\omega^\omega}(5) = F_5(6)$.
:::
::::
:::::
