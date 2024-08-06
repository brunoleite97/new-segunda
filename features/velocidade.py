import speedtest

try:
    st = speedtest.Speedtest()
except:
    print("Please check your internet connection.")
    st = None

def velocidade_de_download():
    if st:
        down = round(st.download() / 10 ** 6, 2)
        return down
    else:
        return None

def velocidade_de_upload():
    if st:
        up = round(st.upload() / 10 ** 6, 2)
        return up
    else:
        return None

def ping():
    if st:
        servernames = []
        st.get_servers(servernames)
        results = st.results.ping
        return results
    else:
        return None

def speed_test(*args, **kwargs):
    try:
        print("Checking internet speed. Please wait...")
        download_speed = velocidade_de_download()
        upload_speed = velocidade_de_upload()
        ping_time = ping()
        
        if download_speed is not None and upload_speed is not None and ping_time is not None:
            return f"Velocidade de download: {download_speed} MB/s\nVelocidade de Upload: {upload_speed} MB/s\nPing: {ping_time} ms"
        else:
            return "Unable to perform speed test. Please check your internet connection."
    except Exception as e:
        print(e)
        return "Error in internet speed test"

if __name__ == '__main__':
    print(speed_test())
