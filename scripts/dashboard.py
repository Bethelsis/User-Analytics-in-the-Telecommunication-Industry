import os
import pandas as pd
import mysql.connector
import numpy as np
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from mysql.connector import Error
import matplotlib.pyplot as plt

class DBoperations:

    def DBConnect(self,dbName=None):
        conn=mysql.connector.connect(host='localhost',port="3306", user='root', password="",
                            database=dbName)
        cur = conn.cursor()
        return conn, cur
   
    def createDB(self,dbName: str) -> None:
        """

        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :


        Returns
        -------

        """
        conn, cur = DBoperations.DBConnect(self)
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
        conn.commit()
        cur.close()

    def createTables(self,dbName: str) -> None:
        """

        Parameters
        ----------
        dbName :
            str:
        dbName :
            str:
        dbName:str :


        Returns
        -------

        """
        conn, cur = DBoperations.DBConnect(self,' UserAnalytics')
        sqlFile = '/home/bethelhem/User-Analytics-in-the-Telecommunication-Industry/schema.sql'
        fd = open(sqlFile, 'r')
        readSqlFile = fd.read()
        fd.close()

        sqlCommands = readSqlFile.split(';')

        for command in sqlCommands:
            try:
                res = cur.execute(command)
            except Exception as ex:
                print("Command skipped: ", command)
                print(ex)
        conn.commit()
        cur.close()

        return


    def insert_to_table(self,dbName: str, df: pd.DataFrame, table_name: str) -> None:
        """

        Parameters
        ----------
        dbName :
            str:
        df :
            pd.DataFrame:
        table_name :
            str:
        dbName :
            str:
        df :
            pd.DataFrame:
        table_name :
            str:
        dbName:str :

        df:pd.DataFrame :

        table_name:str :


        Returns
        -------

        """
        conn, cur = DBoperations.DBConnect(self,' UserAnalytics')



    
        for _, row in df.iterrows():
            sqlQuery = f"""INSERT INTO {table_name} ( Customer_ID,Social_media_usage)
                VALUES(%s, %s);"""
            data = (float(row[0]),str(row[1]))

            try:
                # Execute the SQL command
                cur.execute(sqlQuery, data)
                # Commit your changes in the database
                conn.commit()
                print("Data Inserted Successfully")
            except Exception as e:
                conn.rollback()
                print("Error: ", e)
        return

    def db_execute_fetch(self,*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
        """

        Parameters
        ----------
        *args :

        many :
            (Default value = False)
        tablename :
            (Default value = '')
        rdf :
            (Default value = True)
        **kwargs :


        Returns
        -------

        """
        connection, cursor1 = DBoperations.DBConnect(self,'UserAnalytics')
        if many:
            cursor1.executemany(*args)
        else:
            cursor1.execute(*args)

        # get column names
        field_names = [i[0] for i in cursor1.description]

        # get column values
        res = cursor1.fetchall()

        # get row count and show info
        nrow = cursor1.rowcount
        if tablename:
            print(f"{nrow} records from {tablename} table")

        cursor1.close()
        connection.close()

        # return result
        if rdf:
            return pd.DataFrame(res, columns=field_names)
        else:
            return res
class dashbrd:
    def loadData(self):
            query = "select * from Final_table"
            
            df =DBoperations.db_execute_fetch(self,query, dbName="UserAnalytics", rdf=True)
            return df  
    def Top_10_mostEngaged(self):
        df = dashbrd.loadData(self)
        df1=df.sort_values(by='Social_media_usage', ascending=False)[['Customer_ID','Social_media_usage']].head()
        st.table(df1)

         
if __name__ == "__main__":
    db1 = DBoperations()
    #db1.createDB('UserAnalytics')
    #db1.createTables('Final_table')
    df = pd.read_csv('/home/bethelhem/User-Analytics-in-the-Telecommunication-Industry/Data/final_table.csv')
    
    db1.insert_to_table('UserAnalytics', df=df, table_name='Final_table')
    #query = "select * from Final_table"
    #df1 = db1.db_execute_fetch(query, dbName="UserAnalytics", rdf=True)
    
    
   # obj1=dashbrd()
    #st.set_page_config(page_title="User Analytics in the Telecommunication Industry Dashboard", layout="wide")
    #st.markdown("<p style='padding:30px;text-align:center; background-color:#000000;color:#00ECB9;font-size:26px;border-radius:10px;'>User Analytics in the Telecommunication Industry Dashboard</p>", unsafe_allow_html=True)
    #st.markdown("<p style='padding:30px;text-align:center; background-color:#00000;color:#00CCB9;font-size:26px;border-radius:10px;'>Top 5 social media users</p>", unsafe_allow_html=True)
    #obj1.Top_10_mostEngaged()