# Created by Noah Kantrowitz on 2007-07-04.
# Copyright (c) 2007 Noah Kantrowitz. All rights reserved.

from trac.db import Table, Column

name = 'mastertickets'
version = 2
tables = [
    Table('mastertickets', key=('source','dest'))[
        Column('source', type='integer'),
        Column('dest', type='integer'),
    ],
]

def convert_to_int(data):
    """Convert both source and dest in the mastertickets table to ints."""
    for row in data['mastertickets'][1]:
        for i, (n1, n2) in enumerate(row):
            row[i] = [int(n1), int(n2)]

migrations = [
    (xrange(1,2), convert_to_int),
]