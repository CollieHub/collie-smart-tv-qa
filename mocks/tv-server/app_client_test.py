import urllib.request
import urllib.parse
import json
import time

# Configuración del entorno de prueba
TARGET_IP = "127.0.0.1"
PORT = 8001 # Puerto de Samsung Mock

def test_app_discovery():
    print(f"--- 📱 Simulación de App: Escaneando Red ---")
    url = f"http://{TARGET_IP}:{PORT}/api/v2/"
    try:
        print(f"Buscando TV en {url}...")
        with urllib.request.urlopen(url, timeout=2) as response:
            if response.getcode() == 200:
                data = json.loads(response.read().decode())
                print(f"✅ ¡TV Encontrada!")
                print(f"📺 Nombre: {data['device']['name']}")
                return True
    except Exception as e:
        print(f"❌ Error en escaneo: {e}")
    return False

def test_send_command():
    print(f"\n--- ⌨️ Simulación de App: Enviando COMANDO ---")
    url = f"http://{TARGET_IP}:{PORT}/api/v2/"
    payload = {
        "command": "KEY_VOLDOWN",
        "timestamp": time.time()
    }
    data = json.dumps(payload).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/json')
        with urllib.request.urlopen(req, timeout=2) as response:
            if response.getcode() == 200:
                print(f"✅ Comando enviado exitosamente.")
                print(f"💬 Respuesta: {response.read().decode()}")
    except Exception as e:
        print(f"❌ Falla en envío: {e}")

if __name__ == "__main__":
    if test_app_discovery():
        time.sleep(1)
        test_send_command()
