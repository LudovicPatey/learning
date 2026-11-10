// Shared between server and browser code (no Node imports here).

export const COMMENT_KINDS = ["typo", "unclear", "error", "suggestion", "question"] as const;
export const COMMENT_STATUSES = ["open", "resolved", "declined"] as const;
export type CommentKind = (typeof COMMENT_KINDS)[number];
export type CommentStatus = (typeof COMMENT_STATUSES)[number];

/** W3C-style text quote selector, plus a TeX-friendly rendering of the quote for display. */
export type Anchor = { exact: string; prefix: string; suffix: string; position: number; display: string };

export type CommentDTO = {
  id: number;
  lessonId: string;
  parentId: number | null;
  kind: CommentKind;
  body: string;
  anchor: Anchor | null;
  status: CommentStatus;
  contentHash: string | null;
  createdAt: string;
  updatedAt: string;
  author: { name: string; orcid: string };
  mine: boolean;
  replies: CommentDTO[];
};

export const KIND_LABELS: Record<CommentKind, string> = {
  typo: "Typo",
  unclear: "Unclear",
  error: "Mathematical error",
  suggestion: "Suggestion",
  question: "Question",
};
