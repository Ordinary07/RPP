import csv
import random
import string
import sqlite3
import cherrypy

from peewee import *
from datetime import date

db = SqliteDatabase('dbase.db')


class Student(Model):
    number = IntegerField()
    fio = CharField()
    email = CharField()
    grant = IntegerField()
    group = CharField()

    class Meta:
        database = db


Student.create_table()


class Table(object):
    @cherrypy.expose
    def index(self):
        html_code = """<html>
          <head>
                <meta charset="utf-8">
                <title>Tаблица</title>
                <style>


                    h1 {{
                        font-size: 200px;
                        text-align: center;
                        text-shadow: -10px -10px 0 red, 10px -10px 0 red, -10px 10px 0 red, 10px 10px 0 red;
                        background-repeat: repeat;
                        background-blur: 10px;
                    }}
                    td, th {{
                        padding: 50px;
                        font-size: 50px;
                        border: 30px dotted yellow;
                        cursor: pointer;
                        border-radius: 100px;
                        box-shadow: inset 0px 0px 20px rgba(255, 0, 0, 0.75), 0px 0px 30px green, 0px 0px 50px blue;
                        text-shadow: none;
                    }}
                    th {{
                        background-color: black;
                        color: black;
                    }}
                    tr {{
                        transition: transform 10s ease-in-out, opacity 5s ease;
                    }}
                    tr:hover {{
                        opacity: 1;
                        background-color: yellow !important;
                    }}
                    td:hover {{
                        color: black;
                        background-repeat: repeat;
                        text-shadow: 0px 0px 30px white;
                    }}
                </style>
            </head>
          <body>
          <form method="get" action="add">
              <input type="text" value="number" name="number" />
              <input type="text" value="fio" name="fio" />
              <input type="text" value="email" name="email" />
              <input type="text" value="grant" name="grant" />
              <input type="text" value="group" name="group" />
              <button type="submit">Добавить</button>
          </form>
          <table align="center">
          <style type="text/css">
          TABLE {
              margin: auto;
              max-width: 800px;
              width: 80%;
              border-collapse: separate;
              border-spacing: 20px;
              background-color: #89e085;
              opacity: 0.8;
          }
          TD, TH {
              padding: 3px;
              border: 1px solid black;
              background-color: #cee2cd;
          }
          p{
            font-size: 50px;
        }
          </style>
          <p align="center">Студенты</p>
          <tr>
          <td align="center">Номер</td>
          <td align="center">ФИО</td>
          <td align="center">email</td>
          <td align="center">Стипендия</td>
          <td align="center">Группа</td>
          </tr>"""
        for item in Student.select():
            html_code += """<tr><form method="get" action="changes">
              <td><input type="text" value=" """ + str(item.number) + """"name="number" /></td>
              <td><input type="text" value=" """ + str(item.fio) + """"name="fio" /></td>
              <td><input type="text" value=" """ + str(item.email) + """"name="email" /></td>
              <td><input type="text" value=" """ + str(item.grant) + """"name="grant" /></td>
              <td><input type="text" value=" """ + str(item.group) + """"name="group" /></td>
              <td><input type="hidden" value=" """ + str(item.id) + """"name="id" /></td>
              <td><button type="submit">Изменить</button></td></tr>
          </form>"""
        html_code += """</table>
        </body>
        </html>"""

        return html_code

    @cherrypy.expose
    def add(self, number="number", fio="fio", email="email", grant="grant",
            group="group"):
        flag = True
        for item in Student.select():
            if item.number == int(number):
                flag = False
                break
        if flag:
            Student(number=int(number), fio=str(fio), email=str(email), grant=int(grant),
                    group=str(group)).save()
        return Table.index(self)

    @cherrypy.expose
    def changes(self, number="number", fio="fio", email="email", grant="grant",
                group="group", id="id"):
        Student(number=int(number), fio=str(fio), email=str(email), grant=int(grant),
                group=str(group)).update(number=number)
        for item in Student.select():
            if item.id == int(id):
                item.number = int(number)
                item.fio = fio.strip()
                item.email = email.strip()
                item.grant = int(grant)
                item.group = group.strip()
                item.save()
                break
        return Table.index(self)


if __name__ == '__main__':
    cherrypy.quickstart(Table())
