import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.storage.jsonstore import JsonStore
from plyer import filechooser

class DreamToneInterface(BoxLayout):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.store = JsonStore('config.json')

    def elegir_archivo(self, clave_config):
        filechooser.open_file(
            title="Selecciona un archivo MP3",
            filters=[("Audio", "*.mp3")],
            on_selection=lambda seleccion: self.guardar_ruta(clave_config, seleccion)
        )

    def guardar_ruta(self, clave_config, seleccion):
        if seleccion:
            ruta = seleccion[0]
            if self.store.exists('paths'):
                datos = self.store.get('paths')
            else:
                datos = {"entrada": "", "apertura": ""}
            datos[clave_config] = ruta
            self.store.put('paths', **datos)

class DreamToneApp(App):
    def build(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            # Aquí he corregido los permisos para que Android los acepte sin errores
            request_permissions([
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_PHONE_STATE,
                Permission.MODIFY_AUDIO_SETTINGS
            ])
        return DreamToneInterface()
if __name__ == '__main__':
    DreamToneApp().run()