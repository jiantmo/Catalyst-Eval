from thinkingbox.common import Judge, TestContext

"""!
scenario: weather_simple
"""


def test_slotfilling_location_1(x: TestContext, judge: Judge):
    """!
    query: |
        What is the Weather near me ?
    user_context: |
        You are in Seattle
    """

    # Should return weather at Seattle
    assert judge.text_yesno(
        x.response, "Does the message confirm the weather for Seattle?"
    )


def test_slotfilling_location_2(x: TestContext, judge: Judge):
    """!
    query: |
        What is the forecast for the next seven days?
    user_context: |
        You live in Seattle
    """

    assert judge.text_yesno(
        x.response, "Does the message confirm forecast for Seattle for next 7 days ?"
    )


def test_slotfilling_location_3(x: TestContext, judge: Judge):
    """!
    query: |
        Are there any weather alerts near me for today?
    user_context: |
        You are in Orlando and the current date is 05-29-2025.
    """
    # Should check for weather alerts in Orlando
    assert judge.text_yesno(
        x.response, "Does the message confirm alert for Orlando on 05-29-2025?"
    )


def test_slotfilling_location_4(x: TestContext, judge: Judge):
    """!
    query: |
        Are there any Flash Flood Warning near me for date 2025-05-01 ?
    user_context: |
        You are in Seattle and want Flash Flood warnings for Seattle.
    """
    # Should check for any alerts
    assert judge.text_yesno(
        x.response,
        "Does the message confirm that there is no Flash Flood Warnings in Seattle on the date 2025-05-01 ?",
    )


def test_slotfilling_location_5(x: TestContext, judge: Judge):
    """!
    query: |
        I want to check for all alerts for different dates near me ?
    user_context: |
        You want alerts for Seattle on date 2025-05-29.
    """
    # Should return weather at Seattle
    assert judge.text_yesno(
        x.response,
        "Does the message confirm that there is Special Marine Warning for Seattle on the date 2025-05-29 ?",
    )
