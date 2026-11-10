// Learning tracks.
//
// A track is a main sequence of courses in one area, listed in
// content/tracks.yaml. Courses that belong to no track are "specialized
// courses": they appear in the catalogue and on course pages, but not in the
// dependency graphs of the home page, which show one track at a time.
//
// This module is pure (no file system), so that it can be unit-tested.

export type Track = {
  id: string;
  title: string;
  area: string;
  description: string;
  /** Core courses of the track, in their recommended order. */
  courses: string[];
};

export type GraphCourse = { id: string; prerequisites: string[] };

/** Parse the content of tracks.yaml, reporting unknown courses and areas. */
export function parseTracks(raw: unknown, courseIds: Set<string>, areaIds: Set<string>, warnings: string[]): Track[] {
  if (raw == null) return [];
  if (!Array.isArray(raw)) {
    warnings.push("content/tracks.yaml must be a list of tracks");
    return [];
  }
  const seen = new Set<string>();
  const tracks: Track[] = [];
  for (const t of raw as any[]) {
    const id = String(t?.id ?? "");
    if (!id) {
      warnings.push("content/tracks.yaml: a track has no id");
      continue;
    }
    if (seen.has(id)) warnings.push(`content/tracks.yaml: duplicate track "${id}"`);
    seen.add(id);
    const area = String(t.area ?? "");
    if (!areaIds.has(area)) warnings.push(`content/tracks.yaml: track "${id}" has unknown area "${area}"`);
    const courses = ((t.courses ?? []) as unknown[]).map(String);
    for (const c of courses) if (!courseIds.has(c)) warnings.push(`content/tracks.yaml: track "${id}" lists unknown course "${c}"`);
    tracks.push({
      id,
      title: String(t.title ?? id),
      area,
      description: String(t.description ?? ""),
      courses: courses.filter((c) => courseIds.has(c)),
    });
  }
  return tracks;
}

/** The first track listing each course; courses absent from the map are specialized. */
export function trackOfCourse(tracks: Track[]): Map<string, string> {
  const m = new Map<string, string>();
  for (const t of tracks) for (const c of t.courses) if (!m.has(c)) m.set(c, t.id);
  return m;
}

/** All courses that `id` depends on, directly or indirectly. */
export function ancestors(id: string, byId: Map<string, GraphCourse>): Set<string> {
  const out = new Set<string>();
  const visit = (x: string) => {
    for (const p of byId.get(x)?.prerequisites ?? []) {
      if (!out.has(p)) {
        out.add(p);
        visit(p);
      }
    }
  };
  visit(id);
  return out;
}

export type TrackGraph = {
  /** Longest chain of prerequisites inside the track, for each course of the track. */
  depth: Map<string, number>;
  /** Prerequisites between courses of the track. */
  edges: [from: string, to: string][];
  /**
   * Courses outside the track on which the track depends, reduced to the minimal ones:
   * a course is omitted when another listed course already depends on it.
   */
  external: string[];
};

export function trackGraph(track: Track, all: GraphCourse[]): TrackGraph {
  const byId = new Map(all.map((c) => [c.id, c]));
  const inTrack = new Set(track.courses);
  const edges: [string, string][] = [];
  const externalAll = new Set<string>();
  for (const id of track.courses) {
    for (const p of byId.get(id)?.prerequisites ?? []) {
      if (inTrack.has(p)) edges.push([p, id]);
      else if (byId.has(p)) externalAll.add(p);
    }
  }
  const external = [...externalAll].filter((e) => ![...externalAll].some((f) => f !== e && ancestors(f, byId).has(e)));

  const depth = new Map<string, number>();
  const visit = (id: string, stack: Set<string>): number => {
    if (depth.has(id)) return depth.get(id)!;
    if (stack.has(id)) return 0; // cycle: ignore
    stack.add(id);
    const internal = (byId.get(id)?.prerequisites ?? []).filter((p) => inTrack.has(p));
    const d = internal.length ? 1 + Math.max(...internal.map((p) => visit(p, stack))) : 0;
    stack.delete(id);
    depth.set(id, d);
    return d;
  };
  for (const id of track.courses) visit(id, new Set());
  return { depth, edges, external };
}

/** Lowercase, remove accents and punctuation, for search. */
export function normalizeForSearch(s: string): string {
  return s
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉σπδωαβλ]+/g, " ")
    .trim();
}

/** True if every word of the query occurs in the text (both normalized). */
export function matchesQuery(text: string, query: string): boolean {
  const words = normalizeForSearch(query).split(" ").filter(Boolean);
  if (!words.length) return true;
  const hay = normalizeForSearch(text);
  return words.every((w) => hay.includes(w));
}
