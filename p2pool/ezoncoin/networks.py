import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(ezoncoind, genesis_block_hash):
    try:
        yield ezoncoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(
    ezoncoin=math.Object(
        P2P_PREFIX='a60b3aad'.decode('hex'),
        P2P_PORT=18888,
        ADDRESS_VERSION=33,
        RPC_PORT=18889,
        RPC_CHECK=defer.inlineCallbacks(lambda ezoncoind: defer.returnValue(
            'ezoncoinaddress' in (yield ezoncoind.rpc_help()) and
            not (yield ezoncoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda nBits, height: __import__('ezoncoin_subsidy').GetBlockBaseValue(nBits, height),
        BLOCKHASH_FUNC=data.hash256,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=60, # s
        SYMBOL='EZON',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Ezoncoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Ezoncoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.ezoncoin'), 'ezoncoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.ezoncoin.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.ezoncoin.com/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.ezoncoin.com/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
    ezoncoin_testnet=math.Object(
        P2P_PREFIX='cee2caff'.decode('hex'),
        P2P_PORT=28888,
        ADDRESS_VERSION=139,
        RPC_PORT=18888,
        RPC_CHECK=defer.inlineCallbacks(lambda ezoncoind: defer.returnValue(
            'ezoncoinaddress' in (yield ezoncoind.rpc_help()) and
            (yield ezoncoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda nBits, height: __import__('ezoncoin_subsidy').GetBlockBaseValue_testnet(nBits, height),
        BLOCKHASH_FUNC=data.hash256,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=60, # s
        SYMBOL='tEZON',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Ezoncoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Ezoncoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.ezoncoin'), 'ezoncoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://test.explorer.ezoncoin.qa/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://test.explorer.ezoncoin.qa/address/',
        TX_EXPLORER_URL_PREFIX='http://test.explorer.ezoncoin.qa/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
