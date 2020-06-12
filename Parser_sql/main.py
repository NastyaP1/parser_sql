import sys

import astpretty
from antlr4 import FileStream
from antlr4.tree import Trees

from sqlast import parse

from Parser_sql.printer import print_tree
from Parser_sql.sql_parser.sqlLexer import sqlLexer
from Parser_sql.sql_parser.sqlParser import sqlParser, CommonTokenStream
from utils import *
from file_utils import *
from Parser_sql.file_utils import select_query


def main():
    # input_stream = FileStream('./sql_stmt.sql')
    # lexer = sqlLexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = sqlParser(stream)
    # tree = parser.root()
    #
    # t = Trees.Trees.toStringTree(tree, parser.ruleNames)
    # print(t)

    ast_tree = parse(read_file('./sql_stmt.sql'))
    print_tree(ast_tree)
    read_binary_file()

    select_query(ast_tree._queries[0]._statements[1])



if __name__ == '__main__':
    main()
