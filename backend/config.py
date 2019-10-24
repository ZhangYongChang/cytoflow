import os

DATA_SET_ROOT_DIR = 'datasets'
REPORT_TEMP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_TEMP_DIR = os.path.join(REPORT_TEMP_DIR, "tmp")

SSC_A = 'SSC-A'
PerCP_A = 'PerCP-A'


def get_data_set_dir():
    return DATA_SET_ROOT_DIR


def get_fcsfiledir(fcsfiledir):
    return os.path.join(DATA_SET_ROOT_DIR, fcsfiledir)


def get_fcsfilepath(fcsfiledir, fcsfilename):
    return os.path.join(DATA_SET_ROOT_DIR, fcsfiledir, fcsfilename)


def get_reporttmpdir():
    return REPORT_TEMP_DIR


def get_reportfilepath(reportfilepath):
    return os.path.join(REPORT_TEMP_DIR, reportfilepath)
