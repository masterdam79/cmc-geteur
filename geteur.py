#!/usr/bin/env python

import argparse
import sys
from coinmarketcap import Market
import json


parser = argparse.ArgumentParser(description='Process some arguments.')

parser.add_argument('--crypto', type=str, required=True)
parser.add_argument('--fiat', type=str, required=True)

try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

crypto = args.crypto
fiat = args.fiat

coinmarketcap = Market()

result = coinmarketcap.ticker(crypto, limit=3, convert=fiat)

print json.dumps(result[0], indent=4, sort_keys=True)


print(result[0]['price_eur'])
