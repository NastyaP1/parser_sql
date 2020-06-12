# Generated from /Users/anastasiapereslavceva/Downloads/Sql_parser/Parser_sql/sql.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete listener for a parse tree produced by sqlParser.
class sqlListener(ParseTreeListener):

    # Enter a parse tree produced by sqlParser#root.
    def enterRoot(self, ctx:sqlParser.RootContext):
        pass

    # Exit a parse tree produced by sqlParser#root.
    def exitRoot(self, ctx:sqlParser.RootContext):
        pass


    # Enter a parse tree produced by sqlParser#query_statements_list.
    def enterQuery_statements_list(self, ctx:sqlParser.Query_statements_listContext):
        pass

    # Exit a parse tree produced by sqlParser#query_statements_list.
    def exitQuery_statements_list(self, ctx:sqlParser.Query_statements_listContext):
        pass


    # Enter a parse tree produced by sqlParser#vacuum_statement.
    def enterVacuum_statement(self, ctx:sqlParser.Vacuum_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#vacuum_statement.
    def exitVacuum_statement(self, ctx:sqlParser.Vacuum_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#create_index_statement.
    def enterCreate_index_statement(self, ctx:sqlParser.Create_index_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#create_index_statement.
    def exitCreate_index_statement(self, ctx:sqlParser.Create_index_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#create_table_statement.
    def enterCreate_table_statement(self, ctx:sqlParser.Create_table_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#create_table_statement.
    def exitCreate_table_statement(self, ctx:sqlParser.Create_table_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#reindex_statement.
    def enterReindex_statement(self, ctx:sqlParser.Reindex_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#reindex_statement.
    def exitReindex_statement(self, ctx:sqlParser.Reindex_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#update_statement.
    def enterUpdate_statement(self, ctx:sqlParser.Update_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#update_statement.
    def exitUpdate_statement(self, ctx:sqlParser.Update_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#insert_statement.
    def enterInsert_statement(self, ctx:sqlParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#insert_statement.
    def exitInsert_statement(self, ctx:sqlParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#simp_select_statement.
    def enterSimp_select_statement(self, ctx:sqlParser.Simp_select_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#simp_select_statement.
    def exitSimp_select_statement(self, ctx:sqlParser.Simp_select_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#drop_index_statement.
    def enterDrop_index_statement(self, ctx:sqlParser.Drop_index_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#drop_index_statement.
    def exitDrop_index_statement(self, ctx:sqlParser.Drop_index_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#drop_table_statement.
    def enterDrop_table_statement(self, ctx:sqlParser.Drop_table_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#drop_table_statement.
    def exitDrop_table_statement(self, ctx:sqlParser.Drop_table_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#delete_statement.
    def enterDelete_statement(self, ctx:sqlParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by sqlParser#delete_statement.
    def exitDelete_statement(self, ctx:sqlParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by sqlParser#delete_statement_limited.
    def enterDelete_statement_limited(self, ctx:sqlParser.Delete_statement_limitedContext):
        pass

    # Exit a parse tree produced by sqlParser#delete_statement_limited.
    def exitDelete_statement_limited(self, ctx:sqlParser.Delete_statement_limitedContext):
        pass


    # Enter a parse tree produced by sqlParser#reindex_stmt.
    def enterReindex_stmt(self, ctx:sqlParser.Reindex_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#reindex_stmt.
    def exitReindex_stmt(self, ctx:sqlParser.Reindex_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#create_index_stmt.
    def enterCreate_index_stmt(self, ctx:sqlParser.Create_index_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#create_index_stmt.
    def exitCreate_index_stmt(self, ctx:sqlParser.Create_index_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx:sqlParser.Create_table_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx:sqlParser.Create_table_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#simp_select_stmt.
    def enterSimp_select_stmt(self, ctx:sqlParser.Simp_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#simp_select_stmt.
    def exitSimp_select_stmt(self, ctx:sqlParser.Simp_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#result_column_1.
    def enterResult_column_1(self, ctx:sqlParser.Result_column_1Context):
        pass

    # Exit a parse tree produced by sqlParser#result_column_1.
    def exitResult_column_1(self, ctx:sqlParser.Result_column_1Context):
        pass


    # Enter a parse tree produced by sqlParser#some_operator.
    def enterSome_operator(self, ctx:sqlParser.Some_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#some_operator.
    def exitSome_operator(self, ctx:sqlParser.Some_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#expr1.
    def enterExpr1(self, ctx:sqlParser.Expr1Context):
        pass

    # Exit a parse tree produced by sqlParser#expr1.
    def exitExpr1(self, ctx:sqlParser.Expr1Context):
        pass


    # Enter a parse tree produced by sqlParser#column_constraint.
    def enterColumn_constraint(self, ctx:sqlParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by sqlParser#column_constraint.
    def exitColumn_constraint(self, ctx:sqlParser.Column_constraintContext):
        pass


    # Enter a parse tree produced by sqlParser#foreign_key_clause.
    def enterForeign_key_clause(self, ctx:sqlParser.Foreign_key_clauseContext):
        pass

    # Exit a parse tree produced by sqlParser#foreign_key_clause.
    def exitForeign_key_clause(self, ctx:sqlParser.Foreign_key_clauseContext):
        pass


    # Enter a parse tree produced by sqlParser#table_constraint.
    def enterTable_constraint(self, ctx:sqlParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by sqlParser#table_constraint.
    def exitTable_constraint(self, ctx:sqlParser.Table_constraintContext):
        pass


    # Enter a parse tree produced by sqlParser#column_def.
    def enterColumn_def(self, ctx:sqlParser.Column_defContext):
        pass

    # Exit a parse tree produced by sqlParser#column_def.
    def exitColumn_def(self, ctx:sqlParser.Column_defContext):
        pass


    # Enter a parse tree produced by sqlParser#type_name.
    def enterType_name(self, ctx:sqlParser.Type_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#type_name.
    def exitType_name(self, ctx:sqlParser.Type_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#indexed_column.
    def enterIndexed_column(self, ctx:sqlParser.Indexed_columnContext):
        pass

    # Exit a parse tree produced by sqlParser#indexed_column.
    def exitIndexed_column(self, ctx:sqlParser.Indexed_columnContext):
        pass


    # Enter a parse tree produced by sqlParser#compound_select_stmt.
    def enterCompound_select_stmt(self, ctx:sqlParser.Compound_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#compound_select_stmt.
    def exitCompound_select_stmt(self, ctx:sqlParser.Compound_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#factored_select_stmt.
    def enterFactored_select_stmt(self, ctx:sqlParser.Factored_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#factored_select_stmt.
    def exitFactored_select_stmt(self, ctx:sqlParser.Factored_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx:sqlParser.Simple_select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx:sqlParser.Simple_select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#select_stmt.
    def enterSelect_stmt(self, ctx:sqlParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#select_stmt.
    def exitSelect_stmt(self, ctx:sqlParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#select_or_values.
    def enterSelect_or_values(self, ctx:sqlParser.Select_or_valuesContext):
        pass

    # Exit a parse tree produced by sqlParser#select_or_values.
    def exitSelect_or_values(self, ctx:sqlParser.Select_or_valuesContext):
        pass


    # Enter a parse tree produced by sqlParser#vacuum_stmt.
    def enterVacuum_stmt(self, ctx:sqlParser.Vacuum_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#vacuum_stmt.
    def exitVacuum_stmt(self, ctx:sqlParser.Vacuum_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#update_stmt.
    def enterUpdate_stmt(self, ctx:sqlParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#update_stmt.
    def exitUpdate_stmt(self, ctx:sqlParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#update_stmt_limited.
    def enterUpdate_stmt_limited(self, ctx:sqlParser.Update_stmt_limitedContext):
        pass

    # Exit a parse tree produced by sqlParser#update_stmt_limited.
    def exitUpdate_stmt_limited(self, ctx:sqlParser.Update_stmt_limitedContext):
        pass


    # Enter a parse tree produced by sqlParser#insert_stmt.
    def enterInsert_stmt(self, ctx:sqlParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#insert_stmt.
    def exitInsert_stmt(self, ctx:sqlParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#drop_index_stmt.
    def enterDrop_index_stmt(self, ctx:sqlParser.Drop_index_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#drop_index_stmt.
    def exitDrop_index_stmt(self, ctx:sqlParser.Drop_index_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#drop_table_stmt.
    def enterDrop_table_stmt(self, ctx:sqlParser.Drop_table_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#drop_table_stmt.
    def exitDrop_table_stmt(self, ctx:sqlParser.Drop_table_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#delete_stmt.
    def enterDelete_stmt(self, ctx:sqlParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by sqlParser#delete_stmt.
    def exitDelete_stmt(self, ctx:sqlParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by sqlParser#delete_stmt_limited.
    def enterDelete_stmt_limited(self, ctx:sqlParser.Delete_stmt_limitedContext):
        pass

    # Exit a parse tree produced by sqlParser#delete_stmt_limited.
    def exitDelete_stmt_limited(self, ctx:sqlParser.Delete_stmt_limitedContext):
        pass


    # Enter a parse tree produced by sqlParser#qualified_table_name.
    def enterQualified_table_name(self, ctx:sqlParser.Qualified_table_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#qualified_table_name.
    def exitQualified_table_name(self, ctx:sqlParser.Qualified_table_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#expr.
    def enterExpr(self, ctx:sqlParser.ExprContext):
        pass

    # Exit a parse tree produced by sqlParser#expr.
    def exitExpr(self, ctx:sqlParser.ExprContext):
        pass


    # Enter a parse tree produced by sqlParser#with_clause.
    def enterWith_clause(self, ctx:sqlParser.With_clauseContext):
        pass

    # Exit a parse tree produced by sqlParser#with_clause.
    def exitWith_clause(self, ctx:sqlParser.With_clauseContext):
        pass


    # Enter a parse tree produced by sqlParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:sqlParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by sqlParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:sqlParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by sqlParser#ordering_term.
    def enterOrdering_term(self, ctx:sqlParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by sqlParser#ordering_term.
    def exitOrdering_term(self, ctx:sqlParser.Ordering_termContext):
        pass


    # Enter a parse tree produced by sqlParser#result_column.
    def enterResult_column(self, ctx:sqlParser.Result_columnContext):
        pass

    # Exit a parse tree produced by sqlParser#result_column.
    def exitResult_column(self, ctx:sqlParser.Result_columnContext):
        pass


    # Enter a parse tree produced by sqlParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx:sqlParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by sqlParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx:sqlParser.Table_or_subqueryContext):
        pass


    # Enter a parse tree produced by sqlParser#join_clause.
    def enterJoin_clause(self, ctx:sqlParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by sqlParser#join_clause.
    def exitJoin_clause(self, ctx:sqlParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by sqlParser#join_operator.
    def enterJoin_operator(self, ctx:sqlParser.Join_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#join_operator.
    def exitJoin_operator(self, ctx:sqlParser.Join_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#join_constraint.
    def enterJoin_constraint(self, ctx:sqlParser.Join_constraintContext):
        pass

    # Exit a parse tree produced by sqlParser#join_constraint.
    def exitJoin_constraint(self, ctx:sqlParser.Join_constraintContext):
        pass


    # Enter a parse tree produced by sqlParser#select_core.
    def enterSelect_core(self, ctx:sqlParser.Select_coreContext):
        pass

    # Exit a parse tree produced by sqlParser#select_core.
    def exitSelect_core(self, ctx:sqlParser.Select_coreContext):
        pass


    # Enter a parse tree produced by sqlParser#conflict_clause.
    def enterConflict_clause(self, ctx:sqlParser.Conflict_clauseContext):
        pass

    # Exit a parse tree produced by sqlParser#conflict_clause.
    def exitConflict_clause(self, ctx:sqlParser.Conflict_clauseContext):
        pass


    # Enter a parse tree produced by sqlParser#compound_operator.
    def enterCompound_operator(self, ctx:sqlParser.Compound_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#compound_operator.
    def exitCompound_operator(self, ctx:sqlParser.Compound_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#foreign_table.
    def enterForeign_table(self, ctx:sqlParser.Foreign_tableContext):
        pass

    # Exit a parse tree produced by sqlParser#foreign_table.
    def exitForeign_table(self, ctx:sqlParser.Foreign_tableContext):
        pass


    # Enter a parse tree produced by sqlParser#signed_number.
    def enterSigned_number(self, ctx:sqlParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by sqlParser#signed_number.
    def exitSigned_number(self, ctx:sqlParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by sqlParser#literal_value.
    def enterLiteral_value(self, ctx:sqlParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by sqlParser#literal_value.
    def exitLiteral_value(self, ctx:sqlParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by sqlParser#unary_operator.
    def enterUnary_operator(self, ctx:sqlParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by sqlParser#unary_operator.
    def exitUnary_operator(self, ctx:sqlParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by sqlParser#column_alias.
    def enterColumn_alias(self, ctx:sqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by sqlParser#column_alias.
    def exitColumn_alias(self, ctx:sqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by sqlParser#keyword.
    def enterKeyword(self, ctx:sqlParser.KeywordContext):
        pass

    # Exit a parse tree produced by sqlParser#keyword.
    def exitKeyword(self, ctx:sqlParser.KeywordContext):
        pass


    # Enter a parse tree produced by sqlParser#name.
    def enterName(self, ctx:sqlParser.NameContext):
        pass

    # Exit a parse tree produced by sqlParser#name.
    def exitName(self, ctx:sqlParser.NameContext):
        pass


    # Enter a parse tree produced by sqlParser#database_name.
    def enterDatabase_name(self, ctx:sqlParser.Database_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#database_name.
    def exitDatabase_name(self, ctx:sqlParser.Database_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#schema_name.
    def enterSchema_name(self, ctx:sqlParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#schema_name.
    def exitSchema_name(self, ctx:sqlParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#table_function_name.
    def enterTable_function_name(self, ctx:sqlParser.Table_function_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#table_function_name.
    def exitTable_function_name(self, ctx:sqlParser.Table_function_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#table_name.
    def enterTable_name(self, ctx:sqlParser.Table_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#table_name.
    def exitTable_name(self, ctx:sqlParser.Table_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#column_name.
    def enterColumn_name(self, ctx:sqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#column_name.
    def exitColumn_name(self, ctx:sqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#collation_name.
    def enterCollation_name(self, ctx:sqlParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#collation_name.
    def exitCollation_name(self, ctx:sqlParser.Collation_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#index_name.
    def enterIndex_name(self, ctx:sqlParser.Index_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#index_name.
    def exitIndex_name(self, ctx:sqlParser.Index_nameContext):
        pass


    # Enter a parse tree produced by sqlParser#table_alias.
    def enterTable_alias(self, ctx:sqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by sqlParser#table_alias.
    def exitTable_alias(self, ctx:sqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by sqlParser#any_name.
    def enterAny_name(self, ctx:sqlParser.Any_nameContext):
        pass

    # Exit a parse tree produced by sqlParser#any_name.
    def exitAny_name(self, ctx:sqlParser.Any_nameContext):
        pass



del sqlParser