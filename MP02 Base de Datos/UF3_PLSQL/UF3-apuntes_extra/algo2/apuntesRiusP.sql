set serveroutput on;


/*Ex1*/
declare
    num_min numeric;
    num_max numeric;
    num_sal numeric;
    cont numeric;
begin
    num_min := &num_min;
    num_max := &num_max;
    num_sal := &num_sal;
    
    if num_max < num_min then
        dbms_output.put_line('El valor minimo no puede ser mayor al valor maximo');
        
    elsif num_min < 0 or num_max < 0 then
        dbms_output.put_line('El valor minimo o maxino ha de ser positivo');
        
    elsif num_sal < 1 or num_sal > (num_max - num_min) then
        dbms_output.put_line('El numero de salto ha de ser superior de 0 e inferior de ' || (num_max - num_min));
        
    else
    
        dbms_output.put_line('Rang entre ' || num_min || '  y ' || num_max || ' anys (inclosos) y salto de ' || num_sal || '...');
        
        while num_min-1 < num_max loop
            select count(*) into cont from cliente where trunc((sysdate-fechanac)/365) = num_max;
            
            dbms_output.put_line('Clientes de ' || num_max || ' anys: '|| cont);
            
            num_max := num_max - num_sal;
            
        end loop;
    end if;
    
end;
/


/*Ex2*/
declare
    obj numeric;
begin
    obj := &obj;
    if obj < 0 then
        dbms_output.put_line('Pon un valor positivo');
    else
        delete from vendedor where objetivo <= obj;
    end if;
    
end;
/


/*Ex3*/
declare
    reg numeric;
    contador numeric;
begin
    reg := &reg;
    
    if reg < 1 or reg > 4 then
        dbms_output.put_line('Introduce numeros del 1 al 4');
    else
        for i in 1..reg loop
            select count(*)
            into contador
            from departments d
            inner join locations l on d.location_id=l.location_id
            inner join countries c on l.country_id=c.country_id
            where c.region_id = i;
            
            dbms_output.put_line('En la region ' || i || ' hay ' || contador || ' departamentos');
        end loop;
    end if;
end;
/


/*Ex4*/
declare
    nom employees.first_name%type;
    ape employees.last_name%type;
    existe numeric;
    
    f_name employees.first_name%TYPE;
    l_name employees.last_name%TYPE;
    id employees.employee_id%TYPE;
    dep employees.department_id%TYPE;
begin
    nom := '&nom';
    ape := '&ape';
    
    select count(*) into existe from employees where first_name = nom and last_name = ape;
    
    if existe = 0 then
        dbms_output.put_line('El nombre del empleado no existe');
    else
        select upper(substr(first_name,1,2)), lower(substr(last_name,length(last_name))), employee_id * 3, department_id 
        into f_name, l_name, id, dep
        from employees
        where first_name = nom and last_name = ape;
        dbms_output.put_line('Hola ' || nom || ' ' || ape || ' tu contraseña segura es ' || f_name || l_name || id || dep || '@');
    end if;

end;
/


/*Ex5*/

declare
    nom pok_pokemon.nombre%type;
    pes pok_pokemon.peso%type;
    alt pok_pokemon.altura%type;
    tip pok_tipo.nombre%type;
    pre pok_pokemon.nombre%type;
    pos pok_pokemon.nombre%type;
    
    existe numeric;
    existe1 numeric;
begin
    nom := '&nom';
    pes := &pes;
    alt := &alt;
    tip := &tip;
    pre := &pre;
    pos := &pos;
    
    select count(*) into existe from pok_pokemon where nombre = nom;
    select count(*) into existe1 from pok_tipo where nombre = tip;
    if existe >= 1 then
        dbms_output.put_line('El nombre del pokemon ya existe');
    elsif pes < 0 or alt < 0 then
        dbms_output.put_line('Peso y altura han de ser positivos');
    elsif existe1 = 0 then
        insert into pok_tipo values ((select max(id_tipo)+3 from pok_tipo),tip,1);
    else
        insert into pok_pokemon values ((select max(numero_pokemon)+3 from pok_pokemon), nom, pes, alt);
        insert into pok_pokemon_tipo values ((select max(numero_pokemon) from pok_pokemon_tipo),(SELECT id_tipo FROM pok_tipo where nombre = tip));
        
        if pre != 'no' then
            insert into pok_evoluciona_de values ((select max(numero_pokedex) from pok_pokemon), (select numero_pokedex from pok_pokemon where nombre = pre));
        end if;
            
        if pos != 'no' then
            insert into pok_evoluciona_de values ((select numero_pokedex from pok_pokemon where nombre = pre), (select max(numero_pokedex) from pok_pokemon));
        end if;
    end if;
end;
/
