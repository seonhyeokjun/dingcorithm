input = "abadabac"

def find_not_repeating_first_character(string):
    split = list(string.replace(" ", ""))

    for i in split:
        if split.count(i) == 1:
            return i

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))