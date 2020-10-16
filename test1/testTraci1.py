# -*- coding: utf-8 -*-
"""

@author: lukeliuli@163.com
"""
import os
import sys
import traci

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

# sys.path.append(os.path.join('c:', os.sep, 'whatever', 'path', 'to', 'sumo', 'tools'))
print("preparing now \n")


path = os.getcwd()
path2 = path+"\sumoCfg\my1LaneMap1NoVeh-server.sumocfg"
sumoBinary = "sumo-gui.exe"
# sumoBinary = "sumo.exe"
traci.start([sumoBinary, "-c", path2])
print("start now \n")

stepNum = 0
requireStop = 0
while requireStop == 0:
    stepNum += 1
    requireStop = 0
    timeT = traci.simulation.getTime()  # 当前时间
    vehicles = traci.vehicle.getIDList()  # 当前在道路上的车辆
    curTime = timeT
    # for len(vehicles)>0:
    #    traci.vehicle.setParameter("00001", "carFollowModel.SimpleCACC1", "Hi")

    print("running "+str(curTime)+"\n")

   # 每隔20秒加入1车，步长0.01
    if stepNum % 2000 == 1:
        vehSpeed = 0
        vehPos = 10
        vehLane = 0
        vehichID = "veh"+str(stepNum)
        traci.vehicle.addLegacy(
            vehichID, "r1", -3, vehPos, vehSpeed, str(vehLane), "car1")
        print("add a car "+vehichID+" at " + str(int(timeT))+"\n")
    # libsumo.vehicle.setLaneChangeMode(vehichID,0)
    traci.simulationStep()

    if timeT > 60:  # if time is over 200 second stoping the simulation
        requireStop = 1

traci.close()
