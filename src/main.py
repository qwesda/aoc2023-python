import argparse
import os
import pathlib
import importlib
import importlib.util
import cProfile
import timeit

from helper import load_env


def load_problem_data(input_file_path: pathlib.Path) -> bytes:
    with open(input_file_path, 'rb') as f:
        return f.read()


def get_problem_answer(problem_file_path: pathlib.Path, problem_data: bytes, problem_part: str, is_test=False, measure_execution_time: bool=False, profile: bool=False) -> str:
    solution_module_spec = importlib.util.spec_from_file_location('problem', problem_file_path)
    solution_module = importlib.util.module_from_spec(solution_module_spec)
    solution_module_spec.loader.exec_module(solution_module)

    problem_answer_function_prefix = f'get_problem_answer_{problem_part}'
    any_problem_answer_function_found = False

    for problem_answer_function_name in dir(solution_module):
        if problem_answer_function_name.startswith(problem_answer_function_prefix):
            any_problem_answer_function_found = True
            problem_answer_function = getattr(solution_module, problem_answer_function_name)

            if not profile and not measure_execution_time:
                problem_answer = problem_answer_function(problem_data)

                if not is_test:
                    print(f'{problem_answer_function_name}() -> {problem_answer}')
                else:
                    print(f'{problem_answer_function_name}() -> {problem_answer} [test]')
            elif measure_execution_time:
                timeit_result = timeit.timeit(f'problem_answer_function(problem_data)', globals=locals(), number=10000)
                print(f'{problem_answer_function_name}() 10k executions took -> {timeit_result:.4f} seconds')
            elif profile:
                cProfile.runctx(f'problem_answer_function(problem_data)', globals(), locals(), sort='cumtime')

    # if not any_problem_answer_function_found:
    #     raise Exception(f'Solution file `{problem_file_path}` does not have a function that starts with `{problem_answer_function_prefix}`')


def main():
    is_pycharm_debug_run = 'IPYTHONENABLE' in os.environ

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--user', type=str, help="who's solutions to use", choices=['stan', 'doga', 'qwesda'], required=True)
    arg_parser.add_argument('--problem', type=str, help='Problem to run', required=True)

    args = arg_parser.parse_args()

    problem_year, problem_day = args.problem.split('/')

    repository_directory = pathlib.Path(__file__).parent.parent.absolute()
    current_directory = pathlib.Path(__file__).parent.absolute()

    input_file_path = repository_directory / 'inputs' / args.user / problem_year / f'day_{problem_day}.txt'
    input_test_a_file_path = repository_directory / 'inputs' / args.user / problem_year / f'day_{problem_day}-test-a.txt'
    input_test_b_file_path = repository_directory / 'inputs' / args.user / problem_year / f'day_{problem_day}-test-b.txt'
    solution_file_path = current_directory / 'solutions' / args.user / problem_year / f'day_{problem_day}.py'

    if not solution_file_path.exists():
        raise Exception(f'Problem file {solution_file_path.relative_to(repository_directory)} does not exist')

    if input_test_a_file_path.exists():
        get_problem_answer(solution_file_path, load_problem_data(input_test_a_file_path), 'a', is_test=True)

    if input_test_b_file_path.exists():
        get_problem_answer(solution_file_path, load_problem_data(input_test_b_file_path), 'b', is_test=True)

    if input_file_path.exists():
        problem_data = load_problem_data(input_file_path)
        get_problem_answer(solution_file_path, problem_data, 'a')
        get_problem_answer(solution_file_path, problem_data, 'b')

    if not is_pycharm_debug_run:
        get_problem_answer(solution_file_path, problem_data, 'a', measure_execution_time=True)
        get_problem_answer(solution_file_path, problem_data, 'b', measure_execution_time=True)

        get_problem_answer(solution_file_path, problem_data, 'a', profile=True)
        get_problem_answer(solution_file_path, problem_data, 'b', profile=True)


if __name__ == '__main__':
    load_env()
    main()
