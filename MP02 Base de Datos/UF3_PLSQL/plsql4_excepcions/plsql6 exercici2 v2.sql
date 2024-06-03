create or replace FUNCTION f_customer_prod ( IN_ID_PRODUCT products.product_id%type,
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
        select 1 into v_num 
        from orders o join order_items oi on o.order_id=oi.order_id 
        where oi.product_id=IN_ID_PRODUCT 
        and o.order_date between IN_DATA_INI AND IN_DATA_FI;
    exception
        when no_data_found then v_ok:=FALSE;
        when too_many_rows then null;
    end;
    --si no hi ha comandes retornar -1
    IF not v_ok THEN return -1; 
    else
		--hi ha comandes retornar el comprador que n'ha comprat més
        --ordenem per quantitat i retornem la primera fila
        begin
            select o.customer_id,sum(oi.quantity) as prod_quantity 
			into v_id, v_max
            from orders o join order_items oi on o.order_id=oi.order_id 
			where oi.product_id=IN_ID_PRODUCT
			and o.order_date between IN_DATA_INI AND IN_DATA_FI
			group by o.customer_id
            order by prod_quantity desc
			fetch FIRST 1 ROW ONLY;
        exception 
            when others then 
				-- hi ha algun error retornem -1
                v_id :=-1;
        end;
        return v_id; 
    END IF;
END f_customer_prod;