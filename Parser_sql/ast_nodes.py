from typing import List


class ASTNode:
    def __init__(self):
        pass


class QueryStatement(ASTNode):
    def __init__(self):
        super().__init__()


class Query(ASTNode):
    _fields = ['_statements']

    def __init__(self, statements: List[QueryStatement]):
        super().__init__()
        self._statements = statements


class ColumnDefinition(ASTNode):
    _fields = ['_name', '_type']

    def __init__(self, column_name: str, column_type: str):
        super().__init__()
        self._name = column_name
        self._type = column_type
#
    # _fields_spec = ['db_name=create_table_stmt.database_name', 'table_name=create_table_stmt.table_name',
    #                 'columns=create_table_stmt.columns', 'constraints=create_table_stmt.constraints',
    #                 'select=create_table_stmt.select_stmt']


class CreateTable(QueryStatement):
    _fields = ['_db_name', '_table_name', '_columns_definitions']

    def __init__(self, db_name: str, table_name: str, columns_definitions=List[ColumnDefinition]):
        super().__init__()
        self._db_name = db_name
        self._table_name = table_name
        self._columns_definitions = columns_definitions



class SimpleSelect(QueryStatement):
    _fields = ['_column_results', '_table_name', '_where', '_oper']

    def __init__(self,column_results: str, table_name: str, where=str, oper=str):
        super().__init__()
        self._column_results = column_results
        self._table_name = table_name
        self._where = where
        self._oper = oper

class Insert(QueryStatement):
    _fields = ['_table_name', '_values', '_column_name']

    def __init__(self, table_name: str, values: str, column_name: str):
        super().__init__()
        self._values = values
        self._table_name = table_name
        self._column_name = column_name


class Delete(QueryStatement):
    _fields = ['_table_name']

    def __init__(self,table_name: str):
        super().__init__()
        self._table_name = table_name


class QueriesList(ASTNode):
    _fields = ['_queries']

    def __init__(self, queries: List[Query]):
        super().__init__()
        self._queries = queries
