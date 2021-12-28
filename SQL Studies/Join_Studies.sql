-- Before executing this queries, please run the PL/SQL procedures 'tbl_A.sql' and 'tbl_B.sql' in the folder.

WITH
tblA
AS
(
    SELECT
        *
    FROM
        tbl_A
),
tblB
AS
(
    SELECT
        *
    FROM
        tbl_B
),
tblA_left_join_tblB
AS
(
    SELECT
         a.*
        ,b.department
        ,b.department_description
    FROM
            tblA a
    LEFT JOIN
            tblB b
         ON a.department_key = b.department_key
    ORDER BY
        a.id
),
tblA_right_join_tblB
AS
(
    SELECT
         a.*
        ,b.department
        ,b.department_description
    FROM
            tblA a
    RIGHT JOIN
            tblB b
         ON a.department_key = b.department_key
    ORDER BY
        a.id
),
tblB_left_join_tblA
AS
(
    SELECT
         b.*
        ,a.transaction_key
        ,a.transaction_date
        ,a.transaction_description
    FROM
            tblB b
    LEFT JOIN
            tblA a
         ON b.department_key = a.department_key
    ORDER BY
        b.id
),
tblB_right_join_tblA
AS
(
    SELECT
         b.*
        ,a.transaction_key
        ,a.transaction_date
        ,a.transaction_description
    FROM
            tblB b
    RIGHT JOIN
            tblA a
         ON b.department_key = a.department_key
    ORDER BY
        b.id
),
tblA_left_outer_join_tblB
AS
(
    SELECT
         a.*
        ,b.department
        ,b.department_description
    FROM
            tblA a
    LEFT OUTER JOIN
            tblB b
         ON a.department_key = b.department_key
    ORDER BY
        a.id
),
tblA_right_outer_join_tblB
AS
(
    SELECT
         a.*
        ,b.department
        ,b.department_description
    FROM
            tblA a
    RIGHT OUTER JOIN
            tblB b
         ON a.department_key = b.department_key
    ORDER BY
        a.id
),
tblA_full_outer_join_tblB
AS
(
    SELECT
         a.*
        ,b.department
        ,b.department_description
    FROM
            tblA a
    FULL OUTER JOIN
            tblB b
         ON a.department_key = b.department_key
    ORDER BY
        a.id
),
tblB_left_outer_join_tblA
AS
(
    SELECT
         b.*
        ,a.transaction_key
        ,a.transaction_date
        ,a.transaction_description
    FROM
            tblB b
    LEFT OUTER JOIN
            tblA a
         ON b.department_key = a.department_key
    ORDER BY
        b.id
),
tblB_right_outer_join_tblA
AS
(
    SELECT
         b.*
        ,a.transaction_key
        ,a.transaction_date
        ,a.transaction_description
    FROM
            tblB b
    RIGHT OUTER JOIN
            tblA a
         ON b.department_key = a.department_key
    ORDER BY
        b.id
),
tblB_full_outer_join_tblA
AS
(
    SELECT
         b.*
        ,a.transaction_key
        ,a.transaction_date
        ,a.transaction_description
    FROM
            tblB b
    FULL OUTER JOIN
            tblA a
         ON b.department_key = a.department_key
    ORDER BY
        b.id
),
tblA_all
AS
(
    SELECT
        'LEFT JOIN' AS JOINTYPE
        ,'TBLA_LEFT_JOIN_TBLB' AS FROM_ENTITY
        ,al.*
    FROM
        tblA_left_join_tblB al
    UNION ALL
    SELECT
        'RIGHT JOIN' AS JOINTYPE
        ,'TBLA_RIGHT_JOIN_TBLB' AS FROM_ENTITY
        ,ar.*
    FROM
        tblA_right_join_tblB ar
    UNION ALL
    SELECT
        'LEFT OUTER JOIN' AS JOINTYPE
        ,'TBLA_LEFT_OUTER_JOIN_TBLB' AS FROM_ENTITY
        ,alo.*
    FROM
        tblA_left_outer_join_tblB alo
    UNION ALL
    SELECT
        'RIGHT OUTER JOIN' AS JOINTYPE
        ,'TBLA_RIGHT_OUTER_JOIN_TBLB' AS FROM_ENTITY
        ,aro.*
    FROM
        tblA_right_outer_join_tblB aro
    UNION ALL
    SELECT
        'FULL OUTER JOIN' AS JOINTYPE
        ,'TBLA_FULL_OUTER_JOIN_TBLB' AS FROM_ENTITY
        ,afo.*
    FROM
        tblA_full_outer_join_tblB afo
),
tblB_all
AS
(
    SELECT
        'LEFT JOIN' AS JOINTYPE
        ,'TBLB_LEFT_JOIN_TBLA' AS FROM_ENTITY
        ,bl.*
    FROM
        tblB_left_join_tblA bl
    UNION ALL
    SELECT
        'RIGHT JOIN' AS JOINTYPE
        ,'TBLB_RIGHT_JOIN_TBLA' AS FROM_ENTITY
        ,br.*
    FROM
        tblB_right_join_tblA br
    UNION ALL
    SELECT
        'LEFT OUTER JOIN' AS JOINTYPE
        ,'TBLB_LEFT_OUTER_JOIN_TBLA' AS FROM_ENTITY
        ,blo.*
    FROM
        tblB_left_outer_join_tblA blo
    UNION ALL
    SELECT
        'RIGHT OUTER JOIN' AS JOINTYPE
        ,'TBLB_RIGHT_OUTER_JOIN_TBLA' AS FROM_ENTITY
        ,bro.*
    FROM
        tblB_right_outer_join_tblA bro
    UNION ALL
    SELECT
        'FULL OUTER JOIN' AS JOINTYPE
        ,'TBLB_FULL_OUTER_JOIN_TBLA' AS FROM_ENTITY
        ,bfo.*
    FROM
        tblB_full_outer_join_tblA bfo
)
 
-- Run one line at a time
 
SELECT * FROM tblA_all;
--SELECT * FROM tblB_all;