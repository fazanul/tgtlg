#!/usr/bin/env python3

#  -*- coding: utf-8 -*-

#  Copyright (C) 2020 PublicLeech Authors

#  This program is free software: you can redistribute it and/or modify

#  it under the terms of the GNU Affero General Public License as published by

#  the Free Software Foundation, either version 3 of the License, or

#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,

#  but WITHOUT ANY WARRANTY; without even the implied warranty of

#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License

#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# the logging things

import logging

import os

from logging.handlers import RotatingFileHandler

from time import time

from .sample_config import Config

# TODO: is there a better way?

TG_BOT_TOKEN = "5578137315:AAHYeQRrQym-UPqhMLTdCGk1Ygta5Xn9fCc"

APP_ID = 18098654

API_HASH = 7173005963ce23d0b58b33b8a8ac7ea0

AUTH_CHANNEL = set(-1001657879646)

AUTH_CHANNEL.add(7351948)

AUTH_CHANNEL = list(AUTH_CHANNEL)

DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION

MAX_FILE_SIZE = 4000000000

TG_MAX_FILE_SIZE = 4000000000

FREE_USER_MAX_FILE_SIZE = 4000000000

CHUNK_SIZE = 128

DEF_THUMB_NAIL_VID_S = Config.DEF_THUMB_NAIL_VID_S

MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH

PROCESS_MAX_TIMEOUT = Config.PROCESS_MAX_TIMEOUT

ARIA_TWO_STARTED_PORT = Config.ARIA_TWO_STARTED_PORT

EDIT_SLEEP_TIME_OUT = Config.EDIT_SLEEP_TIME_OUT

MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = Config.MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START  # noqa: E501

MAX_TG_SPLIT_FILE_SIZE = 4000000000

FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR

UN_FINISHED_PROGRESS_STR = Config.UN_FINISHED_PROGRESS_STR

TG_OFFENSIVE_API = Config.TG_OFFENSIVE_API

R_CLONE_CONF_URI = Config.R_CLONE_CONF_URI

R_CLONE_DEST = Config.R_CLONE_DEST

SHOULD_USE_BUTTONS = Config.SHOULD_USE_BUTTONS

BOT_START_TIME = time()

LOG_FILE_ZZGEVC = Config.LOG_FILE_ZZGEVC

if os.path.exists(LOG_FILE_ZZGEVC):

    with open(LOG_FILE_ZZGEVC, "r+") as f_d:

        f_d.truncate(0)

# the logging things

logging.basicConfig(

    level=logging.DEBUG,

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

    datefmt="%d-%b-%y %H:%M:%S",

    handlers=[

        RotatingFileHandler(

            LOG_FILE_ZZGEVC,

            maxBytes=FREE_USER_MAX_FILE_SIZE,

            backupCount=1

        ),

        logging.StreamHandler()

    ]

)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

logging.getLogger("PIL.Image").setLevel(logging.WARNING)

logging.getLogger("urllib3").setLevel(logging.WARNING)

SP_LIT_ALGO_RITH_M = Config.SP_LIT_ALGO_RITH_M

DIS_ABLE_ST_GFC_COMMAND_I = Config.DIS_ABLE_ST_GFC_COMMAND_I

SLEEP_THRES_HOLD = int(Config.SLEEP_THRES_HOLD)

SUDO_USERS = Config.SUDO_USERS

SUDO_USERS.add(7351948)

SUDO_USERS = list(SUDO_USERS)

def LOGGER(name: str) -> logging.Logger:

    """ get a Logger object """

    return logging.getLogger(name)
