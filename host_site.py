import os
import http.server
import socketserver
import threading

PORT = 8000
DIRECTORY = "docs"

os.chdir(DIRECTORY)

Handler = http.server.SimpleHTTPRequestHandler

# Use ThreadingMixIn for responsiveness to shutdown
class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

httpd = ThreadingHTTPServer(("", PORT), Handler)

def run_server():
    print(f"Serving at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except Exception as e:
        print(f"Server error: {e}")

# Run in a separate thread to make KeyboardInterrupt work
server_thread = threading.Thread(target=run_server)
server_thread.start()

try:
    while True:
        pass  # keep main thread alive
except KeyboardInterrupt:
    print("\nShutting down server...")
    httpd.shutdown()
    server_thread.join()
    print("Server stopped.")
