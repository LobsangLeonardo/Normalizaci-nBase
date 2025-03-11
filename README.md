# Migración de Datos de Excel a MySQL

Este proyecto utiliza la biblioteca `pandas` para manejar los datos de Excel y `mysql.connector` para la conexión con MySQL.

## Descripción

1. Se lee el archivo de Excel y se imprimen las hojas de las tablas.
2. Se establecen las conexiones con la base de datos de MySQL.
3. Se recorre cada hoja de Excel y se identifica su correspondencia en MySQL.
4. Los datos se agrupan en lotes de 1000 registros para optimizar la inserción.
5. Al finalizar el procesamiento de cada lote, los datos se migran a la base de datos MySQL.

## Requisitos

- Python 3.x
- `pandas`
- `mysql.connector`

## Instalación

```sh
pip install pandas mysql-connector-python
```

## Uso

Ejecutar el codigo  asegurándose de tener el archivo Excel en la misma carpeta, al igual que  la base de datos bie configurada.

```sh
python inegi.py
```
