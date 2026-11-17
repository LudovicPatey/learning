---
title: Merging at level 2
summary: A forcing question for Σ⁰₂ sentences that is Σ⁰₁ relative to the condition and merges two negative answers gives jump PA avoidance; Cohen forcing has one; Mathias forcing with one reservoir in a partition regular class produces cohesive sets, and one large class cannot keep both halves of a split.
duration: 35
prerequisites: [jump-pa-avoidance, jump-cone-avoidance/sigma2-questions, jump-cone-avoidance/largeness, jump-cone-avoidance/pigeonhole-forcing, compactness-avoidance/weak-merging]
---

The previous lesson reduced the construction of ω-models without cohesive sets to jump PA avoidance. This lesson gives the abstract tool, which is :ref{to="compactness-avoidance/weak-merging"} one level up: a forcing question for $\Sigma^0_2$ sentences, with answers $\Sigma^0_1$ relative to $\emptyset'$, that forces two negative answers at once. Cohen forcing has such a question. The variants of Mathias forcing used for combinatorial principles do not, as long as they keep a single reservoir: their generic sets are cohesive. The last section locates the failure on the forcing question, and states the remedy developed in the rest of the course.

## Merging at level 2

Recall from :ref{to="jump-cone-avoidance/sigma2-questions"} the forcing questions for $\Sigma^0_2$ sentences: property 1 gives, after a positive answer, an extension forcing the sentence, and property 2 gives, after a negative answer, an extension forcing its negation, a $\Pi^0_2$ sentence, in the sense of :ref{#def-forcing-relation}. A question is $\Sigma^0_1(\mathcal M)$-preserving if its answers below each condition are $\Sigma^0_1$ relative to some member of $\mathcal M$ (:ref{#def-jump-question-local}). Sentences are about $Z \oplus G$ for a fixed set $Z$. By Post's theorem relativized, as in :ref{to="jump-cone-avoidance/sigma2-questions"}, there is a computable function $t$ such that for every set $G$, "$\Phi^{(Z \oplus G)'}_e(x)\converge = v$" holds if and only if the $\Sigma^0_2$ sentence
$$
\chi_{e, x, v} = \exists y\ \Phi^{Z \oplus G}_{t(e, x, v)}(y)\diverge
$$
holds. These sentences are used throughout the course.

:::definition{#def-jump-merging}
A forcing question for $\Sigma^0_2$ sentences is **merging** if for every condition $c$ and all $\Sigma^0_2$ sentences $\varphi_0$, $\varphi_1$ with $c \mathrel{?{\nvdash}} \varphi_0$ and $c \mathrel{?{\nvdash}} \varphi_1$, some extension of $c$ forces $\neg\varphi_0$ and $\neg\varphi_1$.
:::

The two negations are $\Pi^0_2$ sentences, forced by density. Merging asks that one condition carry both, so that later extensions cannot satisfy one of $\varphi_0$, $\varphi_1$ while keeping the other false.

:::theorem{#thm-jump-pa-merging}
Let $\mathbb P$ be a notion of forcing with a merging forcing question for $\Sigma^0_2$ sentences that is $\Sigma^0_1(\mathcal M)$-preserving, and let $D$ be a set such that no member of $\mathcal M$ is PA relative to $D'$. For every sufficiently generic set $G$, $(Z \oplus G)'$ is not PA relative to $D'$.
:::

:::proof{of=thm-jump-pa-merging}
For each $e$, let $E_e$ be the set of conditions $d$ for which there is $x$ such that either $J^{D'}(x)$ is defined and $d \Vdash \chi_{e, x, J^{D'}(x)}$, or $d \Vdash \neg\chi_{e, x, 0}$ and $d \Vdash \neg\chi_{e, x, 1}$. We show that $E_e$ is dense. Let $c$ be a condition and $X \in \mathcal M$ as in :ref{#def-jump-question-local}. The set
$$
U = \{ (x, v) \in \nat \times \{0, 1\} : c \mathrel{?{\vdash}} \chi_{e, x, v} \}
$$
is $\Sigma^0_1(X)$.

1. If $(x, J^{D'}(x)) \in U$ for some $x$ with $J^{D'}(x)$ defined, property 1 gives an extension in $E_e$.
2. If $(x, 0), (x, 1) \notin U$ for some $x$, merging gives an extension in $E_e$.
3. Otherwise, let $g(x)$ be the second coordinate of the first pair with first coordinate $x$ in an $X$-computable enumeration of $U$. It is total since case 2 fails, and $g(x) \neq J^{D'}(x)$ whenever $J^{D'}(x)$ is defined since case 1 fails. So $X$ is PA relative to $D'$, which is excluded.

Let $F$ be a $2$-generic filter (:ref{#def-n-generic-notion}) meeting every $E_e$. By :ref{#thm-forcing-truth}, the sentences forced by its conditions hold for $G_F$. For each $e$ there is $x$ such that $\Phi^{(Z \oplus G_F)'}_e(x)$ converges to $J^{D'}(x)$ or has no value in $\{0, 1\}$; so no $\Phi^{(Z \oplus G_F)'}_e$ is a $\{0, 1\}$-valued function DNC relative to $D'$.
:::

This is :ref{#thm-local-pa-avoidance} with $G'$ in place of $G$ and $D'$ in place of $D$, and :ref{#thm-local-jump-cone} with a merging step in the second case.

:::quiz[the abstract theorem]
In case 2 of the proof of :ref{#thm-jump-pa-merging}, why are two separate extensions, one forcing $\neg\chi_{e, x, 0}$ and one forcing $\neg\chi_{e, x, 1}$, useless?

- [x] On the first, $\Phi^{(Z \oplus G)'}_e(x)$ may still converge to $1$, which is a correct value of a DNC function when $J^{D'}(x)$ is undefined or equal to $0$.
- [ ] Because $\Pi^0_2$ sentences are only forced by density.

  Density is how each negation is forced; the issue is that one negation alone leaves a correct value available.
- [ ] Because the question is not $\Sigma^0_2$-preserving.

  Its definability is used in case 3.

---

In case 3, where is the hypothesis on $\mathcal M$ used?

- [x] The function $g$ is computable in the member $X$ of $\mathcal M$ attached to $c$ and is DNC relative to $D'$, so $X$ would be PA relative to $D'$.
- [ ] To show that $U$ is $\Sigma^0_1(X)$.

  This is the definition of a $\Sigma^0_1(\mathcal M)$-preserving question.
- [ ] To show that $g$ is total.

  Totality comes from the failure of case 2.
:::

:::example{#ex-cohen-jump-pa}
For Cohen forcing, let $\sigma \mathrel{?{\vdash}} \varphi$ if some $\tau \succeq \sigma$ forces $\varphi$ (:ref{#ex-cohen-question}). It is $\Sigma^0_2$-preserving, that is, $\Sigma^0_1(\{\emptyset'\})$-preserving. If $\sigma \mathrel{?{\nvdash}} \varphi_0$ and $\sigma \mathrel{?{\nvdash}} \varphi_1$, then $\sigma$ itself forces $\neg\varphi_0$ and $\neg\varphi_1$ by item 3 of :ref{#prop-forcing-basic}, so the question is merging. Since $\emptyset'$ is not PA relative to $\emptyset'$, :ref{#thm-jump-pa-merging} with $Z = D = \emptyset$ shows that every sufficiently generic set $G$ has a jump that is not PA relative to $\emptyset'$.
:::

The Cohen question is merging for the simplest reason: a negative answer is witnessed by the condition itself. Questions with this property, called **$\Pi^0_2$-extremal** in the monograph, are merging. For Mathias-type forcing, a negative answer about a $\Sigma^0_2$ sentence is witnessed by a restriction of the possible reservoirs, and two restrictions may be incompatible. The next section shows that this is unavoidable for notions of forcing with one reservoir.

::::exercise{#ex-weak-merging-level-two difficulty=2 objective="Lift the weakly merging version of the abstract theorem one jump up, with Liu's lemma relative to $D'$."}
Call a forcing question for $\Sigma^0_2$ sentences **weakly merging** if for every condition $c$ there is $k \geq 2$ such that for all $\Sigma^0_2$ sentences $\varphi_0, \dots, \varphi_{k-1}$ with $c \mathrel{?{\nvdash}} \varphi_s$ for every $s < k$, some extension of $c$ forces $\neg\varphi_s$ and $\neg\varphi_t$ for some $s < t < k$. Let $D$ be a set and $\mathcal M$ a class of sets computing $D'$, none of which is PA relative to $D'$. Show that if the question is weakly merging and $\Sigma^0_1(\mathcal M)$-preserving, then $(Z \oplus G)'$ is not PA relative to $D'$ for every sufficiently generic $G$.

:::solution
For a finite valuation $h$ (:ref{#def-valuation}), let $\varphi_{e, h}$ be the $\Sigma^0_2$ sentence "$\Phi^{(Z \oplus G)'}_e$ is incompatible with $h$", the disjunction of the sentences $\chi_{e, x, 1 - h(x)}$ for $x \in \mathrm{dom}\, h$, written with one existential quantifier. Let $E_e$ be the set of conditions $d$ that force $\varphi_{e, h}$ for some $h$ correct relative to $D'$, or force $\neg\varphi_{e, h}$ and $\neg\varphi_{e, h'}$ for two incompatible valuations $h, h'$. Let $c$ be a condition, $k$ as in the definition and $X \in \mathcal M$ attached to $c$. The set $U$ of valuations $h$ with $c \mathrel{?{\vdash}} \varphi_{e, h}$ is $\Sigma^0_1(X)$. If $U$ contains a correct valuation, property 1 gives an extension in $E_e$. If $k$ pairwise incompatible valuations lie outside $U$, weak merging gives an extension in $E_e$. One of the two cases holds by :ref{#lem-liu-valuations} with $W = X$, $D'$ in place of $D$, and $m$ with $2^m \geq k$; its hypotheses are that $D' \leq_T X$ and that $X$ is not PA relative to $D'$. So $E_e$ is dense. For a $2$-generic filter meeting every $E_e$, :ref{#thm-forcing-truth} shows that each $\Phi^{(Z \oplus G)'}_e$ takes the value $J^{D'}(x)$ at some $x$, or is compatible with two incompatible valuations, hence undefined at some $x$. Unlike :ref{#thm-jump-pa-merging}, the argument needs $D' \leq_T X$, because Liu's lemma does.
:::
::::

## Mathias forcing with one reservoir

:::proposition{#prop-one-reservoir-cohesive}
Let $\mathcal I$ be a Turing ideal and $\mathcal P$ a non-trivial partition regular class. Consider Mathias conditions $(\sigma, X)$ with $X \in \mathcal I \cap \mathcal P$, with Mathias extension. Let $\vec R \in \mathcal I$ be a sequence of sets. For each $n$, the conditions with $X \subseteq R_n$ or $X \subseteq \overline{R_n}$ are dense, and so are the conditions whose stem has at least $n$ elements. Every set that is a member of some condition in each of these dense sets is $\vec R$-cohesive.
:::

:::proof{of=prop-one-reservoir-cohesive}
Let $(\sigma, X)$ be a condition. The sets $X \cap R_n$ and $X \setminus R_n$ cover $X \in \mathcal P$, so one of them is in $\mathcal P$; it is in $\mathcal I$, since $X$ and $R_n$ are. So $(\sigma, X \cap R_n)$ or $(\sigma, X \setminus R_n)$ is an extension in the first dense set. Since $\mathcal P$ is non-trivial, $X$ is infinite; adding an element $x \in X$ above $|\sigma|$ to the stem and replacing $X$ by $X \setminus \{0, \dots, x\}$, which is in $\mathcal P$ by :ref{#lem-partition-regular-basic}, gives the second. A set $G$ that is a member of $(\sigma, X)$ with $X \subseteq R_n$ satisfies $G \setminus \{0, \dots, |\sigma| - 1\} \subseteq R_n$, and it is infinite by the second family.
:::

With $\mathcal I$ the computable sets and $\vec R$ the sequence of :ref{#prop-coh-no-low}, the sets built by such a notion of forcing have jumps PA relative to $\emptyset'$, whatever $\mathcal P$ is. This applies to each side of the forcing of :ref{to="jump-cone-avoidance/pigeonhole-forcing"}, whose reservoirs lie in the core of a cohesive class: that forcing gives non-high sets, but never sets whose jump avoids the PA degrees relative to $\emptyset'$. The obstruction is the operation of splitting the reservoir along a set and keeping a part: a forcing that allows it produces cohesive sets.

::::exercise{#ex-mathias-no-merging difficulty=1 objective="Deduce from the cohesiveness of generic sets that computable Mathias forcing has no merging $\Sigma^0_2$-preserving question."}
Let $\vec R$ be the computable sequence of :ref{#prop-coh-no-low}. Show directly that a sufficiently generic set $G$ for computable Mathias forcing, with conditions $(\sigma, X)$ where $X$ is an infinite computable set, has a jump PA relative to $\emptyset'$, and deduce that computable Mathias forcing has no merging $\Sigma^0_2$-preserving forcing question for $\Sigma^0_2$ sentences.

:::solution
The class of infinite sets is a non-trivial partition regular class, and the computable sets form a Turing ideal containing $\vec R$. By :ref{#prop-one-reservoir-cohesive}, a set $G$ that is a member of some condition in each of the dense sets of the proposition is $\vec R$-cohesive, so $G'$ is PA relative to $\emptyset'$. If the forcing had a merging $\Sigma^0_2$-preserving question, :ref{#thm-jump-pa-merging} with $Z = D = \emptyset$ and $\mathcal M = \{\emptyset'\}$ would give, for a sufficiently generic $G$, a jump that is not PA relative to $\emptyset'$. A filter generic enough for both families of dense sets exists, which is a contradiction.
:::
::::

## Where merging fails

:ref{#prop-one-reservoir-cohesive} can be read on the forcing question. Fix a Scott ideal $\mathcal M$ coded by $M$, and use the classes $\mathcal U_S$ of :ref{to="jump-cone-avoidance/largeness"}. Suppose that conditions are triples $(\sigma, X, S)$, where $\mathcal U_S$ is a large class of possible future reservoirs, and that a negative answer about a $\Sigma^0_2$ sentence $\exists y\ \psi(y)$ is witnessed by adding to $S$ the indices of the classes $\mathcal V_{\tau, \neg\psi(m)}$ of :ref{to="jump-cone-avoidance/pigeonhole-forcing"}: every future reservoir must allow, for every $m$, an extension of each possible stem satisfying $\neg\psi(m)$. Take a computable set $R$ and the two sentences "$G \cap R$ is finite" and "$G \setminus R$ is finite". The first is $\exists y\ \psi(y)$ with $\psi(y)$ the $\Pi^0_1$ formula "no element $z \geq y$ of $G$ is in $R$", and the intersection over $m$ of the classes $\mathcal V_{\tau, \neg\psi(m)}$ is the class $\mathcal L_R$ of sets meeting $R$ infinitely often. A negative answer for the first sentence restricts the class to $\mathcal U_S \cap \mathcal L_R$, for the second to $\mathcal U_S \cap \mathcal L_{\overline R}$. Both can be large; their intersection never is.

:::lemma{#lem-no-two-sides}
For every set $R$, no large class is contained in $\mathcal L_R \cap \mathcal L_{\overline R}$.
:::

:::proof{of=lem-no-two-sides}
A large class contains $R$ or $\overline R$, by the $2$-cover $R, \overline R$ of $\nat$; but $R \notin \mathcal L_{\overline R}$ and $\overline R \notin \mathcal L_R$.
:::

So a single large class can promise that $G \cap R$ is infinite, or that $G \setminus R$ is infinite, but not both: two negative answers cannot be merged, in accordance with :ref{#prop-one-reservoir-cohesive}. The remedy is to keep both classes. Instead of one reservoir in $\mathcal U_S \cap \mathcal L_R \cap \mathcal L_{\overline R}$, the condition keeps a pair of reservoirs $(X_0, X_1)$, and a class of pairs, here $(\mathcal U_S \cap \mathcal L_R) \times (\mathcal U_S \cap \mathcal L_{\overline R})$: the first reservoir will provide elements of $R$ and the second elements of $\overline R$, and the stem may use both. The class of pairs must allow splitting both reservoirs along the same cover. This leads to largeness for classes of tuples of sets, the subject of the next lesson.

## Notes and references

The abstract theorem for merging questions is left as an exercise in the section *Jump PA avoidance* of the chapter *Jump compactness avoidance* of Patey's monograph, where the Cohen example is proved directly; the merging of negative answers by a single condition is called $\Pi^0_2$-merging there. The cohesiveness of generic sets with one reservoir and the analysis of the failure of merging follow the section *Mathias forcing and COH*, and the remedy by products is due to Monin and Patey (2021). The weakly merging version of :ref{#ex-weak-merging-level-two} is the form used for the pigeonhole principle in :ref{to="jump-compactness-avoidance/delta2-jump-pa"}; Liu's lemma is from Liu (2012).

- L. Liu, *RT²₂ does not imply WKL₀*, Journal of Symbolic Logic 77 (2012), 609–620.
- B. Monin and L. Patey, *SRT²₂ does not imply RT²₂ in ω-models*, Advances in Mathematics (2021); arXiv:1905.08427.
- L. Patey, *Lowness and avoidance*, monograph, chapter *Jump compactness avoidance*, sections *Jump PA avoidance* and *Mathias forcing and COH*.

:::::exercises
::::exercise{#ex-chi-sigma2 difficulty=1 objective="Write the convergence of a computation relative to $(Z \oplus G)'$ as a $\Sigma^0_2$ sentence about $Z \oplus G$, as in the sentences $\chi_{e, x, v}$."}
Show directly, without quoting Post's theorem, that the statement "$\Phi^{(Z \oplus G)'}_e(x)\converge = v$" is equivalent to a sentence $\exists y\ \psi(y)$ with $\psi$ a $\Pi^0_1$ formula about $Z \oplus G$, uniformly in $e$, $x$ and $v$.

:::solution
Write $\Phi^\rho_{e, s}(x)\converge = v$ when the computation with oracle $\rho$ halts within $s$ steps with output $v$, querying the oracle only below $|\rho|$. By the use principle, $\Phi^{(Z \oplus G)'}_e(x)\converge = v$ holds if and only if there are a string $\rho$ and a number $s$ with $\Phi^\rho_{e, s}(x)\converge = v$ and $\rho \prec (Z \oplus G)'$: if the computation halts at step $s$, take $\rho = (Z \oplus G)' \upharpoonright s$; conversely a computation with oracle $\rho \prec (Z \oplus G)'$ is a computation with oracle $(Z \oplus G)'$.

The condition $\rho \prec (Z \oplus G)'$ says that $\Phi^{Z \oplus G}_n(n)$ converges for the $n < |\rho|$ with $\rho(n) = 1$ and diverges for the $n < |\rho|$ with $\rho(n) = 0$. It is equivalent to the existence of $t$ such that $\Phi^{Z \oplus G}_{n, t}(n)\converge$ for every $n < |\rho|$ with $\rho(n) = 1$, a condition decidable in $Z \oplus G$, and $\Phi^{Z \oplus G}_{n, t'}(n)\diverge$ for every $t'$ and every $n < |\rho|$ with $\rho(n) = 0$, a $\Pi^0_1$ condition. Grouping $\rho$, $s$ and $t$ into one number $y = \langle \rho, s, t \rangle$, the statement is $\exists y\ \psi(y)$, where $\psi(y)$ is the conjunction of "$\Phi^\rho_{e, s}(x)\converge = v$" (decidable), of the decidable condition on $t$ and of the $\Pi^0_1$ condition on $\rho$. A conjunction of a decidable and a $\Pi^0_1$ formula is $\Pi^0_1$. All the steps are uniform in $e$, $x$ and $v$.
:::
::::

::::exercise{#ex-cohen-jump-pa-relative difficulty=2 objective="Relativize the Cohen example of jump PA avoidance to a parameter $Z$, and apply it to the problem of finding a set not computable in a given one." lessons="effective-forcing/forcing-relation"}
Let $D \leq_T Z$ be sets such that $Z'$ is not PA relative to $D'$. For Cohen forcing and $\Sigma^0_2$ sentences about $Z \oplus G$, let $\sigma \mathrel{?{\vdash}} \varphi$ if some $\tau \succeq \sigma$ forces $\varphi$; as in :ref{#ex-cohen-jump-pa}, this is a forcing question.

1. Show that it is $\Sigma^0_1(\{Z'\})$-preserving and merging, and deduce that $(Z \oplus G)'$ is not PA relative to $D'$ for every sufficiently generic $G$.
2. Deduce that the problem whose instances are all sets, the solutions to $X$ being the sets $Y$ with $Y \not\leq_T X$, admits jump PA avoidance.

:::solution
1. Let $\varphi = \exists y\ \psi(y)$ with $\psi$ a $\Pi^0_1$ formula about $Z \oplus G$. By :ref{#def-forcing-relation}, $\tau \Vdash \varphi$ if $\tau \Vdash \psi(m)$ for some $m$, that is, if every member of $\tau$ satisfies $\psi(m)$. A member of $\tau$ failing $\psi(m)$ satisfies the $\Sigma^0_1$ formula $\neg\psi(m)$, and by the use principle some prefix $\rho \succeq \tau$ of it already makes $\neg\psi(m)$ true with oracle $Z \oplus \rho$; conversely such a $\rho$ gives such a member. So "$\tau \Vdash \psi(m)$" says that no $\rho \succeq \tau$ makes $\neg\psi(m)$ true, a $\Pi^0_1(Z)$ condition on $\tau$ and $m$. The question "$\exists \tau \succeq \sigma\ \exists m\ \tau \Vdash \psi(m)$" is therefore $\Sigma^0_2(Z)$, that is, $\Sigma^0_1(Z')$ by Post's theorem relativized, uniformly in the parameters: the question is $\Sigma^0_1(\{Z'\})$-preserving. It is merging: if $\sigma \mathrel{?{\nvdash}} \varphi_0$ and $\sigma \mathrel{?{\nvdash}} \varphi_1$, no extension of $\sigma$ forces $\varphi_0$ or $\varphi_1$, so $\sigma$ forces $\neg\varphi_0$ and $\neg\varphi_1$ by item 3 of :ref{#prop-forcing-basic}. The only member of $\mathcal M = \{Z'\}$ is not PA relative to $D'$, so :ref{#thm-jump-pa-merging} applies.
2. Let $D \leq_T Z$ with $Z'$ not PA relative to $D'$, and let $X \leq_T Z$. For each $e$, let $F_e$ be the set of strings $\tau$ such that $\Phi^Z_e$ is not total, or $\Phi^Z_e(x)\converge \neq \tau(x)$ for some $x < |\tau|$. It is dense: if $\Phi^Z_e$ is total and $\sigma$ is a string, then $\sigma b \in F_e$ for $b = 1 - \Phi^Z_e(|\sigma|)$. Take a filter generic enough for the proof of :ref{#thm-jump-pa-merging} that also meets every $F_e$; there is one, since only countably many dense sets are involved. Its generic set $G$ has $(Z \oplus G)'$ not PA relative to $D'$, and $G \neq \Phi^Z_e$ for every $e$ such that $\Phi^Z_e$ is total, so $G \not\leq_T Z$, and a fortiori $G \not\leq_T X$.
:::
::::

::::exercise{#ex-two-sides-class difficulty=1 objective="Compare the intersection and the union of the classes $\mathcal L_R$ and $\mathcal L_{\overline R}$ with respect to largeness and partition regularity."}
Let $R$ be infinite and coinfinite.

1. Show that $\mathcal L_R \cap \mathcal L_{\overline R}$ is upward closed, contains $\nat$ and has only infinite members, but is not partition regular.
2. Show that $\mathcal L_R \cup \mathcal L_{\overline R}$ is the class of infinite sets, hence is large.

:::solution
1. If $X \subseteq Y$ and $X \cap R$ and $X \cap \overline R$ are infinite, so are $Y \cap R$ and $Y \cap \overline R$. The set $\nat$ meets $R$ and $\overline R$ infinitely often, since both are infinite. A member meets $R$ infinitely often, so it is infinite. For the $2$-cover $R, \overline R$ of $\nat$, neither part is in the class, since $R \cap \overline R = \emptyset$; so the class is not partition regular, although it contains $\nat$.
2. A set meeting $R$ or $\overline R$ infinitely often is infinite. Conversely, if $X$ is infinite, one of $X \cap R$ and $X \cap \overline R$ is infinite. The class of infinite sets is large: a finite cover of $\nat$ has an infinite part. So the union is large, while the intersection contains no large class (:ref{#lem-no-two-sides}).
:::
::::

::::exercise{#ex-one-reservoir-trivial difficulty=1 objective="See why the partition regular class in the cohesiveness of generic sets with one reservoir must be non-trivial." lessons="jump-cone-avoidance/partition-regularity"}
Let $\mathcal I$ be the class of computable sets and $\mathcal P = \{ X : 0 \in X \}$, a trivial partition regular class. Show that, for Mathias conditions $(\sigma, X)$ with $X \in \mathcal I \cap \mathcal P$, the conditions whose stem has at least $2$ elements are not dense. Where does the proof of :ref{#prop-one-reservoir-cohesive} use non-triviality?

:::solution
The pair $(\varepsilon, \{0\})$ is a condition, since $\{0\}$ is computable and contains $0$. An extension $(\tau, Y)$ has $Y \subseteq \{0\}$ and every element of $\tau$ in $\{0\}$, since the stem $\varepsilon$ has no element and the new elements of $\tau$ come from the reservoir. So $\tau$ has at most one element, and no extension of $(\varepsilon, \{0\})$ has a stem with $2$ elements. The proof of the proposition uses non-triviality to know that the reservoir $X$ is infinite, so that it has an element $x$ above $|\sigma|$ to add to the stem.
:::
::::
:::::
