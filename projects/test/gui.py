import tkinter as tk
from tkinter import filedialog, messagebox
import os

def create_scene_file():
    scene_name = scene_name_entry.get()
    if scene_name:
        scene_file_path = os.path.join("scenes", f"{scene_name}.py")
        with open(scene_file_path, 'w') as f:
            f.write("# This is a new scene file.")
        messagebox.showinfo("Scene Created", f"Scene '{scene_name}.py' created successfully!")

def list_files_in_directory(directory):
    files_listbox.delete(0, tk.END)  # Clear previous list
    files = os.listdir(directory)
    for file in files:
        files_listbox.insert(tk.END, file)

def open_file_in_editor(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
    text_editor.delete(1.0, tk.END)  # Clear previous content
    text_editor.insert(tk.END, file_content)
    # Disable scene list and show back button
    files_listbox.config(state=tk.DISABLED)
    back_button.pack(side=tk.LEFT, padx=10)

def save_file_changes(file_path):
    new_content = text_editor.get(1.0, tk.END)
    with open(file_path, 'w') as f:
        f.write(new_content)
    messagebox.showinfo("File Saved", "Changes saved successfully!")

def back_to_file_list():
    files_listbox.config(state=tk.NORMAL)
    back_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Scene Editor")

# Create Scene Section
scene_frame = tk.Frame(root, pady=10)
scene_frame.pack()

scene_name_label = tk.Label(scene_frame, text="Enter Scene Name:")
scene_name_label.grid(row=0, column=0)

scene_name_entry = tk.Entry(scene_frame, width=20)
scene_name_entry.grid(row=0, column=1)

create_scene_button = tk.Button(scene_frame, text="Create Scene", command=create_scene_file)
create_scene_button.grid(row=0, column=2, padx=10)

# List Files Section
files_frame = tk.Frame(root, pady=10)
files_frame.pack()

files_label = tk.Label(files_frame, text="Files in 'scenes' and 'graphics' folders:")
files_label.grid(row=0, column=0)

files_listbox = tk.Listbox(files_frame, width=40, height=10)
files_listbox.grid(row=1, column=0)

# Update listbox with initial files
list_files_in_directory("scenes")  # List files in 'scenes' folder initially

# Bind listbox double-click event to open file in editor
def on_file_selected(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        file_name = widget.get(selection[0])
        file_path = os.path.join("scenes", file_name)
        open_file_in_editor(file_path)

files_listbox.bind("<Double-Button-1>", on_file_selected)

# Back Button for Text Editor
back_button = tk.Button(files_frame, text="Back to File List", command=back_to_file_list)

# Text Editor Section
text_editor_frame = tk.Frame(root, pady=10)
text_editor_frame.pack()

text_editor_label = tk.Label(text_editor_frame, text="Scene Editor:")
text_editor_label.pack()

text_editor = tk.Text(text_editor_frame, width=60, height=15)
text_editor.pack()

# Save Changes Button
save_changes_button = tk.Button(root, text="Save Changes", command=lambda: save_file_changes(file_path))
save_changes_button.pack(pady=10)

root.mainloop()
