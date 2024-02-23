import os
from sshtunnel import SSHTunnelForwarder

env_file = ".env"
tunnel = None


def get_env_variables(env_file):
    with open(env_file) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value


def start_tunnel(remote_server, remote_port, local_port):
    get_env_variables(env_file)
    ssh_username = os.getenv("IMAGINATION_USER")
    ssh_password = os.getenv("IMAGINATION_PASS")
    global tunnel
    tunnel = SSHTunnelForwarder(
        (remote_server, 22),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=("localhost", remote_port),
        local_bind_address=("localhost", local_port),
    )
    tunnel.start()
    print(f"Tunnel opened at localhost:{tunnel.local_bind_port}")


def stop_tunnel():
    """
    Stops the SSH tunnel
    """
    global tunnel
    if tunnel:
        tunnel.stop()
        print("Tunnel closed")
