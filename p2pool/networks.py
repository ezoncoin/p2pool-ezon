from p2pool.ezoncoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    ezoncoin=math.Object(
        PARENT=networks.nets['ezoncoin'],
        SHARE_PERIOD=20, # seconds
        CHAIN_LENGTH=24*60*60//20, # shares
        REAL_CHAIN_LENGTH=24*60*60//20, # shares
        TARGET_LOOKBEHIND=100, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=10, # blocks
        IDENTIFIER='aa185015e0a384f5'.decode('hex'),
        PREFIX='85fd8cff82f170de'.decode('hex'),
        P2P_PORT=8888,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=3333,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-ezon',
        VERSION_CHECK=lambda v: v >= 1000000,
    ),
    ezoncoin_testnet=math.Object(
        PARENT=networks.nets['ezoncoin_testnet'],
        SHARE_PERIOD=20, # seconds
        CHAIN_LENGTH=24*60*60//20, # shares
        REAL_CHAIN_LENGTH=24*60*60//20, # shares
        TARGET_LOOKBEHIND=100, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=10, # blocks
        IDENTIFIER='fa417f64e92d1a3c'.decode('hex'),
        PREFIX='e6fc75a2eca9f373'.decode('hex'),
        P2P_PORT=28888,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=17903,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
