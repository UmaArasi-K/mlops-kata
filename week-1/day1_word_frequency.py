"""Day 1: Word frequency counter from file.

Concepts practiced: dict.get(), list comprehensions, sorted(), heapq.nlargest, file I/O, lambda.
"""
import heapq


def count_words(filename: str) -> dict[str, int]:
    """Read a file and return word frequency counts."""
    hand = open(filename)
    freq = dict()
    for line in hand:
        line = line.rstrip()
        words = line.split()
        for word in words:
            freq[word] = freq.get(word, 0) + 1
    hand.close()
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Return top N words by frequency."""
    return heapq.nlargest(n, freq.items(), key=lambda item: item[1])


if __name__ == "__main__":
    fname = input("enter file name: ")
    if len(fname) < 1:
        fname = "testdoc.txt"

    freq = count_words(fname)
    print(freq)
    print("---------------------")
    print("Sorted alphabetically:", sorted(freq.items()))
    print("---------------------")
    print("Flipped and sorted (desc):")
    flipped_sorted = sorted([(v, k) for k, v in freq.items()], reverse=True)
    print(flipped_sorted)
    print("---------------------")
    print("Top 5:", top_n(freq))
