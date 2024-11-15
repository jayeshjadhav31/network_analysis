from connect_database import *

schema_name = 'campus'
input_table = 'classified_polygons'
threshold = -95
min_area = 8 * 1e-9  # Minimum area threshold to filter small areas

conn = get_connection()
curs = conn.cursor()

sql_query = f'''
    CREATE TABLE campus.poor_network_areas AS 
    SELECT 
        ST_Collect(ST_MakePolygon(geom)) AS geom 
    FROM (
        SELECT 
            ST_ExteriorRing((ST_Dump(geom)).geom) AS geom 
        FROM campus.classi_poors
    ) s 
    GROUP BY geom
    HAVING ST_Area(ST_Collect(ST_MakePolygon(geom))) > {min_area};
'''

# Execute the SQL query
curs.execute(sql_query)
conn.commit()
