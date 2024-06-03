set SERVEROUTPUT on
declare
periode 	varchar2(50):='03-2017';
cust_list 	varchar2(50):='47,48';
resultado number;

begin
	resultado := F_REPETIR_COMANDES_ERIK_MOLINAWILLIAM(periode,cust_list);
	dbms_output.put_line('Orders repetides ' || resultado); 

end;