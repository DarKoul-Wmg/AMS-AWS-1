SET SERVEROUTPUT ON
DECLARE
  in_product_id products.product_id%Type;
  in_data_ini orders.order_date%Type;
  in_data_fi  orders.order_date%Type;
  v_Return NUMBER;
BEGIN
  in_product_id := 2345;
  in_data_ini := to_date('01/01/2015','DD/MM/YYYY');
  in_data_fi  := to_date('31/12/2015','DD/MM/YYYY');
  v_Return := f_customer_prod(in_product_id,in_data_ini,in_data_fi);
  DBMS_OUTPUT.PUT_LINE('v_Return f_customer_prod= ' || v_Return);
  in_product_id := 1;
  in_data_ini := to_date('01/01/2015','DD/MM/YYYY');
  in_data_fi  := to_date('31/12/2015','DD/MM/YYYY');
  v_Return := f_customer_prod(in_product_id,in_data_ini,in_data_fi);
  DBMS_OUTPUT.PUT_LINE('v_Return f_customer_prod= ' || v_Return);
  in_product_id := 1;
  in_data_ini := to_date('01/01/2017','DD/MM/YYYY');
  in_data_fi  := to_date('31/12/2017','DD/MM/YYYY');
  v_Return := f_customer_prod(in_product_id,in_data_ini,in_data_fi);
  DBMS_OUTPUT.PUT_LINE('v_Return f_customer_prod= ' || v_Return);
  in_product_id := 10;
  in_data_ini := to_date('01/01/2016','DD/MM/YYYY');
  in_data_fi  := to_date('31/12/2017','DD/MM/YYYY');
  v_Return := f_customer_prod(in_product_id,in_data_ini,in_data_fi);
  DBMS_OUTPUT.PUT_LINE('v_Return f_customer_prod= ' || v_Return);
END;
