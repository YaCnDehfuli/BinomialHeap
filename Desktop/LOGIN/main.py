from os import name
from typing import Text
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import json
from functools import partial
from kivy.clock import Clock

# class pop(Screen):
#     pass

Window.size = (510, 610)


class windowsManager(ScreenManager):
    pass

# class Floors_page(Screen):
#     view = ObjectProperty(None)
#     def __init__(self, **kwargs):
#         super(Floors_page, self).__init__(**kwargs)
#         Clock.schedule_once(self.create_scrollview)
                        
#     def check(self,id,name):
#         if(id==13):
#             sm.current = 'Family_page'
#         elif (id==12):
#             sm.current = 'Watch_page'
            
#     def create_scrollview(self, dt):
#         layout = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=0.3, pos_hint={"x":0.4} )
#         layout.bind(minimum_height=layout.setter("height"))  
#         f = open ('floors.json', "r")
#         data = json.loads(f.read())
#         floor_names = []
#         room_names = []
#         room_ids = []
#         for i in data['floors']:
#             floor_names.append(i['floor_name'])
#             room_names.append(i['room_names'])
#             room_ids.append(i['room_ids'])
#         print(room_ids[2][2])
#         now_top = 0.95
#         for i in range(len(floor_names)):
#             now_top -= 0.07
#             lbl = Label(text = floor_names[i],size_hint = (0.1,None))#, pos_hint = {"x":0.37,"top":now_top})
#             layout.add_widget(lbl)
#             for j in range(len(room_names[i])):
#                 now_top -= 0.05
#                 btn = Button(text = room_names[i][j], background_color= (0, 0, 0, 0), size_hint = (0.1,None))#, pos_hint= {"x":0.4,"top":now_top})
#                 btn.bind(on_release=partial(self.check,room_ids[i][j]))
#                 layout.add_widget(btn)  
        # scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        # scrollview.add_widget(layout)
        # self.view.add_widget(scrollview)    

class Floors_page(Screen):
    def __init__(self, **kwargs):
        super(Floors_page, self).__init__(**kwargs)
        f = open ('JSON/floors.json', "r")
        data = json.loads(f.read())
        floor_names = []
        room_names = []
        room_ids = []
        for i in data['floors']:
            floor_names.append(i['floor_name'])
            room_names.append(i['room_names'])
            room_ids.append(i['room_ids'])

        now_top = 0.95
        for i in range(len(floor_names)):
            now_top -= 0.07
            lbl = Label(text = floor_names[i],size_hint = (0.1,0.07), pos_hint = {"x":0.37,"top":now_top})
            self.add_widget(lbl)
            for j in range(len(room_names[i])):
                now_top -= 0.05
                btn = Button(text = room_names[i][j], background_color= (0, 0, 0, 0), size_hint = (0.1,0.07), pos_hint= {"x":0.4,"top":now_top})
                btn.bind(on_release=partial(self.check,room_ids[i][j]))
                self.add_widget(btn)
    
    def check(self,id,name):
        if(id==13):
            sm.current = 'Family_page'
        elif (id==21):
            sm.current = 'Family_page'
        elif  (id==31):
            sm.current = 'Family_page'
            

class Floors_page1(Screen):
    pass
class Family_page(Screen):
    def __init__(self, **kwargs):
        super(Family_page, self).__init__(**kwargs)
        f = open ('JSON/Family.json', "r")
        data = json.loads(f.read())
        button_names = []
        button_ids = []
        print(data['Buttons'])
        for i in data['Buttons']:
            button_names.append(i['button_name'])
            button_ids.append(i['id'])
        now_top = 0.85
        now_x = 0.36  
        for j in range(len(button_names)):
            btn = Button(text = button_names[j], size_hint = (0.1,0.07), pos_hint= {"x":now_x,"top":now_top})
            btn.bind(on_release=partial(self.check,button_ids[j]))
            self.add_widget(btn)
            if(j%2==0):
                now_x += 0.2
            else:
                now_x -= 0.2
                now_top -= 0.15
    def check(self,id,name):
        if(id==1):
            sm.current = 'Watch_page'    
    
    
    
class Watch_page(Screen):
    def __init__(self, **kwargs):
        super(Watch_page, self).__init__(**kwargs)
        f = open ('JSON/watch.json', "r")
        data = json.loads(f.read())
        item_names = []
        item_ids = []
        print(data['items'])  
        for i in data['items']:
            item_names.append(i['item_name'])
            item_ids.append(i['id'])
        now_top = 0.85 
        for j in range(len(item_names)):
            btn = Button(text =  item_names[j], size_hint = (0.1,0.07),background_color= (0, 0, 0, 0), pos_hint= {"x":0.4,"top":now_top})
            btn.bind(on_release=partial(self.check,item_ids[j]))
            self.add_widget(btn)
            now_top -= 0.07
    
    def check(self,id,name):
        if(id==1):
            sm.current = 'Apple_TV_page'
        elif(id==2):
            sm.current = 'Camera_page'  
        elif(id==3):
            sm.current = 'DVD_page'  
        elif(id==4):
            sm.current = 'Cable_box_page'  
        elif(id==5):
            sm.current = 'Android_box_page'  
    
class Apple_TV_page(Screen):
    pass
class Cable_box_page(Screen):
    pass
class Android_box_page(Screen):
    pass
class DVD_page(Screen):
    pass
class Camera_page(Screen):
    pass

class login(Screen):
 
    username = ObjectProperty(None)
    password = ObjectProperty(None)
        
    def check(self):
        if self.ids.password.text == 'admin' and self.ids.username.text == 'admin' :
            sm.current = 'Floors_page'

        self.ids.username.text = ""
        self.ids.password.text = ""
    
    

kv = Builder.load_file('mainpage.kv')
sm = windowsManager()
# sm = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
# sm=Floors_page()
# sm.add_widget(login(name='login'))
sm.add_widget(Floors_page(name ='Floors_page'))
sm.add_widget(Floors_page1(name='Floors_page1'))
sm.add_widget(Family_page(name='Family_page'))
sm.add_widget(Watch_page(name='Watch_page'))
sm.add_widget(Apple_TV_page(name='Apple_TV_page'))
sm.add_widget(Cable_box_page(name='Cable_box_page'))
sm.add_widget(Android_box_page(name='Android_box_page'))
sm.add_widget(DVD_page(name='DVD_page'))
sm.add_widget(Camera_page(name='Camera_page'))


class homeApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    homeApp().run()
