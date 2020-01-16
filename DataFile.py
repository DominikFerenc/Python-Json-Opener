import json
import urllib.request
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

class Synop:
    def downloadSynopData(self):
        pathSynopFile = "https://danepubliczne.imgw.pl/api/data/synop"
        try:
            with urllib.request.urlopen(pathSynopFile) as SynopUrl:
                json_synop_data = SynopUrl.read()
                parse_synop_json_data = json.loads(json_synop_data)
                #self.showData(parse_synop_json_data)
                self.showAllSynopData(parse_synop_json_data)
        except ConnectionError:
            print("Failed to open url")

    def showData(self, parse_json_data):
        print("\nPrezentacja pojedyńczych danych")
        print("Stacja Pomiarowa: " + parse_json_data[15]['stacja'] + "\n")

    def showAllSynopData(self, parse_json_data):
        print("Dane z pliku Synop:")
        print(parse_json_data[20])

    def dataScheduler(self):
        self.downloadSynopData()
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.downloadSynopData, 'interval', hours=1)
        scheduler.start()


class Hydro:
    def downloadHydroData(self):
        pathHydroFile = "http://danepubliczne.imgw.pl/api/data/hydro"
        try:
            with urllib.request.urlopen(pathHydroFile) as urlHydro:
                json_hydro_data = urlHydro.read()
                parse_hydro_json_data = json.loads(json_hydro_data)
                self.ShowAllHydroData(parse_hydro_json_data)
        except ConnectionError:
            print("Failed to open url")

    def ShowAllHydroData(self, parse_hydro_json_data):
        print("Dane z pliku Hydro:")
        print(parse_hydro_json_data[272]) #225 TSZ

    def dataHydroScheduler(self):
        self.downloadHydroData()
        scheduler = BlockingScheduler()
        scheduler.add_job(self.downloadHydroData, 'interval', hours=1)
        scheduler.start()



def main():
    print("\nDane meteo IMGW:\n")

    synop = Synop()
    synop.dataScheduler()

    hydro = Hydro()
    hydro.dataHydroScheduler()

if __name__ == '__main__':
    main()


