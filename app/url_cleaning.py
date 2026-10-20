# SPDX-FileCopyrightText: 2026 Sarah Gäumann <sarahgaeumann01@gmail.com>
#
# SPDX-License-Identifier: MIT

# normalizes the given URL.

from loguru import logger


def clean_url(url: str) -> str:
    # convert url to lowercase
    url = url.strip().lower()
    # remove slash at the end
    url = url.rstrip("/")
    # remove port
    url = "".join([char for char in url if not char.isdigit()])
    cleansed_url = url.rstrip(":")

    logger.debug(cleansed_url)
    return cleansed_url
