from questions.challenge1 import convert_12_hour_time_to_24_hour_time


def test_convert_12_hour_time_to_24_hour_time():
    """
        Converting a 12-hour time like "8:30 am" or "8:30 pm" 
        to 24-hour time (like "0830" or "2030").
    """
    result1 = convert_12_hour_time_to_24_hour_time(8, 30, "am")
    result2 = convert_12_hour_time_to_24_hour_time(8, 30, "pm")
    result3 = convert_12_hour_time_to_24_hour_time(12, 00, "am")
    result4 = convert_12_hour_time_to_24_hour_time(12, 00, "pm")
    result5 = convert_12_hour_time_to_24_hour_time(12, 15, "am")
    result6 = convert_12_hour_time_to_24_hour_time(12, 15, "pm")
    result7 = convert_12_hour_time_to_24_hour_time(11, 30, "am")
    result8 = convert_12_hour_time_to_24_hour_time(11, 30, "pm")

    assert result1 == "0830"
    assert result2 == "2030"
    assert result3 == "1200"
    assert result4 == "0000"
    assert result5 == "1215"
    assert result6 == "0015"
    assert result7 == "1130"
    assert result8 == "2330"
