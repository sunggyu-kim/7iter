#!/usr/bin/env python3
"""Minimal HTTP receiver for inference start/done signals.

POST /signal with JSON:
  {"source":"openclaw|codex|openai|manual", "event":"start|done|error", "run_id":"..."}
GET /health returns ok.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse, json, time
from pathlib import Path

class Handler(BaseHTTPRequestHandler):
    log_path = Path('item-2-reactive-keyboard-goods/software/inference_signal_events.jsonl')
    def _send(self, code, payload):
        body=json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        if self.path.startswith('/health'): self._send(200, {'ok': True, 'service':'inference-signal-server'})
        else: self._send(404, {'ok': False, 'error':'not_found'})
    def do_POST(self):
        if not self.path.startswith('/signal'):
            self._send(404, {'ok': False, 'error':'not_found'}); return
        n=int(self.headers.get('Content-Length','0') or 0)
        try: data=json.loads(self.rfile.read(n) or b'{}')
        except Exception as e: self._send(400, {'ok':False,'error':str(e)}); return
        event={'ts':time.time(),'client':self.client_address[0],**data}
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open('a', encoding='utf-8') as f: f.write(json.dumps(event, ensure_ascii=False)+chr(10))
        self._send(200, {'ok': True, 'received': event})
    def log_message(self, fmt, *args):
        return

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--host',default='127.0.0.1'); ap.add_argument('--port',type=int,default=8765)
    a=ap.parse_args(); print(f'listening http://{a.host}:{a.port}'); HTTPServer((a.host,a.port), Handler).serve_forever()
if __name__=='__main__': main()
