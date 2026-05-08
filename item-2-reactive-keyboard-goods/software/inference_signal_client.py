#!/usr/bin/env python3
"""Send a test inference signal to the local receiver."""
import argparse, json, urllib.request, time, socket

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--url',default='http://127.0.0.1:8765/signal'); ap.add_argument('--event',choices=['start','done','error'],required=True); ap.add_argument('--source',default='manual'); ap.add_argument('--run-id',default='test-run')
    a=ap.parse_args(); payload={'event':a.event,'source':a.source,'run_id':a.run_id,'host':socket.gethostname(),'sent_ts':time.time()}
    req=urllib.request.Request(a.url, data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
    print(urllib.request.urlopen(req, timeout=5).read().decode())
if __name__=='__main__': main()
