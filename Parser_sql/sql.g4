// grammar
grammar sql;

//full query
root
 : ( queries+=query_statements_list )* EOF
 ;

//combination of different queries
query_statements_list
 : ';'* query_statements+=statement_node ( ';'+ query_statements+=statement_node )* ';'*
 ;

//names of statements
statement_node
 :  /*compound_select_stmt     #compound_statement
    | factored_select_stmt  #factored_select_statement
    | simple_select_stmt    #simple_select_statement
    | select_stmt           #select_statement*/
     vacuum_stmt           #vacuum_statement
    | create_index_stmt     #create_index_statement
    | create_table_stmt     #create_table_statement
    | reindex_stmt          #reindex_statement
    | update_stmt           #update_statement
    | update_stmt_limited   #update_statement
    | insert_stmt           #insert_statement
    | simp_select_stmt      #simp_select_statement
    | drop_index_stmt       #drop_index_statement
    | drop_table_stmt       #drop_table_statement
    | delete_stmt           #delete_statement
    | delete_stmt_limited   #delete_statement_limited
  ;


//change index statement
reindex_stmt
 : K_REINDEX ( collation_name
             | ( database_name '.' )? ( table_name | index_name )
             )?
 ;

//creation of index statement
create_index_stmt
 : K_CREATE K_UNIQUE? K_INDEX ( K_IF K_NOT K_EXISTS )?
   ( database_name '.' )? index_name K_ON table_name '(' indexed_column ( ',' indexed_column )* ')'
   ( K_WHERE expr )?
 ;

//creation of table statement
create_table_stmt
 : K_CREATE ( K_TEMP | K_TEMPORARY )? K_TABLE ( K_IF K_NOT K_EXISTS )?
   ( database_name '.' )? table_name
   ( '(' columns+=column_def ( ',' columns+=column_def )*? ( ',' constraints+=table_constraint )* ')' ( K_WITHOUT IDENTIFIER )?
   | K_AS select_stmt
   )
 ;

simp_select_stmt
: K_SELECT ( K_DISTINCT | K_ALL )? columns+=result_column_1 ( ',' columns+=result_column_1 )*
( K_FROM table_name )?
( K_FROM ( tables+=table_or_subquery ( ',' tables+=table_or_subquery )* | join=join_clause ) )?
( K_WHERE where = expr1 )?
;

result_column_1
: '*'
| expr
;

some_operator
: ASSIGN
|LT
|LT_EQ
|GT
|GT_EQ
|NOT_EQ1
;

expr1
: literal_value
| BIND_PARAMETER
| ( ( database_name '.' )? table_name '.' )? column_name
| some_operator expr1
| expr1 some_operator expr1
;

//collumn of constratints
column_constraint
 : ( K_CONSTRAINT name )?
   ( K_PRIMARY K_KEY ( K_ASC | K_DESC )? conflict_clause K_AUTOINCREMENT?
   | K_NOT? K_NULL conflict_clause
   | K_UNIQUE conflict_clause
   | K_CHECK '(' expr ')'
   | K_DEFAULT (signed_number | literal_value | '(' expr ')')
   | K_COLLATE collation_name
   | foreign_key_clause
   )
 ;

//foreign key clause
foreign_key_clause
 : K_REFERENCES foreign_table ( '(' column_name ( ',' column_name )* ')' )?
   ( ( K_ON ( K_DELETE | K_UPDATE ) ( K_SET K_NULL
                                    | K_SET K_DEFAULT
                                    | K_CASCADE
                                    | K_RESTRICT
                                    | K_NO K_ACTION )
     | K_MATCH name
     )
   )*
   ( K_NOT? K_DEFERRABLE ( K_INITIALLY K_DEFERRED | K_INITIALLY K_IMMEDIATE )? )?
 ;

//table with constraints
table_constraint
 : ( K_CONSTRAINT name )?
   ( ( K_PRIMARY K_KEY | K_UNIQUE ) '(' indexed_column ( ',' indexed_column )* ')' conflict_clause
   | K_CHECK '(' expr ')'
   | K_FOREIGN K_KEY '(' column_name ( ',' column_name )* ')' foreign_key_clause
   )
 ;


column_def
 : column_name type_name? column_constraint*
 ;


//name of type (+/-)
type_name
 : name+? ( '(' signed_number ')'
         | '(' signed_number ',' signed_number ')' )?
 ;

//indexed(ordered) column
indexed_column
 : column_name ( K_COLLATE collation_name )? ( K_ASC | K_DESC )?
 ;

//multiple select statement-two or more simple selects
compound_select_stmt
 : with_clause?
   select_core ( ( K_UNION K_ALL? | K_INTERSECT | K_EXCEPT ) select_core )+
   ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
   ( K_LIMIT expr ( ( K_OFFSET | ',' ) expr )? )?
 ;

//select statement with smaller chunks
factored_select_stmt
 : with_clause?
   select_parts+=select_core ( operators+=compound_operator select_parts+=select_core )*
   ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
   ( K_LIMIT expr ( ( K_OFFSET | ',' ) expr )? )?
 ;

//common select statement;
// includes FROM, WHERE, GROUP BY, HAVING AND DISTINCT clauses
simple_select_stmt
 : with_clause?
   select_core ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
   ( K_LIMIT expr ( ( K_OFFSET | ',' ) expr )? )?
 ;


//select statement
//wider interpretation of select statement
select_stmt
 : with_clause?
   select_or_values ( compound_operator select_or_values )*
   ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
   ( K_LIMIT expr ( ( K_OFFSET | ',' ) expr )? )?
 ;

//select query or select subquery
select_or_values
 : K_SELECT ( K_DISTINCT | K_ALL )? result_column ( ',' result_column )*
   ( K_FROM ( table_or_subquery ( ',' table_or_subquery )* | join_clause ) )?
   ( K_WHERE expr )?
   ( K_GROUP K_BY expr ( ',' expr )* ( K_HAVING expr )? )?
 | K_VALUES '(' expr ( ',' expr )* ')' ( ',' '(' expr ( ',' expr )* ')' )*
 ;

vacuum_stmt
 : K_VACUUM
 ;


//update table statement
update_stmt //
 : with_clause? K_UPDATE ( K_OR K_ROLLBACK
                         | K_OR K_ABORT
                         | K_OR K_REPLACE
                         | K_OR K_FAIL
                         | K_OR K_IGNORE )? qualified_table_name
   K_SET column_name '=' values+=expr1 ( ',' column_name '=' values+=expr1 )* ( K_WHERE where = expr1 )?
 ;

//update table statement with limit clause
update_stmt_limited
 : with_clause? K_UPDATE ( K_OR K_ROLLBACK
                         | K_OR K_ABORT
                         | K_OR K_REPLACE
                         | K_OR K_FAIL
                         | K_OR K_IGNORE )? qualified_table_name
   K_SET column_name '=' expr ( ',' column_name '=' expr )* ( K_WHERE expr )?
   ( ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
     K_LIMIT expr ( ( K_OFFSET | ',' ) expr )?
   )?
 ;

//insert table statement
insert_stmt
 : with_clause? ( K_INSERT
                | K_REPLACE
                | K_INSERT K_OR K_REPLACE
                | K_INSERT K_OR K_ROLLBACK
                | K_INSERT K_OR K_ABORT
                | K_INSERT K_OR K_FAIL
                | K_INSERT K_OR K_IGNORE ) K_INTO
   ( database_name '.' )? table_name ( '(' column_name ( ',' column_name )* ')' )?
   ( K_VALUES '(' expr1 ( ',' expr1 )* ')' ( ',' '(' expr1 ( ',' expr1 )* ')' )*
   | select_stmt
   | K_DEFAULT K_VALUES
   )
 ;

// drops an existing index from the database system
drop_index_stmt
 : K_DROP K_INDEX ( K_IF K_EXISTS )? ( database_name '.' )? index_name
 ;

// drop an existing table in a database
drop_table_stmt
 : K_DROP K_TABLE ( K_IF K_EXISTS )? ( database_name '.' )? table_name
 ;

// delete existing records in a table
delete_stmt
 : with_clause? K_DELETE K_FROM qualified_table_name
   ( K_WHERE where = expr1 )?
 ;

// delete existing records in a table with limit clause
delete_stmt_limited
 : with_clause? K_DELETE K_FROM qualified_table_name
   ( K_WHERE expr )?
   ( ( K_ORDER K_BY ordering_term ( ',' ordering_term )* )?
     K_LIMIT expr ( ( K_OFFSET | ',' ) expr )?
   )?
 ;

//indexed table
qualified_table_name //
 : ( database_name '.' )? table_name ( K_INDEXED K_BY index_name
                                     | K_NOT K_INDEXED )?
 ;

//expression - combinations of one or more values, operators and SQl functions, evaluated to a value
expr
 : literal_value
 | BIND_PARAMETER
 | ( ( database_name '.' )? table_name '.' )? column_name
 | unary_operator expr
 | expr '||' expr
 | expr ( '*' | '/' | '%' ) expr
 | expr ( '+' | '-' ) expr
 | expr ( '<<' | '>>' | '&' | '|' ) expr
 | expr ( '<' | '<=' | '>' | '>=' ) expr
 | expr ( '=' | '==' | '!=' | '<>' ) expr
 | expr K_NOT? K_IN ( '(' ( select_stmt
                          | expr ( ',' expr )*
                          )?
                      ')'
                    | ( database_name '.' )? table_name )
 | expr K_AND expr
 | expr K_OR expr
 | '(' expr ')'
 | expr K_COLLATE collation_name
 | expr K_NOT? ( K_LIKE | K_GLOB | K_REGEXP | K_MATCH ) expr ( K_ESCAPE expr )?
 | expr ( K_ISNULL | K_NOTNULL | K_NOT K_NULL )
 | expr K_IS K_NOT? expr
 | expr K_NOT? K_BETWEEN expr K_AND expr
 | ( ( K_NOT )? K_EXISTS )? '(' select_stmt ')'
 | K_CASE expr? ( K_WHEN expr K_THEN expr )+ ( K_ELSE expr )? K_END
 ;

//optional prefix for select
with_clause
 : K_WITH K_RECURSIVE? common_table_expression ( ',' common_table_expression )*
 ;

//common table expression
  common_table_expression
 : table_name ( '(' column_name ( ',' column_name )* ')' )? K_AS '(' select_stmt ')'
 ;

//presents order by clause
ordering_term
 : expr ( K_COLLATE collation_name )? ( K_ASC | K_DESC )?
 ;


result_column
 : '*'
 | table_name '.' '*'
 | expr ( K_AS? column_alias )?
 ;

//table or subquery
table_or_subquery
 : ( schema_name '.' )? table_name ( K_AS? table_alias )?
   ( K_INDEXED K_BY index_name
   | K_NOT K_INDEXED )?
 | ( schema_name '.' )? table_function_name '(' ( expr ( ',' expr )* )? ')' ( K_AS? table_alias )?
 | '(' ( table_or_subquery ( ',' table_or_subquery )*
       | join_clause )
   ')'
 | '(' select_stmt ')' ( K_AS? table_alias )?
 ;

//join clause
//combines rows from two or more tables
join_clause
 : table_or_subquery ( join_operator table_or_subquery join_constraint )*
 ;

//type of join clause
join_operator
 : ','
 | K_NATURAL? ( K_LEFT K_OUTER? | K_INNER | K_CROSS )? K_JOIN
 ;

//specificstion of rules for data in a table
join_constraint
 : ( K_ON expr
   | K_USING '(' column_name ( ',' column_name )* ')' )?
 ;

//select core
//used by compound select statement, factored select statement, simple select
select_core
 : K_SELECT ( K_DISTINCT | K_ALL )? columns+=result_column ( ',' columns+=result_column )*
   ( K_FROM ( tables+=table_or_subquery ( ',' tables+=table_or_subquery )* | join=join_clause ) )?
   ( K_WHERE where=expr )?
   ( K_GROUP K_BY group_by+=expr ( ',' group_by+=expr )* ( K_HAVING having=expr )? )?
// | K_VALUES '(' values+=expr ( ',' expr )* ')' ( ',' '(' expr ( ',' expr )* ')' )*
 ;

//non-standart clause
//specifies an algorythm used to resolve constraint conflicts
conflict_clause
 : ( K_ON K_CONFLICT ( K_ROLLBACK
                     | K_ABORT
                     | K_FAIL
                     | K_IGNORE
                     | K_REPLACE
                     )
   )?
 ;

//compound operators
compound_operator
 : K_UNION
 | K_UNION K_ALL
 | K_INTERSECT
 | K_EXCEPT
 ;

//foreign table
foreign_table
 : any_name
 ;

// + or -
signed_number
 : ( '+' | '-' )? NUMERIC_LITERAL
 ;

//literal values
literal_value
 : NUMERIC_LITERAL
 | STRING_LITERAL
 | BLOB_LITERAL
 | K_NULL
 | K_CURRENT_TIME
 | K_CURRENT_DATE
 | K_CURRENT_TIMESTAMP
 ;

//unary operator
unary_operator
 : '-'
 | '+'
 | '~'
 | K_NOT
 ;

//column alias
column_alias
 : IDENTIFIER
 | STRING_LITERAL
 ;
//keywords
//represent main keywords from sql-language
keyword
 : K_ABORT
 | K_ACTION
 | K_ADD
 | K_AFTER
 | K_ALL
 | K_ALTER
 | K_ANALYZE
 | K_AND
 | K_AS
 | K_ASC
 | K_ATTACH
 | K_AUTOINCREMENT
 | K_BEFORE
 | K_BEGIN
 | K_BETWEEN
 | K_BY
 | K_CASCADE
 | K_CASE
 | K_CAST
 | K_CHECK
 | K_COLLATE
 | K_COLUMN
 | K_COMMIT
 | K_CONFLICT
 | K_CONSTRAINT
 | K_CREATE
 | K_CROSS
 | K_CURRENT_DATE
 | K_CURRENT_TIME
 | K_CURRENT_TIMESTAMP
 | K_DATABASE
 | K_DEFAULT
 | K_DEFERRABLE
 | K_DEFERRED
 | K_DELETE
 | K_DESC
 | K_DETACH
 | K_DISTINCT
 | K_DROP
 | K_EACH
 | K_ELSE
 | K_END
 | K_ESCAPE
 | K_EXCEPT
 | K_EXCLUSIVE
 | K_EXISTS
 | K_EXPLAIN
 | K_FAIL
 | K_FOR
 | K_FOREIGN
 | K_FROM
 | K_FULL
 | K_GLOB
 | K_GROUP
 | K_HAVING
 | K_IF
 | K_IGNORE
 | K_IMMEDIATE
 | K_IN
 | K_INDEX
 | K_INDEXED
 | K_INITIALLY
 | K_INNER
 | K_INSERT
 | K_INSTEAD
 | K_INTERSECT
 | K_INTO
 | K_IS
 | K_ISNULL
 | K_JOIN
 | K_KEY
 | K_LEFT
 | K_LIKE
 | K_LIMIT
 | K_MATCH
 | K_NATURAL
 | K_NO
 | K_NOT
 | K_NOTNULL
 | K_NULL
 | K_OF
 | K_OFFSET
 | K_ON
 | K_OR
 | K_ORDER
 | K_OUTER
 | K_PLAN
 | K_PRAGMA
 | K_PRIMARY
 | K_QUERY
 | K_RAISE
 | K_RECURSIVE
 | K_REFERENCES
 | K_REGEXP
 | K_REINDEX
 | K_RELEASE
 | K_RENAME
 | K_REPLACE
 | K_RESTRICT
 | K_RIGHT
 | K_ROLLBACK
 | K_ROW
 | K_SAVEPOINT
 | K_SELECT
 | K_SET
 | K_TABLE
 | K_TEMP
 | K_TEMPORARY
 | K_THEN
 | K_TO
 | K_TRANSACTION
 | K_TRIGGER
 | K_UNION
 | K_UNIQUE
 | K_UPDATE
 | K_USING
 | K_VACUUM
 | K_VALUES
 | K_VIEW
 | K_VIRTUAL
 | K_WHEN
 | K_WHERE
 | K_WITH
 | K_WITHOUT
 ;

// TODO check all names below

name
 : any_name
 ;

database_name
 : any_name
 ;

schema_name
 : any_name
 ;

table_function_name
 : any_name
 ;

table_name
 : any_name
 ;


column_name
 : any_name
 ;

 collation_name
 : any_name
 ;


index_name
 : any_name
 ;


table_alias
 : IDENTIFIER
 | STRING_LITERAL
 | '(' table_alias ')'
 ;


any_name
 : IDENTIFIER
 | keyword
 | STRING_LITERAL
 | '(' any_name ')'
 ;


SCOL : ';';
DOT : '.';
OPEN_PAR : '(';
CLOSE_PAR : ')';
COMMA : ',';
ASSIGN : '=';
STAR : '*';
PLUS : '+';
MINUS : '-';
TILDE : '~';
PIPE2 : '||';
DIV : '/';
MOD : '%';
LT2 : '<<';
GT2 : '>>';
AMP : '&';
PIPE : '|';
LT : '<';
LT_EQ : '<=';
GT : '>';
GT_EQ : '>=';
EQ : '==';
NOT_EQ1 : '!=';
NOT_EQ2 : '<>';

// http://www.sqlite.org/lang_keywords.html
K_ABORT : A B O R T;
K_ACTION : A C T I O N;
K_ADD : A D D;
K_AFTER : A F T E R;
K_ALL : A L L;
K_ALTER : A L T E R;
K_ANALYZE : A N A L Y Z E;
K_AND : A N D;
K_AS : A S;
K_ASC : A S C;
K_ATTACH : A T T A C H;
K_AUTOINCREMENT : A U T O I N C R E M E N T;
K_BEFORE : B E F O R E;
K_BEGIN : B E G I N;
K_BETWEEN : B E T W E E N;
K_BY : B Y;
K_CASCADE : C A S C A D E;
K_CASE : C A S E;
K_CAST : C A S T;
K_CHECK : C H E C K;
K_COLLATE : C O L L A T E;
K_COLUMN : C O L U M N;
K_COMMIT : C O M M I T;
K_CONFLICT : C O N F L I C T;
K_CONSTRAINT : C O N S T R A I N T;
K_CREATE : C R E A T E;
K_CROSS : C R O S S;
K_CURRENT_DATE : C U R R E N T '_' D A T E;
K_CURRENT_TIME : C U R R E N T '_' T I M E;
K_CURRENT_TIMESTAMP : C U R R E N T '_' T I M E S T A M P;
K_DATABASE : D A T A B A S E;
K_DEFAULT : D E F A U L T;
K_DEFERRABLE : D E F E R R A B L E;
K_DEFERRED : D E F E R R E D;
K_DELETE : D E L E T E;
K_DESC : D E S C;
K_DETACH : D E T A C H;
K_DISTINCT : D I S T I N C T;
K_DROP : D R O P;
K_EACH : E A C H;
K_ELSE : E L S E;
K_END : E N D;
K_ESCAPE : E S C A P E;
K_EXCEPT : E X C E P T;
K_EXCLUSIVE : E X C L U S I V E;
K_EXISTS : E X I S T S;
K_EXPLAIN : E X P L A I N;
K_FAIL : F A I L;
K_FOR : F O R;
K_FOREIGN : F O R E I G N;
K_FROM : F R O M;
K_FULL : F U L L;
K_GLOB : G L O B;
K_GROUP : G R O U P;
K_HAVING : H A V I N G;
K_IF : I F;
K_IGNORE : I G N O R E;
K_IMMEDIATE : I M M E D I A T E;
K_IN : I N;
K_INDEX : I N D E X;
K_INDEXED : I N D E X E D;
K_INITIALLY : I N I T I A L L Y;
K_INNER : I N N E R;
K_INSERT : I N S E R T;
K_INSTEAD : I N S T E A D;
K_INTERSECT : I N T E R S E C T;
K_INTO : I N T O;
K_IS : I S;
K_ISNULL : I S N U L L;
K_JOIN : J O I N;
K_KEY : K E Y;
K_LEFT : L E F T;
K_LIKE : L I K E;
K_LIMIT : L I M I T;
K_MATCH : M A T C H;
K_NATURAL : N A T U R A L;
K_NO : N O;
K_NOT : N O T;
K_NOTNULL : N O T N U L L;
K_NULL : N U L L;
K_OF : O F;
K_OFFSET : O F F S E T;
K_ON : O N;
K_OR : O R;
K_ORDER : O R D E R;
K_OUTER : O U T E R;
K_PLAN : P L A N;
K_PRAGMA : P R A G M A;
K_PRIMARY : P R I M A R Y;
K_QUERY : Q U E R Y;
K_RAISE : R A I S E;
K_RECURSIVE : R E C U R S I V E;
K_REFERENCES : R E F E R E N C E S;
K_REGEXP : R E G E X P;
K_REINDEX : R E I N D E X;
K_RELEASE : R E L E A S E;
K_RENAME : R E N A M E;
K_REPLACE : R E P L A C E;
K_RESTRICT : R E S T R I C T;
K_RIGHT : R I G H T;
K_ROLLBACK : R O L L B A C K;
K_ROW : R O W;
K_SAVEPOINT : S A V E P O I N T;
K_SELECT : S E L E C T;
K_SET : S E T;
K_TABLE : T A B L E;
K_TEMP : T E M P;
K_TEMPORARY : T E M P O R A R Y;
K_THEN : T H E N;
K_TO : T O;
K_TRANSACTION : T R A N S A C T I O N;
K_TRIGGER : T R I G G E R;
K_UNION : U N I O N;
K_UNIQUE : U N I Q U E;
K_UPDATE : U P D A T E;
K_USING : U S I N G;
K_VACUUM : V A C U U M;
K_VALUES : V A L U E S;
K_VIEW : V I E W;
K_VIRTUAL : V I R T U A L;
K_WHEN : W H E N;
K_WHERE : W H E R E;
K_WITH : W I T H;
K_WITHOUT : W I T H O U T;

IDENTIFIER
 : '"' (~'"' | '""')* '"'
 | '`' (~'`' | '``')* '`'
 | '[' ~']'* ']'
 | [a-zA-Z_] [a-zA-Z_0-9]* // TODO check: needs more chars in set
 ;

NUMERIC_LITERAL
 : DIGIT+ ( '.' DIGIT* )? ( E [-+]? DIGIT+ )?
 | '.' DIGIT+ ( E [-+]? DIGIT+ )?
 ;

BIND_PARAMETER
 : '?' DIGIT*
 | [:@$] IDENTIFIER
 ;

STRING_LITERAL
 : '\'' ( ~'\'' | '\'\'' )* '\''
 ;

BLOB_LITERAL
 : X STRING_LITERAL
 ;

SINGLE_LINE_COMMENT
 : '--' ~[\r\n]* -> channel(HIDDEN)
 ;

MULTILINE_COMMENT
 : '/*' .*? ( '*/' | EOF ) -> channel(HIDDEN)
 ;

SPACES
 : [ \u000B\t\r\n] -> channel(HIDDEN)
 ;

UNEXPECTED_CHAR
 : .
 ;

fragment DIGIT : [0-9];

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
