import npyscreen as scr
#comment
class InvalidPassword(scr.Popup):
    def create(self):
        self.msg = self.add(scr.Textfield, 'msg', value='Invalid credentials')
    def afterEditing(self):
        self.parentApp.setNextFormPrevious()

class SetupForm(scr.Form):
    OK_BUTTON_TEXT = "Start"
    def create(self):
        self.add(scr.FixedText, value="Select the IO units installed on Raspberry GPIO")
        self.I2CBoardsChoice = self.add(scr.MultiSelect, name = 'i2c_boards', values=['GYRO', 'ADC', 'DAC', 'BME280', 'INA219', 'GPS', 'PROXIMITY SENSOR'], max_height=8)
        self.start_server = self.add(scr.MultiSelect, name="server", values=['Start Server?'], max_height=2)
        self.pollingInterval = self.add(scr.TitleText, name='Interval', value='500')
    def afterEditing(self):
        self.parentApp.setNextForm(None)

class LoginForm(scr.Popup):
    def create(self):
        self.name = 'Login Form'
        self.user_name = self.add(scr.TitleText, 'user_name', name='User name:')
        self.password = self.add(scr.TitlePassword,'password', name='Password')
    def afterEditing(self):
        if self.user_name.value == "denis" and self.password.value=='':
            self.parentApp.setNextForm('SETUP')
        else:
            print('Invalid username or password')
            self.parentApp.error = self.user_name.value
            self.parentApp.setNextForm('ERROR')

class SensorsApp (scr.NPSAppManaged):
    def onStart(self):
        self.error = "hello"
        self.addForm('MAIN', LoginForm)
        self.addForm('SETUP', SetupForm)
        #self.addForm('DETAILS', DetailsForm)
        self.addForm('ERROR', InvalidPassword)

if __name__=='__main__':
    print ('Py Sensors Managing app...')
    app = SensorsApp()
    app.run()