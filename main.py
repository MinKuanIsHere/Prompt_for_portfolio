import tkinter as tk
import prompt

from prompt import API_KEY, begin_text, end_text, text_generate_model_name, text_mask_model_name

def submit_message():
    
    inputs = message_entry.get() #input string
    
    message1 = prompt.single_mask(inputs, text_mask_model_name)
    display_text1.config(state=tk.NORMAL)  # Enable editing temporarily
    display_text1.delete("1.0", tk.END)    # Clear existing text
    display_text1.insert(tk.END, message1)  # Insert new message
    display_text1.config(state=tk.DISABLED) # Disable editing

    message2 = prompt.single_generate(inputs, text_generate_model_name)
    display_text2.config(state=tk.NORMAL)  # Enable editing temporarily
    display_text2.delete("1.0", tk.END)    # Clear existing text
    display_text2.insert(tk.END, message2)  # Insert new message
    display_text2.config(state=tk.DISABLED) # Disable editing

if __name__ == '__main__':

    # Create the main window
    root = tk.Tk()
    root.title("Prompt with portfolio") # window title name
    root.geometry("800x500")  # window size: 500x300
    root.config(bg="darkgrey") # window background color

    # Create a label for instruction
    label = tk.Label(root, text="Enter your message:", bg="darkgrey", font='Hlveticae 14 bold')
    label.pack(pady=(10, 0))

    # Create a text entry box
    message_entry = tk.Entry(root, width=50)
    message_entry.pack(pady=10)

    # Create a submit button
    submit_button = tk.Button(root, text="Submit", command=submit_message, font='Hlveticae 12 bold')
    submit_button.pack(pady=10)

    # Create a label Mask
    display_label = tk.Label(root, text="Prompt by MASK:", bg="darkgrey", wraplength=480, justify=tk.LEFT, font='Hlveticae 14 bold')
    display_label.pack(pady=(0, 10))
    # show result by mask
    display_text1 = tk.Text(root, height=10, width=95, wrap=tk.WORD, state=tk.DISABLED, bg="whitesmoke")
    display_text1.pack(pady=(0, 10))

    # Create a label gererate
    display_label = tk.Label(root, text="Prompt by Generate:", bg="darkgrey", wraplength=480, justify=tk.LEFT, font='Hlveticae 14 bold')
    display_label.pack(pady=(0, 10))
    # show result by generate
    display_text2 = tk.Text(root, height=10, width=95, wrap=tk.WORD, state=tk.DISABLED, bg="whitesmoke")
    display_text2.pack(pady=(0, 10))

    root.mainloop()