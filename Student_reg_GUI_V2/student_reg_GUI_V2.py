        ##### Updated GUI Version #####

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.modalview import ModalView
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import re  # Import the regular expressions module
import random  # Import the random module

# Import additional modules for the shiny button effect
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle

class ShiningButton(Button):
    def __init__(self, **kwargs):
        super(ShiningButton, self).__init__(**kwargs)
        self.background_color_normal = (0.1, 0.5, 0.8, 1)  # Normal background color
        self.background_color_down = (7, 2, 3.6, 5, 5.5, 4, 2.9, 1)   # Background color when pressed
        self.bind(state=self.on_state_changed)

    def on_state_changed(self, instance, value):
        if value == 'down':
            # Animate the background color change when pressed
            anim = Animation(background_color=self.background_color_down, duration=1)
            anim.start(self)
        else:
            # Animate back to the normal background color when released
            anim = Animation(background_color=self.background_color_normal, duration=6)
            anim.start(self)

class ExamRegistrationApp(App):
    def build(self):
        self.title = 'Exam Registration'
        self.layout = BoxLayout(orientation='vertical')
        self.registered_students = self.load_registered_students()  # Load registered students from file
        
        # Create widgets with shiny button effect
        self.register_button = ShiningButton(text='Register Students')
        self.register_button.bind(on_release=self.show_registration_form_with_animation)
        self.options_button = ShiningButton(text='Options')
        self.options_button.bind(on_release=self.show_options_popup_with_animation)
        self.output_label = Label(text='Output will appear here')
        self.print_button = ShiningButton(text='Print Registration Form')
        self.print_button.bind(on_release=self.print_registration_form_with_animation)
        
        # Add widgets to the layout
        self.layout.add_widget(self.register_button)
        self.layout.add_widget(self.options_button)
        self.layout.add_widget(self.output_label)
        self.layout.add_widget(self.print_button)
        
        return self.layout

    def show_registration_form_with_animation(self, instance):
        # Animate the button before showing the registration form
        anim = Animation(background_color=self.register_button.background_color_normal, duration=1)
        anim.bind(on_complete=lambda instance, value: self.show_registration_form(instance))
        anim.start(self.register_button)

    def show_options_popup_with_animation(self, instance):
        # Animate the button before showing the options popup
        anim = Animation(background_color=self.options_button.background_color_normal, duration=1)
        anim.bind(on_complete=lambda instance, value: self.show_options_popup(instance))
        anim.start(self.options_button)

    def print_registration_form_with_animation(self, instance):
        # Animate the button before printing the registration form
        anim = Animation(background_color=self.print_button.background_color_normal, duration=1)
        anim.bind(on_complete=lambda instance, value: self.print_registration_form(instance))
        anim.start(self.print_button)

    def show_registration_form(self, instance):
        registration_layout = BoxLayout(orientation='vertical', padding=10)
        
        name_label = Label(text='Enter student name:')
        self.name_input = TextInput()
        id_label = Label(text='Student ID:')
        self.student_input = TextInput()
        self.student_input.text = str(random.randint(1, 10000))  # Generate a random student ID
        self.student_input.readonly = True  # Make the student ID input read-only
        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.register_student)
        close_button = Button(text='Close')
        close_button.bind(on_press=self.close_registration_form)
        
        registration_layout.add_widget(name_label)
        registration_layout.add_widget(self.name_input)
        registration_layout.add_widget(id_label)
        registration_layout.add_widget(self.student_input)
        registration_layout.add_widget(submit_button)
        registration_layout.add_widget(close_button)
        
        # Adjust the 'pos_hint' to position the window higher on the screen
        registration_popup = Popup(title='Registration Form', content=registration_layout,
                                size_hint=(None, None), size=(400, 300), auto_dismiss=False)
        registration_popup.pos_hint = {'center_x': 0.5, 'center_y': 0.7}  # Adjust 'center_y' to your desired position
        registration_popup.open()

        
    def close_registration_form(self, instance):
        # Close the registration form popup
        self.root_window.children[0].dismiss()
        
    def register_student(self, instance):
        name_input_text = self.name_input.text.strip()
        student_input_text = self.student_input.text.strip()

        if not name_input_text or not student_input_text:
            self.output_label.text = 'Please enter both a valid name and student ID.'
            return

        # Use regular expressions to validate the name input
        if not re.match("^[A-Za-z]*$", name_input_text):
            error_message = 'Invalid input. Name should only contain letters.\n'
            self.write_to_error_log(error_message)
            self.output_label.text = error_message
            return

        try:
            student_id = int(student_input_text)
            if student_id in self.registered_students:
                self.output_label.text = f'Student with ID: {student_id} is already registered.'
            else:
                self.registered_students[student_id] = name_input_text  # Add to the dictionary of registered students
                self.output_label.text = f'Student Name: {name_input_text.upper()}\nStudent ID: {student_id}\n\nregistered successfully.'

                # Write the registration info to the "reg_form.txt" file only if it doesn't already exist
                with open('reg_form.txt', 'a', encoding='utf-8') as reg_file:
                    reg_file.write(f"{name_input_text}, {student_id}\n")

        except ValueError as ve:
            error_message = f'Invalid input. Please enter a valid student ID: {str(ve)}\n'
            self.write_to_error_log(error_message)
            self.output_label.text = error_message


    def show_options_popup(self, instance):
        options_popup = Popup(title='Options', size_hint=(None, None), size=(300, 200), auto_dismiss=False)
        options_layout = BoxLayout(orientation='vertical', padding=10)

        view_reg_button = Button(text='View Registration Log')
        clear_reg_button = Button(text='Clear Registration Log')
        view_error_button = Button(text='View Error Log')
        clear_error_button = Button(text='Clear Error Log')

        # Add a close button to the options menu
        close_button = Button(text='Close')
        close_button.bind(on_press=lambda instance: options_popup.dismiss())

        view_reg_button.bind(on_press=lambda instance: self.view_log('reg_form.txt', 'Registration Log'))
        clear_reg_button.bind(on_press=lambda instance: self.clear_log('reg_form.txt', 'Registration Log'))
        view_error_button.bind(on_press=lambda instance: self.view_log('error_log.txt', 'Error Log'))
        clear_error_button.bind(on_press=lambda instance: self.clear_log('error_log.txt', 'Error Log'))

        options_layout.add_widget(view_reg_button)
        options_layout.add_widget(clear_reg_button)
        options_layout.add_widget(view_error_button)
        options_layout.add_widget(clear_error_button)

        # Add the close button to the options menu
        options_layout.add_widget(close_button)

        options_popup.content = options_layout
        options_popup.open()


    def print_registration_form(self, instance):
        pdf_filename = 'registration_form.pdf'
        try:
            # Generate a PDF document
            c = canvas.Canvas(pdf_filename, pagesize=letter)
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Registration Form")
            c.drawString(100, 720, "-----------------------------")

            # Read and write student information from the "reg_form.txt" file
            y_offset = 690
            with open('reg_form.txt', 'r', encoding='utf-8') as reg_file:
                for line in reg_file:
                    student_info = line.strip().split(',')
                    if len(student_info) == 2:
                        student_name, student_id = student_info
                        c.drawString(100, y_offset, f"Student Name: {student_name}")
                        c.drawString(100, y_offset - 20, f"Student ID: {student_id}")
                        c.drawString(100, y_offset - 40, "Please sign here: .................")
                        y_offset -= 60  # Adjust the y offset for the next student

            c.save()

            # Print the PDF using the default PDF viewer
            os.system(f'start {pdf_filename}')

            self.output_label.text = 'Registration form printed successfully.'
        except Exception as e:
            self.output_label.text = f'Error printing registration form: {str(e)}'

    def view_log(self, log_filename, title):
        try:
            with open(log_filename, 'r', encoding='utf-8') as file:
                log_contents = file.read()
                log_scroll = ScrollView(
                    size_hint=(None, None),
                    size=(400, 400),
                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                log_text_input = TextInput(
                    readonly=True,
                    text=log_contents,
                    size_hint=(None, None),
                    size=(400, 400),
                    multiline=True,
                )
                log_scroll.add_widget(log_text_input)

                close_button = Button(text='Close', size_hint=(1, None), height=40)
                close_button.bind(on_release=lambda instance: popup.dismiss())

                content_layout = BoxLayout(orientation='vertical')
                content_layout.add_widget(log_scroll)
                content_layout.add_widget(close_button)

                popup = Popup(title=title, content=content_layout, size_hint=(None, None), size=(400, 440))
                popup.open()
        except FileNotFoundError:
            self.output_label.text = f'{log_filename} not found.'

    def clear_log(self, log_filename, title):
        try:
            with open(log_filename, 'w', encoding='utf-8') as file:
                file.write('')
            self.output_label.text = f'{log_filename} cleared successfully.'
        except Exception as e:
            self.output_label.text = f'Error clearing {log_filename}: {str(e)}'

    def write_to_error_log(self, message):
        try:
            with open("error_log.txt", 'a') as file:
                file.write(message)
            # Display the error message in the app's output_label
            self.output_label.text = f'Error: {message}'
        except Exception as e:
            self.output_label.text = f'Error writing to error log: {str(e)}'


    def load_registered_students(self):
        # Load registered students from the "reg_form.txt" file
        registered_students = {}
        try:
            with open('reg_form.txt', 'r', encoding='utf-8') as reg_file:
                for line in reg_file:
                    student_info = line.strip().split(',')
                    if len(student_info) == 2:
                        student_name, student_id = student_info
                        registered_students[int(student_id)] = student_name
        except FileNotFoundError:
            pass  # If the file doesn't exist yet, return an empty dictionary
        return registered_students

if __name__ == '__main__':
    ExamRegistrationApp().run()
