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

def register(name, username, password, role):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resRegister, err = datastore.register_user(conn, name, username, password, role)
        if err != None:
            raise Exception(err)
        return resRegister, None
    except Exception as e:
        return None, e

def getListUserAccount(keyword:str, limit: int, page: int):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        # hit api ke service login next meet
        resListUserAccount, err = datastore.getListUserAccount(conn, keyword, limit, page )
        if err != None:
            raise Exception(err)
        return resListUserAccount, None
    except Exception as e:
        return None, e

def delete(id):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resdelete, err = datastore.delete_user(conn, id)  
        if err != None:
            raise Exception(err)
        
        return resdelete, None
    except Exception as e:
        return None, e

def update_username(id, new_username):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resupdate, err = datastore.update_username(conn, id, new_username)  
        if err != None:
            raise Exception(err)
        
        return resupdate, None
    except Exception as e:
        return None, e