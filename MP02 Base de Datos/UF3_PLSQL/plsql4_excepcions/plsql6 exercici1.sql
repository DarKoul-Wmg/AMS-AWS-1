create or replace NONEDITIONABLE FUNCTION f_magatzem_ex6 ( in_id_product products.product_id%type,
                                        in_id_country countries.country_id%type)
RETURN number IS
    v_ok boolean;
    v_num number(3);
    v_id warehouses.warehouse_id%type;
    v_max inventories.quantity%type;
BEGIN
    --comprovar producte si no existeix retornar null
    v_ok:=TRUE;
    begin
        select 1 into v_num
        from products 
        where product_id = in_id_product;
    exception
        when no_data_found then v_ok:=FALSE;
    end;
    IF not v_ok THEN return null; END IF;

    --buscar magatzem del producte en el pais i quantitat màxima
    --si no n'hi ha retornar -1
    v_ok:=TRUE;
    select NVL(max(quantity),-1) into v_max
    from inventories 
    where product_id=in_id_product
      and warehouse_id in ( select warehouse_id 
                            from warehouses w, locations l
                            where w.location_id=l.location_id and l.country_id=in_id_country);
    if v_max<0 then return -1;
    --hi ha magatzem i tenim la quantitat màxima 
    --si n'hi ha més d'un retornar el 1er
   else
        begin
            select wh.warehouse_id into v_id
            from (select w.warehouse_id 
                  from warehouses w, locations l
                  where w.location_id=l.location_id and l.country_id=in_id_country) wh
                 join  inventories i ON wh.warehouse_id=i.warehouse_id
            where i.product_id=in_id_product and i.quantity= v_max;
        exception 
            when too_many_rows then 
                select wh.warehouse_id into v_id
                from (select w.warehouse_id 
                      from warehouses w, locations l
                      where w.location_id=l.location_id and l.country_id=in_id_country) wh
                     join  inventories i ON wh.warehouse_id=i.warehouse_id
                where i.product_id=in_id_product and i.quantity= v_max
                  and rownum=1;
        end;
        return v_id; 
    END IF;
END f_magatzem_ex6;
