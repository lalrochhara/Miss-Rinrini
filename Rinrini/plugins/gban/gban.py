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


from Rinrini import BOT_ID, OWNER_ID, SUDO_USERS, RinriniAPI, RinriniCli
from Rinrini.database.users_mongo import GetAllChats
from Rinrini.helper import custom_filter
from Rinrini.helper.get_user import get_text, get_user_id


@RinriniCli.on_message(custom_filter.command(commands=('gban')))
async def Gban(client, message):

    if not (
        message.from_user.id in SUDO_USERS
        or message.from_user.id in OWNER_ID
    ):
        return 
    
    admin_id = message.from_user.id 
    user_info = await get_user_id(message)
    GbannedUser = user_info.id 
    
    reason = get_text(message)

    operation, request_message = RinriniAPI.gban_protocol(admin_id, GbannedUser, reason)
    if operation:
        CHATS_LIST = GetAllChats()
        BannedChats = []
        for chat_id in CHATS_LIST:
            GetData = await RinriniCli.get_chat_member(
                chat_id=chat_id,
                user_id=BOT_ID
            )
            if GetData['can_restrict_members']:
                try:
                    if await RinriniCli.kick_chat_member(
                        chat_id,
                        GbannedUser
                    ):
                        BannedChats.append(chat_id)
                except:
                    continue
            else:
                continue
        
        await message.reply(
            text=(
                "New banned user:\n"
                f"Admin: `{admin_id}`\n"
                f"GBanned user: `{GbannedUser}`\n"
                f"Reason: `{reason}`\n"
                f"Affected chat: `{len(BannedChats)}`"
            )
        )
    else:
        await message.reply(
            request_message
        )
    