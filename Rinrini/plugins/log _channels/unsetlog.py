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
from Rinrini.database.log_channels_mongo import unset_log_db
from Rinrini.helper import custom_filter
from Rinrini.helper.anon_admin import anonadmin_checker
from Rinrini.helper.chat_status import isUserCan
from Rinrini.plugins.connection.connection import connection


@RinriniCli.on_message(custom_filter.command(commands=('unsetlog')))
@anonadmin_checker
async def unset_log(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id
    
    if not await isUserCan(message, permissions='can_change_info'):
        return

    unset_log_db(chat_id)

    await message.reply(
        "Successfully unset log channel. Admin actions will no longer be logged.",
        quote=True
    )
    
