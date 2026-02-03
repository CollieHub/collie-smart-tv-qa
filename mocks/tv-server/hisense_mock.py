import http.server
import socketserver
import json
import socket
from datetime import datetime

# Configuración
PORT_REST = 8091  # Puerto REST API de Hisense
PORT_MQTT = 36669 # Puerto MQTT de Hisense
IP_ADDRESS = socket.gethostbyname(socket.gethostname())

class HisenseMockHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🔍 Escaneo Hisense detectado desde: {self.client_address[0]}")
        
        # Simular respuesta de información de Hisense (REST)
        if self.path == "/api/v1/device/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "deviceName": "Hisense Smart TV Mock",
                "modelName": "HISENSE-U7-2026",
                "softwareVersion": "V0000.01.00A",
                "type": "Hisense TV"
            }
            self.wfile.write(json.dumps(response).encode())
            print(f"✅ Info Hisense enviada.")
        else:
            self.send_error(404)

    def do_POST(self):
        # Hisense suele usar POST para comandos vía REST o MQTT
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] ⌨️ Comando Hisense recibido.")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"result":"success"}')

def run_server():
    # Nota: Simulamos el puerto REST que es el que nuestra App busca primero en NetworkScanner.kt
    with socketserver.TCPServer(("", PORT_REST), HisenseMockHandler) as httpd:
        print("-" * 50)
        print(f"🚀 COLLIE SMART TV MOCK SERVER - ACTIVO")
        print(f"📺 Simulando: Hisense Smart TV")
        print(f"🌐 IP Local: {IP_ADDRESS}")
        print(f"🔌 Puerto REST: {PORT_REST}")
        print(f"🔌 Puerto MQTT (Simulado): {PORT_MQTT}")
        print("-" * 50)
        print("Esperando conexión de la App Collie (Hisense Driver)...")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
