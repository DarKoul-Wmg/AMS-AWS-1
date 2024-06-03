CREATE OR REPLACE PACKAGE pk_repetir_comandes AS

    FUNCTION f_validar_comandas_molinawilliampintoerik(p_id_comanda IN NUMBER, p_periodo VARCHAR2, p_clientes VARCHAR2) RETURN NUMBER;
    
    FUNCTION f_validarfecha_pintoerik_molinawilliam(p_periodo VARCHAR2) RETURN BOOLEAN;
    
    FUNCTION f_repeat_comanda(p_id_comanda IN NUMBER) RETURN NUMBER;

    FUNCTION f_repetir_comandes_erik_molinawilliam(p_id_comanda IN NUMBER, p_periodo VARCHAR2, p_clientes VARCHAR2) RETURN NUMBER;

END pk_repetir_comandes;

CREATE OR REPLACE PACKAGE BODY pk_repetir_comandes AS

    CREATE OR REPLACE FUNCTION F_validar_comandas_MolinaWilliamPintoErik(
    p_clients VARCHAR2,
    v_month NUMBER,
    v_year NUMBER
)   RETURN NUMBER IS
    v_orders_count NUMBER := 0;
    v_client_id NUMBER;
    str_aux VARCHAR2(4000) := p_clients || ','; -- Agregamos una coma al final para asegurar el último elemento
    v_element VARCHAR2(4000);
    BEGIN
    -- Recorre la lista de clientes
    WHILE LENGTH(str_aux) > 0 LOOP
        -- Obtener el primer ID de cliente de la lista
        v_element := TRIM(SUBSTR(str_aux, 1, INSTR(str_aux, ',', 1, 1) - 1));
        
        -- Convertir el elemento a número
        BEGIN
            v_client_id := TO_NUMBER(v_element);
        EXCEPTION
            WHEN VALUE_ERROR THEN
                -- Si el elemento no es un número, continuar con el siguiente
                CONTINUE;
        END;
        
        -- Verificar si el cliente tiene órdenes en el período indicado
        SELECT COUNT(*)
        INTO v_orders_count
        FROM orders
        WHERE customer_id = v_client_id
        AND EXTRACT(MONTH FROM order_date) = v_month
        AND EXTRACT(YEAR FROM order_date) = v_year;

        -- Si se encuentra al menos una orden, terminar la búsqueda
        IF v_orders_count > 0 THEN
            RETURN v_orders_count;
        END IF;

        -- Retallar la lista eliminando el primer elemento
        str_aux := SUBSTR(str_aux, INSTR(str_aux, ',', 1, 1) + 1);
    END LOOP;

    -- Si se recorre toda la lista y no se encuentra ninguna orden, retornar 0
    RETURN 0;

    EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        RETURN -1; -- Error genérico
    END F_validar_comandas_MolinaWilliamPintoErik;






    
    CREATE OR REPLACE FUNCTION F_validarfecha_PintoErik_MolinaWilliam(p_period VARCHAR2)
    RETURN BOOLEAN
    IS
    v_month NUMBER;
    v_year NUMBER;
    v_periode_ok BOOLEAN;

    BEGIN
    -- Validar periodo
    v_periode_ok := TRUE;

    -- periode mida 7
    IF LENGTH(p_period) != 7 THEN
        v_periode_ok := FALSE;
    ELSE
        -- Extraer mes y año
        v_month := TO_NUMBER(SUBSTR(p_period, 1, 2));
        v_year := TO_NUMBER(SUBSTR(p_period, 4));

        -- Validar mes y año
        IF v_month < 1 or v_month > 12 THEN
            v_periode_ok := FALSE;
        ELSIF v_year < 2000 or v_year > 2023 THEN
            v_periode_ok := FALSE;
        END IF;
    END IF;

    RETURN v_periode_ok;
    END F_validarfecha_PintoErik_MolinaWilliam;







    
    CREATE OR REPLACE FUNCTION "BOTIGA".f_repeat_comanda (
    id_comanda IN orders.ORDER_ID%TYPE)
    RETURN NUMBER IS
    old_date DATE;
    new_date DATE;
    new_status orders.STATUS%TYPE;
    org_customer_id customers.customer_id%TYPE;
    org_name customers.name%TYPE;
    org_address customers.address%TYPE;
    org_website customers.website%TYPE;
    org_credit_limit customers.credit_limit%TYPE;
    org_salesman_id orders.SALESMAN_ID%TYPE;
    BEGIN

    
    SELECT ORDER_DATE INTO old_date
    FROM ORDERS
    WHERE ORDER_ID = id_comanda;

    -- Sumamos 18 meses a la fecha obtenida
    new_date := ADD_MONTHS(old_date, 18);

    -- Cambiamos estado
    new_status := 'Pending';

    --Extraemos información de la comanda original
    SELECT customer_id, salesman_id
    INTO org_customer_id, org_salesman_id
    FROM ORDERS
    WHERE order_id = id_comanda;

    --Creamos la nueva comanda con los valores pedidos


    INSERT INTO orders (order_id, customer_id, status, salesman_id, order_date)
    VALUES ( ISEQ$$_80104.nextval,id_comanda, new_status, org_salesman_id, new_date);

    FOR item IN (SELECT * FROM order_items WHERE order_id = id_comanda) LOOP
        UPDATE order_items
        SET UNIT_PRICE = item.UNIT_PRICE * 1.025
        WHERE order_id = id_comanda
        AND item_id = item.item_id;
    END LOOP;

    -- Aquí seleccionamos el customerid de la comanda
    SELECT customer_id INTO org_customer_id
    FROM orders
    WHERE order_id = id_comanda;

    -- Aquí crearemos un nuevo customer
    -- Copiaremos los atributos del customer
    SELECT name, address, website, credit_limit
    INTO org_name, org_address, org_website, org_credit_limit
    FROM CUSTOMERS
    WHERE customer_id = org_customer_id;

    --Insertamos el nuevo customer con los parametros indicados
    INSERT INTO CUSTOMERS (name, address, website, credit_limit)
    VALUES (org_name, org_address, concat(org_website, '.WEK'), org_credit_limit);

    RETURN null;


    END f_repeat_comanda;






    CREATE OR REPLACE FUNCTION F_repetir_comandes_Erik_MolinaWilliam(p_period String, p_clients String)
    RETURN NUMBER --
    IS
    v_month number;
    v_year number;

    v_client_id NUMBER;
    v_orders_repeated NUMBER := 0;
    v_orders_count NUMBER := 0;

    -- Variable de control per verificar el periode y la lista
    v_periode_ok BOOLEAN;
    v_clients_ok BOOLEAN;
    v_clientes_con_comandas NUMBER;
    v_comanda_repetida NUMBER;

    CURSOR c_orders IS
        SELECT o.order_id
        FROM ORDERS o
        WHERE o.order_date BETWEEN TO_DATE('01-' || p_period, 'DD-MM-YYYY')
                               AND LAST_DAY(TO_DATE('01-' || p_period, 'DD-MM-YYYY'))
        AND (',' || p_clients || ',' LIKE '%,' || TO_CHAR(o.customer_id) || ',%')
        AND o.status = 'Shipped';


    BEGIN

-- Validar periodo
    v_periode_ok := F_validarfecha_PintoErik_MolinaWilliam(p_period);
    IF NOT v_periode_ok THEN
            RETURN -2;
    END IF;

    v_month := TO_NUMBER(SUBSTR(p_period, 1, 2));
    v_year := TO_NUMBER(SUBSTR(p_period, -4));

-- Validar string clientes
    v_clients_ok := F_validar_clientes_PintoErik_MolinaWilliam(p_clients);


    IF NOT v_clients_ok THEN
        RETURN -1;
    END IF;



-- Validar clientes con comandas
    v_clientes_con_comandas := F_validar_comandas_MolinaWilliamPintoErik(p_clients, v_month, v_year);

    IF v_clientes_con_comandas = 0  THEN
        RETURN 0;
    END IF;


    FOR r_order in c_orders LOOP


        -- Consulta para contar las comandas del cliente en el período indicado
        SELECT COUNT(*)
        INTO v_orders_count
        FROM orders o
        WHERE customer_id = o.CUSTOMER_ID AND status = 'Shipped'
        
        AND EXTRACT(MONTH FROM order_date) = v_month
        AND EXTRACT(YEAR FROM order_date) = v_year;

        


        -- FUNCION PASANDO EL CUSTOMER_ID
        v_comanda_repetida := F_REPEAT_COMANDA(r_order.order_id);

        v_orders_repeated := v_orders_repeated + v_orders_count;

    END LOOP;

    -- Si ningún cliente tiene comandas en el período, retornamos 0
    IF v_orders_repeated = 0 THEN
        RETURN 0;
    END IF;

    dbms_output.put_line('Function Executed Succesfully'); 


    RETURN v_orders_repeated;
EXCEPTION
    -- Manejo de excepciones
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        RETURN -1; 
END F_repetir_comandes_Erik_MolinaWilliam;

END pk_repetir_comandes;

