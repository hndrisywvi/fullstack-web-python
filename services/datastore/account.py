def login (conn, username:str, password:str):
    try:
        cur = conn.cursor()
        query = '''
            select username, password 
            from public.users
            where username = '{0}' and password = '{1}'
        '''.format(username, password)
        cur.execute(query)
        resdata = cur.fetchone()
        if resdata:
            return resdata, None
        else:
            raise Exception("username or password incorrect")
    except Exception as e:
        return None, e

def register_user(conn, name, username, password, role):
    try:
        cur = conn.cursor()
        query = '''
            INSERT INTO public.users (name, username, password, role, created_at) 
            VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
        '''
        cur.execute(query, (name.lower(), username.lower(), password, role))
        conn.commit()
        return "Registration successful", None
    except Exception as e:
        conn.rollback()
        return None, e

def get_user_by_username(username):
    try:
        conn, err = openConnection()
        if err:
            raise Exception(f"Database connection error: {err}")

        cur = conn.cursor()
        query = "SELECT * FROM public.users WHERE LOWER(username) = LOWER(%s)"
        cur.execute(query, (username.lower(),))
        user = cur.fetchone()
        return user, None
    except Exception as e:
        return None, e

def getListUserAccount (conn, keyword:str, limit: int, page: int):
    try:
        cur = conn.cursor()

        # terms = ""
        # if keyword not in (None):
        #     terms += f"where name = {keyword} or username = {keyword}"
        query = '''
            select u.id ,u."name" , u.username , u."role" 
            from public.users u 
        '''
        cur.execute(query)
        resdata = cur.fetchall()
        if resdata not in (None, []):
            return resdata, None
        else:
            raise Exception("data not found")
    except Exception as e:
        return None, e

def delete_user(conn, id):
    try:
        cur = conn.cursor()
        query = '''
            DELETE FROM public.users 
            WHERE id = %s
        '''
        cur.execute(query, (id))
        conn.commit()
        return "User deleted successfully", None
    except Exception as e:
        conn.rollback()
        return None, e

def update_username(conn, id, new_username):
    try:
        cur = conn.cursor()
        query = '''
            UPDATE public.users 
            SET username = %s
            WHERE id = %s
        '''
        cur.execute(query, (new_username, id))
        conn.commit()
        return "Username updated successfully", None
    except Exception as e:
        conn.rollback()
        return None, e