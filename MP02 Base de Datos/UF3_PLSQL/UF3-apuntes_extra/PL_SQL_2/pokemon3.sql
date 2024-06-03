
declare
s varchar2 := &s
begin
s:=concat(upper())

select pok.nombre,mov.nombre,pok_tipo.nombre from pok_pokemon pok
inner join pok_pokemon_movimiento_forma pok_mov on pok_mov.numero_pokedex = pok.numero_pokedex
inner join pok_movimiento mov on pok_mov.id_movimiento = mov.id_movimiento
inner join pok_tipo on pok_tipo.id_tipo = mov.id_tipo;