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
import db_test_config





def dump_partial_table(connection_string, table_name, csv_output_path, start_from, stop_at=None):
    logging.debug('dump_partial_table() locals() = {0!r}'.format(locals()))# Record arguments

    Base = automap_base()

    engine = create_engine(connection_string, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite

    Base.prepare(engine, reflect=True)

    # Map the tables
    Images = Base.classes[table_name]

    session = Session(engine, autoflush=False)

    # Select all rows
    all_images_q = session.query(Images)
    logging.info('len(all_images_q.all()) = {0}'.format(len(all_images_q.all())))

    # Select the subset as or more recent than the supplied value
    new_images_q = all_images_q.filter(Images.media >= u'debug/g/image/153/2/1532795456190.png')
    logging.info('len(new_images_q.all()) = {0}'.format(len(new_images_q.all())))

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

    with open(csv_output_path, 'w') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        header = Images.__table__.columns.keys()

        outcsv.writerow(header)

        for record in range_images_q.all():# Write only images in the specified range
            outcsv.writerow([getattr(record, c) for c in header ])
    return


def dump_table(connection_string, table_name, csv_output_path):
    logging.debug('dump_table() locals() = {0!r}'.format(locals()))# Record arguments
    # https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy

    Base = automap_base()

    engine = create_engine(connection_string, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite

    Base.prepare(engine, reflect=True)

    # Map the tables
    Images = Base.classes[table_name]

    session = Session(engine, autoflush=False)

    q = session.query(Images)

    with open(csv_output_path, 'w') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        header = Images.__table__.columns.keys()

        outcsv.writerow(header)

        for record in q.all():
            outcsv.writerow([getattr(record, c) for c in header ])
    return


def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')

    db_name = 'asagi experiments 2018-7'

    # Dump a table
    dump_table(
        connection_string=db_test_config.SQLITE_CONNECT_STRING,
        table_name=db_test_config.SQLITE_TABLE_NAME,
        csv_output_path=db_test_config.CSV_OUTPUT_FILEPATH
    )

    # Dump a range within a table
    dump_partial_table(
        connection_string=db_test_config.SQLITE_CONNECT_STRING,
        table_name=db_test_config.SQLITE_TABLE_NAME,
        csv_output_path=db_test_config.CSV_OUTPUT_FILEPATH,
        start_from='debug/g/image/153/2/1532795456190.png',
        stop_at=None
    )

    logging.warning('exiting dev()')
    return


def main():
    dev()
    return


if __name__ == '__main__':
    setup_logging(os.path.join("debug", "db_test.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info("Program finished.")



##
##connection_string=db_test_config.SQLITE_CONNECT_STRING
##table_name=db_test_config.SQLITE_TABLE_NAME
##csv_output_path=db_test_config.CSV_OUTPUT_FILEPATH
##
##
##Base = automap_base()
##
##engine = create_engine(connection_string, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite
##
##Base.prepare(engine, reflect=True)
##
### Map the tables
##Images = Base.classes[table_name]
##
##session = Session(engine, autoflush=False)
##
##all_images_q = session.query(Images)
##new_images_q = all_images_q.filter(Images.media >= u'debug/g/image/153/2/1532795456190.png')
##
##print('len(all_images_q.all()) = {0}'.format(len(all_images_q.all())))
##print('len(new_images_q.all()) = {0}'.format(len(new_images_q.all())))
####with open(csv_output_path, 'w') as csvfile:
####    outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)
####
####    header = Images.__table__.columns.keys()
####
####    outcsv.writerow(header)
####
####    for record in q.all():
####        outcsv.writerow([getattr(record, c) for c in header ])

