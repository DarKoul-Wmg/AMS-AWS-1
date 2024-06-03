SET SERVEROUTPUT ON

create or replace procedure new_customer(
    c_name customer.customer_name%TYPE, 
    c_address  customer.customer_address%TYPE,
    c_cp  customer.customer_cp%TYPE,
    c_born   customer.born_date%TYPE,
    c_email  customer.email%TYPE)
is
begin

    insert into customer (customer_code,customer_name ,customer_address ,customer_cp ,born_date ,email)
    values ((select max(customer_code)+1 from customer),c_name, c_address,c_cp,c_born,c_email);
    
    COMMIT;
end ;


begin
    new_customer('Mireia','Avinguda','08940','26/09/2002','mireia@gmail.com');
end;


select * from customer;
