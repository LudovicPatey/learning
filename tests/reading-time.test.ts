import { describe, expect, it } from "vitest";
import { durationFor, openTextWords } from "@/lib/reading-time";

describe("openTextWords", () => {
  it("counts the open text only", () => {
    const md = [
      "---",
      "title: Not counted here",
      "duration: 10",
      "---",
      "One two three.",
      ":::theorem{#thm-x}",
      "Four $x+y$ five.",
      ":::",
      ":::quiz[the proof]",
      "Hidden question?",
      "- [x] Hidden.",
      ":::",
      "::::exercise{#ex-a difficulty=1 objective=\"Six.\"}",
      "Seven eight.",
      "",
      ":::solution",
      "Hidden solution.",
      ":::",
      "::::",
      ":::hint",
      "Hidden hint.",
      ":::",
      '<svg class="fig"><text>hidden</text>',
      "<line/>",
      "</svg>",
      '<svg class="fig"><text>hidden</text></svg>',
      "Nine.",
      ":::::exercises",
      "::::exercise{#ex-b}",
      "Hidden further exercise.",
      "::::",
      ":::::",
    ].join("\n");
    // One two three. (3) + fence (1) + Four $x+y$ five. (3) + fence (1) + exercise line (3) +
    // Seven eight. (2) + closing fence (1) + Nine. (1)
    expect(openTextWords(md)).toBe(15);
  });

  it("closes a collapsed block at a fence with at least as many colons", () => {
    expect(openTextWords("::::solution\nhidden\n:::\nstill hidden\n::::\nshown")).toBe(1);
  });
});

describe("durationFor", () => {
  it("rounds to a multiple of 5 minutes, at least 5", () => {
    expect(durationFor(0)).toBe(5);
    expect(durationFor(55 * 22)).toBe(20);
    expect(durationFor(55 * 23)).toBe(25);
    expect(durationFor(55 * 45)).toBe(45);
    expect(durationFor(55 * 48)).toBe(50);
  });
});
