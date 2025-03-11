CREATE DATABASE DB_inegi

use DB_inegi

CREATE TABLE Ubicacion (
    id INT PRIMARY KEY,
    tipo_vial VARCHAR(50),
    numero_ext VARCHAR(10),
    edificio_e VARCHAR(50),
    numero_int VARCHAR(10),
    tipo_asent VARCHAR(50),
    cod_postal VARCHAR(10),
    cve_mun VARCHAR(10),
    cve_loc VARCHAR(10),
    latitud DECIMAL(10, 6),
    longitud DECIMAL(10, 6)
);

CREATE TABLE Municipio (
	id INT PRIMARY KEY,
    nomb_asent VARCHAR(100),
    cve_mun VARCHAR(10)
);


CREATE TABLE Establecimiento (
    id INT PRIMARY KEY,
    nom_estab VARCHAR(255),
    raz_social VARCHAR(255),
    codigo_act VARCHAR(50),
    fecha_alta DATE
);

CREATE TABLE Contactos (
    id INT PRIMARY KEY,
    telefono VARCHAR(20),
    correoelec VARCHAR(255),
    www VARCHAR(255),
    contactos VARCHAR(255)
);