import allure
# import requests
from allure_commons.types import AttachmentType

# from tests.conftest import USER_NAME, ACCESS_KEY


def add_video(browser):
    video_url = (
       f"https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/"
       f"{browser.driver.session_id}/video-" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        body=html,
        name='video_' + browser.driver.session_id,
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )


# def video_from_browserstack(session_id, *, name='video recording'):
#     video_url = video_url(session_id=session_id)
#
#     allure.attach(
#         '<html><body>'
#         '<video width="100%" height="100%" controls autoplay>'
#         f'<source src="{video_url}" type="video/mp4">'
#         '</video>'
#         '</body></html>',
#         name=name,
#         attachment_type=allure.attachment_type.HTML,
#     )
#
# def video_url(*, session_id):
#     session_details = requests.get(f'https://api.browserstack.com/app-automate/session/{session_id}.json',
#                                    auth=(USER_NAME, ACCESS_KEY),).json()
#     return session_details['automation_session']['video_url']