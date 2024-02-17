# EqIoT_EarthquakeMonitoring
EqIoT, short for “Earthquake Internet of Things”, is a smart system designed to keep a close eye on earthquakes around Campi Flegrei, Italy.

It uses sensors to feel ground movements and quickly alert a potential control centre whenever it senses a quake with a magnitude higher than 4.00 on the Ritcher’s scale. In this way, people in charge can monitor the situation and, eventually, warn authorities and law enforcement to keep everyone safe.

More informations on the system design and architecture are contained in the [Documentation pdf](EqIoT_documentation.pdf)


## Set up

These are the steps to follow to get the system working right away

1. Clone this repo

        git clone https://github.com/itsrocchi/EqIoT_EarthquakeMonitoring.git

2. Go to the project directory

        cd EqIoT_EarthquakeMonitoring
   
3. Compose the project (be sure to have the docker engine up and running)

        docker-compose up

7. Once everything has started up, you should be able to access the various webapps via localhost URLS on your host machine.
   - [http://localhost:1880/](http://localhost:1880/) (Node-RED)
   - [http://localhost:8086/](http://localhost:8086/) (InfluxDB)
   - [http://localhost:3000/](http://localhost:3000/) (Grafana)
  
----

**Note**

Credentials to access InfluxDB and Grafana:
  
User: admin

Password: adminadmin
