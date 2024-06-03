set serveroutput on;

create or replace procedure pro_desc (literal product.description%type)
is
    cursor lit is
    select product_code, description, prize, stock, minimum_stock, instr(description,literal) as estar from product;
    
    contador numeric := 0;
    not_found exception;
begin
    for i in lit loop
        if i.estar != 0 then
            DBMS_OUTPUT.PUT_LINE('PRODUCT_CODE: '||i.product_code);
            DBMS_OUTPUT.PUT_LINE('DESCRIPTION: '||i.description);
            DBMS_OUTPUT.PUT_LINE('PRIZE: '||i.prize);
            DBMS_OUTPUT.PUT_LINE('STOCK: '||i.stock);
            DBMS_OUTPUT.PUT_LINE('MINIMUM_STOCK: '||i.minimum_stock);
            DBMS_OUTPUT.PUT_LINE('--------------------');
            contador := contador + 1;
        end if;
    end loop;
    if contador = 0 then
        raise not_found;
    end if;
exception
when not_found then
    dbms_output.put_line('ERROR: No se han encontrado descripciones con ese literal');
end;
/

begin
    pro_desc('&literal');
end;
/
