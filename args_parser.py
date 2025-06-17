import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Traveling Salesman Problem Solver using Evolutionary Algorithm"
    )

    parser.add_argument(
        "--mode",
        type=str,
        choices=["benchmark", "single"],
        required=True,
        help="Mode to run the program: 'benchmark' or 'single'"
    )

    # Example: add more arguments later if needed
    # parser.add_argument("--config-file", type=str, default="config/default.json")

    return parser.parse_args()


def args_not_found():
    print("No arguments provided. Please use the --mode argument to specify the mode.")
    print("Example usage: python main.py --mode benchmark or python main.py --mode single")
    exit(1)
