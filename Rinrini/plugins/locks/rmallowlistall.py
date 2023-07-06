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

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Rinrini import RinriniCli
from Rinrini.database.locks_mongo import rmallowall_db
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import isUserAdmin


@RinriniCli.on_message(custom_filter.command(commands=("rmallowlistall")))
async def rmallowlistall(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title

    if not await isUserAdmin(message):
        return

    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text='Delete allowlist', callback_data=f'allowlist_confirm')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data=f'allowlist_cancel')
        ]]
    )

    await message.reply(
        text=f'Are you sure you would like to remove **ALL** of the allowlist in {html.escape(chat_title)}? This action cannot be undone.',
        reply_markup=keyboard
    )

@RinriniCli.on_callback_query(filters.create(lambda _, __, query: 'allowlist_' in query.data))
async def rmallowlistall_callback(client: RinriniCli, callback_query: CallbackQuery):

    chat_id = callback_query.message.chat.id
    query_data = callback_query.data.split('_')[1]

    if not await isUserAdmin(callback_query, chat_id=chat_id, silent=True):
        await callback_query.answer(
            text="You are not allowed to do that."
        )
        return
        
    if query_data == 'confirm':
        rmallowall_db(chat_id)
        await callback_query.edit_message_text(
            "Delete chat allowlist."
        )
    else:
        await callback_query.edit_message_text(
            "Removal of the allowlist has been cancelled."
        )
