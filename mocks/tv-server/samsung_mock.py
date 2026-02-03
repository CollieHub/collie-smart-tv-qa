import http.server
import socketserver
import json
import socket
from datetime import datetime

# Configuración
PORT = 8001  # Puerto estándar para Samsung Tizen
IP_ADDRESS = socket.gethostbyname(socket.gethostname())

class SmartTVMockHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Silenciar logs estándar para tener una consola limpia
        pass

    def do_GET(self):
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🔍 Escaneo detectado desde: {self.client_address[0]}")
        
        # Simular respuesta de información de la TV (Samsung estilo)
        if self.path == "/api/v2/":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "device": {
                    "name": "Collie Mock TV (Samsung Style)",
                    "model": "MOCK-2026",
                    "id": "mock-device-id-12345",
                    "type": "Samsung SmartTV"
                }
            }
            self.wfile.write(json.dumps(response).encode())
            print(f"✅ Respuesta de información enviada a la App.")
        else:
            self.send_error(404)

    def do_POST(self):
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] ⌨️ Comando recibido desde: {self.client_address[0]}")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print(f"📦 Datos del comando: {post_data.decode()}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

def run_server():
    with socketserver.TCPServer(("", PORT), SmartTVMockHandler) as httpd:
        print("-" * 50)
        print(f"🚀 COLLIE SMART TV MOCK SERVER - ACTIVO")
        print(f"📺 Simulando: Samsung Tizen")
        print(f"🌐 IP Local: {IP_ADDRESS}")
        print(f"🔌 Puerto: {PORT}")
        print("-" * 50)
        print("Esperando conexión de la App Collie...")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
