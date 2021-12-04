import datetime
import random

from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

from .utils import format_ts, seconds2minutes, format_time


class File:

    VIDEO_SIZES = {
        '60.0': {
            '1080': '13000',
            '720': '6500',
            '640': '4600',
            '540': '4500',
            '360': '3000'
        },
        '30.0': {
            '1080': '7000',
            '720': '3500',
            '640': '3250',
            '568': '3000',
            '540': '2500',
            '480': '2250',
            '406': '2200',
            '404': '2200',
            '384': '2100',
            '360': '2000',
            '352': '1990',
            '320': '1850',
            '288': '1825',
            '240': '1800',
        },
        '25.0': {
            '1080': '6500',
            '720': '3250',
            '640': '3000',
            '540': '2250',
            '480': '2000',
            '408': '2000',
            '392': '2000',
            '360': '2000'
        },
        '24.0': {
            '1080': '6000',
            '720': '3000',
            '640': '2500',
            '540': '2000',
            '480': '2000',
            '360': '2000',
            '352': '1990',
            '336': '1950',
            '288': '1880',
            '240': '1750'
        }
    }

    def __init__(self, source, start=None, end=None, options=None):
        """Stores information about a media file.

        :param source: Source file or path.
        :param start: Starting position of clip in seconds.
        :param end: Ending position of clip in seconds.
        :param options: Parameters set by user.
        """
        start = format_ts(start)
        end = format_ts(end)
        self.source = source
        self.clip = VideoFileClip(source).subclip(start, end) if start is not None else VideoFileClip(source)
        self.fps = round(self.clip.fps, 0)
        self.bitrate = self.VIDEO_SIZES[str(self.fps)][str(self.clip.h)] + 'k'
        self.duration = self.clip.duration
        self.height = self.clip.size[1]
        self.width = self.clip.size[0]
        self.filename = self.clip.filename

        self.options = options

    def _save(self):
        pass

    def make_time_stamps(self, amount, length, buffer, tail):
        """Generate set of timestamps

        :param amount: Total number of clips to make.
        :param length: Length of each clip.
        :param buffer: Begin grabbing timestamps BUFFER seconds into clip.
        :return timestamps: List of timestamps
        """
        timestamps = []

        duration = self.clip.duration - tail
        frequency = (duration // amount)

        i = 0 + buffer
        while i < duration:
            if self.options.verbose:
                print("Timestamp start: {} ({})".format(i, seconds2minutes(i)))

            i += frequency
            if i >= duration:
                if self.options.verbose:
                    print("Timestamp end: {} ({})".format(i, seconds2minutes(i)))
                break
            length = int(length) if length != 'r' else random.randrange(1, 5)
            timestamps.append([i, i+length])
        return timestamps


class Video(File):
    def __init__(self, source, start=None, end=None, options=None):
        """Make .mp4 or other video file with source video.
        :param source: source video file to convert to mp4
        :param start: if provided, start of clip to convert
        :param end: if provided, end of clip to convert
        """
        File.__init__(self, source, start, end, options)


class Webm(File):

    def __init__(self, source, start=None, end=None, options=None):
        """Make webm file with source video.
        :param source: source video file to convert to mp4
        :param start: if provided, start of clip to convert
        :param end: if provided, end of clip to convert
        """
        File.__init__(self, source, start, end, options)
        self._save()

    def _save(self):
        output = 'webm' + self.filename[6:-4]+'.webm'
        self.clip.write_videofile(output, fps=int(self.fps), bitrate=self.bitrate)
        self.clip.close()


class GIF(File):

    def __init__(self, source, start=None, end=None, options=None):
        File.__init__(self, source, start, end, options)
        self._save()

    def _save(self):
        resized_clip = self.clip.resize(width=480)
        output = self.filename[6:-4]+'.gif'
        resized_clip.write_gif(output, fps=int(self.fps))
        self.clip.close()
