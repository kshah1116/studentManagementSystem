from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk 



#creating the login window
frm_login=Tk()
frm_login.title('LOGIN')
frm_login.geometry('500x300')
frm_login.config(bg='olivedrab1')
frm_login.resizable(False, False)

##########################################################################            

#defining function for login form
    
def login():
    
    strUSerName=txt_var.get()
    strPassword=pass_var.get()
    
    con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
    cursor=con.cursor()
    sql="select password,login_name from user  "
    
    cursor.execute(sql)
    rs=cursor.fetchall()
    print(rs)
    if  (strPassword,strUSerName,) in rs:
        #connecting to database mysql
        con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
        cursor=con.cursor()
        
        sql="select password from user where login_name= %s "
        name=(strUSerName,)
        cursor.execute(sql,name)
        rs=cursor.fetchall()
        print(rs)
        
               
        sql3="select user_type from user where password =%s"
        Pass=(strPassword,)
        
        cursor.execute(sql3,Pass)
        rs=cursor.fetchall()
        
        if rs==[('admin',)]:
            admin_window()
        elif rs==[('teacher',)]:
            teacher_window()
        else:
            student_window()
                
        
    else:
         messagebox.showinfo('Error','user name or password invalid')

    
##########################################################################            


#defining function to exit the form
def quit():
    user_ans=messagebox.askyesno('Exit','Do you want to exit')
    if user_ans==True:
        frm_login.destroy()
              
###########################################################################
        
#defining function for admin
def admin_window():
    
    #view teachers detail
    frm_login.destroy()
    frm_admin=Tk()
    frm_admin.title('ADMIN')
    frm_admin.geometry('300x300')
    frm_admin.config(bg='orange')
    frm_admin.resizable(False, False)
    
    #creating buttons for different functions
    
    l=Label(frm_admin,text='    ',bg='orange').grid(row=0,column=0)
    
    tch_detail=Button(frm_admin,text='TEACHERS DETAIL',bg='white',command=tch_details,width=30,height=1).grid(row=1,column=4)
    l=Label(frm_admin,text='    ',bg='orange').grid(row=2,column=0)

    student_detail=Button(frm_admin,text='STUDENT DETAIL',bg='white',command=student_details,width=30,height=1).grid(row=5,column=4)
    l=Label(frm_admin,text='    ',bg='orange').grid(row=6,column=0)

    adding_newmember=Button(frm_admin,text='ADD USER',bg='white',command=add_user,width=30,height=1).grid(row=7,column=4)
    
   
##########################################################################            


#definig teacher detail
def tch_details():
    
    tch_details=Tk()
    tch_details.title('TEACHER DETAILS')
    tch_details.geometry('450x500')
    tch_details.config(bg='black')
    tch_details.resizable(False, False)
    
    
    #creating frame
    lbl=Label(tch_details,text='     ',bg='black').grid(row=0,column=0)
    Left_frame=LabelFrame(tch_details,text='teacher details',bg='black',fg='orange',width=400,height=100)
    Left_frame.grid(row=2,column=2)
    lbl=Label(tch_details,text='     ',bg='black').grid(row=2,column=0)

    Right_frame=LabelFrame(tch_details,text='search result',bg='black',fg='orange',width=600,height=600)
    Right_frame.grid(row=4,column=2)
    
    
    #creating name labels
    tchNme=Label(Left_frame,text=' ',bg='black').grid(row=4,column=0)
    tchNme=Label(Left_frame,text='TEACHERS NAME ',bg='black',fg='orange').grid(row=4,column=1)
    
    tchNme=Label(Right_frame,text=' ',bg='black').grid(row=5,column=0)
    tchNme=Label(Right_frame,text=' ',bg='black').grid(row=5,column=0)
    
    
    
    #creating function to get the value
    
    def DispTeacherDetails(event):
        TeacherName_Selected=Combotch_Choosen.get()
        con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
        cursor=con.cursor()
        
        sql8='select teacher_ID from teacher where teacher_name=%s '
        Id=(TeacherName_Selected,)
                
        cursor.execute(sql8,Id)
        rs1=cursor.fetchall()
        for i in rs1:
            
            txt_var.set(i[0])
            
#defining the search command
    def SearchCmd():
        Teacher_ID=txt_var.get()
        con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
        cursor=con.cursor()
        
        sqlquery='select subject,address,mb_no,class from teacher,user where teacher.user_ID=user.user_ID AND teacher_ID=%s '
        Tch_ID=(Teacher_ID,)
                
        cursor.execute(sqlquery,Tch_ID)
        rs1=cursor.fetchall()
        for i in rs1:
            
            sub_var.set(i[0])
            address_var.set(i[1])
            mobile_var.set(i[2])
            classTaken_var.set(i[3])
            
        
    #creating combobox/dropdown boxes
        
    Combotch_Choosen =ttk.Combobox(Left_frame, width = 27)
    Combotch_Choosen.grid(row=4,column = 2) 

    
    # Adding combobox drop down list
    
    Combotch_Choosen['values'] = ('    ')
    
    #connecting to mysql database
    
    con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
    cursor=con.cursor()
    strTeacher='select teacher_name from teacher'
    cursor.execute(strTeacher)   
    rs=cursor.fetchall()
    
    #inserting data into combobox
    for i in rs:
        Combotch_Choosen['values']=Combotch_Choosen['values']+(i,)
        
         
    Combotch_Choosen.current() 
    #binding the combobox
    Combotch_Choosen.bind('<<ComboboxSelected>>',DispTeacherDetails)
    
    #creating label to display
    
    tchNme2=Label(Left_frame,text='TEACHER ID ',bg='black',fg='orange').grid(row=5,column=1)
    txt_var=StringVar(Left_frame)
    txtTeacherId=Entry(Left_frame,textvariable=txt_var).grid(row=5,column=2)
   
    #creating search button
    lblForSpace=Label(Left_frame,text='  ',bg='black').grid(row=6,column=2)
    search_button=Button(Left_frame,text='search',bg='orange',command=SearchCmd,width=25).grid(row=7,column=2,sticky=W)
    
#creating label for right frame
    
    #creating lbl for search
    lblForSpace=Label(Right_frame,text='            ',bg='black').grid(row=0,column=0)
    subjectLabel=Label(Right_frame,text='SUBJECT ',bg='black',fg='orange').grid(row=5,column=1,sticky=W)
    
    #displaying the subject of selected teacher
    sub_var=StringVar(Right_frame)
    txtTeacherId=Entry(Right_frame,textvariable=sub_var).grid(row=5,column=2)
    lblForSpace6=Label(Right_frame,text='            ',bg='black').grid(row=5,column=3)

    
    #displaying address
    lblForSpace=Label(Right_frame,text='            ',bg='black').grid(row=6,column=2)
    addressLabel=Label(Right_frame,text='ADDRESS',bg='black',fg='orange').grid(row=7,column=1,sticky=W)
    address_var=StringVar(Right_frame)
    AddTeacherId=Entry(Right_frame,textvariable=address_var).grid(row=7,column=2)
    
    
    #displaying mobile number
    lblForSpace1=Label(Right_frame,text='  ',bg='black').grid(row=8,column=2)
    mobileLabel=Label(Right_frame,text='MOBILE NUMBER',bg='black',fg='orange').grid(row=9,column=1,sticky=W)
    mobile_var=StringVar(Right_frame)
    mobTeacherId=Entry(Right_frame,textvariable=mobile_var).grid(row=9,column=2)
    #lblForSpace=Label(Right_frame,text='            ',bg='black').grid(row=10,column=2)
    
    
    #diaplaying CLASS TAKEN by the teacher
    lblForSpace1=Label(Right_frame,text='  ',bg='black').grid(row=10,column=2)
    classTakenLabel=Label(Right_frame,text='CLASS TAKEN',bg='black',fg='orange').grid(row=11,column=1,sticky=W)
    classTaken_var=StringVar(Right_frame)
    classTakenTeacherEntry=Entry(Right_frame,textvariable=classTaken_var).grid(row=11,column=2)



    
    tch_details.mainloop()
#########################################################################################################
#defining a function for student details
def student_details():
    
    
    student_details=Tk()
    student_details.title('STUDENT DETAILS')
    student_details.geometry('600x500')
    student_details.config(bg='#91093b')
    student_details.resizable(False, False)
    
    def SearchCmdStudent():
         
        Class_choosen=ComboStudent_Choosen.get()
        if Class_choosen=='12A':
            Class_choosen1=1
        else:
            Class_choosen1=2
        
        
        #connecting to mysql
        con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
        cursor=con.cursor()
        
        sqlquery='select student_ID,student_name,mb_no,class_ID from student where  class_ID=%s '
        Class_id=(Class_choosen1,)
                
        cursor.execute(sqlquery,Class_id)
        rs1=cursor.fetchall()
        
        
        #creating labels for columns
        lbl=Label(Right_frame,text='STUDENT ID',bg='#91093b',fg='white',font=3).grid(row=1,column=1)
        lbl=Label(student_details,text='     ',bg='#91093b').grid(row=0,column=2)

        lbl=Label(Right_frame,text='STUDENT NAME',bg='#91093b',fg='white',font=3).grid(row=1,column=3)
        lbl=Label(student_details,text='     ',bg='#91093b').grid(row=0,column=4)

        lbl=Label(Right_frame,text='STUDENT MOBILE',bg='#91093b',fg='white',font=3).grid(row=1,column=5)
        
        J=2
        for i in rs1:
            
              #displaying the data obtained through mysql

                lbl=Label(Right_frame,text=i[0],bg='#91093b',fg='white',font=2).grid(row=J,column=1)
                lbl=Label(Right_frame,text='     ',bg='#91093b').grid(row=0,column=2)

                lbl=Label(Right_frame,text=i[1],bg='#91093b',fg='white',font=2).grid(row=J,column=3)
                lbl=Label(Right_frame,text='     ',bg='#91093b').grid(row=0,column=4)

                lbl=Label(Right_frame,text=i[2],bg='#91093b',fg='white',font=2).grid(row=J,column=5)
                J=J+1
            
                         
    
    #creating frame
    
    lbl=Label(student_details,text='     ',bg='#91093b').grid(row=0,column=0)
    Left_frame=LabelFrame(student_details,text='student details',bg='#91093b',fg='white',width=400,height=100)
    Left_frame.grid(row=2,column=2)
    lbl=Label(student_details,text='     ',bg='#91093b').grid(row=2,column=0)
    
    
    Right_frame=LabelFrame(student_details,text='search result',bg='#91093b',fg='white',width=400,height=100)
    Right_frame.grid(row=4,column=2)
    
 
           
    #creating combobox/dropdown boxes
    
    Student_class=Label(Left_frame,text='CLASS ',bg='#91093b',fg='white',font=3).grid(row=4,column=1)
    
    ComboStudent_Choosen =ttk.Combobox(Left_frame, width = 27)
    ComboStudent_Choosen.grid(row=4,column = 2) 
    
    
    # Adding combobox drop down list
    
    ComboStudent_Choosen['values'] = ('    ')
    
    
    
    con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
    cursor=con.cursor()
    strClass='select distinct class from class'
    cursor.execute(strClass)   
    rs=cursor.fetchall()
    
    #inserting data into combobox
    for i in rs:
        ComboStudent_Choosen['values']=ComboStudent_Choosen['values']+(i,)
        
         
    
    
    ComboStudent_Choosen.current() 
    #binding the combobox
    #ComboStudent_Choosen.bind('<<ComboboxSelected>>',DispTeacherDetails)
    
    
    
    #creating search button
    lbl=Label(Left_frame,text='     ',bg='#91093b').grid(row=5,column=0)
    btnsrch=Button(Left_frame,text='Search',command=SearchCmdStudent,bg='white',width=30,height=1).grid(row=14,column=2)

    student_details.mainloop()
####################################################################################################################3

def add_user():
    
    add_user=Tk()
    add_user.title('ADD USER')
    add_user.geometry('300x100')
    add_user.config(bg='black')
    add_user.resizable(False, False)
    
    type_lbl=Label(add_user,text=' ',bg='black').grid(row=0,column=0)
    type_lbl=Label(add_user,text='TYPE',fg='orange',bg='black',).grid(row=7,column=2)
   
    def choosing_type(event):
        
           
        def addstudent():
            
           #getting the values entered in entry boxes
           IDstudent=studentID_var2.get()
           Name_student=studentName_var.get()
           Mobile_student=studentMobile_var.get()
           ClassId_student=studentClassLabel_var.get()
           password1=pass_var.get()
           user_id=USER_id_var.get()
           address=address_var.get()
           #connecting to mysql through python
           con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
           cursor=con.cursor()
           sqlquery='INSERT INTO  student (student_ID,student_name,mb_no,class_ID) VALUES(%s,%s,%s,%s) '
           sqlquery1='INSERT INTO  user (user_ID, name, login_name, password, mb_no, address, user_type) VALUES(%s,%s,%s,%s,%s,%s,%s) '
           my_data2=(user_id,Name_student,Name_student,password1,Mobile_student,address,'student')
           my_data=(IDstudent,Name_student,Mobile_student,ClassId_student)
           cursor.execute(sqlquery,my_data)
           cursor.execute(sqlquery1,my_data2)
           con.commit()
           add_student.destroy()
           messagebox.showinfo('successful','user has beeen added successfully')
           
           
           
        def addteacher():
            IDteacher=teacherID_var2.get()
            NAMEteacher=teacherName_var.get()
            IDuser=userId_var.get()
            SUBJECT=subjectLabel_var.get()
            SUBJECTID=subjectIdLabel_var.get()
            CLASS=classTakenLabel_var.get()
            LOGINname=loginName_var.get()
            Password=password_var.get()
            MOBILEno=mobile_var.get()
            Address=address_var.get()
            
            #connecting database and python
            con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
            cursor=con.cursor()
            sqlquery1='INSERT INTO  teacher (teacher_ID,teacher_name,user_ID,subject,subject_id,class) VALUES(%s,%s,%s,%s,%s,%s) '
            my_data1=(IDteacher,NAMEteacher,IDuser,SUBJECT,SUBJECTID,CLASS)
            cursor.execute(sqlquery1,my_data1)
            if CLASS=='12A':
                classid=1
            else:
                classid=2
            sqlquery2='INSERT INTO  class (class_ID,teacher_ID,class,teacher_name) VALUES(%s,%s,%s,%s) '
            my_data2=(classid,IDteacher,CLASS,NAMEteacher)
            cursor.execute(sqlquery2,my_data2)
            
            sqlquery3='INSERT INTO user(user_ID,name,login_name,password,mb_no,address,user_type) values(%s,%s,%s,%s,%s,%s,%s)'
            my_data3=(IDuser,NAMEteacher,LOGINname,Password,MOBILEno,Address,'teacher')
            cursor.execute(sqlquery3,my_data3)

            con.commit()
            add_teacher.destroy()
            messagebox.showinfo('Successful','Teacher  has beeen added successfully!')
           
           
     
                
        Value_selected=Combotch_Choosen.get()
        if Value_selected==' Student ':
            add_user.destroy()
            add_student=Tk()
            add_student.title('ADD STUDENT')
            add_student.geometry('750x500')
            add_student.config(bg='maroon')
            add_student.resizable(False, False)
            
        
                
            #creating labels and entry boxes for admin to add details of students
            
            #creating label and entry box for student id
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=1,column=1)
            studentIDLabel=Label(add_student,text='STUDENT ID',bg='maroon',fg='yellow').grid(row=3,column=3,sticky=W)
            studentID_var2=StringVar(add_student)
            AddstudentID=Entry(add_student,textvariable=studentID_var2).grid(row=3,column=5)
            
            #creating label and entry box for student name
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=4,column=1)
            studentNameLabel=Label(add_student,text='STUDENT NAME',bg='maroon',fg='yellow').grid(row=5,column=3,sticky=W)
            studentName_var=StringVar(add_student)
            AddstudentName=Entry(add_student,textvariable=studentName_var).grid(row=5,column=5)
            
             #creating label and entry box for student mobile number
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=6,column=1)
            studentMobileLabel=Label(add_student,text='STUDENT MOBILE NUMBER',bg='maroon',fg='yellow').grid(row=7,column=3,sticky=W)
            studentMobile_var=StringVar(add_student)
            AddstudentMobile=Entry(add_student,textvariable=studentMobile_var).grid(row=7,column=5)
            
             #creating label and entry box for student class
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=8,column=1)
            studentClassLabel=Label(add_student,text='STUDENT CLASS ID (1/2)',bg='maroon',fg='yellow').grid(row=9,column=3,sticky=W)
            studentClassLabel_var=StringVar(add_student)
            AddstudentClass=Entry(add_student,textvariable=studentClassLabel_var).grid(row=9,column=5)
            
            #creating label and entry box for student password
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=10,column=1)
            passLabel=Label(add_student,text='STUDENT PASSWORD',bg='maroon',fg='yellow').grid(row=11,column=3,sticky=W)
            pass_var=StringVar(add_student)
            AddstudentClass=Entry(add_student,textvariable=pass_var).grid(row=11,column=5)
            
            #creating label and entry box for user ID
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=12,column=1)
            USER_idLabel=Label(add_student,text='USER ID',bg='maroon',fg='yellow').grid(row=13,column=3,sticky=W)
            USER_id_var=StringVar(add_student)
            AddstudentClass=Entry(add_student,textvariable=USER_id_var).grid(row=13,column=5)
            
            #creating label and entry box for ADDRESS
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=14,column=1)
            addressLabel=Label(add_student,text='ADDRESS',bg='maroon',fg='yellow').grid(row=15,column=3,sticky=W)
            address_var=StringVar(add_student)
            AddstudentClass=Entry(add_student,textvariable=address_var).grid(row=15,column=5)
            
            
            #creating buttons to add 
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=16,column=1)
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=17,column=1)
            btn1=Button(add_student,text='Add',command=addstudent,bg='white',width=30,height=1).grid(row=18,column=4)
            lblForSpace=Label(add_student,text='            ',bg='maroon').grid(row=19,column=1)
            
        
       
        else:
            add_user.destroy()
            add_teacher=Tk()
            add_teacher.title('ADD TEACHER')
            add_teacher.geometry('700x700')
            add_teacher.config(bg='maroon')
            add_teacher.resizable(False, False)
            def clear():
               AddteacherID.delete(0,'end')
               AddteacherName.delete(0,'end')
               AdduserId.delete(0,'end')
               Addsubject.delete(0,'end')
               Addclass.delete(0,'end')
               AddsubjectID.delete(0,'end')
               AddloginNamE.delete(0,'end')
               Addpassword.delete(0,'end')
               Addmobile.delete(0,'end')
               Addaddress.delete(0,'end')
            
            
            #creating labels and entry boxes for admin to add details of teachers
            
            #creating label and entry box for student id
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=1,column=1)
            teacherIDLabel=Label(add_teacher,text='TEACHER ID',bg='maroon',fg='yellow').grid(row=3,column=3,sticky=W)
            teacherID_var2=StringVar(add_teacher)
            AddteacherID=Entry(add_teacher,textvariable=teacherID_var2)
            AddteacherID.grid(row=3,column=5)
            
            #creating label and entry box for teacher id name
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=4,column=1)
            teacherNameLabel=Label(add_teacher,text='TEACHER NAME',bg='maroon',fg='yellow').grid(row=5,column=3,sticky=W)
            teacherName_var=StringVar(add_teacher)
            AddteacherName=Entry(add_teacher,textvariable=teacherName_var)
            AddteacherName.grid(row=5,column=5)
            
             #creating label and entry box for student user id
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=6,column=1)
            useridLabel=Label(add_teacher,text='USER ID',bg='maroon',fg='yellow').grid(row=7,column=3,sticky=W)
            userId_var=StringVar(add_teacher)
            AdduserId=Entry(add_teacher,textvariable=userId_var)
            AdduserId.grid(row=7,column=5)
            
             #creating label and entry box for student class
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=8,column=1)
            subjectLabel=Label(add_teacher,text='SUBJECT',bg='maroon',fg='yellow').grid(row=9,column=3,sticky=W)
            subjectLabel_var=StringVar(add_teacher)
            Addsubject=Entry(add_teacher,textvariable=subjectLabel_var)
            Addsubject.grid(row=9,column=5)
            
            #creating label and entry box for SUBJECT ID
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=10,column=1)
            subjectIdLabel=Label(add_teacher,text='SUBJECT ID',bg='maroon',fg='yellow').grid(row=11,column=3,sticky=W)
            subjectIdLabel_var=StringVar(add_teacher)
            AddsubjectID=Entry(add_teacher,textvariable=subjectIdLabel_var)
            AddsubjectID.grid(row=11,column=5)
            
            #creating label for CLASS TAKEN BY THE TEACHER
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=12,column=1)
            classTakenLabel=Label(add_teacher,text='CLASS TAKEN',bg='maroon',fg='yellow').grid(row=13,column=3,sticky=W)
            classTakenLabel_var=StringVar(add_teacher)
            Addclass=Entry(add_teacher,textvariable=classTakenLabel_var)
            Addclass.grid(row=13,column=5)
            
            #creating label and entry box for login name
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=14,column=1)
            loginNamELabel=Label(add_teacher,text='LOGIN NAME',bg='maroon',fg='yellow').grid(row=15,column=3,sticky=W)
            loginName_var=StringVar(add_teacher)
            AddloginNamE=Entry(add_teacher,textvariable=loginName_var)
            AddloginNamE.grid(row=15,column=5)

            #creating label and entry box for password
  
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=16,column=1)
            passworDLabel=Label(add_teacher,text='PASSWORD',bg='maroon',fg='yellow').grid(row=17,column=3,sticky=W)
            password_var=StringVar(add_teacher)
            Addpassword=Entry(add_teacher,textvariable=password_var)
            Addpassword.grid(row=17,column=5)
            
            #creating label and entry box for mobile number

            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=18,column=1)
            mobileLabel=Label(add_teacher,text='MOBILE NUMMBER',bg='maroon',fg='yellow').grid(row=19,column=3,sticky=W)
            mobile_var=StringVar(add_teacher)
            Addmobile=Entry(add_teacher,textvariable=mobile_var)
            Addmobile.grid(row=19,column=5)
            
            #creating label and entry box for address

            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=20,column=1)
            addressLabel=Label(add_teacher,text=' ADDRESS',bg='maroon',fg='yellow').grid(row=21,column=3,sticky=W)
            address_var=StringVar(add_teacher)
            Addaddress=Entry(add_teacher,textvariable=address_var)
            Addaddress.grid(row=21,column=5)
            
            #creating buttons to add and clear to delete entries entered in entry box
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=22,column=1)
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=23,column=1)
            btn1=Button(add_teacher,text='Add',command=addteacher,bg='white',width=30,height=1).grid(row=24,column=4)
            lblForSpace=Label(add_teacher,text='            ',bg='maroon').grid(row=25,column=1)
            btn2=Button(add_teacher,text='Clear details',command=clear ,bg='white',width=30,height=1).grid(row=26,column=4)
            
            
            #messagebox.showinfo('successful','user has beeen added successfully')  
            
            
            
            
        
    
    #creating drop down box for type of user to choose
    Combotch_Choosen =ttk.Combobox(add_user, width = 27)
    Combotch_Choosen.grid(row=7,column = 4) 

    
    # Adding combobox drop down list
    
    Combotch_Choosen['values'] = (" Student ","Teacher")
    Combotch_Choosen.current()
    
    
    #binding the combobox
    Combotch_Choosen.bind('<<ComboboxSelected>>',choosing_type)
    
    
    add_user.mainloop()

########################################################################################

#creating teachers window
def teacher_window():
    
    #creating teacher form
    frm_login.destroy()
    
    
    
    def add_marks12A():
        frm_teacher=Tk()
        frm_teacher.title('12 A')
        frm_teacher.geometry('700x500')
        frm_teacher.config(bg='orange')
        frm_teacher.resizable(False, False)
        
         #creating labels and entry boxes for admin to add details of students
            
        #creating label and entry box for student id
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=1,column=1)
        studentIDLabel=Label(frm_teacher,text='STUDENT ID',bg='orange',fg='black').grid(row=3,column=3,sticky=W)
        studentID_var2=StringVar(frm_teacher)
        AddstudentID=Entry(frm_teacher,textvariable=studentID_var2)
        AddstudentID.grid(row=3,column=5,sticky=W)
        
        #creating label and entry box for maths marks
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=4,column=1)
        marksMathsLabel=Label(frm_teacher,text='MATHS MARKS',bg='orange',fg='black').grid(row=5,column=3,sticky=W)
        marksMaths_var=StringVar(frm_teacher)
        Addmaths=Entry(frm_teacher,textvariable=marksMaths_var)
        Addmaths.grid(row=5,column=5,sticky=W)
        
        #creating label and entry box for english marks
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=6,column=1)
        marksEnglishLabel=Label(frm_teacher,text='ENGLISH MARKS',bg='orange',fg='black').grid(row=7,column=3,sticky=W)
        marksEnglish_var2=StringVar(frm_teacher)
        Addenglish=Entry(frm_teacher,textvariable=marksEnglish_var2)
        Addenglish.grid(row=7,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=8,column=4)
        
        #creating label and entry box for computer marks
        marksComputerLabel=Label(frm_teacher,text='COMPUTER SCIENCE MARKS',bg='orange',fg='black').grid(row=9,column=3,sticky=W)
        marksComputer_var2=StringVar(frm_teacher)
        Addcomputer=Entry(frm_teacher,textvariable=marksComputer_var2)
        Addcomputer.grid(row=9,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=10,column=4)
        
        #creating label and entry box for physics marks
        marksPHYSICSLabel=Label(frm_teacher,text='PHYSICS MARKS',bg='orange',fg='black').grid(row=11,column=3,sticky=W)
        marksPHYSICS_var2=StringVar(frm_teacher)
        Addphysics=Entry(frm_teacher,textvariable=marksPHYSICS_var2)
        Addphysics.grid(row=11,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=12,column=4)
        
        #creating label and entry box for chemistry marks
        marksCHEMISTRYLabel=Label(frm_teacher,text='CHEMISTRY MARKS',bg='orange',fg='black').grid(row=13,column=3,sticky=W)
        marksCHEMISTRY_var2=StringVar(frm_teacher)
        Addchemistry=Entry(frm_teacher,textvariable=marksCHEMISTRY_var2)
        Addchemistry.grid(row=13,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=14,column=4)
        
        #creating label and entry box for total marks of exam
        marksTOTALLabel=Label(frm_teacher,text='TOTAL MARKS',bg='orange',fg='black').grid(row=15,column=3,sticky=W)
        marksTOTALL_var2=StringVar(frm_teacher)
        Addtotal=Entry(frm_teacher,textvariable=marksTOTALL_var2)
        Addtotal.grid(row=15,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=16,column=4)
        
        #btn1=Button(frm_teacher,text='ADD',command=add,bg='white',width=30,height=1).grid(row=15,column=5)
        
        
        def add():
            #getting the value inserted in the entr box
            id_student=studentID_var2.get()
            math_mark=marksMaths_var.get()
            english_mark=marksEnglish_var2.get()
            computer_mark=marksComputer_var2.get()
            physics_mark=marksPHYSICS_var2.get()
            chemistry_mark=marksCHEMISTRY_var2.get()
            total_mark=marksTOTALL_var2.get()
            
            #connecting to mysql through python
            con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
            cursor=con.cursor()
            sqlquery='INSERT INTO  marks (student_ID, MATHS, ENGLISH, COMPUTERSCIENCE, PHYSICS, CHEMISTRY, marks_ttl) VALUES(%s,%s,%s,%s,%s,%s,%s) '
            my_data=(id_student,math_mark,english_mark,computer_mark,physics_mark,chemistry_mark,total_mark)
            cursor.execute(sqlquery,my_data)
            con.commit()
            
            AddstudentID.delete(0,'end')
            Addmaths.delete(0,'end')
            Addenglish.delete(0,'end')
            Addcomputer.delete(0,'end')
            Addphysics.delete(0,'end')
            Addchemistry.delete(0,'end')
            Addtotal.delete(0,'end')
            
            messagebox.showinfo('successful','marks has beeen added successfully')
            
        btn1=Button(frm_teacher,text='ADD',command=add,bg='white',width=30,height=1).grid(row=17,column=5)
    def add_marks12B():                                                                                  
        frm_teacher=Tk()
        frm_teacher.title('12 B')
        frm_teacher.geometry('700x500')
        frm_teacher.config(bg='orange')
        frm_teacher.resizable(False, False)
        
         #creating labels and entry boxes for admin to add details of students
            
        #creating label and entry box for student id
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=1,column=1)
        studentIDLabel=Label(frm_teacher,text='STUDENT ID',bg='orange',fg='black').grid(row=3,column=3,sticky=W)
        studentID_var2=StringVar(frm_teacher)
        AddstudentID=Entry(frm_teacher,textvariable=studentID_var2)
        AddstudentID.grid(row=3,column=5,sticky=W)
        
        #creating label and entry box for maths marks
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=4,column=1)
        marksMathsLabel=Label(frm_teacher,text='MATHS MARKS',bg='orange',fg='black').grid(row=5,column=3,sticky=W)
        marksMaths_var=StringVar(frm_teacher)
        Addmaths=Entry(frm_teacher,textvariable=marksMaths_var)
        Addmaths.grid(row=5,column=5,sticky=W)
        
        #creating label and entry box for english marks
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=6,column=1)
        marksEnglishLabel=Label(frm_teacher,text='ENGLISH MARKS',bg='orange',fg='black').grid(row=7,column=3,sticky=W)
        marksEnglish_var2=StringVar(frm_teacher)
        Addenglish=Entry(frm_teacher,textvariable=marksEnglish_var2)
        Addenglish.grid(row=7,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=8,column=4)
        
        #creating label and entry box for computer marks
        marksComputerLabel=Label(frm_teacher,text='COMPUTER SCIENCE MARKS',bg='orange',fg='black').grid(row=9,column=3,sticky=W)
        marksComputer_var2=StringVar(frm_teacher)
        Addcomputer=Entry(frm_teacher,textvariable=marksComputer_var2)
        Addcomputer.grid(row=9,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=10,column=4)
        
        #creating label and entry box for physics marks
        marksPHYSICSLabel=Label(frm_teacher,text='PHYSICS MARKS',bg='orange',fg='black').grid(row=11,column=3,sticky=W)
        marksPHYSICS_var2=StringVar(frm_teacher)
        Addphysics=Entry(frm_teacher,textvariable=marksPHYSICS_var2)
        Addphysics.grid(row=11,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=12,column=4)
        
        #creating label and entry box for chemistry marks
        marksCHEMISTRYLabel=Label(frm_teacher,text='CHEMISTRY MARKS',bg='orange',fg='black').grid(row=13,column=3,sticky=W)
        marksCHEMISTRY_var2=StringVar(frm_teacher)
        Addchemistry=Entry(frm_teacher,textvariable=marksCHEMISTRY_var2)
        Addchemistry.grid(row=13,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=14,column=4)
        
        #creating label and entry box for total marks of exam
        marksTOTALLabel=Label(frm_teacher,text='TOTAL MARKS',bg='orange',fg='black').grid(row=15,column=3,sticky=W)
        marksTOTALL_var2=StringVar(frm_teacher)
        Addtotal=Entry(frm_teacher,textvariable=marksTOTALL_var2)
        Addtotal.grid(row=15,column=5,sticky=W)
        lblForSpace=Label(frm_teacher,text='            ',bg='orange').grid(row=16,column=4)
        
        #btn1=Button(frm_teacher,text='ADD',command=add,bg='white',width=30,height=1).grid(row=15,column=5)
        
        
        def add():
            #getting the value inserted in the entr box
            id_student=studentID_var2.get()
            math_mark=marksMaths_var.get()
            english_mark=marksEnglish_var2.get()
            computer_mark=marksComputer_var2.get()
            physics_mark=marksPHYSICS_var2.get()
            chemistry_mark=marksCHEMISTRY_var2.get()
            total_mark=marksTOTALL_var2.get()
            
            #connecting to mysql through python
            con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
            cursor=con.cursor()
            sqlquery='INSERT INTO  marks12B (student_ID, MATHS, ENGLISH, COMPUTERSCIENCE, PHYSICS, CHEMISTRY, marks_ttl) VALUES(%s,%s,%s,%s,%s,%s,%s) '
            my_data=(id_student,math_mark,english_mark,computer_mark,physics_mark,chemistry_mark,total_mark)
            cursor.execute(sqlquery,my_data)
            con.commit()
            
            AddstudentID.delete(0,'end')
            Addmaths.delete(0,'end')
            Addenglish.delete(0,'end')
            Addcomputer.delete(0,'end')
            Addphysics.delete(0,'end')
            Addchemistry.delete(0,'end')
            Addtotal.delete(0,'end')
            
            messagebox.showinfo('successful','marks has beeen added successfully')
            
        btn1=Button(frm_teacher,text='ADD',command=add,bg='white',width=30,height=1).grid(row=17,column=5) 
    
     
    strPassword=pass_var.get()
    #connecting to database mysql
    con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
    cursor=con.cursor()
    
    sql1="select * from user,teacher where teacher.user_ID=user.user_ID AND password=%s"
    password1=(strPassword,)
    cursor.execute(sql1,password1)
    rs=cursor.fetchall()
    if rs[0][12]=='12A':
        add_marks12A()
    elif rs[0][12]=='12B':
        add_marks12B()
    
    
############################################################################################
        
def student_window():
    frm_login.destroy()
    
    strUSerName=txt_var.get()
    
    #connecting to database mysql
    con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
    cursor=con.cursor()
    
    sql="select student_name from student "
    #name=(strUSerName,)
    cursor.execute(sql)
    rs=cursor.fetchall()
    if (strUSerName,) in rs:
        sql="select class_ID from student where student_name=%s"
        name=(strUSerName,)
        cursor.execute(sql,name)
        rs=cursor.fetchall()
        
        if rs==[(1,)]:
            student_window=Tk()
            student_window.title('STUDENT WINDOW')
            student_window.geometry('500x600')
            student_window.config(bg='#00ace6')
            student_window.resizable(False, False)
            
            
            lbl=Label(student_window,text='     ',bg='#00ace6').grid(row=0,column=0)
            Left_frame=LabelFrame(student_window,text='STUDENT DETAILS',bg='#00ace6',fg='black',width=900,height=100)
            Left_frame.grid(row=0,column=2)
            lbl=Label(student_window,text='     ',bg='#00ace6').grid(row=2,column=0)

            Right_frame=LabelFrame(student_window,text='RESULT',bg='#00ace6',fg='black',width=900,height=600)
            Right_frame.grid(row=4,column=2)
            #creating lbl for maths
            lblForSpace6=Label(Left_frame,text='            ',bg='#00ace6').grid(row=0,column=0)
            lblForSpace=Label(Left_frame,text='STUDENT NAME',bg='black',fg='#00ace6').grid(row=1,column=2,sticky=W)
            name_var=StringVar(Left_frame)
            txtTeacherId=Entry(Left_frame,textvariable=name_var).grid(row=1,column=5,sticky=W)
            lblForSpace=Label(Left_frame,text='  ',bg='#00ace6').grid(row=1,column=3,sticky=W)
            
            lblForSpace=Label(Left_frame,text='CLASS',bg='black',fg='#00ace6').grid(row=2,column=2,sticky=W)
            class_var=StringVar(Left_frame)
            txtTeacherId=Entry(Left_frame,textvariable=class_var).grid(row=2,column=5,sticky=W)
            lblForSpace6=Label(Left_frame,text='            ',bg='#00ace6').grid(row=3,column=2)
            lblForSpace=Label(Left_frame,text='  ',bg='#00ace6').grid(row=2,column=3,sticky=W)
            
            
            
            subjectLabel=Label(Right_frame,text='MATHS MARKS ',bg='black',fg='#00ace6').grid(row=4,column=3,sticky=W)
            
            #displaying the maths
            math_var=StringVar(Right_frame)
            txtTeacherId=Entry(Right_frame,textvariable=math_var).grid(row=4,column=5,sticky=W)
            

            
            #displaying english
            lblForSpace=Label(Right_frame,text='            ',bg='#00ace6').grid(row=6,column=4)
            addressLabel=Label(Right_frame,text='ENGLISH MARKS',bg='black',fg='#00ace6').grid(row=7,column=3,sticky=W)
            english_var=StringVar(Right_frame)
            AddTeacherId=Entry(Right_frame,textvariable=english_var).grid(row=7,column=5,sticky=W)
            
            
            #displaying computer science number
            lblForSpace1=Label(Right_frame,text='  ',bg='#00ace6').grid(row=8,column=4)
            mobileLabel=Label(Right_frame,text='COMPUTER SCIENCE MARKS',bg='black',fg='#00ace6').grid(row=9,column=3,sticky=W)
            cs_var=StringVar(Right_frame)
            mobTeacherId=Entry(Right_frame,textvariable=cs_var).grid(row=9,column=5,sticky=W)
            #lblForSpace=Label(Right_frame,text='            ',bg='black').grid(row=10,column=2)
            
            
            #diaplaying physics
            lblForSpace1=Label(Right_frame,text='  ',bg='#00ace6').grid(row=10,column=4)
            classTakenLabel=Label(Right_frame,text='PHYSICS MARKS',bg='black',fg='#00ace6').grid(row=11,column=3,sticky=W)
            physic_var=StringVar(Right_frame)
            classTakenTeacherEntry=Entry(Right_frame,textvariable=physic_var).grid(row=11,column=5,sticky=W)
            
            
            #diaplaying chemistry
            lblForSpace1=Label(Right_frame,text='  ',bg='#00ace6').grid(row=12,column=4)
            classTakenLabel=Label(Right_frame,text='CHEMISTRY MARKS',bg='black',fg='#00ace6').grid(row=13,column=3,sticky=W)
            chemistry_var=StringVar(Right_frame)
            classTakenTeacherEntry=Entry(Right_frame,textvariable=chemistry_var).grid(row=13,column=5,sticky=W)
            
            #diaplaying total marks
            lblForSpace1=Label(Right_frame,text='  ',bg='#00ace6').grid(row=15,column=4)
            ttlLabel=Label(Right_frame,text='TOTAL MARKS',bg='black',fg='#00ace6').grid(row=16,column=3,sticky=W)
            ttl_var=StringVar(Right_frame)
            ttlEntry=Entry(Right_frame,textvariable=ttl_var).grid(row=16,column=5,sticky=W)
            
            #diaplaying percentage
            lblForSpace1=Label(Right_frame,text='  ',bg='#00ace6').grid(row=17,column=4)
            perLabel=Label(Right_frame,text='PERCENTAGE',bg='black',fg='#00ace6').grid(row=18,column=3,sticky=W)
            per_var=StringVar(Right_frame)
            perEntry=Entry(Right_frame,textvariable=per_var).grid(row=18,column=5,sticky=W)
            
            
            con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
            cursor=con.cursor()
            sql='select student_ID from student where student_name=%s'
            name=(strUSerName,)
            cursor.execute(sql,name)
            rs1=cursor.fetchall()
            
        
            sqlquery='select  MATHS, ENGLISH, COMPUTERSCIENCE, PHYSICS, CHEMISTRY, marks_ttl from marks where student_ID=%s'
            name=(rs1[0][0],)
            cursor.execute(sqlquery,name)
            rs=cursor.fetchall()
            for i in rs:
                name_var.set(strUSerName.upper())
                class_var.set('12A')
                math_var.set(i[0])
                english_var.set(i[1])
                cs_var.set(i[2])
                physic_var.set(i[3])
                chemistry_var.set(i[4])
                total=i[0]+i[1]+i[2]+i[3]+i[4]
                ttl_var.set(total)
                sql='select marks_ttl from marks where student_ID=%s'
                name=(rs1[0][0],)
                cursor.execute(sql,name)
                rs=cursor.fetchall()
                percentage=(total/rs[0][0])*100
                
                per_var.set(percentage)
            
        else:
            student_window=Tk()
            student_window.title('STUDENT WINDOW')
            student_window.geometry('500x600')
            student_window.config(bg='#ff0066')
            student_window.resizable(False, False)
            
            
            lbl=Label(student_window,text='     ',bg='#ff0066').grid(row=0,column=0)
            Left_frame=LabelFrame(student_window,text='STUDENT DETAILS',bg='#ff0066',fg='black',width=900,height=100)
            Left_frame.grid(row=0,column=2)
            lbl=Label(student_window,text='     ',bg='#ff0066').grid(row=2,column=0)

            Right_frame=LabelFrame(student_window,text='RESULT',bg='#ff0066',fg='black',width=900,height=600)
            Right_frame.grid(row=4,column=2)
            #creating lbl for maths
            lblForSpace6=Label(Left_frame,text='            ',bg='#ff0066').grid(row=0,column=0)
            lblForSpace=Label(Left_frame,text='STUDENT NAME',bg='black',fg='pink').grid(row=1,column=2,sticky=W)
            name_var=StringVar(Left_frame)
            txtTeacherId=Entry(Left_frame,textvariable=name_var).grid(row=1,column=5,sticky=W)
            lblForSpace=Label(Left_frame,text='  ',bg='#ff0066').grid(row=1,column=3,sticky=W)
            
            lblForSpace=Label(Left_frame,text='CLASS',bg='black',fg='pink').grid(row=2,column=2,sticky=W)
            class_var=StringVar(Left_frame)
            txtTeacherId=Entry(Left_frame,textvariable=class_var).grid(row=2,column=5,sticky=W)
            lblForSpace6=Label(Left_frame,text='            ',bg='#ff0066').grid(row=3,column=2)
            lblForSpace=Label(Left_frame,text='  ',bg='#ff0066').grid(row=2,column=3,sticky=W)
            
            
            
            subjectLabel=Label(Right_frame,text='MATHS MARKS ',bg='black',fg='pink').grid(row=4,column=3,sticky=W)
            
            #displaying the maths
            math_var=StringVar(Right_frame)
            txtTeacherId=Entry(Right_frame,textvariable=math_var).grid(row=4,column=5,sticky=W)
            

            
            #displaying english
            lblForSpace=Label(Right_frame,text='            ',bg='#ff0066').grid(row=6,column=4)
            addressLabel=Label(Right_frame,text='ENGLISH MARKS',bg='black',fg='pink').grid(row=7,column=3,sticky=W)
            english_var=StringVar(Right_frame)
            AddTeacherId=Entry(Right_frame,textvariable=english_var).grid(row=7,column=5,sticky=W)
            
            
            #displaying computer science number
            lblForSpace1=Label(Right_frame,text='  ',bg='#ff0066').grid(row=8,column=4)
            mobileLabel=Label(Right_frame,text='COMPUTER SCIENCE MARKS',bg='black',fg='pink').grid(row=9,column=3,sticky=W)
            cs_var=StringVar(Right_frame)
            mobTeacherId=Entry(Right_frame,textvariable=cs_var).grid(row=9,column=5,sticky=W)
            #lblForSpace=Label(Right_frame,text='            ',bg='black').grid(row=10,column=2)
            
            
            #diaplaying physics
            lblForSpace1=Label(Right_frame,text='  ',bg='#ff0066').grid(row=10,column=4)
            classTakenLabel=Label(Right_frame,text='PHYSICS MARKS',bg='black',fg='pink').grid(row=11,column=3,sticky=W)
            physic_var=StringVar(Right_frame)
            classTakenTeacherEntry=Entry(Right_frame,textvariable=physic_var).grid(row=11,column=5,sticky=W)
            
            
            #diaplaying chemistry
            lblForSpace1=Label(Right_frame,text='  ',bg='#ff0066').grid(row=12,column=4)
            classTakenLabel=Label(Right_frame,text='CHEMISTRY MARKS',bg='black',fg='pink').grid(row=13,column=3,sticky=W)
            chemistry_var=StringVar(Right_frame)
            classTakenTeacherEntry=Entry(Right_frame,textvariable=chemistry_var).grid(row=13,column=5,sticky=W)
            
            #diaplaying total marks
            lblForSpace1=Label(Right_frame,text='  ',bg='#ff0066').grid(row=15,column=4)
            ttlLabel=Label(Right_frame,text='TOTAL MARKS',bg='black',fg='pink').grid(row=16,column=3,sticky=W)
            ttl_var=StringVar(Right_frame)
            ttlEntry=Entry(Right_frame,textvariable=ttl_var).grid(row=16,column=5,sticky=W)
            
            #diaplaying percentage
            lblForSpace1=Label(Right_frame,text='  ',bg='#ff0066').grid(row=17,column=4)
            perLabel=Label(Right_frame,text='PERCENTAGE',bg='black',fg='pink').grid(row=18,column=3,sticky=W)
            per_var=StringVar(Right_frame)
            perEntry=Entry(Right_frame,textvariable=per_var).grid(row=18,column=5,sticky=W)
            
            
            con=mysql.connector.connect(host='localhost',user='root',password='khushidiya1116',database='pyprgm')
            cursor=con.cursor()
            sql='select student_ID from student where student_name=%s'
            name=(strUSerName,)
            cursor.execute(sql,name)
            rs1=cursor.fetchall()
            
        
            sqlquery='select  MATHS, ENGLISH, COMPUTERSCIENCE, PHYSICS, CHEMISTRY, marks_ttl from marks12b where student_ID=%s'
            name=(rs1[0][0],)
            cursor.execute(sqlquery,name)
            rs=cursor.fetchall()
            for i in rs:
                name_var.set(strUSerName.upper())
                class_var.set('12B')
                math_var.set(i[0])
                english_var.set(i[1])
                cs_var.set(i[2])
                physic_var.set(i[3])
                chemistry_var.set(i[4])
                total=i[0]+i[1]+i[2]+i[3]+i[4]
                ttl_var.set(total)
                sql='select marks_ttl from marks12b where student_ID=%s'
                name=(rs1[0][0],)
                cursor.execute(sql,name)
                rs=cursor.fetchall()
                percentage=(total/rs[0][0])*100
                
                per_var.set(percentage)
            
    
    
    
############################################################################################
#creating the login form

#creating login name entery box and labels
lblUSerNme=Label(frm_login,text='Login Name',bg='olivedrab1',fg='olivedrab1').grid(row=0,column=0)
lblUSerNme=Label(frm_login,text='LOGIN NAME* ',bg='olivedrab1').grid(row=4,column=1)
txt_var=StringVar(frm_login)
txtUserName=Entry(frm_login,textvariable=txt_var).grid(row=4,column=3)

#creating password entry box and labels
pass_var=StringVar(frm_login)
lbl2=Label(frm_login,text='PASSWORD*   ',bg='olivedrab1').grid(row=5,column=1)
txtPassword=Entry(frm_login,textvariable=pass_var,show='*').grid(row=5,column=3)

#creating button for login and exit
lbl3=Label(frm_login,text='   ',bg='olivedrab1').grid(row=7,column=1)
btn1=Button(frm_login,text='Log In',command=login,bg='white',width=10,height=1).grid(row=9,column=1)
btn2=Button(frm_login,text='Exit',command=quit,bg='white',width=10,height=1).grid(row=9,column=3)
frm_login.mainloop()
