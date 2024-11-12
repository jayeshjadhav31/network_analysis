from connect_database import *

schema_name = 'campus'
input_table = 'vectorised_raster'
threshold = -95

conn = connection()
curs = conn.cursor()

sql_query = f'''
    drop table if exists {schema_name}.classified_polygons;
    create table {schema_name}.classified_polygons (
        geom Geometry(MultiPolygon, 4326),
        signal varchar(20)
    );

    insert into {schema_name}.classified_polygons (
        geom, signal
    )
    select
        st_union(input_table.geom) as geom,
        'poor' as signal
    from
        {schema_name}.{input_table} as input_table
    where
        input_table.rsrp < {threshold}
    ;

    insert into {schema_name}.classified_polygons (
        geom, signal
    )
    select
        st_union(input_table.geom) as geom,
        'good' as signal
    from
        {schema_name}.{input_table} as input_table
    where
        input_table.rsrp >= {threshold}
    ;
'''
curs.execute(sql_query)
conn.commit()