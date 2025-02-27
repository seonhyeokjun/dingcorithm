from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
    # 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def move_until_wall_or_hole(row, col, diff_r, diff_c, game_map):
    move_count = 0

    while game_map[row + diff_r][col + diff_c] != "#" and game_map[row][col] != "O":
        row += diff_r
        col += diff_c
        move_count += 1

    return row, col, move_count

def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()

        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, red_move_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, blue_move_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':
                continue

            if game_map[next_red_row][next_red_col] == 'O':
                return True

            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_move_count > blue_move_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    # print('visited', visited)

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))