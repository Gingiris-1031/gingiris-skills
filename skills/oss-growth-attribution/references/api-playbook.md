# API playbook

Use GitHub API version `2022-11-28` and `GITHUB_TOKEN` when available:

```text
GET /repos/{owner}/{repo}
GET /repos/{owner}/{repo}/releases?per_page=100
GET /repos/{owner}/{repo}/commits?per_page=100&page={n}
GET /repos/{owner}/{repo}/stargazers?per_page=100&page={n}
GET /repos/{owner}/{repo}/contributors?per_page=1&anon=true
```

For timestamped stargazers send `Accept: application/vnd.github.star+json`. Record rate-limit and pagination limits. Label interpolation and coverage when sampling.

Use exact-name and channel-specific web queries. Search engines are discovery tools, not final evidence. Open canonical result URLs.

```text
"{project}" "GitHub Trending"
"{project}" stars
site:reddit.com "{project}"
site:news.ycombinator.com "{project}"
site:producthunt.com "{project}"
site:x.com "{project}"
site:instagram.com "{project}"
site:tiktok.com "{project}"
site:youtube.com/watch "{project}"
"{project}" tutorial OR install OR review
"{project}" Japanese OR Chinese OR Spanish
```
