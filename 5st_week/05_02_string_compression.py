input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    result = n
    for split_size in range(1, len(string) // 2 + 1):
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        compressed = ""
        count = 1
        for i in range(0, len(splited) - 1):
            cur, next = splited[i], splited[i + 1]

            if cur == next:
                count += 1
            else:
                if count == 1:
                    compressed += cur
                else:
                    compressed +=  f"{count}{cur}"
                count = 1

        if count == 1:
            compressed += splited[-1]
        else:
            compressed += f"{count}{splited[-1]}"

        result = min(result, len(compressed))

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))