def _fuzz_location(lat, lon, radius):
    """
    Shift the given point randomly to some location within the specified
    radius.

    :param lat: The latitude of the point.
    :param lon: The longitude of the point.
    :param radius: The radius describing the maximal possible shift distance
                   from the given point in meters.
    :return: A shifted point that is at most radius meters from the starting
             point. Returned as (latitude, longitude)
    """
    start = Point(lat, lon)
    length = random.uniform(0, radius)
    bearing = random.uniform(0, 360)

    distance_vec = distance(meters=length)

    new_pt = distance_vec.destination(start, bearing)
    return new_pt.latitude, new_pt.longitude 