def find_max_occurred_alphabet(string):
    # 공백을 제거하고 문자열을 문자 리스트로 변환
    split = list(string.replace(" ", ""))

    # 알파벳 별로 개수를 세기 위한 딕셔너리
    alphabet_occurrence = {}

    for i in split:
        if not i.isalpha():
            continue

        if i in alphabet_occurrence:
            alphabet_occurrence[i] += 1
        else:
            alphabet_occurrence[i] = 1

    return max(alphabet_occurrence, key=alphabet_occurrence.get)

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))