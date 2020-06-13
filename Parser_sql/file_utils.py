import shelve
from enum import Enum
from typing import List
from Parser_sql.ast_nodes import SimpleSelect, Insert, CreateTable, Delete


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
        tables["dogs"] = {
            'data':
                [
                    {
                        'id': 1,
                        'name': 'pes'
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
            print('-------------------------------------BEFORE SELECT---------------------------------')
            for table in tables.items():
                print(table)
            print('-------------------------------------AFTER SELECT---------------------------------')
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


def delete_all_query(query: Delete):
    with shelve.open(FILENAME) as tables:
        print('-------------------------------BEFORE DELETE-------------------------------------')
        for table in tables.items():
            print(table)
        del tables[query._table_name]

        print('-------------------------------AFTER DELETE-------------------------------------')
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
        print('-------------------------------AFTER DELETE-------------------------------------')
        for table in tables.items():
            print(table)


def insert_query(query: Insert):
    database_name = query._table_name
    keys = query._column_name
    values = query._values
    with shelve.open(FILENAME) as tables:
        print('-------------------------------BEFORE INSERT----------------------------------------------')
        for table in tables.items():
            print(table)
        dogs = tables[database_name]['data']
        dogs = dogs + generate_dict_list(keys, values)
        tables[database_name] = {
            'data': dogs
        }
        print('-------------------------------AFTER INSERT-------------------------------------')
        for table in tables.items():
            print(table)


def create_table_query(query: CreateTable):
    with shelve.open(FILENAME) as tables:
        print('-------------------------------------BEFORE CREATE---------------------------------')
        for table in tables.items():
            print(table)
        tables[query._table_name] = {
            'data': []
        }
        print('-------------------------------------AFTER CREATE---------------------------------')
        for table in tables.items():
            print(table)


def generate_dict_list(keys: list, values: list):
    dic_list = []
    for key in keys:
        dic_list.append({key: values[keys.index(key)]})
    return dic_list



