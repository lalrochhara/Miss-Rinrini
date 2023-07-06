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


__mod_name__ = "CAPTCHA"

__help__ = """
Some chats get a lot of users joining just to spam. This could be because they're trolls, or part of a spam network.
To slow them down, you could try enabling CAPTCHAs. New users joining your chat will be required to complete a test to confirm that they're real people.'

Admin commands:
- /captcha `<yes/no/on/off>`: All users that join will need to solve a CAPTCHA. This proves they aren't a bot!
- /captchamode `<button/math/text>`: Choose which CAPTCHA type to use for your chat.
- /captcharules `<yes/no/on/off>`: Require new users accept the rules before being able to speak in the chat.
- /captchatime `<Xw/d/h/m>`: Unmute new users after X time. If a user hasn't solved the CAPTCHA yet, they get automatically unmuted after this period.
- /captchakick `<yes/no/on/off>`: Kick users that haven't solved the CAPTCHA.
- /captchakicktime `<Xw/d/h/m>`: Set the time after which to kick CAPTCHA'd users.
- /setcaptchatext `<text>`: Customise the CAPTCHA button.
- /resetcaptchatext: Reset the CAPTCHA button to the default text.
- /recaptcha `<yes/no/on/off>`: Rinrini will ask the CAPTCHA to every new user, be it someone who has joined before and verified already

Examples:
- Enable CAPTCHAs
-> `/captcha on`
- Change the CAPTCHA mode to text.
-> `/captchamode text`
- Enable CAPTCHA rules, forcing users to read the rules before being allowed to speak.
-> `/captcharules on`

NOTE:
For CAPTCHAs to be enabled, you MUST have enabled welcome messages. If you disable welcome messages, CAPTCHAs will also stop.
"""