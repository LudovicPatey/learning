---
title: α-large sets and fast-growing functions
summary: Ordinals below ε₀ in Cantor normal form and their fundamental sequences; α-large finite sets, which generalize relative largeness; the decomposition of (β + γ)-large sets; the least y such that [x, y) is ω^k-large is F_k(x), and ω^α-largeness defines the Schwichtenberg–Wainer hierarchy; IΣ₁ does not prove that every interval contains an ω^ω-large one; the theorems of Ketonen–Solovay and Schwichtenberg–Wainer are stated.
duration: 40
prerequisites: [ph-unprovable, computable-ordinals/ordinals]
---

Relative largeness, $|A| > \min A$, is one step of a scale of largeness notions indexed by ordinals, introduced by Ketonen and Solovay. A set is $\alpha$-large when one can descend from $\alpha$ to $0$ by reading its elements in increasing order, each element $a$ allowing one step $\beta \mapsto \beta[a]$ down a fundamental sequence. For finite $\alpha = n$, this means having $n$ elements; for $\alpha = \omega$ it is relative largeness. The scale measures the growth of the functions met in this course exactly: the least $y$ such that $[x, y)$ is $\omega^k$-large is $F_k(x)$, so lesson 1 was about $\omega^k$-large intervals, and the Paris–Harrington function of lesson 5 lives at the level $\varepsilon_0$.

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

For each standard $k$, by contrast, $\mathrm I\Sigma_1$ proves that every interval $[x, \infty)$ contains an $\omega^k$-large interval, by a formalization of :ref{#thm-large-fgh} (Hájek and Pudlák, Theorem II.3.32 and Fact II.3.34) and :ref{#lem-fgh-isigma1}. The scale of $\alpha$-largeness thus separates $\mathrm I\Sigma_1$ from its consequences at the level $\omega^\omega = \omega_2$.

## The theorems of Ketonen–Solovay and Schwichtenberg–Wainer

The same picture holds at every level of the hierarchy of fragments. We state the results and do not prove them.

:::theorem[Schwichtenberg; Wainer]{#thm-schwichtenberg-wainer}
A function is provably total in $\mathrm{PA}$ if and only if it is primitive recursive in $F_\alpha$ for some $\alpha < \varepsilon_0$; for $k \geq 1$, it is provably total in $\mathrm I\Sigma_k$ if and only if it is primitive recursive in $F_\alpha$ for some $\alpha < \omega_k$.
:::

Hájek and Pudlák prove this by indicators (Theorem IV.3.5 with Lemma IV.3.4): the functions $x \mapsto L_{\omega_n}(x)$, $n \in \nat$, form an envelope for $\mathrm{PA}$, with similar envelopes for $\mathrm I\Sigma_k$, the indicators being built from $\alpha$-largeness and "Paris sequences of the second kind" (Section IV.3(d)). For $k = 1$, $\omega_1 = \omega$, and the functions primitive recursive in some $F_n$ are the primitive recursive functions, in accordance with :ref{#thm-isigma1-envelope}; in terms of largeness, the ordinals $\omega^\alpha$ with $\alpha < \omega$ are those below $\omega^\omega = \omega_2$. Consequently $\mathrm{PA}$ does not prove that $F_{\varepsilon_0}$ is total, with $F_{\varepsilon_0}(x) = F_{\omega_x}(x + 1)$; equivalently, it does not prove that every interval $[x, \infty)$ contains an $\omega^{\varepsilon_0} = \varepsilon_0$-large interval.

Ketonen and Solovay (1981) related the two notions of largeness directly, by finite combinatorics. They showed that relatively large homogeneous sets for colorings of $(k+1)$-sets exist in every interval that is $\alpha$-large for an ordinal $\alpha$ of the order of $\omega_{k+c}$, with a small constant $c$ (Hájek and Pudlák quote the precise statement in the comment after Theorem II.3.36), and computed the growth of the corresponding Paris–Harrington functions, which is that of the hierarchy at the level $\omega_k$. As a consequence, the function $g$ of :ref{#cor-ph-envelope} grows at the level $\varepsilon_0$, and the unprovability of $\mathrm{PH}$ in $\mathrm{PA}$ also follows from the Schwichtenberg–Wainer theorem. Hájek and Pudlák ask for a simple proof of these relations in $\mathrm I\Sigma_1$ (Problem II.3.37).

## Exercises

::::exercise{difficulty=1}
Compute $L_\omega(x)$, $L_{\omega \cdot 2}(x)$ and $L_{\omega^2}(1)$, and check the last value with :ref{#ex-fgh-values}.

:::solution
$L_\omega(x) = L_x(x + 1) = 2x + 1$. By the composition rule, $L_{\omega \cdot 2}(x) = L_\omega(L_\omega(x)) = 4x + 3$. $L_{\omega^2}(1) = L_{\omega \cdot 1}(2) = 5 = F_2(1)$.
:::
::::

::::exercise{difficulty=2}
Show that $[x, y)$ is $\omega^\omega$-large if and only if $[x + 1, y)$ is $\omega^x$-large, and deduce from :ref{#thm-large-fgh} that $L_{\omega^\omega}(x) = F_x(x + 1)$. Compute $L_{\omega^\omega}(1)$.

:::solution
$\{ \omega^\omega \}(x) = \omega^{\{ \omega \}(x)} = \omega^x$, so the run on $[x, y)$ continues from $\omega^x$ on $[x + 1, y)$. Hence $L_{\omega^\omega}(x) = L_{\omega^x}(x + 1) = F_x(x + 1)$. For $x = 1$: $F_1(2) = 5$.
:::
::::

## Notes and references

$\alpha$-large sets were introduced by Ketonen and Solovay (1981) in their combinatorial analysis of the Paris–Harrington principle. The presentation follows Hájek and Pudlák, Chapter II, Section 3: ordinals below $\varepsilon_0$ (3(a)), fundamental sequences (Theorem 3.12), $\alpha$-large sets (Definition 3.19, Remark 3.20, Theorem 3.21), and the hierarchy $f_\alpha$ with $f_\alpha(x)$ the least $y$ such that $[x, y)$ is $\omega^\alpha$-large (3.22 and Theorem 3.30). :ref{#lem-large-sum} is their Theorem II.3.21 (3), here with a proof by running the definition; :ref{#cor-omega-omega-large} is an instance of Corollary IV.3.8. The characterization of the provably total functions of $\mathrm{PA}$ is due to Schwichtenberg (1971) and Wainer (1970), first by proof theory.

- J. Ketonen and R. Solovay, *Rapidly growing Ramsey functions*, Annals of Mathematics 113 (1981), 267–314.
- H. Schwichtenberg, *Eine Klassifikation der ε₀-rekursiven Funktionen*, Zeitschrift für mathematische Logik und Grundlagen der Mathematik 17 (1971), 61–74.
- S. S. Wainer, *A classification of the ordinal recursive functions*, Archiv für mathematische Logik und Grundlagenforschung 13 (1970), 136–153.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter II, Section 3, and Chapter IV, Section 3(d).
