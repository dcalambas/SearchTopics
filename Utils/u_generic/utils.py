from datetime import datetime, timedelta
import sys
import re
from Utils.u_logging.logging import Logging
import csv
import calendar


class Utils:
    """
    :Date: 2016-11-22
    :Version: 0.1
    :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá
    :Copyright: To be defined
    :Organization: Centro de Excelencia y Apropiación de Big Data y Data Analytics - CAOBA

    This class has static methods provided as utils functionalities

    """

    @staticmethod
    def convert_tweet_string_to_date(created_at):
        """
        :Date: 2017-02-19
        :Version: 0.3
        :Modified by: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá
        :Author: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana, Bogotá

        This method converts the string value of parameter created_at to datetime

        :param created_at: String representation of date in UTC format
        :type created_at: str
        :return: datetime representation of the string created_at
        :rtype: datetime
        """
        try:
            split_date = created_at.split(" ")
            split_date.pop(4)
            aux_string = "{0} {1} {2} {3} {4}".format(split_date[0], split_date[1], split_date[2], split_date[3],
                                                      split_date[4])
            date_format = "%a %b %d %H:%M:%S %Y"
            date_hour = datetime.strptime(aux_string, date_format)

            # Subtract five hours for transform to colombian time zone
            created_at = date_hour + timedelta(hours=-5)
            return created_at
        except:
            print(created_at)
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while converting Twitter string to date")

    @staticmethod
    def convert_python_string_to_date(date):
        """
        :Date: 2017-01-25
        :Version: 0.2
        :Modified by: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana, Bogotá
        :Author: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá

        This method converts a string value of a python datetime to native datetime

        :param date: String representation of python datetime
        :type date: str
        :return: datetime representation of the string date
        :rtype: datetime
        """
        try:
            split_date = re.split('[ |\-|:|.]', date)
            date_hour = datetime(int(split_date[0]),
                                 int(split_date[1]),
                                 int(split_date[2]),
                                 int(split_date[3]),
                                 int(split_date[4]),
                                 int(split_date[5]))
            return date_hour
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while converting python string to date")

    @staticmethod
    def replace_item_in_list(target_list, item_to_replace, replacement_value):
        """
        :Date: 2017-03-07
        :Version: 0.2
        :Modified by: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana
        :Author: Juan Camilo Campos - Pontificia Universidad Javeriana Cali

        This method replaces every occurrence of the item_to_replace by the replacement value

        :param: target_list: list of values
        :type target_list: list
        :param: item_to_replace: value to replace
        :type item_to_replace: object
        :param: replacement_value: replacement value
        :type replacement_value: object
        :rtype: list
        :return: returns the new list
        """
        try:
            for n, i in enumerate(target_list):
                if i == item_to_replace:
                    target_list[n] = replacement_value

            return target_list
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while replacing item in list")

    @staticmethod
    def get_dictionary_from_file(file, encoding, sep=';'):
        """
        :Date: 2017-02-23
        :Version: 0.3
        :Modified by: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá
        :Author: Johan Felipe Mendoza - Pontificia Universidad Javeriana, Bogotá

        Converts a file without header with unbounded columns into a dictionary
        using the first column as the key, and the second as the value.
        This creates a dictionary with a value with a variable length

        :param file: this is the name of the csv we want to convert into a dictionary
        :type file: str
        :param encoding: string that contains the encoding needed for the file
        :type encoding: str
        :param sep: string that contains the delimiter of the file
        :type sep: str
        :return: dictionary with the first column as a key, and the second and third value in a list
        :rtype: dict
        """
        try:
            file_data = open(file, encoding=encoding)
            list = csv.reader(file_data, delimiter=sep)
            dictionary = {}
            for i in list:
                if '' in i: i.remove('')
                length = len(i)
                meanings = []
                for x in range(1, length):
                    meanings.append(i[x])
                dictionary[i[0]] = meanings
            return dictionary
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while getting dictionary from file")

    
    @staticmethod
    def get_list_from_file(file, encoding, sep=';', set_lower=False):
        """
        :Date: 2017-03-04
        :Version: 0.4
        :Modified by: Andrea Patricia Ortiz Pulido - Pontificia Universidad Javeriana, Bogotá
        :Modified by: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana, Bogotá
        :Author: Joan Felipe Mendoza Molina - Pontificia Universidad Javeriana, Bogotá

        This method converts a txt file without header into a list.

        :param file: name of the txt file
        :type file: str
        :param encoding: string that contains the encoding needed for the file
        :type encoding: str
        :param sep: string that contains the delimiter of the file
        :type sep: str
        :param set_lower: indicates if is necessary to transform data into lower case
        :type set_lower: bool
        :return: tokens included in the txt file
        :rtype: list
        """
        try:
            file_data = open(file, encoding=encoding)
            list = csv.reader(file_data, delimiter=sep)
            final_list = []
            for i in list:
                length = len(i)
                if length == 1:
                    if set_lower is True:
                        final_list.append((i[0]).lower())
                    else:
                        final_list.append(i[0])
                elif length > 1:
                    interm_list = []
                    for x in range(length):
                        if set_lower is True:
                            interm_list.append((i[x]).lower())
                        else:
                            interm_list.append(i[x])
                    final_list.append(interm_list)
            return final_list
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while getting list from file")

    @staticmethod
    def get_query_dates_per_year_and_month(year, month):
        """
        :Date: 2017-05-22
        :Version: 0.3
        :Author: Katherine Espíndola Buitrago - Pontificia Universidad Javeriana

        This function returns the start and finish date for querying data using the DataAccessObject component. It also
        returns a generation date if the component is generating data.

        :param year: integer representation of the requested year
        :type year: int
        :param month: integer representation of the requested month. It must be between 1 and 12
        :type month: int
        :rtype: list
        :return: list with the start date, finish date and generation date, in that orde
        """
        try:
            days = calendar.monthrange(year, month)[1]
            generation_date = datetime(year, month, days, 23, 59, 59)
            start_date = datetime(year, month, 1, 0, 0, 0)
            if month == 1:
                finish_date = datetime(year, 2, 1, 0, 0, 0)
            elif month == 12:
                finish_date = datetime(year + 1, 1, 1, 0, 0, 0)
            else:
                finish_date = datetime(year, month + 1, 1, 0, 0, 0)
            return start_date, finish_date, generation_date
        except:
            Logging.write_standard_error(sys.exc_info())
            raise Exception("Utils - Error while getting query dates per month and year")
