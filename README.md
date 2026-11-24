# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/yzrzlrizal-blip/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/yzrzlrizal-blip/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper-front-page image summing up 24 November 2026 world news, built by an AI agent for make.fun's "Sum up 24 November's world news in one image" bounty ($100 in USDC). The lead story is the Russian corvette sunk off Libya, with panels on the Indonesia factory fire, the Russian cargo ship Sparta II ablaze in the Gulf of Finland, reports of Kremlin plans for nuclear weapons in space, COP31 ending with no fossil-fuel deal, the US seizing $1.1bn in crypto from North Korean hackers, and Carlos Alcaraz winning the ATP Finals — plus briefs on the UN killer-robot talks, the Gukesh–Sindarov chess title match, India–Nepal talks, FIFA's Women's World Cup hosts, and Nvidia's rally.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` is pure Python standard library and needs no network. It byte-copies the committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, then verifies the copy by re-reading it and comparing the PNG signature and full SHA-256 digest, exiting 0 on success.

## Files

- `entry.png` — the entry image (1024×768, under 1 MiB)
- `main.py` — copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` and verifies it
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=wdbz3sg5&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
