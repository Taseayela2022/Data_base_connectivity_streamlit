# Follow more on TTeach channel on youtube
##I am Ethiopian <<Tessema Ayele>> Data scientist at JU/WCU
import streamlit as st
import pandas as pd 
#Db management
import sqlite3
conn=sqlite3.connect('data.db')
c=conn.cursor()


def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username text, password text)') 


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES(?,?)',(username,password)) 
    
conn.commit()

def login_user(username,password):
  c.execute('SELECT * from userstable WHERE username=? AND  password=?',( username, password))
  data=c.fetchall()
  return data

def view_all_users():
  c.execute('SELECT * from userstable')
  data=c.fetchall()
  return data





def main():
    " ""Strimlit Login App"" "

    st.title("Online Login App")

    Menu=["Home","Login","Signup"]
    choice=st.sidebar.selectbox("Menu", Menu)

    if choice=="Home":
       st.subheader("Home")



    elif choice=="Login":
    	st.subheader("Login")

    	username=st.sidebar.text_input("user Name")
    	password=st.sidebar.text_input("password",type='password')

    
       
    if st.sidebar.checkbox("Login"):
        	#if password=='12345':
         create_usertable()
         result=login_user(username,password)
         if result:

            st.success("Logged in as{}".format(username))
            
    task=st.selectbox("Task",["Add post","Data_Scientist","Profile"]) 
            
    if task=="Add post":
            	  st.subheader("Add your posts")
    elif task=="Data_Scientist":
            	st.subheader("You are Data_Scientist")
    elif task=="Profile":
            	st.subheader("User profiles ")
            	user_result=view_all_users()
            	clean_db=pd.DataFrame(user_result,columns=["username","password"])
            	st.dataframe(clean_db)
    else:
        st.warning("Invalid username/password")
    
    if choice=="Signup":
    	st.subheader("Signup")

    new_user=st.text_input("username")
    new_password=st.text_input("password")

    
    if st.button("Signup"):
        	create_usertable()
        	add_userdata(new_user,new_password)

    
        	st.write("You have sucessfully created the account")
        	st.info("Go to Login Page")

    if st.button("view"):
            view_all_users(username,password)



if __name__=='__main__':
    main() 
