# GitHub Profile Inspiration Scan

Reviewed examples:

- [Andrej Karpathy](https://github.com/karpathy): memorable flagship repos such as `nanoGPT`, `llm.c`, and `micrograd`.
- [Sebastian Raschka](https://github.com/rasbt): strong educational/from-scratch positioning and book-linked repos.
- [Phil Wang / lucidrains](https://github.com/lucidrains): consistent implementation-library pattern across many AI papers.
- [Georgi Gerganov](https://github.com/ggerganov): infrastructure credibility through focused systems repos.
- [Soumith Chintala](https://github.com/soumith): long-term open-source infrastructure identity.
- [lllyasviel](https://github.com/lllyasviel): profile README as an extended index when pinned repos are not enough.
- [Simon Willison](https://github.com/simonw): project ecosystem around practical, well-documented tools.
- [Chip Huyen](https://github.com/chiphuyen): books, resource repos, and small productivity tools around one AI-engineering identity.
- [Francois Chollet](https://github.com/fchollet): frameworks, notebooks, benchmarks, and documentation linked through one research/software identity.
- [Jeremy Howard](https://github.com/jph00): notebook-first software, courses, and developer tools.
- [Jake VanderPlas](https://github.com/jakevdp): full-text notebook books, tutorials, and reusable Python libraries.
- [tiangolo](https://github.com/tiangolo): one developer-experience promise across FastAPI, Typer, SQLModel, templates, and CLI tooling.
- [Armin Ronacher](https://github.com/mitsuhiko): small durable infrastructure tools that compound into long-term trust.
- [Hugging Face](https://github.com/huggingface): ecosystem map across libraries, datasets, model tooling, and community infrastructure.

## Borrowed Patterns

| Pattern | What to borrow | Local action |
|---|---|---|
| Flagship clarity | One project should be obviously strongest | Keep `l40s-llm-bench` as the public flagship |
| Evidence-first README | State what the repo proves and what it does not prove | Add reports, run manifests, and limitations before claims |
| Consistent project family | Similar repos should share structure | Use README + docs + script + tests + generated-report pattern |
| Release boundary discipline | Strong projects do not overclaim | Keep paper/competition repos public-safe until human gates clear |
| Extended profile index | Profile README should guide the six pinned repos | Add a compact project matrix and next-action table |
| Book/notebook bridge | Learning artifacts can be the public entrypoint | Add safe synthetic notebooks or tutorials when they teach the method |
| Developer-experience promise | A tool family should feel easy to try quickly | Give each repo a 10-minute path and consistent commands |
| Ecosystem bridge | Related projects should point to each other clearly | Use the profile README as the map, not a pile of links |

## Modeling Step

The local portfolio signal model scores projects across reproducibility,
evidence artifacts, community utility, technical depth, focus alignment, release
safety, and profile clarity.

The second pass adds a profile-pattern coverage model. It estimates which
borrowed pattern is underdeveloped for each local project, then ranks the next
small experiment by weighted gap and public-release priority. This keeps
competition-sensitive or paper-sensitive work from outranking safer public
experiments just because the visible gap is larger.

Run:

```bash
python scripts/build_portfolio_model.py
```

Generated artifacts:

- `outputs/portfolio_signal_model.json`
- `outputs/profile_optimization_queue.json`
- `outputs/portfolio_signal_model.md`

The generated report is local planning evidence, not a public claim.
