# -*- coding: utf-8 -*-
"""

@author: lukeliuli@163.com
"""
import os, sys
import libsumo


if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:   
     sys.exit("please declare environment variable 'SUMO_HOME'")
     
# sys.path.append(os.path.join('c:', os.sep, 'whatever', 'path', 'to', 'sumo', 'tools'))
print("preparing now \n")
lateralResolution = 0.01 

path = os.getcwd()
path2 = path+"\sumoCfg\my1LaneMap1NoVeh-server.sumocfg"
sumoBinary = "sumo-gui.exe"
sumoBinary = "sumo.exe"

libsumo.start([sumoBinary, "-c", path2])


stepNum = 0
requireStop = 0
while requireStop == 0:
     stepNum += 1
     requireStop = 0
     timeT = libsumo.simulation.getCurrentTime();#当前时间
     vehicles = libsumo.vehicle.getIDList();#当前在道路上的车辆
     curTime = timeT/1000
     #for len(vehicles)>0:
     #    traci.vehicle.setParameter("00001", "carFollowModel.SimpleCACC1", "Hi")


      
    #每隔20秒加入1车队   
    if timeT%20000==0:
     vehSpeed = 40 / 3.6
     vehPos
     libsumo.vehicle.addLegacy(vehichID,"r1",-3,veh.position,veh.speed,str(veh.lane),"car1")
     #libsumo.vehicle.setLaneChangeMode(vehichID,0)
        
     

        
    libsumo.simulationStep()
    if timeT/1000 >300: #if time is over 200 second stoping the simulation
        requireStop = 1

libsumo.close()
