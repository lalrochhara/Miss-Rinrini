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


import asyncio
import html
import time

from Rinrini import BOT_ID, RinriniCli
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import (can_restrict_member, isBotCan,
                                       isUserAdmin)
from Rinrini.helper.disable import disable
from Rinrini.helper.get_user import get_text, get_user_id


@RinriniCli.on_message(custom_filter.command(commands=('kickme'), disable=True))
@disable
async def kick(client, message):
        
    chat_id = message.chat.id 
    user_id = message.from_user.id 

    if not await isBotCan(message, permissions='can_restrict_members'):
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "Hahahaha. I'm not willing to ban myself."
        )
        return
    
    await RinriniCli.kick_chat_member(
        chat_id,
        user_id,
        int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
        )
        
    text = "Ara Ara! Sayonara (´；v；`)"
    reason = get_text(message)
    if reason:
        text += f"Given reason: {reason}"

    await message.reply(
        text
    )
    
    # Unbanning proceess and wait 5 sec to give server to kick user first
    await asyncio.sleep(5) 
    await RinriniCli.unban_chat_member(chat_id, user_id)
