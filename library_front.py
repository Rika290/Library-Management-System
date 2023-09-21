import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.set_page_config(page_title="YOURLIBRARY",page_icon="https://e0.pxfuel.com/wallpapers/540/340/desktop-wallpaper-lot-of-books-in-library.jpg")
choice=st.sidebar.selectbox("Menu",("Home","Student Login","Admin Login"))
st.sidebar.image("https://photosfile.com/wp-content/uploads/2023/01/Study-DP-2.jpg")
st.sidebar.image("https://cdn.pixabay.com/photo/2016/02/16/21/07/books-1204029_640.jpg")
if choice=="Home":
    st.title("Library Management System")
    st.text("    HEY! WELCOME TO YOURLIBRARY 📚👩‍🎓👨‍🎓🤓")
    st.image('https://images.unsplash.com/photo-1481627834876-b7833e8f5570?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGlicmFyeXxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80')
    st.text("A reader lives a thousand lives before he dies.....")
    st.text("The man who never reads lives only one")
elif choice=="Student Login":
    st.image("https://img.freepik.com/premium-vector/college-university-library-study-place-students-professors-borrowing-reserving-books-online-access-scientific-publications-cartoon-vector-illustration_1284-71255.jpg")
    st.text("Hi there 😊 Please enter your UserID and Password.")
    if 'login' not in st.session_state:
        st.session_state['login']=False
    if(not st.session_state['login']):
        U=st.text_input("enter UserID:")
        P=st.text_input("enter Password:")
        btn=st.button("Login")
        if btn:
            mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="LMS")
            c=mydb.cursor()
            c.execute("select * from Users")
            for row in c:
                if(row[0]==U and row[1]==P):
                    st.session_state['login']=True
                    st.experimental_rerun()
                    break
            if(not st.session_state['login']):
                st.header("SORRY 😢. Incorrect ID or Password. Please try again later")
    if(st.session_state['login']):
        st.header("You logged in successfully 😁👍")
        ch1=st.selectbox("Choose",("🏠","View books📚","Issue books 📖📖"))
        if(ch1=="🏠"):
            st.image("https://cdn.pixabay.com/photo/2015/11/19/21/10/glasses-1052010_640.jpg")
        elif(ch1=="View books📚"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="LMS")
            c=mydb.cursor()
            c.execute("select * from Books")
            b=[]
            for i in c:
                b.append(i)
            df=pd.DataFrame(data=b,columns=c.column_names)
            st.dataframe(df)
        elif(ch1=="Issue books 📖📖"):
            B=st.text_input("Enter the book id")
            d=st.text_input("Enter your ID")
            btt=st.button("Issue")
            if btt:
                dt=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="LMS")
                c=mydb.cursor()
                c.execute("insert into Issue_book values(%s,%s,%s)",(dt,B,d))
                mydb.commit()
                st.header("Book issued successfully")
elif choice=="Admin Login":
    st.image("https://img.freepik.com/premium-vector/librarian-concept-library-staff-cataloguing-sorting-books-knowledge-education-idea-llibrary-bookshelves-guid-isolated-vector-illustration_613284-1665.jpg")
    st.text("Hello Admin 😎")
    ch2=st.selectbox("Select",("📚","View Books","Add Books"))
    if(ch2=="📚"):
        st.image("https://cdn.gtricks.com/2019/09/5-book-reading-android-apps-to-read-and-manage-books-for-free-1280x720.jpg")
    elif(ch2=="View Books"):
        db=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="LMS")
        c=db.cursor()
        c.execute("select * from Books")
        g=[]
        for t in c:
            g.append(t)
            de=pd.DataFrame(data=g,columns=c.column_names)
        st.dataframe(de)
    elif(ch2=="Add Books"):
        x=st.text_input("Enter the Book_ID")
        y=st.text_input("Enter the book name")
        z=st.text_input("Enter the author name")
        bti=st.button("Add")
        if bti:
            mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="LMS")
            c=mydb.cursor()
            c.execute("insert into Books values(%s,%s,%s)",(x,y,z))
            mydb.commit()
            st.header("Book added successfully")
    
            
                  
        
        
    
        
        
      
            

    

