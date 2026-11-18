---
title: Learning isomorphism types from informant
summary: A learner reads more and more atomic facts about a copy of a structure and must eventually name its isomorphism type; locking sequences; a family of pairwise non-isomorphic structures is learnable if and only if each member is singled out in the family by an infinitary Σ₂ sentence (Bazhenov, Fokina, San Mauro); computable learners; examples and non-examples among abelian p-groups, linear orders and Boolean algebras.
duration: 45
prerequisites: [computable-structures/presentations]
---

Algorithmic learning theory, started by Gold and Putnam in the 1960s, studies procedures that receive more and more data about an unknown object and must eventually identify it. A learner may change its mind finitely often; it succeeds if its guesses eventually stabilize on a correct one. Fokina, Kötzing and San Mauro brought this framework to countable structures: the data are the atomic facts of a copy, and the learner must identify the isomorphism type. Bazhenov, Fokina and San Mauro then found a characterization of the learnable families in terms of infinitary formulas. This lesson proves it. The learner does not have to be computable. The characterization is about the information available in finite parts of a copy, and it is close to the back-and-forth analysis of structures.

## The framework

Fix a computable relational vocabulary $\tau$, containing equality. All structures are infinite and countable. Let $\mathrm{Atm}$ be the set of atomic sentences and negations of atomic sentences of $\tau$ with constants from $\nat$. A **fact** is an element of $\mathrm{Atm}$, such as $R(3, 5)$ or $\neg (2 = 7)$. For a structure $\mathcal S$ with domain $\nat$, its **diagram** $D(\mathcal S)$ is the set of facts true in $\mathcal S$, each number naming itself.

:::definition[Fokina, Kötzing, San Mauro]{#def-infex}
Let $\mathcal K = \{ \mathcal B_i : i \in \nat \}$ be a family of pairwise non-isomorphic structures.
- An **informant** for a structure $\mathcal S$ with domain $\nat$ is a sequence $(\varphi_0, \varphi_1, \ldots)$ of facts such that $\{ \varphi_k : k \in \nat \} = D(\mathcal S)$.
- A **learner** is a function $M$ from finite sequences of facts to $\nat$.
- $M$ **learns** $\mathcal K$ if, for every $i$, every copy $\mathcal S$ of $\mathcal B_i$ with domain $\nat$ and every informant $I$ for $\mathcal S$, the sequence $M(I \uh n)$ is eventually equal to $i$.

The family is **InfEx-learnable** (explanatory learning from informant) if some learner learns it.
:::

The learner must succeed on every copy and every order of presentation of the facts: it sees a structure through an arbitrary presentation, as computability theory does. It may output anything on sequences that are not initial segments of informants. A learner may be any function; whether it can be computable is a separate question.

:::example{#ex-learn-omega}
The family $\{ \omega, \omega^* \}$ of linear orders, with $\mathcal B_0 = \omega$ and $\mathcal B_1 = \omega^*$, the reverse of $\omega$, is learnable. Given a finite sequence of facts, count the numbers $m \neq 0$ for which a fact $m < 0$ has appeared, and those for which a fact $0 < m$ has appeared. Output $0$ if the first count is smaller than the second, and $1$ otherwise. In a copy of $\omega$, the number $0$ names an element with finitely many predecessors and infinitely many successors. Along any informant, the first count is eventually constant and the second grows without bound, so the learner eventually outputs $0$ forever. Symmetrically, it eventually outputs $1$ on the copies of $\omega^*$.
:::

## Locking sequences

The key notion goes back to Blum and Blum, in classical learning theory. Let $M$ learn $\mathcal K$. For a finite sequence $\sigma$ of facts, let $N_\sigma$ be the finite set of numbers it mentions. A **realization** of $\sigma$ in a structure $\mathcal B$ is an injective map $\nu : N_\sigma \to B$ such that every fact of $\sigma$ is true in $\mathcal B$ when each number $m$ is interpreted as $\nu(m)$.

:::definition{#def-locking}
Let $M$ learn $\mathcal K$. A finite sequence $\sigma$ of facts, with a realization $\nu$ in $\mathcal B_i$, is a **locking sequence** for $\mathcal B_i$ if $M(\sigma) = i$ and $M(\tau) = i$ for every finite sequence $\tau$ extending $\sigma$ that has a realization in $\mathcal B_i$ extending $\nu$.
:::

:::lemma{#lem-locking}
If $M$ learns $\mathcal K$, then every $\mathcal B_i$ has a locking sequence.
:::

:::proof{of=lem-locking}
Suppose not. We build an informant for a copy of $\mathcal B_i$ on which $M$ fails. We build finite sequences $\sigma_0 \preceq \sigma_1 \preceq \cdots$ with realizations $\nu_0 \subseteq \nu_1 \subseteq \cdots$ in $\mathcal B_i$. Fix an enumeration $b_0, b_1, \ldots$ of the domain of $\mathcal B_i$. Start with the empty sequence.

At stage $s$, the sequence $\sigma_s$ with $\nu_s$ is not a locking sequence. So either $M(\sigma_s) \neq i$ and no extension realized over $\nu_s$ changes the value of $M$, or some extension $\tau$ realized over an extension $\nu$ of $\nu_s$ satisfies $M(\tau) \neq M(\sigma_s)$. In the second case, let $\sigma' = \tau$ and $\nu' = \nu$; in the first case, $\sigma' = \sigma_s$ and $\nu' = \nu_s$. Then complete: let $m$ be the least number not in the domain of $\nu'$ and $b$ the first element of $\mathcal B_i$ not in its range; extend $\nu'$ by $m \mapsto b$. Append to $\sigma'$ all the facts, true under this map, about tuples of numbers below $s$ in the domain of the map, for the first $s$ relation symbols. This gives $\sigma_{s+1}$ and $\nu_{s+1}$.

The union $\nu = \bigcup_s \nu_s$ is a bijection between $\nat$ and $B_i$, since each stage adds the least missing number and the first missing element. Its pull-back $\mathcal S$ is a copy of $\mathcal B_i$ with domain $\nat$, and $\bigcup_s \sigma_s$ is an informant for $\mathcal S$. It contains only true facts, and it contains every true fact, since every tuple and symbol is eventually covered. If the second case occurs infinitely often, $M$ changes its value infinitely often along this informant. If it occurs finitely often, then from some stage on the first case holds: $M(\sigma_s) \neq i$, and no later extension changes the value. So $M$ converges to a value different from $i$. In both cases $M$ fails to learn $\mathcal B_i$.
:::

## The characterization

Recall the infinitary formulas: an **$\Sigma^{\mathrm{inf}}_2$ sentence** is a countable disjunction of sentences $\exists \bar x\, \psi(\bar x)$, where $\psi$ is a countable conjunction of formulas $\forall \bar y\, \theta(\bar x, \bar y)$ with $\theta$ quantifier-free. Countable disjunctions and conjunctions are arbitrary: no effectiveness is required.

:::theorem[Bazhenov, Fokina, San Mauro]{#thm-infex-characterization}
Let $\mathcal K = \{ \mathcal B_i : i \in \nat \}$ be a family of pairwise non-isomorphic infinite structures. Then $\mathcal K$ is InfEx-learnable if and only if there are $\Sigma^{\mathrm{inf}}_2$ sentences $\psi_i$ such that, for all $i$ and $j$,
$$
\mathcal B_j \models \psi_i \iff i = j.
$$
:::

**Intuition.** A learner that has stabilized has seen a finite configuration after which nothing it can see changes its mind: a locking sequence. "There is a configuration like this, and no finite extension of it of a certain kind exists" is an existential-universal statement, true in $\mathcal B_i$ and false in the other members of the family. Conversely, given the sentences, a learner guesses a witness for some $\psi_i$ and abandons it when the data refute it. Refutations of $\forall$-statements arrive in finite time, while the correct witness is never refuted.

:::proof{of=thm-infex-characterization}
($\Rightarrow$) Let $M$ learn $\mathcal K$, and fix $i$. By :ref{#lem-locking}, there is a locking sequence $\sigma$ for $\mathcal B_i$, with realization $\nu$. List $N_\sigma = \{ m_1, \ldots, m_k \}$, and use variables $x_1, \ldots, x_k$ for these numbers. For a finite sequence $\tau$ extending $\sigma$, list the numbers of $N_\tau \setminus N_\sigma$ as $m_{k+1}, \ldots, m_{k+l}$, with variables $y_1, \ldots, y_l$. Let $\theta_\tau(\bar x, \bar y)$ be the conjunction of the facts of $\tau$, with each number replaced by its variable, and of the inequalities between any two distinct variables. Let
$$
\psi_i \equiv \exists x_1 \ldots x_k \Big( \theta_\sigma(\bar x) \wedge \bigwedge_{\tau \succeq \sigma,\ M(\tau) \neq i} \forall y_1 \ldots y_l\ \neg \theta_\tau(\bar x, \bar y) \Big),
$$
where $l$ depends on $\tau$. This is a $\Sigma^{\mathrm{inf}}_2$ sentence.

*$\mathcal B_i \models \psi_i$*, with each $x_r$ interpreted as $\nu(m_r)$. The formula $\theta_\sigma$ holds, since $\nu$ realizes $\sigma$. If, for some $\tau \succeq \sigma$ with $M(\tau) \neq i$, elements $\bar b$ satisfied $\theta_\tau(\nu(\bar m), \bar b)$, then $\tau$ would have a realization extending $\nu$. Since $\sigma$ is locking, $M(\tau) = i$, a contradiction.

*$\mathcal B_j \not\models \psi_i$ for $j \neq i$.* Suppose that elements $\bar a$ of $\mathcal B_j$ witness $\psi_i$. They are distinct, by the inequalities in $\theta_\sigma$. Let $\mathcal S$ be a copy of $\mathcal B_j$ with domain $\nat$ in which each number $m_r \in N_\sigma$ names $a_r$. Let $I$ be an informant for $\mathcal S$ that starts with $\sigma$, followed by an enumeration of $D(\mathcal S)$; this is possible because the facts of $\sigma$ are true in $\mathcal S$. Every initial segment $\tau \succeq \sigma$ of $I$ consists of true facts about the numbers it mentions, so $\theta_\tau(\bar a, \bar b)$ holds for the elements $\bar b$ named by the new numbers. By the choice of $\bar a$, $M(\tau) = i$. So $M$ converges to $i$ on an informant for a copy of $\mathcal B_j$, and fails to learn $\mathcal B_j$.

($\Leftarrow$) Write each $\psi_i$ as $\bigvee_{k \in \nat} \exists \bar x\, \bigwedge_{l \in \nat} \forall \bar y\, \theta_{i, k, l}(\bar x, \bar y)$, repeating disjuncts or conjuncts if needed, with $\bar x$ of length $n_{i, k}$. A **candidate** is a triple $(i, k, \bar a)$ with $\bar a$ a tuple of $n_{i, k}$ numbers. Given a finite sequence $\rho$ of facts, a candidate is **refuted** by $\rho$ if there are $l$ and a tuple $\bar c$ of numbers such that $\rho$ contains facts about the tuple $\bar a \bar c$ from which $\neg \theta_{i, k, l}(\bar a, \bar c)$ follows. Here $\theta$ is quantifier-free, so its truth value is determined by the atomic facts about $\bar a \bar c$ in its vocabulary. Fix a coding of candidates by natural numbers. Let $M(\rho)$ be the first coordinate $i$ of the least candidate not refuted by $\rho$. Every finite sequence refutes only finitely many candidates, since each refutation needs the numbers of the candidate to appear in the sequence. So $M$ is well defined.

Let $I$ be an informant for a copy $\mathcal S$ of $\mathcal B_j$. Since $\mathcal S \models \psi_j$, there are $k_0$ and numbers $\bar a_0$ such that $\mathcal S \models \forall \bar y\, \theta_{j, k_0, l}(\bar a_0, \bar y)$ for every $l$. The candidate $t_0 = (j, k_0, \bar a_0)$ is never refuted, since the informant contains only true facts. Let $t = (i, k, \bar a)$ be a candidate with $i \neq j$. Since $\mathcal S \not\models \psi_i$, there are $l$ and $\bar c$ with $\mathcal S \models \neg \theta_{i, k, l}(\bar a, \bar c)$. Once the informant has given all atomic facts about $\bar a \bar c$, $t$ is refuted, and it stays refuted. Only finitely many candidates precede $t_0$. Those with first coordinate different from $j$ are all eventually refuted. So from some point on, the least unrefuted candidate is $t_0$ or a candidate preceding it with first coordinate $j$. Then $M(I \uh n) = j$ for all large $n$.
:::

:::quiz[the characterization of learnability]
In the proof of ($\Rightarrow$), why must the conjunction in $\psi_i$ range over all extensions $\tau$ of $\sigma$ on which $M$ changes its mind, and not only over those that are true in $\mathcal B_i$?

- [x] The sentence must be evaluated in every $\mathcal B_j$; there, the dangerous extensions are those true of the witnesses in $\mathcal B_j$, which need not be realizable in $\mathcal B_i$. Listing all mind-changing extensions makes $\psi_i$ false in $\mathcal B_j$, while the locking property makes it true in $\mathcal B_i$.
- [ ] Because the set of extensions true in $\mathcal B_i$ is not computable.

  Effectiveness plays no role here: the formulas are arbitrary infinitary formulas.
- [ ] To make $\psi_i$ a $\Sigma^{\mathrm{inf}}_2$ sentence.

  Any subset of the extensions would also give a $\Sigma^{\mathrm{inf}}_2$ sentence; the choice is made for correctness.

---

In the proof of ($\Leftarrow$), why does the learner use triples with a witness $\bar a$, rather than the indices $i$ alone?

- [x] Refuting $\psi_i$ itself would require seeing that no witness works, which is never finitely observable; refuting one candidate witness is finitely observable, and the correct candidate is never refuted.
- [ ] Because the structures are infinite.

  The point is the logical form of $\psi_i$, an existential over universal statements, not the size of the structures.
- [ ] To make the learner computable.

  The learner is not computable in general; the triples are needed for correctness.
:::

The learner of the proof can be made computable when the sentences are computable infinitary sentences given uniformly. The conjuncts $\theta_{i, k, l}$ are then listed effectively, and it suffices to count as refutations by $\rho$ only those that use $l < |\rho|$ and conjuncts listed within $|\rho|$ steps. Refutation becomes a finite check, and every true refutation is eventually counted, so the proof goes through.

:::corollary[Bazhenov, Fokina, San Mauro]{#cor-computable-learner}
If there are uniformly computable $\Sigma^c_2$ sentences $\psi_i$ with $\mathcal B_j \models \psi_i \iff i = j$, then $\mathcal K$ is learnable by a computable learner.
:::

::::exercise{#ex-learn-p-groups difficulty=1 objective="Apply the characterization to a family of abelian p-groups."}
Fix a prime $p$, and let $\mathcal B_i = \bigoplus_{n \in \nat} \mathbb Z(p^{i+1})$, the direct sum of countably many cyclic groups of order $p^{i+1}$, in the vocabulary of groups (with the graph of addition). Show that the family $\{ \mathcal B_i : i \in \nat \}$ is learnable by a computable learner.

:::solution
Let $\psi_i$ say that some element has order exactly $p^{i+1}$ and that every element $y$ satisfies $p^{i+1} y = 0$. Written with the graph of addition, "$p^{i+1} y = 0$" is existential in $y$: there are $y_1, \ldots, y_{p^{i+1}}$ with $y_1 = y$, $y_{r+1} = y_r + y$ and $y_{p^{i+1}} = 0$. Since addition is a function, the same condition can be written as a universal formula: for all $y_1, \ldots, y_{p^{i+1}}$, if $y_1 = y$ and $y_{r+1} = y_r + y$ for each $r$, then $y_{p^{i+1}} = 0$. Similarly, "$x$ has order exactly $p^{i+1}$" is the conjunction of $p^{i+1} x = 0$ and $p^i x \neq 0$, which is existential. So $\psi_i$ is a finitary $\exists\forall$ sentence. The group $\mathcal B_j$ has exponent $p^{j+1}$, and it has elements of order exactly $p^{j+1}$. If $j < i$, no element has order $p^{i+1}$; if $j > i$, some element does not satisfy $p^{i+1} y = 0$. So $\mathcal B_j \models \psi_i$ if and only if $i = j$. The sentences are computable and given uniformly, so :ref{#cor-computable-learner} gives a computable learner.
:::
::::

## Non-learnable families

The characterization turns non-learnability into a question about $\Sigma^{\mathrm{inf}}_2$ theories. For two structures, learnability of $\{ \mathcal B_0, \mathcal B_1 \}$ requires a $\Sigma^{\mathrm{inf}}_2$ sentence true in $\mathcal B_0$ and false in $\mathcal B_1$, and one true in $\mathcal B_1$ and false in $\mathcal B_0$. So if every $\Sigma^{\mathrm{inf}}_2$ sentence true in $\mathcal B_0$ is true in $\mathcal B_1$, the pair is not learnable. In the language of back-and-forth relations of a later course, $\mathcal B_1 \leq_2 \mathcal B_0$.

The following results are admitted.
- **Boolean algebras** (Bazhenov, Fokina, San Mauro). No family containing two non-isomorphic infinite Boolean algebras is learnable. The proof uses a lemma of Alaev: the $\Pi^{\mathrm{inf}}_2$ theories of two infinite Boolean algebras are comparable under inclusion, in the order of their numbers of atoms. Hence so are their $\Sigma^{\mathrm{inf}}_2$ theories, and no two members can be separated in both directions.
- **Linear orders** (Bazhenov, Fokina, San Mauro). No infinite family of pairwise non-isomorphic infinite linear orders is learnable, while there are learnable finite families of any size, such as the orders $(k - i) + \eta + (i + 1)$ for $i < k$, where $\eta$ is the order of the rationals.
- **Descriptive set theory** (Bazhenov, Cipriani, San Mauro, 2023). A family is InfEx-learnable if and only if the isomorphism relation on the copies of its members reduces continuously to $E_0$, the relation of eventual equality on $2^\nat$.

The last result places learnability in the theory of Borel equivalence relations. Learnability is the weakest level of classification above the trivial ones: a learner turns a copy into a sequence of guesses, and two copies are isomorphic exactly when their sequences of guesses eventually agree.

## Notes and references

The framework is that of Fokina, Kötzing and San Mauro (2019), for equivalence structures, extended to arbitrary families by Bazhenov, Fokina and San Mauro (2020), whose Theorem 3.1 is :ref{#thm-infex-characterization}. Their proof of ($\Rightarrow$) goes through a Turing embedding into a fixed learnable class and the pull-back theorem of Knight, Miller and Vanden Boom. The direct proof given here, with locking sequences, adapts the argument that Bazhenov, Fokina, Rossegger, Soskova and Vatev use for learning from text. Locking sequences are due to Blum and Blum (1975). The learner in ($\Leftarrow$) follows Bazhenov, Fokina and San Mauro. Here we use the hypothesis space of indices of the family, as in the 2024 paper, instead of indices in a computable enumeration of a larger class; for the characterization, the two settings are equivalent.

- E. Fokina, T. Kötzing and L. San Mauro, *Limit learning equivalence structures*, Proceedings of ALT 2019, PMLR 98 (2019), 383–403.
- N. Bazhenov, E. Fokina and L. San Mauro, *Learning families of algebraic structures from informant*, Information and Computation 275 (2020), 104590; arXiv:1905.01601.
- N. Bazhenov, V. Cipriani and L. San Mauro, *Learning algebraic structures with the help of Borel equivalence relations*, Theoretical Computer Science 951 (2023), 113762.
- L. Blum and M. Blum, *Toward a mathematical theory of inductive inference*, Information and Control 28 (1975), 125–155.
- E. M. Gold, *Language identification in the limit*, Information and Control 10 (1967), 447–474.

:::::exercises
::::exercise{#ex-learn-omega-zeta difficulty=1 objective="Find a separating Σ₂ sentence between two linear orders, in one direction."}
Find a finitary $\exists\forall$ sentence true in $\omega$ and false in the order $\zeta$ of the integers. Show that every finitary universal sentence true in $\omega$ is true in $\zeta$.

:::solution
The sentence $\exists x\, \forall y\, (x \leq y)$, saying that there is a least element, is true in $\omega$ and false in $\zeta$. A universal sentence $\forall \bar y\, \theta(\bar y)$ with $\theta$ quantifier-free is true in a linear order if and only if $\theta$ holds of every finite tuple, and the truth of $\theta(\bar b)$ depends only on the order type of the finite set of elements of $\bar b$, with their equalities. Every finite linear order embeds into $\omega$ and into $\zeta$, so $\omega$ and $\zeta$ satisfy the same universal sentences.
:::
::::

::::exercise{#ex-learn-equivalence difficulty=2 objective="Separate equivalence structures by Σ₂ sentences to show that a family is learnable."}
For $n \geq 1$, let $\mathcal E_n$ be the equivalence structure with exactly $n$ equivalence classes, all infinite. Show that $\{ \mathcal E_n : n \geq 1 \}$ is learnable by a computable learner.

:::solution
Let $\psi_n$ say that there are $n$ pairwise inequivalent elements $x_1, \ldots, x_n$ and that every element $y$ is equivalent to one of them: $\exists x_1 \ldots x_n \big( \bigwedge_{j \neq j'} \neg E(x_j, x_{j'}) \wedge \forall y \bigvee_j E(y, x_j) \big)$. This is a finitary $\exists\forall$ sentence, true in $\mathcal E_m$ if and only if $\mathcal E_m$ has exactly $n$ classes, that is, $m = n$. The sentences are computable uniformly in $n$, and :ref{#cor-computable-learner} applies (index the family by $n - 1$).
:::
::::

::::exercise{#ex-locking-finite difficulty=1 objective="See why locking sequences are needed by checking a learner on a structure it should not identify."}
Let $M$ be the learner that outputs $0$ on every sequence. Which families does it learn? Describe its locking sequences.

:::solution
It learns the families with a single member $\mathcal B_0$: on every informant for a copy of $\mathcal B_0$, it outputs $0$ forever. If the family has a second member $\mathcal B_1$, $M$ fails on its copies. When $M$ learns $\{ \mathcal B_0 \}$, every finite sequence realized in $\mathcal B_0$, the empty sequence included, is a locking sequence, since $M$ never changes its value.
:::
::::
:::::
