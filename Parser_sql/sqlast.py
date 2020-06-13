import astpretty

from antlr_ast.ast import (
    AliasNode,
    BaseNode as AstNode,  # used in other tests
    parse as parse_ast,
    process_tree,
    BaseNodeTransformer,
    Terminal,
)
from antlr_ast.inputstream import CaseTransformInputStream
from antlr_ast.marshalling import AstEncoder, get_decoder

from Parser_sql.ast_nodes import QueriesList, Query, CreateTable, ColumnDefinition, SimpleSelect, Delete, Insert
from Parser_sql.sql_parser.sqlParser import sqlParser
from Parser_sql.sql_parser.sqlLexer import sqlLexer


class Grammar:
    @staticmethod
    def Lexer(arg):
        return sqlLexer(arg)

    @staticmethod
    def Parser(arg):
        return sqlParser(arg)


class RootQueryNode(AliasNode):
    _fields_spec = ['queries']
    _rules = ['root']

    def build_ast(self):
        return QueriesList([query.build_ast() for query in self.queries])


class QueryNode(AliasNode):
    _fields_spec = ['statements=query_statements']
    _rules = ['query_statements_list']

    def build_ast(self):
        return Query([statement.build_ast() for statement in self.statements])


class CreateTableNode(AliasNode):
    _fields_spec = ['db_name=create_table_stmt.database_name', 'table_name=create_table_stmt.table_name',
                    'columns=create_table_stmt.columns']

    #'constraints=create_table_stmt.constraints','select=create_table_stmt.select_stmt'

    _rules = ['create_table_statement']

    def build_ast(self):
        return CreateTable(self.db_name, self.table_name,
                           [column_definition.build_ast() for column_definition in self.columns])


class SimpSelectNode(AliasNode):
    _fields_spec = ['columns=simp_select_stmt.columns','table_name=simp_select_stmt.table_name', 'where=simp_select_stmt.where.expr1', 'oper=simp_select_stmt.where.some_operator']

    _rules = ['simp_select_statement']

    def build_ast(self):
        return SimpleSelect(self.columns, self.table_name, self.where, self.oper)


class ColumnDefinitionNode(AliasNode):
    _fields_spec = ['name=column_name', 'type=type_name.name']
    _rules = ['column_def']

    def build_ast(self):
        return ColumnDefinition(self.name, self.type)

class DeleteNode(AliasNode):
    _fields_spec = ['table_name=delete_stmt.qualified_table_name']

    _rules = ['delete_statement']

    def build_ast(self):
        return Delete(self.table_name)


class InsertNode(AliasNode):
    _fields_spec = ['table_name=insert_stmt.table_name', 'values=insert_stmt.expr1', 'column_name=insert_stmt.column_name']

    _rules = ['insert_statement']

    def build_ast(self):
        return Insert(self.table_name, self.values, self.column_name)


# TODO: add _rules property and implement build_ast method
# class FactoredStatementNode(AliasNode):
#     _fields_spec = ['select_parts', 'operators']
#
#
# class SelectNode(AliasNode):
#     _fields_spec = ['columns', 'tables', 'where', 'group_by', 'having']
#
#
# class ExprNode(AliasNode):
#     _fields_spec = ['database_name', 'table_name', 'column_name', 'select_stmt', 'expr', 'literal_value']


class Transformer(BaseNodeTransformer):
    def visit_Terminal(self, terminal: Terminal) -> Terminal:
        return terminal.value


def parse(text, start="root", **kwargs):
    antlr_tree = parse_ast(
        Grammar, text, start, **kwargs
    )

    Transformer.bind_alias_nodes([RootQueryNode, QueryNode, CreateTableNode, ColumnDefinitionNode, SimpSelectNode, DeleteNode, InsertNode])
    simple_tree = process_tree(antlr_tree, transformer_cls=Transformer)

    return simple_tree.build_ast()
