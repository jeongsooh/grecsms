import asyncio
import logging
from chargepoint import ChargePoint

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)

from ocpp.routing import on
from ocpp.v16 import call, call_result
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import RegistrationStatus, Action

logging.basicConfig(level=logging.INFO)

# heartbeat_interval = 60

async def heartbeat_send(cp):
    while True:
        await cp.send_heartbeat()
        await asyncio.sleep(cp.heartbeat_interval)

async def main():

    # EVNest 
    # async with websockets.connect(
    #     'ws://3.37.224.145:80/ws/ocpp/k-11-1',
    #     subprotocols=['ocpp1.6']
    # ) as ws:

    # Naver
    # async with websockets.connect(
    #     'ws://106.10.32.171:8000/webServices/ocpp/202021',
    #     subprotocols=['ocpp1.6']
    # ) as ws:

    # Windows Server(local)
    # async with websockets.connect(
    #     'ws://192.168.0.215:8000/webServices/ocpp/gre300001',
    #     subprotocols=['ocpp1.6']
    # ) as ws:
    #
    # async with websockets.connect(
    #     'ws://127.0.0.1:8000/webServices/ocpp/gre202021',
    #     subprotocols=['ocpp1.6']
    # # ) as ws:

    # async with websockets.connect(
    #     'ws://emcms.watchpoint.co.kr/webServices/ocpp/100198',
    #     subprotocols=['ocpp1.6']
    # ) as ws:

    # virtual client
    # async with websockets.connect(
    #     'ws://192.168.0.215:8000/webServices/ocpp/grevcli01',
    #     subprotocols=['ocpp1.6']
    # ) as ws:
    async with websockets.connect(
        'ws://34.64.149.53:5555/f160',
        subprotocols=['ocpp1.6']
    ) as ws:

        cp = ChargePoint('f160', ws) # virtual client
        # cp = ChargePoint('grevcli01', ws) # virtual client
        # cp = ChargePoint('202021', ws) # Naver
        # cp = ChargePoint('gre300001', ws) # Windows Server(local)

        await asyncio.gather(
          cp.start(), 
          cp.send_boot_notification(),
          cp.send_status_notification('Available'),
          heartbeat_send(cp),
        #   cp.send_authorize()
        #   heartbeat_send(cp, heartbeat_interval)
        )

if __name__ == '__main__':
    try:
        # asyncio.run() is used when running this example with Python 3.7 and
        # higher.
        asyncio.run(main())
    except AttributeError:
        # For Python 3.6 a bit more code is required to run the main() task on
        # an event loop.
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
