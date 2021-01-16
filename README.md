# LightsOutPuzzle

This is a Python AI designed to solve any iteration of the lights out puzzle.

The lights out puzzle is defined as follows:
A one-person game played on a rectangular lattice of lamps which can be turned on and off. A move consists of flipping a "switch" inside one of the squares, thereby toggling the on/off state of this and all four vertically and horizontally adjacent squares. Starting from a randomly chosen light pattern, the aim is to turn all the lamps off.

Additionally, included is a GUI for the lights out puzzle. The GUI opens with a solved puzzle, meaning all lights are off. Pressing the scramble button generates a puzzle, which the user can either solve on their own or press the solve button to allow the AI to solve the puzzle. In order to open the GUI, navigate to the location of the files from the command line and enter:

`python LightsOutGUI.py rows cols`

where rows and cols are numbers indicating the number of rows and columns for the puzzle.

Please note that the AI may run slowly on puzzles larger than 4 x 4.
