import sys

table = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "km": 1000,
    "m": 1
}


def translation(digit, initial, target):
    return digit * table[initial] / table[target]


if (len(sys.argv) > 1):
    digit = float(sys.argv[1])
    initial = sys.argv[2]
    target = sys.argv[3]

    print(translation(digit, initial, target))