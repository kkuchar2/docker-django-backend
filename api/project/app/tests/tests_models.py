from django.test import TestCase


def db_table_exists(table, cursor=None):
    try:
        if not cursor:
            from django.db import connection
            cursor = connection.cursor()
        if not cursor:
            raise Exception
        table_names = connection.introspection.get_table_list(cursor)
    except:
        raise Exception("unable to determine if the table '%s' exists" % table)
    else:
        return table in table_names


class MyAppBaseTestCase(TestCase):

    def test_create_user(self):
        if not db_table_exists("test_db"):
            self.fail("Table: {} does not exist".format("test_db"))

