"use client";

import { useEffect, useState } from "react";

// A real Turing machine, animated: binary increment.
//   q0 (go right): on 0/1 move right; on blank move left and switch to q1.
//   q1 (carry):    on 1 write 0 and move left; on 0 or blank write 1 and halt.

const CELLS = 11;
const BLANK = " ";
type State = "q0" | "q1" | "h";
type Machine = { tape: string[]; head: number; state: State; rule: string; written: number | null };

function load(n: number): Machine {
  const bits = n.toString(2);
  const start = Math.max(1, Math.floor((CELLS - bits.length) / 2));
  const tape = Array(CELLS).fill(BLANK);
  for (let i = 0; i < bits.length; i++) tape[start + i] = bits[i];
  return { tape, head: start, state: "q0", rule: "start in state q₀ on the first digit", written: null };
}

const sym = (s: string) => (s === BLANK ? "⊔" : s);

function step(m: Machine): Machine {
  const tape = [...m.tape];
  const a = tape[m.head];
  if (m.state === "q0") {
    if (a === BLANK) return { tape, head: m.head - 1, state: "q1", rule: `δ(q₀, ⊔) = (q₁, ⊔, L)`, written: null };
    return { tape, head: m.head + 1, state: "q0", rule: `δ(q₀, ${a}) = (q₀, ${a}, R)`, written: null };
  }
  if (m.state === "q1") {
    if (a === "1") {
      tape[m.head] = "0";
      return { tape, head: m.head - 1, state: "q1", rule: `δ(q₁, 1) = (q₁, 0, L)`, written: m.head };
    }
    tape[m.head] = "1";
    return { tape, head: m.head, state: "h", rule: `δ(q₁, ${sym(a)}) = (h, 1, ·)  — halt`, written: m.head };
  }
  return m;
}

const value = (tape: string[]) => parseInt(tape.join("").trim() || "0", 2);

export function TuringTape() {
  const [n, setN] = useState(11);
  const [m, setM] = useState<Machine>(() => load(11));

  useEffect(() => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const delay = m.state === "h" ? 1800 : reduce ? 1400 : 650;
    const t = setTimeout(() => {
      if (m.state === "h") {
        const next = value(m.tape) > 30 ? 11 : value(m.tape);
        setN(next);
        setM(load(next));
      } else setM(step(m));
    }, delay);
    return () => clearTimeout(t);
  }, [m]);

  return (
    <div className="tm-card" aria-label="Animated Turing machine adding one in binary">
      <div className="tm-head-row">
        <span className="tm-title">Turing machine · binary successor</span>
        <span className="tm-dots" aria-hidden>
          <i />
          <i />
          <i />
        </span>
      </div>
      <div className="tm-tape">
        <div className="tm-pointer" style={{ left: `calc(${m.head} * ((100% - ${CELLS - 1} * var(--tm-gap)) / ${CELLS} + var(--tm-gap)))` }}>
          <span>{m.state === "h" ? "halt" : m.state === "q0" ? "q₀" : "q₁"}</span>
        </div>
        {m.tape.map((c, i) => (
          <div
            key={i}
            className={`tm-cell ${c === BLANK ? "blank" : ""} ${i === m.head ? "is-head" : ""} ${i === m.written ? "just-written" : ""}`}
          >
            {sym(c)}
          </div>
        ))}
      </div>
      <div className="tm-rule">
        <span>{m.rule}</span>
        <span className="muted">{m.state === "h" ? `${n} + 1 = ${value(m.tape)}` : `input ${n}`}</span>
      </div>
      <p className="tm-caption">A Turing machine with two states computing the successor in binary. Each step applies one transition of δ.</p>
    </div>
  );
}
