# SPDX-FileCopyrightText: 2026 Sarah Gäumann <sarahgaeumann01@gmail.com>
#
# SPDX-License-Identifier: MIT

from app.url_cleaning import clean_url


def test_cleanse_url():
    expected_url = "https://test.com"

    slash_url = "https://test.com/"
    port_url = "https://test.com:443/"
    uppercase_url = "https://TeSt.com/"

    assert clean_url(uppercase_url) == expected_url
    assert clean_url(port_url) == expected_url
    assert clean_url(slash_url) == expected_url
