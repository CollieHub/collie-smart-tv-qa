import urllib.request
import json
import time

# Configuración: Simular App apuntando a LG
TARGET_IP = "127.0.0.1"
PORT_LG = 3000

def test_lg_discovery():
    print(f"--- 📱 Simulación de App: Escaneando LG Smart TV ---")
    
    # Pruebas de descubrimiento que hace la app de Collie
    endpoints = ["/", "/description.xml"]
    
    for path in endpoints:
        url = f"http://{TARGET_IP}:{PORT_LG}{path}"
        try:
            print(f"Probando endpoint: {url}...")
            with urllib.request.urlopen(url, timeout=2) as response:
                if response.getcode() == 200:
                    content = response.read().decode()
                    if "json" in response.getheader('Content-Type'):
                        data = json.loads(content)
                        print(f"✅ JSON Recibido: {data.get('modelName')}")
                    else:
                        print(f"✅ XML Recibido (Fragmento): {content[:50]}...")
        except Exception as e:
            print(f"❌ Error en {path}: {e}")

def test_lg_command():
    print(f"\n--- ⌨️ Simulación de App: Enviando COMANDO a LG ---")
    url = f"http://{TARGET_IP}:{PORT_LG}/"
    payload = {
        "type": "request",
        "uri": "ssap://system.notifications/createToast",
        "payload": {"message": "Hola desde Collie App"}
    }
    data = json.dumps(payload).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/json')
        with urllib.request.urlopen(req, timeout=2) as response:
            if response.getcode() == 200:
                print(f"✅ Comando LG enviado exitosamente.")
                print(f"💬 Respuesta LG: {response.read().decode()}")
    except Exception as e:
        print(f"❌ Falla en envío LG: {e}")

if __name__ == "__main__":
    test_lg_discovery()
    time.sleep(1)
    test_lg_command()
