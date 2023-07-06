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

from Rinrini import RinriniCli
from Rinrini.database.locks_mongo import allowlist_db, get_allowlist
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import check_user
from urlextract import URLExtract


@RinriniCli.on_message(custom_filter.command(commands=('allowlist')))
async def allowlist(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title
    if not await check_user(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        ARG_LIST = message.command[1:]
        INCORRECT_ITEMS = []
        CORRECT_ITEMS = []
        for arg in ARG_LIST:
            extractor = URLExtract()
            URLs_list = extractor.find_urls(arg)
            if arg.startswith('-100'):
                CORRECT_ITEMS.append(int(arg))
            
            elif arg.startswith('@'):
                CORRECT_ITEMS.append(arg)
            
            elif len(URLs_list) != 0:
                for url in URLs_list:
                    if url.startswith('https://'):
                        url = url.replace('https://', '')
                    elif url.startswith('http://'):
                        url = url.replace('http://', '')
                    elif url.startswith('www.'):
                        url= url.replace('www.', '')
                    elif url.startswith('https://www.'):
                        url =url.replace('https://www.', '')
                    elif url.startswith('http://www.'):
                        url = url.replace('http://www.', '')
                CORRECT_ITEMS.append(url)

            else:
                INCORRECT_ITEMS.append(arg)
        
        if (
            len(INCORRECT_ITEMS) != 0
        ):
            text = (
                "I have rejected these args to be added in the `allowlist` due to wrong format of the provided data.\n"
            )
            for item in INCORRECT_ITEMS:
                text += f'- {item}\n'

            await message.reply(
                text
            )
            return
        
        for item in CORRECT_ITEMS:
            allowlist_db(chat_id, item)
        
        text = "These are added to the allowlist.\n"
        for item in CORRECT_ITEMS:
            if len(CORRECT_ITEMS) == 1:
                text = f"'{item}' added to the allowlist."
            else:
                text += f'- {item}\n'
        
        await message.reply(
            text
        )

    else:
        ALLOW_LIST = get_allowlist(chat_id)
        if len(ALLOW_LIST) != 0:
            text = f"The following items are allowlisted in {html.escape(chat_title)}\n"
            for item in ALLOW_LIST:
                text += f'- {item}\n'
            
            await message.reply(
                text
            )
        else:
            await message.reply(
                f"There are no allowlisted items in {html.escape(chat_title)}!"
            )
