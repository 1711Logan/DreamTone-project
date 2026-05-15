import os
import time
from jnius import autoclass
from kivy.storage.jsonstore import JsonStore

MediaPlayer = autoclass('android.media.MediaPlayer')
TelephonyManager = autoclass('android.telephony.TelephonyManager')
Context = autoclass('android.content.Context')
PythonService = autoclass('org.kivy.android.PythonService')

service = PythonService.mService
base_dir = os.path.dirname(os.path.abspath(__file__))
store = JsonStore(os.path.join(base_dir, 'config.json'))

def play_audio(ruta):
    try:
        if os.path.exists(ruta):
            mPlayer = MediaPlayer()
            mPlayer.setDataSource(ruta)
            mPlayer.prepare()
            mPlayer.start()
    except Exception as e:
        print(f"Error: {e}")

while True:
    try:
        tm = service.getSystemService(Context.TELEPHONY_SERVICE)
        estado = tm.getCallState()
        if estado == TelephonyManager.CALL_STATE_RINGING:
            if store.exists('paths'):
                ruta_tono = store.get('paths').get('entrada')
                if ruta_tono:
                    play_audio(ruta_tono)
                    time.sleep(15) 
    except:
        pass
    time.sleep(1)