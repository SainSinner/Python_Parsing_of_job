import sqlite3
item = input()

with sqlite3.connect('DB/NLMK_JOB_DATABASE.db') as connect:
    # cursor = connect.cursor()
    # cursor.execute("SELECT job_title, job_link FROM job WHERE city='Москва' ")
    # queryStart = """UPDATE job SET Type_of_work = CASE """
    # query1 = """WHEN job_title LIKE '%уководитель%' THEN 'руководитель' """
    # query2 = """WHEN job_title LIKE '%енеджер%' THEN 'руководитель' """
    # query3 = """WHEN job_title LIKE '%астер%' THEN 'руководитель' """
    # query4 = """WHEN job_title LIKE '%ачальник%' THEN 'руководитель' """
    # query5 = """WHEN job_title LIKE '%лавный%' THEN 'руководитель' """
    # query6 = """WHEN job_title LIKE '%eveloper%' THEN 'специалист' """
    # query7 = """WHEN job_title LIKE '%нженер%' THEN 'специалист' """
    # query8 = """WHEN job_title LIKE '%налитик%' THEN 'специалист' """
    # query9 = """WHEN job_title LIKE '%onsultant%' THEN 'специалист' """
    # query10 = """WHEN job_title LIKE '%пециалист%' THEN 'специалист' """
    # query11 = """WHEN job_title LIKE '%ценарист%' THEN 'специалист' """
    # query11 = """WHEN job_title LIKE '%cientist%' THEN 'специалист' """
    # query12 = """WHEN job_title LIKE '%колог%' THEN 'специалист' """
    # query13 = """WHEN job_title LIKE '%roduct%' THEN 'специалист' """
    # queryEnd = """ELSE 'работник' END"""
    # comandSetForType_of_work = "".join([queryStart, query1, query2, query3, query4, query5, query6, query7, query8,
    #                                     query9, query10, query11, query12, query13, queryEnd])
    cursor = connect.cursor()
    # Разбиваем словосочетание полученное от пользователя на список
    item = item.split()
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
    data = cursor.fetchmany(10)
    print(data)


