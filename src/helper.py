def load_env():
    import pathlib
    import os

    current_directory = pathlib.Path(__file__).parent.absolute()
    env_file_path = current_directory.parent / 'env_vars.env'

    if env_file_path.exists():
        with open(env_file_path) as f:
            for line in f:
                if '=' in line:
                    key, value = line.split('=')
                    key, value = key.strip(), value.strip()

                    os.environ[key] = value
