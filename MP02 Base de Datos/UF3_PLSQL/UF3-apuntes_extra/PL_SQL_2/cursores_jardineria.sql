set serveroutput on

declare

var1 number:=&var1;

cursor c1 is
select c.apellido_contacto,sum(total) as tot 
from cliente c 
inner join pago p
on p.codigo_cliente = c.codigo_cliente
group by c.apellido_contacto
order by tot desc
fetch first var1 rows only ;

--emp_id employees.employee_id%TYPE;
--nom employees.first_name%TYPE;
cli_row c1%ROWTYPE;

begin
    dbms_output.put_line('----------------------------------------');
    dbms_output.put_line('--'||var1||' CLIENTES QUE MAS HAN GASTADO--');
    dbms_output.put_line('----------------------------------------');

    open c1;
    loop
    
    fetch c1 into cli_row;
    
    exit when c1%notfound;

    dbms_output.put_line('APELLIDO: '||cli_row.apellido_contacto||' --- TOTAL GASTADO: '||cli_row.tot);
    
    
    end loop;
    close c1;
end;