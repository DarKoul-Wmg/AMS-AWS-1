set serveroutput on;

declare
    num_min numeric;
    num_max numeric;
    contar numeric;
    pokimon pok_pokemon.nombre%TYPE;
    pokimon_post varchar2(100);
    pokimon_previa varchar2(100);
begin
    num_min := &num_min;
    num_max := &num_max;
    
    
    if num_min > num_max then
        dbms_output.put_line('No se han registrado pokemon en esos rangos');
    else
        select count(*) into contar from pok_pokemon where numero_pokedex between num_min and num_max;
        
        if contar != 0 then 
            for i in num_min..num_max loop
            select pok.nombre,nvl(pok2.nombre,'no tiene') as post,nvl(pok3.nombre,'no tiene')as previa 
                into pokimon,pokimon_post,pokimon_previa
                from pok_pokemon pok
                full outer join pok_evoluciona_de evo 
                on evo.pokemon_origen=pok.numero_pokedex
                full outer join pok_evoluciona_de evo2 
                on evo2.pokemon_evolucionado=pok.numero_pokedex
                full outer join pok_pokemon pok2 on pok2.numero_pokedex=evo.pokemon_evolucionado
                full outer join pok_pokemon pok3 on pok3.numero_pokedex=evo2.pokemon_origen
                inner join pok_pokemon_tipo ppt on ppt.numero_pokedex=pok.numero_pokedex
                inner join pok_tipo pt on pt.id_tipo=ppt.id_tipo
                where pok.numero_pokedex = i
                and pt.nombre = 'Agua';
                dbms_output.put_line(pokimon || pokimon_post || pokimon_previa);
                
            end loop;
        else
            dbms_output.put_line('Pon rangos correctos');
            
        end if;
    end if;
end;
/
select pok.nombre,nvl(pok2.nombre,'no tiene') as post,nvl(pok3.nombre,'no tiene')as previa from pok_pokemon pok
            full outer join pok_evoluciona_de evo 
            on evo.pokemon_origen=pok.numero_pokedex
            full outer join pok_evoluciona_de evo2 
            on evo2.pokemon_evolucionado=pok.numero_pokedex
            full outer join pok_pokemon pok2 on pok2.numero_pokedex=evo.pokemon_evolucionado
            full outer join pok_pokemon pok3 on pok3.numero_pokedex=evo2.pokemon_origen
            inner join pok_pokemon_tipo ppt on ppt.numero_pokedex=pok.numero_pokedex
            inner join pok_tipo pt on pt.id_tipo=ppt.id_tipo
            where pok.numero_pokedex between 10 and 100
            and pt.nombre = 'Agua';
            

select * from pok_pokemon_tipo;
select * from pok_tipo;




declare
    pokimon pok_pokemon.nombre%TYPE;
    pokimon_post CHAR;
    pokimon_previa CHAR;

begin
    for i in 10..100 loop
            select pok.nombre,nvl(pok2.nombre,'no tiene') as post,nvl(pok3.nombre,'no tiene')as previa 
                into pokimon,pokimon_post,pokimon_previa
                from pok_pokemon pok
                full outer join pok_evoluciona_de evo 
                on evo.pokemon_origen=pok.numero_pokedex
                full outer join pok_evoluciona_de evo2 
                on evo2.pokemon_evolucionado=pok.numero_pokedex
                full outer join pok_pokemon pok2 on pok2.numero_pokedex=evo.pokemon_evolucionado
                full outer join pok_pokemon pok3 on pok3.numero_pokedex=evo2.pokemon_origen
                inner join pok_pokemon_tipo ppt on ppt.numero_pokedex=pok.numero_pokedex
                inner join pok_tipo pt on pt.id_tipo=ppt.id_tipo
                where pok.numero_pokedex = i
                and pt.nombre = 'Agua';
    dbms_output.put_line(pokimon || pokimon_post || pokimon_previa);
end loop;
end;
/
