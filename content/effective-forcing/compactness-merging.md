---
title: Compactness and merging
summary: Compact forcing questions and the preservation of hyperimmunity; merging forcing questions and the avoidance of PA degrees; ω-merging and DNC functions; the properties of the questions of Cohen, Jockusch–Soare, computable Sacks and computable Mathias forcing.
duration: 30
prerequisites: [forcing-question, pi01-classes/pa-degrees, immunity-growth/immune-sets]
---

A $\Sigma^0_1$-preserving forcing question gives cone avoidance by comparing the set of positive answers with the set to be avoided (:ref{#thm-question-preservation}). Two other weakness properties need more of the question. To preserve a hyperimmune function, a positive answer about a convergence must come with a bound on the value, so that the answers define a computable function to compare with the hyperimmune one: this is **compactness**. To avoid PA degrees, two negative answers must be realized by one extension, so that a $\{0, 1\}$-valued functional can be made to diverge: this is **merging**. Jockusch–Soare forcing is compact but not merging, and its generic sets may be PA. Both properties are stated at level $1$ only.

## Preservation of hyperimmunity

A function $f$ is **hyperimmune relative to $G$** if no $G$-computable function dominates it (:ref{#def-hyperimmune-fn} relativized). Weakly 1-generic sets compute hyperimmune functions, so Cohen generic sets do not preserve all hyperimmune functions at once; they preserve each one separately. The property needed is that a positive answer about a convergence is witnessed by a finite bound on the value. For a functional $\Phi_e$, let $\Phi_{b(e)}$ be the functional such that $\Phi^G_{b(e)}(m, k)\converge$ if and only if $\Phi^G_e(m)\converge < k$, with $b$ computable; we write "$\Phi^G_e(m)\converge < k$" for this $\Sigma^0_1$ sentence.

:::definition{#def-question-compact}
A forcing question is **compact** (at level $1$) if for every condition $c$, functional $\Phi_e$ and number $m$, if $c \mathrel{?{\vdash}} \Phi^G_e(m)\converge$, then $c \mathrel{?{\vdash}} \Phi^G_e(m)\converge < k$ for some $k$.
:::

:::theorem{#thm-question-hyperimmunity}
Let $\mathbb P$ have a $\Sigma^0_1$-preserving compact forcing question, and let $f$ be a hyperimmune function. For every sufficiently generic set $G$, $f$ is hyperimmune relative to $G$.
:::

:::proof{of=thm-question-hyperimmunity}
Fix $e$, and let $E_e$ be the set of conditions $d$ such that $d \Vdash \Phi^G_e(m)\diverge$ for some $m$, or $d \Vdash \Phi^G_e(m)\converge < f(m)$ for some $m$. Given a condition $c$, the set of pairs $(m, k)$ with $c \mathrel{?{\vdash}} \Phi^G_e(m)\converge < k$ is c.e., since the question is $\Sigma^0_1$-preserving. Let $g$ be the partial computable function such that $g(m)$ is the $k$ of the first such pair enumerated with first coordinate $m$.

- If $g(m)$ is undefined for some $m$, then $c \mathrel{?{\nvdash}} \Phi^G_e(m)\converge$ by compactness, so some extension of $c$ forces $\Phi^G_e(m)\diverge$.
- If $g$ is total, it is computable, so $f(m) > g(m)$ for some $m$, since $f$ is hyperimmune. Some extension of $c$ forces $\Phi^G_e(m)\converge < g(m)$, hence $\Phi^G_e(m)\converge < f(m)$: every member satisfies it.

So $E_e$ is dense. If $G$ is generic for every $E_e$, then for every $e$, $\Phi^G_e$ is partial or $\Phi^G_e(m) < f(m)$ for some $m$, so no $G$-computable function dominates $f$.
:::

The questions of Cohen, Jockusch–Soare and computable Sacks forcing (:ref{#ex-cohen-question}, :ref{#thm-tree-question}) are compact at level $1$. For Cohen forcing, a string $\tau \succeq \sigma$ with $\Phi^\tau_e(m)\converge = v$ gives $\sigma \mathrel{?{\vdash}} \Phi^G_e(m)\converge < v + 1$; for Sacks forcing, a node does the same. For Jockusch–Soare forcing, if all members of $\mathcal P$ make $\Phi_e(m)$ converge, the computations converge on the strings of $T_{\mathcal P}$ of some length $\ell$, as in :ref{#lem-uniform-bound}, and one more than the largest of their values bounds them all. So for each of these notions and each hyperimmune $f$, every sufficiently generic set preserves the hyperimmunity of $f$. For Jockusch–Soare forcing this gives a **hyperimmunity-preserving basis theorem**: every non-empty $\Pi^0_1$ class has a member relative to which a given hyperimmune function remains hyperimmune. Monin and Patey state the theorem at every level $n$: if the question is $\Sigma^0_{n+1}$-preserving and compact for $\Sigma^0_{n+1}$ sentences (a positive answer about $\exists y\ \psi(y)$ is already positive for $\exists y < k\ \psi(y)$, for some $k$), then $f$ hyperimmune relative to $\emptyset^{(n)}$ remains hyperimmune relative to $G^{(n)}$. The proof is the same, with the formulas $\Phi^{G^{(n)}}_e(m)\converge < k$ written as $\Sigma^0_{n+1}$ sentences; it is not given here.

## Avoiding PA degrees

The last property controls two questions at once. Recall that a set is PA if it computes a $\{0, 1\}$-valued DNC function (:ref{#def-pa-degree}).

:::definition{#def-question-merging}
A forcing question is **merging** (at level $1$) if for every condition $c$ and all $\Sigma^0_1$ sentences $\varphi_0$ and $\varphi_1$ with $c \mathrel{?{\nvdash}} \varphi_0$ and $c \mathrel{?{\nvdash}} \varphi_1$, some extension of $c$ forces both $\neg \varphi_0$ and $\neg \varphi_1$.
:::

:::theorem{#thm-question-pa}
Let $\mathbb P$ have a $\Sigma^0_1$-preserving merging forcing question. Every sufficiently generic set $G$ is not PA.
:::

:::proof{of=thm-question-pa}
Fix $e$, and let $E_e$ be the set of conditions $d$ for which there is $i$ such that every member $X$ of $d$ satisfies $\Phi^X_e(i) \notin \{0, 1\}$, the computation diverging or giving another value, or every member satisfies $\Phi^X_e(i)\converge = \Phi_i(i)$, the right-hand side converging. Given a condition $c$, let $g$ be the partial computable function such that $g(i)$ is the first $v \in \{0, 1\}$ found with $c \mathrel{?{\vdash}} \Phi^G_e(i)\converge = v$; it is partial computable since the question is $\Sigma^0_1$-preserving. Let $i$ be an index of $g$, so that $\Phi_i = g$.

- If $g(i)$ is undefined, then $c \mathrel{?{\nvdash}} \Phi^G_e(i)\converge = 0$ and $c \mathrel{?{\nvdash}} \Phi^G_e(i)\converge = 1$, and since the question is merging, some extension of $c$ forces both negations: on its members, $\Phi_e(i)$ does not converge to $0$ or $1$.
- If $g(i) = v$, then $\Phi_i(i) = v$, and some extension of $c$ forces $\Phi^G_e(i)\converge = v = \Phi_i(i)$.

So $E_e$ is dense. If $G$ is generic for every $E_e$, no $\Phi^G_e$ is a $\{0, 1\}$-valued DNC function, so $G$ is not PA.
:::

The questions of Cohen and Sacks forcing are merging: if no extension of $\sigma$, or no node of $T$, makes either of two computations converge, the condition itself forces both divergences. Jockusch–Soare forcing has no $\Sigma^0_1$-preserving merging question: below the condition $\mathrm{DNC}_2$, every generic set is PA, so the conclusion of :ref{#thm-question-pa} fails. Here, two classes $\mathcal P \cap \{ X : \neg \varphi_0(X) \}$ and $\mathcal P \cap \{ X : \neg \varphi_1(X) \}$ can both be non-empty and disjoint.

:::quiz[compactness and merging]
In the proof of :ref{#thm-question-hyperimmunity}, why is compactness needed in the first case?

- [x] To conclude from the absence of any bound $k$ that the question about $\Phi^G_e(m)\converge$ itself is answered negatively, so that property 2 gives an extension forcing divergence.
- [ ] To show that $g$ is computable.

  $g$ is partial computable by $\Sigma^0_1$-preservation alone.
- [ ] To find an $m$ with $f(m) > g(m)$.

  That is the hyperimmunity of $f$, in the second case.

---

In the proof of :ref{#thm-question-pa}, why is $i$ chosen as an index of $g$ itself?

- [x] So that a positive answer $g(i) = v$ makes the forced value $\Phi^G_e(i) = v$ coincide with $\Phi_i(i)$, which defeats diagonal non-computability at $i$.
- [ ] So that $g$ is total.

  $g$ may be partial; the case $g(i)$ undefined is handled by merging.
- [ ] So that $\Phi_i(i)$ diverges.

  If $g(i)$ is defined, $\Phi_i(i)$ converges to it.
:::

## Summary

The table collects the properties of the questions of :ref{#ex-cohen-question}, :ref{#thm-tree-question} and of the question of computable Mathias forcing, studied in the next lesson (:ref{to="effective-forcing/mathias-forcing"}). The "no" for Jockusch–Soare forcing means that no $\Sigma^0_1$-preserving forcing question is merging, because of the condition $\mathrm{DNC}_2$; the "no" for Mathias forcing means that no forcing question is $\Sigma^0_2$-preserving, because its generic sets are high, as the next lesson shows.

| notion of forcing | $\Sigma^0_1$-preserving | $\Sigma^0_n$-preserving, all $n$ | compact | merging |
| --- | --- | --- | --- | --- |
| Cohen | yes | yes | yes | yes |
| Jockusch–Soare | yes | yes | yes | no |
| computable Sacks | yes | yes | yes | yes |
| computable Mathias | yes | no ($n = 2$) | yes | yes |

## Exercises

::::exercise{#exr-sacks-dnc difficulty=2}
Call a forcing question **$\omega$-merging** if whenever $c \mathrel{?{\nvdash}} \varphi_v$ for all $v$ in an infinite computable sequence of $\Sigma^0_1$ sentences $(\varphi_v)$, some extension of $c$ forces every $\neg \varphi_v$. Show that if a $\Sigma^0_1$-preserving forcing question is $\omega$-merging, every sufficiently generic set computes no DNC function, and that the question of Sacks forcing is $\omega$-merging.

:::solution
Repeat the proof of :ref{#thm-question-pa} with $g(i)$ the first $v \in \nat$ found with $c \mathrel{?{\vdash}} \Phi^G_e(i)\converge = v$. If $g(i)$ is undefined, $c \mathrel{?{\nvdash}} \Phi^G_e(i)\converge = v$ for every $v$, and $\omega$-merging gives an extension forcing all the negations, that is, $\Phi^G_e(i)\diverge$. Otherwise an extension forces $\Phi^G_e(i) = \Phi_i(i)$. So $\Phi^G_e$ is not DNC, for every $e$. For Sacks forcing, $T \mathrel{?{\nvdash}} \varphi_v$ means that no node of $T$ makes the corresponding computation converge, so $T$ forces all the negations at once, by :ref{#prop-sacks-complexity}.
:::
::::

## Notes and references

Compactness and merging, with the theorems on hyperimmunity and PA degrees and the exercise on $\omega$-merging, follow the chapter *Effective forcing* of Monin and Patey, section *Forcing question*, where merging is called $\Pi$-merging and both properties are stated at every level, for questions about $\Sigma^0_n$ and $\Pi^0_n$ sentences. The hyperimmunity-preserving basis theorem for $\Pi^0_1$ classes is a special case. Preservation of hyperimmunity as a tool for separating Ramsey-type principles is due to Patey (2017); the avoidance of PA degrees through merging is developed in :ref{to="compactness-avoidance/pa-avoidance"}.

- L. Patey, *Iterative forcing and hyperimmunity in reverse mathematics*, Computability 6 (2017), doi:10.3233/COM-160062; arXiv:1501.07709.
- B. Monin and L. Patey, *Computability theory*, chapter *Effective forcing*, section *Forcing question*.
