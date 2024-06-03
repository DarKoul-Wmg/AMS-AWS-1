-- 1
ALTER TABLE appointment
ADD CONSTRAINT appointment_call_unique
UNIQUE (veterinarian_id, appointment_date);
-- Si no es posible realizar la restricción es porque se debe a que existen citas con datos duplicados en la tabla appointment
-- donde un veterinario tiene mas de una cita en la misma hora. 
-- Para aplicar UNIQUE es necesario borrar los datos duplicados.

-- 2
ALTER TABLE appointment
ADD COLUMN created_at TIMESTAMP NOT NULL;
  