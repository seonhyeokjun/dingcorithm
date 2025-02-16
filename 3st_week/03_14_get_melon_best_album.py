def get_melon_best_album(genre_array, play_array):
    # 1. dict 에 장르별로 얼마나 재생횟수를 가지고 있는가
    # 2. dict 에 장르별로 어느 인덱스에 몇번 재생횟수를 가지고 있는가

    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(n):
        genre = genre_array[i]  # classic
        play = play_array[i]  # 500

        if genre in genre_total_play_dict:  # classic 이라는 키값이 있었으면
            genre_total_play_dict[genre] += play  # 재생횟수를 더해줘야 할테니까요
            genre_index_play_array_dict[genre].append([i, play])
        else:  # 키 값이 없는 상황이라면
            genre_total_play_dict[genre] = play  # 500
            genre_index_play_array_dict[genre] = [[i, play]]

    # 장르별로 가장 재생횟수가 많은 장르들 중, 곡수가 많은 순서대로 2개씩 출력하기.
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)

        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break

            result.append(index)
            genre_song_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))