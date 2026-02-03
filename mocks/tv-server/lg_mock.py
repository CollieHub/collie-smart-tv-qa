import http.server
import socketserver
import json
import socket
from datetime import datetime

# Configuración
PORT = 3000  # Puerto estándar para LG webOS
IP_ADDRESS = socket.gethostbyname(socket.gethostname())

class LGwebOSMockHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🔍 Escaneo LG detectado desde: {self.client_address[0]}")
        
        # Simular respuesta de información de LG webOS
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "type": "webOS TV",
                "modelName": "LG-MOCK-OLED-2026",
                "version": "6.0.0",
                "sdkVersion": "1.2.0"
            }
            self.wfile.write(json.dumps(response).encode())
            print(f"✅ Respuesta LG enviada.")
        
        # Simular el endpoint de descripción XML que agregamos hoy para validación real
        elif self.path == "/description.xml":
            self.send_response(200)
            self.send_header('Content-type', 'text/xml')
            self.end_headers()
            xml_response = """<?xml version="1.0"?>
<root xmlns="urn:schemas-upnp-org:device-1-0">
  <specVersion><major>1</major><minor>0</minor></specVersion>
  <device>
    <deviceType>urn:schemas-upnp-org:device:Basic:1</deviceType>
    <friendlyName>LG WebOS TV Mock</friendlyName>
    <manufacturer>LG Electronics</manufacturer>
    <modelDescription>LG TV</modelDescription>
    <modelName>WEBOS6</modelName>
  </device>
</root>"""
            self.wfile.write(xml_response.encode())
            print(f"✅ XML de descripción enviado (Validación de LG real).")
        else:
            self.send_error(404)

    def do_POST(self):
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] ⌨️ Comando LG recibido desde: {self.client_address[0]}")
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print(f"📦 Payload (WebSocket/JSON): {post_data.decode()}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"returnValue":true}')

def run_server():
    with socketserver.TCPServer(("", PORT), LGwebOSMockHandler) as httpd:
        print("-" * 50)
        print(f"🚀 COLLIE SMART TV MOCK SERVER - ACTIVO")
        print(f"📺 Simulando: LG webOS")
        print(f"🌐 IP Local: {IP_ADDRESS}")
        print(f"🔌 Puerto: {PORT}")
        print("-" * 50)
        print("Esperando conexión de la App Collie (LG Driver)...")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
