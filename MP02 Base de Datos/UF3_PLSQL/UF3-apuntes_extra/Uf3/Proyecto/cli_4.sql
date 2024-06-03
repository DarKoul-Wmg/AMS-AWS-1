set serveroutput on;

create or replace procedure cli_cp (cp customer.customer_cp%type)
is
    cursor cli_cp is
    select * from customer where customer_cp = cp;
    
    existe number;
    not_found exception;
    
begin
    select count(*) into existe from customer where customer_cp = cp;
    if existe = 0 then
        raise not_found;
    end if;
    for i in cli_cp loop
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_CODE: '||i.customer_code);
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_NAME: '||i.customer_name);
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_ADDRESS: '||i.customer_address);
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_CP: '||i.customer_cp);
        DBMS_OUTPUT.PUT_LINE('BORN_DATE: '||i.born_date);
        DBMS_OUTPUT.PUT_LINE('EMAIL: '||i.email);
        DBMS_OUTPUT.PUT_LINE('--------------------');
    end loop;
    
exception
when not_found then
    dbms_output.put_line('ERROR: No se ha encontrado nada');
end;
/

begin
    cli_cp('&cp');
end;
/
