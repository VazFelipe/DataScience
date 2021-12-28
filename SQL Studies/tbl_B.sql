--DROP TABLE tbl_B;
--DROP SEQUENCE sequence_tbl_B;
--Does not work, I do not know how to delete from a table using where clause
--DELETE from tbl_B
--where (department_key = 2706503459);
--Does not work, I do not know how to delete from a table
--DELETE from tbl_B;
--TRUNCATE table tbl_B;

CREATE sequence sequence_tbl_B
    START with 1
    INCREMENT by 1
    CACHE 1000;

CREATE table tbl_B
(
     id                      INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) NOT NULL
    ,department_key          NUMBER NOT NULL
    ,department              VARCHAR2(32) NOT NULL
    ,department_description  VARCHAR2(64) NOT NULL
    ,insert_time             TIMESTAMP(6)
);

INSERT INTO tbl_B(department_key, department, department_description, insert_time)
values(2706503459, 'Old_But_Gold_99999', 'People that make things happen_99999_manual', CAST(TO_CHAR(SYSTIMESTAMP - INTERVAL '3' HOUR, 'DD/MM/YYYY HH24:MI:SS,FF6') AS TIMESTAMP));

BEGIN
FOR loop_counter IN 1..10 LOOP
INSERT INTO tbl_B (department_key, department, department_description, insert_time)
values ( 
          ORA_HASH(TRUNC(DBMS_RANDOM.VALUE(1,25)))
         ,'Old_But_Gold_'||TRUNC(DBMS_RANDOM.VALUE(1,1000))
         ,'People that make things happen_'||TRUNC(DBMS_RANDOM.VALUE(1,1000))||'_'||DBMS_RANDOM.STRING('X', 10)
         ,CAST(TO_CHAR(SYSTIMESTAMP - INTERVAL '3' HOUR, 'DD/MM/YYYY HH24:MI:SS,FF6') AS TIMESTAMP)
       );
END LOOP;
COMMIT;
END;
/

SELECT
    *
FROM
    tbl_B;