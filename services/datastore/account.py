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

def register_user(conn, name, username, password):
    try:
        cur = conn.cursor()
        query = '''
            INSERT INTO public.users (name, username, password) VALUES (%s, %s, %s)
        '''
        cur.execute(query, (name, username, password))
        conn.commit()
        return "Registration successful", None
    except Exception as e:
        conn.rollback()
        return None, e