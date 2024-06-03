set serveroutput on;


create or replace procedure cli_email (mail customer.email%type)
is
    cursor email_dominio is
    select customer_code, customer_name, customer_address, customer_cp, born_date, email, substr(email,instr(email,'@') +1, instr(substr(email, (instr(email,'@') +1)),'.') -1) as dominio from customer;
    
    existe number;
    
    not_found exception;
begin

    select count(*) into existe from customer where substr(email,instr(email,'@') +1, instr(substr(email, (instr(email,'@') +1)),'.') -1) = lower(mail);
    if existe = 0 then
        raise not_found;
    end if;
    
    for i in email_dominio loop
        if i.dominio = lower(mail) then
            DBMS_OUTPUT.PUT_LINE('CUSTOMER_CODE: '||i.customer_code);
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_NAME: '||i.customer_name);
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_ADDRESS: '||i.customer_address);
        DBMS_OUTPUT.PUT_LINE('CUSTOMER_CP: '||i.customer_cp);
        DBMS_OUTPUT.PUT_LINE('BORN_DATE: '||i.born_date);
        DBMS_OUTPUT.PUT_LINE('EMAIL: '||i.email);
        DBMS_OUTPUT.PUT_LINE('--------------------');
        end if;
    end loop;
exception
when not_found then
    dbms_output.put_line('ERROR: No se encuentra ese dominio');
end;
/

begin
    cli_email('&email');
end;
/