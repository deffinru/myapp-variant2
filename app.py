from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data_file = '/app/data/data.txt'
        # Записываем время запроса в файл
        with open(data_file, 'a') as f:
            f.write(f"Запрос: {datetime.datetime.now()}\n")
        
        # Читаем историю
        with open(data_file, 'r') as f:
            content = f.read()
            
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(f"Привет! Версия 0.9.0 работает.\n\nИстория:\n{content}".encode('utf-8'))

if __name__ == '__main__':
    os.makedirs('/app/data', exist_ok=True)
    server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
    print("Сервер запущен...")
    server.serve_forever()
