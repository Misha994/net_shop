from datetime import datetime
from decimal import Decimal
import logging

logging.basicConfig(filename='requests.log', level=logging.INFO, format="")


class MyMiddleware(object):
    def process_request(self, request):
        self.start_time_request = Decimal(datetime.now().strftime("%S.%f"))
        self.time_request = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.method = request.method
        self.full_path = request.get_full_path()
        self.parameters = request.GET

    def process_response(self, request, response):
        self.response_time = ("%.4f" % (Decimal(datetime.now().strftime("%S.%f")) - self.start_time_request))
        logging.info(u"time request {}, method {}, full path {}, parameters {}, response time {}".format(
                                                                                                self.time_request,
                                                                                                self.method,
                                                                                                self.full_path,
                                                                                                self.parameters,
                                                                                                self.response_time))
        return response
