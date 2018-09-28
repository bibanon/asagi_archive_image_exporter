#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     26-09-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# StdLib
import logging
import argparse
import os
import csv
# Remote libraries
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
# local
from common import *# Things like logging setup






def dump_partial_table(connection_string, table_name, csv_filepath, start_from, stop_at=None):
    logging.debug('dump_partial_table() locals() = {0!r}'.format(locals()))# Record arguments
    # https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy

    Base = automap_base()

    engine = create_engine(connection_string, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite

    Base.prepare(engine, reflect=True)

    # Map the tables
    Images = Base.classes[table_name]

    session = Session(engine, autoflush=False)

##    # Select all rows
##    all_images_q = session.query(Images)
##    logging.info('len(all_images_q.all()) = {0}'.format(len(all_images_q.all())))

##    # Select the subset as or more recent than the supplied value
##    new_images_q = all_images_q.filter(Images.media >= u'debug/g/image/153/2/1532795456190.png')
##    logging.info('len(new_images_q.all()) = {0}'.format(len(new_images_q.all())))

    if stop_at:
        # Select the subset between the supplied values
        range_images_q = session.query(Images)\
            .filter(Images.media >= start_from)\
            .filter(Images.media >= stop_at)
    else:
        # Select the range greater than or equal to the supplied value
        range_images_q = session.query(Images)\
            .filter(Images.media >= start_from)
    logging.info('len(range_images_q.all()) = {0}'.format(len(range_images_q.all())))

    with open(csv_filepath, 'w') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        # Write header
        header = Images.__table__.columns.keys()
        outcsv.writerow(header)

        # Write records
        for record in range_images_q.all():# Write only images in the specified range
            outcsv.writerow([getattr(record, c) for c in header ])

    logging.info('Finished dumping table {0} to {1}'.format(table_name, csv_filepath))
    return


def dump_table(connection_string, table_name, csv_filepath):
    logging.debug('dump_table() args = {0!r}'.format(locals()))# Record arguments
    # https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy

    Base = automap_base()

    engine = create_engine(connection_string, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite

    Base.prepare(engine, reflect=True)

    # Map the tables
    Images = Base.classes[table_name]

    session = Session(engine, autoflush=False)

    q = session.query(Images)

    with open(csv_filepath, 'w') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        # Write header
        header = Images.__table__.columns.keys()
        logging.debug('header = {0!r}'.format(header))
        outcsv.writerow(header)

        # Store actual rows
        for record in q.all():
            outcsv.writerow([getattr(record, c) for c in header ])

    logging.info('Finished dumping table {0} to {1}'.format(table_name, csv_filepath))
    return


def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')
    import config

##    # Dump a table
##    dump_table(
##        connection_string=config.CONNECT_STRING,
##        table_name=config.TABLE_NAME,
##        csv_filepath=config.CSV_FILEPATH
##    )

    # Dump a range within a table
    dump_partial_table(
        connection_string=config.CONNECT_STRING,
        table_name=config.TABLE_NAME,
        csv_filepath=config.CSV_FILEPATH,
        start_from='1536638719722.webm',
        stop_at=None
    )

    logging.warning('exiting dev()')
    return


def cli():
    """Command line running"""
    # Handle command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('connection_string', help='connection_string',
                    type=str)
    parser.add_argument('table_name', help='table_name',
                    type=str)
    parser.add_argument('csv_filepath', help='csv_filepath',
                    type=int)
    parser.add_argument('start_from', help='start_from',
                    type=str)
    args = parser.parse_args()

    logging.debug('args: {0!r}'.format(args))# Record CLI arguments

    dump_partial_table(
        connection_string=args.connection_string,
        table_name=args.table_name,
        csv_filepath=args.csv_filepath,
        start_from=args.start_from,
        stop_at=None
    )

    logging.info('exiting cli()')
    return


def main():
##    dev()
    cli()
    return


if __name__ == '__main__':
    setup_logging(os.path.join("debug", "step1_dump_img_table.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info( "Program finished.")
