set serveroutput on;
/* Ejercicio 1. (2 Puntos)
PLSQL que ens mostri quants clients de x edat hi ha en un
rang determinat per l'usuari que cridara† el procediment. Comprovar que les dades introdu√Ødes
son correctes. Per exemple no poden haver edats negatives ...
EX: 
 Rang entre 20 y 30 anys (inclosos) ...
 Clients de 20 anys : 5
 Clients de 21 anys: 6
 Clients de 24 anys: 1
...

*/
declare
    aÒo1 numeric;
    aÒo2 numeric;
    numero numeric;
begin
    aÒo1 := &aÒo1;
    aÒo2 := &aÒo2;
    if aÒo2 < aÒo1 then
        dbms_output.put_line('El segundo aÒo no puede ser inferior al primero');
    elsif aÒo1 < 0 or  aÒo2 < 0 then
        dbms_output.put_line('No valen negativos');
    else
        dbms_output.put_line('Rang entre ' || aÒo1 || ' y ' || aÒo2 || ' anys');
        for i in aÒo1..aÒo2 loop
            select count(*) into numero from cliente where trunc((sysdate - fechanac)/365) = i;
            if numero != 0 then
            dbms_output.put_line('Clients de ' || i || ' anys: ' || numero );
            end if;
        end loop;
    end if;
end;
/

/*
Ejercicio 2 (1,5 punto).
Pedir al usuario un valor numerico positivo y borrar a todos los vendedores que no hayan llegado a ese objetivo.
*/
declare
    objetiv numeric;
begin
    objetiv := &objetivo;
    if objetiv < 1 then
        dbms_output.put_line('Porfavor, pon un objetivo superior a 0');
    else
        delete from vendedor where objetivo <= objetiv;
    end if;
end;
/

/*Ejercicio 3 (2 punto)
Sobre las tablas de la BBDD HR, el usuario introduce un n√∫mero del 1 al 4 y se deben mostrar cuantos departamentos hay en las primeras 
x(numero introducido) regiones ( Las regiones tienen n√∫meros correlativos como PK).
*/

declare
    region numeric;
    num_dep numeric;
    contador numeric;
begin
    contador := 0;
    region := &region;
    if region < 1 or region > 4 then
        dbms_output.put_line('Inserta valores del 1 al 4');
    else
        for i in 1..region loop
            select count(*) 
            into num_dep
            from departments d
            inner join locations l on d.location_id=l.location_id
            inner join countries c on l.country_id=c.country_id
            where region_id = i;
            contador := contador + num_dep;
        end loop;
        dbms_output.put_line('El total de departamentos de la region 1 a la region ' || region || ' es de ' ||contador);
    end if;
    
end;
/

/*Ejercicio 4 ( 2 puntos ).

Ejercicio de Cifrado. Tabla employees de HR. Queremos generar un password seguro para un trabajador introducido por el usuario y que exista.
La contrase√±a tiene que ser la primera letra del nombre en minusculas, la √∫ltima letra del apellido en mayusculas, numero de empleado y departamento, exclamaci√≥n.

Ejemplo de mensaje de salida:

Hola Steven King, tu password es sG10090!.

Si no existe devolver mensaje de que no existe el empleado.
*/

declare
    nombre employees.first_name%type;
    apellido employees.last_name%type;
    existe numeric;
    
    usr_n employees.first_name%type;
    usr_a employees.last_name%type;
    usr_num employees.employee_id%type;
    usr_d employees.department_id%type;
begin
    nombre := '&nombre';
    apellido := '&apellido';
    select count(*) into existe from employees where first_name = nombre and last_name = apellido;
    if existe = 0 then
        dbms_output.put_line('El empleado no existe');
    else
        select lower(substr(first_name,1,1)), upper(substr(last_name,length(last_name))), employee_id, department_id into usr_n, usr_a, usr_num, usr_d from employees where first_name = nombre and last_name = apellido;
        dbms_output.put_line('Hola ' || nombre || ' ' || apellido || ' tu contraseÒa segura es ' || usr_n || usr_a || usr_num || usr_d || '!');
    end if;
end;
/

/*Ejercicio 5 ( 2,5 puntos ).
Bloque PLSQL que permita insertar un pokemon nuevo Si no existe el tipo de pokemon a insertar se crear√° nuevo. 
Hay que preguntar si es preevoluci√≥n o evoluci√≥n para insertarlo en la tabla de evoluciones tambi√©n.

    
    
    El programa funcionar√° de la siguiente manera.
    El usuario introducir√° los siguientes datos ( se les pedir√° nada m√°s empezar ).
    Nombre del pokemon a insertar.
    Peso.
    Altura.
    Tipo.
    Preevolucion
    Evoluci√≥n.
    
    Realizar las siguientes comprobaciones.
    -Nombre de pokemon no existe.
        Se insertar√° el pokemon en la tabla pok_pokemon con numero_pokemon=max(numero_pokemon)+1.
    -Comprobar que el tipo de pokemon no existe: Si existe no se inserta el nuevo tipo en la tabla pok_tipo.
        Insertar la relacion entre el pokemon a introducir y el tipo ( Ejemplo Charmander(fk) - Fuego(fk) )
        El id_tipo ha de ser el max(id_tipo)+1
    -Preguntar por el nombre de su preevolucion (tabla pok_evoluciona_de).
        Si tiene, a√±adir los datos correspondientes en la tabla.
    -Preguntar por el nombre de su evolucion (tabla pok_evoluciona_de).
        Si tiene, a√±adir los datos correspondientes en la tabla.


Como ejemplo para validar que funciona, intentar introducir este pokemon,
    Nombre Sylveon
    peso=23,5
    altura=1
    tipo = Hada
    evoluci√≥n de Eevee
    no evoluciona.
    
    */
    
    
    