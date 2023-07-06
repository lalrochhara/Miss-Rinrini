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
from Rinrini.database.blocklists_mongo import add_blocklist_db
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import CheckAllAdminsStuffs
from Rinrini.helper.get_data import get_text_reason


@RinriniCli.on_message(custom_filter.command(commands=['addblocklist', 'addblacklist']))
async def add_blocklist(client, message):

    chat_id = message.chat.id 
    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            (
                "You're gonna need to provide a blocklist trigger and reason!\n"
                "eg: `/addblocklist \"the admins suck\" Respect your admins!`"
            )
        )
        return
    
    text, reason = get_text_reason(message)
    add_blocklist_db(chat_id, text, reason)
    await message.reply(
        f"I have added blocklist filter '`{text}`'!",
        quote=True
    )


    

    
        