from pkg import openConnection
import datastore

def login(username: str, password: str):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resLogin, err = datastore.login(conn, username, password)
        if err != None:
            raise Exception(err)
        return resLogin, None
    except Exception as e:
        return None, e

def register(name, username, password):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resRegister, err = datastore.register_user(conn, name, username, password)  # Memanggil fungsi register_user dari datastore
        if err != None:
            raise Exception(err)
        return resRegister, None
    except Exception as e:
        return None, e
