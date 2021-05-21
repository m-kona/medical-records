from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x400")
window.title("Medical Records")
frame = Frame(window)



#The layout of The Sick Class

illness_ID = Label(window, text = "Illness Code")
illness_ID.pack(side = LEFT)
illness_ID.place(x = 20, y = 20)

illness_entry = Entry(window, bd =1)
illness_entry.pack(side = RIGHT)
illness_entry.place(x = 300, y = 20)

treatment_duration = Label(window, text = "Duration Of Treatment")
treatment_duration.pack(side =LEFT )
treatment_duration.place(x = 20, y= 80)

week_month = Label(window, text = "Weekly/Months")
week_month.pack(side = RIGHT)
week_month.place(x = 380, y = 80)

due_entry = Entry(window, bd =1, width = 8)
due_entry.pack(side =RIGHT)
due_entry.place(x = 300, y = 80)

dr_number = Label(window, text="Dr Practice Number")
dr_number.pack(side = LEFT)
dr_number.place(x = 20, y = 150)

doc_entry = Entry(window, bd =1)
doc_entry.pack(side = RIGHT)
doc_entry.place(x = 300, y =150)

scan_fee = Label(window, text = "Scan/Consultation Fee")
scan_fee.pack(side = LEFT)
scan_fee.place(x = 20, y = 190)

scan_entry = Entry(window, bd =1)
scan_entry.pack(side = RIGHT)
scan_entry.place(x = 301, y = 190)


amount_paid = Label(window)
amount_paid.pack(side = LEFT)
amount_paid.place(x = 20, y = 260)

var = StringVar()

# The Calculations for the Sick Class
class Sick():
    def sickness(self):
        self.illness_ID = illness_ID
        self.treatment_duration = treatment_duration
        self.dr_number = dr_number
        self.medcancer = 400
        self.medinflu = 350.50

# Calculating Cancer
def illness():
    if var.get() == "Cancer":
        if int(scan_entry.get()) > 600:
            messagebox.showinfo("Message", "Sorry we cannot treat you") # Error message will display
        elif int(scan_entry.get()) < 600:
           cancer_answer = int(scan_entry.get()) + 400
           amount_paid.config(text="Amount Paid For Treatment: " + str(cancer_answer))

    if var.get() == "Influenza": # Calculating Influenza
        if int(scan_entry.get()) >= 600:
            influ_answer = 350.50 + int(scan_entry.get())
            amount_paid.config(text="Amount Paid For Treatment: " + str(influ_answer))
        elif int(scan_entry.get()) < 600:
            influ_answer = 350.50 + int(scan_entry.get())
            discount = (influ_answer * (2/100)) + influ_answer # Calculating the discount recieve
            messagebox.showinfo("Message", "2% discount")
            amount_paid.config(text="Amount Paid For Treatment: "  + str(discount)) #discount will be included in the calculation




radio_btn1 = Radiobutton(window, text = "Cancer" , variable = var, value ="Cancer") # Radiobutton for Cancer
radio_btn1.pack(side = LEFT)
radio_btn1.place(x = 20, y= 220)

radio_btn2 = Radiobutton(window, text = "Influenza", variable = var, value = "Influenza")# Radiobutton for Influenza
radio_btn2.pack(side = LEFT)
radio_btn2.place(x = 20, y= 240)

calculate_btn = Button(window, text = "Calculate", command = illness) # Calculates the amount paid for treatment once pushed
calculate_btn.pack(side = LEFT)
calculate_btn.place(x = 20, y = 300)

# Function on the clear all button
def clear_all():
    illness_entry.delete(0,END)
    due_entry.delete(0,END)
    doc_entry.delete(0,END)
    scan_entry.delete(0,END)

clear_btn = Button(window, text = "Clear", command = clear_all) #Clears everything when the button is pushed
clear_btn.pack(side = RIGHT)
clear_btn.place(x = 300, y = 300)



window.mainloop()