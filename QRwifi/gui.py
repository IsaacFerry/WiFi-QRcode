import PySimpleGUI as sg

layout = [[sg.Text('Network Name')],
          [sg.Input(key="ssid")],
          [sg.Text('Password')],
          [sg.Input(key="password")],
          [sg.Text('Security')],
          [sg.OptionMenu(['None', 'WPA/WPA2', 'WEP'], default_value='None', key='security')],
          [sg.OK("Generate Code")] ]

window = sg.Window('WiFi QR Code Generator', layout)

event, values = window.read()

window.close()

print ("network name: ", values["ssid"])
print ("password: ", values["password"])
print ("security: ", values["security"])