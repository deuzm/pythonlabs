#!/usr/bin/env python3
import logging

logging.basicConfig(level=logging.INFO)


def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    while True:
        n = str(input())
        if n.isnumeric():
            n = int(n)
            break
    logging.info(fib(n))


if __name__ == "__main__":
    main()
