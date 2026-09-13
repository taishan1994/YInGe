"""从 xinhua_words_pinyin.csv 构建游戏运行时词库。

用法：python build_wordbank.py
输出：xinhua_words_pinyin.compiled.js

原始 CSV 只在构建时解析一次，浏览器运行时直接加载生成的索引包。
"""
from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "xinhua_words_pinyin.csv"
OUT_PATH = ROOT / "xinhua_words_pinyin.compiled.js"


def strip_tone(pinyin: str) -> str:
    table = str.maketrans({
        "ā": "a", "á": "a", "ǎ": "a", "à": "a",
        "ē": "e", "é": "e", "ě": "e", "è": "e",
        "ī": "i", "í": "i", "ǐ": "i", "ì": "i",
        "ō": "o", "ó": "o", "ǒ": "o", "ò": "o",
        "ū": "u", "ú": "u", "ǔ": "u", "ù": "u",
        "ǖ": "ü", "ǘ": "ü", "ǚ": "ü", "ǜ": "ü", "ǹ": "n",
    })
    return pinyin.translate(table).lower().strip()


def main() -> None:
    words: set[str] = set()
    chars: dict[str, set[str]] = {}
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as fh:
        for row in csv.reader(fh):
            if len(row) < 2:
                continue
            word, pinyin = row[0].strip(), row[1].strip()
            if not word or word == "字词":
                continue
            words.add(word)
            if len(word) == 1 and pinyin:
                key = strip_tone(pinyin)
                chars.setdefault(key, set()).add(word)

    payload = {
        "words": sorted(words),
        "chars": {key: sorted(values) for key, values in sorted(chars.items())},
    }
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    OUT_PATH.write_text(
        "window.XINHUA_COMPILED=" + encoded + ";\n",
        encoding="utf-8",
    )
    print(f"已生成 {OUT_PATH.name}: {len(words):,} 词，{len(chars):,} 个音节索引")


if __name__ == "__main__":
    main()
