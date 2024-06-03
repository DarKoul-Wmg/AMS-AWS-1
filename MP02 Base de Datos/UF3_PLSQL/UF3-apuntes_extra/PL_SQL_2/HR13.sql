select employee_id, first_name,last_name, job_title from employees e inner join jobs j on j.job_id = e.job_id FETCH FIRST 5 row only;
/*solo salen los 5 primeros */