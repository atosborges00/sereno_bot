from os import path
from csv import writer


def export_log_file(download_log, folder_path):
    file_path = path.join(folder_path, 'downloads_log.csv')

    fields = ['Plant name', 'Status', 'Download number']

    with open(file_path, 'w') as export_file:
        file_writer = writer(export_file)

        file_writer.writerow(fields)
        file_writer.writerows(download_log)
