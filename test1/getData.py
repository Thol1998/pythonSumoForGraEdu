import traci
import traci.constants as tc

def storeVehStats(vehicles, step):
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

               

           
                


    return


