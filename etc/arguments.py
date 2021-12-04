import optparse
import argparse


def parse_options(arguments=None):
    parser = optparse.OptionParser()
    parser.add_option("-a", action="store_true", dest="auto")
    parser.add_option("--auto", action="store_true", dest="auto")
    parser.add_option("-w", action="store_true", dest="webm")
    parser.add_option("--webm", action="store_true", dest="webm")
    parser.add_option("-g", action="store_true", dest="gif")
    parser.add_option("--gif", action="store_true", dest="gif")
    parser.add_option("-l", action="store", dest="length", nargs=2)
    parser.add_option("--length", action="store", dest="length", nargs=2)
    parser.add_option("-c", action="store", dest="clips")
    parser.add_option("--clips", action="store", dest="clips")
    parser.add_option("-f", action="store", dest="batch")
    parser.add_option("--file", action="store", dest="batch")
    parser.add_option("-b", action="store", dest="buffer")
    parser.add_option("--buffer", action="store", dest="buffer")
    parser.add_option("-t", action="store", dest="tail")
    parser.add_option("--tail", action="store", dest="tail")
    parser.add_option("-v", action="store_true", dest="verbose")
    parser.add_option("--verbose", action="store_true", dest="verbose")

    parser.set_defaults(auto=False,
                        length=(10, 6),
                        webm=False,
                        gif=False,
                        clips=None,
                        batch=None,
                        buffer=0,
                        tail=0,
                        verbose=False)

    opts, args = parser.parse_args(arguments)

    # Arg parse method
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--auto", action="store", type=int, nargs="+", help="Auto-generate clips L C H T")
    parser.add_argument("-f", "--format", choices=["mp4", "gif", "webm"],  help="Specify output file format", default="mp4")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-c", "--clips", action="store")


    return opts
