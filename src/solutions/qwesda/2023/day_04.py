from collections import defaultdict


def get_problem_answer_a_v1(input_data: bytes) -> str:
    answer = 0

    for line in input_data.splitlines():
        _, line = line.split(b':', 2)
        line_part_1, line_part_2 = line.split(b'|', 2)

        winning_numbers = set(line_part_1.split())
        my_numbers = set(line_part_2.split())

        answer += int(2 ** (len(winning_numbers.intersection(my_numbers)) - 1))

    return str(answer)


def get_problem_answer_a_v2(input_data: bytes) -> str:
    answer = 0

    winning_numbers = set()
    my_numbers = set()
    in_header = True
    in_winning_numbers = False
    in_my_numbers = False
    current_number = 0

    for char in input_data:
        if in_header:
            if char == 0x3A:
                in_header, in_winning_numbers = False, True
                continue
        elif in_winning_numbers:
            if 0x30 <= char <= 0x39:
                current_number = current_number * 10 + char - 0x30
            elif char == 0x20 and current_number != 0:
                winning_numbers.add(current_number)
                current_number = 0
            elif char == 0x7C:
                in_winning_numbers, in_my_numbers = False, True
        elif in_my_numbers:
            if 0x30 <= char <= 0x39:
                current_number = current_number * 10 + char - 0x30
            elif char == 0x20 and current_number != 0:
                my_numbers.add(current_number)
                current_number = 0
            elif char == 0x0A:
                if current_number != 0:
                    my_numbers.add(current_number)

                answer += int(2 ** (len(winning_numbers.intersection(my_numbers)) - 1))

                in_my_numbers, in_header = False, True
                current_number = 0
                winning_numbers.clear()
                my_numbers.clear()

    return str(answer)


def get_problem_answer_b_v1(input_data: bytes) -> str:
    answer = 0
    card_multipliers = defaultdict(lambda: 1)

    for line in input_data.splitlines():
        header, line = line.split(b':', 2)
        card_id = int(header.split(b' ')[-1])
        line_part_1, line_part_2 = line.split(b'|', 2)

        winning_numbers = set([x for x in line_part_1.strip().split(b' ') if x != b''])
        my_numbers = set([x for x in line_part_2.strip().split(b' ') if x != b''])

        wins = len(winning_numbers.intersection(my_numbers))

        for x in range(card_id + 1, card_id + 1 + wins):
            card_multipliers[x] += card_multipliers[card_id]

        answer += card_multipliers[card_id]

    return str(answer)
