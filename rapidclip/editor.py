import datetime

from moviepy.editor import concatenate_videoclips, TextClip, CompositeVideoClip

from .video import File
from .utils import seconds2minutes


class Editor:

    def __init__(self, source, timestamps, options):
        """ Create new Video based on timestamps from source.

        :param source:
        :param timestamps:
        :param options:
        """
        self.source = source
        self.options = options
        self.clips = self._fill_clip_list(timestamps)

    def create(self):
        """Concatenates video clips

        :return new_file: the new video file's name
        """
        new_file = self._make_filename()

        self._paste_clips(new_file)
        return new_file[6:-4]+'.mp4'

    def _fill_clip_list(self, timestamps):
        # Empty list for clips.
        clip_list = []
        self.options.length = 0
        for timestamp in timestamps:
            # New video File created at start = timestamp[0], stop = timestamp[1]
            # Depreciated:
            # new_clip = File(self.source, timestamp[0], timestamp[1]).clip
            # add Video clip to list
            self.options.length += timestamp[1] - timestamp[0]
            clip_list.append(File(self.source, timestamp[0], timestamp[1]).clip)
        return clip_list

    def _make_filename(self):
        # Creates a pseudo random filename for output file
        now = datetime.datetime.now()
        iso = now.replace().isoformat()
        mask = "".join(iso.split('T')[1].replace(':', '').replace('.', '').split('-'))

        return "{}_{}".format(mask, self.source)

    def _paste_clips(self, destination):
        """Concatenate clips

        :param destination:
        """
        # Set whether write_videofile should output  a progress bar or not.
        logging = 'bar' if self.options.verbose else None

        # Concatenate clips together, one after the other.
        final_clip = concatenate_videoclips(self.clips)

        # Add watermark
        ic = TextClip("made with RapidClip", fontsize=25).set_position(("right", "top"))
        final_clip = CompositeVideoClip([final_clip, ic]).set_duration(self.options.length)
        final_clip.write_videofile(destination[6:-4] + '.mp4', logger=logging)
        final_clip.close()
        # Close open clip connections.
        for clip in self.clips:
            clip.close()
