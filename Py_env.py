import os
from shutil import rmtree
import PySimpleGUI as sg

class Py_env():
    
    def create_env(self, name):

        if os.path.exists(name):
            sg.popup('The virtual environment already exists ')
        else:
            try:
                path = os.getcwd()

                os.mkdir(name)
                os.chdir(name)
                os.system("virtualenv env")
                os.chdir(path)
            except Exception as e:
                sg.popup(e)
    
    def list_env(self):

        envs = []

        for env_dir in os.listdir():
            
            if os.path.exists(f'{env_dir}\env'):
                envs.append(env_dir)

        return envs

    def activate_env(self, name):

        try:
            
            if os.path.exists(name):

                path = os.getcwd()

                os.chdir(name)
                os.system("start cmd /k env\Scripts\Activate.bat")

                os.chdir(path)
            else:
                sg.popup('The virtual environment does not exist ')
        except Exception as e:
            sg.popup(e)

    def eliminate_env(self, name):

        try:
            
            if os.path.exists(name):
                rmtree(name)
            else:
                sg.popup('The virtual environment does not exist ')
        except Exception as e:
            sg.popup(e)