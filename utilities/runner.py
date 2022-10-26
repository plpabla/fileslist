import subprocess
from pathlib import Path
import argparse
from datetime import datetime
import os

PROJECT_NAME = "fileslist"


def generate_unique_run_id(already_called=[False]) -> str:
    if already_called[0]:
        return already_called[0]

    datetime_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    already_called[0] = datetime_id
    return datetime_id


def store_run_id_in_env(run_id: str, env_var_name: str = "RUN_ID") -> None:
    os.environ[env_var_name] = run_id


def get_allure_report_dir() -> str:
    return os.path.join("logs", generate_unique_run_id())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--dry-run", required=False, action="store_true", help="Dry run"
    )
    parser.add_argument(
        "-p", "--print-stdout", required=False, action="store_true", help="Print stdout"
    )
    parser.add_argument(
        "-j",
        "--json",
        required=False,
        action="store_true",
        help="Create json report file",
    )
    parser.add_argument(
        "-a", "--allure", required=False, action="store_true", help="Run Allure report"
    )
    parser.add_argument(
        "--behave-options", required=False, type=str, help="Extra behave options"
    )
    arg = parser.parse_args()
    return arg


def prepare_command_from_args() -> str:
    arg = parse_args()
    json_filename = os.path.join("logs", generate_unique_run_id() + "_behave.json")
    allure_dir = get_allure_report_dir()

    cmd = f"python manage.py behave --no-capture --no-logcapture "
    cmd = cmd + (f"-f json.pretty -o {json_filename} " if arg.json else "")
    cmd = cmd + (
        f"-f allure_behave.formatter:AllureFormatter -o {allure_dir} "
        if arg.allure
        else ""
    )
    cmd = cmd + ("--dry-run " if arg.dry_run else "")
    cmd = cmd + (arg.behave_options if arg.behave_options else "")

    return cmd


if __name__ == "__main__":
    command = prepare_command_from_args()
    print(f"Running test suite...\n\t{command}")

    # Project is one level up and then under PROJECT_NAME
    PROJECT_DIR = Path(__file__).resolve().parent.parent.joinpath(PROJECT_NAME)

    # Get & store run id
    run_id = generate_unique_run_id()
    store_run_id_in_env(run_id)

    # Run the test
    res = subprocess.run(command, shell=True, capture_output=True, cwd=PROJECT_DIR)
    print(f"Process exited with status code {res.returncode}.")

    if parse_args().print_stdout:
        print(res.stdout.decode())

    if parse_args().allure:
        subprocess.run(
            f"allure serve {get_allure_report_dir()}", shell=True, cwd=PROJECT_DIR
        )
