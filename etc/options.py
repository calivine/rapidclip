

class Options:
    """ Contains configuration options provided by user.

    """
    def __init__(self, arguments, source):
        """

        :param arguments:  parsed arguments
        :param source:     filename
        """
        self.source = source
        self.length = int(arguments.length[0]) * int(arguments.length[1])
        self.total_clips = int(arguments.length[0])
        self.clip_length = int(arguments.length[1])
        self.auto = arguments.auto
        self.webm = arguments.webm
        self.gif = arguments.gif
        self.clips = arguments.clips
        self.batch = arguments.batch
        self.buffer = arguments.buffer
        self.tail = arguments.tail
        self.verbose = arguments.verbose
