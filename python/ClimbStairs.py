def count_steps(steps_left, total_path):
    if steps_left == 0:
        total_path.append(1)
        return
        # print(total_path)

    if steps_left < 0:
        return

    s = count_steps(steps_left - 1, total_path)
    print("steps for {0} are {1}".format(steps_left - 1, s))
    s = count_steps(steps_left - 2, total_path)
    print("steps for {0} are {1}".format(steps_left - 2, s))

    # ount_steps(n)
    return sum(total_path)


def dp_count_steps(n, memo):
    if n < 0:
        return 0

    if n - 1 not in memo:
        memo[n - 1] = dp_count_steps(n - 1, memo)
    if n - 2 not in memo:
        memo[n - 2] = dp_count_steps(n - 2, memo)

    return memo[n - 1] + memo[n - 2]


# print(count_steps(4, []))

temp = {0: 1, 1: 1}
print(dp_count_steps(n, temp))
