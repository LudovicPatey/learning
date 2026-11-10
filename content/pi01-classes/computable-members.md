---
title: Computable members
summary: Isolated members of Π⁰₁ classes are computable; countable Π⁰₁ classes have computable members; a non-empty Π⁰₁ class without computable member is perfect; the class of DNC₂ functions.
duration: 35
prerequisites: [trees-and-classes]
---

A non-empty $\Pi^0_1$ class always has a member computable in $\emptyset'$: follow the leftmost extendible node, which $\emptyset'$ can recognize. Does it always have a computable member? This lesson shows that the answer depends on the topology of the class. Isolated members are computable, so countable classes have computable members. But there are non-empty $\Pi^0_1$ classes without computable members, and these classes are necessarily large: they contain a copy of Cantor space.

## The leftmost path

:::proposition{#prop-leftmost-path}
Every non-empty $\Pi^0_1$ class has a member computable in $\emptyset'$, namely its leftmost member.
:::

:::proof{of=prop-leftmost-path}
Let $\mathcal P = [T]$ with $T$ computable. By :ref{#prop-pi01-emptiness}, the set of extendible nodes of $T$ is co-c.e., hence computable in $\emptyset'$. Define $X$ by induction: $X(n) = 0$ if $(X \uh n)\, 0$ is extendible, and $X(n) = 1$ otherwise. Since $X \uh n$ is extendible, one of its two successors is, so every $X \uh n$ is extendible, and $X \in [T]$. The construction asks finitely many questions to $\emptyset'$ at each step. The sequence $X$ is the leftmost path of $T$, that is, the least member of $\mathcal P$ in the lexicographic order.
:::

The proposition is the **Kreisel basis theorem**: the sets computable in $\emptyset'$ form a basis for the $\Pi^0_1$ classes, in the sense that every non-empty $\Pi^0_1$ class has a member among them. The next lesson improves it considerably.

## Isolated members

:::definition{#def-isolated}
A member $X$ of a class $\mathcal P$ is **isolated** if there is a string $\sigma \prec X$ with $[\sigma] \cap \mathcal P = \{ X \}$. A non-empty closed class without isolated members is **perfect**.
:::

:::proposition{#prop-isolated-computable}
Every isolated member of a $\Pi^0_1$ class is computable.
:::

:::proof{of=prop-isolated-computable}
Let $\mathcal P = [T]$ with $T$ computable, and $\sigma \prec X$ with $[\sigma] \cap \mathcal P = \{ X \}$. We compute $X(n)$ for $n \geq |\sigma|$ by induction, the bits below $|\sigma|$ being given by $\sigma$. Suppose $\tau = X \uh n$ is known, with $n \geq |\sigma|$. The two strings $\tau 0$ and $\tau 1$ extend $\sigma$; the one that is a prefix of $X$ is extendible, and the other one is not, since a path through it would be a second member of $[\sigma] \cap \mathcal P$. Non-extendibility is a $\Sigma^0_1$ property (:ref{#prop-pi01-emptiness}), so a search eventually finds which of $\tau 0$ and $\tau 1$ is not extendible, and never wrongly reports the other one. Set $X(n)$ to the other bit.
:::

:::theorem{#thm-perfect-continuum}
Let $\mathcal P$ be a perfect class. Then there is an injective map $Z \mapsto X_Z$ from $\cs$ into $\mathcal P$. In particular, $\mathcal P$ has the cardinality of the continuum.
:::

:::proof{of=thm-perfect-continuum}
Let $\mathcal P = [T]$, with $T$ the tree of prefixes of members of $\mathcal P$, so that every node of $T$ is extendible. We define strings $\sigma_\rho \in T$, for $\rho \in \bstr$, such that $\sigma_{\rho 0}$ and $\sigma_{\rho 1}$ are incompatible extensions of $\sigma_\rho$. Let $\sigma_\varepsilon = \varepsilon$. Given $\sigma_\rho \in T$, let $X$ be a member of $\mathcal P$ through $\sigma_\rho$. Since $X$ is not isolated, $[\sigma_\rho] \cap \mathcal P$ contains a member $Y \neq X$. If $n$ is the first position where they differ, the strings $X \uh (n+1)$ and $Y \uh (n+1)$ are incompatible extensions of $\sigma_\rho$ in $T$. Let $\sigma_{\rho 0}, \sigma_{\rho 1}$ be the first pair of incompatible extensions of $\sigma_\rho$ in $T$, in a fixed enumeration of pairs of strings; this avoids any arbitrary choice.

For $Z \in \cs$, the classes $[\sigma_{Z \uh k}] \cap \mathcal P$ form a decreasing sequence of non-empty closed classes, so their intersection is non-empty (:ref{#prop-cantor-compact}), and it contains a single sequence $X_Z$, since the lengths of the strings $\sigma_{Z \uh k}$ increase. If $Z \neq Z'$ first differ at position $k$, then $X_Z$ and $X_{Z'}$ extend the incompatible strings $\sigma_{(Z \uh k) 0}$ and $\sigma_{(Z \uh k) 1}$, so they are different.
:::

:::corollary{#cor-countable-computable}
1. Every countable non-empty $\Pi^0_1$ class has a computable member; in particular, every member of a finite $\Pi^0_1$ class is computable.
2. A non-empty $\Pi^0_1$ class without computable member is perfect, and has the cardinality of the continuum.
:::

:::proof{of=cor-countable-computable}
1. A countable non-empty closed class is not perfect, by :ref{#thm-perfect-continuum}, so it has an isolated member, which is computable by :ref{#prop-isolated-computable}. In a finite class, every member is isolated.
2. If the class had an isolated member, this member would be computable. So the class is perfect, and :ref{#thm-perfect-continuum} applies.
:::

:::quiz[isolated members]
In the proof of :ref{#prop-isolated-computable}, why does the search for a non-extendible successor of $\tau = X \uh n$ always succeed?

- [x] Because one of the two successors is not extendible: otherwise $[\sigma] \cap \mathcal P$ would contain a member other than $X$, through the successor that is not a prefix of $X$.
- [ ] Because $T$ is computable.

  Computability of $T$ makes non-extendibility $\Sigma^0_1$; the existence of a non-extendible successor comes from isolation.
- [ ] Because $X$ is the leftmost path.

  An isolated member need not be the leftmost path.

---

Why does the proof of :ref{#thm-perfect-continuum} not apply to a class with an isolated member $X$?

- [x] Above a prefix isolating $X$, there is no pair of incompatible extendible extensions, so the splitting cannot continue there.

  The construction needs two different members through each node it uses.
- [ ] Because the class is then countable.

  A class with an isolated member can still be uncountable: the isolated member may be the only one in some cylinder, while others are perfect.
- [ ] Because the map would not be injective.

  Injectivity comes from the incompatibility of the strings chosen at each splitting; the problem is that the splitting cannot be found above an isolating prefix.
:::

## A Π⁰₁ class without computable members

:::theorem{#thm-dnc2-no-computable}
The class $\mathrm{DNC}_2 = \{ X \in \cs : X(e) \neq \Phi_e(e) \text{ for every } e \text{ with } \Phi_e(e)\converge \}$ is a non-empty $\Pi^0_1$ class without computable member. It is the class of sets separating $A = \{ e : \Phi_e(e)\converge = 0 \}$ from $B = \{ e : \Phi_e(e)\converge = 1 \}$.
:::

:::proof{of=thm-dnc2-no-computable}
A set $X$ satisfies $X(e) \neq \Phi_e(e)$ for all $e$ with $\Phi_e(e)\converge$ if and only if $X(e) = 1$ for $e \in A$ and $X(e) = 0$ for $e \in B$, since $X(e)$ can only equal $0$ or $1$; so $\mathrm{DNC}_2$ is the class of separating sets $\mathcal S(A, B)$, which is $\Pi^0_1$ by :ref{#ex-pi01-classes}. It is non-empty: $A$ itself separates $A$ from $B$.

Suppose $X \in \mathrm{DNC}_2$ is computable, and let $c$ be an index of its characteristic function, so that $\Phi_c$ is total with values in $\{0, 1\}$. Then $\Phi_c(c)\converge = X(c)$, contradicting $X(c) \neq \Phi_c(c)$.
:::

By :ref{#cor-countable-computable}, the class $\mathrm{DNC}_2$ is perfect and has continuum many members, none of them computable. The class plays a central role in the next lessons: its members are exactly the $\{0, 1\}$-valued functions that escape every computable function on the diagonal, and their degrees are the **PA degrees**.

:::quiz[the class DNC₂]
Why is the class $\mathrm{DNC}_2$ non-empty, although none of its members is computable?

- [x] Because the c.e. set $A = \{ e : \Phi_e(e)\converge = 0 \}$ is a member: it has the value $1$ on $A$ and $0$ on $B$.

  A member may be c.e. without being computable; $A$ is c.e. and not computable.
- [ ] By weak König's lemma applied to a finite tree.

  Weak König's lemma applies to infinite trees; here an explicit member is available.
- [ ] Because every $\Pi^0_1$ class is non-empty.

  The empty class is a $\Pi^0_1$ class.
:::

## Exercises

::::exercise{difficulty=1}
Give a $\Pi^0_1$ class whose leftmost member is $\emptyset'$, and deduce that the leftmost member of a $\Pi^0_1$ class may compute $\emptyset'$.

:::solution
The class $\{ X : \emptyset' \subseteq X \}$ is $\Pi^0_1$: $X$ is outside it if and only if some $n$ enters $\emptyset'$ with $X(n) = 0$, a $\Sigma^0_1$ condition on prefixes. Its least member in the lexicographic order has the bit $0$ wherever possible, that is, outside $\emptyset'$, so it is $\emptyset'$.
:::
::::

::::exercise{difficulty=2}
Let $(T_e)$ be an enumeration of the computable trees, given by indices. Show that the set of $e$ such that $[T_e]$ has a computable member is $\Sigma^0_3$.

:::solution
$[T_e]$ has a computable member if and only if there is $i$ such that $\Phi_i$ is total with values in $\{0, 1\}$, and every prefix of the sequence $\Phi_i$ belongs to $T_e$. The first condition is $\Pi^0_2$. Given it, the second is equivalent to "for all $n$ and $s$, if $\Phi_i(0), \dots, \Phi_i(n-1)$ converge at stage $s$, the string they form belongs to $T_e$", which is $\Pi^0_1$. So the condition on $(e, i)$ is $\Pi^0_2$, and its projection over $i$ is $\Sigma^0_3$.
:::
::::

## Notes and references

The basis theorem for $\emptyset'$ is due to Kreisel (1953). The computability of isolated members and the study of the Cantor–Bendixson rank of $\Pi^0_1$ classes go back to Cenzer, Clote, Smith, Soare and Wainer (1986). Kleene constructed the first non-empty $\Pi^0_1$ class without computable member.

- G. Kreisel, *A variant to Hilbert's theory of the foundations of arithmetic*, British Journal for the Philosophy of Science 4 (1953), 107–129.
- C. G. Jockusch and R. I. Soare, *Π⁰₁ classes and degrees of theories*, Transactions of the American Mathematical Society 173 (1972), 33–56.
- D. Cenzer and J. B. Remmel, *Π⁰₁ classes in mathematics*, in *Handbook of Recursive Mathematics*, Volume 2, Studies in Logic 139, North-Holland, 1998, 623–821.
