from checkers.check import Checker
from osgeo import gdal


class GDALChecker(Checker):

    def __init__(self, path):
        Checker.__init__(self, path)
        self.type = "GDAL {}".format(gdal.VersionInfo())

    def check(self):
        ds = gdal.Open(self.path)
        if ds == None or ds.GetProjection() == "" or ds.GetGeoTransform() == "":
            self.result = False
        else:
            self.result = True

        return self.to_json()





