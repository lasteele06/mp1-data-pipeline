import argparse
import logging
import sys
from pathlib import Path
from data_loaders import load_data
from data_processor import process_data, create_cleaning_report

logger = logging.getLogger(__name__)

def setup_logging(verbose=False):
    if verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )


def parse_arguments():
    parser = argparse.ArgumentParser(description="A simple data pipeline")

    parser.add_argument("--verbose", "-v",action="store_true",help="Enable verbose logging")

    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file"
    )

    parser.add_argument(
        "--config", "-c",
        required=True,
        help="Path to the configuration file"
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to the output file"
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
        f"config={args.config}, output={args.output}"
    )

    if not validate_input(args.input):
        sys.exit(1)

    if not validate_input(args.config):
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)

    data_before = data.copy()

    try:
        cleaned_data = process_data(data, config)
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(data_before, cleaned_data)
    print(report)

   
    logger.info(f"process complete: {len(data_before)} rows before, {len(cleaned_data)} rows after cleaning.")
    cleaned_data.to_csv(args.output, index=False)

    logger.info(f"Cleaned data saved to {args.output}")





if __name__ == "__main__":
    main()