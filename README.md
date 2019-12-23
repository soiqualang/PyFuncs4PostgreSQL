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


