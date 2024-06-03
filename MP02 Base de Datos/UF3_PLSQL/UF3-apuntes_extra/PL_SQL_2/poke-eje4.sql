/* 
4- A partir de la siguiente Query ( que debeis / podeis modificar según os surja ):

select pok.nombre,mov.nombre,pok_tipo.nombre from pok_pokemon pok
inner join pok_pokemon_movimiento_forma pok_mov on pok_mov.numero_pokedex = pok.numero_pokedex
inner join pok_movimiento mov on pok_mov.id_movimiento = mov.id_movimiento
inner join pok_tipo on pok_tipo.id_tipo = mov.id_tipo;

Realizar un programa que pida al usuario un nombre de pokemon ( este no debe de ser case sensitive ejemplo : Charmander, CHARMANDER, ChARmANDer ... ) 
y un número positivo.

A partir de este nombre de pokemon, teneis que mostrar el  número de movimientos que introduzca el usuario, siempre y cuando existan.

Si el número que introduce el usuario es 0 y el pokemon existe se mostrará un mensaje como este:
El pokemon Bulbasaur existe y has decidido mostrar 0 movimientos.

Si el número que introduce el usuario es >1 y el pokemon existe se mostrará un mensaje como este:
El pokemon Bulbasaur existe y has decidido mostrar 2 movimientos.
Hoja Afilada de tipo Planta.
Placaje de tipo Normal.

Si se cumple lo anterior, pero el número es igual o mayor que el total de movimientos, entonces se mostrará un mensaje como este:
El pokemon Bulbasaur existe y estos son todos sus movimientos:
Hoja Afilada de tipo Planta.
Placaje de tipo Normal.
...
...
...
(mostrar todos los movimientos)

Si el pokemon no existe devolver el mensaje:

No existe... ¡Gracias por participar!
*/


select * from
(select nom,nommov,tipo, rownum as r from

(select pok.nombre as nom,mov.nombre as nommov,pok_tipo.nombre aS TIPO from pok_pokemon pok
inner join pok_pokemon_movimiento_forma pok_mov on pok_mov.numero_pokedex = pok.numero_pokedex
inner join pok_movimiento mov on pok_mov.id_movimiento = mov.id_movimiento
inner join pok_tipo on pok_tipo.id_tipo = mov.id_tipo 
where pok.nombre='Bulbasaur'
)
)where r=1;