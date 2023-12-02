def get_problem_answer_a(input_data_list: list[str]) -> str:
    answer = 0

    for input_data in input_data_list:
        game_id_data, game_draws_data = input_data.split(':')

        game_id = int(game_id_data.split(' ')[1])
        game_is_impossible = False

        for game_draw in game_draws_data.split(';'):
            for cubes in game_draw.split(','):
                cube_count, cube_color = cubes.strip().split(' ')
                cube_count = int(cube_count)

                if cube_color == 'red' and cube_count > 12:
                    game_is_impossible = True
                    break
                elif cube_color == 'green' and cube_count > 13:
                    game_is_impossible = True
                    break
                elif cube_color == 'blue' and cube_count > 14:
                    game_is_impossible = True
                    break

            if game_is_impossible:
                break

        if not game_is_impossible:
            answer += game_id

    return str(answer)


def get_problem_answer_b(input_data_list: list[str]) -> str:
    answer = 0

    for input_data in input_data_list:
        _, game_draws_data = input_data.split(':')
        min_red_dice = 0
        min_green_dice = 0
        min_blue_dice = 0

        for game_draw in game_draws_data.split(';'):
            for cubes in game_draw.split(','):
                cube_count, cube_color = cubes.strip().split(' ')
                cube_count = int(cube_count)

                if cube_color == 'red':
                    min_red_dice = max(min_red_dice, cube_count)
                elif cube_color == 'green':
                    min_green_dice = max(min_green_dice, cube_count)
                elif cube_color == 'blue':
                    min_blue_dice = max(min_blue_dice, cube_count)

        answer += min_red_dice * min_green_dice * min_blue_dice

    return answer
