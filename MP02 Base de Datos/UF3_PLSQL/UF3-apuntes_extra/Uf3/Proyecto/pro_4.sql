set serveroutput on;

create or replace procedure stock
is
    cursor prod is
    select * from product;
begin
    for i in prod loop
        if i.stock is null or i.stock <= i.minimum_stock then
            DBMS_OUTPUT.PUT_LINE('PRODUCT_CODE: '||i.product_code);
            DBMS_OUTPUT.PUT_LINE('DESCRIPTION: '||i.description);
            DBMS_OUTPUT.PUT_LINE('PRIZE: '||i.prize);
            DBMS_OUTPUT.PUT_LINE('STOCK: '||i.stock);
            DBMS_OUTPUT.PUT_LINE('MINIMUM_STOCK: '||i.minimum_stock);
            DBMS_OUTPUT.PUT_LINE('--------------------');
        end if;  
    end loop;
end;
/

begin
    stock;
end;
/