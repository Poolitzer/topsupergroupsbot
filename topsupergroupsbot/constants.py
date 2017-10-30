# TopSupergroupsBot - A telegram bot for telegram public groups leaderboards
# Copyright (C) 2017  Dario <dariomsn@hotmail.it> (github.com/91DarioDev)
#
# TopSupergroupsBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TopSupergroupsBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TopSupergroupsBot.  If not, see <http://www.gnu.org/licenses/>.

from topsupergroupsbot import config

from telegram import Bot


CURRENT_CHOICE = "🔘"
EMOJI_STAR = "⭐️"
EMOJI_NSFW = "🔞"
EMOJI_NEW = "🆕"

BUTTON_START = "•"
BUTTON_END = "•"

FEEDBACK_INV_CHAR = "\ufeff"

GET_ME = Bot(config.BOT_TOKEN).getMe()