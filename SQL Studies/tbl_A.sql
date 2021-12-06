--DROP TABLE tbl_A;
--DROP SEQUENCE sequence_tbl_A;
--Does not work, I do not know how to delete from a table using where clause
--DELETE from tbl_A
--where (transaction_key = 612889299);
--Does not work, I do not know how to delete from a table
--DELETE from tbl_A;
--TRUNCATE table tbl_A;

CREATE sequence sequence_tbl_A
    START with 1
    INCREMENT by 1
    CACHE 1000;

CREATE table tbl_A
(
     id                      INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL
    ,transaction_key         NUMBER NOT NULL
    ,transaction_date        DATE   NOT NULL
    ,transaction_description VARCHAR2(32) NOT NULL
    ,department_key          NUMBER NOT NULL
    ,insert_time             TIMESTAMP(6)
);

INSERT INTO tbl_A(transaction_key, transaction_date, transaction_description, department_key, insert_time)
values(612889299, '10/12/1982', 'Teste_aleatorio_manual', 2706503459, CAST(TO_CHAR(SYSTIMESTAMP - INTERVAL '3' HOUR, 'DD/MM/YYYY HH24:MI:SS,FF6') AS TIMESTAMP));

BEGIN
FOR loop_counter IN 1..10 LOOP
INSERT INTO tbl_A (transaction_key, transaction_date, transaction_description, department_key, insert_time)
VALUES ( 
          ORA_HASH(loop_counter+TRUNC(DBMS_RANDOM.VALUE(1,1000000)))
         ,TO_DATE('01/01/2021', 'dd/mm/yyyy')+ TRUNC(DBMS_RANDOM.VALUE(1,1000))
         ,'Teste_aleatorio_'||TRUNC(DBMS_RANDOM.VALUE(1,1000))||'_'||DBMS_RANDOM.STRING('X', 10)
         ,ORA_HASH(TRUNC(DBMS_RANDOM.VALUE(1,50)))
         ,CAST(TO_CHAR(SYSTIMESTAMP - INTERVAL '3' HOUR, 'DD/MM/YYYY HH24:MI:SS,FF6') AS TIMESTAMP)
       );
END LOOP;
COMMIT;
END;
/

SELECT
    *
FROM
    tbl_A;