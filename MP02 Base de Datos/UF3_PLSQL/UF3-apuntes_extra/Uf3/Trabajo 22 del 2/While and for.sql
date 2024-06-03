set serveroutput on;

declare
    x numeric;
begin
    x := &x;
    for i in 1..x loop
        dbms_output.put_line(i);
    end loop;
end;
/

declare
    x numeric;
    y numeric := 1;
begin
    x := &x;
    while y <= x loop
        dbms_output.put_line(y);
        y:= y + 1;
    end loop;
end;
/


declare
    minimo numeric;
    maximo numeric;
    
begin
    minimo := &minimo;
    maximo := &maximo;
    
    if maximo < minimo then
        dbms_output.put_line('Introduce valores validos');
    else
        for i in minimo .. maximo loop
            dbms_output.put_line('Numero: ' || i);
        end loop;

    end if;
end;
/