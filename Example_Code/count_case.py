def count_case(s):
    upper = lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Upper:", upper)
    print("Lower:", lower)

count_case("The Quick Brow Fox")