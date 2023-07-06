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

from Rinrini import RinriniCli
from Rinrini.database.notes_mongo import NoteList
from Rinrini.helper import custom_filter
from Rinrini.helper.disable import disable
from Rinrini.helper.get_data import GetChat
from Rinrini.plugins.connection.connection import connection


@RinriniCli.on_message(custom_filter.command(commands=(['notes', 'saved']), disable=True))
@disable
async def Notes(client, message):
    if await connection(message) is not None:
        chat_id = await connection(message)
        chat_title = await GetChat(chat_id)
    else:    
        chat_id = message.chat.id
        chat_title = message.chat.title

        if (
            message.chat.type == 'private'
        ):
            chat_title = 'local'

    Notes_list = NoteList(chat_id)
    
    NoteHeader = f"List of notes  in {html.escape(chat_title)}:\n"
    if (
        len(Notes_list) != 0
    ): 
        for notes in Notes_list:
            NoteName = f" • `#{notes}`\n"
            NoteHeader += NoteName
        await message.reply(
            (
                f"{NoteHeader}\n"
                "You can retrieve these notes by using `/get notename`, or `#notename`"
            ),
            quote=True
        )
        
    else:
        await message.reply(
            f"No notes in {chat_title}.",
            quote=True
        )
