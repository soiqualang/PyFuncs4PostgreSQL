import psycopg2
import configparser
from osgeo import ogr
import numpy as np
import sys
import os

# os.chdir(os.path.dirname(sys.argv[0]))
#create a dictionary of parameter using configparser
def config (configFile = r'db.txt', section = 'postgresql'):
	parserA = configparser.ConfigParser()
	parserA.read(configFile)
	return dict(parserA.items(section))

def insertSQL (db,table,fieldsValues):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldState =str()
	valueState =str()
	for field, value in fieldsValues.items():
		fieldState = fieldState + "%s, "%(field)
		valueState = valueState + "'%s', "%(value)
	state = "INSERT INTO " + table + ' (' + fieldState[0:-2] + ') VALUES (' + valueState[0:-2] + ')'

	print (state)
	cur.execute(state)
	conn.commit()
	conn.close()

def selectAll (db,table):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	cur.execute("SELECT * FROM %s"%(table))
	records = cur.fetchall()
	conn.close()
	return records
	
def selectCol_where (db,table, *fields, where):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldState =str()
	for field in fields:
		fieldState = fieldState + "%s, "%(field)
	state = 'SELECT ' + fieldState[0:-2] + ' FROM ' + table + ' WHERE ' + where
	print (state)
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records


def inner_join(db,tab1, tab2, connector,*fields,where):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldState =str()
	for field in fields:
		fieldState = fieldState + "%s, "%(field)
	state = 'SELECT %s FROM %s INNER JOIN %s ON %s.%s=%s.%s WHERE %s'%(fieldState[0:-2],tab1, tab2, tab1, connector, tab2 , connector, where)
	print (state)
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records


def selectCol (db,table, *fields):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldState =str()
	for field in fields:
		fieldState = fieldState + "%s, "%(field)
	state = 'SELECT ' + fieldState[0:-2] + ' FROM ' + table
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records
#usage: update ('hehe',*{a = 1, b = 2}, where = "he = 'him'")
#or: update ('hehe',a = 1, b = 2, where = "he = 'him'")
def update (db,table,where,**fieldsValues):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldValueState = str()
	for field, value in fieldsValues.items():
		fieldValueState = fieldValueState + field + ' = ' + "'%s', " %(value)
	state = 'UPDATE ' + table + ' SET ' + fieldValueState[0:-2] +' WHERE ' + where
	cur.execute(state)
	conn.commit()
	conn.close()

def getGeom(db,Xmin,Ymin,Xmax,Ymax,Projection):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	state = 'SELECT ST_MakeEnvelope('+ str(Xmin) +',' + str(Ymin) +','+ str(Xmax) +','+ str(Ymax) +','+ str(Projection)  +')'
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records[0][0]

def getCoord(db,geom):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	state = 'SELECT  ST_AsText('+ "'%s'"%(geom) +')'	
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records[0][0]

	table = 'cctl_giatri_doman'
	fields = ['maso_tramdo','giatri']
	where = "thoigian = '%s'"%(date)
	station_value = selectCol (table, *fields, where = where)
	print (station_value)
	values, stations, xcoords, ycoords = list(), list(), list(), list()

def select_row_json (db,tab1, tab2, connector,*fields,where):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldState =str()
	for field in fields:
		fieldState = fieldState + "%s, "%(field)
	state = 'SELECT row_to_json(%s) FROM %s INNER JOIN %s ON %s.%s=%s.%s WHERE %s'%(tab1,tab1, tab2, tab1, connector, tab2, connector, where)
	print (state)
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records


def select_ST_AsGeoJSON (db,tab1, tab2, connector,*fields,where):
	conn = psycopg2.connect(**db)
	cur = conn.cursor()
	fieldState =str()
	for field in fields:
		fieldState = fieldState + "%s, "%(field)
	state = 'SELECT ST_AsGeoJSON(%s) FROM %s INNER JOIN %s ON %s.%s=%s.%s WHERE %s'%(*fields,tab1, tab2, tab1, connector, tab2, connector, where)
	print (state)
	cur.execute(state)
	records = cur.fetchall()
	conn.close()
	return records