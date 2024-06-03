use hr;
select city,state_province, street_address, postal_code,
coalesce(state_province, street_address, postal_code,'No location') as loc
from locations; 


SELECT state_province,city,CONCAT(ifnull(state_province, "No state"),"-",city)
FROM hr.locations;


USE hr;
SELECT city, coalesce(state_province, street_address, postal_code) as loc,
(CASE
	WHEN state_province IS NOT NULL then "state"
	WHEN street_address IS NOT NULL then "address"
	WHEN postal_code IS NOT NULL then "postal"
else 'none'
END) as loc_origin
from locations;


use hr;
select(LCASE(SUBSTRING(UPPER(first_name), 1, 1)),SUBSTRING(UPPER(first_name), 2)) AS nombre_mod
from employees;


use hr;
select first_name,
case
	when first_name like 'A%' then 'Alfred'
    when first_name like 'B%' then 'Boniface'
    when ucase(substr(first_name,1,1)) = 'C%' then 'Charles'
    else ifnull(first_name,'no modificado')
 end as name_mod
from employees
order by first_name;


use hr;
select concat(lower(job_id),lower(left(first_name, 1)),lower(left(last_name,1)), employee_id,'@ieti.com')
from employees;

select first_name,job_id_employee_id,concat(rpad(job_id,10,'0'), ucase(substr(first_name,1,1)),lpad(employee_id,5,'0'),
'@ieti.com') as email
from employees
order by job_id;


use hr;
select first_name,
	concat(
		substr(reverse("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
				locate(ucase(substr(first_name, 1, 1)),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"),1),
substr(first_name,2)) as name_changed

from employees order by name_changed;



SELECT first_name,
        concat(
            substr("ABCDEFGHIJKLMNOPQRSTUVXYZ",
                 if(LOCATE(ucase(substr(first_name, 1,1)),
                          "ABCDEFGHIJKLMNOPQRSTUVXYZ")-
                    LOCATE('M',"ABCDEFGHIJKLMNOPQRSTUVXYZ")+1 > 0, 
                    LOCATE(ucase(substr(first_name, 1,1)),
                          "ABCDEFGHIJKLMNOPQRSTUVXYZ")-
                    LOCATE('M',"ABCDEFGHIJKLMNOPQRSTUVXYZ")+1,
                    LOCATE(ucase(substr(first_name, 1,1)),
                          "ABCDEFGHIJKLMNOPQRSTUVXYZ")-
                    LOCATE('M',"ABCDEFGHIJKLMNOPQRSTUVXYZ")+26)
                   ,
                   1),
            substr(first_name,2)
            ) as name_changed
from employees order by name_changed;
    
 
