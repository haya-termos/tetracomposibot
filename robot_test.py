# Projet "robotique" IA&Jeux 2025
#
# Binome:
#  Prénom Nom No_étudiant/e : _________
#  Prénom Nom No_étudiant/e : _________
#
# check robot.py for sensor naming convention
# all sensor and motor value are normalized (from 0.0 to 1.0 for sensors, -1.0 to +1.0 for motors)

from robot import * 

nb_robots = 0

class Robot_player(Robot):

    team_name = "Test"  # vous pouvez modifier le nom de votre équipe
    robot_id = -1             # ne pas modifier. Permet de connaitre le numéro de votre robot.
    memory = 0                # vous n'avez le droit qu'a une case mémoire qui doit être obligatoirement un entier

    def __init__(self, x_0, y_0, theta_0, name="n/a", team="n/a"):
        global nb_robots
        self.robot_id = nb_robots
        nb_robots+=1
        super().__init__(x_0, y_0, theta_0, name="Robot "+str(self.robot_id), team=self.team_name)

    
    
    def step(self, sensors, sensor_view=None, sensor_robot=None, sensor_team=None):
        sensor_to_wall = []
        sensor_to_robot = []

        for i in range (0,8):
            if  sensor_view[i] == 1:
                sensor_to_wall.append( sensors[i] )
                sensor_to_robot.append(1.0)
            elif  sensor_view[i] == 2:
                sensor_to_wall.append( 1.0 )
                sensor_to_robot.append( sensors[i] )
            else:
                sensor_to_wall.append(1.0)
                sensor_to_robot.append(1.0)

        if (self.robot_id%4==0): #robot 0
            if (sensor_to_wall[sensor_front]<0.9 or sensor_to_wall[sensor_front_right]<0.9 or sensor_to_wall[sensor_front_left]<0.9): #subsomption
                translation = sensor_to_wall[sensor_front]*0.6 #braitenberg
                rotation =  sensor_to_wall[sensor_front_left]- sensor_to_wall[sensor_front_right] +(1-sensor_to_wall[sensor_front])  + (random.random()-0.5)*0.1
            elif (sensor_to_robot[sensor_front]<1 or sensor_to_robot[sensor_front_right]<1 or sensor_to_robot[sensor_front_left]<1) and (sensor_team[sensor_front]==self.team_name or sensor_team[sensor_front_right]==self.team_name or sensor_team[sensor_front_left]==self.team_name):
                translation = sensor_to_robot[sensor_front]*0.6 #braitenberg
                rotation =  sensor_to_robot[sensor_front_left]- sensor_to_robot[sensor_front_right] +(1-sensor_to_robot[sensor_front])  + (random.random()-0.5)*0.1
            elif (sensor_to_robot[sensor_front]<1 or sensor_to_robot[sensor_front_right]<1 or sensor_to_robot[sensor_front_left]<1) and (sensor_team[sensor_front]!=self.team_name or sensor_team[sensor_front_right]!=self.team_name or sensor_team[sensor_front_left]!=self.team_name):
                translation = sensor_to_robot[sensor_front]*0.5 
                rotation = sensor_to_robot[sensor_front_right] - sensor_to_robot[sensor_front_left] + (random.random()-0.5)*0.1
            else:
                translation=1
                rotation=(random.random()-0.5)*0.1

        elif (self.robot_id%4==3): #robot 3
                if sensors[sensor_rear]!=1 and self.memory==0: #arbre de décision
                    rotation=1.0 
                    translation=0
                elif sensors[sensor_front]<0.5:
                    self.memory=1
                    rotation=-1
                    translation=0
                elif sensors[sensor_left]<0.3:
                    self.memory=1
                    translation= 1.0
                    rotation=-0.03
                elif sensors[sensor_right]<0.3:
                    self.memory=1
                    translation= 1.0
                    rotation=0.03
                else:
                    translation=1.0
                    rotation=(random.random()-0.5)

        else:
            if (sensor_to_robot[sensor_rear]<1 or sensor_to_robot[sensor_rear_right]<1 or sensor_to_robot[sensor_rear_left]<1) and (sensor_team[sensor_rear]==self.team_name or sensor_team[sensor_rear_right]==self.team_name or sensor_team[sensor_rear_left]==self.team_name):
                translation = 1.0
                rotation =0
                if (sensor_to_wall[sensor_front]<0.3 or sensor_to_wall[sensor_front_right]<0.3 or sensor_to_wall[sensor_front_left]<0.3): #très petite marge
                    translation = 0.2 
                    rotation = 1.0    
    
            else:
                if (sensor_to_wall[sensor_front]<0.9 or sensor_to_wall[sensor_front_right]<0.9 or sensor_to_wall[sensor_front_left]<0.9): #subsomption
                    translation = sensor_to_wall[sensor_front]*0.7 #braitenberg
                    rotation =  sensor_to_wall[sensor_front_left]- sensor_to_wall[sensor_front_right] +(1-sensor_to_wall[sensor_front])  + (random.random()-0.5)*0.1
                elif (sensor_to_robot[sensor_front]<1 or sensor_to_robot[sensor_front_right]<1 or sensor_to_robot[sensor_front_left]<1) and (sensor_team[sensor_front]==self.team_name or sensor_team[sensor_front_right]==self.team_name or sensor_team[sensor_front_left]==self.team_name):
                    translation = sensor_to_robot[sensor_front]*0.7 #braitenberg
                    rotation =  sensor_to_robot[sensor_front_left]- sensor_to_robot[sensor_front_right] +(1-sensor_to_robot[sensor_front])  + (random.random()-0.5)*0.1
                else:
                    translation=1
                    rotation=(random.random()-0.5)*0.1
            
        return translation, rotation, False

