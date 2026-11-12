---
title: The complexity function is not computable
summary: No algorithm certifies large complexity (the Berry paradox and Chaitin's incompleteness theorem); C is approximable from above and Turing equivalent to the halting problem; the lower envelope of C grows more slowly than every computable unbounded function.
duration: 40
prerequisites: [plain-complexity, turing-degrees/turing-reducibility]
---

The **Berry paradox** concerns "the least number that cannot be defined in fewer than twenty words": this phrase defines that number in fewer than twenty words. With "defined" replaced by "described by a program", the paradox becomes a theorem. If an algorithm could find, for each $n$, a string of complexity larger than $n$, then that string would have a description of about $\log n$ bits, namely $n$ together with the algorithm. So no algorithm finds strings of large complexity, and in particular the complexity function is not computable. This lesson proves this, with its logical form due to Chaitin, and then determines the exact computational strength of $C$: it is approximable from above and Turing equivalent to the halting problem. It ends with the lower envelope of $C$, which grows to infinity more slowly than any computable function.

## The Berry paradox

:::theorem{#thm-c-not-computable}
1. The function $C$ is not computable. More precisely, if $g : \bstr \to \nat$ is a partial computable function such that $g(\sigma) \leq C(\sigma)$ for every $\sigma$ in its domain, then $g$ is bounded.
2. The function $C$ is **approximable from above**: there is a computable function $(s, \sigma) \mapsto C_s(\sigma)$, non-increasing in $s$, with $\lim_s C_s(\sigma) = C(\sigma)$.
:::

:::proof{of=thm-c-not-computable}
1. Suppose that $g$ is unbounded on its domain. Let $f(n)$ be the first string $\sigma$ found, in an enumeration of the domain of $g$, with $g(\sigma) > n$. Then $f$ is total computable, and $C(f(n)) \geq g(f(n)) > n$. By :ref{#prop-c-basic}, $C(f(n)) \leq^+ C(n) \leq^+ \log n$. So $n < \log n + c$ for some constant $c$ and every $n \geq 1$, which fails for large $n$. If $C$ were computable, it would be such a function $g$, and it is unbounded by :ref{#prop-incompressible-count}.
2. Let $d$ be a constant with $C(\sigma) \leq |\sigma| + d$ for every $\sigma$. Let $C_s(\sigma)$ be the least length of a string $\tau$ with $|\tau| \leq |\sigma| + d$ and $U(\tau)[s]\converge = \sigma$, or $|\sigma| + d$ if there is none. It is computable, non-increasing in $s$, and equal to $C(\sigma)$ from the stage at which a shortest description converges.
:::

The asymmetry between the two statements comes from the existential form of short descriptions: "$C(\sigma) \leq k$" says that some string of length at most $k$ is a description of $\sigma$, a $\Sigma^0_1$ condition, which is confirmed as soon as a computation halts. Its negation "$C(\sigma) > k$" is $\Pi^0_1$, and statement 1 says that it cannot be confirmed by any algorithm, except for finitely many values of $k$.

:::quiz[non-computability of C]
In the proof of :ref{#thm-c-not-computable} (1), where is the hypothesis $g \leq C$ used?

- [x] To deduce $C(f(n)) > n$ from the choice of $f(n)$, which satisfies $g(f(n)) > n$.
- [ ] To show that $f$ is computable.

  $f$ is computable because $g$ is partial computable with unbounded values on its domain; the inequality is not needed for this.
- [ ] To show that $C(f(n)) \leq^+ \log n$.

  This bound comes from the computability of $f$, by :ref{#prop-c-basic}.

---

Why is $C$ approximable from above, and not from below?

- [x] Because the discovery of a new description can only decrease the current upper bound, while the absence of a short description is never confirmed at a finite stage.
- [ ] Because $C(\sigma) \leq |\sigma| + d$.

  This bound only provides a starting value for the approximation.
- [ ] Because $U$ is total.

  $U$ is partial, which is exactly why short descriptions may appear late.
:::

## Chaitin's incompleteness theorem

Statement 1 has a logical counterpart. The statements "$C(\sigma) > n$", for a string $\sigma$ and a number $n$, can be written in the language of arithmetic, through a formula expressing that no string of length at most $n$ is a $U$-description of $\sigma$. A formal theory can prove only finitely many values of these lower bounds, although almost all of them are true.

:::theorem[Chaitin]{#thm-chaitin-incompleteness}
Let $T$ be a theory with a c.e. set of theorems that proves only true statements of the form "$C(\sigma) > n$". There is a number $n_0$ such that $T$ proves no statement "$C(\sigma) > n$" with $n \geq n_0$. In particular, for all but finitely many $\sigma$, the true statement "$C(\sigma) > n_0$" is not provable in $T$.
:::

:::proof{of=thm-chaitin-incompleteness}
The set $S$ of pairs $(\sigma, n)$ such that $T$ proves "$C(\sigma) > n$" is c.e., by enumerating the theorems of $T$. Suppose that $S$ contains pairs with arbitrarily large second coordinate. The function $f(m)$, the first $\sigma$ found such that $(\sigma, n) \in S$ for some $n > m$, is then total computable, and $C(f(m)) > m$ since $T$ proves only true statements of this form. The argument of :ref{#thm-c-not-computable} (1) gives a contradiction. So the second coordinates of $S$ are bounded by some $n_0 - 1$. Only finitely many strings satisfy $C(\sigma) \leq n_0$, since they have descriptions of length at most $n_0$; so "$C(\sigma) > n_0$" is true for all other strings, and it is never provable.
:::

Unlike Gödel's sentence, the unprovable statements are not self-referential, and they are abundant: by :ref{#prop-incompressible-count}, most strings of each large length satisfy them. The number $n_0$ depends on $T$; Chaitin related it to the complexity of the axioms of $T$, a refinement not treated here.

## The Turing degree of C

The approximation from above makes $C$ computable in $\emptyset'$: $C(\sigma)$ is the value of $C_s(\sigma)$ at the first stage $s$ such that no description shorter than $C_s(\sigma)$ ever converges, and whether a given $s$ has this property is the negation of a c.e. condition, which $\emptyset'$ decides. Conversely, $C$ computes $\emptyset'$. The reduction cannot simply read off halting times from complexities, since a short description may converge late. The idea is to describe, from a halting time, a string that has no short description converging before that time: if this string has small complexity, as an oracle for $C$ reveals, then its short description must converge later, and the stage at which it does bounds the halting time. :ref{#ex-domain-complete} proves the analogous fact for the domain of $U$, and :ref{#ex-c-complete} for $C$, which yields:

:::proposition{#prop-c-degree}
$C \equiv_T \emptyset'$, where $C$ is used as an oracle through its graph.
:::

:::proof{of=prop-c-degree}
$C \leq_T \emptyset'$ by the argument above, and $\emptyset' \leq_T C$ by :ref{#ex-c-complete} below.
:::

## The lower envelope

For each $k$, only finitely many numbers $n$ satisfy $C(n) \leq k$, since they have descriptions of length at most $k$. So $C(n)$ tends to infinity. It does so more slowly than any computable function tending to infinity: the Berry argument applied to the numbers at which a computable function crosses a threshold shows that $C$ takes small values arbitrarily far.

:::theorem{#thm-c-envelope}
Let $\mu(n) = \min \{ C(m) : m \geq n \}$. Then $\mu$ is non-decreasing and unbounded. For every total computable non-decreasing unbounded function $\varphi$, $\mu(n) < \varphi(n)$ for all large enough $n$.
:::

:::proof{of=thm-c-envelope}
The function $\mu$ is non-decreasing by definition, and unbounded since $\{ m : C(m) \leq k \}$ is finite for each $k$.

Let $h(k)$ be the least $x$ with $\varphi(x) > k$; it is total computable, since $\varphi$ is unbounded, and it is non-decreasing and unbounded. By :ref{#prop-c-basic}, there is $c$ with $C(h(k)) \leq \log (k + 1) + c$ for every $k$. Let $n \geq h(0)$, and let $k$ be such that $h(k) \leq n < h(k+1)$. Then $\varphi(n) > k$, since $n \geq h(k)$ and $\varphi$ is non-decreasing, and $h(k+1) \geq n$, so $\mu(n) \leq C(h(k+1)) \leq \log(k + 2) + c$. As $n$ tends to infinity, so does $k$, and $\log(k + 2) + c < k < \varphi(n)$ for $k$ large.
:::

:::figure[Schematic values of $C(m)$ for small $m$ (the values depend on $U$ and are only illustrative). They stay close to $\log m$, with occasional low values at numbers with a short description, such as $16$, $32$ or $64$. The lower envelope $\mu$ is the staircase.]
<svg class="fig" viewBox="0 0 600 280" width="600" role="img" aria-label="Schematic values of C(m) as dots, close to log m, with occasional low values; the lower envelope mu(n), the minimum of C(m) over m at least n, is a slowly increasing staircase"><line x1="50" y1="230" x2="576" y2="230" class="axis"/><line x1="50" y1="230" x2="50" y2="32" class="axis"/><text x="582" y="234" class="math" font-size="14">m</text><text x="42" y="234" text-anchor="end" class="mrm muted" font-size="10">0</text><text x="42" y="190" text-anchor="end" class="mrm muted" font-size="10">2</text><text x="42" y="146" text-anchor="end" class="mrm muted" font-size="10">4</text><text x="42" y="102" text-anchor="end" class="mrm muted" font-size="10">6</text><text x="42" y="58" text-anchor="end" class="mrm muted" font-size="10">8</text><text x="58" y="246" text-anchor="middle" class="mrm muted" font-size="10">1</text><text x="178" y="246" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="306" y="246" text-anchor="middle" class="mrm muted" font-size="10">32</text><text x="434" y="246" text-anchor="middle" class="mrm muted" font-size="10">48</text><text x="562" y="246" text-anchor="middle" class="mrm muted" font-size="10">64</text><polyline points="58.0,230.0 66.0,208.0 74.0,195.1 82.0,186.0 90.0,178.9 98.0,173.1 106.0,168.2 114.0,164.0 122.0,160.3 130.0,156.9 138.0,153.9 146.0,151.1 154.0,148.6 162.0,146.2 170.0,144.0 178.0,142.0 186.0,140.1 194.0,138.3 202.0,136.5 210.0,134.9 218.0,133.4 226.0,131.9 234.0,130.5 242.0,129.1 250.0,127.8 258.0,126.6 266.0,125.4 274.0,124.2 282.0,123.1 290.0,122.0 298.0,121.0 306.0,120.0 314.0,119.0 322.0,118.1 330.0,117.2 338.0,116.3 346.0,115.4 354.0,114.5 362.0,113.7 370.0,112.9 378.0,112.1 386.0,111.4 394.0,110.6 402.0,109.9 410.0,109.2 418.0,108.5 426.0,107.8 434.0,107.1 442.0,106.5 450.0,105.8 458.0,105.2 466.0,104.6 474.0,104.0 482.0,103.4 490.0,102.8 498.0,102.2 506.0,101.7 514.0,101.1 522.0,100.6 530.0,100.0 538.0,99.5 546.0,99.0 554.0,98.5 562.0,98.0" class="muted-stroke" stroke-dasharray="4 3" stroke-width="1.1"/><text x="568" y="92.0" class="label">log m</text><path d="M58,208 L62.0,208 L62.0,208 L70.0,208 L70.0,208 L78.0,208 L78.0,186 L86.0,186 L86.0,186 L94.0,186 L94.0,186 L102.0,186 L102.0,186 L110.0,186 L110.0,186 L118.0,186 L118.0,186 L126.0,186 L126.0,186 L134.0,186 L134.0,186 L142.0,186 L142.0,186 L150.0,186 L150.0,186 L158.0,186 L158.0,186 L166.0,186 L166.0,186 L174.0,186 L174.0,186 L182.0,186 L182.0,164 L190.0,164 L190.0,164 L198.0,164 L198.0,164 L206.0,164 L206.0,164 L214.0,164 L214.0,164 L222.0,164 L222.0,164 L230.0,164 L230.0,164 L238.0,164 L238.0,164 L246.0,164 L246.0,164 L254.0,164 L254.0,164 L262.0,164 L262.0,164 L270.0,164 L270.0,164 L278.0,164 L278.0,164 L286.0,164 L286.0,164 L294.0,164 L294.0,164 L302.0,164 L302.0,164 L310.0,164 L310.0,142 L318.0,142 L318.0,142 L326.0,142 L326.0,142 L334.0,142 L334.0,142 L342.0,142 L342.0,142 L350.0,142 L350.0,142 L358.0,142 L358.0,142 L366.0,142 L366.0,142 L374.0,142 L374.0,142 L382.0,142 L382.0,142 L390.0,142 L390.0,142 L398.0,142 L398.0,142 L406.0,142 L406.0,142 L414.0,142 L414.0,142 L422.0,142 L422.0,142 L430.0,142 L430.0,142 L438.0,142 L438.0,142 L446.0,142 L446.0,142 L454.0,142 L454.0,142 L462.0,142 L462.0,142 L470.0,142 L470.0,142 L478.0,142 L478.0,142 L486.0,142 L486.0,142 L494.0,142 L494.0,142 L502.0,142 L502.0,142 L510.0,142 L510.0,142 L518.0,142 L518.0,142 L526.0,142 L526.0,142 L534.0,142 L534.0,142 L542.0,142 L542.0,142 L550.0,142 L550.0,142 L558.0,142 L558.0,142 L570,142" class="accent-stroke" stroke-width="1.8"/><circle cx="58" cy="208" r="2.6" class="ink-fill"/><circle cx="66" cy="164" r="2.6" class="ink-fill"/><circle cx="74" cy="208" r="2.6" class="ink-fill"/><circle cx="82" cy="164" r="2.6" class="ink-fill"/><circle cx="90" cy="186" r="2.6" class="ink-fill"/><circle cx="98" cy="164" r="2.6" class="ink-fill"/><circle cx="106" cy="142" r="2.6" class="ink-fill"/><circle cx="114" cy="164" r="2.6" class="ink-fill"/><circle cx="122" cy="142" r="2.6" class="ink-fill"/><circle cx="130" cy="164" r="2.6" class="ink-fill"/><circle cx="138" cy="142" r="2.6" class="ink-fill"/><circle cx="146" cy="120" r="2.6" class="ink-fill"/><circle cx="154" cy="164" r="2.6" class="ink-fill"/><circle cx="162" cy="142" r="2.6" class="ink-fill"/><circle cx="170" cy="164" r="2.6" class="ink-fill"/><circle cx="178" cy="186" r="2.6" class="ink-fill"/><circle cx="186" cy="98" r="2.6" class="ink-fill"/><circle cx="194" cy="142" r="2.6" class="ink-fill"/><circle cx="202" cy="120" r="2.6" class="ink-fill"/><circle cx="210" cy="142" r="2.6" class="ink-fill"/><circle cx="218" cy="120" r="2.6" class="ink-fill"/><circle cx="226" cy="98" r="2.6" class="ink-fill"/><circle cx="234" cy="142" r="2.6" class="ink-fill"/><circle cx="242" cy="164" r="2.6" class="ink-fill"/><circle cx="250" cy="142" r="2.6" class="ink-fill"/><circle cx="258" cy="120" r="2.6" class="ink-fill"/><circle cx="266" cy="98" r="2.6" class="ink-fill"/><circle cx="274" cy="142" r="2.6" class="ink-fill"/><circle cx="282" cy="120" r="2.6" class="ink-fill"/><circle cx="290" cy="142" r="2.6" class="ink-fill"/><circle cx="298" cy="120" r="2.6" class="ink-fill"/><circle cx="306" cy="164" r="2.6" class="ink-fill"/><circle cx="314" cy="120" r="2.6" class="ink-fill"/><circle cx="322" cy="98" r="2.6" class="ink-fill"/><circle cx="330" cy="120" r="2.6" class="ink-fill"/><circle cx="338" cy="98" r="2.6" class="ink-fill"/><circle cx="346" cy="76" r="2.6" class="ink-fill"/><circle cx="354" cy="120" r="2.6" class="ink-fill"/><circle cx="362" cy="98" r="2.6" class="ink-fill"/><circle cx="370" cy="142" r="2.6" class="ink-fill"/><circle cx="378" cy="98" r="2.6" class="ink-fill"/><circle cx="386" cy="76" r="2.6" class="ink-fill"/><circle cx="394" cy="120" r="2.6" class="ink-fill"/><circle cx="402" cy="98" r="2.6" class="ink-fill"/><circle cx="410" cy="120" r="2.6" class="ink-fill"/><circle cx="418" cy="98" r="2.6" class="ink-fill"/><circle cx="426" cy="76" r="2.6" class="ink-fill"/><circle cx="434" cy="142" r="2.6" class="ink-fill"/><circle cx="442" cy="98" r="2.6" class="ink-fill"/><circle cx="450" cy="120" r="2.6" class="ink-fill"/><circle cx="458" cy="98" r="2.6" class="ink-fill"/><circle cx="466" cy="76" r="2.6" class="ink-fill"/><circle cx="474" cy="120" r="2.6" class="ink-fill"/><circle cx="482" cy="98" r="2.6" class="ink-fill"/><circle cx="490" cy="120" r="2.6" class="ink-fill"/><circle cx="498" cy="142" r="2.6" class="ink-fill"/><circle cx="506" cy="76" r="2.6" class="ink-fill"/><circle cx="514" cy="120" r="2.6" class="ink-fill"/><circle cx="522" cy="98" r="2.6" class="ink-fill"/><circle cx="530" cy="120" r="2.6" class="ink-fill"/><circle cx="538" cy="98" r="2.6" class="ink-fill"/><circle cx="546" cy="76" r="2.6" class="ink-fill"/><circle cx="554" cy="120" r="2.6" class="ink-fill"/><circle cx="562" cy="142" r="2.6" class="ink-fill"/><circle cx="70" cy="266" r="2.6" class="ink-fill"/><text x="80" y="270" class="label">C(m), schematic values</text><line x1="260" y1="266" x2="282" y2="266" class="accent-stroke" stroke-width="1.8"/><text x="288" y="270" class="label">μ(n) = min of C(m) over m ≥ n</text></svg>
:::

For instance, $C(n)$ is small for infinitely many $n$ in a range where $\log n$ is large: $C(2^{2^j}) \leq^+ C(j) \leq^+ \log j$ for $j \geq 1$. The function $\mu$ is a typical example of a function that tends to infinity, but slower than every computable function tending to infinity; it is computable in $\emptyset'$, since $\mu(n) < v$ holds if and only if some string of length less than $v$ is a $U$-description of a number $m \geq n$, a c.e. condition.

:::quiz[the lower envelope]
In the proof of :ref{#thm-c-envelope}, why does the number $h(k+1)$ have small complexity?

- [x] Because it is computed from $k + 1$ by a fixed algorithm, so its complexity is at most that of $k + 1$ up to a constant, which is at most about $\log k$.
- [ ] Because $h(k + 1)$ is small.

  It may be very large; its complexity is small because it has a short description.
- [ ] Because $\varphi$ is non-decreasing.

  Monotonicity is used to locate $n$ between $h(k)$ and $h(k+1)$, not to bound the complexity.
:::

## Exercises

::::exercise{difficulty=1 #ex-domain-complete}
Let $X$ be the set of strings $\sigma$ such that $U(\sigma)$ converges. Show that $\emptyset' \leq_T X$.

:::solution
Let $M$ be the machine with $M(0^e) = 0^s$, where $s$ is the least stage with $\Phi_e(e)[s]\converge$, and $M$ undefined elsewhere. Let $d$ be such that $C \leq C_M + d$. If $\Phi_e(e)$ converges at stage $s$, then $C(0^s) \leq e + d$. With oracle $X$, list the strings $\tau$ of length at most $e + d$ such that $U(\tau)$ converges, compute their outputs, and let $t$ be the largest number such that $0^t$ is one of them ($t = 0$ if there is none). Then $\Phi_e(e)$ converges if and only if $\Phi_e(e)[t]\converge$.
:::
::::

::::exercise{difficulty=2 #ex-c-complete}
Show that $\emptyset' \leq_T C$, where $C$ is used as an oracle through its graph.

:::hint
Adapt the previous solution: when $\Phi_e(e)$ converges at stage $s$, describe with about $e$ bits a string of length $2e$ that has no short description converging by stage $s$.
:::

:::solution
Let $M$ be the machine defined on the strings $0^e$ as follows: search for the least $s$ with $\Phi_e(e)[s]\converge$, and output the first string $\sigma$ of length $2e$, in the lexicographic order, such that $U(\tau)[s] \converge = \sigma$ for no $\tau$ of length less than $2e$. Such a string exists, since fewer than $2^{2e}$ strings are outputs of strings of length less than $2e$. Let $d$ be such that $C \leq C_M + d$, and let $e > d$.

With oracle $C$, compute the finite set $S$ of strings $\sigma$ of length $2e$ with $C(\sigma) < 2e$, and then a stage $t$ such that every $\sigma \in S$ satisfies $U(\tau)[t]\converge = \sigma$ for some $\tau$ of length less than $2e$; the search for $t$ terminates, since every element of $S$ has such a description. If $\Phi_e(e)$ converges at stage $s$, the string $\sigma = M(0^e)$ satisfies $C(\sigma) \leq e + d < 2e$, so $\sigma \in S$, and no description of $\sigma$ of length less than $2e$ converges by stage $s$; hence $s < t$. So $\Phi_e(e)\converge$ if and only if $\Phi_e(e)[t]\converge$. The finitely many $e \leq d$ are handled by a finite table.
:::
::::

::::exercise{difficulty=1}
Fix $c$. Show that the set $R_c = \{ \sigma : C(\sigma) \geq |\sigma| - c \}$ of $c$-incompressible strings is **immune**: it is infinite and has no infinite c.e. subset. Deduce that the set of strings $\sigma$ with $C(\sigma) < |\sigma| - c$ is **simple**: c.e., with an infinite complement that has no infinite c.e. subset.

:::solution
$R_c$ contains a string of each length by :ref{#prop-incompressible-count}, so it is infinite. If $W \subseteq R_c$ were an infinite c.e. set, the partial computable function $g(\sigma) = \max(|\sigma| - c, 0)$ with domain $W$ would satisfy $g \leq C$ on its domain, and it would be unbounded, since $W$ contains strings of arbitrary length. This contradicts :ref{#thm-c-not-computable}. The complement of $R_c$ is c.e., since $C(\sigma) < |\sigma| - c$ holds if and only if $C_s(\sigma) < |\sigma| - c$ for some $s$; its complement $R_c$ is infinite and immune.
:::
::::

::::exercise{difficulty=2}
Show that no total computable function $f : \bstr \to \nat$ satisfies $f =^+ C$, that is, $|f(\sigma) - C(\sigma)| \leq b$ for a constant $b$ and every $\sigma$.

:::solution
If $|f(\sigma) - C(\sigma)| \leq b$ for every $\sigma$, then $g = \max(f - b, 0)$ is total computable with $g \leq C$ and $g \geq C - 2b$, which is unbounded since $C$ is. This contradicts :ref{#thm-c-not-computable} (1).
:::
::::

## Notes and references

The use of the Berry paradox to prove the non-computability of complexity goes back to the founders of the theory; Chaitin's incompleteness theorem is from his 1974 paper. Monin and Patey credit the Turing completeness of $C$ (:ref{#ex-c-complete}) to Gács, after Li and Vitányi. Kummer (1996) proved that the set of compressible strings $\{ \sigma : C(\sigma) < |\sigma| \}$ is truth-table complete, a stronger form of :ref{#ex-c-complete}; Nies (Proposition 2.1.28) proves that it is weak truth-table complete and simple, and Downey and Hirschfeldt (Section 16.3) present Kummer's theorem. The lower envelope is treated in Zvonkin and Levin's survey and in Nies, Proposition 2.1.22.

- G. J. Chaitin, *Information-theoretic limitations of formal systems*, Journal of the ACM 21 (1974), 403–424.
- M. Kummer, *On the complexity of random strings*, STACS 96, Lecture Notes in Computer Science 1046, Springer, 1996, 25–36.
- A. K. Zvonkin and L. A. Levin, *The complexity of finite objects and the development of the concepts of information and randomness by means of the theory of algorithms*, Russian Mathematical Surveys 25 (1970), 83–124.
- A. Nies, *Computability and Randomness*, Oxford University Press, 2009, Section 2.1.
- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity*, Springer, 2010, Sections 3.1 and 16.3.
- B. Monin and L. Patey, *Computability theory*, chapter "Kolmogorov complexity and random numbers".
