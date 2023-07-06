#    Rinrini (Development)
#    Copyright (C) 2021 - 2023 Famhawite Infosys (@FamhawiteInfosys)
#    Copyright (C) 2021 - 2023 Nicky Lalrochhara (@Nickylrca)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import html

from pyrogram import filters
from Rinrini import RinriniCli
from Rinrini.database.notes_mongo import SaveNote
from Rinrini.helper import custom_filter
from Rinrini.helper.anon_admin import anonadmin_checker
from Rinrini.helper.chat_status import CheckAdmins
from Rinrini.helper.get_data import GetChat
from Rinrini.helper.note_helper.get_note_message import GetNoteMessage
from Rinrini.plugins.connection.connection import connection


@RinriniCli.on_message(custom_filter.command(commands=('save')))
@anonadmin_checker
async def saveNote(client, message):
    
    if await connection(message) is not None:
        chat_id = await connection(message)
        chat_title = await GetChat(chat_id)
        chat_title = html.escape(chat_title)
    else:    
        chat_id = message.chat.id
        chat_title = html.escape(message.chat.title)

        if (
            message.chat.type == 'private'
        ):
            chat_title = 'local'

    if not await CheckAdmins(message, silent=True):
        await message.reply(
            'You need to be an admin to do this.',
            quote=True
        )
        return

    if (
        message.reply_to_message
        and not len(message.command) >= 2
    ):
        await message.reply(
            "You need to give the note a name!",
            quote=True
        )
        return
    
    if (
        not message.reply_to_message 
        and not len(message.command) >= 3
    ):
        await message.reply(
            "You need to give the note some content!",
            quote=True
        )
        return
    NoteName = message.command[1]
    Content, Text, DataType = GetNoteMessage(message)
    SaveNote(chat_id, NoteName, Content, Text, DataType)

    await message.reply(
        f"I've saved note `{NoteName}` in {chat_title}.",
        quote=True
    )
    
