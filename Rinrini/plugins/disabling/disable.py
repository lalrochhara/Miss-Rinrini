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
from Rinrini.database.disable_mongo import disable_db
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import check_user
from Rinrini.helper.custom_filter import DISABLE_COMMANDS


@RinriniCli.on_message(custom_filter.command(commands=('disable')))
async def disable(client, message):
    chat_id = message.chat.id 

    if not await check_user(message, permissions='can_change_info'):
        return

    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You haven't specified a command to disable."
            )
        return
    
    disable_args = message.command[1:]

    DISABLE_ITMES = []
    INCORRECT_ITEMS = []
    
    for disable_arg in disable_args:
        if (
            disable_arg not in DISABLE_COMMANDS
        ):
            INCORRECT_ITEMS.append(disable_arg)
        else:
            DISABLE_ITMES.append(disable_arg)

    if (
        len(INCORRECT_ITEMS) != 0
    ):
        text = (
            "Unknown command to disable:\n"
        )
        for item in INCORRECT_ITEMS:
            text += f'- `{item}`\n'
        text += "Check /disableable!"
        await message.reply(
                text
            )
        return
            
    for items in DISABLE_ITMES:
        disable_db(chat_id, items)

    text = 'Disabled:\n'
    for disable_arg in DISABLE_ITMES:
        if len(DISABLE_ITMES) != 1:
            text += f'- `{disable_arg}`\n'
        else:
            text = (
                f"Disable `{disable_arg}`."
            )
    
    await message.reply(
        text
    )
