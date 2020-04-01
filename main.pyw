import PySimpleGUI as sg
from Py_env import Py_env

class Gui():

    def main_gui(self):

        layout = [
                    [sg.Listbox(values=Py_env().list_env(), key='lista', size=(30, 6))],
                    [sg.Text('virtual environment'), sg.InputText(key='entorno')],
                    [sg.Button('Create'), sg.Button('Activate'), sg.Button('Eliminate')]
                ]
        
        window = sg.Window('Virtualenv GUI', layout)

        while True:             

            event, values = window.read()

            print(values)

            if values['entorno'] != '' and event == 'Create':
                Py_env().create_env(values['entorno'])
            elif event == 'Activate':

                if values['lista'] != '' and len(values['lista'])==1:
                    Py_env().activate_env(values['lista'][0])
                elif values['entorno'] != '':
                    Py_env().activate_env(values['entorno'])
                else:
                    sg.popup('Fill in the parameters ')   

            elif event == 'Eliminate':

                if values['lista'] != '' and len(values['lista'])==1:
                    Py_env().eliminate_env(values['lista'][0])
                elif values['entorno'] != '':
                    Py_env().eliminate_env(values['entorno'])
                else:
                    sg.popup('Fill in the parameters ')  

            else:
                sg.popup('Fill in the parameters ')     

            window.FindElement('lista').Update(values=Py_env().list_env())

            if event in (None, 'Cancel'):
                break

        window.close()

if __name__ == '__main__':
    Gui().main_gui()