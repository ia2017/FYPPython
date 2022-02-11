import os,sys,shutil

# MICHALIS ADDITION
if os.path.exists("of_grad_new3.dat"):
    flow_grad = open("of_grad_new3.dat", mode="r")
    flow_lines = flow_grad.readlines()
#        fea_grad = open("of_grad_solid.dat", mode="r")
#        fea_lines = fea_grad.readlines()
#        fea_grad.close()
    flow_grad.close()

    # %% Write the new file of_grad . dat first line
    merged_file = open("of_grad.dat", mode="w")
    merged_file.write(flow_lines[0])

    # Add the two gradients and write them
    for count in range(1, len(flow_lines)):
#            fea_value = float(fea_lines[count][0: -1])
        flow_value = float(flow_lines[count][0: -1])
#            total_value = fea_value + flow_value
        merged_file.write(str(flow_value) + '\n')

    # Close the file
    merged_file.close()
    # END OF MICHALIS ADDITION