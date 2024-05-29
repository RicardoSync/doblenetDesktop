Me ayudas, quiero ingresar el id del cliente, buscarlo en la tabla cliente.
Y obtener nombre, ip, fecha instalacion, prxoximo pago y mensualidad.

CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    fecha_instalacion DATE,
    equipos VARCHAR(255),
    paquete VARCHAR(100),
    mensualidad DECIMAL(10, 2)
);


Despues de obtener esos datos, darle a un boton que se llame registro pago  y guarde. Clente id, fecha_pago y mensualidad

CREATE TABLE pago (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    fecha_pago DATE,
    mensualidad DECIMAL(10, 2)
);
