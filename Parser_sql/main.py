from Parser_sql.sqlast import parse
from Parser_sql.printer import print_tree
from Parser_sql.utils import *
from Parser_sql.file_utils import select_query, delete_query,  create_table_query, insert_query, \
    read_binary_file, update_query


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
    create_table_query(ast_tree._queries[0]._statements[0])
    insert_query(ast_tree._queries[0]._statements[1])
    select_query(ast_tree._queries[0]._statements[2])
    select_query(ast_tree._queries[0]._statements[3])
    select_query(ast_tree._queries[0]._statements[4])
    delete_query(ast_tree._queries[0]._statements[5])  # delete with clause
    delete_query(ast_tree._queries[0]._statements[6])  # delete all
    update_query(ast_tree._queries[0]._statements[7])
    update_query(ast_tree._queries[0]._statements[8])



if __name__ == '__main__':
    main()
