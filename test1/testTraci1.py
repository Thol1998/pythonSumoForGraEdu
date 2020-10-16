# -*- coding: utf-8 -*-
"""

@author: lukeliuli@163.com
"""


import cProfile
import os
import sys


if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

import traci

def test1():

    print("preparing now \n")
    path = os.getcwd()
    path2 = path+"\sumoCfg2\my1LaneMap1NoVeh-server.sumocfg"
    sumoBinary = "sumo-gui.exe"
    # sumoBinary = "sumo.exe"
    traci.start([sumoBinary, "-c", path2])
    print("start now \n")

    stepNum = 0
    requireStop = 0
    while requireStop == 0:
        traci.simulationStep()

        stepNum += 1
        requireStop = 0
        timeT = traci.simulation.getTime()  # 当前时间
        vehicles = traci.vehicle.getIDList()  # 当前在道路上的车辆
        curTime = timeT
        # for len(vehicles)>0:
        #    traci.vehicle.setParameter("00001", "carFollowModel.SimpleCACC1", "Hi")

        print("running "+str(curTime))

    # 每隔15秒加入1车，步长0.01
        if stepNum % 1500 == 1:
            vehSpeed = 0
            vehPos = 10
            vehLane = 0
            vehichID = "veh"+str(stepNum)
            traci.vehicle.addLegacy(
                vehichID, "r1", -3, vehPos, vehSpeed, str(vehLane), "car1")
            print("add a car "+vehichID+" at " + str(int(timeT))+"\n")

        if timeT > 60:  # if time is over 200 second stoping the simulation
            requireStop = 1

        #################################################################################
        #
        if len(vehicles) > 0:
            for vehName in vehicles:
                curspeed = traci.vehicle.getSpeed(vehName)
                position = traci.vehicle.getPosition(vehName)
                angle = traci.vehicle.getAngle(vehName)
                latpos = traci.vehicle.getLateralLanePosition(vehName)
                vehLatAlignment = traci.vehicle.getLateralAlignment(vehName)
                vehNextTLS = traci.vehicle.getNextTLS(vehName)
                laneID = traci.vehicle.getLaneID(vehName)
                laneIndex = traci.vehicle.getLaneIndex(vehName)
                roadId = traci.vehicle.getRoadID(vehName)

                dist1 = traci.vehicle.getDistance(vehName)
                drivingDist1 = traci.vehicle.getDrivingDistance(vehName, roadId, 0)

                leader = traci.vehicle.getLeader(vehName)
                leftLeader = traci.vehicle.getLeftLeaders(vehName)
                leftFollower = traci.vehicle.getLeftFollowers(vehName)
                rightFollowers = traci.vehicle.getRightFollowers(vehName)
                rightLeaders = traci.vehicle.getRightLeaders(vehName)
                slope = traci.vehicle.getSlope(vehName)
                getAcceleration = traci.vehicle.getAcceleration(vehName)
                fuelConsumption = traci.vehicle.getFuelConsumption(vehName)
                lineInfo = traci.vehicle.getLine(vehName)
                idEdges = traci.vehicle.getRoute(vehName)
                routeID = traci.vehicle.getRouteID(vehName)
                routeIndex = traci.vehicle.getRouteIndex(vehName)

                # traci.vehicle.highlight(vehName)
                nextStops = traci.vehicle.getNextStops(vehName)

                # Return list of upcoming traffic lights [(tlsID, tlsIndex, distance, state), ...]
                nextTLS = traci.vehicle.getNextTLS(vehName)
                if len(nextTLS) == 0:
                    continue

                nextTLSID = nextTLS[0][0]
                nextTLSDist = nextTLS[0][2]
                states = traci.trafficlight.getRedYellowGreenState(nextTLSID)
                nextSwitch = traci.trafficlight.getNextSwitch(nextTLSID)
                phaseName = traci.trafficlight.getPhaseName(nextTLSID)
                phase = traci.trafficlight.getPhase(nextTLSID)
                phaseDuration = traci.trafficlight.getPhaseDuration(nextTLSID)
                programLogic = traci.trafficlight.getProgram(nextTLSID)
                controlledLinks = traci.trafficlight.getControlledLinks(nextTLSID)
                allProgramLogics = traci.trafficlight.getAllProgramLogics(
                    nextTLSID)
                lgc1 = allProgramLogics[0]
                greenDurTime = lgc1.phases[0].duration
                yellowDurTime = lgc1.phases[1].duration
                redDurTime = lgc1.phases[2].duration

                phaseLeftTime = nextSwitch - timeT+0.00001
                arrivalTimeNextTLS = nextTLSDist / (curspeed+0.000001)

                if states == "GG":
                    speedPassGreenTLSInGreen = nextTLSDist / phaseLeftTime

                if states == "rr":
                    speedPassGreenTLSInRed = nextTLSDist / (phaseLeftTime + 0.5)  # 加0.5秒

                if states == "yy":
                    speedPassYellowTLSInYellow = nextTLSDist / (phaseLeftTime)
                    speedPassGreenTLSInYellow = nextTLSDist / (phaseLeftTime+redDurTime+0.5)


    traci.close()


if __name__ == '__main__':
   cProfile.run('test1()')
