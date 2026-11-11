#!/usr/bin/env python3
"""Print the Collatz sequence starting from 27 and the number of steps to reach 1."""


def collatz_sequence(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz_sequence(27)
    for value in sequence:
        print(value)
    total_steps = len(sequence) - 1
    print(f"Total steps: {total_steps}")


if __name__ == "__main__":
    main()
