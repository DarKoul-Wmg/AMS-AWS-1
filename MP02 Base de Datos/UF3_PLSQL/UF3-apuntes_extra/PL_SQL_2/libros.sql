select * from libros;

create or replace  PROCEDURE cierto(edito in libros.editorial%TYPE,aumento number:=10)
is 

begin 
update libros set precio=precio+(precio*aumento)/100
where editorial=edito;
end;

