import asyncio
import sys
import json
from pathlib import Path

def storm_gate():
    # 1. Baca input dari Engine Rust Storm
    # Contoh input: {"module": "email", "target": "target@gmail.com", "json_out": "result.json"}
    try:
        line = sys.stdin.readline()
        if not line:
            return
        data = json.loads(line)
    except Exception:
        return

    module = data.get("module")
    target = data.get("target")
    json_path = Path(data.get("json_out")) if data.get("json_out") else None

    # 2. Eksekusi Langsung ke Jantung GHunt
    match module:
        case "email":
            from ghunt.modules import email
            asyncio.run(email.hunt(None, target, json_path))
        case "gaia":
            from ghunt.modules import gaia
            asyncio.run(gaia.hunt(None, target, json_path))
        case "drive":
            from ghunt.modules import drive
            asyncio.run(drive.hunt(None, target, json_path))
        case "geolocate":
            from ghunt.modules import geolocate
            # geolocate butuh bssid atau file, sesuaikan input dari Storm
            asyncio.run(geolocate.main(None, target, None, json_path))
        case "login":
            from ghunt.modules import login
            asyncio.run(login.check_and_login(None, False))

if __name__ == "__main__":
    storm_gate()




