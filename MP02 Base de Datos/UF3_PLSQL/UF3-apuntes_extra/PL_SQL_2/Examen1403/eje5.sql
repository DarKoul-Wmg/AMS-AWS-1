SET SERVEROUTPUT ON;
/*Ejercicio 5 ( 2,5 puntos ). - BBDD POKEMON
    Bloque PLSQL que permita insertar un pokemon nuevo Si no existe el tipo de pokemon a insertar se creará nuevo. 
    Hay que preguntar si es preevolución o evolución para insertarlo en la tabla de evoluciones también.

    
    
    El programa funcionará de la siguiente manera.
    El usuario introducirá los siguientes datos ( se les pedirá nada más empezar ).
    Nombre del pokemon a insertar.
    Peso.
    Altura.
    Tipo.
    Preevolucion
    Evolución.
    
    Realizar las siguientes comprobaciones.
    -Nombre de pokemon no existe.
        Se insertará el pokemon en la tabla pok_pokemon con numero_pokemon=max(numero_pokemon)+3.
    -Comprobar que el tipo de pokemon no existe: Si existe no se inserta el nuevo tipo en la tabla pok_tipo. La columna id_tipo_ataque se pondrá a 1 por defecto.
        Insertar la relacion entre el pokemon a introducir y el tipo ( Ejemplo Charmander(fk) - Fuego(fk) )
        El id_tipo ha de ser el max(id_tipo)+3
    -Preguntar por el nombre de su preevolucion (tabla pok_evoluciona_de).
        Si tiene, añadir los datos correspondientes en la tabla.
    -Preguntar por el nombre de su evolucion (tabla pok_evoluciona_de).
        Si tiene, añadir los datos correspondientes en la tabla.


Como ejemplo para validar que funciona, intentar introducir este pokemon,
    Nombre Sylveon
    peso=23,5
    altura=1
    tipo = Hadita
    evolución de Eevee
    no evoluciona.
*/

/* Si tienen o no evolucion  */
select pok.nombre,nvl(pok2.nombre,'no tiene') as post,nvl(pok3.nombre,'no tiene')as previa from pok_pokemon pok
    full outer join pok_evoluciona_de evo 
    on evo.pokemon_origen=pok.numero_pokedex
    full outer join pok_evoluciona_de evo2 
    on evo2.pokemon_evolucionado=pok.numero_pokedex
    full outer join pok_pokemon pok2 on pok2.numero_pokedex=evo.pokemon_evolucionado
    full outer join pok_pokemon pok3 on pok3.numero_pokedex=evo2.pokemon_origen;

/*nombre , peso, altura  */ 
SELECT
    * FROM pok_pokemon;

DECLARE
nom INT;
peso INT;
altura INT;
tipo INT;
preevo INT;
evolu  INT;



BEGIN
nom:=&nom;
peso:=&peso;
altura:=&altura;
tipo:=&tipo;
preevo:=&preevo;
evolu:=&evolu;

/*
select nombre from pok_pokemon where nombre = 'nom';

if existe 
dbms_output.put_line('Este pokenon ya existe ');

Else

meter los datos del nuevo pokemon en uniner join de la tabla pok_pokemon y la tabla ppok_evolucion y evolucion_de

count(numero_pokedex)+1, nom , peso, altura , preevo , evolu

LOOP



END LOOP;
*/
END;