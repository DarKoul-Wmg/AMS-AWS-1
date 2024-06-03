/* Ejercicio 1. (2 Puntos) - BBDD PEDIDOS
PLSQL que nos muestre cuántos clientes de x edad hay en un
rango determinado que introducirá el usuario así como un rango de salto que tendrá que estar entre 1 y la diferencia entre edad_max y edad_min introducida por el usuario.
Por ejemplo, si el usuario inserta 20 y 30 de rangos de edad, el salto que ha introducido solo será valido si está entre 1 y 10 inclusive.
Los datos tienen que mostrarse de mayor a menor edad. Comprobar que los datos introducidos
son correctos. Por ejemplo no pueden haber edades negativas ...


Esta formula os será util:  trunc(sysdate-fechanac)/365;
EX (datos no reales):

 Rang entre 20 y 30 anys (inclosos) y salto de 2...
 Clientes de 30 anys: 5
 Clientes de 28 anys: 6
 Clientes de 26 anys: 0
 
...
...
..

*/

/*
Ejercicio 2 (1,5 punto). - BBDD PEDIDOS
Pedir al usuario un valor numerico positivo y borrar a todos los vendedores cuyan ventas no hayan llegado a su objetivo y cuyo objetivo sea igual o menor que el introdico por el usuario.
*/


/*Ejercicio 3 (2 punto) - BBDD HR
Sobre las tablas de la BBDD HR, el usuario introduce un número del 1 al 4 y se deben mostrar cuantos departamentos hay en las primeras 
x(numero introducido) regiones ( Las regiones tienen números correlativos como PK).
*/



/*Ejercicio 4 ( 2 puntos ). - BBDD HR

Ejercicio de Cifrado. Tabla employees de HR. Queremos generar un password seguro para un trabajador introducido por el usuario y que exista.
La contraseña tiene que ser las 2 primeras letra del nombre en mayusculas, la última letra del apellido en minusculas, numero de empleado*3,departamento,@.

Ejemplo de mensaje de salida:

Hola Steven King, tu password es STg30090@.

Si no existe devolver mensaje de que no existe el empleado.



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