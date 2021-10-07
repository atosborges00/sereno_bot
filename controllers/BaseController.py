from config.ConfigSices import ConfigSices
from os import path
from csv import writer


def export_log_file(download_log):
    file_path = path.join(ConfigSices.PREFERENCES['download.default_directory'], 'downloads_log.csv')

    fields = ['Plant name', 'Status']

    with open(file_path, 'w') as export_file:
        file_writer = writer(export_file)

        file_writer.writerow(fields)
        file_writer.writerows(download_log)
