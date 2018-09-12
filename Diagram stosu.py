
from .cwicz2 import print_twice


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

    part1 = "bum"
    part2 = "bam."
    cat_twice(part1, part2)
    print(cat)


