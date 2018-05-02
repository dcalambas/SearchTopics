import logging
import sys
from Utils import u_root
import os
import configparser


class Logging:
    """
        :Date: 2016-11-22
        :Version: 0.1
        :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá
        :Copyright: To be defined
        :Organization: Centro de Excelencia y Apropiación de Big Data y Data Analytics - CAOBA

        This class has static methods provided as utils functionalities

    """

    @staticmethod
    def configure_log(log_file_name):
        """
        :Date: 2017-01-13
        :Version: 0.1
        :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá

        This method configure the log file to write an error occurred while running the component

        :param log_file_name: name for the log file
        :type log_file_name: str
        """
        try:
            file = u_root.ROOT_DIR + os.sep + 'u_configuration' + os.sep + 'utils.ini'
            config = configparser.ConfigParser()
            config.read(file)

            path = config.get('Logging', 'LogPath')

            logging.basicConfig(filename=path + log_file_name + '.log', level=logging.ERROR,
                                format='DATE: %(asctime)s \n%(message)s')
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.error(
                'ERROR: ' + exc_type.__name__ + ': ' + str(exc_obj) + '\nFILE: ' + exc_tb.tb_frame.f_code.co_filename +
                '\nMETHOD: ' + exc_tb.tb_frame.f_code.co_name +
                '\nLINE: ' + str(exc_tb.tb_lineno) +
                '\n------------------------------------------------------------------------')
            raise Exception("Utils - Error while configuring log file")

    @staticmethod
    def write_standard_error(error_data):
        """
        :Date: 2017-01-13
        :Version: 0.1
        :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá

        This method write in the log file an error occurred while running the component

        :param error_data: data representing the error
        :type error_data: list
        """
        try:
            exc_type, exc_obj, exc_tb = error_data
            logging.error(
                'ERROR: ' + exc_type.__name__ + ': ' + str(exc_obj) + '\nFILE: ' + exc_tb.tb_frame.f_code.co_filename +
                '\nMETHOD: ' + exc_tb.tb_frame.f_code.co_name +
                '\nLINE: ' + str(exc_tb.tb_lineno) +
                '\n------------------------------------------------------------------------')
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.error(
                'ERROR: ' + exc_type.__name__ + ': ' + str(exc_obj) + '\nFILE: ' + exc_tb.tb_frame.f_code.co_filename +
                '\nMETHOD: ' + exc_tb.tb_frame.f_code.co_name +
                '\nLINE: ' + str(exc_tb.tb_lineno) +
                '\n------------------------------------------------------------------------')

    @staticmethod
    def write_success_message(message):
        """
        :Date: 2017-01-13
        :Version: 0.1
        :Author: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana, Bogotá

        This method write in the log file a personalized success message received as a parameter

        :param message: str representing the success message
        :type message: str
        """
        try:
            logging.info('SUCCESS: ' + message +
                         '\n------------------------------------------------------------------------')
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.error(
                'ERROR: ' + exc_type.__name__ + ': ' + str(exc_obj) + '\nFILE: ' + exc_tb.tb_frame.f_code.co_filename +
                '\nMETHOD: ' + exc_tb.tb_frame.f_code.co_name +
                '\nLINE: ' + str(exc_tb.tb_lineno) +
                '\n------------------------------------------------------------------------')

    @staticmethod
    def write_specific_error(message):
        """
        :Date: 2017-03-12
        :Version: 0.2
        :Author: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana, Bogotá

        This method write in the log file a personalized error received as a parameter

        :param message: str representing the error message
        :type message: str
        """
        try:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.error('ERROR: ' + message +
                          '\nFILE: ' + exc_tb.tb_frame.f_code.co_filename +
                          '\nMETHOD: ' + exc_tb.tb_frame.f_code.co_name +
                          '\nLINE: ' + str(exc_tb.tb_lineno) +
                          '\n------------------------------------------------------------------------')
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.error(
                'ERROR: ' + exc_type.__name__ + ': ' + str(exc_obj) + '\nFILE: ' + exc_tb.tb_frame.f_code.co_filename +
                '\nMETHOD: ' + exc_tb.tb_frame.f_code.co_name +
                '\nLINE: ' + str(exc_tb.tb_lineno) +
                '\n------------------------------------------------------------------------')
