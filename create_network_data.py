from connect_database import *

conn = connection()
curs = conn.cursor()

sql_query = '''
    alter table campus.final_merge
    drop column if exists rsrp;

    alter table campus.final_merge
    add column if not exists rsrp INTEGER;
'''
curs.execute(sql_query)
conn.commit()

sql_query = '''
    select
        description
    from
        campus.final_merge
    order by
        ogc_fid
    ;
'''
curs.execute(sql_query)
descriptions = curs.fetchall()

num_rows = len(descriptions)

# this adds the rsrp values in separate column
for i in range(num_rows):
    first = descriptions[i][0].split()

    sql_query = f'''
        update campus.final_merge
        set rsrp = {int(first[1])}
        where ogc_fid = {i+1}
        ;
    '''
    curs.execute(sql_query)
    conn.commit()
