import simulation_tools
import config

def main():

    # Specify parameters

    total_list = []

    # Optimal snubber run_tests
    simulation_tools.set_params(config.LTSpice_asc_filename, 'C_s2', '0', True)
    simulation_tools.set_params(config.LTSpice_asc_filename, 'R_gOff', '3.9', True)
    total_list.append(('C_s1', ['0.9n', '1.8n', '3.5n', '6.2n', '8.8n']))

    for elem in total_list:
        # Pick parameter and corresponding values
        param = elem[0]
        param_value_list = elem[1]

        # Run tests with the given parameter and corresponding list of parameter values
        simulation_tools.run_tests(param, param_value_list, True)


    simulation_tools.output_final_data(total_list, config.output_data_summary_filename)

if __name__ == "__main__":
    main()
