import os
import socket
import ssl


def check_port(host: str, port: str) -> bool:
    """_summary_

    Args:
        host (str): the host to be connected to
        port (str): _description_

    Returns:
        bool: _description_
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()


def port_check(targets: list):
    for target in targets:
        host, port = target
        response = os.system(f"ping -c 1 {host}")
        if response == 0:
            print(f"{host} is up")
            if check_port(host, port):
                print(f"Port {port} on {host} is open")
            else:
                print(f"Port {port} on {host} is closed")
        else:
            print(f"{host} is down")


def check_ssl_certificate(host, port):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                certificate = ssock.getpeercert()
                return certificate
    except:
        return False
