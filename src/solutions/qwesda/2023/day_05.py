import itertools


def get_problem_answer_a_v1(input_data: bytes) -> str:
    answer = None
    seeds = None
    maps = {}
    steps = []
    maps_from = {}
    current_parser_map = None

    for line in input_data.splitlines():
        if seeds is None:
            seeds = line.split()[1:]
        elif line == b'':
            pass
        elif line[-4:] == b'map:':
            current_parser_map = line.split()[0]
            from_map, _, to_map = current_parser_map.split(b'-')

            steps.append(from_map)
            maps_from[from_map] = current_parser_map
            maps[current_parser_map] = []
        else:
            a, b, c = line.split()
            maps[current_parser_map].append((int(a), int(b), int(c)))

    for seed in seeds:
        current_id = int(seed)

        for step in steps:
            for dest_start, source_start, range_len in maps[maps_from[step]]:
                if source_start <= current_id < source_start + range_len:
                    current_id = dest_start + (current_id - source_start)
                    break

        if answer is not None:
            answer = min(current_id, answer)
        else:
            answer = current_id

    return str(answer)


def get_problem_answer_b_v1(input_data: bytes) -> str:
    def resolve(step, input_range_start, input_range_end, trail=None):
        for source_range_start, source_range_end, offset in maps[maps_from[step]]:
            intersection_start = max(input_range_start, source_range_start)
            intersection_end = min(input_range_end, source_range_end)

            if intersection_end > intersection_start:
                if next_steps[step] not in maps_from:
                    yield intersection_start + offset
                else:
                    yield from resolve(next_steps[step], intersection_start + offset, intersection_end + offset, trail)

    answer = None
    seed_ranges = None
    maps = {}
    next_steps = {}
    maps_from = {}
    current_parser_map = None

    for line in input_data.splitlines():
        if seed_ranges is None:
            seed_ranges = list(itertools.batched([int(x) for x in line.split()[1:]], 2))
        elif line == b'':
            pass
        elif line[-4:] == b'map:':
            current_parser_map = line.split()[0]
            from_map, _, to_map = current_parser_map.split(b'-')

            next_steps[from_map] = to_map
            maps_from[from_map] = current_parser_map
            maps[current_parser_map] = []
        else:
            a, b, c = line.split()
            maps[current_parser_map].append((int(a), int(b), int(c)))

    for map_key in maps.keys():
        map, new_map = maps[map_key], []
        map.sort(key=lambda x: x[1])

        last_upper_bound = 0

        for (dest_n, source_n, length) in map:
            if source_n > last_upper_bound:
                new_map.append((last_upper_bound, source_n, 0))

            new_map.append((source_n, source_n + length, dest_n - source_n))

            last_upper_bound = source_n + length

        new_map.append((last_upper_bound, 2 ** 32, 0))

        maps[map_key] = new_map

    for seed_range_start, seed_range_length in seed_ranges:
        for location_id in resolve(b'seed', seed_range_start, seed_range_start + seed_range_length):
            if location_id is None:
                continue

            if answer is not None:
                answer = min(location_id, answer)
            else:
                answer = location_id

    return str(answer)
