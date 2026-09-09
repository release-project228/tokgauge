#!/usr/bin/env python3
"""TikTok account growth: a summary over a CSV of your own history
(date,followers,likes). Prints total follower gain, best day and avg likes.

Rows: 2026-01-01,12000,350000
"""
import csv
import sys


def main(path: str) -> int:
    points = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.reader(fh):
            if len(row) < 3:
                continue
            try:
                points.append((row[0].strip(), int(float(row[1])), int(float(row[2]))))
            except ValueError:
                pass
    if len(points) < 2:
        print("need >=2 rows: date,followers,likes", file=sys.stderr)
        return 1
    start, end = points[0], points[-1]
    gain = end[1] - start[1]
    pct = gain / start[1] * 100 if start[1] else 0.0
    best = max(zip(points[1:], points), key=lambda p: p[0][1] - p[1][1])[0]
    avg_likes = sum(p[2] for p in points) / len(points)
    print(f"{start[0]} -> {end[0]}")
    print(f"  followers: {start[1]:,} -> {end[1]:,}  ({gain:+,} / {pct:+.1f}%)")
    print(f"  best day:  {best[0]} (+{best[1] - points[points.index(best) - 1][1]:,})")
    print(f"  avg likes/post: {avg_likes:,.0f}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
