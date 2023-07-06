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

from pyrogram.types import ChatPermissions
from Rinrini import BOT_ID, RinriniCli
from Rinrini.helper import custom_filter
from Rinrini.helper.anon_admin import anonadmin_checker
from Rinrini.helper.chat_status import isBotCan, isUserBanned, isUserCan
from Rinrini.helper.get_user import get_text, get_user_id


@RinriniCli.on_message(custom_filter.command(commands=('unban')))
@anonadmin_checker
async def ban(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isBotCan(message, permissions='can_restrict_members'):
        return
    if not await isUserCan(message, permissions='can_restrict_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if not await isUserBanned(chat_id, user_id):
        await message.reply(
            "So you're trying to unban someone who has never been banned? Good use of brain!"
        )
        return

    await RinriniCli.unban_chat_member(
        chat_id,
        user_id
        )
    
    await message.reply(
        "Alright, they can join again."
    )
