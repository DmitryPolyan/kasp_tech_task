from tech_task.parser import dicts_maker
from tech_task.parser import parse_file

example_result = {'as-block': 'AS30720 - AS30979',
                  'type': 'REGULAR',
                  'descr': 'RIPE NCC ASN block',
                  'remarks': 'These AS Numbers are further assigned to network\n' \
                             'operators in the RIPE NCC service region. AS\n' \
                             'assignment policy is documented in:\n' \
                             '<http://www.ripe.net/ripe/docs/asn-assignment.html>\n' \
                             'RIPE NCC members can request AS Numbers using the\n' \
                             'form located at:\n' \
                             '<http://lirportal.ripe.net/lirportal/liruser/resource_request/draw.html?name=as-number>\n' \
                             'data has been transferred from RIPE Whois Database 20050221',
                  'org': 'ORG-AFNC1-AFRINIC',
                  'admin-c': 'TEAM-AFRINIC',
                  'tech-c': 'TEAM-AFRINIC',
                  'mnt-by': 'AFRINIC-HM-MNT',
                  'mnt-lower': 'AFRINIC-HM-MNT',
                  'changed': '***@ripe.net 20031001\n' \
                             '***@ripe.net 20040421\n' \
                             '***@ripe.net 20050202\n' \
                             '***@afrinic.net 20050205',
                  'source': 'AFRINIC'}


def test_dicts_maker():
    path = 'tests/example.txt'
    with open(path, 'r') as file:
        assert dicts_maker(file)[0] == example_result


def test_parse_txt():
    path = 'tests/example.txt'
    assert parse_file(path)[0] == example_result


def test_parse_gzip():
    path = 'tests/file.txt.gz'
    assert parse_file(path)[0] == example_result
