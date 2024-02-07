#!/usr/bin/env python3
''' filtered_logger.py '''

import re
from typing import List


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
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt
