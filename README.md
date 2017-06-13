# mpc_plot

## Explanations to mpc_plot.plot_functions

def getPlot(
 - data="x", -> describes which data ("x", "u" or "b")
 - step_a=1, step_b=3, -> describes which steps(1 and 2 or 3)
 - data_ind=0, -> describes in which column the data of the first plot is 
 - save_loc="plots/", -> path where the created plots get saved 
 - file_format=".pdf", -> format of the plot 
 - fig_size=(20, 10), -> size of the pylab figure
 - plots=4, -> describes how many different curves are in the figure  
 - iterations=10, -> describes how many iteration will be plotted
 - buffer_ind=5, -> describes the buffer for shifting the time axis
 - label="Label", -> label of the different curves
 - title="Title", -> title of the plots
 - time_unit="sec", -> unit of time ("s","sec","min" or "h") for x-axis
 - y_label="", -> label of the y-axis
 - colors=['darkred', 'darkorange', 'darkgreen', 'darkblue', 'red', 'orange', 'green', 'blue'] -> color array for the different curves 
 \n)