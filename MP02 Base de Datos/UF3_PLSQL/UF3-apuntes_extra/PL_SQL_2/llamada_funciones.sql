set SERVEROUTput on
select funcion_1() from dual;

select funcion_2(employee_id) from employees;


select mayor(6,9) from dual; 


begin 
if (multiplos(12,3)=true) then
DBMS_OUTPUT.PUT_LINE('Es multiple');
else
DBMS_OUTPUT.PUT_LINE('No es multiple');
end if;
end;