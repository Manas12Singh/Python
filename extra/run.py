import tkinter as tk
import json
from tkinter import simpledialog,filedialog
import tkinter as tk
import json
from tkinter import messagebox
import sys
import subprocess
import os

global CLEAR
global C_CPP_EXTENSION
if sys.platform=="linux":
    CLEAR="clear"
    C_CPP_EXTENSION="out"
else:
    CLEAR="cls"
    C_CPP_EXTENSION="exe"

class StudentForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Information Form")
        self.setup_ui()

    def setup_ui(self):
        form_dict={'name_label':"Name:"}
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)

        self.rollno_label = tk.Label(self, text="Roll Number:")
        self.rollno_entry = tk.Entry(self)

        self.section_label = tk.Label(self, text="Section:")
        self.section_entry = tk.Entry(self)

        self.sem_label = tk.Label(self, text="Semester:")
        self.sem_entry = tk.Entry(self)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_form)

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        self.rollno_label.grid(row=1, column=0)
        self.rollno_entry.grid(row=1, column=1)

        self.section_label.grid(row=2, column=0)
        self.section_entry.grid(row=2, column=1)

        self.sem_label.grid(row=3, column=0)
        self.sem_entry.grid(row=3, column=1)

        self.submit_button.grid(row=4, column=0, columnspan=2)

    def submit_form(self):  
        name = self.name_entry.get()
        rollno = self.rollno_entry.get()
        section = self.section_entry.get()
        sem = self.sem_entry.get()

        if name and rollno and section and sem:
            student_data = {
                "Name": name,
                "RollNo": rollno,
                "Section": section,
                "Semester": sem
            }

            try:
                with open("students.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            data.append(student_data)

            with open("students.json", "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo("Form Submission", "Student data has been saved.")
            self.destroy()
            app=Login()
            app.mainloop()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

class insertInput(tk.Tk):
    def __init__(self,input_files):
        super().__init__()

class CCPPRunner(tk.Tk):
    def __init__(self,index):
        super().__init__()
        with open("students.json", "r") as file:
                self.ids = json.load(file)
        self.title("C/C++ Runner")
        self.id=index
        self.file_label = tk.Label(self, text="Select C/C++ files:")
        self.cpp_files = tk.Listbox(self, selectmode=tk.MULTIPLE, width=40)
        self.browse_button = tk.Button(self, text="Browse", command=self.open_files)
        self.run_button = tk.Button(self, text="Compile & Run", command=self.compile_and_run)
        self.result_label = tk.Label(self, text="")

        self.file_label.grid(row=0, column=0)
        self.cpp_files.grid(row=0, column=1)
        self.browse_button.grid(row=0, column=2)
        self.run_button.grid(row=1, column=0, columnspan=3)
        self.result_label.grid(row=2, column=0, columnspan=3)

    def wait_for_keypress(self):
        print("\n\n\n\n\nPress any key to continue...")
        input()

    def open_files(self):
        initial_directory = os.getcwd()
        file_paths = filedialog.askopenfilenames(
            initialdir=initial_directory, filetypes=[("C/C++ files", "*.c *.cpp *.java")])
        if file_paths:
            self.cpp_files.delete(0, tk.END)
            for file_path in file_paths:
                self.cpp_files.insert(tk.END, file_path)

    def compile_and_run(self):
        cp=os.getcwd()+'\\bin\\'
        if not os.path.exists(cp):
            os.makedirs(cp)
        selected_files = self.cpp_files.get(0, tk.END)
        if selected_files:
            for file in selected_files:
                subprocess.check_call(CLEAR, shell=True)
                file = file.strip()
                path1=str(os.path.dirname(file))
                try:
                    file_extension = file.split(".")[-1]
                    if file_extension == "c":
                        compile_command = f'gcc \"{file}\" -o \"{cp}a.{C_CPP_EXTENSION}\"'
                        run_command = f'.\\a.{C_CPP_EXTENSION}'
                    elif file_extension == "cpp":
                        compile_command = f'g++ \"{file}\"  -o \"{cp}a.{C_CPP_EXTENSION}\"'
                        run_command = f'.\\a.{C_CPP_EXTENSION}'
                    elif file_extension=="java":
                        compile_command = f'javac -d {cp} \"{file}\"'
                        k=open(file).readline().split(' ')
                        if(k[0]=='package'):
                            run_command = f'java {k[1][:-2]}.{file.split("/")[-1].split(".")[0]}'
                            path1=path1.removesuffix(k[1][:-2].replace('.','/'))
                        else:
                            run_command=f'java {file.split("/")[-1].split(".")[0]}'
                    else:
                        self.result_label.config(
                            text=f"Unsupported file format: {file}")
                        continue

                    print(f"{file}\n\n{self.ids[self.id]['Name']}\\{self.ids[self.id]['RollNo']}\\{self.ids[self.id]['Semester']}\\{self.ids[self.id]['Section']}>{f'java {file.split("/")[-1].split(".")[0]}' if file_extension=='java' else '.\\a.exe'}")
                    subprocess.check_call(compile_command, shell=True,cwd=path1)
                    subprocess.check_call(run_command, shell=True,cwd=cp)
                    self.wait_for_keypress()

                except subprocess.CalledProcessError:
                    self.result_label.config(
                        text=f"Error: Compilation or execution failed for {file}")
                else:
                    self.result_label.config(
                        text=f"Program executed successfully: {file}")
        else:
            self.result_label.config(text="Please select C/C++ files to run.")

class Login(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        try:
            with open("students.json") as file:
                self.ids=json.load(file)
        except:
            self.ids={}
        self.title("Login")
        self.geometry("300x200+100+100")
        for i in range(len(self.ids)):
            frame = tk.Frame(self, padx=5, pady=5)
            frame.pack()
            button = tk.Button(frame, text=f"{self.ids[i]['Name']}", command=lambda index=i: self.login(index))
            button.pack()
        frame = tk.Frame(self, padx=10, pady=10)
        frame.pack()
        button=tk.Button(frame,text=f"Create New Id",command=lambda :self.createId())
        button.pack()
    def createId(self):
        self.destroy()
        app=StudentForm()
        app.mainloop()
    def login(self,index):
        with open("students.json") as file:
            self.ids=json.load(file)
        self.destroy()
        app=CCPPRunner(index)
        app.mainloop()

if __name__ == "__main__":
    app = Login()
    app.mainloop()
