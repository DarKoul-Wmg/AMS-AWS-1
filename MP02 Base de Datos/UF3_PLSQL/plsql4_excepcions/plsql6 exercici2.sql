create or replace FUNCTION f_customer_ex6 ( IN_ID_PRODUCT products.product_id%type,
                                            IN_DATA_INI orders.order_date%type,
                                            IN_DATA_FI orders.order_date%type)
RETURN number IS
    v_ok boolean;
    v_num number(3);
    v_id customers.customer_id%type;
    v_max order_items.quantity%type;
BEGIN
    --comprovar producte si no existeix retornar null
    v_ok:=TRUE;    
    begin
        select 1 into v_num
        from products 
        where product_id = IN_ID_PRODUCT;
    exception
        when no_data_found then v_ok:=FALSE;
    end;
    IF not v_ok THEN return null; END IF;

    --buscar si hi ha comandes del producte en l'interval de dates
    v_ok:=TRUE;
    begin
        select distinct 1 into v_num
        from (select oi.product_id,o.order_date, oi.quantity 
                from orders o join order_items oi on o.order_id=oi.order_id 
                where oi.product_id=IN_ID_PRODUCT 
                and o.order_date between IN_DATA_INI AND IN_DATA_FI
                );
    exception
        when no_data_found then v_ok:=FALSE;
    end;
    --si no hi ha comandes retornar -1
    IF not v_ok THEN return -1; 
    else
    --hi ha comandes retornar el comprador que n'ha comprat més
        --calcular la quantitat màxima de producte comprada en l'inteval de dates
        select max ( prod_quantity ) into v_max
        from (select o.customer_id,sum(oi.quantity) as prod_quantity 
            from orders o join order_items oi on o.order_id=oi.order_id 
            where oi.product_id=IN_ID_PRODUCT
            and o.order_date between IN_DATA_INI AND IN_DATA_FI
            group by o.customer_id);
        --calcular el comprador que han comprat el màxim
        DBMS_OUTPUT.PUT_LINE('el màxim és ' || v_max);
        begin
            select o.customer_id into v_id
            from (select o.customer_id,sum(oi.quantity) as prod_quantity 
                from orders o join order_items oi on o.order_id=oi.order_id 
                where oi.product_id=IN_ID_PRODUCT
                and o.order_date between IN_DATA_INI AND IN_DATA_FI
                group by o.customer_id ) o
            where o.prod_quantity=v_max;
            DBMS_OUTPUT.PUT_LINE('només hi ha 1 comprador de màxim');
        exception 
            when too_many_rows then 
                DBMS_OUTPUT.PUT_LINE('hi ha més d''1 comprador de màxim');
                select o.customer_id into v_id
                from (select o.customer_id,sum(oi.quantity) as prod_quantity 
                    from orders o join order_items oi on o.order_id=oi.order_id 
                    where oi.product_id=IN_ID_PRODUCT
                    and o.order_date between IN_DATA_INI AND IN_DATA_FI
                    group by o.customer_id ) o
                where o.prod_quantity=v_max
                  and rownum=1;
        end;
        return v_id; 
    END IF;
END f_customer_ex6;
