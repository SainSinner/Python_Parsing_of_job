import sqlite3
import re


async def city():
    connect = sqlite3.connect('DB/NLMK_JOB_DATABASE.db')
    cursor = connect.cursor()
    query = "SELECT DISTINCT city FROM job ORDER BY city"
    cursor.execute(query)
    data = cursor.fetchall()

    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
        g.append(a)
    c = []

    for i in g:
        q = "/" + i
        c.append(q)

    v = '\n'.join(c)
    return v

    connect.commit()
    connect.close()


async def search_city(item):
    connect = sqlite3.connect('DB/NLMK_JOB_DATABASE.db')
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute("SELECT job_title, job_link FROM job WHERE city=?", m)
    data = cursor.fetchmany(25)

    k = []

    for i in data:
        k.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(k[i]))
        g.append(a)
    c = []

    for i in g:
        q = "/" + i
        c.append(q)

    v = '\n'.join(c)
    return v

    connect.commit()
    connect.close()


async def search_job(item):
    connect = sqlite3.connect('DB/NLMK_JOB_DATABASE.db')
    cursor = connect.cursor()
    m = []
    m.append(item)
# Здесь нужно доработать запрос который выводил бы все строки с вакансиями в названии вакансии которых содеражлось бы то что мы вводим после /search_job
    cursor.execute("SELECT job_title, job_link FROM job WHERE job_title =?", m)
    data = cursor.fetchmany(10)

    k = []

    for i in data:
        k.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(k[i]))
        g.append(a)
    c = []

    for i in g:
        q = "/" + i
        c.append(q)

    v = '\n'.join(c)
    return v

    connect.commit()
    connect.close()
