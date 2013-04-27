import datetime

def parse_iso_datetime(strdate):
    """
    Tries to convert date from ISO format to a datetime object. Returns None if it fails

    :strdate: String formated with ISO format
    
    """
    if strdate is not None:
        try :
            return datetime.datetime.strptime(strdate, "%Y-%m-%dT%H:%M:%S")
        except ValueError :
            try:
                return datetime.datetime.strptime(strdate, "%Y-%m-%dT%H:%M:%S.%f")
            except ValueError:
                return None

    return None
