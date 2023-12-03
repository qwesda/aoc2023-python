def get_problem_answer_a(input_data_list: list[str]) -> str:
    answer = 0
    non_symbols = '0123456789.'

    for pos_y, curr_line in enumerate(input_data_list):
        line_length = len(curr_line)
        prev_line = input_data_list[pos_y - 1] if pos_y > 0 else ('.' * line_length)
        next_line = input_data_list[pos_y + 1] if pos_y < len(input_data_list) - 1 else ('.' * line_length)

        current_number = 0
        current_number_has_symbol_adjacent = False
        current_number_complete = False

        for pos_x in range(line_length):
            current_char = curr_line[pos_x]

            if current_char.isdigit():
                if current_number == 0 and pos_x > 0:
                    if prev_line[pos_x - 1] not in non_symbols or curr_line[pos_x - 1] not in non_symbols or next_line[pos_x - 1] not in non_symbols:
                        current_number_has_symbol_adjacent = True

                current_number = current_number * 10 + int(current_char)

                if not current_number_has_symbol_adjacent:
                    if prev_line[pos_x] not in non_symbols or curr_line[pos_x] not in non_symbols or next_line[pos_x] not in non_symbols:
                        current_number_has_symbol_adjacent = True

                if pos_x == line_length - 1:
                    current_number_complete = True
            elif current_number > 0:
                current_number_complete = True

            if current_number_complete:
                if not current_number_has_symbol_adjacent and pos_x < line_length:
                    if prev_line[pos_x] not in non_symbols or curr_line[pos_x] not in non_symbols or next_line[pos_x] not in non_symbols:
                        current_number_has_symbol_adjacent = True

                if current_number_has_symbol_adjacent:
                    answer += current_number

                current_number = 0
                current_number_has_symbol_adjacent = False
                current_number_complete = False

    return str(answer)


def get_problem_answer_b(input_data_list: list[str]) -> str:
    answer = 0

    for pos_y, curr_line in enumerate(input_data_list):
        line_length = len(curr_line)
        prev_line = input_data_list[pos_y - 1] if pos_y > 0 else ('.' * line_length)
        next_line = input_data_list[pos_y + 1] if pos_y < len(input_data_list) - 1 else ('.' * line_length)

        for pos_x in range(line_length):
            current_char = curr_line[pos_x]

            if current_char == '*':
                prev_left_number_scanner, prev_left_number = '', None
                curr_left_number_scanner, curr_left_number = '', None
                next_left_number_scanner, next_left_number = '', None

                for number_scan_pos in range(pos_x - 1, -1, -1):
                    if prev_left_number_scanner is not None:
                        if prev_line[number_scan_pos].isdigit():
                            prev_left_number_scanner = prev_line[number_scan_pos] + prev_left_number_scanner

                        if number_scan_pos == 0 or not prev_line[number_scan_pos].isdigit():
                            prev_left_number = int(prev_left_number_scanner) if prev_left_number_scanner else prev_left_number
                            prev_left_number_scanner = None

                    if curr_left_number_scanner is not None:
                        if curr_line[number_scan_pos].isdigit():
                            curr_left_number_scanner = curr_line[number_scan_pos] + curr_left_number_scanner

                        if number_scan_pos == 0 or not curr_line[number_scan_pos].isdigit():
                            curr_left_number = int(curr_left_number_scanner) if curr_left_number_scanner else curr_left_number
                            curr_left_number_scanner = None

                    if next_left_number_scanner is not None:
                        if next_line[number_scan_pos].isdigit():
                            next_left_number_scanner = next_line[number_scan_pos] + next_left_number_scanner

                        if number_scan_pos == 0 or not next_line[number_scan_pos].isdigit():
                            next_left_number = int(next_left_number_scanner) if next_left_number_scanner else next_left_number
                            next_left_number_scanner = None

                    if prev_left_number_scanner is None and curr_left_number_scanner is None and next_left_number_scanner is None:
                        break

                # print(f'found left numbers {prev_left_number}, {curr_left_number}, {next_left_number}')

                prev_right_number_scanner, prev_right_number = '', None
                curr_right_number_scanner, curr_right_number = '', None
                next_right_number_scanner, next_right_number = '', None

                if prev_line[pos_x].isdigit():
                    if prev_left_number is not None:
                        prev_right_number_scanner = str(prev_left_number) + prev_line[pos_x]
                    else:
                        prev_right_number_scanner = prev_line[pos_x]

                    prev_left_number = None

                if next_line[pos_x].isdigit():
                    if next_left_number is not None:
                        next_right_number_scanner = str(next_left_number) + next_line[pos_x]
                    else:
                        next_right_number_scanner = next_line[pos_x]

                    next_left_number = None

                for number_scan_pos in range(pos_x + 1, line_length, 1):
                    if prev_right_number_scanner is not None:
                        if prev_line[number_scan_pos].isdigit():
                            prev_right_number_scanner += prev_line[number_scan_pos]

                        if number_scan_pos == line_length - 1 or not prev_line[number_scan_pos].isdigit():
                            prev_right_number = int(prev_right_number_scanner) if prev_right_number_scanner else prev_right_number
                            prev_right_number_scanner = None

                    if curr_right_number_scanner is not None:
                        if curr_line[number_scan_pos].isdigit():
                            curr_right_number_scanner += curr_line[number_scan_pos]

                        if number_scan_pos == line_length - 1 or not curr_line[number_scan_pos].isdigit():
                            curr_right_number = int(curr_right_number_scanner) if curr_right_number_scanner else curr_right_number
                            curr_right_number_scanner = None

                    if next_right_number_scanner is not None:
                        if next_line[number_scan_pos].isdigit():
                            next_right_number_scanner += next_line[number_scan_pos]

                        if number_scan_pos == line_length - 1 or not next_line[number_scan_pos].isdigit():
                            next_right_number = int(next_right_number_scanner) if next_right_number_scanner else next_right_number
                            next_right_number_scanner = None

                    if prev_right_number_scanner is None and curr_right_number_scanner is None and next_right_number_scanner is None:
                        break

                non_empty_numbers = []

                if prev_left_number:
                    non_empty_numbers.append(prev_left_number)

                if curr_left_number:
                    non_empty_numbers.append(curr_left_number)

                if next_left_number:
                    non_empty_numbers.append(next_left_number)

                if prev_right_number:
                    non_empty_numbers.append(prev_right_number)

                if curr_right_number:
                    non_empty_numbers.append(curr_right_number)

                if next_right_number:
                    non_empty_numbers.append(next_right_number)

                print(f'non_empty_numbers: {non_empty_numbers}')

                if len(non_empty_numbers) == 2:
                    answer += non_empty_numbers[0] * non_empty_numbers[1]

    return str(answer)
