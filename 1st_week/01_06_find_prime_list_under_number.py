import math

input = 20

def find_prime_list_under_number(number):
    prime_list = []

    is_prime = [True] * (number + 1) # 처음에는 모두 true로 초기화
    is_prime[0], is_prime[1] = False, False # 0과 1은 소수가 아니므로 False로 설정

    for i in range(2, int(math.sqrt(number)) + 1): # 2부터 number의 제곱근까지만 검사
        if not is_prime[i]: continue # 이미 소수가 아니면 넘어감
        for j in range(i * 2, number + 1, i): # i의 배수들은 False로 판정
            is_prime[j] = False

    for i in range(2, number + 1):
        if is_prime[i]:
            prime_list.append(i)

    return prime_list

result = find_prime_list_under_number(input)
print(result)