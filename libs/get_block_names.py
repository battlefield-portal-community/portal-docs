import os

import requests
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
from dotenv import load_dotenv
from helper import project_dir
load_dotenv()

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


# chrome_options.add_argument("--detach")

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
        email = os.getenv('BFPORTAL_EMAIL', None)
        password = os.getenv('BFPORTAL_PASSWORD', None)
        if email is None or password is None:
            sys.exit("email and password to login not found")
        web_driver_wait(By.ID, 'email').send_keys(email)
        web_driver_wait(By.ID, 'password').send_keys(password)
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

logger.debug("Saving Version info")

ver_file = project_dir / "data" / "rules_editor_version"
ver_backup_file = project_dir / "data" / "rules_editor_version_history"
ver_file.touch(exist_ok=True)

with ver_file.open() as file:
    data = file.read().strip().split('\n')[-1]
    if len(data):
        curr_ver = int(data)
    else:
        curr_ver = 0

new_ver = 0
for elm in driver.find_elements(By.TAG_NAME, 'script'):
    src = elm.get_attribute('src')
    if "main" in src:
        new_ver = int(src.split("/")[-2])
        break

if new_ver > curr_ver:
    with ver_backup_file.open('a') as file:
        file.write(f'{curr_ver}\n')
    with ver_file.open('w') as file:
        file.write(f'{new_ver}')

logger.debug("filter and save i18n json")
with open(project_dir / "data" / "i18n.json", 'w') as file:
    json.dump(requests.get(f"https://portal.battlefield.com/{new_ver}/assets/i18n/en-US.json").json(), file)

logger.debug("All tasks complete ")
