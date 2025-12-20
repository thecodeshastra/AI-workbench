# Summarizer Agent — Architecture & Execution Flow

This document explains **how the Summarizer Agent works from start to end**, why each component exists, and how data flows through the system. This is meant as **internal documentation + learning reference**, not marketing material.

---

## 1. What the Summarizer Agent Does

**One-line definition:**

> The Summarizer Agent takes a user instruction involving a file, summarizes its contents, extracts actionable items, and saves the results using a structured, reliable execution flow.

It demonstrates:

- Tool usage
- Planner–Executor architecture
- Async-safe execution
- Deterministic, non-hallucinatory behavior

---

## 2. High-Level Architecture

```
User Input
   ↓
Agent (Orchestrator)
   ↓
Planner (LLM → JSON plan)
   ↓
Plan Validation
   ↓
Executor
   ↓
Tools (File → Summarize → Extract → Write)
   ↓
Context (shared state)
```

Each component has **one responsibility only**.

---

## 3. Entry Point (User → Agent)

### Example User Input

```
/home/user/meeting.txt , summarize it, extract action items, and save actions to /home/user/actions.txt
```

This is the **only free-form input** in the system. Everything else becomes structured.

---

## 4. Agent Role (Orchestration Only)

The agent:

- Builds the planner prompt
- Calls the LLM via a provider
- Expects a strict JSON plan
- Validates the plan
- Passes the plan to the executor

The agent:

- ❌ does NOT summarize
- ❌ does NOT call tools directly
- ❌ does NOT reason about execution

---

## 5. Planner — From Language to Plan

### Planner Responsibility

> Convert user intent into a **deterministic execution plan** using known tools.

### Example Planner Output

```json
{
  "steps": [
    { "tool": "file_read", "input": { "path": "/home/user/meeting.txt" } },
    { "tool": "text_summarize", "input": {} },
    { "tool": "extract_actions", "input": {} },
    { "tool": "file_write", "input": { "path": "/home/user/actions.txt", "source": "actions" } }
  ]
}
```

The planner:

- Decides **what to do**
- Does NOT execute anything
- Outputs JSON only

---

## 6. Plan Validation (Safety Gate)

Before execution:

- Ensure valid JSON
- Ensure `steps` exists
- Ensure tool names are registered

If validation fails → execution stops immediately.

This prevents hallucinated execution.

---

## 7. Executor — Turning Plan into Action

The executor:

- Iterates over steps
- Calls tools in order
- Manages async execution
- Controls failures
- Writes and reads shared context

The executor **never reasons** — it only executes.

---

## 8. Context — Shared Short-Term Memory

### What Context Is

A protected key–value store shared across tools during execution.

### Example Context Keys

- `text` → raw file contents
- `summary` → summarized text
- `actions` → extracted action items

Context is async-safe and accessed via:

```python
await context.set(key, value)
await context.get(key)
```

---

## 9. Tool Execution (Step-by-Step)

### Tool 1 — File Read

**Input:**

```json
{ "path": "/home/user/meeting.txt" }
```

**Action:**

- Reads file
- Stores text in context

---

### Tool 2 — Text Summarize

**Input:** none (reads from context)

**Action:**

- Pulls `text` from context
- Calls LLM
- Stores `summary`

Why summarization first:

- Reduces token size
- Improves extraction accuracy
- Lowers cost

---

### Tool 3 — Extract Actions

**Input:** none (uses summary)

**Action:**

- Extracts actionable items
- Stores `actions`

This avoids noisy raw-text extraction.

---

### Tool 4 — File Write

**Input:**

```json
{ "path": "/home/user/actions.txt", "source": "actions" }
```

**Action:**

- Pulls `actions` from context
- Writes to disk

Tool does not know how actions were created.

---

## 10. Async Execution (Where It Fits)

Async is used for:

- LLM calls (summarization, extraction)
- Non-blocking execution

Async is **not** used for:

- Planning
- Context logic

Shared context is protected to prevent race conditions.

---

## 11. Final Output

After execution:

- Summary is printed to console
- Action items are printed
- Actions file is saved

No post-hoc parsing or guessing is needed.

---

## 12. Why This Design Is Correct

| Component | Responsibility    |
| --------- | ----------------- |
| Agent     | Orchestration     |
| Planner   | Decide steps      |
| Executor  | Run steps         |
| Tools     | Single task       |
| Context   | Shared state      |
| Provider  | LLM communication |

No component overlaps responsibility.

---

## 13. Summary

The Summarizer Agent is:

- Deterministic
- Structured
- Async-safe
- Extensible

It is intentionally **boring and predictable**, which is exactly what makes it powerful.

---

## 14. Exit

- Type `exit` or `quit` to terminate the session.
