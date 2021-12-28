DESC emp_b;

WITH
tbl_emp_b
AS
(
    SELECT
         empno
        ,ename
        ,job
        ,mgr
        ,hiredate
        ,sal
        ,comm
        ,deptno 
    FROM
        emp_b
),
tbl_sort
AS
(
    SELECT
          empno
         ,dense_rank
         ,row_num
    FROM
        (
        SELECT
             job
            ,empno
            ,sal
            ,deptno
            ,ROW_NUMBER() OVER(PARTITION BY deptno ORDER BY sal) AS row_num
            ,RANK() OVER(PARTITION BY deptno ORDER BY sal) AS rank
            ,DENSE_RANK() OVER(PARTITION BY deptno ORDER BY sal) AS dense_rank
            ,ROUND(SUM(sal) OVER(PARTITION BY deptno ORDER BY sal), 2) AS cume_sum
            ,ROUND(CUME_DIST() OVER(PARTITION BY deptno ORDER BY sal), 2) AS cume_dist
            ,PERCENT_RANK() OVER(PARTITION BY deptno ORDER BY sal) AS perc_rank
            ,NTILE(10) OVER (ORDER BY sal) AS quartile
            ,SUM(sal) OVER(PARTITION BY deptno ORDER BY sal ROWS UNBOUNDED PRECEDING) AS cume_sum_2
        FROM
            tbl_emp_b
        ORDER BY
            deptno) tbl_a
    WHERE
        row_num <= 2
)
SELECT * FROM tbl_sort;
tbl_metrics_2
AS
(
    SELECT
--         job
--         sal
--         deptno
--        ,hiredate
--        ,ROUND(AVG(sal) OVER(PARTITION BY deptno ORDER BY job ROWS 2 PRECEDING), 2) AS mov_sal
--        ,ROUND(AVG(sal) OVER(PARTITION BY deptno ORDER BY hiredate RANGE BETWEEN INTERVAL '1' YEAR PRECEDING AND INTERVAL '6' MONTH FOLLOWING), 2) AS mov_sal_hire
        MAX(empno) KEEP(DENSE_RANK FIRST ORDER BY hiredate)
--        OVER(PARTITION BY deptno)
    FROM
        emp_B
--    GROUP BY
--         deptno
--        ,hiredate
)
SELECT * FROM tbl_metrics_2;


SELECT * FROM emp;



SELECT 
     job
    ,deptno
    ,SUM(sal) OVER(PARTITION BY deptno ORDER BY sal RANGE BETWEEN 2 PRECEDING AND 1 FOLLOWING) as moving_sum
    ,SUM(sal) OVER(PARTITION BY deptno ORDER BY sal RANGE UNBOUNDED PRECEDING) as moving_sum
FROM emp;

