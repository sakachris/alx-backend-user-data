#!/usr/bin/env python3
''' filtered_logger.py '''

import re
import os
import mysql.connector
import logging
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def extract_pattern(fields: List[str], separator: str) -> str:
    ''' Generate the regular expression pattern for extracting fields '''
    return rf'(?P<field>{ "|".join(fields) })=[^{separator}]*'


def replace_pattern(redaction: str) -> str:
    ''' Generate the replacement pattern '''
    return rf'\g<field>={redaction}'


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    ''' Filters a log line '''
    extract = extract_pattern(fields, separator)
    replace = replace_pattern(redaction)
    return re.sub(extract, replace, message)


class RedactingFormatter(logging.Formatter):
    ''' Redacting Formatter class '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' formatting log record '''
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def get_logger() -> logging.Logger:
    ''' Setup logger named user_data '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Connect to the database '''
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    dbname = os.getenv('PERSONAL_DATA_DB_NAME', '')

    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        port=3306,
        database=dbname
    )
    return db
