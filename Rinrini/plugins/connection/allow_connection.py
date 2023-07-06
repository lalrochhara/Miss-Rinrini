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


from Rinrini import RinriniCli
from Rinrini.database.connection_mongo import (allow_collection,
                                              get_allow_connection)
from Rinrini.helper import custom_filter
from Rinrini.helper.anon_admin import anonadmin_checker
from Rinrini.helper.chat_status import isUserAdmin
from Rinrini.plugins.connection.connection import connection

ALLOW_CONNECTION_TRUE = ['on', 'yes' ,'true']
ALLOW_CONNECTION_FALSE = ['off', 'no' ,'false']

@RinriniCli.on_message(custom_filter.command(commands=('allowconnection')))
@anonadmin_checker
async def allow_connection(client, message):
    
    if await connection(message) is not None:
        chat_id = connection(message)
        chat_title = None
    else:
        chat_id = message.chat.id 
        chat_title = message.chat.title 

    if not await isUserAdmin(message):
        return 

    if (
        len(message.command) >= 2
    ):
        get_arg = message.command[1]

        if (
            get_arg in ALLOW_CONNECTION_TRUE
        ):
            allow_collection(chat_id, chat_title, allow_collection=True)
            await message.reply(
                "Allow all users in connection.",
                quote=True
            )
        elif (
            get_arg in ALLOW_CONNECTION_FALSE
        ):
            allow_collection(chat_id, chat_title, allow_collection=False)
            await message.reply(
                "Disallow all users in connection.",
                quote=True
            )
        else:
            await message.reply(
                f"I got {get_arg} arg!"
            )
    else:
        if get_allow_connection(chat_id):
            t_message = (
                "Users are allowed to connect chat to PM."
            )
        else:
            t_message = (
                "users are ** allowed to connect chat to PM."
            )
        
        await message.reply(
            t_message,
            quote=True
        )
    