import PySimpleGUI as sg
import wifi_qrcode_generator as qr

# Create a simple GUI window
# Collect the network name, password and security type from the user
layout = [[sg.Text('Network Name')],
          [sg.Input(key="ssid")],
          [sg.Text('Password')],
          [sg.Input(key="password")],
          [sg.Text('Security')],
          [sg.OptionMenu(['None', 'WPA', 'WEP'], default_value='None', key='security')],
          [sg.OK("Generate Code")] ]

window = sg.Window('WiFi QR Code Generator', layout)

event, values = window.read()

window.close()

# Print the values entered by the user
print ("network name: ", values["ssid"])
print ("password: ", values["password"])
print ("security: ", values["security"])


qr_code = qr.wifi_qrcode(values["ssid"], False, values["security"], values["password"])

# Generate QR code 
qr_image = qr_code.make_image(fill="black", back_color="white")

# Save the QR code as an image file
output_filename = "wifi_qr_code.png"
qr_image.save(output_filename)

# Show confirmation message
sg.popup(f"QR Code saved as {output_filename}", title="Success")

# Display the saved QR code in a new window
layout = [[sg.Text("Generated WiFi QR Code")], 
            [sg.Image(filename=output_filename)], 
            [sg.Button("Close")]]

window = sg.Window("QR Code", layout)
event, values = window.read()
window.close()