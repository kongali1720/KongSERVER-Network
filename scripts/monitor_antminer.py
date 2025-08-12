import requests

ANTMINER_IP = "192.168.1.xx"

def get_status(ip):
    try:
        r = requests.get(f"http://{ip}/cgi-bin/minerStatus.cgi", timeout=5)
        if r.status_code == 200:
            print("Status Antminer:")
            print(r.text)
        else:
            print(f"Gagal akses Antminer: {r.status_code}")
    except Exception as e:
        print("Error:", e)

get_status(ANTMINER_IP)
