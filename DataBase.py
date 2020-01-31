#by Nery Ruiz
#Data base
import sqlite3 as sql
from contextlib import closing
from encrypt import encrypt
import datetime


print("Using DataBase")
class DataBase():
    def __init__(self):
        self.conn = sql.connect("Canvas_DB.sqlite")
        self.student_user = []
        self.prof_user = []
        self.lis_clas = []
        self.load_students()
        self.load_professors()
        self.load_lis_clas()
        self.enc = encrypt()
        

    def create_ad(self):
        ((self.conn).cursor()).execute("CREATE TABLE admin (username text, pass text)")
        #set default password
        with closing((self.conn).cursor()) as c:
            s = "INSERT INTO admin (username, pass) VALUES (?, ?)"
            c.execute(s, ("ADMIN", (self.enc).encrypt_mess("ADMIN")))
            (self.conn).commit()

    def get_ad_pass(self):
        with closing((self.conn).cursor())as c:
            s = "SELECT * FROM admin"
            c.execute(s)
            temp = list(c.fetchone())[-1]
        return temp    
        
    def load_students(self):
        try:
            #students info and classes that they take
            with closing((self.conn).cursor())as c:
                s = "SELECT * FROM Students"
                c.execute(s)
                self.student_user = c.fetchall()
        except sql.OperationalError as err:
            print("Created database")
            ((self.conn).cursor()).execute("CREATE TABLE Students (username text, pass text, name text, email text, classes text)")
            
    def load_professors(self):
        try:
            #professor info and classes that they give
            with closing((self.conn).cursor())as c:
                s = "SELECT * FROM Professors"
                c.execute(s)
                self.prof_user = c.fetchall()
        except sql.OperationalError as err:
            print("Created database")
            ((self.conn).cursor()).execute("CREATE TABLE Professors (username text, pass text, name text, email text, classes text)")

    def load_lis_clas(self):
        try:
            with closing(self.conn.cursor()) as c:
                s = "SELECT * FROM Classes"
                c.execute(s)
                self.lis_clas = c.fetchall()
        except sql.OperationalError as err:
            print("Creating Classes DB")
            (self.conn.cursor()).execute("CREATE TABLE Classes (class_name text, class_number text, professor text)")

    def load_class(self, name = None):#return class data
        try:
            if(name == None):
                return []
            #professor info and classes that they give
            with closing((self.conn).cursor())as c:
                s = "SELECT * FROM "+str(name)+ ""
                c.execute(s)
            return c.fetchall()
        except sql.OperationalError as err:
            print("That course doesn't exist")
            #((self.conn).cursor()).execute("CREATE TABLE "+str(name)+" (course text,  student text, grade text, final text)")
            return []
            #print("Created database")
            #((self.conn).cursor()).execute("CREATE TABLE Professors (username text, name text, email text, classes text)")

    def create_class(self, name, num, professor):#create course table in database, only admin
        try:
            found = self.is_in_lis_clas(name)
            if found:
                print("Class already exist")
                raise Exception("Class already exist")
                return False
            else:
                (self.conn.cursor()).execute("CREATE TABLE "+str(name)+" (class_number text, student text, grade text)")
                with closing(self.conn.cursor()) as c:
                    s = "INSERT INTO Classes (class_name , class_number, professor) VALUES (?, ?, ?)"
                    c.execute(s , (name, num, professor))
                    self.conn.commit()
                return True
        except Exception as err:
            print("Error Create class",err)
        '''try:
            with closing((self.conn).cursor())as c:
                s = "SELECT * FROM "+str(name)
                c.execute(s)
            print("Course already exist")
        except sql.OperationalError as err:
            ((self.conn).cursor()).execute("CREATE TABLE "+str(name)+" (course text, student text, grade text)")
            print("Course created")'''

    def update_class(self, cls, name, grade = 'I'):
        try:
            with closing ((self.conn).cursor()) as c:
                s = "UPDATE "+str(cls)+"SET grade = ? WHERE student = ?"
                c.execute(s, (grade, name))
                self.conn.commit()
        except Exception as err:
            print("Error updating class "+str(name), err)

    def get_all_class_list(self):
        try:
            clas = []
            with closing(self.conn.cursor()) as c:
                s = "SELECT class_name FROM Classes"
                c.execute(s)
                clas = c.fetchall()
            
            all_class = []
            for i in clas:
                #print(str(i[0]))
                with closing (self.conn.cursor()) as c:
                    s = "SELECT * FROM "+str(i[0])+""
                    c.execute(s)
                    temp = c.fetchall()
                    #print(list(temp))
                    if(temp != []):
                        all_class.append(list(temp))
                    else:
                        all_class.append(['',''])
            return all_class, clas
        except Exception as err:
            print("Error get all class list:", err)

    def get_class_list(self, name):
        try:
            with closing(self.conn.cursor()) as c:
                s = "SELECT * FROM "+str(name)+""
                c.execute(s)
                temp = c.fetchall()
            cls_lis = []
            for i in temp:
                cls_lis.append(i[:2])
            return cls_lis
        except Exception as err:
            print("Error get class list", err)

    def add_student_to_class(self, name, clas, grade='I'):#clas is class name not number
        try:#add student to class list
            temp = []
            with closing(self.conn.cursor()) as c:
                s = "SELECT class_number FROM Classes WHERE class_name = ?"
                c.execute(s, (str(clas),))
                temp = c.fetchone()
            #print(temp[0])
            with closing(self.conn.cursor()) as c:
                s = "INSERT INTO "+str(clas)+" (class_number, student, grade) VALUES (?, ?, ?)"
                c.execute(s, (temp[0], name, grade))
                self.conn.commit()
        except Exception as err:
            print("Add student to class:",err)

    def remove_student_from_class(self, name, clas):
        found = self.student_where_class(name)
        if found != None:#self.is_in_student(name):
            locate = found
            lis_class = (self.student_user[location[0]][-1]).split(',')
            new = lis_class[:location[1]] + lis_class[location[1]+1:]
            
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Students SET classes = ? WHERE username = ?"
                c.execute(s, (','.join(new), self.student_user[location[0]][0]))
            (self.conn).commit()
            self.load_students()

            with closing((self.conn).cursor()) as c:
                s = "DELETE FROM "+str(clas)+" WHERE student = ?"
                c.execute(s, (name,))
                self.conn.commit()
        else:
            print("Student not found")
            raise Exception ("Student not found")

    def get_classes(self):
        self.load_lis_clas()
        #print(self.lis_clas)
        return self.lis_clas

    def class_add_assignment(self, cls, assignment):
        try:
            with closing(self.conn.cursor()) as c:
                s = "INSERT INTO "+str(cls)+" "+str(assignment)
                c.execute(s)
                self.conn.commit
        except Exception as err:
            print("error Add assignment",err)
            
    def get_students(self):#get matirx
        self.load_students()
        #print(self.student_user)
        return self.student_user

    def add_student(self, user, pas, name, email, classes = []):#add a student info to student database
        try:
            temp = self.list_string(classes)
            print(temp)
            with closing((self.conn).cursor()) as c:
                s = "INSERT INTO Students (username, pass, name, email, classes) VALUES (?, ?, ?, ?, ?)"
                c.execute(s, (user, pas, name, email, temp))
                (self.conn).commit()
            self.load_students()
            return True #pass
        except sql.OperationalError as err:
            print("Error adding user: ", err)
            return False #fail

    def update_student_pass(self, user, pas):
        try:
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Students SET pass = ? WHERE username = ?"
                c.execute(s, (pas, user))
                (self.conn).commit()
            self.load_students()
            return True #pass
        except sql.OperationalError as err:
            print("Error updating user: ", err)
            return False #fail

    def update_professor_pass(self, user, pas):
        try:
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Professors SET pass = ? WHERE username = ?"
                c.execute(s, (pas, user))
                (self.conn).commit()
            self.load_professors()
            return True
        except Exception as err:
            print("Error updating professor pass",err)

    def del_student(self, name):
        try:
            self.load_students()
            with closing((self.conn).cursor()) as c:
                s = "DELETE FROM Students WHERE name = ?"
                c.execute(s, (name,))
                self.conn.commit()
            print(name+' deleted')
        except sql.OperationalError as err:
            print("Error adding user: ", err)
            return False #fail

    def del_student_user(self, name):
        try:
            self.load_students()
            with closing((self.conn).cursor()) as c:
                s = "DELETE FROM Students WHERE username = ?"
                c.execute(s, (name,))
                self.conn.commit()
            print(name+' deleted')
        except sql.OperationalError as err:
            print("Error adding user: ", err)
            return False #fail
            
    def add_class(self, name, clas):#add course to student or professor class list
        #NEED TO ADD STUDENT TO CLASS LIST
        if self.is_in_student(name):
            locate = self.find_student(name)
            lis_class = (self.student_user[locate][-1]).split(',')
            lis_class.append(clas)
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Students SET classes = ? WHERE name = ?"
                c.execute(s, (','.join(lis_class), name))
                (self.conn).commit()

            with closing((self.conn).cursor()) as c:
                s = "UPDATE Students SET classes = ? WHERE username = ?"
                c.execute(s, (','.join(lis_class), name))
                (self.conn).commit()
            
            self.load_students()
        elif self.is_in_professor(name):
            locate = self.find_professor(name)
            lis_class = (self.prof_user[locate][-1]).split(',')
            lis_class.append(clas)
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Professors SET classes = ? WHERE name = ?"
                c.execute(s, (','.join(lis_class), name))
                (self.conn).commit()

            with closing((self.conn).cursor()) as c:
                s = "UPDATE Professors SET classes = ? WHERE username = ?"
                c.execute(s, (','.join(lis_class), name))
                (self.conn).commit()
                
            self.load_professors()
        else:
            print('User not found')

    def del_class(self, name):#deletes course from student or professor class list
        with closing(self.conn.cursor()) as c:
            s = "DROP TABLE "+str(name)
            c.execute(s)
            self.conn.commit()
        print('deleted table')
        
        with closing(self.conn.cursor()) as c:
            s = "DELETE FROM Classes WHERE class_name = ?"
            c.execute(s, (name,))
        self.conn.commit()
        print('deleted from table')
            
        found = self.student_where_class(name)
        if found != None:#self.is_in_student(name):
            locate = found
            lis_class = (self.student_user[location[0]][-1]).split(',')
            new = lis_class[:location[1]] + lis_class[location[1]+1:]
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Students SET classes = ? WHERE username = ?"
                c.execute(s, (','.join(new), self.student_user[location[0]][0]))
            (self.conn).commit()
            self.load_students()
        else:
            print("Class not found")
            
        found = self.professor_where_class(name)
        if found != None:
            print ('found',found)
            location = found #student index, class index
            lis_class = (self.prof_user[location[0]][-1]).split(',')
            new = lis_class[:location[1]] + lis_class[location[1]+1:]
            print(new)
            with closing((self.conn).cursor()) as c:
                s = "UPDATE Professors SET classes = ? WHERE username = ?"
                c.execute(s, (','.join(new), self.prof_user[location[0]][0]))
            (self.conn).commit()
            self.load_professors()
        else:
            print('user not found')
        self.load_lis_clas()

    def get_professors(self):#get matrix
        self.load_professors()
        return self.prof_user

    def add_professor(self, user, pas, name, email, classes = []): #add a professor info to professor database
        try:
            temp = self.list_string(classes)
            with closing((self.conn).cursor()) as c:
                s = "INSERT INTO Professors (username, pass, name, email, classes) VALUES (?, ?, ?, ?, ?)"
                c.execute(s, (user, pas, name, email, temp))
                (self.conn).commit()
            self.load_professors()
            return True #pass
        except sql.OperationalError as err:
            print("Error adding user: ", err)
            return False #fail

    def del_professor(self, name):
        try:
            self.load_professors()
            with closing((self.conn).cursor()) as c:
                s = "DELETE FROM Professors WHERE name = ?"
                c.execute(s, (name,))
            self.conn.commit()
            print(name+' deleted')
        except sql.OperationalError as err:
            print("Error adding user: ", err)
            return False #fail

    def del_professor_user(self, name):
        try:
            self.load_professors()
            with closing((self.conn).cursor()) as c:
                s = "DELETE FROM Professors WHERE username = ?"
                c.execute(s, (name,))
            self.conn.commit()
            print(name+' deleted')
        except sql.OperationalError as err:
            print("Error adding user: ", err)
            return False #fail

    def add_professor_class(self, cls, user):
        try:
            self.load_professors()
            cls +=","+ str(self.prof_user[self.find_professor(user)][-1])
            with closing ((self.conn).cursor()) as c:
                s = "UPDATE Professors SET classes = ? WHERE username = ?"
                c.execute(s, (cls, user))
                self.conn.commit()
        except Exception as err:
            print("Add professor class",err)
        pass

    def list_string(self, a):
        temp = ''
        for i in a:
            temp = temp + str(i)+','
        return temp

    def find_student(self, a):
        self.load_students()
        for i in self.student_user:
            if a in i:
                return (self.student_user).index(i)
            else:
                pass
        return None

    def is_in_student(self, a):
        self.load_students()
        print('looking up student list')
        for i in self.student_user:
            if a in i:
                return True
            else:
                pass
        return False

    def student_where_class(self, a):
        self.load_students()
        count = 0
        for i in self.student_user:
            temp = i[-1].split(',')
            if a in temp:
                return (count, temp.index(a))
            else:
                count+=1
        return None

    def find_professor(self, a):
        self.load_professors()
        for i in self.prof_user:
            if a in i:
                return (self.prof_user).index(i)
            else:
                pass
        return None

    def is_in_professor(self, a):
        self.load_professors()
        print('looking up professor list')
        for i in self.prof_user:
            if a in i:
                return True
            else:
                pass
        return False

    def professor_where_class(self, a):
        self.load_professors()
        count = 0
        for i in self.prof_user:
            temp = i[-1].split(',')
            if a in temp:
                return (count, temp.index(a))
            else:
                count+=1
        return None

    def find_clas(self, a):
        self.load_lis_clas()
        for i in self.lis_clas:
            if a in i:
                return self.lis_clas.index(i)
            else:
                pass
        return None

    def is_in_lis_clas(self, a):
        self.load_lis_clas()
        for i in self.lis_clas:
            if a in i:
                return True
            else:
                pass
        return False

    def get_professor_classes(self, username):
        name = ''
        with closing(self.conn.cursor()) as c:
            s = "SELECT name FROM  Professors WHERE username = ?"
            c.execute(s, (username,))
            name = c.fetchone()
        #print(str(name[0]))
        cls = []
        with closing(self.conn.cursor()) as c:
            s = "SELECT class_name FROM Classes WHERE professor = ?"
            c.execute(s, (name[0],))
            temp = c.fetchall()
        for i in temp:
            cls.append(i[0])
        #print(cls)
        return cls

    def add_announcement(self, username, clas, message):
        self.now = datetime.datetime.now()
        try:
            with closing(self.conn.cursor()) as c:
                s = "INSERT INTO "+str(clas)+"_ann (date, class, message) VALUES (?, ?, ?)"
                c.execute(s, (self.now.strftime("%Y-%m-%d %H:%M"), clas, message))
                self.conn.commit()
        except sql.OperationalError as err:
            ((self.conn).cursor()).execute("CREATE TABLE "+str(clas)+"_ann (date text, class text, message text)")
            with closing(self.conn.cursor()) as c:
                s = "INSERT INTO "+str(clas)+"_ann (date, class, message) VALUES (?, ?, ?)"
                c.execute(s, (self.now.strftime("%Y-%m-%d %H:%M"), clas, message))
                self.conn.commit()
        except Exception as err:
            print("Error adding announcement:", err)

    def view_announcement(self, username, clas = ''):
        try:
            if(self.is_in_student(username)):
                with closing(self.conn.cursor()) as c:
                    s = "SELECT * FROM "+str(clas)+"_ann"
                    c.execute(s)
                    temp = c.fetchall()
                return temp
            elif(self.is_in_professor(username)):
                lis_class = self.get_professor_classes(username)
                ann = []
                for i in lis_class:
                    try:
                        with closing(self.conn.cursor()) as c:
                            s = "SELECT * FROM "+str(i)+"_ann"
                            c.execute(s)
                            temp = c.fetchall()
                        ann.append(temp)
                    except sql.OperationalError as err:
                        ann.append(['\n'])
                return ann
                    
            else:
                 raise Exception("User not found")
        except Exception as err:
            print("Error view announcement:",err)
            
    def get_student_classes(self, username):
        try:
            with closing(self.conn.cursor()) as c:
                s = "SELECT classes From Students WHERE username = ?"
                c.execute(s, (username,))
                temp = c.fetchone()[0].split(',')
            #print(temp)
            cls = []
            for i in temp:
                if i == []:
                    pass
                else:
                    cls.append(i)
            
            return cls
            
        except Exception as err:
            print("Error get student classes",err)

    
        
#d = DataBase()
#d.create_ad()
#d.add_student('nr', 'Nery Ruiz', 'neryruiz@gmail.com', '')
#print(d.list_string([2,42,]))
#print(d.get_students())
#print(d.get_students()[0][0])





    
