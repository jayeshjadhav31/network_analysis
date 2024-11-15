schema_name = 'campus'
centroids_table = 'centroids'  # Table containing centroid data
constructions_table = 'constructions'  # Table containing construction building data
acad_area_table = 'Acad_area'  # Table containing academic area data
outer_radius = 0.01 # Outer radius in meters (1 km)
inner_radius = 0.005   # Inner radius in meters (900 m)

conn = get_connection()
curs = conn.cursor()

sql_query = f'''

-- Step 2: Find buildings around 1 km from clustered centroids
DROP TABLE IF EXISTS {schema_name}.buildings_around_centroids;
CREATE TABLE {schema_name}.buildings_around_centroids AS
SELECT 
    b.wkb_geometry AS building_geom,
    c.geom AS centroid_geom,
    'constructions' AS source
FROM 
    campus.constructions b,
    campus.centroids c
WHERE 
    ST_DWithin(b.wkb_geometry::geography, c.geom::geography, 1000)  -- assuming 1000 meters as the distance
    AND NOT ST_DWithin(b.wkb_geometry::geography, c.geom::geography, 900)

UNION ALL

SELECT 
    a.geom AS building_geom,
    c.geom AS centroid_geom,
    'Acad_area' AS source
FROM 
    campus.acad_area a,
    campus.centroids c
WHERE 
    ST_DWithin(a.geom::geography, c.geom::geography, 1000) 
	AND NOT ST_DWithin(a.geom::geography, c.geom::geography, 900)
'''

# Execute the SQL query
curs.execute(sql_query)
conn.commit()

print("Clustered centroids and buildings around 1 km have been calculated.")
