#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     27-09-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# StdLib
import logging
import argparse
import os
import csv
import zipfile
# Remote libraries
# local
from common import *# Things like logging setup






def add_to_zip(zip_obj, filepath, internal_path):
    try:
        logging.debug('Zipping {0!r} as {1!r}'.format(filepath, internal_path))
        zip_obj.write(filepath, internal_path)
    except WindowsError, err:
        logging.error(err)
    return


def generate_image_filepath(board_dir, filename):
    # Expects filename to look like: '1536631035276.webm'
    # Outputs: 'BASE/153/6/1536631035276.webm'
    # boards/<boardName>/<thumb or image>/<char 0-3>/<char 4-5>/<full image name>
    # base/image/1536/63/1536631035276.webm
    assert(len(filename) > 4)# We can't generate a path is this is lower, and the value is based on unix time so should always be over 1,000,000
    media_filepath = os.path.join(board_dir, filename[0:4], filename[4:6], filename)# string positions 0,1,2,3/4,5/filename
    return media_filepath


def generate_full_image_filepath(images_dir, board_name, filename):
    # boards/<boardName>/<thumb or image>/<char 0-3>/<char 4-5>/<full image name>
    board_dir = os.path.join(images_dir, 'image', board_name)
    full_image_filepath = generate_image_filepath(board_dir, filename)
    return full_image_filepath


def generate_thumbnail_image_filepath(images_dir, board_name, filename):
    # boards/<boardName>/<thumb or image>/<char 0-3>/<char 4-5>/<full image name>
    board_dir = os.path.join(images_dir, 'thumb', board_name)
    full_image_filepath = generate_image_filepath(board_dir, filename)
    return full_image_filepath


def zip_from_csv(csv_path, images_dir, zip_path, board_name):
    logging.info('Zipping files in {0} to {1}'.format(csv_path, zip_path))
    row_counter = 0
    with zipfile.ZipFile(zip_path, 'w') as myzip:
        # First, add the CSV to the zip
        add_to_zip(
            zip_obj=myzip,
            filepath=os.path.join(csv_path),
            internal_path=os.path.basename(csv_path)
        )

        # Add images from each row in the CSV file
        with open(csv_path, 'rb', ) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)
            for row in reader:
                row_counter += 1
                if (row_counter % 100 == 0):
                    logging.info('Processed {0} rows.'.format(row_counter))
                # Add media to zip
                if row['media']:
                    add_to_zip(
                        zip_obj=myzip,
                        filepath=generate_full_image_filepath(
                            images_dir=images_dir,
                            board_name=board_name,
                            filename=row['media']
                        ),
                        internal_path=row['media']
                    )

                # Add preview_op to zip
                if row['preview_op']:
                    add_to_zip(
                        zip_obj=myzip,
                        filepath=generate_thumbnail_image_filepath(
                            images_dir=images_dir,
                            board_name=board_name,
                            filename=row['preview_op']
                        ),
                        internal_path=row['preview_op']
                    )

                # Add preview_reply to zip
                if row['preview_reply']:
                    add_to_zip(
                        zip_obj=myzip,
                        filepath=generate_thumbnail_image_filepath(
                            images_dir=images_dir,
                            board_name=board_name,
                            filename=row['preview_reply']
                        ),
                        internal_path=row['preview_reply']
                    )
    logging.info('Finished zipping files from {0} rows in {1} to {2}'.format(row_counter, csv_path, zip_path))
    return


def cli():
    """Command line running"""
    # Handle command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path', help='csv_path',
                    type=str)
    parser.add_argument('images_dir', help='images_dir',
                    type=str)
    parser.add_argument('zip_path', help='zip_path',
                    type=str)
    parser.add_argument('board_name', help='board_name',
                    type=str)
    args = parser.parse_args()

    logging.debug('args: {0!r}'.format(args))# Record CLI arguments

    zip_from_csv(
        csv_path=args.csv_path,
        images_dir=args.images_dir,
        zip_path=args.zip_path,
        board_name=args.board_name
    )

    logging.info('exiting cli()')
    return


def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')

    import config

    csv_path = config.CSV_FILEPATH
    zip_path = config.ZIP_PATH
    images_dir = '.'
    board_name = config.BOARD_NAME
    zip_from_csv(
        csv_path=csv_path,
        images_dir=images_dir,
        zip_path=zip_path,
        board_name=board_name,
    )

    logging.warning('exiting dev()')
    return


def main():
    cli()
##    dev()
    return

if __name__ == '__main__':
    setup_logging(os.path.join("debug", "step2_zip.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info("Program finished.")







