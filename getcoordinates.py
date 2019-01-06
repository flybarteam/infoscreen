import gps

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
x = 0
while x < 1:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print(report)
        if report['class'] == 'TPV':
            if hasattr(report, 'lat'):
                latitude = report.lat
                print('Latitude ' + str(latitude))
                x = 1
        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                longitude = report.lon
                print('Longitude ' + str(longitude))
                x = 1
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")