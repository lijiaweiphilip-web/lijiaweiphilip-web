# GitHub Profile Inspiration Scan

Reviewed examples:

- [Andrej Karpathy](https://github.com/karpathy): memorable flagship repos such as `nanoGPT`, `llm.c`, and `micrograd`.
- [Sebastian Raschka](https://github.com/rasbt): strong educational/from-scratch positioning and book-linked repos.
- [Phil Wang / lucidrains](https://github.com/lucidrains): consistent implementation-library pattern across many AI papers.
- [Georgi Gerganov](https://github.com/ggerganov): infrastructure credibility through focused systems repos.
- [Soumith Chintala](https://github.com/soumith): long-term open-source infrastructure identity.
- [lllyasviel](https://github.com/lllyasviel): profile README as an extended index when pinned repos are not enough.
- [Simon Willison](https://github.com/simonw): project ecosystem around practical, well-documented tools.

## Borrowed Patterns

| Pattern | What to borrow | Local action |
|---|---|---|
| Flagship clarity | One project should be obviously strongest | Keep `l40s-llm-bench` as the public flagship |
| Evidence-first README | State what the repo proves and what it does not prove | Add reports, run manifests, and limitations before claims |
| Consistent project family | Similar repos should share structure | Use README + docs + script + tests + generated-report pattern |
| Release boundary discipline | Strong projects do not overclaim | Keep paper/competition repos public-safe until human gates clear |
| Extended profile index | Profile README should guide the six pinned repos | Add a compact project matrix and next-action table |

## Modeling Step

The local portfolio signal model scores projects across reproducibility,
evidence artifacts, community utility, technical depth, focus alignment, release
safety, and profile clarity.

Run:

```bash
python scripts/build_portfolio_model.py
```

The generated report is local planning evidence, not a public claim.
