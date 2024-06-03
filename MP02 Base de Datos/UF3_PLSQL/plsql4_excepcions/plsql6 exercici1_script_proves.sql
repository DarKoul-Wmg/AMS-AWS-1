SET SERVEROUTPUT ON
DECLARE
  in_country_id countries.country_id%type;
  in_product_id products.product_id%Type;
  v_Return NUMBER;
BEGIN
  in_product_id := 2345;
  in_country_id := 'UK';
  v_Return := f_magatzem_ex6(in_product_id,in_country_id);
  DBMS_OUTPUT.PUT_LINE('v_Return f_magatzem_ex6= ' || v_Return);
  in_product_id := 11;
  in_country_id := 'UK';
  v_Return := f_magatzem_ex6(in_product_id,in_country_id);
  DBMS_OUTPUT.PUT_LINE('v_Return f_magatzem_ex6= ' || v_Return);
  in_product_id := 11;
  in_country_id := 'US';
  v_Return := f_magatzem_ex6(in_product_id,in_country_id);
  DBMS_OUTPUT.PUT_LINE('v_Return f_magatzem_ex6= ' || v_Return);
END;
