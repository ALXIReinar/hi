from time import sleep

from src.mission_type import Mission, GeoSpecificSpeedLimit
from src.sitl import SITL
from geopy import Point as GeoPoint

from src.communication_gateway import BaseCommunicationGateway
from src.control_system import BaseControlSystem
from src.navigation_system import BaseNavigationSystem
from src.servos import Servos
from src.mission_planner import MissionPlanner
from src.cargo_bay import CargoBay





work_time: int = 5





start_point = GeoPoint(latitude=0, longitude=0) 
car_id = "m1"

queues_dir = {} # Dict Queues

sitl = SITL(queues_dir=queues_dir, position=start_point, car_id=car_id, post_telemetry=True)
communicate = BaseCommunicationGateway(queues_dir)
controlSys = BaseControlSystem(queues_dir)
navigation = BaseNavigationSystem(queues_dir)
sitlControl = Servos(queues_dir)
planner = MissionPlanner(queues_dir)
cargo = CargoBay(queues_dir)
# sensors = 

components = [planner, communicate, controlSys, navigation, sitl, sitlControl, cargo]


mission = Mission(waypoints=[GeoPoint(latitude=59.9386, longitude=30.3121),
                        GeoPoint(latitude=59.9386, longitude=30.3149),
                        GeoPoint(latitude=59.9421, longitude=30.3067)
                  ],
                  speed_limits=[
                        GeoSpecificSpeedLimit(0, 30),
                        GeoSpecificSpeedLimit(1, 45)
                  ],
                  armed=True
                  )

planner.set_new_mission(mission)




















def main(time: int):
    # start()
    for component in components:
        component.start()

    # work time
    sleep(time)

    # stop + wait for all stops
    for on_proccess in components:
        on_proccess.stop()

    for off_proccess in components:
        off_proccess.join()


if __name__ == '__main__':
    main(work_time)






