# Accesing databases using Python

## Examples of libraries used by database systems to connect to Python applications


| NOMBRE DATABASE       | NOMBRE DB API           |
|-----------------------|-------------------------|
| DB2 WAREHOUSE ON CLOUD| ibm_db                  |
| COMPOSE FOR MySQL     | MySQL Connector/Python  |
| COMPOSE FOR POSTGRESQL| psycopg2                |
| COMPOSE FOR MONGODB   | PyMongo                 |


#### Connection Objects:
* Database connections
* Manage Transactions

#### Cursor Objects
* Database Queries



---

## Descripción del Código

Este código muestra cómo trabajar con una base de datos SQLite utilizando Python y la biblioteca `sqlite3`. A continuación se detalla el flujo de trabajo:

### Instalación y Carga de sqlite3

Primero, necesitas instalar y cargar la biblioteca `sqlite3`. Puedes hacerlo descomentando la línea `#!pip install sqlite3` si aún no tienes la biblioteca instalada.

```python
import sqlite3
import pandas as pd

# Establecemos la conexión a la base de datos SQLite
conn = sqlite3.connect('INSTRUCTOR.db')
cursor = conn.cursor()
```

### Creación de la Tabla

Se crea una tabla llamada `INSTRUCTOR` dentro de la base de datos `INSTRUCTOR.db`. La tabla tiene columnas para `ID`, `FNAME`, `LNAME`, `CITY`, y `CCODE`.

```python
cursor.execute("DROP TABLE IF EXISTS INSTRUCTOR")

table = """CREATE TABLE IF NOT EXISTS INSTRUCTOR (
            ID INTEGER PRIMARY KEY NOT NULL,
            FNAME VARCHAR(20),
            LNAME VARCHAR(20),
            CITY VARCHAR(20),
            CCODE CHAR(2));"""

cursor.execute(table)
```

### Inserción de Datos

Se insertan datos en la tabla `INSTRUCTOR`, tanto individualmente como en múltiples inserciones a la vez.

```python
cursor.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
cursor.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')
```

### Consulta y Actualización de Datos

Se realiza una consulta para mostrar todos los datos en la tabla, luego se actualiza un valor específico en la tabla y se muestra nuevamente para verificar la actualización.

```python
statement ='SELECT * FROM INSTRUCTOR'
cursor.execute(statement)
output = cursor.fetchall()

# Mostrar todos los datos antes de la actualización
print("All the data")
for row in output:
  print(row)

# Actualizar un valor específico
query_update = '''update INSTRUCTOR set CITY='MOOSETOWN' WHERE FNAME = "Rav"'''
cursor.execute(query_update)

# Mostrar los datos actualizados
cursor.execute(statement)
output = cursor.fetchall()
for i in output:
  print(i)
```

### Creación de un DataFrame

Se crea un DataFrame de Pandas a partir de los datos en la tabla para su posterior análisis.

```python
dataframe = pd.read_sql(statement, conn)
print(dataframe.head())
```

### Cierre de la Conexión

Finalmente, se cierra la conexión con la base de datos.

```python
conn.close()
```

Este código es útil para entender cómo trabajar con bases de datos SQLite en Python, desde la creación de tablas hasta la inserción, consulta y actualización de datos.

--- 

# SQL MAGIC SOLO FUNCIONA EN JUPYTER NOTEBOOK


| Magic Statement        | Description                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------|
| %pwd                   | Prints the current working directory                                                                |
| %ls                    | Lists all files in the current directory                                                            |
| %history               | Shows the command history                                                                           |
| %reset                 | Resets the namespace by removing all user-defined names                                             |
| %who                   | Lists all variables in the namespace                                                               |
| %whos                  | Provides detailed information about all variables in the namespace                                  |
| %matplotlib inline     | Makes matplotlib plots appear within the notebook                                                   |
| %timeit                | Times the execution of a single statement                                                           |





