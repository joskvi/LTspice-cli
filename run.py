import sys, getopt
import simulation_tools
import config

def simulate(filename=None):

    asc_file_path = config.LTSpice_asc_filename

    if filename is not None:
        # Parse the file containing the parameters
        command_list = simulation_tools.parse_parameter_file(filename)

        # Run the list of commands
        if command_list is None:
            print('Syntax error in parameter file.')
            return
        for command in command_list:
            if command[0] == 's':
                parameter = command[1]
                value = command[2]
                # Set parameter as specified
                print('Setting parameter:  ' + str(parameter) + '=' + str(value))
                simulation_tools.set_parameters(asc_file_path, parameter, value, True)
            if command[0] == 'r':
                parameter = command[1]
                parameter_values = command[2]
                # Run tests with the given parameter and corresponding list of parameter values
                simulation_tools.run_simulations([parameter, parameter_values])
            print '\n'
    else:
        # No parameters are set, run simulations with defaults values
        simulation_tools.run_simulations()

def help():
    print 'auto.py -r -f <parameterFile>'

def main(argv):

    # Get arguments
    try:
        opts, args = getopt.getopt(argv, 'hrf:', ['file=', 'run'])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    # Run program based on arguments
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ('-f', '--file'):
            parameter_file = arg
            simulate(parameter_file)
        elif opt in ('-r', '--run'):
            simulate()

if __name__ == '__main__':
    main(sys.argv[1:])
