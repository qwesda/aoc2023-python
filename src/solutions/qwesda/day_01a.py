def get_problem_answer(input_data_list: list[str]) -> str:
    elf_highest_calories_count = 0
    elf_current_calories_count = 0

    for input_data in input_data_list:
        if input_data == '':
            if elf_highest_calories_count < elf_current_calories_count:
                elf_highest_calories_count = elf_current_calories_count

            elf_current_calories_count = 0
        else:
            elf_current_calories_count += int(input_data)

    return str(elf_highest_calories_count)
