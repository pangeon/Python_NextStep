from trip_class import Trip
import datetime as dt

if __name__ == "__main__":
    trips = [
            Trip(
                'IT-VNC', 
                'Italy-Venice', 
                dt.date(2023, 6, 1), 
                dt.date(2023, 6, 12)
            ),
            Trip(
                'SP-BRC', 
                'Spain-Barcelona', 
                dt.date(2023, 6, 12), 
                dt.date(2023, 5, 22)
            ),
            Trip(
                'IT-ROM', 
                'Italy-Rome', 
                dt.date(2023, 6, 21), 
                dt.date(2023, 6, 12)
            )
        ]
    try:
        print('Publishing trips...')
        Trip.publish_offer(trips)
        print('... done')
    except Exception as e:
        print('THERE ARE ERRORS')
        print(e)
        print('THE OFFER CANNOT BE PUBLISHED')

