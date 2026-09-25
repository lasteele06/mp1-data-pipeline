import argparse
import logging
import sys
from pathlib import Path
from data_loaders import load_data

logger = logging.getLogger(__name__)

def setup_logging(verbose=False):
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s  %(message)s",
        datefmt="%H:%M:%S"
    )


def parse_arguments():
    parser = argparse.ArgumentParser(description="A simple data pipeline")

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file"
    )

    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to the output file"
    )

    parser.add_argument(
        "--format", "-f",
        choices=["csv", "json"],
        default="csv",
        help="Output file format (default: csv)"
    )

    return parser.parse_args()


def validate_input(filepath):
    path = Path(filepath)

    if not path.is_file():
        logger.error(f"Input file {filepath} does not exist.")
        return False

    logger.info(f"Input file validated: {filepath}")
    return True


def main():
    args = parse_arguments()

    setup_logging(args.verbose)

    logger.debug(
        f"Arguments parsed: input={args.input}, "
        f"output={args.output}, format={args.format}"
    )

    if not validate_input(args.input):
        sys.exit(1)

    try:
        data = load_data(args.input)
    except ValueError:
        sys.exit(1)


if __name__ == "__main__":
    main()