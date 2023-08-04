import os

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
from helper import project_dir


class ProductionEnvironment(Exception):
    pass


def get_block_names():
    DEBUG = os.getenv("DEBUG", False)

    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = Options()

    if not DEBUG:
        options = [
            "--headless",
            "--window-size=1920,1200",
            "--ignore-certificate-errors"
        ]

        for option in options:
            chrome_options.add_argument(option)
    else:
        logger.debug("Running in detach mode")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("user-data-dir=/tmp/selenium")
        chrome_options.binary_location = '/usr/bin/chromium'

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def web_driver_wait(by: By, element: str, time: int = 10) -> WebElement:
        return WebDriverWait(driver, time).until(
            EC.presence_of_element_located((by, element))
        )

    # workflow
    # Check if logged-in, If not > log in
    # load the page
    # execute

    if DEBUG:
        driver.get('https://portal.battlefield.com/experience/rules?playgroundId=a56cf4d0-c713-11ec-b056-e3dbf89f52ce')

    # handle login
    try:
        if DEBUG:
            web_driver_wait(By.CLASS_NAME, 'blocklyWorkspace', 10)
        else:
            raise ProductionEnvironment
        logger.debug("Already Logged in 😃")
    except (TimeoutException, ProductionEnvironment):
        try:
            logger.debug('Not logged in....')
            # driver.get("https://accounts.ea.com")  # needed as selenium only sets cookies for a domain when on it
            # driver.add_cookie({'name': 'remid', 'value': os.getenv('REMID')})
            # driver.add_cookie({'name': 'sid', 'value': os.getenv('SID')})
            driver.get("https://portal.battlefield.com/login")
            web_driver_wait(By.ID, 'email')
            driver.find_element(By.ID, 'email').send_keys('bfportal.community@gmail.com')
            logger.debug('Email set')
            driver.find_element(By.ID, 'password').send_keys(os.getenv('EA_LOGIN_PASS'))
            logger.debug('Password set')
            driver.find_element(By.ID, 'logInBtn').click()
            logger.debug('Clicked Login')
            try:
                logger.debug('Waiting for login to complete')
                wait = WebDriverWait(driver, 10)
                wait.until(lambda d: d.current_url != "https://portal.battlefield.com/experiences")
                logger.debug(f"at {driver.current_url}")
                logger.debug('Waiting for playground to load')
                driver.get(
                    'https://portal.battlefield.com/experience/rules?playgroundId=a56cf4d0-c713-11ec-b056-e3dbf89f52ce')
                logger.debug(f"at {driver.current_url}")
                web_driver_wait(By.CLASS_NAME, 'blocklyWorkspace')
                logger.debug('Login Successful')
            except TimeoutException:
                logger.debug('Login failed...Info was set')
                raise
        except TimeoutException:
            logger.debug('Login failed...')
            driver.quit()
            sys.exit("Login failed... exiting")
        except ConnectionRefusedError:
            raise
    except ConnectionRefusedError:
        driver.quit()
        sys.exit("Unable to connect to portal.battlefield.com.. exiting")
    except Exception:
        raise

    time.sleep(5)
    blocks = {'blocks': ''}
    data = driver.execute_script("return _Blockly.Blocks")
    logger.debug(f"got {len(data)} blocks")
    with open(project_dir / "data" / "enabled_blocks.json", 'w') as json_file:
        bad_blocks = ['Compare', 'IndexOfFirstTrue', 'actionComment', 'missingActionBlockType_v1',
                      'missingValueBlockType_v1']
        blocks['blocks'] = [block for block in data.keys() if block not in bad_blocks]
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


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    get_block_names()
