import numpy as np
import pylab as plt


class plotFunctions:

	def getMinMax(act_values1, act_values2, data_ind, plots, rel_delta=10.0):
		minList = []
		maxList = []
		for k in range(plots):
			minList.append(min(act_values1[:, k + data_ind]))
			minList.append(min(act_values2[:, k + data_ind]))
			maxList.append(max(act_values1[:, k + data_ind]))
			maxList.append(max(act_values2[:, k + data_ind]))
		minVal = min(minList)
		maxVal = max(maxList)
		abs_delta = (maxVal - minVal) * rel_delta / 100.0
		return (minVal - abs_delta, maxVal + abs_delta)


	def getLabel(label, k):
		if (isinstance(label, list)):
			return label[k]
		return label + str(k)


	def getPlot(data="x", data_loc="", step_a=1, step_b=3, data_ind=0, save_loc="", file_format=".pdf", fig_size=(20, 10), plots=4, iterations=10, buffer_ind=5, label="Label", title="Title", time_unit="sec", y_label="", colors=['darkred', 'darkorange', 'darkgreen', 'darkblue', 'red', 'orange', 'green', 'blue']):

		past_values = []
		past_time_values = []
		act_values_st1 = []
		act_values_st2 = []
		time_fac = 1.0

		x_label = r" t in [$\displaystyle\mathrm{" + time_unit + "}$]"
		plt.rc('text', usetex=True)
		plt.rc('font', family='serif')

		if (time_unit == "h"):
			time_fac = 3600.0
		elif(time_unit == "min"):
			time_fac = 60.0

		for i in range(iterations):
			data1 = np.loadtxt(data_loc + "iteration_" + str(i) + "_step_" + str(step_a) + "_" + str(data) + "_data.csv", delimiter=",")
			data2 = np.loadtxt(data_loc + "iteration_" + str(i) + "_step_" + str(step_b) + "_" + str(data) + "_data.csv", delimiter=",")
			time_ind = np.loadtxt(data_loc + "iteration_0_final_states.csv", delimiter=",")[0] / time_fac

			time_values = data1[:, 0] / time_fac
			past_time_values.insert(0, -i * time_ind)

			act_values_st1 = data1[:, 1:]
			act_values_st2 = data2[:, 1:]
			past_values.append(act_values_st1[0])


			plt.figure(figsize=fig_size)

			axes = plt.gca()
			if (i < buffer_ind):
				x_min = past_time_values[0]
				x_max = time_values[-1] + past_time_values[0] + buffer_ind * time_ind
			elif (i == buffer_ind):
				x_min = past_time_values[0]
				x_max = time_values[-1] + past_time_values[0] + buffer_ind * time_ind

			if (i == 0):
				y_min, y_max = plotFunctions.getMinMax(act_values_st1, act_values_st2, data_ind, plots)

			axes.set_xlim(x_min, x_max)
			axes.set_ylim(y_min, y_max)

			for k in range(plots):
				temp_past_values = [[row[i] for row in past_values] for i in range(len(past_values[0]))][k + data_ind]
				plt.plot(past_time_values, temp_past_values, "-o", label=plotFunctions.getLabel(label, k), color=colors[k],)

			plt.xlabel(x_label)
			plt.ylabel(y_label)
			plt.legend(loc="best")
			plt.title(title)
			plt.savefig(save_loc + title + str(i) + "1" + file_format)

			lines = []
			for k in range(plots):
				line, = plt.plot(time_values, act_values_st1[:, k + data_ind], "--", color=colors[k])
				lines.append(line)

			plt.savefig(save_loc + title + str(i) + "2" + file_format)

			for k in range(plots):
				lines[k].set_alpha(0.2)

			for k in range(plots):
				plt.plot(time_values, act_values_st2[:, k + data_ind], "--", color=colors[k])

			plt.savefig(save_loc + title + str(i) + "3" + file_format)

			plt.close("all")
