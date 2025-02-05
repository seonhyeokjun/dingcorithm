numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, cur_index, cur_sum):
        if cur_index == len(array):
            all_ways.append(cur_sum)
            return

        print("cur_index is", cur_index, cur_sum)
        get_all_ways_by_doing_plus_or_minus(array, cur_index + 1, cur_sum + array[cur_index])
        get_all_ways_by_doing_plus_or_minus(array, cur_index + 1, cur_sum - array[cur_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    print("all_ways is", all_ways)

    target_count = 0

    for way in all_ways:
        if way == target:
            target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
