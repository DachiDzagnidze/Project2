import re
from tkinter import *  

#=======================================================Window Setup================================================================

win = Tk()  # Create main window
win.title("Professional Calculator")  
win.resizable(False, False)  
win.config(bg="#2E2E2E") 

#====================================================Defining the Calculator Functions==============================================

# es funcia anaxlebs ekrans ra drosac xdeba raimeze daklikeba
def button_press(num):
    current = input_text.get()
    input_text.set(current + str(num))  # daumatebs archeul iricxvis gamotqmas

# es function amushavebs (+, -, /, *)operatorrebs da aaxlebs exxpersions
def button_oper(opr):
    current = input_text.get()
    if current and current[-1] in "+-*/":  # amowmebs tu bolo operatori simboloa
        input_text.set(current[:-1] + opr)  # es dzvel operators cvlis axlit 
    elif current:  # mxolod mashin amatebs operators tu raime aris win
        input_text.set(current + str(opr))

# This function clears the display and resets the expression
def clr_scr():
    input_text.set("")  # Clear the display

# This function removes the last character from the current input (backspace)
def backspace():
    current = input_text.get()
    input_text.set(current[:-1])  # Remove the last character from the current expression

# This function calculates the result when the "=" button is pressed
def equal():
    try:
        result = calculate_result(input_text.get())  # Use the custom calculate_result function
        input_text.set(result)  # Update the display with the result
    except:
        input_text.set("Error")  # Show an error message if the expression is invalid

# This function calculates the percentage when the "%" button is pressed
def percent():
    current = input_text.get()
    try:
        result = str(float(current) / 100)  # Convert to percentage
        input_text.set(result)  # Update the display with the result
    except:
        input_text.set("Error")

# This function calculates the square root when the "√" button is pressed
def square_root():
    current = input_text.get()
    try:
        result = str(float(current) ** 0.5)  # Calculate the square root
        input_text.set(result)  # Update the display with the result
    except:
        input_text.set("Error")

# Custom function to safely evaluate the expression (without using eval)
def calculate_result(expression):
    # Remove all spaces
    expression = expression.replace(' ', '')
    
    # Check if the expression contains invalid characters
    if re.search(r'[^0-9\+\-\*/\.\(\)\^]', expression):
        raise ValueError("Invalid character in expression")

    try:
        # Basic mathematical expression evaluation
        # Replace ^ with ** for power operations
        expression = expression.replace('^', '**')
        
        # Safe evaluation using eval
        result = eval(expression)
        return str(result)
    except Exception as e:
        print(e)
        return "Error"
    

def equal():
    try:
        result = calculate_result(input_text.get())
        # If the result is an integer (e.g., 45.0), convert it to an integer without the .0
        if float(result).is_integer():
            result = str(int(float(result)))  # Convert to int if it's a whole number
        input_text.set(result)
    except:
        input_text.set("Error")

def equal():
    try:
        result = calculate_result(input_text.get())
        # Convert to float for processing
        result = float(result)

        # If the result is very large (greater than 1e9) or very small (less than 1e-5), format in scientific notation
        if abs(result) >= 1e9 or abs(result) < 1e-5:
            result = "{:.5e}".format(result).replace("+", "")  # Scientific notation, remove the "+"
        elif result.is_integer():
            result = str(int(result))  # Convert to int if it's a whole number
        else:
            result = str(result)  # Otherwise, keep it as a float string
        
        input_text.set(result)
    except:
        input_text.set("Error")

#====================================================Setting up the Display===========================================================

# Frame for the display area, this adds some structure and aesthetics
display_frame = LabelFrame(win, text=" Calculator by DachiDzagno ", relief=SUNKEN, padx=10, pady=10, bg="#444")
display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# This variable stores and displays the current expression
input_text = StringVar()

# Entry widget to show the input/output. The font size and width are set to make the display clearer.
display = Entry(display_frame, font=('Arial', 24, 'bold'), textvariable=input_text, width=16, bg="#1E1E1E", fg="#FFF", bd=0, justify=RIGHT)
display.pack(ipady=20)  # `ipady` makes the display area slightly larger for better readability

#====================================================Defining the Buttons===========================================================

# Defining buttons with appropriate colors, sizes, and commands
button_1 = Button(win, text="1", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(1))
button_2 = Button(win, text="2", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(2))
button_3 = Button(win, text="3", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(3))
button_4 = Button(win, text="4", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(4))
button_5 = Button(win, text="5", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(5))
button_6 = Button(win, text="6", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(6))
button_7 = Button(win, text="7", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(7))
button_8 = Button(win, text="8", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(8))
button_9 = Button(win, text="9", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(9))
button_0 = Button(win, text="0", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press(0))

# Operator buttons with different colors for better distinction
button_add = Button(win, text="+", bg="#4C90E2", fg="white", font=("Arial", 20, "bold"), command=lambda: button_oper("+"))
button_sub = Button(win, text="-", bg="#4C90E2", fg="white", font=("Arial", 20, "bold"), command=lambda: button_oper("-"))
button_div = Button(win, text="÷", bg="#4C90E2", fg="white", font=("Arial", 20, "bold"), command=lambda: button_oper("/"))
button_mul = Button(win, text="×", bg="#4C90E2", fg="white", font=("Arial", 20, "bold"), command=lambda: button_oper("*"))

# Action buttons for "=" (equal) and "C" (clear)
button_equal = Button(win, text="=", bg="#F5A623", fg="white", font=("Arial", 20, "bold"), command=equal)
button_clear = Button(win, text="C", bg="#D0021B", fg="white", font=("Arial", 20, "bold"), command=clr_scr)

# Decimal point button
button_dec = Button(win, text=".", bg="#4C4C4C", fg="white", font=("Arial", 20, "bold"), command=lambda: button_press("."))

# Percentage button in purple
button_percent = Button(win, text="%", bg="#9B59B6", fg="white", font=("Arial", 20, "bold"), command=percent)

# Square root button in purple
button_sqrt = Button(win, text="√", bg="#9B59B6", fg="white", font=("Arial", 20, "bold"), command=square_root)

# Backspace button to remove the last character
button_backspace = Button(win, text="⌫", bg="#F5A623", fg="white", font=("Arial", 20, "bold"), command=backspace)

#====================================================Placing Buttons on the Window===================================================

# Using grid layout to arrange the buttons in the window
button_7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button_8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button_9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
button_add.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

button_4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
button_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
button_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
button_sub.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

button_1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button_2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
button_3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
button_mul.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

button_clear.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")  # Clear is now on the bottom left
button_0.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
button_dec.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
button_div.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

button_backspace.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")  # Backspace moved to the top-right
button_percent.grid(row=2, column=4, padx=5, pady=5, sticky="nsew")  # Percentage moved below
button_sqrt.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")
button_equal.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")  # "=" moved to the bottom-right

# Make all buttons resize according to the window size
for i in range(5):
    win.grid_rowconfigure(i, weight=1)
    win.grid_columnconfigure(i, weight=1)

#========================================================Main Loop===================================================================

win.mainloop()
