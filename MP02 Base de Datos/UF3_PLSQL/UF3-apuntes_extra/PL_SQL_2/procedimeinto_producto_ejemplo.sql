SET SERVEROUTPUT ON
declare
codi producto.codigo_producto%TYPE;
begin

productos(codi);
dbms_output.put_line(codi||' <- Este es el codigo al reves');
end;