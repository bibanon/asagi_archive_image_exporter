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





### https://www.blog.pythonlibrary.org/2010/09/10/sqlalchemy-connecting-to-pre-existing-databases/
##
##
##from sqlalchemy import create_engine, MetaData, Table
##from sqlalchemy.orm import mapper, sessionmaker
##
##class BoardClass(object):
##    """Represents a board we are running over"""
##    pass
##
###----------------------------------------------------------------------
##def loadSession():
##    """"""
##
##    return session
##
##if __name__ == "__main__":
##    # Load session
##    engine = create_engine(db_test_config.CONNECT_STRING, echo=True)
##
##    metadata = MetaData(engine)
##    table = Table('a', metadata, autoload=True)
##    mapper(BoardClass, table)
##
##    Session = sessionmaker(bind=engine)
##    session = Session()
##
##    # Get column names
##
##    # Read table
##    res = session.query(BoardClass).all()
####    print(res[1].timestamp)
##    for row_number in xrange(0, 1000):
##        print(res[row_number])








### https://stackoverflow.com/questions/4613465/using-python-to-write-mysql-query-to-csv-need-to-show-field-names
##import MySQLdb as dbapi
##import sys
##import csv
##
##
##dbQuery='SELECT * FROM `asagi experiments 2018-7`.a;'
##
##db=dbapi.connect(
##    host=db_test_config.IP,
##    user=db_test_config.USERNAME,
##    passwd=db_test_config.PASSWEORD
##)
##
##cur=db.cursor()
##cur.execute(dbQuery)
##
##result = cur.fetchall()
##
###Getting Field Header names
##column_names = [i[0] for i in cur.description]
##fp = open('Result_Set.csv' 'w')
##myFile = csv.writer(fp, lineterminator = '\n') #use lineterminator for windows
##myFile.writerow(column_names)
##myFile.writerows(result)
##fp.close()




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
    setup_logging(os.path.join("debug", "step1_dump_img_table.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical("Unhandled exception!")
        logging.exception(e)
    logging.info( "Program finished.")
