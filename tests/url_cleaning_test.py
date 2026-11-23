# SPDX-FileCopyrightText: 2026 Sarah Gäumann <sarahgaeumann01@gmail.com>
#
# SPDX-License-Identifier: MIT

from app.url_cleaning import clean_url


def test_cleanse_url():
    expected_url = "https://test.com/"

    slash_url = "https://test.com/"
    port_url = "https://test.com:443/"
    port_url_1 = "https://test.com:8080/"
    uppercase_url = "https://TeSt.com/"
    advanced_url = "https://algomaster.io/learn/system-design-interviews/design-url-shortener#this-is-a-test"
    query_param_url = "https://example.com/path/?name=Branch&products=[Journeys,Email,Universal%20Ads]"
    number_url = "https://test2test.com/"
    query_url = "https://test.com?x=y"

    assert clean_url(uppercase_url) == expected_url
    assert clean_url(port_url) == expected_url
    assert clean_url(slash_url) == expected_url
    assert clean_url(advanced_url) == "https://algomaster.io/learn/system-design-interviews/design-url-shortener"
    assert clean_url(query_param_url) == "https://example.com/path/"
    assert clean_url(port_url_1) == port_url_1
    assert clean_url(number_url) == number_url
    assert clean_url(query_url) == "https://test.com"
