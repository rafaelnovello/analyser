# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv


def get_delimiter(path):
    sniffer = csv.Sniffer()
    with open(path, 'rb') as doc:
        dialect = sniffer.sniff(doc.readline())
    return dialect.delimiter