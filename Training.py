import sqlite3

connect = sqlite3.connect('DB/NLMK_JOB_DATABASE.db')
cursor = connect.cursor()
cursor.execute("SELECT job_title, job_link FROM job WHERE city='Москва' ")

while True:
    data = cursor.fetchone()
    if data:
        print(data)
    else:
        break
