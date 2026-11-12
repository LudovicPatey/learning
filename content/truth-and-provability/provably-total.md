---
title: Provably total functions of IΣ₁
summary: Provably total functions of a theory; every primitive recursive function is provably total in IΣ₁, with its recursion equations, and so are the functions defined by course-of-values recursion; the converse, due to Parsons, Mints and Takeuti, is stated; IΣ₁ does not prove the totality of the Ackermann function, and IΣ₂ does.
duration: 50
prerequisites: [fragments-of-arithmetic/coding, fragments-of-arithmetic/induction-collection, models-of-computation/ackermann-function]
---

A theory of arithmetic can be measured by the functions it knows to be total. Every total computable function $f$ has a $\Sigma_1$ definition in $\nat$, by :ref{#cor-sigma1-ce} applied to its graph, but a theory may be unable to prove that this definition defines a total function. Parikh's theorem shows that the total functions of $\mathrm I\Delta_0$ with bounded graphs grow at most polynomially. This lesson shows that $\mathrm I\Sigma_1$ proves the totality of every primitive recursive function, and more: it proves their recursion equations, so that the usual recursive definitions of arithmetic, in particular those of syntax used in the next lesson, can be carried out inside $\mathrm I\Sigma_1$. By a theorem of Parsons, Mints and Takeuti, which we state without proof, the primitive recursive functions are exactly the provably total functions of $\mathrm I\Sigma_1$.

## Provably total functions

:::definition{#def-provably-total}
Let $T$ be a theory in $\mathcal L_A$ true in $\nat$. A function $f : \nat^k \to \nat$ is **provably total** in $T$ if there is a $\Sigma_1$ formula $\varphi(\bar x, y)$ such that $\nat \models \varphi(\bar x, y) \leftrightarrow f(\bar x) = y$ for all $\bar x, y$, and $T \vdash \forall \bar x\ \exists! y\ \varphi(\bar x, y)$.
:::

In every model $M$ of $T$, such a formula defines a total function $f^M : M^k \to M$, and since $\nat \subseteq_e M$ and $\Sigma_1$ formulas go up (:ref{#cor-sigma1-upward}), $f^M$ extends $f$. The graph of $f^M$ is $\Delta_1$ in $T$: $y = f(\bar x)$ is equivalent to the $\Pi_1$ formula $\forall y'\ (\varphi(\bar x, y') \rightarrow y' = y)$. So a provably total function can be used inside $T$ as a new function symbol, without changing the classes $\Sigma_n$ and $\Pi_n$, as long as $T$ proves enough collection to absorb the bounded quantifiers created by its use.

The definition depends on the formula, not only on the function. Let $\mathrm{Prf}(p)$ be a $\Delta_0$ formula expressing, in $\nat$, that $p$ codes a proof of $0 = 1$ in $\mathrm{PA}$, and let $\varphi(x, y) \equiv y = 0 \wedge \forall p < x\ \neg \mathrm{Prf}(p)$. Since $\mathrm{PA}$ is consistent, $\varphi$ defines the zero function in $\nat$; but $\mathrm{PA} \vdash \forall x\ \exists y\ \varphi(x, y)$ would give $\mathrm{PA} \vdash \forall p\ \neg \mathrm{Prf}(p)$, the consistency of $\mathrm{PA}$, which is impossible by Gödel's second theorem.

## Primitive recursive functions in IΣ₁

The primitive recursive functions are obtained from the basic functions by composition and primitive recursion (:ref{#def-primitive-recursive}). We attach a $\Sigma_1$ formula $\varphi_f$ to each derivation of a primitive recursive function $f$, by induction on the derivation, as in the course on arithmetic definability (:ref{#thm-pr-sigma1}), but with the coding of sequences of the course on fragments of arithmetic instead of the β-function:

- for the basic functions, $y = 0$, $y = x + 1$ and $y = x_i$;
- for $f(\bar x) = h(g_1(\bar x), \dots, g_m(\bar x))$, the formula $\exists \bar z\ \big( \bigwedge_i \varphi_{g_i}(\bar x, z_i) \wedge \varphi_h(\bar z, y) \big)$;
- for $f(\bar x, 0) = g(\bar x)$ and $f(\bar x, n + 1) = h(\bar x, n, f(\bar x, n))$, the formula
$$
\varphi_f(\bar x, n, y) \equiv \exists s\ \Big( \mathrm{Seq}(s, n + 1) \wedge \varphi_g(\bar x, (s)_0) \wedge \forall i < n\ \varphi_h\big(\bar x, i, (s)_i, (s)_{i+1}\big) \wedge (s)_n = y \Big),
$$
which says that $s$ is the sequence of values $f(\bar x, 0), \dots, f(\bar x, n)$.

The last formula is not literally $\Sigma_1$, because of the bounded quantifier $\forall i < n$ in front of the $\Sigma_1$ formula $\varphi_h$; it is $\Sigma_1$ in $\mathrm I\Sigma_1$, by Parsons' lemma (:ref{#lem-fo-collection-closure}) in $\mathrm B\Sigma_1$, which $\mathrm I\Sigma_1$ proves (:ref{#thm-fo-parsons}). We replace it by an equivalent $\Sigma_1$ formula. In $\nat$, each $\varphi_f$ defines the graph of $f$.

:::theorem{#thm-pr-provably-total}
Every primitive recursive function is provably total in $\mathrm I\Sigma_1$. More precisely, for every derivation of a primitive recursive function $f$, $\mathrm I\Sigma_1$ proves $\forall \bar x\ \exists! y\ \varphi_f(\bar x, y)$, and it proves the equations of the derivation: if $f$ is obtained by primitive recursion from $g$ and $h$, then, writing $f$, $g$ and $h$ for the functions defined by $\varphi_f$, $\varphi_g$ and $\varphi_h$,
$$
\mathrm I\Sigma_1 \vdash f(\bar x, 0) = g(\bar x) \wedge \forall n\ f(\bar x, n + 1) = h(\bar x, n, f(\bar x, n)),
$$
and similarly for composition.
:::

Totality is proved by induction on $n$, applied to the statement "there is a sequence of values of length $n + 1$". This statement begins with an unbounded $\exists s$, so it is $\Sigma_1$ and no better: this is why $\Sigma_1$ induction, and not bounded induction, is needed. Uniqueness only compares two given sequences, entry by entry, and needs only bounded induction.

:::proof{of=thm-pr-provably-total}
By induction on the derivation; we work in $\mathrm I\Sigma_1$, which contains $\mathrm I\Delta_0 + \mathrm{exp}$ by :ref{#prop-isigma1-exp}, so that coded sequences (:ref{#def-coded-sequence}) are available. The basic functions are clear, and for composition, existence and uniqueness of $y$ follow from those for the $g_i$ and $h$, by logic.

Let $f$ be obtained by primitive recursion from $g$ and $h$, which are provably total by the induction hypothesis. *Existence.* Fix $\bar x$, and apply $\Sigma_1$ induction to $\exists y\ \varphi_f(\bar x, n, y)$, a $\Sigma_1$ formula of $\mathrm I\Sigma_1$ in the variable $n$. For $n = 0$, let $s$ be the sequence of length $1$ whose entry is $g(\bar x)$, given by concatenation (:ref{#prop-seq-basic}) with the empty sequence. If $s$ witnesses $\varphi_f(\bar x, n, y)$, let $w = h(\bar x, n, y)$ and $s' = s^\frown w$; then $s'$ has length $n + 2$, agrees with $s$ below $n + 1$, and $\varphi_h(\bar x, n, (s')_n, (s')_{n+1})$ holds; so $s'$ witnesses $\varphi_f(\bar x, n + 1, w)$.

*Uniqueness.* Let $s$ and $s'$ witness $\varphi_f(\bar x, n, y)$ and $\varphi_f(\bar x, n, y')$. Apply bounded induction, with parameters $s, s', n$, to $i \leq n \rightarrow (s)_i = (s')_i$. For $i = 0$, both entries satisfy $\varphi_g(\bar x, \cdot)$, so they are equal by the uniqueness for $g$. If $(s)_i = (s')_i$ and $i + 1 \leq n$, then $(s)_{i+1}$ and $(s')_{i+1}$ both satisfy $\varphi_h(\bar x, i, (s)_i, \cdot)$, so they are equal by the uniqueness for $h$. At $i = n$, $y = (s)_n = (s')_n = y'$.

*Equations.* $\varphi_f(\bar x, 0, y)$ holds if and only if $\varphi_g(\bar x, y)$, by the case $n = 0$. If $s$ witnesses $\varphi_f(\bar x, n + 1, y)$, then its restriction $s \restriction (n + 1)$ (:ref{#prop-seq-basic}) witnesses $\varphi_f(\bar x, n, (s)_n)$, and $\varphi_h(\bar x, n, (s)_n, y)$; so $f(\bar x, n + 1) = h(\bar x, n, f(\bar x, n))$.
:::

:::quiz[primitive recursion in IΣ₁]
Where does the proof of :ref{#thm-pr-provably-total} use $\Sigma_1$ collection, through Parsons' lemma?

- [x] To know that $\varphi_f$ is $\Sigma_1$ in $\mathrm I\Sigma_1$, despite the bounded quantifier $\forall i < n$ in front of $\varphi_h$; without this, $\Sigma_1$ induction could not be applied to $\exists y\ \varphi_f(\bar x, n, y)$.
- [ ] To bound the entries of the sequence $s$.

  No bound on the entries is needed: the sequence $s^\frown w$ exists for every $w$, by concatenation.
- [ ] In the proof of uniqueness.

  Uniqueness uses bounded induction on a formula with the parameters $s$ and $s'$; no collection is involved.

---

Why is the theorem proved for derivations, and not for functions?

- [x] The formula $\varphi_f$ is built from a derivation; two derivations of the same function give two formulas whose equivalence is true in $\nat$ but need not be proved by the method.
- [ ] Because a primitive recursive function has a unique derivation.

  Every primitive recursive function has infinitely many derivations, for instance by composing with identities.
- [ ] Because provably total functions are not closed under composition.

  They are, as the case of composition in the proof shows.
:::

The same argument applies to **course-of-values recursion** (:ref{#thm-course-of-values}), in which $f(\bar x, n)$ is computed from the whole sequence of previous values: the witness $s$ is again the sequence of values $f(\bar x, 0), \dots, f(\bar x, n)$, and the condition on its entries becomes $\forall i < n + 1\ \varphi_h(\bar x, i, s \restriction i, (s)_i)$, where $s \restriction i$ is the code of the sequence of the first $i$ values, in the coding of :ref{#def-coded-sequence}.

:::corollary{#cor-course-of-values-provable}
If $f$ is defined by course-of-values recursion from a function $h$ provably total in $\mathrm I\Sigma_1$, $f(\bar x, n) = h(\bar x, n, \langle f(\bar x, 0), \dots, f(\bar x, n - 1) \rangle)$, the sequence being coded as in :ref{#def-coded-sequence}, then $f$ is provably total in $\mathrm I\Sigma_1$, and $\mathrm I\Sigma_1$ proves this equation for the function defined by $\varphi_f$.
:::

The proof is that of the theorem, with the restriction $s \restriction i$ in place of the previous entry. The corollary is the form in which the theorem is used: syntactic notions such as "$z$ is the code of a term" or "the value of the term coded by $t$ under the assignment coded by $e$" are defined by course-of-values recursion on codes, since the codes of subterms are smaller than the code of the term, and the corollary provides $\Delta_1$ definitions of them in $\mathrm I\Sigma_1$ together with proofs of their recursive characterizations.

## The converse, and the Ackermann function

:::theorem[Parsons; Mints; Takeuti]{#thm-pmt}
A function is provably total in $\mathrm I\Sigma_1$ if and only if it is primitive recursive.
:::

We admit the converse direction. Parsons (1970) obtained it from his theorem that $\mathrm I\Sigma_1$ proves the same $\Pi_2$ sentences as primitive recursive arithmetic; Mints and Takeuti gave proof-theoretic proofs. A model-theoretic proof, by the method of indicators of Paris and Kirby, is in Hájek and Pudlák (Corollary IV.3.7); it belongs to the last course of this track, on independence results. Its idea is that if $f$ grows faster than every primitive recursive function, then in a non-standard model of $\mathrm I\Sigma_1$, the cut of the elements below $g(a)$, for the primitive recursive functions $g$ and a fixed non-standard $a$, is a model of $\mathrm I\Sigma_1$ that is not closed under $f$, as in the proof of Parikh's theorem.

:::corollary{#cor-ack-isigma1}
No $\Sigma_1$ definition of the Ackermann function (:ref{#def-ackermann}) is proved by $\mathrm I\Sigma_1$ to define a total function.
:::

:::proof{of=cor-ack-isigma1}
By :ref{#thm-pmt}, the Ackermann function would be primitive recursive, contradicting :ref{#cor-ack-not-pr}.
:::

The corollary depends on the admitted direction of :ref{#thm-pmt}. Its converse is the last exercise: $\mathrm I\Sigma_2$ proves the totality of the Ackermann function, through a $\Pi_2$ induction on the first argument. This is a first instance of the general phenomenon studied at the end of the track: the provably total functions of $\mathrm I\Sigma_{n+1}$ grow strictly faster than those of $\mathrm I\Sigma_n$.

## Exercises

::::exercise{difficulty=1}
Let $\theta(\bar x, y)$ be a $\Delta_0$ formula such that $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists! y\ \theta(\bar x, y)$, and $f$ the function it defines in $\nat$. Show that $f$ is bounded by a polynomial. Deduce that $x \mapsto 2^x$ is not provably total in $\mathrm I\Delta_0$ through a $\Delta_0$ definition.

:::solution
By Parikh's theorem (:ref{#thm-parikh}), there is a term $t$ with $\mathrm I\Delta_0 \vdash \forall \bar x\ \exists y < t(\bar x)\ \theta(\bar x, y)$. In $\nat$, the unique $y$ with $\theta(\bar x, y)$ is $f(\bar x)$, so $f(\bar x) < t(\bar x)$, and $t$ is a polynomial with natural coefficients. The function $2^x$ is not bounded by a polynomial.
:::
::::

::::exercise{difficulty=2}
Let $M$ be a model of $\mathrm I\Sigma_1$ and $I$ a cut of $M$, closed under addition and multiplication, such that $I \models \mathrm I\Sigma_1$. Show that $I$ is closed under $f^M$ for every primitive recursive function $f$, where $f^M$ is the function defined in $M$ by the formula $\varphi_f$ of a derivation of $f$.

:::solution
By :ref{#thm-pr-provably-total} applied in $I$, the formula $\varphi_f$ defines a total function $f^I$ on $I$. Let $\bar a \in I$. Then $I \models \varphi_f(\bar a, f^I(\bar a))$, and $\varphi_f$ is a $\Sigma_1$ formula, so $M \models \varphi_f(\bar a, f^I(\bar a))$ by :ref{#cor-sigma1-upward}. By uniqueness in $M$, $f^M(\bar a) = f^I(\bar a)$, which belongs to $I$.
:::
::::

::::exercise{difficulty=3}
Let $\mathrm{Comp}(c)$ be the bounded formula saying that $c$ codes a finite set of triples $\langle x, y, z \rangle$ such that every triple in $c$ is **justified** in $c$: either $x = 0$ and $z = y + 1$; or $x = x' + 1$, $y = 0$ and $\langle x', 1, z \rangle \in c$; or $x = x' + 1$, $y = y' + 1$ and there is $w$ with $\langle x, y', w \rangle \in c$ and $\langle x', w, z \rangle \in c$. Let $\alpha(x, y, z) \equiv \exists c\ (\mathrm{Comp}(c) \wedge \langle x, y, z \rangle \in c)$. Show that $\alpha$ defines the Ackermann function in $\nat$, that $\mathrm I\Sigma_1$ proves that it defines a partial function, and that $\mathrm I\Sigma_2$ proves that it is total.

:::solution
*In $\nat$.* Every triple of a computation is correct, by induction on $\langle x, y \rangle$ in the lexicographic order, using the defining equations; conversely, the set of triples used in the evaluation of $A(x, y)$ by the equations is a computation.

*Partial function.* Work in $\mathrm I\Sigma_1$. The union of two computations is a computation, since justifications are preserved when the set is enlarged, and it is coded by :ref{#thm-delta0-comprehension}; so it suffices to show that a single computation $c$ is functional. Suppose not. By the least number principle for bounded formulas, with parameter $c$, let $x$ be least such that $c$ contains two triples $\langle x, y, z \rangle$ and $\langle x, y, z' \rangle$ with $z \neq z'$ for some $y$, and then $y$ least for this $x$. If $x = 0$, then $z = y + 1 = z'$. If $x = x' + 1$ and $y = 0$, then $\langle x', 1, z \rangle$ and $\langle x', 1, z' \rangle$ are in $c$, a conflict at $x' < x$. If $x = x' + 1$ and $y = y' + 1$, the two triples are justified by $w$ and $w'$ with $\langle x, y', w \rangle, \langle x, y', w' \rangle \in c$, so $w = w'$ by the minimality of $y$, and then $\langle x', w, z \rangle$ and $\langle x', w, z' \rangle$ are in $c$, a conflict at $x' < x$. Each case contradicts the choice of $x$ and $y$.

*Totality in $\mathrm I\Sigma_2$.* Apply $\Pi_2$ induction, available by :ref{#thm-fo-isigma-ipi}, to $\tau(x) \equiv \forall y\ \exists z\ \alpha(x, y, z)$. For $x = 0$, the computation $\{ \langle 0, y, y + 1 \rangle \}$ works. Assume $\tau(x)$, and prove $\forall y\ \exists z\ \alpha(x + 1, y, z)$ by $\Sigma_1$ induction on $y$, with $x$ as a parameter, using $\tau(x)$ as a hypothesis. For $y = 0$, take a computation $c$ containing $\langle x, 1, z \rangle$ and add $\langle x + 1, 0, z \rangle$. If $c$ contains $\langle x + 1, y, w \rangle$, take a computation $c'$ containing $\langle x, w, z \rangle$, given by $\tau(x)$, and add $\langle x + 1, y + 1, z \rangle$ to $c \cup c'$. The induction on $y$ is $\Sigma_1$, and the induction on $x$ is for the $\Pi_2$ formula $\tau$.
:::
::::

## Notes and references

The closure of the $\mathrm I\Sigma_1$-provably total functions under primitive recursion is Theorem I.1.54 of Hájek and Pudlák, with the lemma I.1.55 used in the proof above; they remark that course-of-values recursion is treated in the same way, and use it for the arithmetization of syntax (Section I.1(d)). The characterization of the provably total functions of $\mathrm I\Sigma_1$ is due to Parsons (1970), and was reproved by Mints and by Takeuti; Hájek and Pudlák prove it by indicators (Corollary IV.3.7, credited there to Takeuti and Mints). The consistency statement of the example is Gödel's.

- C. Parsons, *On a number theoretic choice schema and its relation to induction*, in Intuitionism and Proof Theory, North-Holland, 1970, 459–473.
- P. Hájek and P. Pudlák, *Metamathematics of First-Order Arithmetic*, Springer, 1993, Chapter I, Section 1(c), and Chapter IV, Section 3.
- G. Takeuti, *Proof Theory*, North-Holland, 1975.
