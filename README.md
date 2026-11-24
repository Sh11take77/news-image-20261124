# Sum up 24 November's world news in one image

Entry for make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124)
by @peng-zhan-gao, GitHub: Sh11take77.

## What it is

A one-page newspaper infographic summarising Tuesday
24 November 2026 world news, in six panels:

1. NATO sends AWACS to Poland after Russian missiles land in Poland
2. Ukraine sinks Russian warship Merkury off Libya (Benghazi port)
3. Iran flogs singer 74 lashes; US naval blockade standoff grows
4. COP31 climate talks collapse in Türkiye over fossil fuels
5. Trump backs Nvidia chief Huang; Huang reinstated as CEO
6. Gaza strikes; Vanuatu quake 6.5, no tsunami threat

## How it runs

`main.py` (Python 3.13, standard library only, no network)
copies `image.png` (1024×1024 PNG, under 1 MiB) to
`/output/entry.png`, byte-for-byte. Two runs produce
identical output.

```sh
python3 main.py
# Wrote /output/entry.png (901171 bytes)
```

## Files

- `main.py` — the entry program
- `image.png` — the infographic
- `LICENSE` — MIT
