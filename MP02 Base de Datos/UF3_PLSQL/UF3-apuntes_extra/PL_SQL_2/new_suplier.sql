SET SERVEROUTPUT ON
select * from supplier ;


create or replace procedure new_supplier(
    s_name  supplier.supplier_name%TYPE,
    s_hiredate supplier.hiredate%TYPE,
    s_sales_objective supplier.sales_objective%TYPE,
    s_real  supplier.real_sales%TYPE,
    s_boss_code supplier.boss_code%TYPE)
is
begin

    insert into product(supplier_code,supplier_name,hiredate,sales_objective,real_sales,boss_code)
    values ((select max(supplier_code)+10 from supplier),
    s_name,
    s_hiredate,
    s_sales_objective,
    s_real,
    s_boss_code);
    
    COMMIT;
end ;

select count(*) from supplier where supplier_code=100;
