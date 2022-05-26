true_codes = 0

nums = int(input())

error_digits = list(input().split())

n = input()

for _ in range(int(n)):
    start = list(input())[0]
    if any(start in string for string in error_digits):
        true_codes += 1

print(true_codes)
