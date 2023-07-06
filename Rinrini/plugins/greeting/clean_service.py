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
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import CheckAllAdminsStuffs
from Rinrini.database.welcome_mongo import (
    SetCleanService,
    GetCleanService
)
from Rinrini.plugins.connection.connection import connection
from Rinrini.helper.anon_admin import anonadmin_checker

CLEAN_SERVICE_TRUE = ['on', 'yes']
CLEAN_SERVICE_FALSE = ['off', 'no']

@RinriniCli.on_message(custom_filter.command(commands=('cleanservice')))
@anonadmin_checker
async def CleanService(client, message):
    
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not (
        await  CheckAllAdminsStuffs(message, permissions='can_delete_messages')
    ):
        return 

    if (
        len(message.command) >= 2
    ):
        get_clean_service = message.command[1]

        if (
            get_clean_service in CLEAN_SERVICE_TRUE
        ):
            clean_service = True
            SetCleanService(chat_id, clean_service)
            await message.reply(
                "I'll be deleting all service messages from now on!",
                quote=True
            )

        elif (
            get_clean_service in CLEAN_SERVICE_FALSE
        ):
            clean_service = False 
            SetCleanService(chat_id, clean_service)
            await message.reply(
                "I'll leave service messages.",
                quote=True
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off",
                quote=True
            )
    elif (
        len(message.command) == 1
    ):
        if GetCleanService(chat_id):
            CleanServiceis = "I am currently deleting service messages when new members join or leave."

        else:
            CleanServiceis = "I am not currently deleting service messages when members join or leave."
        
        await message.reply(
            (
                f'{CleanServiceis}\n\n'
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True
        )