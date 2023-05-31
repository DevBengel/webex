import tkinter as tk
import subprocess

def start_module():
    try:
        process = subprocess.Popen(["python", "../init_lab.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        console_output.configure(state='normal')
        console_output.delete('1.0', tk.END)
        console_output.insert(tk.END, stdout.decode())
        console_output.insert(tk.END, stderr.decode())
        console_output.configure(state='disabled')
    except FileNotFoundError:
        console_output.configure(state='normal')
        console_output.delete('1.0', tk.END)
        console_output.insert(tk.END, "Error: Module not found.")
        console_output.configure(state='disabled')

# Create the main window
window = tk.Tk()
window.title("Module Launcher")

# Create a button to start the module
start_button = tk.Button(window, text="Start Module", command=start_module)
start_button.pack()

# Create a text widget to display console output
console_output = tk.Text(window, height=10, width=50, state='disabled')
console_output.pack()

# Run the GUI main loop
window.mainloop()
