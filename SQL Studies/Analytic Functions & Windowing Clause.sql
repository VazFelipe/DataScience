-- Using analytics functions in Oracle SQL
-- Credits: https://www.oracleplsqltr.com/2020/05/09/analytic-functions-windowing-clause/

-- Using AVG()
SELECT
     deptno
    ,AVG(sal)
FROM
    emp_B
GROUP BY
    deptno;
    
-- If sal, other dimensions and AVG() gets in, the average cannot be seen
SELECT
     deptno
    ,empno
    ,ename
    ,job
    ,sal
    ,AVG(sal)
FROM
    emp_B
GROUP BY
     deptno
    ,empno
    ,ename
    ,job
    ,sal;

-- That is the purpose of analytics function
-- Analytic functions are similar to aggregate functions. 
-- However, the output of the query does not reduce the rows.
-- In other words, unlike aggregate functions you can see the
-- whole result set when using the analytic functions.

-- Now, using AVG() and SUM() OVER(PARTITION BY)
SELECT
     empno
    ,ename
    ,job
    ,sal
    ,ROUND(AVG(sal) OVER(PARTITION BY deptno), 2) AS avg_dept_sal
    ,ROUND(SUM(sal) OVER(PARTITION BY deptno), 2) AS sum_dept_sal
FROM
    emp_B;
    
-- The most used sort functions are the followings. 
-- So, you can look at the result set below to see the difference between each other.
-- ROW_NUMBER function is the conventional way to sort the data. 
-- RANK function is like much more gradation and as the name suggests, 
-- DENSE_RANK sorts the data without leave a blank.

SELECT
     empno
    ,ename
    ,job
    ,deptno
    ,sal
    ,ROW_NUMBER() OVER (PARTITION BY deptno ORDER BY sal) AS ROW_NUM
    ,RANK() OVER (PARTITION BY deptno ORDER BY sal) AS RANK_NUM
    ,DENSE_RANK() OVER (PARTITION BY deptno ORDER BY sal)DENSE_RANK_NUM
FROM
    emp_B
ORDER BY
    deptno;
    
    
-- Which function would you use if you want to get the EMPNO
-- of the person with the highest salary? Actually, 
-- there are several ways to get this data. 
-- Assuming that only one person gets the highest salary, 
-- the following queries get the same result. However, 
-- I would prefer to use the KEEP one.

-- My first thought was using ROW_NUM() and ORDER BY SAL DESC and after that choose the RN = 1, but...

SELECT
      MAX(empno) KEEP(DENSE_RANK FIRST ORDER BY SAL DESC) AS empno_max_salary
     ,MAX(ename) KEEP(DENSE_RANK FIRST ORDER BY SAL DESC) AS empno_max_salary
--    ,AVG(EMPNO) KEEP(DENSE_RANK FIRST ORDER BY SAL DESC) AS empno_avg_salary
--    ,MIN(EMPNO) KEEP(DENSE_RANK FIRST ORDER BY SAL DESC) AS empno_min_salary
FROM
    emp_B;
    
SELECT * FROM emp_B;