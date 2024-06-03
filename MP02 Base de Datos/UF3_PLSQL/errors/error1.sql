declare
v_id regions.region_id%type;
v_name regions.region_name%type;
BEGIN
FOR v_id IN 1..4 LOOP
    select region_name into v_name from regions;
    DBMS_OUTPUT.PUT_LINE('El nom de la regió:'||v_id||' és '|| v_name);
END LOOP;
END;





