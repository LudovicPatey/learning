---
title: Weak preservation
summary: To build low sets, a forcing question needs only to be decided by ∅′, not to be Σ⁰₁; every Σ⁰₂ set whose complement is hyperimmune has an infinite low subset (Jockusch); both hypotheses are needed.
duration: 40
prerequisites: [forcing-the-jump, immunity-growth/immune-sets, avoidance/forcing-question-method]
---

In cone avoidance, the forcing question must be $\Sigma^0_1$-preserving (:ref{#thm-question-preservation}), or at least $\Sigma^0_1$ relative to a member of a class of weak sets (:ref{#thm-local-cone-avoidance}): the argument compares the set of answers with the graph of the set $C$ to avoid, and needs the set of answers to be c.e. For lowness, the requirement is different. By :ref{#thm-jump-control}, it suffices that $\emptyset'$ decide the question and find the extensions. A relation decided by $\emptyset'$ is $\Delta^0_2$, and need not be $\Sigma^0_1$. Lowness can therefore be obtained with a question that is not $\Sigma^0_1$, a situation that Patey's monograph calls **weak preservation**.

For a combinatorial notion of forcing, a question that is $\Delta^0_2$ without being $\Sigma^0_1$ is unusual: a question built from the combinatorics of the problem is typically $\Sigma^0_1$, or else more complex than $\Delta^0_2$. The example of this lesson, and its application to linear orders in the next lesson, exploit a computability-theoretic hypothesis, the hyperimmunity of a set, to decide between two $\Sigma^0_2$ alternatives, one of which is always true.

## Low subsets of co-hyperimmune sets

When does a set $A$ have an infinite low subset? Being infinite is not enough, nor being $\Delta^0_2$.

:::example{#ex-no-low-subset}
Code strings by numbers, so that the set $F_n$ of codes of the strings of length $n$ has a canonical index computable from $n$. Let $A$ be the set of codes of the prefixes of $\emptyset'$. It is infinite and $\Delta^0_2$. Every infinite subset $H$ of $A$ computes $\emptyset'$: to find $\emptyset'(x)$, search $H$ for the code of a string of length larger than $x$, and read its bit $x$. So $A$ has no infinite low subset. Its complement meets every $F_n$ with $n \geq 1$, since only one string of length $n$ is a prefix of $\emptyset'$; the sets $F_n$ form a disjoint strong array, so $\overline A$ is not hyperimmune (:ref{#def-hyperimmune-set}).
:::

If $\overline A$ is hyperimmune, the elements of $\overline A$ cannot be located by a computable array: $\overline A$ is sparse, and $A$ is large in a strong sense. The following theorem shows that this largeness, together with a bound on the complexity of $A$, gives low subsets.

:::theorem[Jockusch]{#thm-cohyperimmune-low}
Let $A$ be a $\Sigma^0_2$ set whose complement is hyperimmune. Then $A$ has an infinite low subset.
:::

The set $A$ is infinite: otherwise $\overline A$ would be cofinite, and a cofinite set contains an infinite computable set, so it is not even immune. We use a variant of Cohen forcing. The **conditions** are the strings $\sigma$ whose set of elements $\{ n < |\sigma| : \sigma(n) = 1 \}$ is contained in $A$; we write $\sigma \subseteq A$. A condition $\tau$ extends $\sigma$ if $\sigma \preceq \tau$, and the **members** of $\sigma$ are the sets $Z \subseteq A$ with $\sigma \prec Z$. This class is closed and non-empty, it contains $\sigma 0^\infty$, and refinement holds: if some $Z \subseteq A$ extends $\sigma$ and a string $\rho$, the longer of $\sigma$ and $\rho$ is a condition. The members are subsets of $A$, so the generic set will be a subset of $A$. The difficulty is that $\emptyset'$ need not be able to decide whether $\sigma$ has an extension $\tau \subseteq A$ with $\Phi^\tau_e(e)\converge$: this is a $\Sigma^0_2$ question, since membership in $A$ is $\Sigma^0_2$. The following lemma replaces this question by a choice between two $\Sigma^0_2$ statements, one of which is true.

:::lemma{#lem-cohyperimmune-dichotomy}
Under the hypotheses of :ref{#thm-cohyperimmune-low}, for every condition $\sigma$ and every $e$, at least one of the following holds:
1. there is a condition $\tau \succeq \sigma$ with $\Phi^\tau_e(e)\converge$;
2. there is $n$ such that $\Phi^\mu_e(e)\diverge$ for every string $\mu \succeq \sigma 0^n$.

Both statements are $\Sigma^0_2$, uniformly in $\sigma$ and $e$.
:::

:::proof{of=lem-cohyperimmune-dichotomy}
Statement 1 says that there are $\tau \succeq \sigma$ and $s$ with $\Phi^\tau_e(e)[s]\converge$ and every element of $\tau$ in $A$; the last condition is a finite conjunction of $\Sigma^0_2$ conditions, so statement 1 is $\Sigma^0_2$. Statement 2 is the projection of a $\Pi^0_1$ relation.

Suppose that statement 2 fails. Then for every $n$ there is a string $\mu \succeq \sigma 0^n$ with $\Phi^\mu_e(e)\converge$, and a search finds one, $\mu_n$, computably in $n$. Let $F_n$ be the set of elements of $\mu_n$ that are at least $|\sigma| + n$, a finite set whose canonical index is computable from $n$. The string $\mu_n$ extends $\sigma$ and makes the computation converge; if statement 1 also failed, $\mu_n$ would not be a condition, so some element of $\mu_n$ would lie outside $A$. The elements of $\mu_n$ below $|\sigma|$ are those of $\sigma$, which lie in $A$, and those between $|\sigma|$ and $|\sigma| + n$ are absent. So $F_n$ meets $\overline A$, for every $n$.

The sets $F_n$ need not be disjoint, but a computable subsequence is: let $n_0 = 0$ and $n_{k+1} = |\mu_{n_k}|$. Every element of $F_{n_{k+1}}$ is at least $|\sigma| + n_{k+1} \geq |\mu_{n_k}|$, hence larger than every element of $F_{n_k}$, and, by induction, of the earlier blocks. So $(F_{n_k})_{k \in \nat}$ is a disjoint strong array, each of whose members meets $\overline A$, contradicting the hyperimmunity of $\overline A$. Hence statement 1 or statement 2 holds.
:::

:::figure[The proof of :ref{#lem-cohyperimmune-dichotomy}. If statement 2 fails, for every $n$ some string $\mu_n \succeq \sigma 0^n$ makes the computation converge. If statement 1 fails too, $\mu_n$ is not a condition, so the block $F_n$ of elements it adds after the zeros meets the complement of $A$. Choosing each $n$ beyond the previous string makes the blocks disjoint, which contradicts hyperimmunity.]
<svg class="fig" viewBox="0 0 600 236" width="600" role="img" aria-label="Three strings extending sigma followed by blocks of zeros of increasing length; each makes the computation converge, and the positions where it adds elements form a finite set that meets the complement of A; the blocks are pairwise disjoint"><text x="46.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">0</text><text x="100.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">4</text><text x="154.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">8</text><text x="208.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">12</text><text x="262.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">16</text><text x="316.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">20</text><text x="370.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">24</text><text x="424.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">28</text><text x="478.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">32</text><text x="532.8" y="18" text-anchor="middle" class="mrm muted" font-size="10">36</text><text x="32" y="50" text-anchor="end" class="math" font-size="14">μ<tspan class="mrm" font-size="10" dy="4">0</tspan></text><rect x="40.0" y="36" width="13.5" height="20" class="cell head-cell"/><rect x="53.5" y="36" width="13.5" height="20" class="cell head-cell"/><rect x="67.0" y="36" width="13.5" height="20" class="cell head-cell"/><rect x="80.5" y="36" width="13.5" height="20" class="cell head-cell"/><rect x="94.0" y="36" width="13.5" height="20" class="cell"/><rect x="107.5" y="36" width="13.5" height="20" class="cell"/><rect x="121.0" y="36" width="13.5" height="20" class="cell"/><circle cx="127.8" cy="46" r="4" class="ink-fill"/><rect x="134.5" y="36" width="13.5" height="20" class="cell"/><rect x="148.0" y="36" width="13.5" height="20" class="cell"/><circle cx="154.8" cy="46" r="4" class="accent-fill"/><text x="169.5" y="50" class="label">Φₑ converges</text><text x="32" y="96" text-anchor="end" class="math" font-size="14">μ<tspan class="mrm" font-size="10" dy="4">1</tspan></text><rect x="40.0" y="82" width="13.5" height="20" class="cell head-cell"/><rect x="53.5" y="82" width="13.5" height="20" class="cell head-cell"/><rect x="67.0" y="82" width="13.5" height="20" class="cell head-cell"/><rect x="80.5" y="82" width="13.5" height="20" class="cell head-cell"/><rect x="94.0" y="82" width="13.5" height="20" class="cell"/><rect x="107.5" y="82" width="13.5" height="20" class="cell"/><rect x="121.0" y="82" width="13.5" height="20" class="cell"/><rect x="134.5" y="82" width="13.5" height="20" class="cell"/><rect x="148.0" y="82" width="13.5" height="20" class="cell"/><rect x="161.5" y="82" width="13.5" height="20" class="cell"/><rect x="175.0" y="82" width="13.5" height="20" class="cell"/><rect x="188.5" y="82" width="13.5" height="20" class="cell"/><rect x="202.0" y="82" width="13.5" height="20" class="cell"/><rect x="215.5" y="82" width="13.5" height="20" class="cell"/><rect x="229.0" y="82" width="13.5" height="20" class="cell"/><circle cx="235.8" cy="92" r="4" class="accent-fill"/><rect x="242.5" y="82" width="13.5" height="20" class="cell"/><rect x="256.0" y="82" width="13.5" height="20" class="cell"/><rect x="269.5" y="82" width="13.5" height="20" class="cell"/><circle cx="276.2" cy="92" r="4" class="ink-fill"/><rect x="283.0" y="82" width="13.5" height="20" class="cell"/><path d="M94.0,108 L94.0,112 L215.5,112 L215.5,108" class="muted-stroke" stroke-width="1"/><text x="154.8" y="123" text-anchor="middle" class="label muted">0 repeated 9 times</text><text x="304.5" y="96" class="label">Φₑ converges</text><text x="32" y="142" text-anchor="end" class="math" font-size="14">μ<tspan class="mrm" font-size="10" dy="4">2</tspan></text><rect x="40.0" y="128" width="13.5" height="20" class="cell head-cell"/><rect x="53.5" y="128" width="13.5" height="20" class="cell head-cell"/><rect x="67.0" y="128" width="13.5" height="20" class="cell head-cell"/><rect x="80.5" y="128" width="13.5" height="20" class="cell head-cell"/><rect x="94.0" y="128" width="13.5" height="20" class="cell"/><rect x="107.5" y="128" width="13.5" height="20" class="cell"/><rect x="121.0" y="128" width="13.5" height="20" class="cell"/><rect x="134.5" y="128" width="13.5" height="20" class="cell"/><rect x="148.0" y="128" width="13.5" height="20" class="cell"/><rect x="161.5" y="128" width="13.5" height="20" class="cell"/><rect x="175.0" y="128" width="13.5" height="20" class="cell"/><rect x="188.5" y="128" width="13.5" height="20" class="cell"/><rect x="202.0" y="128" width="13.5" height="20" class="cell"/><rect x="215.5" y="128" width="13.5" height="20" class="cell"/><rect x="229.0" y="128" width="13.5" height="20" class="cell"/><rect x="242.5" y="128" width="13.5" height="20" class="cell"/><rect x="256.0" y="128" width="13.5" height="20" class="cell"/><rect x="269.5" y="128" width="13.5" height="20" class="cell"/><rect x="283.0" y="128" width="13.5" height="20" class="cell"/><rect x="296.5" y="128" width="13.5" height="20" class="cell"/><rect x="310.0" y="128" width="13.5" height="20" class="cell"/><rect x="323.5" y="128" width="13.5" height="20" class="cell"/><rect x="337.0" y="128" width="13.5" height="20" class="cell"/><rect x="350.5" y="128" width="13.5" height="20" class="cell"/><rect x="364.0" y="128" width="13.5" height="20" class="cell"/><rect x="377.5" y="128" width="13.5" height="20" class="cell"/><circle cx="384.2" cy="138" r="4" class="ink-fill"/><rect x="391.0" y="128" width="13.5" height="20" class="cell"/><rect x="404.5" y="128" width="13.5" height="20" class="cell"/><rect x="418.0" y="128" width="13.5" height="20" class="cell"/><rect x="431.5" y="128" width="13.5" height="20" class="cell"/><circle cx="438.2" cy="138" r="4" class="accent-fill"/><rect x="445.0" y="128" width="13.5" height="20" class="cell"/><rect x="458.5" y="128" width="13.5" height="20" class="cell"/><circle cx="465.2" cy="138" r="4" class="ink-fill"/><path d="M94.0,154 L94.0,158 L350.5,158 L350.5,154" class="muted-stroke" stroke-width="1"/><text x="222.2" y="169" text-anchor="middle" class="label muted">0 repeated 19 times</text><text x="480.0" y="142" class="label">Φₑ converges</text><rect x="40" y="180" width="13.5" height="14" class="cell head-cell"/><text x="59.5" y="191" class="label">σ</text><circle cx="100" cy="187" r="4" class="ink-fill"/><text x="110" y="191" class="label">element added, in A</text><circle cx="280" cy="187" r="4" class="accent-fill"/><text x="290" y="191" class="label">element added, not in A</text><text x="300" y="222" text-anchor="middle" class="label">each block F_k of added elements meets the complement of A, and the blocks are disjoint</text></svg>
:::

:::proof{of=thm-cohyperimmune-low}
We apply :ref{#thm-jump-control} with $A$ replaced by the oracle $\emptyset'$; conditions are coded by numbers, like strings. A $\Sigma^0_2$ statement is $\Sigma^0_1(\emptyset')$ by Post's theorem (:ref{#thm-post}), so $\emptyset'$ can enumerate the witnesses of each of the two statements of :ref{#lem-cohyperimmune-dichotomy}, uniformly in $\sigma$ and $e$. Given $\sigma$ and $e$, run both enumerations until a witness appears, which happens by the lemma.

- If a witness of statement 1 appears first, it provides a condition $\tau \succeq \sigma$ with $\Phi^\tau_e(e)\converge$. Return $(\tau, 1)$: every member of $\tau$ extends $\tau$, hence makes the computation converge.
- If a witness of statement 2 appears first, it provides $n$. The string $\sigma 0^n$ is a condition, since it adds no element. Return $(\sigma 0^n, 0)$: every member extends $\sigma 0^n$, hence makes the computation diverge.

So the notion of forcing decides the jump $\emptyset'$-effectively. The sets $S_n$ are computably dense, by extension with zeros. For each $k$, the set of conditions with at least $k$ elements is uniformly $\emptyset'$-effectively dense: $A$ is $\Sigma^0_1(\emptyset')$, so $\emptyset'$ enumerates $A$ until it finds an element $x \geq |\sigma|$, which exists since $A$ is infinite, and returns $\sigma 0^{x - |\sigma|} 1$. By :ref{#thm-jump-control}, there is a set $G$, member of all the conditions of a filter meeting all these sets, with $G' \leq_T \emptyset'$. It is infinite, and contained in $A$ since it is a member of the conditions.
:::

The relation "$\sigma \mathrel{?{\vdash}} \Phi^G_e(e)\converge$ if a witness of statement 1 appears first" is a forcing question at level $1$: a positive answer gives an extension forcing the convergence, a negative answer one forcing the divergence. It is decided by $\emptyset'$, but it depends on the order of the enumerations, and it is not $\Sigma^0_1$ in any natural way. The hyperimmunity of $\overline A$ is what makes the two $\Sigma^0_2$ alternatives exhaustive; nothing in the combinatorics of subsets of $A$ would give it.

:::quiz[low subsets of co-hyperimmune sets]
In the proof of :ref{#lem-cohyperimmune-dichotomy}, why are the strings $\mu_n$ required to extend $\sigma 0^n$ rather than only $\sigma$?

- [x] So that the elements they add lie above $|\sigma| + n$; letting $n$ grow pushes the blocks $F_n$ to infinity, which is what allows a disjoint subsequence.
- [ ] So that the strings $\mu_n$ are conditions.

  They are not conditions, under the assumption that statement 1 fails.
- [ ] So that the computation $\Phi^{\mu_n}_e(e)$ converges.

  Convergence comes from the failure of statement 2.

---

Where is it used that $A$ is $\Sigma^0_2$?

- [x] To make statement 1 a $\Sigma^0_2$ statement, so that $\emptyset'$ can search for its witnesses, and to let $\emptyset'$ enumerate elements of $A$ for infinity.
- [ ] To make the complement of $A$ hyperimmune.

  Hyperimmunity is a separate hypothesis.
- [ ] To show that statement 1 or statement 2 holds.

  The dichotomy uses only the hyperimmunity of $\overline A$.
:::

Both hypotheses are needed. :ref{#ex-no-low-subset} gives a $\Delta^0_2$ set with no infinite low subset, whose complement is not hyperimmune. The first exercise gives a set with hyperimmune complement and no infinite $\Delta^0_2$ subset; it is not $\Sigma^0_2$.

The next lesson, :ref{to="lowness/stable-linear-orders"}, applies the theorem to linear orders.

## Exercises

::::exercise{difficulty=2}
Let $G$ be sufficiently generic for Cohen forcing. Show that $\overline G$ is hyperimmune and that $G$ has no infinite $\Delta^0_2$ subset. Which hypothesis of :ref{#thm-cohyperimmune-low} fails?

:::solution
Let $(F_n)$ be a disjoint strong array. If some $F_n$ is empty, it does not meet $\overline G$. Otherwise, given a string $\sigma$, choose $n$ with $\min F_n \geq |\sigma|$, which exists since the sets are disjoint and non-empty, and extend $\sigma$ by ones on $F_n$ and zeros elsewhere up to $\max F_n$. Every $G$ extending the new string contains $F_n$. So the set of strings forcing $F_n \cap \overline G = \emptyset$ for some $n$ is dense. Similarly, for an infinite $\Delta^0_2$ set $H$, extend $\sigma$ by zeros up to an element of $H$ larger than $|\sigma|$, included: every $G$ extending it misses an element of $H$. Finally, extending by zeros, or by ones, shows that $\overline G$ and $G$ are infinite. There are countably many arrays and $\Delta^0_2$ sets, so a sufficiently generic $G$ meets all these dense sets. The set $G$ is not $\Sigma^0_2$: an infinite $\Sigma^0_2$ set has an infinite $\Delta^0_2$ subset, obtained as in :ref{#def-immune} by enumerating it with $\emptyset'$ and keeping increasing elements.
:::
::::

::::exercise{difficulty=2}
Let $A$ be a $\Sigma^0_2$ set whose complement is hyperimmune. Show that $A$ has an infinite low subset $G$ that is not computable, and, if $A$ is immune, explain why every infinite low subset of $A$ is non-computable.

:::solution
Add to the proof of :ref{#thm-cohyperimmune-low} the sets $E_e$ of conditions $\tau$ such that no member of $\tau$ is equal to $\Phi_e$. They are uniformly $\emptyset'$-effectively dense. Given $\sigma$, the oracle $\emptyset'$ enumerates $A$ until it finds an element $x \geq |\sigma|$, and decides whether $\Phi_e(x)\converge$. If not, $\Phi_e$ is not the characteristic function of a set, and $\sigma \in E_e$. If $\Phi_e(x)\converge = 0$, take $\sigma 0^{x - |\sigma|} 1$, a condition since $x \in A$, all of whose members contain $x$. Otherwise take $\sigma 0^{x - |\sigma| + 1}$, all of whose members omit $x$. In each case no member equals $\Phi_e$, so the resulting low set $G \subseteq A$ is not computable. If $A$ is immune, it has no infinite computable subset, so every infinite subset of $A$ is non-computable.
:::
::::

::::exercise{difficulty=1}
Let $A$ be a $\Delta^0_2$ set such that both $A$ and $\overline A$ are infinite. Show that if $A$ is hyperimmune or $\overline A$ is hyperimmune, then $A$ or $\overline A$ has an infinite low subset. Deduce that a $\Delta^0_2$ set with no infinite low subset in itself or its complement, as in the theorem of Downey, Hirschfeldt, Lempp and Solomon, is neither hyperimmune nor co-hyperimmune.

:::solution
If $\overline A$ is hyperimmune, apply :ref{#thm-cohyperimmune-low} to $A$, which is $\Sigma^0_2$. If $A$ is hyperimmune, apply it to $\overline A$, which is $\Sigma^0_2$ with hyperimmune complement $A$. The second statement is the contrapositive.
:::
::::

## Notes and references

:ref{#thm-cohyperimmune-low} is due to Jockusch, and is credited to him by Hirschfeldt, Jockusch, Kjos-Hanssen, Lempp and Slaman (2008); the proof follows the section *Weak preservation* of the chapter *Lowness* of Patey's monograph, from which the term is taken. Hyperimmune sets and disjoint strong arrays are studied in :ref{to="immunity-growth/immune-sets"}.

- D. R. Hirschfeldt, C. G. Jockusch, Jr., B. Kjos-Hanssen, S. Lempp and T. A. Slaman, *The strength of some combinatorial principles related to Ramsey's theorem for pairs*, in *Computational Prospects of Infinity, Part II*, World Scientific, 2008, 143–161.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Lowness*, section *Weak preservation*.
