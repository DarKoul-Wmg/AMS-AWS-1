set serveroutput on;


declare
    n numeric := &n;
    
    cursor x is
    select c.apellido_contacto,sum(total) as tot from cliente c
    inner join pago p on p.codigo_cliente=c.codigo_cliente
    group by c.apellido_contacto
    order by tot desc
    fetch first n rows only;
    
    r x%rowtype;
begin
    open x;
    
        dbms_output.put_line('-------------------------------------');
        dbms_output.put_line('--' || n || ' CLIENTES QUE MAS HAN GASTADO--');
        dbms_output.put_line('-------------------------------------');
        loop
            fetch x into r;
            
            exit when x%notfound;
            dbms_output.put_line('Apellido: ' || r.apellido_contacto || '   --   ' || 'Total Gastado: ' || r.tot );
            
        end loop;
    close x;
end;
/





/*
-------------------------------------
---N(1) clientes que mas han gastado---
-------------------------------------
Apellido: x   --   Total Gastado: y
*/