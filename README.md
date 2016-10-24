# LTspice-cli

## About

LTspice-cli is a command line tool, which enables running simulations in LTspice from the command line. It also has the ability to specify a file containing the circuit parameters which the simulations should be run with. LTspice-cli is written in Python, and requires NumPy to run. The tool is only tested with LTspice IV.

## How to use

After downloading the files, the config.py file must be edited. Once configurated, a simulation can be run using
```
python auto.py -r
```
To specify a file containing parameters, use
```
python auto.py -f <inputfile>
```
Use option -h to see help in the command line.
