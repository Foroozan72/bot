import logging
import asyncio
import httpx
import json

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def get_me(token, proxy_url=None):
    base_url = f'https://api.telegram.org/bot{token}/getMe'
    
    async with httpx.AsyncClient(proxies=proxy_url) as client:
        try:
            response = await client.get(base_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e.response.status_code} {e.response.text}")
        except httpx.RequestError as e:
            logger.error(f"Request error occurred: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")

async def test_proxy():
    proxy_url = 'http://cloudflare.com.nokia.co.uk.do_you.want_to.clash_without.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.msn.com.bsi.ir.enamad.ir.now_sudo.again_to_fight.everyone.i_am.ftp_internet.tcp-udp.co.uk:3443'
    token = '6804582307:AAFiTwiRpcm6fxubfTUWi3SsNJgIY-t2PT8'

    # Test with proxy
    logger.info("Testing with proxy...")
    me = await get_me(token, proxy_url)
    if me:
        print(json.dumps(me, indent=4))
    else:
        logger.error("Failed to connect using proxy.")

    # Test without proxy
    logger.info("Testing without proxy...")
    me = await get_me(token)
    if me:
        print(json.dumps(me, indent=4))
    else:
        logger.error("Failed to connect without proxy.")

if __name__ == '__main__':
    asyncio.run(test_proxy())
