import shelve
from enum import Enum
from typing import List
from Parser_sql.ast_nodes import SimpleSelect


FILENAME = "./tables"
def read_binary_file():
    with shelve.open(FILENAME) as tables:
        tables["users"] = {
            'data':
                [
                    {
                        'id': 1,
                        'age': 12
                    },
                    {
                        'id': 2,
                        'age': 23
                    },
                    {
                        'id': 3,
                        'age': 45
                    }
                ]
        }
        tables["cats"] = {
            'data':
                [
                    {
                        'id': 1,
                        'name': 'Tom',
                        'age': 12
                    }
                ]
        }


class OperandCondition:
    operand: str


def select_query(query: SimpleSelect):
    lp = query._where[0]
    if(query._where[1].isdigit()):
        rp = int(query._where[1])
    else:
        rp = query._where[1]
    operand = query._oper
    database_name = query._table_name
    with shelve.open(FILENAME) as tables:
        if database_name in tables:
            print('-----------------------------------------------------------------------------')
            for table in tables.items():
                print(table)
            print('-----------------------------------------------------------------------------')
            for data in tables[database_name]['data']:
                if operand == '=':
                    if data[lp] == rp:
                        print(data)
                if operand == '>':
                    if data[lp] > rp:
                        print(data)
                if operand == '<':
                    if data[lp] < rp:
                        print(data)
                if operand == '>=':
                    if data[lp] >= rp:
                        print(data)
                if operand == '<=':
                    if data[lp] <= rp:
                        print(data)


def delete_all_query(query: SimpleSelect):
    with shelve.open(FILENAME) as tables:
        del tables[query._table_name]

        for table in tables.items():
            print(table)


def delete_query(query: SimpleSelect):
    lp = query._where[0]
    if (query._where[1].isdigit()):
        rp = int(query._where[1])
    else:
        rp = query._where[1]

    operand = query._oper
    database_name = query._table_name
    with shelve.open(FILENAME) as tables:
        if database_name in tables:
            print(tables[database_name])
            for data in tables[database_name]['data']:
                if operand == '=':
                    if data[lp] == rp:
                        print(data)
                if operand == '>':
                    if data[lp] > rp:
                        print(data)
                if operand == '<':
                    if data[lp] < rp:
                        print(data)
                if operand == '>=':
                    if data[lp] >= rp:
                        print(data)
                if operand == '<=':
                    if data[lp] <= rp:
                        print(data)

        for table in tables.items():
            print(table)


def insert_query(database_name,keys: list, values: list):
    with shelve.open(FILENAME) as tables:
        tables[database_name] = {
            'data': generate_dict_list(keys, values)
        }
        for table in tables.items():
            print(table)


def generate_dict_list(keys: list, values: list):
    dic_list = []
    for key in keys:
        dic_list.append({key: values[keys.index(key)]})
    return dic_list



