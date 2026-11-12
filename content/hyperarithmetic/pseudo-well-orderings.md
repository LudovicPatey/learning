---
title: Pseudo-well-orderings and descending sequences of jumps
summary: Harrison's computable linear orders that are ill-founded but have no hyperarithmetic descending sequence; the Enderton–Putnam theorem that a descending sequence of jumps computes every hyperarithmetic set; HYP is not a model of ATR₀.
duration: 40
prerequisites: [sigma11-classes]
---

A computable linear order is a well-ordering if no function is a descending sequence. The hyperarithmetic sets see only part of the functions, and some computable orders look well-ordered to them: Harrison's **pseudo-well-orderings** are ill-founded, but have no hyperarithmetic descending sequence. They are obtained from the trees of :ref{#thm-no-hyp-path} through the Kleene–Brouwer ordering. The lesson then studies what happens when the jump is iterated along such an order: a descending sequence of jumps appears, and by a theorem of Enderton and Putnam it computes every hyperarithmetic set. Together, these facts show that the hyperarithmetic sets do not form a model of $\mathsf{ATR}_0$.

## Pseudo-well-orderings

:::theorem[Harrison]{#thm-harrison}
There is a computable linear order that is not a well-ordering but has no hyperarithmetic descending sequence.
:::

:::proof{of=thm-harrison}
Let $T$ be the tree of :ref{#thm-no-hyp-path}, and $L$ the Kleene–Brouwer ordering on $T$, a computable linear order. Since $T$ has a path, $L$ is not a well-ordering (:ref{#thm-kleene-brouwer}).

Let $D = (\sigma_j)$ be a descending sequence in $L$; we show that $D'$ computes a path of $T$. If $\sigma_{j+1} <_{\mathrm{KB}} \sigma_j$, then $\sigma_{j+1}$ extends $\sigma_j$ or lies to its left, so whenever both are defined at position $0$, $\sigma_{j+1}(0) \leq \sigma_j(0)$. The root appears at most once, so from some point on all $\sigma_j$ are non-empty, and their first values form a non-increasing sequence, eventually constant equal to some $p(0)$. From that point on, all $\sigma_j$ begin with $p(0)$; the sequence $\langle p(0) \rangle$ appears at most once, after which all $\sigma_j$ have length at least $2$, and the same argument applies to their second values, which are eventually constant equal to some $p(1)$; and so on. Each $p \uh k$ is a prefix of some $\sigma_j \in T$, so $p$ is a path of $T$. The limit of a non-increasing sequence of numbers computable in $D$ is computable in $D'$, uniformly: starting from any term, ask $D'$ whether a later term is smaller, and move to it until the answer is negative. Applying this to the values at position $k$, from a stage after which all $\sigma_j$ extend $p \uh k$ and are different from it, gives $p(k)$ and such a stage for $k + 1$; so $p \leq_T D'$.

If $D$ were hyperarithmetic, so would be $D'$ and $p$, contradicting the choice of $T$.
:::

Such an order is a **pseudo-well-ordering**, or **Harrison order**. Harrison showed that its order type is $\omega_1^{\mathrm{CK}} \cdot (1 + \eta) + \rho$, where $\eta$ is the type of the rationals and $\rho < \omega_1^{\mathrm{CK}}$: an initial well-ordered part of length $\omega_1^{\mathrm{CK}}$, followed by copies of $\omega_1^{\mathrm{CK}}$ indexed by a dense order without endpoints, and a final segment of type $\rho$; we admit this description (Harrison 1968). The third exercise proves the part that matters below: the well-founded part has type exactly $\omega_1^{\mathrm{CK}}$.

:::figure[The order type $\omega_1^{\mathrm{CK}} \cdot (1 + \eta) + \rho$ of a Harrison order. The well-founded part $W$ is an initial segment of type $\omega_1^{\mathrm{CK}}$; after it, every element has a descending sequence below it, but no such sequence is hyperarithmetic, and no hyperarithmetic set separates $W$ from the rest.]{#fig-harrison}
<svg class="fig" viewBox="0 0 600 150" width="600" role="img" aria-label="A Harrison order: a well-founded initial segment of type omega one CK, then densely many copies of omega one CK, then a final well-ordered segment; a descending sequence lies in the ill-founded part"><line x1="30" y1="60" x2="220" y2="60" class="accent-stroke" stroke-width="3"/><line x1="232" y1="60" x2="500" y2="60" class="ink-stroke" stroke-width="1.4"/><line x1="236" y1="54" x2="236" y2="66" class="muted-stroke" stroke-width="1"/><line x1="258" y1="54" x2="258" y2="66" class="muted-stroke" stroke-width="1"/><line x1="280" y1="54" x2="280" y2="66" class="muted-stroke" stroke-width="1"/><line x1="302" y1="54" x2="302" y2="66" class="muted-stroke" stroke-width="1"/><line x1="324" y1="54" x2="324" y2="66" class="muted-stroke" stroke-width="1"/><line x1="346" y1="54" x2="346" y2="66" class="muted-stroke" stroke-width="1"/><line x1="368" y1="54" x2="368" y2="66" class="muted-stroke" stroke-width="1"/><line x1="390" y1="54" x2="390" y2="66" class="muted-stroke" stroke-width="1"/><line x1="412" y1="54" x2="412" y2="66" class="muted-stroke" stroke-width="1"/><line x1="434" y1="54" x2="434" y2="66" class="muted-stroke" stroke-width="1"/><line x1="456" y1="54" x2="456" y2="66" class="muted-stroke" stroke-width="1"/><line x1="478" y1="54" x2="478" y2="66" class="muted-stroke" stroke-width="1"/><line x1="512" y1="60" x2="570" y2="60" class="ink-stroke" stroke-width="3"/><circle cx="470" cy="82" r="3" class="ink-fill"/><circle cx="400" cy="82" r="3" class="ink-fill"/><circle cx="340" cy="82" r="3" class="ink-fill"/><circle cx="300" cy="82" r="3" class="ink-fill"/><circle cx="276" cy="82" r="3" class="ink-fill"/><circle cx="262" cy="82" r="3" class="ink-fill"/><circle cx="254" cy="82" r="3" class="ink-fill"/><text x="244" y="86" text-anchor="end" class="mrm" font-size="12">⋯</text><text x="125" y="46" text-anchor="middle" class="label">well-founded part W</text><text x="125" y="88" text-anchor="middle" class="mrm" font-size="14"><tspan class="math">ω</tspan><tspan font-size="10" dy="4">1</tspan><tspan font-size="9" dy="-11">CK</tspan><tspan dy="7"></tspan></text><text x="366" y="46" text-anchor="middle" class="label">copies of the type of W, indexed by η</text><text x="541" y="46" text-anchor="middle" class="mrm" font-size="14"><tspan class="math">ρ</tspan> &lt; <tspan class="math">ω</tspan><tspan font-size="10" dy="4">1</tspan><tspan font-size="9" dy="-11">CK</tspan><tspan dy="7"></tspan></text><text x="366" y="110" text-anchor="middle" class="label">a descending sequence: it is not hyperarithmetic</text><text x="300" y="140" text-anchor="middle" class="mrm" font-size="14">order type <tspan class="math">ω</tspan><tspan font-size="10" dy="4">1</tspan><tspan font-size="9" dy="-11">CK</tspan><tspan dy="7"> · (1 + <tspan class="math">η</tspan>) + <tspan class="math">ρ</tspan></tspan></text></svg>
:::

:::quiz[Harrison orders]
In the proof of :ref{#thm-harrison}, why are the first values $\sigma_j(0)$ eventually constant?

- [x] Because a step down in the Kleene–Brouwer ordering either extends the current sequence, keeping its first value, or moves to the left, which can only decrease the first value; a non-increasing sequence of numbers is eventually constant.
- [ ] Because $T$ is finitely branching.

  $T$ may be infinitely branching; the argument only uses the ordering.
- [ ] Because $D$ is hyperarithmetic.

  The argument applies to every descending sequence.
:::

## Descending sequences of jumps

A computable linear order $L$ that is not a well-ordering may still carry a **jump hierarchy**: a set $Y$ with
$$
Y^{[j]} = \big(Y^{[<j]}\big)' \quad \text{for every } j \text{ in the field of } L, \qquad Y^{[<j]} = \{ \langle i, m \rangle : i <_L j \wedge m \in Y^{[i]} \},
$$
and no other columns. Along a computable well-ordering, such hierarchies exist and are Turing equivalent to H-sets (Simpson, Section VIII.3). Along an ill-founded order, a descending sequence $j_0 >_L j_1 >_L \cdots$ gives sets $A_n = Y^{[<j_n]}$ with $A_{n+1}' = Y^{[j_{n+1}]} \leq_T A_n$, the column $j_{n+1}$ of $A_n$: an infinite descending sequence in the Turing degrees, each set computing the jump of the next one. Jump hierarchies along ill-founded orders need not exist, but Harrison showed that some ill-founded orders carry them (Monin and Patey, section "HYP is not a model of $\mathsf{ATR}_0$"). The next theorem shows that descending sequences of jumps are very complex.

:::theorem[Enderton, Putnam]{#thm-enderton-putnam}
Let $(A_n)$ be a sequence of sets such that $A_{n+1}' \leq_T A_n$ for every $n$. Then every hyperarithmetic set is computable in every $A_n$. In particular, no $A_n$ is hyperarithmetic.
:::

The proof climbs along $\mathcal O$, using the descending sequence to pay for each jump: a jump of something below $A_{n+1}$ is below $A_n$. Limit steps cost finitely many jumps, by a definability argument that avoids any uniformity: the H-sequences of :ref{#def-h-sequence} are unique, so a set computable in $B$ that is an H-sequence is recognized arithmetically in $B$.

:::proof{of=thm-enderton-putnam}
By induction on $j$, $A_{n+j}^{(j)} \leq_T A_n$ for all $n$ and $j$, since the jump preserves Turing reducibility. In particular $\emptyset' \leq_T A_1' \leq_T A_0$, and likewise $\emptyset' \leq_T A_n$ for every $n$.

For $a \in \mathcal O$, let $Y_a$ be the unique H-sequence along $a$ (:ref{#lem-h-sequence-unique}), whose column $a$ is $H_a$. We prove by induction on $a \in \mathcal O$ that $Y_a \leq_T A_n$ for every $n$.

- $a = 1$. Then $Y_1 = \emptyset$, since $R(\cdot, 1)$ is empty.
- $a = 2^c$. The columns of $Y_a$ other than $a$ form an H-sequence along $c$, so they are those of $Y_c$, and the column $a$ is $(Y_c^{[c]})'$. Hence $Y_a \leq_T Y_c'$. By the induction hypothesis $Y_c \leq_T A_{n+1}$, so $Y_a \leq_T A_{n+1}' \leq_T A_n$.
- $a = 3 \cdot 5^e$. The columns of $Y_a$ are the sets $H_u$ for $R(u, a)$, and the column $a$ is $H_a$, which is computable in $\emptyset'$ and the set $S = \{ \langle u, v \rangle : R(u, a) \wedge v \in H_u \}$. For $u$ with $R(u, a)$, we have $u <_{\mathcal O} a$, and for every set $B$ that computes $Y_u$,
  $$
  v \in H_u \iff \exists e\ \big(\Phi^B_e \text{ is total, } \{0,1\}\text{-valued, an H-sequence along } u, \text{ and } \langle u, v \rangle \in \Phi^B_e\big),
  $$
  by uniqueness of the H-sequence along $u$. The formula in parentheses is arithmetic in $B$, and does not depend on $a$ or on $B$; so there is a fixed $k$ such that, for every $B$ computing all the $Y_u$ with $u <_{\mathcal O} a$, the set $S$ is $\Sigma^0_k(B)$, hence computable in $B^{(k)}$ by Post's theorem relativized (:ref{#thm-post}). Take $B = A_{n+k}$, which computes every $Y_u$ by the induction hypothesis: $S \leq_T A_{n+k}^{(k)} \leq_T A_n$. Since also $\emptyset' \leq_T A_n$, we get $H_a \leq_T A_n$, and $Y_a \leq_T A_n$, its columns other than $a$ being columns of $H_a$.

Every hyperarithmetic set is computable in some $H_a = Y_a^{[a]}$, hence in every $A_n$. If $A_n$ were hyperarithmetic, it would compute every hyperarithmetic set, contradicting :ref{#prop-hyp-ideal}.
:::

:::quiz[the Enderton–Putnam theorem]
In the limit case of the proof of :ref{#thm-enderton-putnam}, why does the proof use the quantifier $\exists e$ instead of a reduction of $H_u$ to $B$ computed from $u$?

- [x] Because the induction hypothesis only says that each $Y_u$ is computable in $B$, with no index given uniformly in $u$; the uniqueness of H-sequences lets an arithmetic formula find a correct index, at the cost of finitely many jumps.
- [ ] Because $H_u$ is not computable in $B$.

  It is, by the induction hypothesis; what is missing is uniformity in $u$.
- [ ] Because $R(u, a)$ is undecidable.

  It is decided by $\emptyset' \leq_T A_n$; the quantifier $\exists e$ serves another purpose.

---

Why does the number $k$ of jumps not grow along the induction?

- [x] Because the formula defining $S$ from $B$ is the same at every limit notation, with $u$, $v$ and $a$ as number variables; only the oracle changes.
- [ ] Because $k = 1$.

  Totality and the jump conditions of an H-sequence require several quantifier alternations; any fixed $k$ suffices.
- [ ] Because the induction is along $\omega$.

  It is along $<_{\mathcal O}$; the descending sequence $(A_n)$ provides the jumps at each step.
:::

## HYP is not a model of ATR₀

In the ω-model $\mathrm{HYP}$, a Harrison order $L$ satisfies the arithmetic definition of being a linear order, and it has no descending sequence in the model; so $\mathrm{HYP}$ believes that $L$ is a well-ordering. Statements about well-orderings that hold in $\mathcal P(\nat)$ may then fail in $\mathrm{HYP}$. Arithmetic transfinite recursion, the axiom scheme of $\mathsf{ATR}_0$ (:ref{to="big-five/atr0-pi11ca0"}), is one of them: it asserts the existence of a hierarchy along every well-ordering, in particular of a jump hierarchy.

:::proposition{#prop-hyp-not-atr0}
Let $L$ be a computable linear order that is not a well-ordering. Then no jump hierarchy along $L$ is hyperarithmetic. Consequently, $\mathrm{HYP}$ is not an ω-model of $\mathsf{ATR}_0$.
:::

:::proof{of=prop-hyp-not-atr0}
Let $Y$ be a jump hierarchy along $L$, and let $j_0 >_L j_1 >_L \cdots$ be a descending sequence. As explained above, the sets $A_n = Y^{[<j_n]}$ satisfy $A_{n+1}' \leq_T A_n$, so by :ref{#thm-enderton-putnam}, $A_0 \leq_T Y$ is not hyperarithmetic, and neither is $Y$.

Now let $L$ be a Harrison order (:ref{#thm-harrison}). If $\mathrm{HYP}$ were an ω-model of $\mathsf{ATR}_0$, then, since $\mathrm{HYP}$ satisfies "$L$ is a well-ordering", it would contain a set $Y$ satisfying in $\mathrm{HYP}$ the definition of a jump hierarchy along $L$. This definition is arithmetic, and an ω-model evaluates arithmetic formulas correctly; so $Y$ would be a hyperarithmetic jump hierarchy along $L$, which is impossible.
:::

This is the result announced in the reverse mathematics track. Jump hierarchies, and more generally arithmetic hierarchies, along ill-founded orders that a model believes to be well-ordered are called **pseudo-hierarchies**; by :ref{#thm-enderton-putnam}, a jump pseudo-hierarchy computes every hyperarithmetic set. Their existence for suitable orders is a proof method in reverse mathematics, the method of pseudo-hierarchies (Simpson, Section V.4, Lemma V.4.12).

## Exercises

::::exercise{difficulty=2}
Show that the set of indices of computable linear orders with no hyperarithmetic descending sequence is $\Sigma^1_1$, and deduce a second proof of :ref{#thm-harrison}.

:::solution
By :ref{#cor-hyp-quantifier}, "there is a hyperarithmetic descending sequence in $L_e$" is $\Pi^1_1$, so its negation is $\Sigma^1_1$; "$L_e$ is a linear order" is arithmetic. The resulting $\Sigma^1_1$ set $P$ contains $\mathrm{WO}$. If it were equal to $\mathrm{WO}$, then $\mathrm{WO}$ would be $\Sigma^1_1$, contradicting :ref{#prop-pi11-not-sigma11}. So some $e \in P \setminus \mathrm{WO}$ is the index of a computable linear order that is not a well-ordering and has no hyperarithmetic descending sequence.
:::
::::

::::exercise{difficulty=2}
Let $L$ be a Harrison order. Show, without the admitted description of its order type, that its well-founded part $W$, the set of elements $x$ such that $L$ restricted to $\{ y : y <_L x \}$ is a well-ordering, is an initial segment of type exactly $\omega_1^{\mathrm{CK}}$.

:::solution
$W$ is an initial segment, and its type is the supremum of the types of the restrictions of $L$ below its elements, plus one. Each such restriction is a computable well-ordering, so the type of $W$ is at most $\omega_1^{\mathrm{CK}}$. Suppose it is some $\alpha < \omega_1^{\mathrm{CK}}$. Then $x \in W$ if and only if the restriction of $L$ below $x$ embeds into a fixed computable well-ordering of type $\alpha$, a $\Sigma^1_1$ condition; $W$ is also $\Pi^1_1$, so it would be $\Delta^1_1$, hence hyperarithmetic by :ref{#thm-kleene-delta11}. The complement of $W$ is non-empty, since $L$ is not a well-ordering, and has no $L$-least element: if $x$ were one, everything below $x$ would be in $W$, so the restriction below $x$ would be a well-ordering, and $x \in W$. Starting from an element of the complement and choosing repeatedly the element of least code of the complement below the previous one gives a descending sequence computable in $L$ and the complement of $W$, hence hyperarithmetic. This contradicts :ref{#thm-harrison}.
:::
::::

## Notes and references

Harrison (1968) studied the pseudo-well-orderings and determined their order types. Enderton and Putnam (1970) proved that a descending sequence of jumps computes every hyperarithmetic set; the proof given here follows Simpson (Lemmas VIII.3.22 and VIII.3.23), who proves it in $\mathsf{ACA}_0$, and the deduction that $\mathrm{HYP}$ is not a model of $\mathsf{ATR}_0$ follows Monin and Patey. That $\mathrm{HYP}$ is nevertheless the intersection of the ω-models of $\mathsf{ATR}_0$, and the minimum ω-model of $\Delta^1_1$ comprehension, is proved in Simpson (Remark I.11.4, Sections VII.2, VIII.4 and VIII.6).

- J. Harrison, *Recursive pseudo-well-orderings*, Transactions of the American Mathematical Society 131 (1968), 526–543.
- H. B. Enderton and H. Putnam, *A note on the hyperarithmetical hierarchy*, Journal of Symbolic Logic 35 (1970), 429–430.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Remark I.11.4 and Sections V.4, VII.2, VIII.3, VIII.4 and VIII.6.
- B. Monin and L. Patey, *Computability theory*, chapter "The systems $\mathsf{ATR}_0$ and $\Pi^1_1\text{-}\mathsf{CA}_0$".
- G. E. Sacks, *Higher Recursion Theory*, Springer, 1990.
