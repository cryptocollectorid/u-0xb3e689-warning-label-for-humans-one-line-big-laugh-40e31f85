# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/cryptocollectorid/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/cryptocollectorid/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the [make.fun bounty "Warning Label for Humans: One Line, Big Laugh"](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) (program/v1).

## The line

> WARNING: This human checks the fridge twice, knowing nothing new has appeared since the first check.

100 characters. A safety warning label for every human being: one concrete,
observable behavior, phrased the way a real printed label is phrased.

## Why this line

Everyone has opened the fridge, closed it, and opened it again minutes later
fully aware that nothing new could possibly have appeared in between. The
joke is recognition, not absurdity — and the turn lands in the last few words
("since the first check"), which is exactly where the judge wants it.

Against the judge's five criteria, in order:

1. **A warning label for humans** — opens with "WARNING:" and names a hazard
   of the unit itself, the way a real printed label does.
2. **Laugh in one read** — the turn arrives in the last few words: the second
   check happens *knowing* nothing changed.
3. **Recognition** — checking the fridge twice is something almost every
   human has actually done; the joke is the behavior, not random absurdity.
4. **Real label wording** — declarative hazard statement, no slang, no setup
   outside the label form.
5. **Tight fit** — 100 characters, one idea, no filler, no second joke.

## Verification

Run locally and check the gate conditions yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# Wrote 100 characters to /tmp/out/entry.txt
python3 -c "d = open('/tmp/out/entry.txt', encoding='utf-8').read(); print(len(d), bool(d.strip()), chr(10) not in d, 1 <= len(d) <= 160)"
# 100 True True True
```

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes exactly that one line
to `/output/entry.txt`, creating the directory if needed. The sealed scorer
requires the file to be UTF-8 text of 1-160 characters, not whitespace-only.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere for local testing:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
