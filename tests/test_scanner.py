"""Tests for port scanner module."""

import threading
from unittest.mock import patch

import pytest

from port_scanner.scanner import banner_grab, get_service_name, scan_port


class TestGetServiceName:
    """Tests for get_service_name function."""

    def test_standard_http_port(self):
        assert get_service_name(80) == "http"

    def test_standard_https_port(self):
        assert get_service_name(443) == "https"

    def test_standard_ssh_port(self):
        assert get_service_name(22) == "ssh"

    def test_unknown_port(self):
        assert get_service_name(12345) == "unknown"


class TestBannerGrab:
    """Tests for banner_grab function."""

    @patch("port_scanner.scanner.socket.socket")
    def test_banner_grab_success(self, mock_socket):
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.recv.return_value = b"SSH-2.0-OpenSSH_8.0\r\n"

        result = banner_grab("127.0.0.1", 22)

        assert result == "SSH-2.0-OpenSSH_8.0"

    @patch("port_scanner.scanner.socket.socket")
    def test_banner_grab_timeout(self, mock_socket):
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.recv.side_effect = TimeoutError()

        result = banner_grab("127.0.0.1", 22)

        assert result is None


class TestScanPort:
    """Tests for scan_port function."""

    @patch("port_scanner.scanner.socket.socket")
    def test_scan_port_open(self, mock_socket):
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.connect_ex.return_value = 0

        results = []
        lock = threading.Lock()

        with patch("port_scanner.scanner.banner_grab", return_value=None):
            scan_port("127.0.0.1", 80, lock, results)

        assert len(results) == 1
        assert results[0]["port"] == 80
        assert results[0]["status"] == "open"
        assert results[0]["service"] == "http"

    @patch("port_scanner.scanner.socket.socket")
    def test_scan_port_closed(self, mock_socket):
        mock_sock = mock_socket.return_value.__enter__.return_value
        mock_sock.connect_ex.return_value = 1

        results = []
        lock = threading.Lock()

        scan_port("127.0.0.1", 80, lock, results)

        assert len(results) == 0
