# mpc_plot
def getPlot(
	data="x", 
	step_a=1, step_b=3, 
	data_ind=0, 
	save_loc="plots/", 
	file_format=".pdf",
	fig_size=(20, 10), 
	plots=4, 
	iterations=10, 
	buffer_ind=5, 
	label="Label", 
	title="Title", 
	time_unit="sec", 
	y_label="", 
	colors=['darkred', 'darkorange', 'darkgreen', 'darkblue', 'red', 'orange', 'green', 'blue'])