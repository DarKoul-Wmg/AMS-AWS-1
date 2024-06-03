set serveroutput on;

declare
    poke_num pok_pokemon.numero_pokedex%type;
    existe numeric;
    existe1 numeric;
    existe2 numeric;
    nom_pokemon pok_pokemon.nombre%type;
    nom_pokemon1 pok_pokemon.nombre%type;
    num_pokemon numeric;
    nombre pok_pokemon.nombre%type;
begin
    poke_num := &poke_num;
    select count(*) into existe from pok_pokemon where numero_pokedex = poke_num;
    
    if existe = 0 then
        dbms_output.put_line('El pokemon no existe');
    
    else
        select count(*) into existe1 from pok_evoluciona_de where pokemon_origen = poke_num;
        select count(*)into existe2 from pok_evoluciona_de where pokemon_evolucionado = poke_num;
        select nombre into nombre from pok_pokemon where numero_pokedex = poke_num;
        
        if existe1 = 0  and existe2 = 0 then
            dbms_output.put_line('El pokemon ' || nombre || ' no evoluciona ni tiene evolucion');
                
        elsif existe1 > 0 and existe2 = 0 then
            select pokemon_evolucionado into num_pokemon from pok_evoluciona_de pe inner join pok_pokemon pk on pk.numero_pokedex=pe.pokemon_origen where pokemon_origen = poke_num;
            select nombre into nom_pokemon from pok_pokemon where numero_pokedex = num_pokemon;
            dbms_output.put_line('El pokemon ' || nombre || ' evoluciona a ' || nom_pokemon || ' y no es evolucion de nadie');
            
        elsif existe1 = 0 and existe2 > 0 then
            select nombre into nom_pokemon from pok_evoluciona_de pe inner join pok_pokemon pk on pk.numero_pokedex=pe.pokemon_origen where pokemon_evolucionado = poke_num;
            dbms_output.put_line('El pokemon ' || nombre || ' no evoluciona y es evolucion a ' || nom_pokemon);
            
        else
            select pokemon_evolucionado into num_pokemon from pok_evoluciona_de pe inner join pok_pokemon pk on pk.numero_pokedex=pe.pokemon_origen where pokemon_origen = poke_num;
            select nombre into nom_pokemon from pok_pokemon where numero_pokedex = num_pokemon;
            
            select nombre into nom_pokemon1 from pok_evoluciona_de pe inner join pok_pokemon pk on pk.numero_pokedex=pe.pokemon_origen where pokemon_evolucionado = poke_num;
    
            dbms_output.put_line('El pokemon ' || nombre || ' evoluciona a ' || nom_pokemon || ' y es evolucion de ' || nom_pokemon1);
        end if;
    end if;
end;
/