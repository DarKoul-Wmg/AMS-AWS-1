SET SERVEROUTPUT ON;
/* Programa que muestre las evoluciones con un rango de 1 a 10 rango agua 
   
    
*/

DECLARE

minimo INT;
maximo INT;

BEGIN

minimo:=&minimo;
maximo:=&maximo;

FOR i in minimo..maximo (select pok.nombre,nvl(pok2.nombre,'no tiene') as post,nvl(pok3.nombre,'no tiene')as previa from pok_pokemon pok
    full outer join pok_evoluciona_de evo 
    on evo.pokemon_origen=pok.numero_pokedex
    full outer join pok_evoluciona_de evo2 
    on evo2.pokemon_evolucionado=pok.numero_pokedex
    full outer join pok_pokemon pok2 on pok2.numero_pokedex=evo.pokemon_evolucionado
    full outer join pok_pokemon pok3 on pok3.numero_pokedex=evo2.pokemon_origen)
LOOP
dbms_output.put_line('Nombre: '|| i.nombre || ' Tipo: '|| i.tipo);

END LOOP;
END;

    
/* FOR i in (select pok.nombre as nombre , tip.nombre as tipo from pok_pokemon pok
    inner join pok_pokemon_tipo poktip on poktip.numero_pokedex=pok.numero_pokedex
    inner join pok_tipo tip on tip.id_tipo=poktip.id_tipo
    where tip.nombre = 'Agua')
    */
