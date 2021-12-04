def add_extension(source, ext=".mp4"):
    if source.endswith(".mp4"):
        return source
    elif source.endswith(".avi"):
        return source
    elif source.endswith(".mov"):
        return source
    elif source.endswith(".wmv"):
        return source
    else:
        return source + ext


def form_clip_list(inpt):
    """Serialize custom timestamp option.
    """
    clip_list = []
    clip_list_raw = inpt[1:-1]
    cll = clip_list_raw.split(",")
    cll.reverse()
    st = True
    while len(cll) > 0:
        ts = cll.pop()
        if st:
            start = ts
            st = False
        else:
            end = ts
            st = True
            clip_list.append([start, end])
    return clip_list


def format_ts(ts):
    """Convert timestamp from MM:SS to total seconds

    :param ts: String/Tuple
    :return: timestamp in seconds
    """

    if ':' in str(ts):
        timestamp = ts.split(':')
        return int(timestamp[0]) * 60 + int(timestamp[1])
    else:
        return ts


def seconds2minutes(ts):
    minutes = ts // 60
    remaining = round(ts % 60, 0)
    output = "{}:{}".format(int(minutes), int(remaining))
    return output


def format_time(ts):
    """
    Clip can take timestamp in the following forms:
        - seconds (15.34)
        - min, sec (1, 12.12)
        - hour, min, sec (1, 5, 9)
        - string '01:03:05.35'
    :param ts: one of the above formats
    :return: Timestamp in seconds or display
    """
    if isinstance(ts, tuple):
        if len(ts) == 2:
            return ts[0] * 60 + ts[1]
        elif len(ts) == 3:
            return ts[0] * 60 + ts[1] * 60 + ts[2]
        else:
            return ts[0]
    else:
        # Use format string to timestamp function
        return format_ts(ts)
