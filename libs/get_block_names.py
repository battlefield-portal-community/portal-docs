from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from loguru import logger
import time
import json
import sys
import pathlib

from utils.helper import project_dir

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())


chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]

for option in options:
    chrome_options.add_argument(option)

chrome_options.add_argument("user-data-dir=/tmp/selenium")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


def web_driver_wait(by: By, element: str, time: int = 10) -> WebElement:
    return WebDriverWait(driver, time).until(
        EC.presence_of_element_located((by, element))
    )

# workflow
# Check if logged-in, If not > log in
# load the page
# execute


driver.get('https://portal.battlefield.com/experience/rules?playgroundId=a56cf4d0-c713-11ec-b056-e3dbf89f52ce')

# handle login
try:
    web_driver_wait(By.CLASS_NAME, 'blocklyWorkspace', 10)
    logger.debug("Already Logged in 😃")
except TimeoutException:
    try:
        logger.debug('Not logged in....')
        web_driver_wait(By.CLASS_NAME, 'login-button').click()
        web_driver_wait(By.ID, 'email').send_keys('bfportal.community@gmail.com')
        web_driver_wait(By.ID, 'password').send_keys('ix*ZaV95%yq55UL!')
        logger.debug('login info set....')
        web_driver_wait(By.ID, 'logInBtn').click()
        logger.debug("Trying to log in ....")
        try:
            web_driver_wait(By.CLASS_NAME, 'blocklyWorkspace')
            logger.debug('Login Successful')
        except TimeoutException:
            logger.debug('Login failed...Info was set')
            raise
    except TimeoutException:
        logger.debug('Login failed...')
        driver.quit()
    except ConnectionRefusedError:
        raise
except ConnectionRefusedError:
    driver.quit()
    sys.exit("Unable to connect to portal.battlefield.com.. exiting")

time.sleep(5)
blocks = {'blocks': ''}
data = driver.execute_script("return _Blockly.Blocks")
logger.debug(f"got {len(data)} blocks")
with open(project_dir / "data" / "enabled_blocks.json", 'w') as json_file:
    blocks['blocks'] = list(data.keys())
    json.dump(blocks, json_file)
logger.debug("Saved info.. exiting")
