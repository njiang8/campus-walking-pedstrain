# campus-walking-pedstrain

## Project Overview
This simulation models campus commuters traveling between classrooms and dormitory locations on a predefined road/walkway network. The model advances in 5-minute time increments, updates commuter statuses dynamically, and collects time-series data on the number of commuters in each state (home/work/transport). It supports two primary run modes:

* Interactive Web Server: Real-time geographic visualization of commuters, buildings, and campus infrastructure with adjustable parameters.
* Headless Batch Mode: Non-interactive simulation that generates animated GIFs of movement and quantitative plots of commuter behavior.

 
├── data/                      # Geographic and population input data
│   ├── population/            # Commuter CSV files (home/work/path coordinates)
│   ├── shp/                   # Uncompressed shapefiles (raw geographic data)
│   └── shp_zip/               # Compressed shapefiles (optimized for loading)
├── outputs/                   # Auto-generated simulation outputs (GIFs, plots)
├── src/                       # Core source code (modular agent/model/visualization)
│   ├── agent/                 # GeoAgent definitions for all simulation entities
│   │   ├── building.py        # Building agent (home/work/neutral function)
│   │   ├── commuter.py        # Core commuter agent (movement/status logic)
│   │   └── geo_agents.py      # Infrastructure agents (walkway/driveway/water)
│   ├── model/                 # Main simulation model logic
│   │   └── model.py           # CampusWalkModel (data loading, clock, scheduling)
│   ├── space/                 # Spatial utilities and campus network logic
│   │   ├── campus.py          # Campus geographic space definition
│   │   ├── road_network.py    # Walkway/road network processing
│   │   └── utils.py           # CRS/geometry transformation utilities
│   └── visualization/         # Visualization and server code
│       ├── server.py          # Interactive web server (map, clock, charts)
│       └── utils.py           # Plot/animation generation for headless mode
├── run_ub_with_server.py      # Launch simulation with interactive web UI
├── run_ub_without_server.py   # Launch headless simulation (GIF/plot output)
├── requirements.txt           # Full project dependency list
└── README.md                  # Project documentation (this file)
