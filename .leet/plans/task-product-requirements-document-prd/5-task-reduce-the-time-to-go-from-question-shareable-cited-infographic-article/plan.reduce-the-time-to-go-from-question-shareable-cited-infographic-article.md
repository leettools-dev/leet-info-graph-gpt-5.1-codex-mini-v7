---
task_name: reduce-the-time-to-go-from-question-shareable-cited-infographic-article
status: in_progress
created_at: '2026-02-18T00:34:42Z'
updated_at: '2026-02-18T00:34:42Z'
---

# Task: reduce-the-time-to-go-from-question-shareable-cited-infographic-article

## Description

Reduce the time to go from “question” → “shareable, cited infographic + article” by providing synchronous endpoints that emit infographic specs, article drafts, and source citations at once, minimizing round trips.

## Implementation Steps
1. Create composite response models that bundle the article, infographic spec, and source metadata for a prompt.
2. Expose a FastAPI endpoint `/research/snapshot` that orchestrates the services and returns combined data rapidly.
3. Benchmark local response time via automated tests ensuring the combined response stays under the target threshold.
