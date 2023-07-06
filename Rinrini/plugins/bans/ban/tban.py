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
import time

from Rinrini import BOT_ID, RinriniCli
from Rinrini.helper import custom_filter
from Rinrini.helper.anon_admin import anonadmin_checker
from Rinrini.helper.chat_status import CheckAllAdminsStuffs, can_restrict_member
from Rinrini.helper.convert import convert_time
from Rinrini.helper.get_user import get_text, get_user_id
from Rinrini.helper.time_checker import get_time, time_string_helper


@RinriniCli.on_message(custom_filter.command(commands=('tban')))
@anonadmin_checker
async def tban(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title
    
    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if user_id == BOT_ID:
        await message.reply(
            "I don't plan to ban myself. NO."
        )
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "I'm not gonna ban an admin. Thanks."
        )
        return
    
    time_args = await get_time(message)
    if time_args:
        cal_time = convert_time(int(time_args[:-1]), time_args[-1])
        until_time = int(time.time() + int(cal_time))
        await RinriniCli.kick_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_time
            )
        
        time_limit, time_format = time_string_helper(time_args)

        text = f"{user_info.mention} was banned for {time_limit} {time_format}.\n"
        raw_reason = get_text(message)
        reason = ' '.join(raw_reason.split()[1:])
        if reason:
            text += f"Reason: {reason}"
        await message.reply(
            text
        )
    
    