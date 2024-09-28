from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested path is "/get-id"
        if self.path == '/get-id':
            # Get the client IP
            client_ip = self.client_address[0]

            # Log the client IP for debugging
            print(f"Client IP: {client_ip}")

            # Check if the IP starts with "128.16"
            if client_ip.startswith("128.166"):
                response_data = {"id": "0x622C03769C8F"}  # Replace with your actual ID logic
                self.send_response(200)
            else:
                response_data = {"ip": client_ip, "message": "IP does not match."}
                self.send_response(200)
        else:
            response_data = {"error": "Not Found"}
            self.send_response(404)

        # Send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the response as JSON
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
