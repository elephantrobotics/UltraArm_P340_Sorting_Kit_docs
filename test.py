from pymycobot import ElephantRobot

er=ElephantRobot("192.168.1.18",5001)
er.start_client()
er.write_angles([0,-90,0,-90,0,0],1000)


