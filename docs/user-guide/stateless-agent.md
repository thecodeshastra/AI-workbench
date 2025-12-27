# Stateless Agent — Architecture & Execution Flow

This document explains **how the Stateless Agent works end to end**, what problems it is designed to solve, and why its simplicity is a strength. This serves as **foundational documentation** and a reference point for more advanced agents.

---

## 1. What the Stateless Agent Does

**One-line definition:**

> The Stateless Agent takes a single user instruction and produces a single focused response using a well-defined prompt, without memory, tools, or multi-step execution.

It demonstrates:

* Prompt engineering discipline
* Deterministic single-shot behavior
* LLM usage without orchestration overhead

---

## 2. Why Stateless Agents Exist

Stateless agents are the **simplest and most reliable** form of AI agents.

They are ideal when:

* The task can be solved in one response
* No history or memory is required
* Predictability matters more than exploration

Examples:

* Code generation
* Text rewriting
* Classification
* Explanation tasks

---

## 3. High-Level Architecture

```
User Input
   ↓
Stateless Agent
   ↓
Prompt Template
   ↓
LLM Provider
   ↓
Single Output
```

There is **no planner**, **no executor**, **no tools**, and **no memory**.

---

## 4. Entry Point (User → Agent)

### Example User Input

```
Write a Python function to check if a number is prime
```

This input is passed directly to the agent.

---

## 5. Agent Role (Single Responsibility)

The Stateless Agent:

* Accepts user input
* Injects it into a prompt template
* Calls the LLM once
* Returns the response

The agent does NOT:

* Remember past inputs
* Call tools
* Plan steps
* Validate output

This is intentional.

---

## 6. Prompt as the Core Control Mechanism

In a stateless agent, **the prompt is the system**.

Typical prompt structure:

* Role
* Context
* Instructions
* Task
* Constraints
* Output expectations

This replaces planners, critics, and memory.

---

## 7. Example Prompt Flow

### Prompt Template (Conceptual)

```
ROLE:
You are a Python software engineer.

INSTRUCTIONS:
- Write a single function
- Use clear variable names
- Include docstrings

TASK:
{user_input}
```

The agent inserts user input and sends it to the LLM.

---

## 8. LLM Provider Interaction

The agent calls:

* `provider.generate(prompt, system_prompt)`

Only one LLM call is made.

No retries, no loops, no async complexity.

---

## 9. Output Handling

The response from the LLM is:

* Returned directly to the user
* Not post-processed
* Not validated

The assumption:

> Prompt quality determines output quality

---

## 10. Why This Design Is Correct

| Aspect        | Reason                |
| ------------- | --------------------- |
| No memory     | Prevents drift        |
| No tools      | Reduces failure modes |
| No planner    | Faster and cheaper    |
| Strong prompt | High precision        |

This agent is **intentionally minimal**.

---

## 11. Relationship to Other Agents

The Stateless Agent is the **root** of your agent system:

* Summarizer Agent = Stateless + Tools + Planner
* Memoryful Agent = Summarizer + Memory + Critic

Understanding this agent makes all others easier.

---

## 12. Summary

The Stateless Agent is:

* Simple
* Predictable
* Cheap
* Powerful when scoped correctly

It proves that **good prompts + clear scope** can outperform complex agents for many tasks.

---

## 13. Exit

- Type `exit` or `quit` to terminate the session.
