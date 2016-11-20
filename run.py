import sys, getopt
import simulation_tools
import config

def simulate(filename=None):
    if filename is not None:
        # Parse the file containing the parameters
        param_list = simulation_tools.parse_parameter_file(filename)
        if param_list is None:
            print('Syntax error in parameter file.')
            return
        for p in param_list:
            # Run tests with the given parameter and corresponding list of parameter values
            simulation_tools.run_simulations(p)
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
