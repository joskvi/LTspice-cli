##########################################
## CONFIGURATION OF LTspice SIMULATIONS ##
##########################################

# File path of the LTspice program installed on the system
LTSpice_executable_path = 'C:\Program Files (x86)\LTC\LTspiceIV\scad3.exe'
# The name of the circuit to be used in simulations
LTSpice_asc_filename = 'example_circuit.asc'

# The measurements to be saved from the simulation. The appropriate numbers can be found in the .raw file generated at simulation.
variable_numbering = {'time': 0, 'V_c': 2, 'I_c': 3}
# The ordering of the measurements to be saved in the output csv files can be changed below, by changing how the numbers are ordered.
# E.g. switch place of 0 and 1 if you want V_c to be placed left of time in the output csv files.
preffered_sorting = [0, 1, 2]

# Leave blank if output should be writtten to root folder.
output_data_path = 'data/'
# Assumes parameter by default. Set to 'parameter' or 'number'.
output_data_naming_convention = 'parameter'
