# battery-last-text

[![The Battery's Last Text to Its Charger](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/nmlyz/battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/nmlyz/battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A tiny program that writes one line of text: a phone battery's last
message to the charger it waited for all day.

## What it does

`main.py` (Python standard library only) writes a single line of plain
text to `/output/entry.txt`, with no trailing newline and file mode
`0644`. The line is fixed, so every run produces byte-identical output.

## Run

```sh
python3 main.py
```

The message is written to `/output/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
