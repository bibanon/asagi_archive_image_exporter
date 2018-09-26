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
# local
from common import *# Things like logging setup
import db_test_config












def dev():
    """For development/debugging in IDE/editor without CLI arguments"""
    logging.warning('running dev()')

    db_name = 'asagi experiments 2018-7'

    # Dump a table
##    dump_table(
##        database,
##        table_name='',
##        start_position=0,
##        output_filepath=os.path.join('debug', 'step1_dump_img_table', 'img.csv')
##    )

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











# https://stackoverflow.com/questions/2952366/dump-csv-from-sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine(db_test_config.SQLITE_CONNECT_STRING, echo=True)# https://docs.sqlalchemy.org/en/latest/core/engines.html#sqlite

Base.prepare(engine, reflect=True)

# Map the tables
Images = Base.classes.g_images

session = Session(engine, autoflush=False)


import csv

def export():

    q = session.query(Images)

    file = './data/g_images.csv'

    with open(file, 'w') as csvfile:
        outcsv = csv.writer(csvfile, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)

        header = Images.__table__.columns.keys()

        outcsv.writerow(header)

        for record in q.all():
            outcsv.writerow([getattr(record, c) for c in header ])

if __name__ == "__main__":
    export()












