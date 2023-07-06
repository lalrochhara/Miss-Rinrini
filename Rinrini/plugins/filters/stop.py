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
from Rinrini.database.filters_mongo import get_filters_list, stop_db
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import isUserAdmin


@RinriniCli.on_message(custom_filter.command('stop'))
async def stop(client, message):

    chat_id = message.chat.id

    if not await isUserAdmin(message):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            'Not enough arguments provided.'
        )
        return
    
    filter_name = message.command[1]
    if (
        filter_name not in get_filters_list(chat_id)
    ):
        await message.reply(
            'You haven\'t saved any filters on this word yet!'
        )
        return
    
    stop_db(chat_id, filter_name)
    await message.reply(
        f'I\'ve stopped `{filter_name}`.'
    )
