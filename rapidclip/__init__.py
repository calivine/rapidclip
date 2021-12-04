import sys

from etc.arguments import parse_options
from etc.options import Options
from .RapidClip import RapidClip


def _real_main(argv=None):
    # Get command options
    if len(argv) == 1:
        sys.exit('\nERROR usage: rapid <filename>[ext] [arg1][arg2]...')
    # Depreciated
    # options = {'params': parse_options(argv), 'source': argv[1]}
    options = Options(parse_options(argv), argv[1])
    # If this is a batch file, run process video on each filename.
    if options.batch is not None:
        file = open(options.batch, 'r')
        while True:
            line = file.readline()
            if line[:-1] == '':
                break
            options.source = line[:-1]
            RapidClip(options).process()
        file.close()
    else:
        RapidClip(options).process()


def main(argv=None):
    """ Processes user inputs and completes the video editing
    based on user's parameters.

    :param argv: User arguments <filename> -flag [arg1] -flag [arg2] -flag [arg3] ...

    argv[1]: filename

    argv[2] - argv[n] option parameters:

    -g, --gif     Save file as GIF

    -w, --webm    Save file as webm

    -a, -auto     Auto-edit file down to summary clip.

    -f, --file   Perform actions on a batch file. Usage: rapid -f FILE.txt OPTIONS

    -c, --clips   Include custom timestamps to edit video on. Usage: rapid FILENAME -c [ts1start, ts1end, ...]

    -l, --length   Controls how many clips and length of each clip for the auto-editor. Usage: rapid -a -l 10 6 OPTIONS

    """
    try:
        _real_main(argv)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
