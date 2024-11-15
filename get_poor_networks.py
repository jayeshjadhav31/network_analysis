from connect_database import *

schema_name = 'campus'
input_table = 'vectorised_raster'
threshold = -95

conn = get_connection()
curs = conn.cursor()

sql_query = f'''
    CREATE TABLE {schema_name}.classified_poors AS 
    SELECT * 
    from
        {schema_name}.{input_table} as input_table
    where
        input_table.DN < {threshold} 
'''

# Execute the SQL query
curs.execute(sql_query)
conn.commit()