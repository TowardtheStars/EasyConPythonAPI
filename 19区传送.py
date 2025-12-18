import serial, asyncio
from easycon_api.api import *



device = serial.Serial('com12', 115200)
engine = RealTimeController(device)
controller = engine.get_command_builder()

for _ in range(5):
    controller.b(100).wait(100)

controller.plus().wait().lstick(225, 100)
for _ in range(3):
    controller.a().wait()
controller.send()

# engine._cmd_queue.join()
# engine.stop()
t = asyncio.run(engine.start(False))
asyncio.as_completed(t)


