import argparse
import logging
import os

from . import utils as uts


def main():
    # Parser
    parser = argparse.ArgumentParser(description="Parsing the inputs to run the module.")
    parser.add_argument("-o", "--output_path", dest="output", help="Output path to store the results.")
    args = parser.parse_args()

    # Create output folder
    os.makedirs(args.output, exist_ok=True)

    # Logger
    logger = uts.set_up_logger(args.output)
    logger.info('Started')

    # Do
    logging.info("Running cleanimage...")
    logging.info('-' * 20)
    logging.info("Doing smart stuff...")
    logging.info('-' * 20)
    logging.info("Process finished!")


if __name__ == "__main__":
    main()
