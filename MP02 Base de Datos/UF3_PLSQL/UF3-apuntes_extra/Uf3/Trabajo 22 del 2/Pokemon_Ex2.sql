set serveroutput on;

declare
    numero_pokedex pok_pokemon.numero_pokedex%TYPE := 155;
    nombre pok_pokemon.nombre%TYPE := 'Cyndaquil';
    peso pok_pokemon.peso%TYPE := 0.5;
    altura pok_pokemon.altura%TYPE := 7.9;
    
    ps pok_estadisticas_base.ps%TYPE := 39;
    ataque pok_estadisticas_base.ataque%TYPE := 52;
    defensa pok_estadisticas_base.defensa%TYPE := 43;
    especial pok_estadisticas_base.especial%TYPE := 60;
    velocidad pok_estadisticas_base.velocidad%TYPE := 65;
    
    valor numeric;
    
    numero numeric;
    
begin
    valor := &valor;
    numero := 1;
    
    if valor = 1 then
        insert into pok_pokemon values (numero_pokedex, nombre, peso, altura);
        insert into pok_estadisticas_base values (numero_pokedex, (ps + 4), (ataque + 2), defensa, (especial + 1), velocidad);
        numero := 0;
    elsif valor = 2 then
        insert into pok_pokemon values (numero_pokedex, nombre, peso, altura);
        insert into pok_estadisticas_base values (numero_pokedex, (ps - 3), ataque, defensa, especial, (velocidad + 9));
        numero := 0;
    elsif valor = 3 then
        insert into pok_pokemon values (numero_pokedex, nombre, 12, 1);
        insert into pok_estadisticas_base values (numero_pokedex, (ps + 3), (ataque + 3), (defensa + 3), (especial + 3), (velocidad + 3));
        numero := 0;
    else
        dbms_output.put_line('Valor no valido');
    end if;
    
    if numero = 0 then
        insert into POK_POKEMON_MOVIMIENTO_FORMA (numero_pokedex, id_movimiento, id_forma_aprendizaje)
        SELECT 155,
        ID_MOVIMIENTO,
        (select id_forma_aprendizaje from pok_forma_aprendizaje
        where id_tipo_aprendizaje = 
        (select id_tipo_aprendizaje from pok_tipo_forma_Aprendizaje where tipo_aprendizaje='Nivel')
        and rownum = 1) as id_tipo_forma
        FROM POK_MOVIMIENTO
        WHERE ID_TIPO=(SELECT ID_TIPO FROM pok_tipo WHERE NOMBRE = 'Fuego');
    end if;
end;
/