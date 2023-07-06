import html

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Rinrini import RinriniCli
from Rinrini.database.blocklists_mongo import get_blocklist, unblocklistall_db
from Rinrini.helper import custom_filter
from Rinrini.helper.chat_status import isUserCreator
from Rinrini.helper.get_data import get_text_reason


@RinriniCli.on_message(custom_filter.command(commands=['unblocklistall', 'unblacklistall']))
async def removeblocklistall(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title 
    if not await isUserCreator(message):
        return
    
    BLOCKLIST_DATA = get_blocklist(chat_id)
    if (
        BLOCKLIST_DATA is None
        or len(BLOCKLIST_DATA) == 0
    ):
        await message.reply(
            f"No blocklist filters active in {html.escape(chat_title)}!"
        )
        return

    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Delete blocklist', callback_data='blocklist_confirm')],
        [InlineKeyboardButton(text='Cancel', callback_data='blocklist_cancel')]]
    )

    await message.reply(
        text=f"Are you sure you would like to stop **ALL** of the blocklist in {html.escape(chat_title)}? This action cannot be undone.",
        reply_markup=button,
        quote=True
    )

@RinriniCli.on_callback_query(filters.create(lambda _, __, query: 'blocklist_' in query.data))
async def removeblocklistall_callback(client: RinriniCli, callback_query: CallbackQuery):
     
    chat_id = callback_query.message.chat.id 
    
    query_data = callback_query.data.split('_')[1]  
    if not await isUserCreator(callback_query, chat_id=callback_query.message.chat.id, user_id=callback_query.from_user.id):
        await callback_query.answer(
            text='You\'re not owner of this chat.'
        )
        return

    if query_data == 'confirm':
        unblocklistall_db(chat_id)
        await callback_query.edit_message_text(
            text="Deleted chat blocklist."
        )
    elif query_data == 'cancel':
        await callback_query.edit_message_text(
            text='Removal of the blocklist has been cancelled.'
        )



    

    
        