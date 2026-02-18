---
task_name: supporting-sources-citations-with-linksmetadata
status: in_progress
created_at: '2026-02-18T00:34:42Z'
updated_at: '2026-02-18T00:34:42Z'
---

# Task: supporting-sources-citations-with-linksmetadata

## Description

supporting sources** (citations with links/metadata) – capture source metadata, snippet summaries, and reliability signals that accompany infographic/article outputs.

## Implementation Steps
1. Design Pydantic models for source metadata with URL, publisher, dates, snippet, and reliability score.
2. Implement a placeholder `SourcesService` that returns sample metadata aligned with a prompt and exposes an API endpoint.
3. Wire sources to existing article/infographic data so citations can be traced back to metadata.
4. Add automated tests ensuring metadata structure and reliability scoring rules are enforced.
