# SPDX-FileCopyrightText: 2026 Sarah Gäumann <sarahgaeumann01@gmail.com>
#
# SPDX-License-Identifier: MIT

# normalizes the given URL.

from urllib.parse import urlsplit, urlunsplit

from loguru import logger

DEFAULT_PORTS = {80, 443}


def clean_url(url: str) -> str:
    # convert url to lowercase
    url = url.strip().lower()
    split_url = urlsplit(url=url)
    # remove default port
    netloc = split_url.netloc
    if split_url.port in DEFAULT_PORTS:
        port = str(split_url.port)
        netloc = split_url.netloc.replace(":" + port, "")
        logger.debug(split_url.netloc)
    # remove query and fragment
    result = urlunsplit((split_url.scheme, netloc, split_url.path, "", ""))
    logger.debug(result)
    
    return result
