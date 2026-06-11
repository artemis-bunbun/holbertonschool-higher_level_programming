#!/usr/bin/python3
"""Simple HTTP API server using http.server module."""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for a basic API."""

    def do_GET(self):
        """Route GET requests to appropriate handlers."""
        if self.path == "/":
            self._handle_root()
        elif self.path == "/data":
            self._handle_data()
        elif self.path == "/status":
            self._handle_status()
        else:
            self._handle_404()

    def _handle_root(self):
        """Return a simple text message."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def _handle_data(self):
        """Return sample JSON data."""
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _handle_status(self):
        """Return OK status."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def _handle_404(self):
        """Return 404 for undefined endpoints."""
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


def main():
    """Run the server on port 8000."""
    server = HTTPServer(("localhost", 8000), SimpleAPIHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
