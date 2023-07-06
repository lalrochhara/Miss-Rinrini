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


from Rinrini import OWNER_ID, RinriniAPI, RinriniCli
from Rinrini.helper import custom_filter


@RinriniCli.on_message(custom_filter.command(commands=('promoteapi')))
async def promote_api_level(client, message):

    if (
        message.chat.type == 'private'
    ):
        return
        
    if not (
        message.from_user.id in OWNER_ID
    ):
        return 
    
    if not message.reply_to_message:
        return 
    
    status, operation = RinriniAPI.promote_api(message.reply_to_message.from_user.id)

    if operation:
        await message.reply_to_message.reply(
            f"{message.reply_to_message.from_user.mention} has been promoted to `api_level: admin`."
        )
    
    else:
        await message.reply(
            status
        )


