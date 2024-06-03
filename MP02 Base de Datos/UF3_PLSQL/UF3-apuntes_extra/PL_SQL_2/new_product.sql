SET SERVEROUTPUT ON
select * from product ;


create or replace procedure new_product(
    p_code product.PRODUCT_CODE%TYPE, 
    p_des  product.description%TYPE,
    p_prize  product.prize%TYPE,
    p_stock   product.stock%TYPE,
    p_minstock  product.minimum_stock%TYPE)
is
begin

    insert into product(PRODUCT_CODE,description,prize,stock,minimum_stock)
    values (p_code,p_des,p_prize,p_stock,p_minstock);
    
    COMMIT;
end ;

begin
    new_product('AA000','Cama','9,0','2','1');
end;

select * from product ;