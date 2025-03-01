def login(uid,psd):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    i=0
    while i==0:
    #Format Errors
        if len(uid)!=6:
           return False
       
        elif uid[0:3].isalpha()!=True or uid[3:6].isdigit()!=True:
            return False
    #Checking the existence in database(admins)
        c.execute('select unique_id from admins;')
        r=c.fetchall()
        a=[]
        for i in r:
            a.append(i[0])
        if uid in a:
            c.execute('''select password from admins where unique_id='{}';'''.format(uid))
            p=c.fetchall()[0][0]
            if psd==p:
                return 'admin'
            else:
                return False
    #Checking the existence in database(users)
        c.execute('select unique_id from users;')
        r=c.fetchall()
        a=[]
        for i in r:
            a.append(i[0])
        if uid in a:
            c.execute('''select password from users where unique_id='{}';'''.format(uid))
            p=c.fetchall()[0][0]
            if psd==p:
                if uid[3:6]=='000':
                    return 'gp'
                else:
                    return 'user'
            else:
                return False
    #Does not exist
        else:
            return False


#Fetching villages in combo box
def villages_combo():
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    c.execute('''select v_code,v_name,district from villages order by v_code;''')
    r=c.fetchall()
    a=[]
    for i in r:
        a.append(i[0]+', '+i[1]+', '+i[2])
    return a

def genuid(e):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    c.execute('''select v_code from villages where v_name='{}';'''.format(e))
    f=(c.fetchone()[0])
    c.execute('''select count(unique_id) from users where v_code='{}';'''.format(f))
    g=str(c.fetchone()[0])
    uid=f
    if len(g)==1:
        g='00'+g
    elif len(g)==2:
        g='0'+g
    uid+=g
    return (uid)

def info(uid):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    ret = []
    #Extract Village Name
    c.execute('''select v_name from villages where v_code='{}';'''.format(uid[0:3]))
    a = c.fetchone()[0]
    b = ''
    for i in range(len(a)):
        b += a[i]+' '
    ret.append(b)
    #Extract Altitude
    c.execute('''select altitude from villages where v_code='{}';'''.format(uid[0:3]))
    a = str(c.fetchone()[0]) + ' mts'
    ret.append(a)
    #Extract Block, District, State
    c.execute('''select block, district, state from villages where v_code='{}';'''.format(uid[0:3]))
    a = c.fetchone()
    ret.extend([a[0],a[1],a[2]])
    return ret

def pop(uid):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    c.execute('''select count(aadhar) from people where unique_id like '{}';'''.format(uid[0:3]+'___'))
    a = str(c.fetchone()[0])+'+'
    a1 = ''
    for i in range(len(a)):
        a1 += a[i]+' '
    c.execute('''select count(aadhar) from people where unique_id like '{}' and sex = 'Male';'''.format(uid[0:3]+'___'))
    b = str(c.fetchone()[0])+'+'
    b1 = ''
    for i in range(len(b)):
        b1 += b[i]+' '
    c.execute('''select count(aadhar) from people where unique_id like '{}' and sex = 'Female';'''.format(uid[0:3]+'___'))
    c = str(c.fetchone()[0])+'+'
    c1 = ''
    for i in range(len(c)):
        c1 += c[i]+' '
    return (a1,b1,c1)

def reg(uid,fname, lname, aadhar, contact, occ, date, lang, edu, sex, marr):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    dob = 'date\''+date+'\''
    name = fname + ' ' + lname
    lan = lang[0]
    if len(lang)>1:
        for i in range(1,len(lang)):
            lan = lan + ',' + lang[i]
    c.execute('''insert into people values ('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}');'''.format(name,uid,aadhar,contact,sex,lan,edu,dob,occ,marr))
    m.commit()

def com(uid,to,sub,mes):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    if to=='Sarpanch':
        to=uid[0:3]+'000'
    else:
        c.execute('''select unique_id from admins where desig = '{}';'''.format(to))
        to=c.fetchone()[0]
    c.execute('''insert into communication values ('{}','{}','{}','{}',Null);'''.format(uid,to,sub,mes))
    m.commit()

def comDlog(uid):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    c.execute('''select * from communication where from_='{}';'''.format(uid))
    dlog=list()
    for rec in c.fetchall():
        st=rec[1]+':'+rec[2]+':'+rec[3]
        dlog.append(st)
    return dlog

def comMes(uid,dlog):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    dlog=dlog.split(':')
    c.execute('''select message,response from communication where from_='{}' and to_='{}' and message='{}' and subject='{}';'''.format(uid,dlog[0],dlog[2],dlog[1]))
    return c.fetchone()

def us(uid):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    c.execute('''select name from people where unique_id='{}';'''.format(uid))
    jkl = c.fetchall()
    ipl = list()
    for i in range(len(jkl)):
        ipl.append(jkl[i][0])
    return ipl

def viewp(uid,name):
    import mysql.connector as ms
    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
    c = m.cursor()
    c.execute('''select * from people where unique_id='{}' and name='{}';'''.format(uid,name))
    k = c.fetchone()
    if not k:
        return ['', '', '', '', '', '', '', '2022-02-01', '', '']
    else:
        return k

