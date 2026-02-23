from pathlib import Path
import json

project_list = ['script', 'backend', 'data/ai']

option_value = 1
folder_name = ""
directory_name = Path("/Users/ibandasca/Documents/Coding/Python")

print("Select the project type:")

for i in project_list:
    print("%s.- %s" % (option_value, i))
    option_value += 1

def select_option():
    while True:
        try:
            option = int(input("\nOption: "))
        except ValueError:
            print("\nInvalid option (out of range)")
            continue

        if not (1 <= option <= len(project_list)):
            print("\nInvalid option (out of range)")
            continue
        return option
    
option = select_option()

def setup_folder(value):
    folder_name = value.replace(" ", "_")

    project_folder= directory_name / folder_name
    project_folder.mkdir(parents=True, exist_ok=True)

    file_path = project_folder / f"{folder_name}.py"
    file_path.write_text("")
    return

def project_setup():
    value = input("Script or project Nname: ").strip().lower()
    setup_folder(value)
    return

def create_script_file():
    print("Creationg an script project...")
    project_setup()
    return

def create_bakend_project():
    print("Creationg a Backend project...")
    project_setup()
    return

def create_data_ai_project():
    print("Creationg a Data/IA project...")
    project_setup()
    return

if option == 1:
    create_script_file()
if option == 2:
    create_bakend_project()
if option == 3:
    create_data_ai_project()



