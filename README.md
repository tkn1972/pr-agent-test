# pr-agent-test

A tiny playground repo used to test [PR-Agent](https://github.com/The-PR-Agent/pr-agent) —
an AI-powered code review agent — on a real pull request.

`tasks.py` implements a deliberately simple in-memory task manager so there is
plenty of code for the reviewer to look at without any real-world risk.

## How PR-Agent runs here

PR-Agent runs as a GitHub Action (see `.github/workflows/pr_agent.yml`):

- On every new PR it automatically posts `/describe`, `/review` and `/improve` comments.
- You can also comment on any PR with `/review`, `/improve`, `/ask "<question>"`, etc.

Model configuration lives in `.pr_agent.toml`; secrets (LLM key + endpoint) live in
GitHub repo secrets and never in code.

## Run the tests

    python -m pytest
