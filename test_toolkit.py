from log_parser import parse_failed_ssh_ips_from_lines


def test_parse_failed_ssh_ips_counts_exact_ips() -> None:
    lines = [
        "May  8 14:01:02 srv sshd[1201]: Failed password for invalid user admin from 192.168.1.45 port 54321 ssh2",
        "May  8 14:01:08 srv sshd[1203]: Failed password for root from 203.0.113.10 port 49812 ssh2",
        "May  8 14:02:11 srv sshd[1210]: Accepted password for nacho from 192.168.1.20 port 51234 ssh2",
        "May  8 14:03:22 srv sshd[1218]: Failed password for invalid user test from 192.168.1.45 port 54322 ssh2",
        "May  8 14:04:09 srv sshd[1225]: Failed password for ubuntu from 198.51.100.23 port 60111 ssh2",
    ]

    failed_ips, failed_counts = parse_failed_ssh_ips_from_lines(lines)

    assert failed_ips == {"192.168.1.45", "203.0.113.10", "198.51.100.23"}
    assert failed_counts == {
        "192.168.1.45": 2,
        "203.0.113.10": 1,
        "198.51.100.23": 1,
    }


def test_parse_failed_ssh_ips_ignores_lines_without_failed_password() -> None:
    lines = [
        "May  8 14:02:11 srv sshd[1210]: Accepted password for nacho from 192.168.1.20 port 51234 ssh2",
        "May  8 14:04:51 srv sshd[1230]: Accepted publickey for deploy from 198.51.100.50 port 44321 ssh2",
        "May  8 14:05:10 srv sudo: nacho : TTY=pts/0 ; COMMAND=/usr/bin/apt update",
    ]

    failed_ips, failed_counts = parse_failed_ssh_ips_from_lines(lines)

    assert failed_ips == set()
    assert failed_counts == {}
