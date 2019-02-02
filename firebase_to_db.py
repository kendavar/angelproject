import pyrebase
import psycopg2
import traceback
import MySQLdb


config = {
    "apiKey": "AIzaSyCUJgLF1b8HoRouY40zzb4HxL13tQGjlSo",
    "authDomain": "angel-5ac50.firebaseapp.com",
    "databaseURL": "https://angel-5ac50.firebaseio.com",
    "projectId": "angel-5ac50",
    "storageBucket": "angel-5ac50.appspot.com",
    "messagingSenderId": "783783522765"
}


firebase = pyrebase.initialize_app(config)

def insert_to_free_spirit(db,cur,conn):
    try:
        free_user = dict(db.child("FREE_USER").get().val())
        free_spirit_list = [k for v, k in free_user.items() if type(k) == dict]
        cur.execute("""DELETE from angelapp_angeltable""")
        for free_spirit in free_spirit_list:
            confirmPassword = None
            created_Date = None
            description = None
            deviceToken = None
            email = None
            firstname = None
            gender = None 
            firebase_id = None
            lastname = None
            password = None
            profilePic =None
            username = None
            flag=0
            for key,value in free_spirit.items():
                if key == "confirmPassword":
                    confirmPassword = value
                elif key == "created_Date":
                    created_Date = value
                elif key == "descripition":
                    description = value 
                elif key == "deviceToken":
                    deviceToken = value 
                elif key == "email":
                    email = value
                elif key == "firstname":
                    firstname = value 
                elif key == "gender":
                    gender = gender
                elif key == "id":
                    firebase_id = value
                elif key == "lastName":
                    lastName = value 
                elif key == "password":
                    password = value 
                elif key == "profilePic":
                    profilePic = value 
                elif key == "username":
                    username = value
                elif key == "flag":
                    flag = value
            
            sql = ('INSERT INTO angelapp_angeltable'\
                    '(confirmPassword,created_Date,'\
                    'description, deviceToken,'\
                    'email, firstname, gender, firebase_id,' \
                    ' lastName, password, profilePic,'\
                    'username,flag)'\
                    'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
            print ("SQL QUERY :{}".format(sql))
            cur.execute(sql, (confirmPassword, created_Date,
                            description, deviceToken,
                            email, firstname, gender, firebase_id,
                            lastName, password, profilePic,
                            username,flag))
            conn.commit()
        print("Done")

    except:
        traceback.print_exc()



def questions():
    try:
        free_user = dict(db.child("user_Questionary").get().val())
        free_spirit_list = [k for v, k in free_user.items() if type(k) == dict]
        for free_spirit in free_spirit_list:
            questions = []
            answers = []
            question_id = None
            for key, value in free_spirit.items():
                if "Question" in key:
                    questions.append(value)
                elif "Answer" in key:
                    answers.append(value)
                elif "id" in key:
                    question_id = value
                

            sql = """INSERT INTO angelapp_angeltable
                    ("confirmPassword","created_Date",
                    description, "deviceToken",
                    email, firstname, gender, firebase_id,
                    "lastName", password, "profilePic",
                    username)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            print("SQL QUERY :{}".format(sql))
            cur.execute(sql, (confirmPassword, created_Date,
                            description, deviceToken,
                            email, firstname, gender, firebase_id,
                            lastName, password, profilePic,
                            username))
            conn.commit()
    except:
        traceback.print_exc() 

def theripst_insert_to_table():
     try:
        free_user = dict(db.child("FREE_USER").get().val())
        free_spirit_list = [k for v, k in free_user.items() if type(k) == dict]
        for free_spirit in free_spirit_list:
            confirmPassword = None
            created_Date = None
            description = None
            deviceToken = None
            email = None
            firstname = None
            gender = None
            firebase_id = None
            lastname = None
            password = None
            profilePic = None
            username = None
            for key, value in free_spirit.items():
                if key == "confirmPassword":
                    confirmPassword = value
                elif key == "created_Date":
                    created_Date = value
                elif key == "descripition":
                    description = value
                elif key == "deviceToken":
                    deviceToken = value
                elif key == "email":
                    email = value
                elif key == "firstname":
                    firstname = value
                elif key == "gender":
                    gender = gender
                elif key == "firebase_id":
                    firebase_id = value
                elif key == "lastName":
                    lastName = value
                elif key == "password":
                    password = value
                elif key == "profilePic":
                    profilePic = value
                elif key == "username":
                    username = value

            sql = """INSERT INTO angelapp_angeltable
                    ("confirmPassword","created_Date",
                    description, "deviceToken",
                    email, firstname, gender, firebase_id,
                    "lastName", password, "profilePic",
                    username)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            print("SQL QUERY :{}".format(sql))
            cur.execute(sql, (confirmPassword, created_Date,
                            description, deviceToken,
                            email, firstname, gender, firebase_id,
                            lastName, password, profilePic,
                            username))
            conn.commit()

     except:
        traceback.print_exc()

# def quotes():
#     try:
#         quotes = dict(db.child("FREE_USER").get().val())
#         free_spirit_list = [k for v, k in free_user.items() if type(k) == dict]
#         for free_spirit in free_spirit_list:



def update_db():
    try:
        #conn = psycopg2.connect(host="localhost", database="angelapp",
        #                        user="kendavar", password="Kaneki3inori")
        conn = MySQLdb.connect("localhost","root","root","angelproject",charset='utf8')
        cur = conn.cursor()
        db = firebase.database()
        insert_to_free_spirit(db,cur,conn)
        conn.close()
    except:
        traceback.print_exc()

    
# if __name__ = "__main__":
#     main()
