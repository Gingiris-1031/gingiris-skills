# Evidence schema

```json
{
  "channel": "reddit",
  "title": "Original title",
  "url": "https://original.example/post",
  "published_at": "2026-04-11",
  "author": "handle",
  "format": "discussion|short_video|tutorial|article|launch|repo_event",
  "hook": "Concise content angle",
  "metrics": {"views": 0, "likes": 0, "comments": 0},
  "source_type": "first_party|original_post|independent|search_snapshot",
  "observation": "What the source directly proves",
  "confidence": "high|medium|low"
}
```

- Preserve only observed public metrics; never estimate engagement counts.
- Prefer canonical URLs without translation or tracking parameters.
- Deduplicate syndication while retaining meaningful localized adaptations.
- Reject unrelated results that merely contain generic words in the project name.
