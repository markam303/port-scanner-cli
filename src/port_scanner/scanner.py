"""TCP Port Scanner Module."""

import socket
import threading
from queue import Queue
from typing import Optional


CONNECTION_TIMEOUT = 1.0
BANNER_TIMEOUT = 2.0
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024
DEFAULT_NUM_THREADS = 100


def get_service_name(port: int) -> str:
    """Get standard service name for a port."""
    try:
        return socket.getservbyport(port)
    except OSError:
        return "unknown"


def banner_grab(host: str, port: int, timeout: float = BANNER_TIMEOUT) -> Optional[str]:
    """Attempt to grab banner from an open port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))
            return sock.recv(1024).decode("utf-8", errors="ignore").strip()
    except (socket.error, OSError):
        return None


def scan_port(
    host: str,
    port: int,
    lock: threading.Lock,
    results: list,
) -> None:
    """Scan a single port and store result."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(CONNECTION_TIMEOUT)
            result = sock.connect_ex((host, port))
            if result == 0:
                service = get_service_name(port)
                banner = banner_grab(host, port)
                with lock:
                    results.append(
                        {
                            "port": port,
                            "status": "open",
                            "service": service,
                            "banner": banner,
                        }
                    )
    except socket.error:
        pass


def thread_worker(
    host: str,
    port_queue: Queue,
    lock: threading.Lock,
    results: list,
) -> None:
    """Worker thread that processes ports from queue."""
    while True:
        port = port_queue.get()
        if port is None:
            port_queue.task_done()
            break
        scan_port(host, port, lock, results)
        port_queue.task_done()


def scan_ports(
    host: str,
    start_port: int = DEFAULT_START_PORT,
    end_port: int = DEFAULT_END_PORT,
    num_threads: int = DEFAULT_NUM_THREADS,
) -> list:
    """Scan a range of ports using worker threads."""
    port_queue: Queue = Queue()
    results: list = []
    lock = threading.Lock()

    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    for _ in range(num_threads):
        port_queue.put(None)

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(
            target=thread_worker,
            args=(host, port_queue, lock, results),
        )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return sorted(results, key=lambda x: x["port"])
