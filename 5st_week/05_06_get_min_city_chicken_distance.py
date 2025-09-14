import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for r in range(n):
        for c in range(n):
            if city_map[r][c] == 1:
                home_location_list.append((r, c))
            elif city_map[r][c] == 2:
                chicken_location_list.append((r, c))
    # print(home_location_list, chicken_location_list)

    combinations_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize
    for combinations_location_m_combination in combinations_location_m_combinations:
        combinations_location_m_combination_total_chicken_distance = 0
        # print("combinations_location_m_combinations is ", combinations_location_m_combination)
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            # print("home_r, home_c is ", home_r, home_c)

            for chicken_location in combinations_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            combinations_location_m_combination_total_chicken_distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(
            min_distance_of_m_combinations,
            combinations_location_m_combination_total_chicken_distance
        )

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))