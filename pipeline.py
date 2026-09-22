import argparse
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

def setup_logging(verbose=False):
    if verbose:
        level= logging.DEBUG
    else:
        level= logging.INFO

    logging.basicConfig(
        level=level,
        format = "%(asctime)s %(levelname)s  %(message)s", 
        datefmt="%H:%M:%S"
     )
    pass

def parse_arguments():
    parser = argparse.ArgumentParser(description="A simple data pipeline")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--input", required=True, help="Path to the input file")
    parser.add_argument("--output", required=True, help="Path to the output file")
    return parser.parse_args()

def validate_input(filepath):
    path= Path(filepath)

    if not path.exists():
        logger.error(f"Input file {filepath} does not exist.")
        return False
    return True

def main():
    setup_logging(args.verbose)
    args = parse_arguments()
    validate_input(args.input)
    pass

if __name__ == "__main__":
    main()
    
    