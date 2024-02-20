import tkinter as tk
import threading
import time

class LinearSearchVisualizer:
    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        self.root.title("Linear Search List Visualizer")
        self.root.geometry("1000x600")
        self.root.configure(bg="light grey")  # Set background color    
        
        # Initialize working list, indices, and flags
        self.working_list = []
        self.current_index = -1
        self.searching = False
        self.enter_mode = False  # Flag to indicate Enter key mode
        self.canvas = tk.Canvas(root, width=800, height=500, bg="white")  # Set canvas background color
        self.canvas.place(x=300, y=0)  # Place the canvas to the right
        
        # Create input fields and buttons
        self.search_entry = tk.Entry(self.root)
        self.search_entry.place(x=10, y=10)
        self.search_entry.bind('<Return>', self.enter_key_mode)

        self.add_entry = tk.Entry(self.root)
        self.add_entry.place(x=10, y=40)
        self.add_entry.bind('<Return>', self.enter_key_mode)

        self.append_entry = tk.Entry(self.root)
        self.append_entry.place(x=10, y=380)
        self.append_entry.bind('<Return>', self.enter_key_mode)

        # ... other UI elements ...

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_application)
        self.exit_button.place(x=150, y=500)

        # ... other UI elements ...

        self.search_result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="white")
        self.search_result_label.place(x=10, y=630)
        
        self.old_value_label = tk.Label(self.root, text="Old Value:")
        self.old_value_label.place(x=10, y=80)
        self.old_value_entry = tk.Entry(self.root)
        self.old_value_entry.place(x=10, y=110)
        
        self.new_value_label = tk.Label(self.root, text="New Value:")
        self.new_value_label.place(x=10, y=140)
        self.new_value_entry = tk.Entry(self.root)
        self.new_value_entry.place(x=10, y=170)
        
        self.search_button = tk.Button(self.root, text="Search", command=self.start_search)
        self.search_button.place(x=150, y=10)
        
        self.add_button = tk.Button(self.root, text="Add", command=self.add_element)
        self.add_button.place(x=150, y=40)
        
        self.update_button = tk.Button(self.root, text="Update", command=self.update_element)
        self.update_button.place(x=40, y=200)
        
        self.delete_label = tk.Label(self.root, text="Value to Delete:")
        self.delete_label.place(x=10, y=240)
        self.delete_entry = tk.Entry(self.root)
        self.delete_entry.place(x=10, y=270)
        
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_element)
        self.delete_button.place(x=40, y=310)
        
        self.append_label = tk.Label(self.root, text="Value to Append:")
        self.append_label.place(x=10, y=350)
        
        
        self.append_button = tk.Button(self.root, text="Append", command=self.append_element)
        self.append_button.place(x=40, y=420)

        self.exit_label =tk.Label(self.root,text="App to Exit")
        self.exit_label.place(x=120,y=470)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_application)
        self.exit_button.place(x=150, y=500)

        self.clear_label =tk.Label(self.root,text="App to clear")
        self.clear_label.place(x=10,y=470)
        
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.place(x=10, y=500)

        self.sort_label = tk.Label(self.root,text="Sorting:")
        self.sort_label.place(x=70,y=540)
        
        self.sort_ascending_button = tk.Button(self.root, text="Sort Ascending", command=self.sort_ascending)
        self.sort_ascending_button.place(x=10, y=570)
        
        self.sort_descending_button = tk.Button(self.root, text="Sort Descending", command=self.sort_descending)
        self.sort_descending_button.place(x=120, y=570)
        
        self.search_result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="white")
        self.search_result_label.place(x=400, y=530)  # Adjust the Y-coordinate as per your preference


        # Draw initial list elements on canvas
        self.draw_list_elements()
     
    # ... other methods ...
    def draw_list_elements(self):
        self.canvas.delete("all")
        for i, num in enumerate(self.working_list):
            x = 50 + i * 60
            y = 400
            self.canvas.create_rectangle(x - 20, y, x + 20, y - num * 2, fill="green")
            self.canvas.create_text(x, y + 10, text=str(num), fill="black")

    def start_search(self):
        if self.searching:
            return
        self.searching = True
        self.search_button.config(state=tk.NORMAL)
        self.add_button.config(state=tk.NORMAL)
        self.update_button.config(state=tk.NORMAL)
        self.delete_button.config(state=tk.NORMAL)
        self.append_button.config(state=tk.NORMAL)
        self.exit_button.config(state=tk.NORMAL)
        
        # Start a thread for searching
        search_thread = threading.Thread(target=self.search)
        search_thread.start()

    # Modify the search method
    def search(self):
        element_found = False
        found_index = -1
        search_value = int(self.search_entry.get())

        while self.current_index < len(self.working_list) - 1:
            self.current_index += 1
            self.highlight_element(self.current_index)
            value = self.working_list[self.current_index]
            if value == search_value:
                found_index = self.current_index
                element_found = True
                break
            self.canvas.update()
            time.sleep(1)

        if element_found:
            self.highlight_element(found_index, color="yellow")
            self.search_result_label.config(text=f"Found value {search_value} at index {found_index}", fg="black")
        else:
            self.search_result_label.config(text="Value not found", fg="red")

        self.searching = False
        self.search_button.config(state=tk.NORMAL)
        self.add_button.config(state=tk.NORMAL)
        self.update_button.config(state=tk.NORMAL)
        self.delete_button.config(state=tk.NORMAL)
        self.append_button.config(state=tk.NORMAL)
        self.exit_button.config(state=tk.NORMAL)
        self.current_index = -1

    def delete_element(self):
        value_to_delete = int(self.delete_entry.get())
        if value_to_delete in self.working_list:
            self.working_list.remove(value_to_delete)
            self.draw_list_elements()
        else:
            self.search_result_label.config(text=f"Value {value_to_delete} not found", fg="red")
      

    def clear_canvas(self):
        self.working_list = []
        self.canvas.delete("all")

    def add_element(self, event=None):
        new_value = int(self.add_entry.get())
        if new_value not in self.working_list:  # Check for duplicate
            self.working_list.append(new_value)
            self.draw_list_elements()
            self.add_entry.delete(0, tk.END)  # Clear the Entry field

    def append_element(self, event=None):
        new_value = int(self.append_entry.get())
        if new_value not in self.working_list:  # Check for duplicate
            self.working_list.append(new_value)
            self.draw_list_elements()
            self.append_entry.delete(0, tk.END)  # Clear the Entry field

    def update_element(self):
        old_value = int(self.old_value_entry.get())
        new_value = int(self.new_value_entry.get())
        if old_value in self.working_list:
            index = self.working_list.index(old_value)
            self.working_list[index] = new_value
            self.draw_list_elements()
        else:
            self.search_result_label.config(text=f"Value {old_value} not found for update", fg="red")


    def exit_application(self):
        self.root.destroy()

    def highlight_element(self, index, color="yellow"):
        x = 50 + index * 60
        y = 400
        value = self.working_list[index]
        self.canvas.create_rectangle(x - 20, y, x + 20, y - value * 2, fill=color)
        self.canvas.create_text(x, y + 10, text=str(value), fill="red")

    def sort_ascending(self):
        self.working_list.sort()
        self.draw_list_elements()

    def sort_descending(self):
        self.working_list.sort(reverse=True)
        self.draw_list_elements()
        
    def enter_key_mode(self, event):
        self.enter_mode = True
        self.process_input()

    def process_input(self):
        if self.enter_mode:
            # Check which entry field has focus and call the appropriate function
            if self.search_entry == self.root.focus_get():
                self.start_search()
            elif self.add_entry == self.root.focus_get():
                self.add_element()
            elif self.append_entry == self.root.focus_get():
                self.append_element()
            elif self.delete_entry == self.root.focus_get():
                self.delete_element()
            elif self.old_value_entry == self.root.focus_get() or self.new_value_entry == self.root.focus_get():
                self.update_element()
            
            self.enter_mode = False  # Reset the Enter mode flag

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearSearchVisualizer(root)
    root.mainloop()
