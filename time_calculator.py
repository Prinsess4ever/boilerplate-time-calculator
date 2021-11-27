def add_time(start, duration, day=None):
    verander_start = start.replace(":", " ")
    verander_duration = duration.replace(":", " ")

    eerste = verander_start.split()
    tweede = verander_duration.split()

    hours = int(eerste[0]) + int(tweede[0])
    minutes = int(eerste[1]) + int(tweede[1])
    days = 0
    week = ["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    if minutes >= 60:
        minutes -= 60
        hours += 1

    if hours >= 24:
        while hours >= 24:
            hours = hours - 24
            days += 1

    if hours >= 12:
        hours = hours - 12
        if hours <= 0:
            hours = 12
        if eerste[2] == "PM":
            eerste[2] = "AM"
            days += 1
        else:
            eerste[2] = "PM"

    if day is not None:
        day = day.lower()
        index = week.index(day)
        if days > 0:
            index += days
        else:
            index = index
        next_day = week[index]
        day = next_day.capitalize()


    oplossing = f"{hours}:{minutes:02d} {eerste[2]}"
    if day is not None:
        oplossing += ", " + day

    if days > 1:
        oplossing += f" ({days} days later)"
    elif days == 1 and hours != 12:
        oplossing += " (next day)"

    return oplossing


def test_do():
    assert add_time("11:43 PM", "24:20", "tueSday") == '12:03 AM, Thursday (2 days later)'
    assert add_time("6:30 PM", "205:12") == '7:42 AM (9 days later)'
    assert add_time("11:43 PM", "00:20") == '12:03 AM'
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"
    assert add_time("10:10 PM", "3:30") == '1:40 AM (next day)'
    assert add_time("3:00 PM", "3:10") == "6:10 PM"
    assert add_time("11:43 AM", "00:20") == '12:03 PM'

