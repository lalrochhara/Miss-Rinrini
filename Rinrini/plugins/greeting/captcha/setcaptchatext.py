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
from Rinrini.database.welcome_mongo import GetCaptchaSettings, SetCaptchaText
from Rinrini.helper import custom_filter
from Rinrini.helper.anon_admin import anonadmin_checker
from Rinrini.helper.chat_status import isBotAdmin, isUserCan
from Rinrini.plugins.connection.connection import connection


@RinriniCli.on_message(custom_filter.command(commands=('setcaptchatext')))
@anonadmin_checker
async def SetCaptchatext(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return

    if not await  isBotAdmin(message, silent=True):
        await message.reply(
            "I need to be admin with the right to restrict to enable CAPTCHAs.",
            quote=True
        )
        return 
    
    CaptchaText = ' '.join(message.text.split()[1:])
    if CaptchaText:
        SetCaptchaText(chat_id, CaptchaText)
        await message.reply(
            "Updated the CAPTCHA button text!",
            quote=True
        )
    else:
        captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)
        
        await message.reply(
            (
                "Users will be welcomed with a button containing the following:\n"
                f"`{captcha_text}`\n\n"
                "To change the text, try this command again followed by your new text"
            ),
            quote=True
        )
