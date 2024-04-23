n = int(input())


def top(num, start, end, other, cnt, result_list):
    if not num:
        return result_list
    result_list = top(num - 1, start, other, end, cnt, result_list)
    result_list.append(f"{start} {end}")
    return top(num - 1, other, end, start, cnt + 1, result_list)


result = top(n, 1, 3, 2, 0, [])

print(len(result))
print("\n".join(result))
