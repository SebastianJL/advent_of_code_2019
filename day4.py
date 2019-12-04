import re


def is_valid_password(n: int):
    valid = True
    n_str: str = str(n)

    valid &= n_str == ''.join(sorted(n_str))
    valid &= re.search(r'(\d)\1+', n_str) is not None

    return valid


passwords = range(136760, 595730+1)
# passwords = [111111, 22345, 123789]

count = sum(is_valid_password(p) for p in passwords)
print(count)
