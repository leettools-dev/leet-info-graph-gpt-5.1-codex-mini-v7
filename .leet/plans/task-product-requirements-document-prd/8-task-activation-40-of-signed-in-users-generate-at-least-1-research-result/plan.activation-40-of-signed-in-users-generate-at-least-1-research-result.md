---
task_name: activation-40-of-signed-in-users-generate-at-least-1-research-result
status: in_progress
created_at: '2026-02-18T00:34:42Z'
updated_at: '2026-02-18T00:34:42Z'
---

# Task: activation-40-of-signed-in-users-generate-at-least-1-research-result

## Description

Activation:** ≥ 40% of signed-in users generate at least 1 research result by providing a starter prompt flow, onboarding checklist, and tracking instrumentation for prompt submissions.

## Implementation Steps
1. Introduce backend endpoints for onboarding state and prompt submission counters.
2. Capture metrics (e.g., prompts per user, first-response-time) via lightweight in-memory counters/fixtures.
3. Expose an admin endpoint that reports activation rates so engineers can monitor progress.
