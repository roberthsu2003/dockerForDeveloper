USE mysql_db;
CREATE TABLE test_table(
	somevalue varchar(50)
);

INSERT INTO test_table(somevalue) VALUES('Test insert');
COMMIT;

SELECT somevalue FROM test_table;
