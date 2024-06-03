declare
v_id regions.region_id%type;
v_name regions.region_name%type;
BEGIN
v_id:=1;
select region_name into v_name from regions where region_id=v_id;
DBMS_OUTPUT.PUT_LINE('El nom de la regió:'||v_id||' és '|| v_name);
v_id:=2;
select region_name into v_name from regions where region_id=v_id;
DBMS_OUTPUT.PUT_LINE('El nom de la regió:'||v_id||' és '|| v_name);
v_id:=3;
select region_name into v_name from regions where region_id=v_id;
DBMS_OUTPUT.PUT_LINE('El nom de la regió:'||v_id||' és '|| v_name);
v_id:=4;
select region_name into v_name from regions where region_id=v_id;
DBMS_OUTPUT.PUT_LINE('El nom de la regió:'||v_id||' és '|| v_name);
v_id:=5;
select region_name into v_name from regions where region_id=v_id;
DBMS_OUTPUT.PUT_LINE('El nom de la regió:'||v_id||' és '|| v_name);
END;
