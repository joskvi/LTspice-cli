import simulation_tools
import config

def main():

    # Specify parameters
    total_list = []

    # Optimal snubber run_tests
    simulation_tools.set_params(config.LTSpice_asc_filename, 'C', '2u', True)
    total_list.append(('R', ['1k', '2k']))

    for elem in total_list:
        # Pick parameter and corresponding values
        param = elem[0]
        param_value_list = elem[1]

        # Run tests with the given parameter and corresponding list of parameter values
        simulation_tools.run_simulations(param, param_value_list, True)


def test():
    filename = 'param.txt'
    param_list = simulation_tools.parse_param_file(filename)
    if param_list is None:
        print("Syntax error in parameter file.")
        return
    for p in param_list:
        # Run tests with the given parameter and corresponding list of parameter values
        simulation_tools.run_simulations(p[0], p[1], True)

if __name__ == "__main__":
    test()
