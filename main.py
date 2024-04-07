import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Scrollbar, Treeview

class HairmessGameEngine:
    def __init__(self, root):
        self.root = root
        self.root.title("Hairmess Game Engine")
        self.root.iconbitmap('gui/graphics/icons/icon.ico')  # Set your icon path correctly

        self.setup_gui()

    def setup_gui(self):
        # Create and configure the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        # Label and Entry for project name
        project_label = tk.Label(self.main_frame, text="Project Name:")
        project_label.grid(row=0, column=0, sticky=tk.W)

        self.project_name_entry = tk.Entry(self.main_frame)
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)

        # Button to create project
        create_button = tk.Button(self.main_frame, text="Create Project", command=self.create_project)
        create_button.grid(row=0, column=2, padx=10, pady=5)

        # Scrollable list of project folders
        scrollbar = Scrollbar(self.main_frame, orient=tk.VERTICAL)
        scrollbar.grid(row=1, column=3, sticky=tk.NS)

        self.project_listbox = Treeview(self.main_frame, yscrollcommand=scrollbar.set, columns=("Folder"))
        self.project_listbox.heading("#0", text="Projects")
        self.project_listbox.column("#0", width=200)
        self.project_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky=tk.NSEW)

        scrollbar.config(command=self.project_listbox.yview)

        # Display existing projects in the list
        self.refresh_projects_list()

    def refresh_projects_list(self):
        # Clear existing items in the project list
        self.project_listbox.delete(*self.project_listbox.get_children())

        # Scan the projects directory for folders
        projects_path = 'projects/'
        if os.path.exists(projects_path):
            for folder_name in os.listdir(projects_path):
                if os.path.isdir(os.path.join(projects_path, folder_name)):
                    self.project_listbox.insert("", "end", text=folder_name)

    def create_project(self):
        project_name = self.project_name_entry.get().strip()

        if not project_name:
            messagebox.showerror("Error", "Please enter a project name.")
            return

        projects_path = 'projects/'

        if project_name in self.project_listbox.get_children():
            messagebox.showerror("Error", "Project already exists.")
            return

        try:
            # Copy the example folder to create a new project
            shutil.copytree('assets/setup/example', os.path.join(projects_path, project_name))
            messagebox.showinfo("Success", f"Project '{project_name}' created successfully!")
            self.refresh_projects_list()  # Refresh the projects list
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create project: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HairmessGameEngine(root)
    root.mainloop()
