import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

for i in range(11):
    iteration = str(i)

    for j in range(3):
        step = str(j+1)
        data = np.loadtxt("results/iteration_"+iteration+"_step_"+step+"_x_data.csv", delimiter = ",")

        time_points = data[:,0]

        x_data = data[:, 1:]

        plt.figure()

        for k in range(4):
            plt.plot(time_points, x_data[:, k], label = "T_sto_HT_" + str(k))

        plt.title("HT storage - step: " +step +"; iteration: " + iteration)
        plt.legend(loc = "best")
        plt.savefig("plots/1-st"+step+"it"+iteration+".png")

        plt.figure()

        for k in range(3):
            plt.plot(time_points, x_data[:, k+4], label = "T_sto_LT_" + str(k))

        plt.title("LT storage - step: "+step+"; iteration: "+iteration)
        plt.legend(loc = "best")
        plt.savefig("plots/2-st"+step+"it"+iteration+".png")

        plt.figure()
        plt.plot(time_points, x_data[:,7])
        plt.title("Solar collectors - step: " +step +"; iteration: " + iteration)
        plt.savefig("plots/3-st"+step+"it"+iteration+".png")

        plt.figure()
        plt.plot(time_points, x_data[:,8:10])
        plt.title("Fan coils - step: " +step +"; iteration: " + iteration)
        plt.savefig("plots/4-st"+step+"it"+iteration+".png")

        plt.figure()
        plt.plot(time_points, x_data[:,10:])
        plt.title("Room temperature - step: " +step +"; iteration: " + iteration)
        plt.savefig("plots/5-st"+step+"it"+iteration+".png")

        data = np.loadtxt("results/iteration_"+iteration+"_step_"+step+"_u_data.csv", delimiter = ",")

        time_points = data[:,0]

        u_data = data[:, 1:]

        plt.figure()
        plt.plot(time_points, u_data)
        plt.title("Massflows - step: " +step +"; iteration: " + iteration)
        plt.savefig("plots/6-st"+step+"it"+iteration+".png")

        data = np.loadtxt("results/iteration_"+iteration+"_step_"+step+"_b_data.csv", delimiter = ",")

        time_points = data[:,0]

        b_data = data[:, 1:]

        plt.figure()
        plt.plot(time_points, b_data)
        plt.title("ACM operation status - step: " +step +"; iteration: " + iteration)
        plt.savefig("plots/7-st"+step+"it"+iteration+".png")

        plt.close("all")
