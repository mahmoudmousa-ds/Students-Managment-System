import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import psycopg2
from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import psycopg2
import pandas
from tkinter import simpledialog
mech_dep = ["mech1", "mech2", "mech3", "mech4", "mech5"]
elec_dep = ["elec1", "elec2", "elec3", "elec4", "elec5"]
comm_dep = ["comm1", "comm2", "comm3", "comm4", "comm5"]
civ_dep = ["civil1", "civil2", "civil3", "civil4", "civil5"]


# Functionality Part
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    port="5432",
    user="postgres",
    # password=""
)

mycursor = con.cursor()


def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    newlist = []
    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)

    table = pd.DataFrame(newlist, columns=['Name','faculty_id','academic_year','degree_type','department',
                                 'course_name','midterm_mark','final_mark','total_mark','gpa','letter_grade'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')


def toplevel_data(title, button_text, command):
    global facultyidEntry,nameEntry,academic_yearEntry,degree_typeEntry,dep_entry,coursesEntry,screen,academic_year_var,degree_type_var,display_dep_subjects,department_var,list_subjects,faculty_id_var,courses_var
    screen = tk.Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)

    name_var = tk.StringVar()
    faculty_id_var = tk.StringVar()
    academic_year_var = tk.StringVar()
    degree_type_var = tk.StringVar()
    department_var = tk.StringVar()
    courses_var = tk.StringVar()

    def display_dep_subjects(event):
        selection = combo2.current()
        if selection == 0:
            list_subjects.delete(0, 'end')
            for each_item in range(len(elec_dep)):
                list_subjects.insert(tk.END, elec_dep[each_item])
        elif selection == 1:
            list_subjects.delete(0, 'end')
            for each_item in range(len(comm_dep)):
                list_subjects.insert(tk.END, comm_dep[each_item])
        elif selection == 2:
            list_subjects.delete(0, 'end')
            for each_item in range(len(mech_dep)):
                list_subjects.insert(tk.END, mech_dep[each_item])
        elif selection == 3:
            list_subjects.delete(0, 'end')
            for each_item in range(len(civ_dep)):
                list_subjects.insert(tk.END, civ_dep[each_item])

    nameLabel = tk.Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=tk.W)
    nameEntry = tk.Entry(screen, font=('roman', 15, 'bold'), width=50, textvariable=name_var)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    facultyidlabel = tk.Label(screen, text='Faculty ID', font=('times new roman', 20, 'bold'))
    facultyidlabel.grid(row=2, column=0, padx=30, pady=15, sticky=tk.W)
    facultyidEntry = tk.Entry(screen, font=('roman', 15, 'bold'), width=50, textvariable=faculty_id_var)
    facultyidEntry.grid(row=2, column=1, pady=15, padx=10)

    combo1 = ttk.Combobox(screen, state="readonly", values=["Pre-Master", "Master", "Phd"], width=50,
                          textvariable=degree_type_var)
    combo1.grid(row=8, column=1, pady=15, padx=10)
    label1 = tk.Label(screen, text="Degree Name", font=("Times New Roman", 17, "bold"))
    label1.grid(row=8, column=0, padx=30, pady=15, sticky=tk.W)


    combo2 = ttk.Combobox(screen, state="readonly",
                          values=["Electrical Engineering", "Communication Engineering", "Mechanical Engineering",
                                  "Civil Engineering"], width=50,textvariable=department_var)
    combo2.bind("<<ComboboxSelected>>", display_dep_subjects)
    combo2.grid(row=9, column=1, pady=15, padx=10)
    label2 = tk.Label(screen, text="Department", font=("Times New Roman", 17, "bold"))
    label2.grid(row=9, column=0, padx=30, pady=15, sticky=tk.W)

    combo3 = ttk.Combobox(screen, state="readonly", values=["2020", "2021", "2022", "2023", "2024"], width=50,
                          textvariable=academic_year_var)
    combo3.grid(row=10, column=1, pady=15, padx=10)
    label3 = tk.Label(screen, text="Academic Year", font=("Times New Roman", 17, "bold"))
    label3.grid(row=10, column=0, padx=30, pady=15, sticky=tk.W)

    label4 = tk.Label(screen, text="Courses", font=("Times New Roman", 17, "bold"))
    label4.grid(row=11,column=0, padx=30, pady=15, sticky=tk.W)
    yscrollbar = tk.Scrollbar(screen)

    list_subjects = tk.Listbox(screen, selectmode="multiple", yscrollcommand=yscrollbar.set,
    font=("Times New Roman", 23, "bold"))
    list_subjects.grid(row=11, column=1, pady=15, padx=10)
    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=12, columnspan=2, pady=15)

    if title == 'Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        facultyidEntry.insert(0, listdata[2])
        academic_yearEntry.insert(0, listdata[3])
        degree_typeEntry.insert(0, listdata[4])
        departmentEntry.insert(0, listdata[5])
        coursesEntry.insert(0, listdata[6])



#def update_data():
#    query = 'UPDATE students SET name=%s, faculty_id=%s, academic_year=%s, degree_type=%s, department=%s, courses=%s, date=%s, time=%s WHERE faculty_id=%s'
#    mycursor.execute(query, (name_var.get(), faculty_id_var.get(), academic_year_var.get(), degree_type_var.get(), department_var.get(), courses_var.get()))
#    con.commit()
#    messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully', parent=screen)
#    screen.destroy()
#    show_student()

#def update_data():
#    name_var = tk.StringVar()
#    faculty_id_var = tk.StringVar()
#    academic_year_var = tk.StringVar()
#    degree_type_var = tk.StringVar()
#    department_var = tk.StringVar()
#    courses_var = tk.StringVar()
#    if  nameEntry.get() == '' or facultyidEntry.get() == '' or academic_yearEntry.get() == '' or degree_typeEntry.get() == '' or departmentEntry.get() == '':
#        messagebox.showerror('Error', 'All fields are required', parent=screen)
#    else:
#        try:
#            student_name = nameEntry.get()
#            faculty_id = facultyidEntry.get()
#            academic_year = academic_yearEntry.get()
#            degree_type = degree_typeEntry.get()
#            department = departmentEntry.get()
#            courses = coursesEntry.get()
#
#            # Update student table
#            query = 'UPDATE students SET name=%s, faculty_id=%s, academic_year=%s, degree_type=%s, department=%s WHERE student_id=%s'
#            mycursor.execute(query, (student_name, faculty_id, academic_year, degree_type, department, student_id))
#
#            # Delete existing student_courses records for the student
#            delete_query = 'DELETE FROM student_courses WHERE student_id=%s'
#            mycursor.execute(delete_query, (student_id,))
#
#            # Insert student_courses records for the student and selected courses
#            selected_courses = list_subjects.curselection()
#            for course_index in selected_courses:
#                course_id = course_ids[course_index]
#                insert_query = 'INSERT INTO student_courses (student_id, course_id) VALUES (%s, %s)'
#                mycursor.execute(insert_query, (student_id, course_id))
#
#            con.commit()
#            messagebox.showinfo('Success', f'Student with ID {student_id} is modified successfully', parent=screen)
#            screen.destroy()
#            show_student()
#        except Exception as e:
#            messagebox.showerror('Error', f'Failed to update student: {str(e)}', parent=screen)

def show_student():
    query = '''
    SELECT  s.name, s.faculty_id, s.academic_year, s.degree_type, s.department,
           sc.course_name, sc.midterm_mark, sc.final_mark, sc.total_mark, sc.gpa, sc.letter_grade
    FROM students s
    LEFT JOIN student_courses sc ON s.faculty_id = sc.faculty_id
    '''
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def delete_student():
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    content_values = content.get('values')
    if not content_values:
        messagebox.showerror('Error', 'Please select a student to delete.')
        return
    content_id = str(content_values[1])
#    query = 'DELETE FROM students WHERE faculty_id = %s'
    query = 'DELETE FROM student_courses WHERE faculty_id = %s'

    mycursor.execute(query, (content_id,))
    con.commit()
    messagebox.showinfo('Success', f'Faculty ID {content_id} has been deleted successfully')
    show_student()


def search_data():
    query='select name,faculty_id,academic_year, degree_type, department from students where faculty_id=%s'
    mycursor.execute(query, (faculty_id_var.get(),))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def get_course_info(course_identifier):
    query = 'SELECT course_identifier, course_name FROM courses WHERE course_identifier = %s'
    mycursor.execute(query, (course_identifier,))
    result = mycursor.fetchone()
    if result:
        return result
    else:
        return None
        
        
#Function to calculate GPA
def calculate_grade(total_mark):
    if total_mark >= 95:
        return 4.00, 'A+'
    elif total_mark >= 90:
        return 4.00, 'A'
    elif total_mark >= 85:
        return 3.70, 'A-'
    elif total_mark >= 80:
        return 3.30, 'B+'
    elif total_mark >= 75:
        return 3.00, 'B'
    elif total_mark >= 70:
        return 2.70, 'B-'
    elif total_mark >= 65:
        return 2.30, 'C+'
    elif total_mark >= 60:
        return 2.00, 'C'
    elif total_mark >= 55:
        return 1.70, 'C-'
    elif total_mark >= 53:
        return 1.30, 'D+'
    elif total_mark >= 50:
        return 1.00, 'D'
    else:
        return 0.00, 'F'
        
        
def add_data():
    if nameEntry.get() == '' or faculty_id_var.get() == '' or academic_year_var.get() == '' or degree_type_var.get() == '' or department_var.get() == '' or len(list_subjects.curselection()) == 0:
        messagebox.showerror('Error', 'All fields are required', parent=screen)
    else:
        try:
            courses = [list_subjects.get(i) for i in list_subjects.curselection()]
            courses_str = ', '.join(courses)
            
            # Get the marks for each course
            marks = {}
            for course in courses:
                marks[course] = {}
                marks[course]['midterm_mark'] = simpledialog.askinteger('Enter Midterm Mark', f'Enter midterm mark for {course}')
                marks[course]['final_mark'] = simpledialog.askinteger('Enter Final Mark', f'Enter final mark for {course}')
            
            # Insert data into the students table
            query = 'INSERT INTO students (name, faculty_id, degree_type, department, academic_year) VALUES (%s, %s, %s, %s, %s) RETURNING faculty_id'
            mycursor.execute(query, (nameEntry.get(), faculty_id_var.get(), degree_type_var.get(), department_var.get(), academic_year_var.get()))
            faculty_id = mycursor.fetchone()[0]
            for course in courses:
                course_info = get_course_info(course)
                if course_info:
                    course_identifier, course_name = course_info
                    query = 'INSERT INTO student_courses (faculty_id, course_identifier, course_name, midterm_mark, final_mark, total_mark, GPA, letter_grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                    midterm_mark = marks[course]['midterm_mark']
                    final_mark = marks[course]['final_mark']
                    total_mark = midterm_mark + final_mark
                    gpa, letter_grade = calculate_grade(total_mark)
                    mycursor.execute(query, (faculty_id_var.get(), course_identifier, course_name, midterm_mark, final_mark, total_mark, gpa, letter_grade))


            con.commit()
            
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clear the form?', parent=screen)
            if result:
                nameEntry.delete(0, END)
                faculty_id_var.set('')
                academic_year_var.set('')
                degree_type_var.set('')
                department_var.set('')
                list_subjects.selection_clear(0, END)
            else:
                pass
        except psycopg2.IntegrityError:
            messagebox.showerror('Error', 'ID cannot be repeated', parent=screen)
            return
        query = '''
    SELECT  s.name, s.faculty_id, s.degree_type, s.department, s.academic_year,
           sc.course_name, sc.midterm_mark, sc.final_mark, sc.total_mark, sc.gpa, sc.letter_grade
    FROM students s
    INNER JOIN student_courses sc ON s.faculty_id = sc.faculty_id
    '''
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=psycopg2.connect(
            host="localhost",
            database="postgres",
            port="5432",
            user="postgres",
#            password=""
        )
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query='create schema if not exists studentmanagementsystem;'
            mycursor.execute(query)
            query='set search_path to studentmanagementsystem;'
            mycursor.execute(query)
            query='create table if not exists students(id Serial primary key, name varchar(30),facluty_id varchar(15),academic_year varchar(30),degree_type varchar(100),department varchar(20),courses varchar(20),date varchar(50), time varchar(50));'
            mycursor.execute(query)

        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''


def slider():
    global count, text
    if count>=len(s):
        count=0
        text=''
        sliderLabel.config(text=text)
    else:
        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
    sliderLabel.after(300,slider)




def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)



#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Student Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Shoubra Faculty Of Engineerin Registery System' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Name','faculty_id','academic_year','degree_type','department',
                                 'course_name','midterm_mark','final_mark','total_mark','gpa','letter_grade'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(expand=1,fill=BOTH)

studentTable.heading('Name', text='Name')
studentTable.heading('faculty_id', text='Faculty ID')
studentTable.heading('academic_year', text='Academic Year')
studentTable.heading('degree_type', text='Degree Type')
studentTable.heading('department', text='Department')
studentTable.heading('course_name', text='Course Name')
studentTable.heading('midterm_mark', text='Midterm Mark')
studentTable.heading('final_mark', text='Final Mark')
studentTable.heading('total_mark', text='Total Mark')
studentTable.heading('gpa', text='GPA')
studentTable.heading('letter_grade', text='Letter Grade')

studentTable.column('Name', width=200, anchor=CENTER)
studentTable.column('faculty_id', width=200, anchor=CENTER)
studentTable.column('academic_year', width=300, anchor=CENTER)
studentTable.column('degree_type', width=300, anchor=CENTER)
studentTable.column('department', width=100, anchor=CENTER)
studentTable.column('course_name', width=200, anchor=CENTER)
studentTable.column('midterm_mark', width=100, anchor=CENTER)
studentTable.column('final_mark', width=100, anchor=CENTER)
studentTable.column('total_mark', width=100, anchor=CENTER)
studentTable.column('gpa', width=100, anchor=CENTER)
studentTable.column('letter_grade', width=100, anchor=CENTER)
style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

studentTable.config(show='headings')

root.mainloop()

