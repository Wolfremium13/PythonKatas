import re


def increment_the_end_number_by_one(line: str) -> str:
    head = line.rstrip('0123456789')
    tail = line[len(head):]
    if tail == "":
        return line + "1"
    return head + str(int(tail) + 1).zfill(len(tail))
