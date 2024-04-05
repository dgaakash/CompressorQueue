#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1322549723
    OWNER = config("OWNER")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset superfast -c:v libx265 -s 854x480 -x265-params "bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1" -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5 -metadata title="@𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛" -metadata author="@𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛" -metadata:s:s title="@𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛" -metadata:s:a title="@𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛" -metadata:s:v title="@𝙰𝚗𝚒𝚖𝚎_𝚆𝚊𝚛𝚒𝚘𝚛" "{}"',
    )
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
