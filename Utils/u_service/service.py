from six import string_types
import sys
import configparser
import os
from Utils.u_logging.logging import Logging
import Utils.u_root


class Service:
    """
    :Date: 2016-11-28
    :Version: 0.1
    :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana Bogotá
    :Copyright: To be defined
    :Organization: Centro de Excelencia y Apropiación de Big Data y Data Analytics - CAOBA

    This class provides utils web service functionalities
    """

    def __init__(self):
        """
        :Date: 2017-02-16
        :Version: 0.2
        :Modified by: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana Bogotá
        :Author: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana Bogotá

        Constructor for the class
        
        :return: Service object
        :rtype: object
        """
        try:
            file = Utils.u_root.ROOT_DIR + os.sep + 'u_configuration' + os.sep + 'utils.ini'
            self.config = configparser.ConfigParser()
            self.config.read(file)
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while creating Service object - Check configuration file path")

    def get_web_service_url(self, service, function, dictionary=dict()):
        """
        :Date: 2016-11-27
        :Version: 0.1
        :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana Bogotá.

        This function generates the URL required to call a function provided by a rest web u_service.

        :param service: The name of the u_service.
        :type service: str
        :param function: The name of the u_service method.
        :type function: str
        :param dictionary: A dictionary containing parameters as name (key) and value (value).
        :type dictionary: dict
        :return: url: The URL generated to call a method from a desired rest web u_service.
        :rtype: str
        """
        try:
            ip = self.config.get('Services', service)
            url = None
            if ip is not None:
                url = 'http://' + ip + '/' + function
                if len(dictionary) > 0:
                    url += '?'
                    for key, value in dictionary.items():
                        if '=' in url:
                            url += '&'
                        if isinstance(value, string_types):
                            value = value.replace(" ", "%20")
                        else:
                            value = str(value)
                        url = url + key + '=' + value
            return url
        except configparser.NoSectionError or configparser.NoOptionError:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while getting data from Service configuration file")
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while getting web service url")
