import shelve
from enum import Enum
from typing import List
from Parser_sql.ast_nodes import SimpleSelect, Insert, CreateTable, Delete, Update


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
                        'name': 'Tom'
                    },
                    {
                        'id': 2,
                        'name': 'Tom2'
                    },
                    {
                        'id': 3,
                        'name': 'Tom'
                    },
                    {
                        'id': 4,
                        'name': 'Kotik'
                    }
                ]
        }
        tables["dogs"] = {
            'data':
                [
                    {
                        'id': 1,
                        'name': 'pes'
                    },
                    {
                        'id': 2,
                        'name': 'pes'
                    },
                    {
                        'id': 3,
                        'name': 'pes2'
                    }
                ]
        }


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
            print_all(tables)
            print('-------------------------------------AFTER SELECT---------------------------------')
            for data in tables[database_name]['data']:
                if operand == '=':
                    if data[lp] == rp:
                        result = []
                        if query._column_results[0] == '*':
                            print(data)
                        else:
                            for res in query._column_results:
                                result.append(res + ': ' + str(data[res]))
                            print(result)
                if operand == '>':
                    result = []
                    if query._column_results[0] == '*':
                        print(data)
                    else:
                        for res in query._column_results:
                            result.append(res + ': ' + str(data[res]))
                        print(result)
                if operand == '<':
                    result = []
                    if query._column_results[0] == '*':
                        print(data)
                    else:
                        for res in query._column_results:
                            result.append(res + ': ' + str(data[res]))
                        print(result)
                if operand == '>=':
                    result = []
                    if query._column_results[0] == '*':
                        print(data)
                    else:
                        for res in query._column_results:
                            result.append(res + ': ' + str(data[res]))
                        print(result)
                if operand == '<=':
                    result = []
                    if query._column_results[0] == '*':
                        print(data)
                    else:
                        for res in query._column_results:
                            result.append(res + ': ' + str(data[res]))
                        print(result)


def delete_query(query: Delete):
    if query._where == None:
        print('-------------------------------BEFORE DELETE-------------------------------------')
        with shelve.open(FILENAME) as tables:
            print_all(tables)
            tables[query._table_name] = {
                'data': []
            }

            print('-------------------------------AFTER DELETE-------------------------------------')
            print_all(tables)
    else:
        lp = query._where[0]
        if (query._where[1].isdigit()):
            rp = int(query._where[1])
        else:
            rp = query._where[1]

        operand = query._oper
        table_name = query._table_name
        with shelve.open(FILENAME) as tables:
            if table_name in tables:
                print('-------------------------------BEFORE DELETE-------------------------------------')
                print_all(tables)
                res = tables[table_name]['data']
                if len(tables[table_name]['data']) == 0:
                    print("Table is empty")
                else:
                    for data in tables[table_name]['data']:
                        if operand == '=':
                            if data[lp] == rp:
                                res.remove(data)
                                tables[table_name] = {
                                    'data': res
                                }
                        if operand == '>':
                            if data[lp] > rp:
                                res.remove(data)
                                tables[table_name] = {
                                    'data': res
                                }
                        if operand == '<':
                            if data[lp] < rp:
                                res.remove(data)
                                tables[table_name] = {
                                    'data': res
                                }
                        if operand == '>=':
                            if data[lp] >= rp:
                                res.remove(data)
                                tables[table_name] = {
                                    'data': res
                                }
                        if operand == '<=':
                            if data[lp] <= rp:
                                res.remove(data)
                                tables[table_name] = {
                                    'data': res
                                }
                    print('-------------------------------AFTER DELETE-------------------------------------')
                    print_all(tables)


def insert_query(query: Insert):
    table_name = query._table_name
    keys = query._column_name
    values = query._values
    with shelve.open(FILENAME) as tables:
        print('-------------------------------BEFORE INSERT----------------------------------------------')
        print_all(tables)
        data = tables[table_name]['data']
        data.append(generate_dict_list(keys, values))
        tables[table_name] = {
            'data': data
        }
        print('-------------------------------AFTER INSERT-------------------------------------')
        print_all(tables)


def update_query(query: Update):
    res = []
    keys = query._column_name
    values = query._values
    table_name = query._table_name
    if query._where == None:
        print('-------------------------------BEFORE UPDATE-------------------------------------')
        with shelve.open(FILENAME) as tables:
            print_all(tables)
            for data in tables[table_name]['data']:
                data.update(generate_dict_list(keys, values))
                res.append(data)
            tables[table_name] = {
                'data': res
            }
            print('-------------------------------AFTER UPDATE-------------------------------------')
            print_all(tables)
    else:
        lp = query._where[0]
        if (query._where[1].isdigit()):
            rp = int(query._where[1])
        else:
            rp = query._where[1]

        operand = query._oper

        with shelve.open(FILENAME) as tables:
            if table_name in tables:
                print('-------------------------------BEFORE UPDATE-------------------------------------')
                print_all(tables)
                if len(tables[table_name]['data']) == 0:
                    print("Table is empty")
                else:
                    for data in tables[table_name]['data']:
                        if operand == '=':
                            if data[lp] == rp:
                                data.update(generate_dict_list(keys, values))
                        if operand == '>':
                            if data[lp] > rp:
                                data.update(generate_dict_list(keys, values))
                        if operand == '<':
                            if data[lp] < rp:
                                data.update(generate_dict_list(keys, values))
                        if operand == '>=':
                            if data[lp] >= rp:
                                data.update(generate_dict_list(keys, values))
                        if operand == '<=':
                            if data[lp] <= rp:
                                data.update(generate_dict_list(keys, values))
                        res.append(data)
                    print('-------------------------------AFTER UPDATE-------------------------------------')
                    tables[table_name] = {
                        'data': res
                    }
                    print_all(tables)


def create_table_query(query: CreateTable):
    with shelve.open(FILENAME) as tables:
        print('-------------------------------------BEFORE CREATE---------------------------------')
        print_all(tables)
        tables[query._table_name] = {
            'data': []
        }
        print('-------------------------------------AFTER CREATE---------------------------------')
        print_all(tables)


def generate_dict_list(keys: list, values: list):
    return {key: values[keys.index(key)] for key in keys}


def print_all(tables):
    for table in tables.items():
        print(table)

