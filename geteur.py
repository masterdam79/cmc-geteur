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

def getfiat( crypto, fiat ):
   "This function returns the CMC value for the passed crypto/fiat pair"
   result = coinmarketcap.ticker(crypto, limit=3, convert=fiat)
   fiatresult = result[0]['price_' + fiat]
   return fiatresult

fiatresult = getfiat(crypto, fiat)

print(fiatresult)
