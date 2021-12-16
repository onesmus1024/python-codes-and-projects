from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import mysql.connector
import hashlib


class LoginScreen(Screen):
    def login(self):
        username1 = self.ids.user.text
        password = self.ids.password.text
        passwordDB=''
        try:
            con = mysql.connector.connect(host='localhost',user='root',password='on07mawa',database='KARU_DEV_PLATFORM')

        except mysql.connector.Error as erro:
            print(erro)
        
        else:
                
            print("connection ok ::")
            pointer = con.cursor()
            try:
                q2="SELECT password FROM user WHERE username = %s"
                val2=(username1,)
                pointer.execute(q2,val2)
                passwordDB=pointer.fetchall()
                passwordDB = passwordDB[0][0]
                con.commit()
            
            except Exception as err2:
                print("query error")
                print(err2)
                    
            else:
                has_fun = hashlib.sha256()
                password = bytes(password,'utf-8')
                has_fun.update(password)
                password = has_fun.hexdigest()
            finally:
                con.close()
        if password==passwordDB:
            self.manager.current="home"
            
        else:
            print("wrong password")

class Create_Account(Screen):

    
    def create_account(self):
        username=self.ids.user.text
        password=self.ids.password.text
        confirm_password=self.ids.confirm_password.text
        email=self.ids.email.text
        programme=self.ids.programme.text
        pass_hash=""
        if password == confirm_password and username != '':
            password=bytes(password,'utf-8')
            hash_fun = hashlib.sha256()
            hash_fun.update(password)
            pass_hash=hash_fun.hexdigest()
            try:
                con = mysql.connector.connect(host='localhost',user='root',password='on07mawa',database='KARU_DEV_PLATFORM')

            except mysql.connector.Error as erro:
                print(erro)
        
            else:
                
                print("connection ok ::")
                pointer = con.cursor()
                try:
                    q1="INSERT INTO user (username,password,email,YOB,programme) VALUES(%s,%s,%s,now(),%s)"
                    val=(username,pass_hash,email,programme)
                    pointer.execute(q1,val)
                    con.commit()
            
                except Exception as err2:
                    print("query error")
                    print(err2)
                    
                else:
            
                    pass
            finally:
                con.close()
            self.manager.current="Login"
        else:
            print("password mismatch")

class Home(Screen):
    def project(self,project):
        self.manager.current="CyberSec"

class CyberSec(Screen):
    pass

class Screens(ScreenManager):
    pass


class Login(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        return Screens()
Login().run()
