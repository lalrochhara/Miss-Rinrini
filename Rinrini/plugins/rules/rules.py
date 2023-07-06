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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Rinrini import BOT_USERNAME, RinriniCli
from Rinrini.database.rules_mongo import (get_private_note, get_rules,
                                         get_rules_button)
from Rinrini.helper import custom_filter
from Rinrini.helper.button_gen import button_markdown_parser
from Rinrini.helper.disable import disable
from Rinrini.helper.get_data import GetChat
from Rinrini.helper.note_helper.note_fillings import \
    NoteFillings as rules_filler


@RinriniCli.on_message(custom_filter.command(commands=('rules'), disable=True))
@disable
async def rules(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title 
    rules_text = get_rules(chat_id)
    if rules_text is None:
        await message.reply(
            "He group hian eng rules mah an la siam lo... Sawmna ka dawng ang ah pawh ka ngai lo ang.",
            quote=True
        )
        return
    
    if not get_private_note(chat_id):
        rules_text, buttons = button_markdown_parser(rules_text)
        button_markdown = None
        if len(buttons) > 0:
            button_markdown = InlineKeyboardMarkup(buttons)

        rules_text = rules_filler(message, rules_text)

        await message.reply(
            (
                f"The rules for `{html.escape(chat_title)}` are:\n\n"
                f"{rules_text}"
            ),
            reply_markup=button_markdown,
            quote=True
        )
    else:
        button_text = get_rules_button(chat_id)
        button = [[InlineKeyboardButton(text=button_text, url=f'http://t.me/{BOT_USERNAME}?start=rules_{chat_id}')]]

        await message.reply(
            "Group rules i hriat duh chuan button khu hmet rawh!",
            reply_markup=InlineKeyboardMarkup(button),
            quote=True
        )

async def rulesRedirect(message):
    chat_id = int(message.command[1].split('_')[1])
    chat_title = await GetChat(chat_id)
    rules_text = get_rules(chat_id)
    
    rules_text, buttons = button_markdown_parser(rules_text)
    button_markdown = None
    if len(buttons) > 0:
        button_markdown = InlineKeyboardMarkup(buttons)

    rules_text = rules_filler(message, rules_text)
    await message.reply(
        (
            f"He `{html.escape(chat_title)}` group rules te chu:\n\n"
            f"{rules_text}"
        ),
        reply_markup=button_markdown,
        quote=True
    )
