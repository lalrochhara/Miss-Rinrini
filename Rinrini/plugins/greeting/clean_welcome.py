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
from Rinrini.helper.chat_status import (
    CheckAdmins
    )
from Rinrini.database.welcome_mongo import (
    SetCleanWelcome,
    GetCleanWelcome
)
from Rinrini.plugins.connection.connection import connection
from Rinrini.helper.anon_admin import anonadmin_checker

CLEAN_WELCOME_TRUE = ['on', 'yes']
CLEAN_WELCOME_FALSE = ['off', 'no']

@RinriniCli.on_message(custom_filter.command(commands=('cleanwelcome')))
@anonadmin_checker
async def CleanWelcome(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await  CheckAdmins(message):
        return 
    
    if (
        len(message.command) >= 2
    ):
        get_args = message.command[1]
        if (
            get_args in CLEAN_WELCOME_TRUE
        ):
            clean_welcome = True 
            SetCleanWelcome(chat_id, clean_welcome)
            await message.reply(
                "I'll be deleting all old welcome/goodbye messages from now on!",
                quote=True
            )
        
        elif (
            get_args in CLEAN_WELCOME_FALSE
        ):
            clean_welcome = False
            SetCleanWelcome(chat_id, clean_welcome)
            await message.reply(
                "I'll leave old welcome/goodbye messages.",
                quote=True
            )
    elif (
        len(message.command) == 1
    ):
        if (
            GetCleanWelcome(chat_id)
        ):
            CleanMessage = "I am currently deleting old welcome messages when new members join."
        else:
            CleanMessage = "I am not currently deleting old welcome messages when new members join."
        
        await message.reply(
            (
                f'{CleanMessage}\n\n'
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True
        )