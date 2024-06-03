select current_date() as Date;
select current_date "date";

select employee_id, last_name, salary, ceil(salary+(salary * 0.15)) 
AS salary_nou   
from employees;

select employee_id, last_name, salary, ceil(salary+(salary * 0.15)) 
AS salary_nou, ceil(salary * 0.15) AS Increase   
from employees;


select concat(LOWER(SUBSTRING(last_name,1,1)), 
UPPER(SUBSTRING(last_name, 2))) AS 'Name',
length(first_name) AS 'lenght'
from employees
where first_name like 'J%' 
or first_name like 'A%' 
or first_name like 'M%'; 
ucase(substr(_,1,1)) in ('A', 'J', 'M');


select last_name, 
timestampdiff(MONTH, hire_date,CURDATE()) 
as MONTHS_WORKED
from employees
order by  MONTHS_WORKED ASC;

select last_name, 
timestampdiff(MONTH, hire_date,current_date+1) 
as MONTHS_WORKED,
str_to_date('20231201','%Y%m%d') as control_date_1,
str_to_date('20231231','%Y%m%d') as control_date_2,
timestampdiff(MONTH,str_to_date('20231201','%Y%m%d'),str_to_date('20231231','%Y%m%d') 
as 'MONTHS_CONTROL_1')
timestampdiff(MONTH,str_to_date('20231201','%Y%m%d'),adddate(str_to_date('20231231','%Y%m%d'),1)) 
as 'MONTHS_CONTROL_1'
from employees
order by  MONTHS_WORKED ASC;



select CONCAT(first_name,' earns ',format(salary,2), 
' monthly but wants ',format(salary*3,2)) as Dream_Salaries
from employees;
select CONCAT(first_name,' earns ',format(salary,2,'es_ES'), 
' monthly but wants ',format(salary*3,2,'es_ES')) as Dream_Salaries
from employees;


select last_name, LPAD(salary, 15, '$') AS SALARY
FROM employees;
select last_name, LPADformat((salary,2,'es_ES'),15, '$') AS SALARY
FROM employees;

select last_name, hire_date,
date_add(hire_date, INTERVAL 6 MONTH),
		(case when dayofweek(date_add(hire_date, INTERVAL 6 MONTH))= 2 then 7
		when dayofweek(date_add(hire_date,INTERVAL 6 MONTH)) = 1 then 1
		else 9-dayofweek(date_add(hire_date, INTERVAL 6 MONTH))
	end) as "hire_date_6 monday",
   date_format( 
		adddate(date_add,INTERVAL 6 MONTH),
        case when dayofweek(date_add(hire_date, INTERVAL 6 MONTH))= 2 then 7
		when dayofweek(date_add(hire_date,INTERVAL 6 MONTH)) = 1 then 1
		else 9-dayofweek(date_add(hire_date, INTERVAL 6 MONTH))
	end),
    '%W,%D of %M,%Y')AS "Review"
from employees

select last_name, hire_date, dayname(hire_date) AS dia_setmana
from employees
order by dayofweek(hire_date)-1 + (case when dayofweek(hire_date) = 1 
then 7 else 0 end);
 
 
select last_name, first_name,
IFNULL(CONCAT(FORMAT(comission_pct*100,2,'es_ES'),'%'), "No Comission") as comission
from employees;


select concat(last_name," -> ",salary," -> ",(salary/1000)," -> ",repeat("*",(salary/1000))) as EMPLOYEES_AND_THEIR_SALARIES
from employees;
select salary, concat(last_name, ',', first_name,' -salary- ',
IF(IFNULL(salary = 0))



select last_name, first_name, job_id,
	(case when job_id = 'AS_PRES' then 'A'
    when job_id = 'ST_MAN' then 'B'
    when job_id = 'IT_PROG' then 'C'
    when job_id = 'SA_REP' then 'D'
    when job_id = 'ST_CLERK' then 'E'
 else '0'end) AS GRAU
from employees e;
    