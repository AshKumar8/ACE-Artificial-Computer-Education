from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser 

import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import MinMaxScaler
from math import *
from sklearn.ensemble import RandomForestRegressor


root = Tk()
root.title('ACE-Artificial Computer Education')
root.iconbitmap('C:/Users/ashwi/OneDrive/Desktop/logo.ico') 
root["bg"] = "#cfebfd"

#WELCOME TEXT MESSAGE
welcome_Label = Label(root, text = "Welcome to The CODING Section!", font = ('Poppins Black',30), bg = 'white', fg = 'dark blue', padx = 400, pady = 25)
welcome_Label.pack()

#SPACE PADDING 1
space_Label = Label(root, pady = 2, bg = '#cfebfd')
space_Label.pack()

def classroom():
	messagebox.showinfo("Coding","Here you find all the courses related to Coding\n\nHave fun learning!")

#create Classroom Button
classroom_Button = Button(root, text = "Classroom",bg= "#ffaf7a", font = ('Poppins Medium',20), padx = 75, pady = 10, command = classroom)
classroom_Button.pack()

#SPACE PADDING 2
space_Label = Label(root, pady = 2, bg = '#cfebfd')
space_Label.pack()

#SCHEDULE
def open_schedule():
	global schedule_img
	top = Toplevel()
	top.title('Weekly Schedule')
	top.iconbitmap('C:/Users/ashwi/OneDrive/Desktop/logo.ico')
	schedule_img = ImageTk.PhotoImage(Image.open("ACE-Schedule.png"))
	schedule_label = Label(top, image= schedule_img).pack()
	space_Label = Label(top, pady = 1)
	space_Label.pack()
	schedule_exit_button = Button(top, text = "Exit", command = top.destroy, padx = 7, bg = '#FF0000').pack()
	space_Label = Label(top, pady = 1)
	space_Label.pack()


#create schedule Button
schedule_Button = Button(root, text = "Schedule",bg= "#ff9d5c", font = ('Poppins Medium',20), padx = 84, pady = 10, command = open_schedule)
schedule_Button.pack()

#SPACE PADDING 3
space_Label = Label(root, pady = 2, bg = '#cfebfd')
space_Label.pack()

#content
def open_content():
	global content_img
	top = Toplevel()
	top.title('Contents')
	top.iconbitmap('C:/Users/ashwi/OneDrive/Desktop/logo.ico')
	content_img = ImageTk.PhotoImage(Image.open("contents.png"))
	content_label = Label(top, image= content_img).pack()
	space_Label = Label(top, pady = 1)
	space_Label.pack()
	content_exit_button = Button(top, text = "Exit", command = top.destroy, padx = 7, bg = '#FF0000').pack()
	space_Label = Label(top, pady = 1)
	space_Label.pack()


#create content Button
content_Button = Button(root, text = "Contents", bg= "#ff8b3d", font = ('Poppins Medium',20), padx = 84, pady = 10, command = open_content)
content_Button.pack()

#SPACE PADDING 3
space_Label = Label(root, pady = 2, bg = '#cfebfd')
space_Label.pack()

#PROGRESS WINDOW
def open():

	global graph
	progress_level = Toplevel()
	progress_level.title('Progress')
	progress_level.iconbitmap('C:/Users/ashwi/OneDrive/Desktop/logo.ico') 
	progress_level.geometry("300x300")

	progress_level["bg"] = "#feeb75"

	space_Label = Label(progress_level, pady = 3, bg = "#feeb75")
	space_Label.pack()


	def graph1():
		ace_path = 'C:/Users/ashwi/OneDrive/Desktop/ace3.csv'
		ace_df = pd.read_csv(ace_path) 
		#ace_df = df.astype(float)

		X = ace_df[['Study','Concentration','Attendance']]
		y = ace_df[['Score']]

		x = ace_df['Study']
		y = ace_df['Score']

		plt.plot(x, y, 'o', color='black')
		plt.annotate("Week 4", (9.2,21))
		plt.annotate("Week 8", (8.5,24.5))
		plt.annotate("Week 1", (10.3,28.7))
		plt.annotate("Week 5", (11.2,31.5))
		plt.annotate("Week 11", (12.3,34.3))
		plt.annotate("Week 2", (13.7,33.6))
		plt.annotate("Week 7", (14.2,38.6))
		plt.annotate("Week 10", (15.2,40.6))
		plt.annotate("Week 9", (16.2,42.8))
		plt.annotate("Week 6", (18,43))
		plt.annotate("Week 3", (17.2,47.4))
		plt.annotate("Week 12", (18.6,48.3))
		plt.title('Study vs Score')
		plt.xlabel('Study')
		plt.ylabel('Score')
		plt.show()

	#current progress button
	graph1_button = Button(progress_level,text= "Current Progress", bg= "white", command = graph1, font = ('Poppins Medium',20))
	graph1_button.pack()

	space_Label = Label(progress_level, pady = 1, bg = "#feeb75")
	space_Label.pack()

	def graph2():
		ace_path = 'C:/Users/ashwi/OneDrive/Desktop/ace3.csv'
		ace_df = pd.read_csv(ace_path) 

		X = ace_df[['Study','Concentration','Attendance']]
		y = ace_df[['Score']]

		x = ace_df['Study']
		y = ace_df['Score']
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

		scaler = MinMaxScaler()

		X_train = scaler.fit_transform(X_train)
		X_test = scaler.transform(X_test)
		
		reg = RandomForestRegressor()
		reg.fit(X_train,y_train)

		reg.score(X_train,y_train)

		pred_data = [[18,5,9]]
		reg.predict(scaler.transform(pred_data))
		#Testing present value

		predict_data = pd.read_csv("C:/Users/ashwi/OneDrive/Desktop/ace_prediction.csv")
		a = reg.predict(scaler.transform(predict_data))

		df = pd.DataFrame(data=a)
		
		x = ace_df['Study']
		y = df.iloc[:,0]

		plt.bar(x, y, color='pink')
		plt.annotate("Week 4", (8.5,31.7))
		plt.annotate("Week 8", (8.6,40.0))
		plt.annotate("Week 1", (19.1,45.5))
		plt.annotate("Week 5", (10.4,25.4))
		plt.annotate("Week 11", (11.3,32.2))
		plt.annotate("Week 2", (12.2,47.2))
		plt.annotate("Week 7", (13.3,30))
		plt.annotate("Week 10", (14.1,38.2))
		plt.annotate("Week 9", (15.1,47.47))
		plt.annotate("Week 6", (16.3,42.7))
		plt.annotate("Week 3", (18.3,32.2))
		plt.annotate("Week 12", (18.3,29.4))

		plt.title('Study vs Predicted Score')
		plt.xlabel('Study')
		plt.ylabel('Predicted Score')
		plt.show()
 
	#Future progress button
	graph2_button = Button(progress_level,text= "Future Progress", bg= "#F2F2F2", font = ('Poppins Medium',20), command = graph2, padx = 10)
	graph2_button.pack() 

	space_Label = Label(progress_level, pady = 3, bg = "#feeb75")
	space_Label.pack()

	#exit button
	button_exit = Button(progress_level, text = "Exit", command = progress_level.destroy, padx = 7, bg = '#FF0000').pack()

	space_Label = Label(root, pady = 2, bg = "#feeb75")
	space_Label.pack()

progress_button = Button(root, text = "Progress",bg= "#ff781f",font = ('Poppins Medium',20), padx = 88, pady = 10, command = open)
progress_button.pack()

#SPACE PADDING 4
space_Label = Label(root, pady = 5, bg = '#cfebfd')
space_Label.pack()


#exit button
button_exit = Button(root, text = "Exit", command = root.destroy, font = ('Poppins Medium',10), padx = 17, pady = 7, bg = 'red').pack()

#SPACE PADDING 4
space_Label = Label(root, pady = 2, bg = '#cfebfd')
space_Label.pack()

root.mainloop()