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
        q = "" + i
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
        q = "" + i
        c.append(q)

    v = '\n'.join(c)
    return v

    connect.commit()
    connect.close()


async def search_job(item):
    connect = sqlite3.connect('DB/NLMK_JOB_DATABASE.db')
    cursor = connect.cursor()
    criterion = item.replace(item[0], "", 1)
    queryStart = """SELECT job_title, job_link FROM job """
    queryMiddle = """WHERE job_title LIKE '%"""
    queryEnd = """%'"""
    querySetForType_of_work = "".join([queryStart, queryMiddle, criterion, queryEnd])
    print(querySetForType_of_work)
    cursor.execute(querySetForType_of_work)
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
        q = "" + i
        c.append(q)

    v = '\n'.join(c)
    return v

    connect.commit()
    connect.close()

async def search_job_in_city(item):
    connect = sqlite3.connect('DB/NLMK_JOB_DATABASE.db')
    cursor = connect.cursor()
    # Разбиваем словосочетание полученное от пользователя на список
    print(item)
    # item = item.split()
    # пример запроса
    """SELECT job_title, job_link FROM job WHERE (job_title LIKE '%уководитель%') AND (city LIKE '%осква%')"""
    # Разбиваем запрос
    queryStart = """SELECT job_title, job_link FROM job """
    queryMiddle1 = """WHERE (job_title LIKE '%"""
    # удаляем первую букву слова, чтобы регистр не препятствовал при поске в базе данных
    criterion1 = item[0]
    criterion1 = criterion1.replace(criterion1[0], "", 1)
    queryMiddle2 = """%') AND (city LIKE '%"""
    # удаляем первую букву слова, чтобы регистр не препятствовал при поске в базе данных
    criterion2 = item[1]
    criterion2 = criterion2.replace(criterion2[0], "", 1)
    queryEnd = """%')"""
    # Соединяем запрос
    querySetForType_of_work = "".join([queryStart, queryMiddle1, criterion1, queryMiddle2, criterion2, queryEnd])
    print(querySetForType_of_work)
    cursor.execute(querySetForType_of_work)
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
        q = "" + i
        c.append(q)

    v = '\n'.join(c)
    return v

    connect.commit()
    connect.close()