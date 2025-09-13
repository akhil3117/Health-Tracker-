import tkinter as tk
from tkinter import messagebox
from backend import HealthTracker
import sugar_plotter, calorie_plotter, bp_plotter

name_var = age_var = gender_var = height_var = weight_var = calorie_target_var = None

valid_entry = True

def show_label_entry_widget(label_text, entry_variable):
    _label = tk.Label(frame, text=label_text)
    _label.pack()
    _entry = tk.Entry(frame, textvariable=entry_variable)
    _entry.pack()

def convert_to_int(var, m):
    global valid_entry
    if not valid_entry:
        return None
    if var.isnumeric():
        var = int(var)
        if var > 0:
            return var
        else:
            valid_entry = False
            messagebox.showerror("Error", f"Please enter valid value for {m}")
    else:
        valid_entry = False
        messagebox.showerror("Error", f"Please enter valid value for {m}")
    return None

def update_profile():
    global valid_entry
    name = name_var.get()
    if len(name) <= 0:
        messagebox.showerror("Error", "Enter valid Name")
        valid_entry = False
    age = convert_to_int(age_var.get(), "Age")
    gender = gender_var.get()
    if valid_entry:
        if len(gender) <= 0:
            messagebox.showerror("Error", "Enter valid Gender")
            valid_entry = False
    height = convert_to_int(height_var.get(), "Height")
    weight = convert_to_int(weight_var.get(), "Weight")
    calorie_target = convert_to_int(calorie_target_var.get(), "Calorie Target")
    if valid_entry:
        health_tracker.init_profile(name,
                                    age,
                                    gender,
                                    height,
                                    weight,
                                    calorie_target)
        return True
    else:
        valid_entry = True
        return False

def update_variables():
    global name_var, age_var, gender_var, height_var, weight_var, calorie_target_var
    name_var = tk.StringVar(frame, health_tracker.name)
    age_var = tk.StringVar(frame, health_tracker.age)
    gender_var = tk.StringVar(frame, health_tracker.gender)
    height_var = tk.StringVar(frame, health_tracker.height)
    weight_var = tk.StringVar(frame, health_tracker.weight)
    calorie_target_var = tk.StringVar(frame, health_tracker.calorie_target)

def on_register_submit():
    success = update_profile()
    if success:
        clear_frame()
        show_profile_page()
    else:
        show_register_page()

def show_register_page():
    clear_frame()
    update_variables()
    show_label_entry_widget("Name", name_var)
    show_label_entry_widget("Age", age_var)
    show_label_entry_widget("Gender", gender_var)
    show_label_entry_widget("Height (in cm)", height_var)
    show_label_entry_widget("Weight (in kg)", weight_var)
    show_label_entry_widget("Your Calorie Target", calorie_target_var)

    submit = tk.Button(frame, text="Continue", command=on_register_submit)
    submit.pack()

def update_list(list_name):
    if list_name == health_tracker.CALORIE_TRACK_LIST_NAME:
        var = cal_var
        value = var.get()
        try:
            value = int(value)
            if value != 0:
                valid = True
        except ValueError:
            valid = False
    elif list_name == health_tracker.SUGAR_TRACK_LIST_NAME:
        var = sugar_var
        value = var.get()
        try:
            value = int(value)
            if value > 0:
                valid = True
        except ValueError:
            valid = False
    if valid:
        health_tracker.update_tracklist(list_name, value)
        messagebox.showinfo("Info", "Value Recorded")
    else:
        messagebox.showerror("Error", "Please enter valid value")
    var.set("")

def update_bp():
    bp_value = bp_var.get()
    if "/" in bp_value and len(bp_value) >= 3:
        health_tracker.update_tracklist(health_tracker.BP_TRACK_LIST_NAME, bp_value)
        messagebox.showinfo("Info", "Blood Pressure Recorded")
    else:
        messagebox.showerror("Error", "Please type in correct format (systolic/diastolic)")
    bp_var.set("")

def show_profile_page():
    update_profile_btn = tk.Button(frame, text="Update Profile", command=show_register_page)
    update_profile_btn.pack()
    name_label = tk.Label(frame, text=f"Welcome {health_tracker.name.upper()}")
    name_label.pack()
    bmi_label = tk.Label(frame, text=f"Current BMI: {health_tracker.get_bmi():.2f}")
    bmi_label.pack()
    
    _label = tk.Label(frame, text="Update Calorie\n(Enter positive for intake, Negative for burnt)")
    _label.pack()
    _input = tk.Entry(frame, textvariable=cal_var)
    _input.pack()
    _btn = tk.Button(frame, text="Add", command=lambda: update_list(health_tracker.CALORIE_TRACK_LIST_NAME))
    _btn.pack()
    _btn = tk.Button(frame, text="Show Graph", command=lambda: calorie_plotter.plot(health_tracker.calorie_track,
                                                                                    health_tracker.calorie_intake,
                                                                                    health_tracker.calorie_burnt))
    _btn.pack()

    _label = tk.Label(frame, text="Record BP (sys/dia)")
    _label.pack()
    _input = tk.Entry(frame, textvariable=bp_var)
    _input.pack()
    _btn = tk.Button(frame, text="Record", command=update_bp)
    _btn.pack()
    _btn = tk.Button(frame, text="Show Graph", command=lambda: bp_plotter.plot(health_tracker.bp_track))
    _btn.pack()

    _label = tk.Label(frame, text="Record Sugar (mg/dL)")
    _label.pack()
    _input = tk.Entry(frame, textvariable=sugar_var)
    _input.pack()
    _btn = tk.Button(frame, text="Record", command=lambda: update_list(health_tracker.SUGAR_TRACK_LIST_NAME))
    _btn.pack()
    _btn = tk.Button(frame, text="Show Graph", command=lambda: sugar_plotter.plot(health_tracker.sugar_track))
    _btn.pack()

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

health_tracker = HealthTracker()
root = tk.Tk()
root.title("Health Tracker App")
root.geometry("700x400")
frame = tk.Frame(root, width=700, height=400)
frame.pack()
cal_var = tk.StringVar(frame, value="")
sugar_var = tk.StringVar(frame, value="")
bp_var = tk.StringVar(frame)

show_register_page()

root.mainloop()