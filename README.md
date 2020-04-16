# PyFuncs4PostgreSQL
Some python functions to work with PostgreSQL Database

> Contributors: <a href="https://github.com/AndrewPham9">@AndrewPham9</a>

## To use

* Required to install `psycopg2`

`!pip install psycopg2`

* Config Database parameter connection in `db.txt`


```python
.....
import connectPostgres
db = connectPostgres.config(section = 'postgresql1')
.....
# Call function
the_geom = connectPostgres.getGeom(db,minx,miny,maxx,maxy,32648)
print(the_geom)
#result:
#0103000020887F000001000000050000000000000042C8234100000000118331410000000042C823410000000055D43241000000008A0526410000000055D43241000000008A05264100000000118331410000000042C823410000000011833141
```

***

```py
#make funtion by soiqualang

def insert_table(db,schema,table,field,value):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**db)
        with conn:
            cur = conn.cursor()
            strfield=""
            strvalue=""
            for i in range(0,(len(field)-1)):
                strfield+=field[i]+", "
                strvalue+="'"+value[i]+"', "
            strfield+=field[i+1]
            strvalue+="'"+value[i+1]+"'"
            sql_add_news="INSERT INTO "+schema+"."+table+"("+strfield+") VALUES ("+strvalue+")"
            #print(sql_add_news)
            cur.execute(sql_add_news)
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
        
def getElement(db,tbl_table,element,where,id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**db)
        with conn:
            #cur = conn.cursor()
            cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            id=str(id)
            #sql='SELECT SQLITE_VERSION()'
            sql="Select "+element+" from "+tbl_table+" where "+where+"='"+id+"'"
            #print(sql)
            cur.execute(sql)
            data = cur.fetchone()
            #data=cur.fetchall()
            return data[element]
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def table_to_array1(db,schema,table):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**db)
        with conn:
            #conn.row_factory = dict_factory
            #cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
            cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            #cur = conn.cursor()
            sql="SELECT * from "+schema+"."+table
            #print(sql)
            cur.execute(sql)
            rows = cur.fetchall()        
            '''
            for row in rows:
                print ("%s %s %s" % (row["id"], row["ques"], row["ans"]))
            '''
            return rows
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
```
