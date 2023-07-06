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


from Rinrini import BOT_ID, RinriniCli
from Rinrini.database.federation_mongo import (get_connected_chats,
                                              get_fed_admins,
                                              get_fed_from_chat, get_fed_name,
                                              is_user_fban, user_unfban)
from Rinrini.helper import custom_filter
from Rinrini.helper.get_user import get_user_id


@RinriniCli.on_message(custom_filter.command(commands=('unfban')))
async def unfed_ban(client, message):
    chat_id = message.chat.id
    user_info = await get_user_id(message)
    userID = user_info.id 
    
    bannerMention = message.from_user.mention 
    banner_name = message.from_user.first_name
    bannedID = message.from_user.id

    fed_id = get_fed_from_chat(chat_id)
    fed_name = get_fed_name(fed_id=fed_id)
    get_user = await RinriniCli.get_users(
                user_ids=userID
            )

    FED_ADMINS = get_fed_admins(fed_id)
    
    if userID == BOT_ID:
        await message.reply(
             "How do you think I would've fbanned myself that you are trying to unfban me? Never seen such retardedness ever before."
        )
        return
    
    if bannedID not in FED_ADMINS:
        await message.reply(
            f"You aren't a federation admin of {fed_name}."
        )
        return

    if (
        message.reply_to_message 
        and len(message.command) >= 2
    ):
        reason_text = ' '.join(message.text.split()[1:])   
    
    elif (
        len(message.command) >= 3
    ):
        reason_text = ' '.join(message.text.split()[2:])  

    else:
        reason_text = 'No reason was given'
     
    
    reason = f"{reason_text} // un-Fbanned by {banner_name} id {bannedID}"
    if is_user_fban(fed_id, userID):
        user_unfban(fed_id, userID)
    else:
        pass

    # await message.reply(
    #     unfed_message
    # )

