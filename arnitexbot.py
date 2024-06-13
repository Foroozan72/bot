import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function to send a signal
def send_signal(update: Update, context: CallbackContext) -> None:
    """Send a cryptocurrency signal"""
    signal_message = "سیگنال خرید: بیت‌کوین \nقیمت ورود: 45000$ \nقیمت هدف: 50000$ \nقیمت توقف ضرر: 44000$"
    update.message.reply_text(signal_message)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('سلام! من ربات سیگنال ارز هستم. از دستور /signal برای دریافت سیگنال استفاده کنید.')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('از دستور /signal برای دریافت سیگنال ارز دیجیتال استفاده کنید.')

async def main() -> None:
    """Start the bot."""
    # Proxy setup (optional)
    proxy_url = "http://cloudflare.com.nokia.co.uk.do_you.want_to.clash_without.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.msn.com.bsi.ir.enamad.ir.now_sudo.again_to_fight.everyone.i_am.ftp_internet.tcp-udp.co.uk:3443"
    application = (
        Application.builder()
        .token("6804582307:AAFiTwiRpcm6fxubfTUWi3SsNJgIY-t2PT8")
        .proxy_url(proxy_url)
        .build()
    )

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("signal", send_signal))

    # Start the Bot
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == '__main__':
    asyncio.run(main())
