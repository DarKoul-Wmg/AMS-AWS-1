select * from libros;

create or replace  PROCEDURE cierto(edito in libros.editorial%TYPE)
is 

begin 
update libros set precio=precio*1.1
where editorial=edito;
end;