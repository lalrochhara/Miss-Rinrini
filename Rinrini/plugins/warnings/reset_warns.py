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
from Rinrini.database.warnings_mongo import count_user_warn, reset_user_warns
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import isUserAdmin
from Rinrini.helper.get_user import get_user_id


@RinriniCli.on_message(custom_filter.command(commands=('resetwarn')))
async def reset_warn(client, message):
    chat_id = message.chat.id 

    if not await isUserAdmin(message):
        return

    user_info = await get_user_id(message)
    user_id = user_info.id 
    warn_num = count_user_warn(chat_id, user_id)

    print(warn_num)
    
    if warn_num is None:
        await message.reply(
            f"User {user_info.mention} has no warnings to delete! What are you trying to acheive?"
        )
        return

    reset_user_warns(chat_id, user_id)
    await message.reply(
        f"User {user_info.mention} has had all their previous warns removed."
    )
