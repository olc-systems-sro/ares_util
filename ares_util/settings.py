# !/usr/bin/python
# coding=utf-8

from __future__ import (absolute_import, division, print_function, unicode_literals)

COMPANY_ID_LENGTH = 8
ARES_API_URL = 'https://ares.gov.cz/'

# Identifiers returned by base endpoint (/ekonomicke-subjekty/) mapped to their respective endpoints
SUB_REGISTER_MAP = {
    "stavZdrojeVr": "ekonomicke-subjekty-vr/",
    "stavZdrojeRes": "ekonomicke-subjekty-res/",
    "stavZdrojeRzp": "ekonomicke-subjekty-rzp/",
    "stavZdrojeNrpzs": "ekonomicke-subjekty-nrpzs/",
    "stavZdrojeRpsh": "ekonomicke-subjekty-rpsh/",
    "stavZdrojeRcns": "ekonomicke-subjekty-rcns/",
    "stavZdrojeSzr": "ekonomicke-subjekty-szr/",
    "stavZdrojeDph": "ekonomicke-subjekty-dph/",
    "stavZdrojeSd": "ekonomicke-subjekty-sd/",
    "stavZdrojeIr": "ekonomicke-subjekty-ir/",
    "stavZdrojeCeu": "ekonomicke-subjekty-ceu/",
    "stavZdrojeRs": "ekonomicke-subjekty-rs/",
    "stavZdrojeRed": "ekonomicke-subjekty-red/",
}
