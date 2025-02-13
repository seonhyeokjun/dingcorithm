from collections import deque

prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    prices_queue = deque(prices)
    answer = []

    while prices_queue:
        current_price = prices_queue.popleft()
        time = 0
        for next_price in prices_queue:
            time += 1
            if current_price > next_price:
                answer.append(time)
                break

    return answer


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))