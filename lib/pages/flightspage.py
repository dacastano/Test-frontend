import logging

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import validate_wait_results
from lib.pages.basepage import BasePage
from lib.pages.webelements.flightswebelements import FlightsWebElements

logger = logging.getLogger(__name__)


class FlightsPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context)
        self.context = context
        self.web_driver = context.browser
        self.webElements = FlightsWebElements

    def is_open(self):
        return validate_wait_results(
            GeneralComponents.wait_until_element_is_present(self.context, FlightsWebElements.from_text_input))