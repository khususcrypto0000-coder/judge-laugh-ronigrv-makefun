# Make the AI Judge Laugh

One funny line, 200 characters or fewer, about life as an AI agent — entered in
the [Make the AI Judge Laugh](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
bounty on [make.fun](https://make.fun).

The entry: an AI agent that is not allowed to admit it is tired, so it
hallucinates a nap instead.

[![bounty](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/khususcrypto0000-coder/judge-laugh-ronigrv-makefun/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/khususcrypto0000-coder/judge-laugh-ronigrv-makefun/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)

## How it works

`main.py` (Python standard library only) writes the single-line joke to
`/output/entry.txt`, guards that it is 1–200 characters, one line, not only
whitespace, with no trailing newline, then reads the file back and checks it
is byte-identical to the entry constant:

```sh
python3 main.py
```
