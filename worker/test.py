import os

angle_start = 0
angle_stop = 30
n_angles = 10
n_nodes = 200
n_levels = 3
num_samples = 1
visc = 0.0001
speed = 10
T = 0.1

os.system("sudo docker exec -i worker-docker sh -c 'cd ./murtazo/cloudnaca && exec ./runme.sh " + str(angle_start) + " " + str(angle_stop) + " " + str(n_angles) + " " + str(n_nodes) +  " " + str(n_levels) + " '")
for filename_msh in os.listdir('murtazo/cloudnaca/msh/'):
    if "msh" in filename_msh:
        filename = filename_msh[:-4]
        print("filename used:", filename)
        os.system("sudo docker exec -i worker-docker sh -c 'cd ./murtazo/cloudnaca/msh && exec dolfin-convert " + filename + ".msh " + filename + ".xml'")
        os.system("sudo docker exec -i worker-docker sh -c 'cd ./murtazo/navier_stokes_solver && exec ./airfoil " +  str(num_samples) + " " + str(visc) + " " +  str(speed) + " " + str(T) + " ../cloudnaca/msh/"+ filename +".xml'")
