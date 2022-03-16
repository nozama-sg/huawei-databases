# huawei-databases

Repository for Flask server running on Huawei Elastic Cloud Server (ECS). Provides backend routes for Elderberry project and runs Food Detection AI, Sentiment Analysis, Anomaly Detection and the generation of monthly reports.

The monthly report system is hosted at http://119.13.104.214:80/customizeReport.

## Navigating this Repository
The file `app.py` contains the list of all routes. It redirects each set of relavent routes (i.e. bluetooth routes) to the corresponding file in `/routes`, for instance `/routes/bluetooth.py`. That file processes the query and uses `/hctools/bluetooth.py` (hctools referring to Huawei Cloud tools) to invoke GaussDB, OBS or otherwise.

The `/mockData` files help generate mock data for the back-end reports and the front-end app.

## Technical Stack

## Database Design
![This is an image](img/database-design.png)
