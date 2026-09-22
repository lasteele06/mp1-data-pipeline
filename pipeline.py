import argparse
import logging
import sys
from unicodedata import name
import verbose
from pathlib import Path

logger = logging.getLogger(name)

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

    pass

def validate_input(filepath):

    pass

def main():

    pass

if __name__ =+ "__main__":
main()
    
    