# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from django.conf import settings
from django.utils.translation import ugettext as _
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

LOGIN, SUCCESS = range(2)


def start(bot, update):
    contact_button = KeyboardButton(text=_('Share my contact information'), request_contact=True)
    reply_keyboard = [[contact_button]]

    update.message.reply_text(_(
        "Hi! I'm alibot, your assistant in filing reports. "
        "first of all you have to give my you mobile number for verification."),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

    return LOGIN


def login(bot, update):
    user = update.message.from_user
    logger.info("Gender of %s: %s" % (user.first_name, update.message.text))
    update.message.reply_text('I see! Please send me a photo of yourself, '
                              'so I know what you look like, or send /skip if you don\'t want to.',
                              reply_markup=ReplyKeyboardRemove())

    return SUCCESS


def success(bot, update):
    user = update.message.from_user
    logger.info(
        "User \"%s %s\" successfully shared his/her contact info" % (
            user.first_name, user.last_name
        )
    )

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


# Create the EventHandler and pass it your bot's token.
updater = Updater(settings.TELEGRAM_TOKEN)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        LOGIN: [MessageHandler(Filters.contact, login)],
        # GENDER: [RegexHandler('^(Boy|Girl|Other)$', gender)],
        #
        # PHOTO: [MessageHandler(Filters.photo, photo),
        #         CommandHandler('skip', skip_photo)],
        #
        # LOCATION: [MessageHandler(Filters.location, location),
        #            CommandHandler('skip', skip_location)],
        #
        SUCCESS: [MessageHandler(Filters.text, success)]
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)

dp.add_handler(conv_handler)

# log all errors
dp.add_error_handler(error)
