---
title: Continuous functions and computable metric spaces
summary: Names of continuous functions on the unit interval by rational rectangles; effective compactness of the unit interval gives a computable modulus of uniform continuity and a computable maximum value; computable metric spaces, and the space of continuous functions with the uniform metric.
duration: 45
prerequisites: [real-functions, pi01-classes/trees-and-classes]
---

To treat problems whose instances are functions, such as the intermediate value theorem, we need names for continuous functions themselves. On $[0, 1]$, two natural choices exist: a list of rational rectangles that the graph does not leave, which is a code of reverse mathematics, and a sequence of rational polygons converging uniformly at a fixed rate, which is a Cauchy name in the metric space of continuous functions. This lesson proves that the two are equivalent. The proof uses the **effective compactness** of $[0, 1]$: a finite subcover of a computably enumerated open cover can be found by search, and from it a modulus of uniform continuity and the maximum value of the function are computed. The last part introduces computable metric spaces, the general framework in which Cauchy names make sense.

We write $C[0, 1]$ for the set of continuous functions $f : [0, 1] \to \mathbb R$.

## Rectangle names

:::definition{#def-rectangle-name}
A **rectangle** is a quadruple $(a, r, b, s)$ of rationals with $r, s > 0$; it is **valid** for $f \in C[0, 1]$ if $|f(y) - b| \leq s$ for every $y \in [0, 1]$ with $|y - a| < r$. The **rectangle representation** $\delta_\square$ of $C[0, 1]$ is defined by $\delta_\square(p) = f$ if every $p(n)$ codes a rectangle valid for $f$, and for every $x \in [0, 1]$ and every $\varepsilon > 0$ some listed rectangle $(a, r, b, s)$ satisfies $|x - a| < r$ and $s < \varepsilon$.
:::

A name lists, possibly with repetitions, enough correct information to determine $f$ at every point to any precision. Every $f \in C[0, 1]$ has names, for instance a list of all rectangles valid for $f$, which satisfies the second condition by continuity. The set listed by a name, with the position in the list as index, is a code of $f$ in the sense of :ref{#def-continuous-code}: validity of two rectangles implies their consistency. Conversely, every rectangle of a code of $f$ is valid for $f$, by the definition of the value.

:::theorem{#thm-rectangle-computable}
1. The evaluation $(f, x) \mapsto f(x)$, for $f \in C[0, 1]$ and $x \in [0, 1]$, is $([\delta_\square, \rho], \rho)$-computable.
2. A function $f \in C[0, 1]$ is computable if and only if it has a computable $\delta_\square$-name. Moreover, a $\delta_\square$-name of $f$ is computed from an index of a Turing functional realizing $f$, uniformly in the index.
:::

:::proof{of=thm-rectangle-computable}
1. Given a $\delta_\square$-name of $f$, a Cauchy name $(q_l)$ of $x \in [0, 1]$ and $k$, search for a listed rectangle $(a, r, b, s)$ and an $l$ with $|q_l - a| + 2^{-l} < r$ and $s \leq 2^{-k}$, and output $b$. As in :ref{#thm-real-continuous-relative}, any pair found gives $|x - a| < r$, hence $|f(x) - b| \leq 2^{-k}$, and the search terminates: the name lists some $(a, r, b, s)$ with $|x - a| < r$ and $s < 2^{-k}$, and $|q_l - a| + 2^{-l} < r$ holds for $l$ large. The outputs form a Cauchy name of $f(x)$ by :ref{#lem-cauchy-variants}.

2. If $f$ has a computable name, then fixing it in (1) gives a computable realizer of $f$. Conversely, let $\Phi_e$ realize $f$. Enumerate the triples $(\sigma, k, r)$ such that $\sigma$ is a valid prefix with $U_\sigma \cap [0, 1] \neq \emptyset$ and $\Phi^\sigma_e(k+1)\converge = r$; this is c.e. by :ref{#lem-type2-finite}. For each such triple, with $U_\sigma = (c - d, c + d)$, list the rectangle $(c, d, r, 2^{-k-1})$.

*Validity.* If $y \in [0, 1] \cap U_\sigma$, then $y$ has a name $q$ extending $\sigma$ (:ref{#lem-prefix-interval}), and $\Phi^q_e(k+1) = r$ by :ref{#lem-type2-finite}. Since $\Phi^q_e$ is a Cauchy name of $f(y)$, $|f(y) - r| \leq 2^{-k-1}$.

*Totality.* Let $x \in [0, 1]$ and $\varepsilon > 0$, and choose $k$ with $2^{-k-1} < \varepsilon$. Let $p$ be a name of $x$ with $x \in U_{p \uh m}$ for every $m$ (:ref{#lem-prefix-interval}). Then $\Phi^p_e(k+1)$ converges, to some $r$, and $\Phi^{p \uh m}_e(k+1)\converge = r$ for some $m$. The triple $(p \uh m, k, r)$ is enumerated, and its rectangle has $x$ inside its interval and height $2^{-k-1} < \varepsilon$.
:::

## Effective compactness of the unit interval

Classically, every open cover of $[0, 1]$ has a finite subcover (Heine–Borel). When the cover is enumerated by an algorithm, the finite subcover can be found by search, because whether finitely many rational intervals cover $[0, 1]$ is decidable. This is the analogue of the effective compactness of Cantor space, where the emptiness of a $\Pi^0_1$ class is $\Sigma^0_1$ (:ref{#prop-pi01-emptiness}).

:::lemma{#lem-effective-heine-borel}
1. Given finitely many open intervals $(c_i, d_i)$ with rational endpoints and a closed interval $[c, d]$ with rational endpoints, one decides whether $[c, d] \subseteq \bigcup_i (c_i, d_i)$.
2. There is an algorithm which, given a sequence $J_0, J_1, \dots$ of rational open intervals covering $[0, 1]$, finds $n$ such that $J_0, \dots, J_{n-1}$ cover $[0, 1]$; it is uniform in the sequence, given as an oracle.
:::

:::proof{of=lem-effective-heine-borel}
1. Sort the intervals by left endpoint and sweep: let $x = c$; while some interval $(c_i, d_i)$ with $c_i < x < d_i$ exists, replace $x$ by the largest such $d_i$; the interval $[c, d]$ is covered if and only if $x$ eventually exceeds $d$. Each step increases $x$ to a right endpoint, so there are at most as many steps as intervals. If the sweep stops at $x \leq d$, the point $x$ is not covered.
2. By the Heine–Borel theorem, some finite initial segment covers $[0, 1]$; test $n = 0, 1, 2, \dots$ with (1).
:::

The algorithm is effective, but its correctness rests on a classical theorem with a non-effective proof. Reverse mathematics, in contrast, measures the strength of the Heine–Borel theorem used here: it is equivalent to weak König's lemma over $\mathsf{RCA}_0$ (:ref{to="big-five/separation-heine-borel"}).

:::theorem{#thm-modulus-max}
There is an algorithm which, given a $\delta_\square$-name of $f \in C[0, 1]$, computes
1. a **modulus of uniform continuity** of $f$: a function $\mu : \nat \to \nat$ such that $|f(x) - f(y)| \leq 2^{-k}$ for all $x, y \in [0, 1]$ with $|x - y| \leq 2^{-\mu(k)}$;
2. a Cauchy name of $\max_{x \in [0, 1]} f(x)$.
:::

The idea for (1): the rectangles of height below $2^{-k-1}$ cover $[0, 1]$, so finitely many of them do, and two points closer than the **Lebesgue number** of this finite cover lie in a common rectangle (:ref{#fig-lebesgue-number}). The Lebesgue number of finitely many rational intervals is computable.

:::figure[A finite cover of $[0, 1]$ by open intervals $J_i = (a_i - r_i, a_i + r_i)$, and the function $m(x) = \max_i (r_i - |x - a_i|)$, the depth of $x$ inside the best interval containing it. Its minimum $\delta$ on $[0, 1]$ is a Lebesgue number: an interval of length less than $\delta$ around $x$ fits inside one of the $J_i$.]{#fig-lebesgue-number}
<svg class="fig" viewBox="0 0 640 270" width="640" role="img" aria-label="Four open intervals covering the unit interval, and the function giving the distance from a point to the boundary of the best interval containing it; its minimum is a Lebesgue number of the cover"><line x1="30.0" y1="30" x2="210.0" y2="30" class="accent-stroke" stroke-width="2.5"/><circle cx="30.0" cy="30" r="3.5" class="node"/><circle cx="210.0" cy="30" r="3.5" class="node"/><text x="120.0" y="22.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">0</tspan></text><line x1="180.0" y1="52" x2="320.0" y2="52" class="accent-stroke" stroke-width="2.5"/><circle cx="180.0" cy="52" r="3.5" class="node"/><circle cx="320.0" cy="52" r="3.5" class="node"/><text x="250.0" y="44.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">1</tspan></text><line x1="280.0" y1="30" x2="440.0" y2="30" class="accent-stroke" stroke-width="2.5"/><circle cx="280.0" cy="30" r="3.5" class="node"/><circle cx="440.0" cy="30" r="3.5" class="node"/><text x="360.0" y="22.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">2</tspan></text><line x1="390.0" y1="52" x2="590.0" y2="52" class="accent-stroke" stroke-width="2.5"/><circle cx="390.0" cy="52" r="3.5" class="node"/><circle cx="590.0" cy="52" r="3.5" class="node"/><text x="490.0" y="44.0" text-anchor="middle" class="math" font-size="13">J<tspan class="mrm" font-size="8" dy="4">3</tspan></text><line x1="60" y1="210" x2="590" y2="210" class="axis"/><line x1="70" y1="210" x2="70" y2="90" class="axis"/><polyline points="70.0,170.0 71.2,168.8 72.5,167.5 73.8,166.2 75.0,165.0 76.2,163.8 77.5,162.5 78.8,161.2 80.0,160.0 81.2,158.8 82.5,157.5 83.8,156.2 85.0,155.0 86.2,153.8 87.5,152.5 88.8,151.2 90.0,150.0 91.2,148.8 92.5,147.5 93.8,146.2 95.0,145.0 96.2,143.8 97.5,142.5 98.8,141.2 100.0,140.0 101.2,138.8 102.5,137.5 103.8,136.2 105.0,135.0 106.2,133.8 107.5,132.5 108.8,131.2 110.0,130.0 111.2,128.8 112.5,127.5 113.8,126.3 115.0,125.0 116.2,123.8 117.5,122.5 118.8,121.2 120.0,120.0 121.2,121.2 122.5,122.5 123.8,123.8 125.0,125.0 126.2,126.3 127.5,127.5 128.8,128.8 130.0,130.0 131.2,131.2 132.5,132.5 133.8,133.8 135.0,135.0 136.2,136.2 137.5,137.5 138.8,138.8 140.0,140.0 141.2,141.2 142.5,142.5 143.8,143.8 145.0,145.0 146.2,146.2 147.5,147.5 148.8,148.8 150.0,150.0 151.2,151.2 152.5,152.5 153.8,153.8 155.0,155.0 156.2,156.2 157.5,157.5 158.8,158.8 160.0,160.0 161.2,161.2 162.5,162.5 163.8,163.8 165.0,165.0 166.2,166.2 167.5,167.5 168.8,168.8 170.0,170.0 171.2,171.2 172.5,172.5 173.8,173.8 175.0,175.0 176.2,176.2 177.5,177.5 178.8,178.8 180.0,180.0 181.2,181.2 182.5,182.5 183.8,183.8 185.0,185.0 186.2,186.2 187.5,187.5 188.8,188.8 190.0,190.0 191.2,191.2 192.5,192.5 193.8,193.8 195.0,195.0 196.2,193.8 197.5,192.5 198.8,191.2 200.0,190.0 201.2,188.7 202.5,187.5 203.8,186.2 205.0,185.0 206.2,183.7 207.5,182.5 208.8,181.2 210.0,180.0 211.2,178.8 212.5,177.5 213.8,176.2 215.0,175.0 216.2,173.8 217.5,172.5 218.8,171.2 220.0,170.0 221.2,168.8 222.5,167.5 223.8,166.2 225.0,165.0 226.2,163.8 227.5,162.5 228.8,161.2 230.0,160.0 231.2,158.8 232.5,157.5 233.8,156.2 235.0,155.0 236.2,153.7 237.5,152.5 238.8,151.2 240.0,150.0 241.2,148.7 242.5,147.5 243.8,146.2 245.0,145.0 246.2,143.8 247.5,142.5 248.8,141.2 250.0,140.0 251.2,141.2 252.5,142.5 253.8,143.8 255.0,145.0 256.2,146.2 257.5,147.5 258.8,148.8 260.0,150.0 261.2,151.2 262.5,152.5 263.8,153.8 265.0,155.0 266.2,156.2 267.5,157.5 268.8,158.8 270.0,160.0 271.2,161.2 272.5,162.5 273.8,163.8 275.0,165.0 276.2,166.2 277.5,167.5 278.8,168.8 280.0,170.0 281.2,171.2 282.5,172.5 283.8,173.8 285.0,175.0 286.2,176.2 287.5,177.5 288.8,178.8 290.0,180.0 291.2,181.2 292.5,182.5 293.8,183.8 295.0,185.0 296.2,186.2 297.5,187.5 298.8,188.8 300.0,190.0 301.2,188.7 302.5,187.5 303.8,186.2 305.0,185.0 306.2,183.8 307.5,182.5 308.8,181.2 310.0,180.0 311.2,178.8 312.5,177.5 313.8,176.2 315.0,175.0 316.2,173.7 317.5,172.5 318.8,171.2 320.0,170.0 321.2,168.8 322.5,167.5 323.8,166.2 325.0,165.0 326.2,163.8 327.5,162.5 328.8,161.2 330.0,160.0 331.2,158.8 332.5,157.5 333.8,156.2 335.0,155.0 336.2,153.8 337.5,152.5 338.8,151.2 340.0,150.0 341.2,148.8 342.5,147.5 343.8,146.2 345.0,145.0 346.2,143.8 347.5,142.5 348.8,141.2 350.0,140.0 351.2,138.7 352.5,137.5 353.8,136.2 355.0,135.0 356.2,133.7 357.5,132.5 358.8,131.2 360.0,130.0 361.2,131.3 362.5,132.5 363.8,133.8 365.0,135.0 366.2,136.3 367.5,137.5 368.8,138.8 370.0,140.0 371.2,141.3 372.5,142.5 373.8,143.8 375.0,145.0 376.2,146.3 377.5,147.5 378.8,148.8 380.0,150.0 381.2,151.3 382.5,152.5 383.8,153.8 385.0,155.0 386.2,156.2 387.5,157.5 388.8,158.8 390.0,160.0 391.2,161.2 392.5,162.5 393.8,163.8 395.0,165.0 396.2,166.2 397.5,167.5 398.8,168.8 400.0,170.0 401.2,171.2 402.5,172.5 403.8,173.8 405.0,175.0 406.2,176.2 407.5,177.5 408.8,178.8 410.0,180.0 411.2,181.3 412.5,182.5 413.8,183.8 415.0,185.0 416.2,183.7 417.5,182.5 418.8,181.2 420.0,180.0 421.2,178.7 422.5,177.5 423.8,176.2 425.0,175.0 426.2,173.7 427.5,172.5 428.8,171.2 430.0,170.0 431.2,168.7 432.5,167.5 433.8,166.2 435.0,165.0 436.2,163.7 437.5,162.5 438.8,161.2 440.0,160.0 441.2,158.7 442.5,157.5 443.8,156.2 445.0,155.0 446.2,153.8 447.5,152.5 448.8,151.2 450.0,150.0 451.2,148.8 452.5,147.5 453.8,146.2 455.0,145.0 456.2,143.8 457.5,142.5 458.8,141.2 460.0,140.0 461.2,138.8 462.5,137.5 463.8,136.2 465.0,135.0 466.2,133.8 467.5,132.5 468.8,131.2 470.0,130.0 471.2,128.8 472.5,127.5 473.8,126.2 475.0,125.0 476.2,123.7 477.5,122.5 478.8,121.2 480.0,120.0 481.2,118.7 482.5,117.5 483.8,116.2 485.0,115.0 486.2,113.7 487.5,112.5 488.8,111.2 490.0,110.0 491.2,111.3 492.5,112.5 493.8,113.8 495.0,115.0 496.2,116.3 497.5,117.5 498.8,118.8 500.0,120.0 501.2,121.3 502.5,122.5 503.8,123.8 505.0,125.0 506.2,126.3 507.5,127.5 508.8,128.8 510.0,130.0 511.2,131.2 512.5,132.5 513.8,133.8 515.0,135.0 516.2,136.2 517.5,137.5 518.8,138.8 520.0,140.0 521.2,141.2 522.5,142.5 523.8,143.8 525.0,145.0 526.2,146.2 527.5,147.5 528.8,148.8 530.0,150.0 531.2,151.2 532.5,152.5 533.8,153.8 535.0,155.0 536.2,156.2 537.5,157.5 538.8,158.8 540.0,160.0 541.2,161.2 542.5,162.5 543.8,163.8 545.0,165.0 546.2,166.2 547.5,167.5 548.8,168.8 550.0,170.0 551.2,171.3 552.5,172.5 553.8,173.8 555.0,175.0 556.2,176.3 557.5,177.5 558.8,178.8 560.0,180.0 561.2,181.3 562.5,182.5 563.8,183.8 565.0,185.0 566.2,186.3 567.5,187.5 568.8,188.8 570.0,190.0" class="ink-stroke" stroke-width="1.6"/><line x1="70" y1="195.0" x2="570" y2="195.0" class="muted-stroke" stroke-dasharray="4 3"/><circle cx="195.0" cy="195.0" r="3.5" class="accent-fill"/><text x="62.0" y="200.0" text-anchor="end" class="math" font-size="14">δ</text><text x="70.0" y="228.0" text-anchor="middle" class="mrm" font-size="12">0</text><text x="570.0" y="228.0" text-anchor="middle" class="mrm" font-size="12">1</text><text x="320.0" y="250.0" text-anchor="middle" class="label">m(x) = max over i of (r − |x − a|) for the intervals (a − r, a + r) of the cover</text></svg>
:::

:::proof{of=thm-modulus-max}
1. Fix $k$. The intervals $(a - r, a + r)$ of the listed rectangles $(a, r, b, s)$ with $s < 2^{-k-1}$ form a sequence of rational open intervals, computable from the name, which covers $[0, 1]$ by the second condition of :ref{#def-rectangle-name}. By :ref{#lem-effective-heine-borel}, compute finitely many of them, $(a_i - r_i, a_i + r_i)$ for $i < N$, covering $[0, 1]$. The function $m(x) = \max_{i < N} (r_i - |x - a_i|)$ is piecewise linear, with rational breakpoints that are computed from the $a_i$ and $r_i$, and it is positive on $[0, 1]$, since every point lies in one of the intervals. Its minimum $\delta$ on $[0, 1]$ is attained at $0$, at $1$ or at a breakpoint, so $\delta$ is a positive rational, computed by evaluating $m$ at finitely many points. Let $\mu(k)$ be least with $2^{-\mu(k)} < \delta$. If $|x - y| \leq 2^{-\mu(k)}$, choose $i$ with $r_i - |x - a_i| = m(x) \geq \delta$; then $|y - a_i| \leq |y - x| + |x - a_i| < \delta + r_i - \delta = r_i$. So $x$ and $y$ both lie in the interval of a rectangle $(a_i, r_i, b_i, s_i)$, and $|f(x) - f(y)| \leq 2 s_i < 2^{-k}$.

2. Let $M = \max f$, which exists since $[0, 1]$ is compact. Given $k$, let $N = 2^{\mu(k+1)}$, and compute rationals $c_j$ with $|c_j - f(j/N)| \leq 2^{-k-1}$ for $j \leq N$, by (1) of :ref{#thm-rectangle-computable}. Let $r_k = \max_{j \leq N} c_j$. Every $x \in [0, 1]$ is within $1/N$ of some $j/N$, so $f(x) \leq f(j/N) + 2^{-k-1} \leq c_j + 2^{-k}$; hence $M \leq r_k + 2^{-k}$. And $r_k \leq \max_j f(j/N) + 2^{-k-1} \leq M + 2^{-k}$. So $|r_k - M| \leq 2^{-k}$, and :ref{#lem-cauchy-variants} gives a Cauchy name.
:::

:::quiz[the modulus of uniform continuity]
In the proof of :ref{#thm-modulus-max} (1), why is a finite subcover needed, rather than the whole list of rectangles?

- [x] Because the Lebesgue number of the whole cover may be $0$ or impossible to compute; for finitely many intervals, the function $m$ is piecewise linear with finitely many breakpoints, and its positive minimum is computed exactly.
- [ ] Because the list of rectangles is not computable from the name.

  The list is the name itself.
- [ ] Because $f$ is not uniformly continuous on an infinite cover.

  Uniform continuity is a property of $f$ on $[0, 1]$, not of a cover; it is what the finite cover makes computable.

---

In the same proof, where is the choice $s < 2^{-k-1}$ used?

- [x] In the last step: two points of a common rectangle have values within $2 s_i < 2^{-k}$ of each other.
- [ ] To ensure that the rectangles cover $[0, 1]$.

  Any positive bound on the heights gives a cover, by the second condition of the definition; the specific bound gives the precision.
- [ ] To compute $\delta$.

  $\delta$ depends only on the intervals, not on the heights.
:::

Consequently, $f \in C[0, 1]$ is computable if and only if $q \mapsto f(q)$ is computable on $\mathbb Q \cap [0, 1]$ and $f$ has a computable modulus of uniform continuity: for the converse, approximate $f(x)$ within $2^{-k}$ by $f(q)$ for a rational $q \in [0, 1]$ within $2^{-\mu(k+1)}$ of $x$. This was Pour-El and Richards' definition of computable functions on compact intervals.

## Computable metric spaces

The Cauchy representation of $\mathbb R$ uses only a dense sequence, the rationals, and the computability of the distances between its terms. The same construction applies to any separable metric space.

:::definition{#def-computable-metric-space}
A **computable metric space** is a triple $(X, d, \alpha)$ where $(X, d)$ is a complete metric space and $\alpha : \nat \to X$ is a sequence with dense range such that the double sequence of reals $(d(\alpha(i), \alpha(j)))_{i,j}$ is computable. Its **Cauchy representation** $\delta_X$ is defined by $\delta_X(p) = x$ if $d(\alpha(p(k)), \alpha(p(l))) \leq 2^{-k}$ for all $k \leq l$ and $x = \lim_k \alpha(p(k))$. The points $\alpha(i)$ are the **rational points**, and the open balls $B(\alpha(i), r)$ with $r$ rational are the **rational balls**.
:::

:::example{#ex-computable-metric-spaces}
1. $\mathbb R$ with $|x - y|$ and an enumeration of $\mathbb Q$: the Cauchy representation is $\rho$. The same holds for $[0, 1]$ with an enumeration of $\mathbb Q \cap [0, 1]$, and for $\mathbb R^n$ with the Euclidean metric and rational vectors, whose Cauchy representation is equivalent to $\rho^n$.
2. Cantor space with $d(X, Y) = 2^{-n}$, $n$ least with $X(n) \neq Y(n)$, and $\alpha(i) = \sigma_i 0^\infty$, where $\sigma_i$ is the $i$-th binary string: the distances are rationals computed from $i$ and $j$. Its Cauchy representation is equivalent to the identity (exercise). Baire space is similar.
3. $C[0, 1]$ with the uniform metric $d(f, g) = \max_{x \in [0, 1]} |f(x) - g(x)|$, and an enumeration of the **rational polygons**: the continuous functions that are piecewise linear with finitely many rational breakpoints in $[0, 1]$, including $0$ and $1$, and rational values at the breakpoints. They are dense, since every continuous function on $[0, 1]$ is uniformly continuous; the distance between two rational polygons is a rational, the maximum of their difference over the union of their breakpoints, where the piecewise linear difference attains its extrema. We write $\delta_C$ for the Cauchy representation of $C[0, 1]$.
:::

In a computable metric space, the computable points are the limits of computable sequences of rational points converging at the rate $2^{-k}$, and the proof of :ref{#lem-cauchy-variants} shows again that a sequence of rational points with $d(\alpha(p(k)), x) \leq 2^{-k}$ can be turned into a name of $x$. A $\delta_C$-name of $f$ is a sequence of rational polygons $P_k$ with $d(P_k, P_l) \leq 2^{-k}$ for $k \leq l$, converging uniformly to $f$.

:::theorem{#thm-cauchy-rectangle}
$\delta_C \equiv \delta_\square$ on $C[0, 1]$.
:::

:::proof{of=thm-cauchy-rectangle}
($\delta_C \leq \delta_\square$) Let $(P_k)$ be a $\delta_C$-name of $f$, so that $|f(y) - P_k(y)| \leq 2^{-k}$ for every $y$. For every $k$ and every rational $a \in [0, 1]$ and rational $r > 0$, compute the minimum $c$ and the maximum $d$ of $P_k$ on $[a - r, a + r] \cap [0, 1]$, attained at the endpoints or at breakpoints, and list the rectangle $(a, r, (c + d)/2, (d - c)/2 + 2^{-k})$. It is valid for $f$: for $y \in [0, 1]$ with $|y - a| < r$, $|f(y) - (c + d)/2| \leq 2^{-k} + (d - c)/2$. Totality: given $x \in [0, 1]$ and $\varepsilon > 0$, choose $k$ with $2^{-k} < \varepsilon/2$; since $P_k$ is continuous, there is a rational $r > 0$ such that $P_k$ varies by less than $\varepsilon/2$ on $[x - 2r, x + 2r]$, and a rational $a \in [0, 1]$ with $|x - a| < r$; the rectangle listed for $(k, a, r)$ has height less than $\varepsilon/4 + 2^{-k} < \varepsilon$.

($\delta_\square \leq \delta_C$) From a $\delta_\square$-name of $f$, compute a modulus $\mu$ by :ref{#thm-modulus-max}. For each $k$, let $N = 2^{\mu(k+2)}$, compute rationals $c_j$ with $|c_j - f(j/N)| \leq 2^{-k-2}$ for $j \leq N$, and let $P_k$ be the rational polygon with values $c_j$ at the breakpoints $j/N$. For $x \in [j/N, (j+1)/N]$, $P_k(x)$ is a convex combination of $c_j$ and $c_{j+1}$, and $|c_i - f(x)| \leq |c_i - f(i/N)| + |f(i/N) - f(x)| \leq 2^{-k-1}$ for $i \in \{j, j+1\}$; so $d(P_k, f) \leq 2^{-k-1}$. Hence $d(P_k, P_l) \leq 2^{-k-1} + 2^{-l-1} \leq 2^{-k}$ for $k \leq l$, and $(P_k)$ is a $\delta_C$-name of $f$.
:::

From now on, $C[0, 1]$ is represented by $\delta_C$, or equivalently by $\delta_\square$. The computable points of $C[0, 1]$ are exactly the computable functions $f : [0, 1] \to \mathbb R$, and evaluation, the arithmetic operations applied pointwise, the maximum value and a modulus of uniform continuity are all computable on $C[0, 1]$. In $\mathsf{RCA}_0$, a code of a continuous function gives neither a modulus of uniform continuity nor the existence of the maximum value: each of these statements is equivalent to $\mathsf{WKL}_0$ (Simpson, Theorem IV.2.3). The difference is the one noted after :ref{#lem-effective-heine-borel}: the algorithms of this lesson are proved correct with the Heine–Borel theorem.

:::quiz[the space of continuous functions]
In the proof that $\delta_\square \leq \delta_C$, why is the modulus computed before the polygon?

- [x] Because the grid $j/N$ must be fine enough that $f$ varies by at most $2^{-k-2}$ between consecutive points, and only a modulus gives such an $N$ from the name.
- [ ] Because evaluation at $j/N$ needs a modulus.

  Evaluation is computable from a rectangle name directly, by :ref{#thm-rectangle-computable}.
- [ ] Because rational polygons have rational breakpoints.

  The breakpoints $j/N$ are rational for every $N$; the question is which $N$ suffices.
:::

## Exercises

::::exercise{difficulty=1}
Show that the integral $f \mapsto \int_0^1 f(x)\, dx$ is $(\delta_C, \rho)$-computable.

:::solution
The integral of a rational polygon is a rational, computed by the trapezoid formula on each piece. If $(P_k)$ is a $\delta_C$-name of $f$, then $|\int_0^1 f - \int_0^1 P_k| \leq d(f, P_k) \leq 2^{-k}$, and :ref{#lem-cauchy-variants} gives a Cauchy name of the integral.
:::
::::

::::exercise{difficulty=2}
Show that the Cauchy representation of Cantor space of :ref{#ex-computable-metric-spaces} is equivalent to the identity representation.

:::solution
Given $X$, the sequence $p(k) = $ the index of $(X \uh (k+1)) 0^\infty$ satisfies $d(\alpha(p(k)), X) \leq 2^{-k-1}$, so $d(\alpha(p(k)), \alpha(p(l))) \leq 2^{-k}$ for $k \leq l$, and $p$ is a name of $X$. Conversely, if $p$ is a name of $X$, then $d(\alpha(p(k)), X) \leq 2^{-k}$, so $\alpha(p(k))$ and $X$ agree on the positions $n < k$; hence $X(n)$ is the $n$-th bit of $\alpha(p(n+1))$, computed from $p$.
:::
::::

## Notes and references

Representations of $C[0, 1]$ are compared in Weihrauch, Section 6.1, which shows the equivalence of a representation by rectangles ("box properties", Definition 6.1.3), the Cauchy representation for the uniform metric (Definition 6.1.9, Lemma 6.1.10) and the representation by realizers. The computable Heine–Borel theorem is his Theorem 5.2.7; the maximum, the modulus of continuity and integration are Corollary 6.2.5, Theorem 6.2.7 and Theorem 6.4.1. Computable metric spaces are Weihrauch, Section 8.1 (Definition 8.1.2 and Example 8.1.3), and Brattka and Presser (2003) develop their theory. Pour-El and Richards (Chapter 0) define computable functions on compact intervals by sequential computability and a computable modulus. In reverse mathematics, the equivalences of $\mathsf{WKL}_0$ with uniform continuity, boundedness and the existence of suprema are Simpson, Theorem IV.2.3, and Dzhafarov–Mummert, Theorems 10.5.11–10.5.12.

- K. Weihrauch, *Computable Analysis: An Introduction*, Springer, 2000, Sections 5.2, 6.1, 6.2, 6.4 and 8.1.
- V. Brattka and G. Presser, *Computability on subsets of metric spaces*, Theoretical Computer Science 305 (2003), 43–76.
- M. B. Pour-El and J. I. Richards, *Computability in Analysis and Physics*, Springer, 1989, Chapter 0.
- S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd edition, Cambridge University Press, 2009, Section IV.2.
- D. D. Dzhafarov and C. Mummert, *Reverse Mathematics: Problems, Reductions, and Proofs*, Springer, 2022, Section 10.5.
