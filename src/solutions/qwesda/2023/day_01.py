def get_problem_answer_a(input_data: bytes) -> str:
    answer = 0

    input_data_list = input_data.decode('utf-8').splitlines()

    for input_data in input_data_list:
        input_data_length = len(input_data)

        for i in range(0, input_data_length, 1):
            if input_data[i].isdigit():
                answer += int(input_data[i]) * 10
                break

        for i in range(input_data_length - 1, -1, -1):
            if input_data[i].isdigit():
                answer += int(input_data[i])
                break

    return str(answer)


def get_problem_answer_b_v1(input_data: bytes) -> str:
    answer = 0

    input_data_list = input_data.decode('utf-8').splitlines()

    input_data_list = input_data.decode('utf-8').splitlines()

    for input_data in input_data_list:
        input_data_length = len(input_data)

        for i in range(0, input_data_length, 1):
            if input_data[i].isdigit():
                answer += int(input_data[i]) * 10
                break
            elif input_data[i:i+3] == 'one':
                answer += 10
                break
            elif input_data[i:i+3] == 'two':
                answer += 20
                break
            elif input_data[i:i+5] == 'three':
                answer += 30
                break
            elif input_data[i:i+4] == 'four':
                answer += 40
                break
            elif input_data[i:i+4] == 'five':
                answer += 50
                break
            elif input_data[i:i+3] == 'six':
                answer += 60
                break
            elif input_data[i:i+5] == 'seven':
                answer += 70
                break
            elif input_data[i:i+5] == 'eight':
                answer += 80
                break
            elif input_data[i:i+4] == 'nine':
                answer += 90
                break

        for i in range(input_data_length - 1, -1, -1):
            if input_data[i].isdigit():
                answer += int(input_data[i])
                break
            elif input_data[i:i+3] == 'one':
                answer += 1
                break
            elif input_data[i:i+3] == 'two':
                answer += 2
                break
            elif input_data[i:i+5] == 'three':
                answer += 3
                break
            elif input_data[i:i+4] == 'four':
                answer += 4
                break
            elif input_data[i:i+4] == 'five':
                answer += 5
                break
            elif input_data[i:i+3] == 'six':
                answer += 6
                break
            elif input_data[i:i+5] == 'seven':
                answer += 7
                break
            elif input_data[i:i+5] == 'eight':
                answer += 8
                break
            elif input_data[i:i+4] == 'nine':
                answer += 9
                break

    return str(answer)


def get_problem_answer_b_v2(input_data: bytes) -> str:
    answer = 0

    input_data_list = input_data.decode('utf-8').splitlines()

    for input_data in input_data_list:
        input_data_length = len(input_data)

        for i in range(0, input_data_length, 1):
            char = input_data[i]
            remaining_char_length = input_data_length - i

            if remaining_char_length >= 3 and input_data[i] == 'o':
                if input_data[i+1] == 'n' and input_data[i+2] == 'e':
                    answer += 10
                    break
            elif input_data[i] == 't':
                if remaining_char_length >= 3 and input_data[i+1] == 'w' and input_data[i+2] == 'o':
                    answer += 20
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'h' and input_data[i+2] == 'r' and input_data[i+3] == 'e' and input_data[i+4] == 'e':
                    answer += 30
                    break
            elif remaining_char_length >= 4 and input_data[i] == 'f':
                if input_data[i+1] == 'o' and input_data[i+2] == 'u' and input_data[i+3] == 'r':
                    answer += 40
                    break
                elif input_data[i+1] == 'i' and input_data[i+2] == 'v' and input_data[i+3] == 'e':
                    answer += 50
                    break
            elif input_data[i] == 's':
                if remaining_char_length >= 3 and input_data[i+1] == 'i' and input_data[i+2] == 'x':
                    answer += 60
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'e' and input_data[i+2] == 'v' and input_data[i+3] == 'e' and input_data[i+4] == 'n':
                    answer += 70
                    break
            elif remaining_char_length >= 5 and input_data[i] == 'e':
                if input_data[i+1] == 'i' and input_data[i+2] == 'g' and input_data[i+3] == 'h' and input_data[i+4] == 't':
                    answer += 80
                    break
            elif remaining_char_length >= 4 and input_data[i] == 'n':
                if input_data[i+1] == 'i' and input_data[i+2] == 'n' and input_data[i+3] == 'e':
                    answer += 90
                    break
            elif char.isdigit():
                answer += int(input_data[i]) * 10
                break

        for i in range(input_data_length - 1, -1, -1):
            char = input_data[i]
            remaining_char_length = input_data_length - i

            if remaining_char_length >= 3 and input_data[i] == 'o':
                if input_data[i+1] == 'n' and input_data[i+2] == 'e':
                    answer += 1
                    break
            elif input_data[i] == 't':
                if remaining_char_length >= 3 and input_data[i+1] == 'w' and input_data[i+2] == 'o':
                    answer += 2
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'h' and input_data[i+2] == 'r' and input_data[i+3] == 'e' and input_data[i+4] == 'e':
                    answer += 3
                    break
            elif remaining_char_length >= 4 and input_data[i] == 'f':
                if input_data[i+1] == 'o' and input_data[i+2] == 'u' and input_data[i+3] == 'r':
                    answer += 4
                    break
                elif input_data[i+1] == 'i' and input_data[i+2] == 'v' and input_data[i+3] == 'e':
                    answer += 5
                    break
            elif input_data[i] == 's':
                if remaining_char_length >= 3 and input_data[i+1] == 'i' and input_data[i+2] == 'x':
                    answer += 6
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'e' and input_data[i+2] == 'v' and input_data[i+3] == 'e' and input_data[i+4] == 'n':
                    answer += 7
                    break
            elif remaining_char_length >= 5 and input_data[i] == 'e':
                if input_data[i+1] == 'i' and input_data[i+2] == 'g' and input_data[i+3] == 'h' and input_data[i+4] == 't':
                    answer += 8
                    break
            elif remaining_char_length >= 4 and input_data[i] == 'n':
                if input_data[i+1] == 'i' and input_data[i+2] == 'n' and input_data[i+3] == 'e':
                    answer += 9
                    break
            elif char.isdigit():
                answer += int(input_data[i])
                break

    return str(answer)


def get_problem_answer_b_v3(input_data: bytes) -> str:
    answer = 0

    input_data_list = input_data.decode('utf-8').splitlines()

    for input_data in input_data_list:
        input_data_length = len(input_data)

        for i in range(0, input_data_length, 1):
            char = input_data[i]
            remaining_char_length = input_data_length - i

            if remaining_char_length >= 3 and char == 'o':
                if input_data[i+1] == 'n' and input_data[i+2] == 'e':
                    answer += 10
                    break
            elif char == 't':
                if remaining_char_length >= 3 and input_data[i+1] == 'w' and input_data[i+2] == 'o':
                    answer += 20
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'h' and input_data[i+2] == 'r' and input_data[i+3] == 'e' and input_data[i+4] == 'e':
                    answer += 30
                    break
            elif remaining_char_length >= 4 and char == 'f':
                if input_data[i+1] == 'o' and input_data[i+2] == 'u' and input_data[i+3] == 'r':
                    answer += 40
                    break
                elif input_data[i+1] == 'i' and input_data[i+2] == 'v' and input_data[i+3] == 'e':
                    answer += 50
                    break
            elif char == 's':
                if remaining_char_length >= 3 and input_data[i+1] == 'i' and input_data[i+2] == 'x':
                    answer += 60
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'e' and input_data[i+2] == 'v' and input_data[i+3] == 'e' and input_data[i+4] == 'n':
                    answer += 70
                    break
            elif remaining_char_length >= 5 and char == 'e':
                if input_data[i+1] == 'i' and input_data[i+2] == 'g' and input_data[i+3] == 'h' and input_data[i+4] == 't':
                    answer += 80
                    break
            elif remaining_char_length >= 4 and char == 'n':
                if input_data[i+1] == 'i' and input_data[i+2] == 'n' and input_data[i+3] == 'e':
                    answer += 90
                    break
            elif char == '1':
                answer += 10
                break
            elif char == '2':
                answer += 20
                break
            elif char == '3':
                answer += 30
                break
            elif char == '4':
                answer += 40
                break
            elif char == '5':
                answer += 50
                break
            elif char == '6':
                answer += 60
                break
            elif char == '7':
                answer += 70
                break
            elif char == '8':
                answer += 80
                break
            elif char == '9':
                answer += 90
                break

        for i in range(input_data_length - 1, -1, -1):
            char = input_data[i]
            remaining_char_length = input_data_length - i

            if remaining_char_length >= 3 and char == 'o':
                if input_data[i+1] == 'n' and input_data[i+2] == 'e':
                    answer += 1
                    break
            elif char == 't':
                if remaining_char_length >= 3 and input_data[i+1] == 'w' and input_data[i+2] == 'o':
                    answer += 2
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'h' and input_data[i+2] == 'r' and input_data[i+3] == 'e' and input_data[i+4] == 'e':
                    answer += 3
                    break
            elif remaining_char_length >= 4 and char == 'f':
                if input_data[i+1] == 'o' and input_data[i+2] == 'u' and input_data[i+3] == 'r':
                    answer += 4
                    break
                elif input_data[i+1] == 'i' and input_data[i+2] == 'v' and input_data[i+3] == 'e':
                    answer += 5
                    break
            elif char == 's':
                if remaining_char_length >= 3 and input_data[i+1] == 'i' and input_data[i+2] == 'x':
                    answer += 6
                    break
                elif remaining_char_length >= 5 and input_data[i+1] == 'e' and input_data[i+2] == 'v' and input_data[i+3] == 'e' and input_data[i+4] == 'n':
                    answer += 7
                    break
            elif remaining_char_length >= 5 and char == 'e':
                if input_data[i+1] == 'i' and input_data[i+2] == 'g' and input_data[i+3] == 'h' and input_data[i+4] == 't':
                    answer += 8
                    break
            elif remaining_char_length >= 4 and char == 'n':
                if input_data[i+1] == 'i' and input_data[i+2] == 'n' and input_data[i+3] == 'e':
                    answer += 9
                    break
            elif char == '1':
                answer += 1
                break
            elif char == '2':
                answer += 2
                break
            elif char == '3':
                answer += 3
                break
            elif char == '4':
                answer += 4
                break
            elif char == '5':
                answer += 5
                break
            elif char == '6':
                answer += 6
                break
            elif char == '7':
                answer += 7
                break
            elif char == '8':
                answer += 8
                break
            elif char == '9':
                answer += 9
                break

    return str(answer)
