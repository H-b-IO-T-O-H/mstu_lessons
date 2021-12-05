from typing import Optional

from fastapi import FastAPI
import subprocess

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health/{hostname}")
def read_item(hostname: str):
    import subprocess

    # easy case
    cmd = "pwd" + hostname
    #cmd = "ping " + hostname + "| sed 3q"
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    return {"for host %s" % hostname: res.stdout or ""}


@app.get("/user/{id}")
def get_user(id: str):
    import sqlite3

    con = sqlite3.connect('identifier.sqlite')
    cur = con.cursor()
    sql = f"select username from main.users where id='{id}'"
    print(sql)
    cur.execute(sql)
    return {"user": cur.fetchall()}

