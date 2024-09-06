# -*- coding: utf-8 -*-

GET_NETWORK_NSM_DEVICE_PAYLOAD = {
    'data': {
        'devices': [
            {
                'band': '5G',
                'connection': 'wifi',
                'current_rate': 144,
                'dev_type': 'others',
                'hostname': 'TV',
                'ip6_addr': '',
                'ip_addr': '10.10.10.244',
                'is_baned': True,
                'is_beamforming_on': False,
                'is_guest': False,
                'is_high_qos': False,
                'is_low_qos': False,
                'is_manual_dev_type': False,
                'is_manual_hostname': True,
                'is_online': True,
                'is_parental_controled': False,
                'is_qos': False,
                'is_wireless': True,
                'mac': '7c:92:e5:1f:b7:0a',
                'max_rate': 300,
                'rate_quality': 'middle',
                'signalstrength': 86,
                'transferRXRate': 142,
                'transferTXRate': 299
            },
            {
                'connection': 'ethernet',
                'dev_type': 'nas',
                'hostname': 'DiskStation',
                'ip6_addr': '',
                'ip_addr': '10.10.10.253',
                'is_baned': False,
                'is_beamforming_on': False,
                'is_high_qos': False,
                'is_low_qos': False,
                'is_manual_dev_type': False,
                'is_manual_hostname': True,
                'is_online': True,
                'is_parental_controled': False,
                'is_qos': False,
                'is_wireless': False,
                'mac': 'a8:9b:32:8e:a0:13'
            },
            {
                'connection': 'ethernet',
                'dev_type': 'computer',
                'hostname': 'Computer',
                'ip6_addr': '',
                'ip_addr': '10.10.10.250',
                'is_baned': False,
                'is_beamforming_on': False,
                'is_high_qos': False,
                'is_low_qos': False,
                'is_manual_dev_type': True,
                'is_manual_hostname': True,
                'is_online': False,
                'is_parental_controled': False,
                'is_qos': False,
                'is_wireless': False,
                'mac': 'db:52:70:85:8e:3a'
            }
        ],
        'exceed_dev_list_max': False
    },
    'success': True
}

GET_SYSTEM_UTILIZATION_PAYLOAD = {
    'data': {
        'cpu': {
            '15min_load': 8,
            '1min_load': 19,
            '5min_load': 9,
            'device': 'System',
            'other_load': 1,
            'system_load': 6,
            'user_load': 1
        },
        'disk': {
            'disk': [],
            'total': {
                'device': 'total',
                'read_access': 0,
                'read_byte': 0,
                'utilization': 0,
                'write_access': 0,
                'write_byte': 0
            }
        },
        'memory': {
            'avail_real': 109484,
            'avail_swap': 260332,
            'buffer': 67712,
            'cached': 122960,
            'device': 'Memory',
            'memory_size': 524288,
            'real_usage': 36,
            'si_disk': 0,
            'so_disk': 0,
            'swap_usage': 0,
            'total_real': 471324,
            'total_swap': 262140
        },
        'network': [
            {
                'device': 'total',
                'rx': 41741,
                'tx': 42506
            },
            {
                'device': 'bwlan0',
                'rx': 0,
                'tx': 0
            },
            {
                'device': 'bwlan1',
                'rx': 0,
                'tx': 0
            },
            {
                'device': 'eth0',
                'rx': 37766,
                'tx': 4359
            },
            {
                'device': 'lbr0',
                'rx': 3975,
                'tx': 38147
            }
        ],
        'space': {
            'lun': [],
            'total': {
                'device': 'total',
                'read_access': 0,
                'read_byte': 0,
                'utilization': 0,
                'write_access': 0,
                'write_byte': 1265
            },
            'volume': [
                {
                    'device': 'mmcblk0p6',
                    'display_name': 'volume1',
                    'read_access': 0,
                    'read_byte': 0,
                    'utilization': 0,
                    'write_access': 0,
                    'write_byte': 1265
                }
            ]
        },
        'time': 1548882854
    },
    'success': True
}

LIST_DDNS_EXTIP_PAYLOAD = {
    'data': [
        {
            'ip': '92.10.197.59',
            'ipv6': '0:0:0:0:0:0:0:0',
            'type': 'WAN'
        }
    ],
    'success': True
}

LIST_DDNS_RECORD_PAYLOAD = {
    'data': {
        'next_update_time': '2019-02-16 08:52',
        'records': [
            {
                'enable': True,
                'heartbeat': True,
                'hostname': 'foobar.synology.me',
                'id': 'Synology',
                'ip': '92.10.197.59',
                'ipv6': '0:0:0:0:0:0:0:0',
                'lastupdated': '2019-02-15 08:52',
                'net': 'DEFAULT',
                'provider': 'Synology',
                'status': 'service_ddns_normal',
                'username': 'foobar@gmail.com'
            }
        ]
    },
    'success': True
}

QUERY_INFO_PAYLOAD = {
    'data': {
        'SYNO.API.Auth': {
            'maxVersion': 3,
            'minVersion': 1,
            'path': 'auth.cgi'
        },
        'SYNO.API.Encryption': {
            'maxVersion': 1,
            'minVersion': 1,
            'path': 'encryption.cgi'
        },
    },
    'success': True
}

GETINFO_ENCRYPTION_PAYLOAD = {
    'data': {
        'cipherkey': '__cIpHeRtExT',
        'ciphertoken': '__cIpHeRtOkEn',
        'public_key': 'MIICIjAePcdf3xkxu9bN3odke8BREE3+AC8x00RJr1WI3NVTLThCRBexrsQXbqL8We8Jy0g9UfM92zTgMW05sG0YLifpXwBwMEK6c3c07Yyp3qi+mMvr5mhVhSgK0cEOw3rzOYlsrY0ritziADWNbYY37DcfusyKYKMyLjcat9AYs1NDGBW2aWuUQRQzbd/jAcrqb3+xXN0dJKnpk8EiBiM7srBzMynVaf4nftQO9gtuErefiLXIjjNTy/PQwUeja1gXhonEiQ3HIOdwXwosfmwUZAomn2Oy87ThXYUILvzUfNI8rzGlyOqrQMsQ3sRPUn7Xg03nJQH9IcoU6M6v35ABjrSJHrtcvVThnYg/Ht2WxNYWi9YvUu5kuSfQK1d0qtKk/Wic0inTs5xHjks+wx5NaLxbrUR/uFB+M+en5UmxzLCDcmqWaKlUHhCAduM4NBnC5IVTCjvmL5De/ohIZzLSmvpO9jr4ql/G7eIOwMy2gAu1Tkl0FunkOCrVmtIA7irmV1cVi80eSIKefEMroerPXULiTUV9ESTz/UtBewuZrmrfpE/ki9XpExiZYum4MRa5tsAHl+on9Z3z9fxHrafKYvlv1WBY0Oq4qdxBV6VX0KCX74oq7qYq2Vzm7Mg2xTgxWZmnfZK/xoyd/msx3vv6MCAwEAAQ==',  # noqa: E501
        'server_time': 1550255617
    },
    'success': True
}

GET_NETWORK_WIFIDEVICE_PAYLOAD = {
    'data': {
        'devices': [
            {
                'band': '5G',
                'connection': 'wifi',
                'current_rate': 780,
                'hostname': 'iPad',
                'is_guest': False,
                'mac': '3e:40:1a:fb:5a:db',
                'max_rate': 866,
                'mesh_node_id': 0,
                'netif': 'wlan1',
                'rate_quality': 'high',
                'signalstrength': 56,
                'transferRX': 7876940,
                'transferRX_rate': 0,
                'transferTX': 269652361,
                'transferTX_rate': 0
            },
            {
                'band': '5G',
                'connection': 'wifi',
                'current_rate': 866,
                'hostname': 'OnePlus 6T',
                'is_guest': False,
                'mac': '1a:e6:cf:84:6d:22',
                'max_rate': 866,
                'mesh_node_id': 0,
                'netif': 'wlan1',
                'rate_quality': 'high',
                'signalstrength': 93,
                'transferRX': 2313469,
                'transferRX_rate': 0,
                'transferTX': 41262501,
                'transferTX_rate': 0
            }
        ]
    },
    'success': True
}

GET_NETWORK_WANSTATUS_PAYLOAD = {
    'data': {
        'wan_connected': True
    },
    'success': True
}

GET_SYSTEM_INFO_PAYLOAD = {
    'data': {
        'nodes': [
            {
                'firmware_ver': 'SRM 1.2-7742 Update 5',
                'is_re': False,
                'model': 'RT2600ac',
                'node_id': 0,
                'sn': '176XXXXXX01',
                'unique': 'synology_xxxxxx_rt2600ac',
                'uptime': 1833868
            }
        ],
        'total': 1
    },
    'success': True
}

GET_NGFW_TRAFFIC_PAYLOAD = {
    'data': [
        {
            'deviceID': '64:0d:50:d6:0b:c7',
            'download': 110,
            'download_packets': 0,
            'recs': [
                {
                    'download': 110,
                    'download_packets': 0,
                    'protocollist': [
                        {
                            'download': 51,
                            'download_packets': 0,
                            'protocol': 120,
                            'upload': 39,
                            'upload_packets': 0
                        },
                        {
                            'download': 59,
                            'download_packets': 0,
                            'protocol': 220,
                            'upload': 39,
                            'upload_packets': 0
                        }
                    ],
                    'time': 1582464854,
                    'upload': 78,
                    'upload_packets': 0
                }
            ],
            'upload': 78,
            'upload_packets': 0
        },
        {
            'deviceID': 'cd:9e:34:f7:52:25',
            'download': 6795,
            'download_packets': 5,
            'recs': [
                {
                    'download': 6795,
                    'download_packets': 5,
                    'protocollist': [
                        {
                            'download': 55,
                            'download_packets': 0,
                            'protocol': 5,
                            'upload': 30,
                            'upload_packets': 0
                        },
                        {
                            'download': 6713,
                            'download_packets': 5,
                            'protocol': 7,
                            'upload': 261,
                            'upload_packets': 2
                        },
                        {
                            'download': 27,
                            'download_packets': 0,
                            'protocol': 81,
                            'upload': 27,
                            'upload_packets': 0
                        }
                    ],
                    'time': 1582464854,
                    'upload': 318,
                    'upload_packets': 2
                }
            ],
            'upload': 318,
            'upload_packets': 2
        },
        {
            'deviceID': 'ae:40:8e:7d:88:91',
            'download': 79,
            'download_packets': 1,
            'recs': [
                {
                    'download': 79,
                    'download_packets': 1,
                    'protocollist': [
                        {
                            'download': 79,
                            'download_packets': 1,
                            'protocol': 37,
                            'upload': 39,
                            'upload_packets': 0
                        }
                    ],
                    'time': 1582464854,
                    'upload': 39,
                    'upload_packets': 0
                }
            ],
            'upload': 39,
            'upload_packets': 0
        },
    ],
    'success': True
}

LIST_CERTIFICATE_PAYLOAD = {
    'data': {
        'certificates': [
            {
                'issuer': {
                    'common_name': 'Madalynn Paris'
                },
                'signature_algorithm': 'sha256WithRSAEncryption',
                'subject': {
                    'common_name': 'routerstation.madalynn.xyz'
                },
                'type': 'server_cert'
            },
            {
                'issuer': {
                    'city': 'Taipei',
                    'common_name': 'Synology Inc. CA',
                    'country': 'TW',
                    'department': 'Certificate Authority',
                    'email': 'product@synology.com',
                    'organization': 'Synology Inc.',
                    'state': 'Taiwan'
                },
                'signature_algorithm': 'sha256WithRSAEncryption',
                'subject': {
                    'city': 'Taipei',
                    'common_name': 'Synology Inc. CA',
                    'country': 'TW',
                    'department': 'Certificate Authority',
                    'email': 'product@synology.com',
                    'organization': 'Synology Inc.',
                    'state': 'Taiwan'
                },
                'type': 'root_cert'
            },
            {
                'issuer': {
                    'common_name': 'Madalynn Paris'
                },
                'signature_algorithm': 'sha256WithRSAEncryption',
                'subject': {
                    'common_name': 'Madalynn Paris'
                },
                'type': 'inter_cert'
            }
        ],
        'renewable': False
    },
    'success': True
}

SAFE_ACCESS_STATUS_PAYLOAD = {
'data': {
    'config_groups': [
        {'config_group_id': 3,
        'name': '$guest_network$',
        'pause': False,
        'profile_id': 3,
        'rewards': {'ultra_rewards': []},
        'timespent': {'has_quota': False,
                        'quota': 0,
                        'total_spent': {'normal': 0, 'reward': 0}}},
        {'config_group_id': 4,
        'name': 'Alice',
        'pause': False,
        'profile_id': 4,
        'rewards': {'ultra_rewards': [{'available': 1725586620,
                                        'expired': 1725590220}]},
        'timespent': {'has_quota': True,
                        'quota': 240,
                        'total_spent': {'normal': 24, 'reward': 0}}},
        {'config_group_id': 5,
        'name': 'Bob',
        'pause': False,
        'profile_id': 5,
        'rewards': {'ultra_rewards': []},
        'timespent': {'has_quota': True,
                        'quota': 120,
                        'total_spent': {'normal': 0, 'reward': 0}}}
        ]
},
'success': True
}

PUT_SUCCESS_RESPONSE = {
    'success': True
}