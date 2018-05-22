<<<<<<< HEAD
from instapy import *
import schedule
import time
# insta_username = input("username")
# insta_password = input("pass")
=======
import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy
>>>>>>> afdf91122afb01f9fed08958eed1d35457caba95

def do_like():
    try:
        insta_username = "ken_c_c_photography"
        insta_password ="lGyhz123"
        # set headless_browser=True if you want to run InstaPy on a server

<<<<<<< HEAD
            # set these if you're locating the library in the /usr/lib/pythonX.X/ directory
            # Settings.database_location = '/path/to/instapy.db'
        #Settings.browser_location = "/Library/Frameworks/Python.framework/Versions/2.7/chromedriver-Darwin"

        session = InstaPy(username=insta_username,
                          password=insta_password,
                          headless_browser=False,
                          use_firefox=True,

                          multi_logs=False)
        session.login()
=======
# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-1.21,
				  delimit_by_numbers=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
    session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza', 'girl'])
>>>>>>> afdf91122afb01f9fed08958eed1d35457caba95

        # settings
        session.set_upper_follower_count(limit=10000)
        session.set_do_comment(True, percentage=30)
        session.set_comments(["Good.","Great!!","Awesome!","Good work...","Nice..."])
        # #session.set_dont_include(['friend1', 'friend2', 'friend3'])
        session.set_dont_like(['sex'])
        session.set_do_follow(True,10)
        # # actions
        session.like_by_tags(['#portrait',"#like4like","photography","landscape"], amount=100, media='Photo')
        session.unfollow_users(8,True)

<<<<<<< HEAD
        #end the bot session
        session.end()
    except: 
        pass
schedule.clear()
schedule.every(15).minutes.do(do_like)

while True:
    schedule.run_pending()
    time.sleep(1)
=======
except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
>>>>>>> afdf91122afb01f9fed08958eed1d35457caba95
