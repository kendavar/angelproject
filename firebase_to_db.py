import pyrebase
import psycopg2
import traceback


config = {
    "apiKey": "AIzaSyCUJgLF1b8HoRouY40zzb4HxL13tQGjlSo",
    "authDomain": "angel-5ac50.firebaseapp.com",
    "databaseURL": "https://angel-5ac50.firebaseio.com",
    "projectId": "angel-5ac50",
    "storageBucket": "angel-5ac50.appspot.com",
    "messagingSenderId": "783783522765"
}


firebase = pyrebase.initialize_app(config)

def insert_to_free_spirit():
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
            profilePic =None
            username = None
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
            print ("SQL QUERY :{}".format(sql))
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


def main():
    try:
        conn = psycopg2.connect(host="localhost", database="angelapp",
                                user="kendavar", password="Kaneki3inori")
        cur = conn.cursor()
        db = firebase.database()

        conn.close()
    except:
        traceback.print_exc()

    
if __name__ = "__main__":
    main()
