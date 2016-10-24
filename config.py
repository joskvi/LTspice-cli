
# Config values for running LTSpiceIV simulations and analysis_tools

output_data_path = 'data/' # Leave blank if output should be writtten to root folder.
output_data_naming_convention = 'parameter' # Assumes parameter by default. Set to 'parameter' or 'number'.

LTSpice_executable_path = 'C:\Program Files (x86)\LTC\LTspiceIV\scad3.exe'
LTSpice_asc_filename = 'example_circuit.asc' # 'example_circuit.asc'

variable_numbering = {'time': 0, 'V_c': 2, 'I_c': 3}
preffered_sorting = [0, 1, 2]
