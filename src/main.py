import argparse
import pathlib

from helper import load_env


def load_problem_data(input_file_path: pathlib.Path) -> list[str]:
    with open(input_file_path) as f:
        return [line.strip() for line in f]


def get_problem_answer(problem_file_path: pathlib.Path, problem_data: list[str]) -> str:
    import importlib.util

    solution_module_spec = importlib.util.spec_from_file_location('problem', problem_file_path)
    solution_module = importlib.util.module_from_spec(solution_module_spec)
    solution_module_spec.loader.exec_module(solution_module)

    if not hasattr(solution_module, 'get_problem_answer'):
        raise Exception(f'Solution file {problem_file_path} does not have a get_problem_answer function')

    return solution_module.get_problem_answer(problem_data)


def main():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--user', type=str, help="who's solutions to use", choices=['stan', 'doga', 'qwesda'], required=True)
    arg_parser.add_argument('--problem', type=str, help='Problem to run', required=True)

    args = arg_parser.parse_args()

    repository_directory = pathlib.Path(__file__).parent.parent.absolute()
    current_directory = pathlib.Path(__file__).parent.absolute()

    input_file_path = repository_directory / 'inputs' / args.user / f'day_{args.problem}.txt'
    solution_file_path = current_directory / 'solutions' / args.user / f'day_{args.problem}.py'

    if not input_file_path.exists():
        raise Exception(f'Input file {input_file_path.relative_to(repository_directory)} does not exist')

    if not solution_file_path.exists():
        raise Exception(f'Problem file {solution_file_path.relative_to(repository_directory)} does not exist')

    problem_data = load_problem_data(input_file_path)
    problem_answer = get_problem_answer(solution_file_path, problem_data)

    print(problem_answer)


if __name__ == '__main__':
    load_env()
    main()
