from house_info import HouseInfo
from datetime import date


class ParticleData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("particulate", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("particulate", rec_date)
        return self._convert_data(recs)

    def get_data_concentrations(self, data):
        particulate = {"good": 0, "moderate": 0, "bad": 0}
        for rec in data:
            if rec <= 50:
                particulate["good"] += 1
            elif 50 < rec <= 100:
                particulate["moderate"] += 1
            elif rec > 100:
                particulate["bad"] += 1
            else:
                assert False, "This should never happen!"
        return particulate
