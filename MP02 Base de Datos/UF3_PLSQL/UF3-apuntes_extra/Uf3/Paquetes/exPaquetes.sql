set serveroutput on;

create or replace package gest_loc as
procedure insertar_nueva_loc (calle locations.street_address%type,postal locations.postal_code%type, ciudad locations.city%type, estado locations.state_province%type, coun_id locations.country_id%type);
procedure modificar_loc_calle (id locations.location_id%type, calle locations.street_address%type);
procedure modificar_loc_cod_pos (id locations.location_id%type, postal locations.postal_code%type);
procedure modificar_loc_city (id locations.location_id%type, ciudad locations.city%type);
procedure modificar_loc_prov (id locations.location_id%type, prov locations.state_province%type);
procedure modificar_loc_country (id locations.location_id%type, coun locations.country_id%type);
end gest_loc;
/
create or replace package body gest_loc as
procedure insertar_nueva_loc (calle locations.street_address%type,postal locations.postal_code%type, ciudad locations.city%type, estado locations.state_province%type, coun_id locations.country_id%type)
is
    existe number;
    id number;
begin
    select count(*) into existe from locations where lower(street_address) = lower(calle);
    if existe = 1 then
        dbms_output.put_line('Esta localizacion ya existe');
    else
        select count(*) into existe from locations where country_id = upper(coun_id);
        if existe = 0 then
            dbms_output.put_line('Este country id no es valido');
        else
            select (max(location_id) + 100) into id from locations;
            insert into locations values (id,calle,postal,ciudad,estado,coun_id);
        end if;
    end if;
end;
/*++++++++++++++++++++++++++++++++++++++++++++++++++++*/
procedure modificar_loc_calle (id locations.location_id%type, calle locations.street_address%type)
is
    existe number;
begin
    select postal_code into existe from locations where location_id = id;
    update locations
        set street_address = calle
        where location_id = id;
exception
when no_data_found then
    dbms_output.put_line('Este ID no existe');
end;
/*++++++++++++++++++++++++++++++++++++++++++++++++++++*/
procedure modificar_loc_cod_pos (id locations.location_id%type, postal locations.postal_code%type)
is
    existe number;
begin
    select postal_code into existe from locations where location_id = id;
    update locations
        set postal_code = postal
        where location_id = id;
exception
when no_data_found then
    dbms_output.put_line('Este ID no existe');
end;
/*++++++++++++++++++++++++++++++++++++++++++++++++++++*/
procedure modificar_loc_city (id locations.location_id%type, ciudad locations.city%type)
is
    existe number;
begin
    select postal_code into existe from locations where location_id = id;
    update locations
        set city = ciudad
        where location_id = id;
exception
when no_data_found then
    dbms_output.put_line('Este ID no existe');
end;
/*++++++++++++++++++++++++++++++++++++++++++++++++++++*/
procedure modificar_loc_prov (id locations.location_id%type, prov locations.state_province%type)
is
    existe number;
begin
    select postal_code into existe from locations where location_id = id;
    update locations
        set state_province = prov
        where location_id = id;
exception
when no_data_found then
    dbms_output.put_line('Este ID no existe');
end;
/*++++++++++++++++++++++++++++++++++++++++++++++++++++*/
procedure modificar_loc_country (id locations.location_id%type, coun locations.country_id%type)
is
    existe number;
begin
    select postal_code into existe from locations where location_id = id;
    select count(*) into existe from locations where country_id = upper(coun);
    if existe != 0 then
        update locations
        set country_id = coun
        where location_id = id;
    else
        dbms_output.put_line('Este Country ID no es valido');
    end if;
exception
when no_data_found then
    dbms_output.put_line('Este ID no existe');
end;
end gest_loc;
/

begin
    gest_loc.insertar_nueva_loc('&calle',&postal , '&ciudad' , '&estado' ,'&coun_id');
end;
/

begin
    gest_loc.modificar_loc_calle(&id,'&calle');
end;
/
begin
    gest_loc.modificar_loc_cod_pos(&id,&postal);
end;
/
begin
    gest_loc.modificar_loc_city(&id,'&ciudad');
end;
/
begin
    gest_loc.modificar_loc_prov(&id,'&prov');
end;
/
begin
    gest_loc.modificar_loc_country(&id,'&coun');
end;
/
select * from locations;