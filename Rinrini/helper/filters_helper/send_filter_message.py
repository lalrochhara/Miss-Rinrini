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


from pyrogram.types import InlineKeyboardMarkup, Message
from Rinrini import RinriniCli
from Rinrini.helper.button_gen import button_markdown_parser
from Rinrini.helper.note_helper.note_fillings import NoteFillings


async def SendFilterMessage(message: Message, filter_name: str, content: str, text: str, data_type: int):
    
    chat_id = message.chat.id
    message_id = message.message_id
    text, buttons = button_markdown_parser(text)
    
    text = NoteFillings(message, text)
    # Check if button button len is Zero then reply_markup=None
    reply_markup = None
    if len(buttons) > 0:
        reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None

    if data_type == 1:
        await RinriniCli.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )

    elif data_type == 2:
        await RinriniCli.send_sticker(
            chat_id=chat_id,
            sticker=content,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
        
    elif data_type ==3:
        await RinriniCli.send_animation(
            chat_id=chat_id,
            animation=content,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )

    elif data_type == 4:
        await RinriniCli.send_document(
            chat_id=chat_id,
            document=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )

    elif data_type == 5:
        await RinriniCli.send_photo(
            chat_id=chat_id,
            photo=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 6:
        await RinriniCli.send_audio(
            chat_id=chat_id,
            audio=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 7:
        await RinriniCli.send_voice(
            chat_id=chat_id,
            voice=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 8:
        await RinriniCli.send_video(
            chat_id=chat_id,
            video=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 9:
        await RinriniCli.send_video_note(
            chat_id=chat_id,
            video_note=content,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
