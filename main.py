#import tkinter 
import tkinter as tk


def temperature_conversion(temp_value,temp_convert):
    if temp_convert == "Celsuis to Fahrenheit":
        return f"{temp_value} Celsius is equal to {temp_value * 9/5 + 32} Fahrenheit"
    elif temp_convert == "Celsuis to Kelvin":
        return f"{temp_value} Celsius is equal to {temp_value + 273.15} Kelvin"
    elif temp_convert == "Fahrenheit to Celsuis":
        return f"{temp_value} Fahrenheit is equal to {(temp_value - 32) *5/9} Celsuis"
    else:
        return "Invaild  Temperature Conversion"
    
def mass_conversion(mass_value,mass_convert):
    if mass_convert == "Gram to Kilogram":
        return f"{mass_value} g is equal to {mass_value/1000} Kg"
    elif mass_convert == "Kilogram to Gram":
        return f"{mass_value} Kg is equal to {mass_value*1000} g"
    else:
        return "Invalid Mass Conversion"

def length_conversion(length_value,length_convert):
    if  length_convert =="Centimeter to Meter":
        return f"{length_value} cm is equal to{length_value/100} m"
    elif length_convert == "Meter to Centimeter":
        return f"{length_value} m is equal to {length_value*100}cm"
    elif length_convert == "Centimeter to Feet":
        return f"{length_value} cm is equal to {length_value/30.48} ft"
    elif length_convert == "Feet to Inches":
        return f"{length_value} ft is equal tp {length_value *12} inch"
    else:
        return "Invalid Length Conversion"
    
def area_conversion(area_value,area_convert):
    if area_convert == "Sqft to Sqmtr":
        return f"{area_value} sqft is equal to {area_value*0.092903} Sqmtr"
    elif area_convert == "Sqft to Hectare":
        return f"{area_value} sqft is equal to {area_value*0.00000929} hectares"
    elif area_convert =="sqft to Acres":
        return f"{area_value} sqft is equal to {area_value*0.000002296} acres"
    else:
        return "Invalid Area Conversion"
    
def Perform_conversion():
    try:
        input_value = float(Entry_val.get())
        selected_conversion = conversion_var.get()

        if selected_conversion == "Temperature":
            temp_var.set(temp_var.get())
            result_label.config(text=temperature_conversion(input_value,temp_var.get()))
        elif selected_conversion == "Mass":
            mass_var.set(mass_var.get())
            result_label.config(text=mass_conversion(input_value,mass_var.get()))
        elif selected_conversion =="Length":
            length_var.set(length_var.get())
            result_label.config(text=length_conversion(input_value,length_var.get()))
        elif selected_conversion=="Area":
            area_var.set(area_var.get())
            result_label.config(text=area_conversion(input_value,area_var.get()))
        else:
            result_label.config(text="Invalid Conversion")

    except ValueError:
        result_label.config(text="Enter the Valid Number")

#creating main Window
window= tk.Tk()
window.title("Conversion")

#declare the Gobal Variables
temp_var =tk.StringVar()
mass_var =tk.StringVar()
length_var = tk.StringVar()
area_var = tk.StringVar()


conversion_var =tk.StringVar()
conversion_var.set("Choose type")

conversion_label = tk.Label(window,text=" Choose conversion Type :")
conversion_label.grid(row=0,column=0,pady=5,padx=10,sticky="e")

conversion_menu = tk.OptionMenu(window,conversion_var,"Temperature","Mass","Length","Area")
conversion_menu.grid(row=0,column=1,pady=5,padx=10,sticky="w")

Entry_val = tk.Label(window,text="Enter the number to convert :")
Entry_val.grid(row=1,column=0,pady=5,padx=10,sticky="e")

Entry_val = tk.Entry(window)
Entry_val.grid(row=1,column=1,pady=5,padx=10,sticky="w")

#Temperature Conversion
temp_var.set(" choose to Conversion")

temp_label = tk.Label(window,text="Choose the Temperature Conversion:")
temp_label.grid(row=2,column=0,pady=5,padx=10,sticky="e")

temp_menu = tk.OptionMenu(window,temp_var,"Celsuis to Fahrenheit","Celsuis to Kelvin","Fahrenheit to Celsuis")
temp_menu.grid(row=2,column=1,pady=5,padx=10,sticky="w")

#Mass Converstion
mass_var.set(" choose to Conversion")

mass_label = tk.Label(window,text="Choose the Mass Converstion :")
mass_label.grid(row=3,column=0,pady=5,padx=10,sticky="e")

mass_menu =tk.OptionMenu(window,mass_var,"Gram to Kilogram","Kilogram to Gram")
mass_menu.grid(row=3,column=1,pady=5,padx=10,sticky="w")

#Length Conversion
length_var.set(" choose to Conversion")

length_label = tk.Label(window,text="Choose the Length Conversion : ")
length_label.grid(row=4,column=0,pady=5,padx=10,sticky="e")

length_menu = tk.OptionMenu(window,length_var,"Centimeter to Meter","Meter to Centimeter","Centimeter to Feet","Feet to Inches")
length_menu.grid(row=4,column=1,pady=5,padx=10,sticky="w")

#Area conversion 
area_var.set(" choose to Conversion")

area_label = tk.Label(window,text="Choose Area conversion : ")
area_label.grid(row=5,column=0,pady=5,padx=10,sticky="e")

area_menu = tk.OptionMenu(window,area_var,"Sqft to Sqmtr","Sqft to Hectare","sqft to Acres")
area_menu.grid(row=5,column=1,pady=5,padx=10,sticky="w")

#conversion button
convert_button = tk.Button(window,text="Convert",command=Perform_conversion)
convert_button.grid(row=6,column=0,columnspan=2,pady=10)

#result
result_label =tk.Label(window,text=" ")
result_label.grid(row=7,column=0,columnspan=2,pady=5)



#tkinter loop
window.mainloop()
    