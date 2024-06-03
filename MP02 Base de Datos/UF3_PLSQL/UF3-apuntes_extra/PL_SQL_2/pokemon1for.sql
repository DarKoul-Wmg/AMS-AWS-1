SET SERVEROUTPUT ON;

begin

for i in (select nombre from pok_pokemon) 
Loop

dbm_output.put_line('Nombre: '|| i.nombre);

end loop;
end;

select * from pok_pokemon;