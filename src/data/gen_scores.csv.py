import random
from pathlib import Path
from typing import Literal

import polars as pl

this_dir = Path(__file__).parent

name = [
    "Ai",
    "Akane",
    "Aya",
    "Ayaka",
    "Daiki",
    "Hitomi",
    "Kenta",
    "Kentaro",
    "Mai",
    "Manami",
    "Miho",
    "Narumi",
    "Ryo",
    "Saori",
    "Shohei",
    "Shota",
    "Shota",
    "Takuya",
    "Tatsuya",
    "Yuta",
]
gender: list[Literal["F", "M"]] = [
    "F",
    "F",
    "F",
    "F",
    "M",
    "F",
    "M",
    "M",
    "F",
    "F",
    "F",
    "F",
    "M",
    "F",
    "M",
    "M",
    "M",
    "M",
    "M",
    "M",
]
length = len(name)


def get_score_list(length: int) -> list[int]:
    return [random.randint(0, 100) for _ in range(length)]


df = pl.DataFrame(
    {
        "name": name,
        "gender": gender,
        "japanese": get_score_list(length),
        "math": get_score_list(length),
        "english": get_score_list(length),
        "science": get_score_list(length),
        "social": get_score_list(length),
    }
)
df.write_csv(this_dir / "scores.csv")
