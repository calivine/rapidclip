from .video import Video, Webm, GIF
from .editor import Editor
from .utils import form_clip_list, add_extension, format_ts, format_time


class RapidClip:

    def __init__(self, options):
        """Clip video according to options.
        Parameters
        -------------
        options:Dict,
            Dictionary of options to tell
            RapidClip how to process.
        """

        self.options = options

        self.source = add_extension(options.source)
        self.output = None
        if self.options.verbose:
            print(self.options.__dict__)

    def process(self):
        """Completes video processing based on the user supplied Options.

        """
        if self.options.auto:
            source_file = Video(self.source, options=self.options)
            # Generate series of timestamps to based edits to source file on.
            total_clips = self.options.total_clips
            clip_length = self.options.clip_length
            buffer = int(self.options.buffer)
            tail = int(self.options.tail)
            timestamps = source_file.make_time_stamps(total_clips, clip_length, buffer, tail)

            if self.options.verbose:
                print("Filename: {}".format(source_file.filename))
                print("Timestamps: {}".format(timestamps))
                print("Number of clips: {}. Clip length: {} seconds. Start buffer: {}. Tail buffer: {}\n"
                      .format(total_clips, clip_length, buffer, tail))
                print("Source Clip length: {} seconds ({} minutes)\n"
                      .format(source_file.clip.duration, int(source_file.clip.duration) / 60))
                print("Target clip length: {} seconds\n"
                      .format(total_clips * clip_length))

            # Put together an edited clip based on the supplied timestamps.
            #
            self.output = Editor(self.source, timestamps, options=self.options).create()
        elif self.options.clips is not None:
            timestamps = form_clip_list(self.options.clips)
            total_length = 0
            for t in timestamps:
                total_length += format_time(t[1]) - format_time(t[0])
                if self.options.verbose:
                    print(total_length)
            self.options.length = total_length
            if self.options.verbose:
                print(timestamps)

            timestamps_seconds = [[format_time(timestamp) for timestamp in pair] for pair in timestamps]

            self.output = Editor(self.source, timestamps_seconds, options=self.options).create()

        if self.options.webm:
            Webm(self.output)
        if self.options.gif:
            GIF(self.output)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self
