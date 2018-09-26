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





def dump_partial_table(connection_string, table_name, csv_output_path, start_from, stop_at):
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

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


def dump_table(connection_string, table_name, csv_output_path):
    # https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy
    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

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

    logging.warning('exiting dev()')
    return


def main():
##    dev()
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




connection_string=db_test_config.SQLITE_CONNECT_STRING
table_name=db_test_config.SQLITE_TABLE_NAME
csv_output_path=db_test_config.CSV_OUTPUT_FILEPATH





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






