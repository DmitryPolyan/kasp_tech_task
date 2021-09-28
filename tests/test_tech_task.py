import unittest
# import pytest
from tech_task.parser import dicts_maker
from tech_task.parser import parse_file
from tech_task.parser import FileTypeNotSupported

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


# В задании указано использовать только стандартные библиотеки, но обычно для тестирования я использую pytest
class TestParsers(unittest.TestCase):
    def test_dicts_maker(self):
        path = 'tests/example.txt'
        with open(path, 'r') as file:
            self.assertEqual(dicts_maker(file)[0], example_result)

    def test_parse_txt(self):
        path = 'tests/example.txt'
        self.assertEqual(parse_file(path)[0], example_result)

    def test_parse_gzip(self):
        path = 'tests/file.txt.gz'
        self.assertEqual(parse_file(path)[0], example_result)

    def test_fail_not_found(self):
        path = 'tests/file.txtz'
        with self.assertRaises(FileNotFoundError) as e_info:
            parse_file(path)[0]

    def test_fail_not_supported(self):
        with self.assertRaises(FileTypeNotSupported) as e_info:
            path = 'tests/err.err'
            parse_file(path)[0]

# def test_dicts_maker():
#     path = 'tests/example.txt'
#     with open(path, 'r') as file:
#         assert dicts_maker(file)[0] == example_result
#
#
# def test_parse_txt():
#     path = 'tests/example.txt'
#     assert parse_file(path)[0] == example_result
#
#
# def test_parse_gzip():
#     path = 'tests/file.txt.gz'
#     assert parse_file(path)[0] == example_result
#
#
# def test_fail_not_found():
#     with pytest.raises(FileNotFoundError) as e_info:
#         path = 'tests/file.txtz'
#         parse_file(path)[0]
#
#
# def test_fail_not_supported():
#     with pytest.raises(FileTypeNotSupported) as e_info:
#         path = 'tests/err.err'
#         parse_file(path)[0]
