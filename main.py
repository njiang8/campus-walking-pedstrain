# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import mesa
import mesa_geo as mg
from src.model.model import CampusWalkModel
from src.visualization.server import (
    agent_draw,
    clock_element,
    status_chart,
)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("main->running...")
    model_params = {
        "population_file": 'data/population/test_pop.csv',
        #"population_file" : 'data/population/ub_pop_with_path.csv',
        "data_crs": 'epsg:4326',
        "buildings_file": f"data/shp_zip/single_bldings.zip",
        #"buildings_file": f"data/shp/UB_bld.zip",
        "walkway_file":   f"data/shp_zip/ub_walkway_clean.zip",
        "lakes_file":     f"data/shp_zip/hydrop.zip",
        "rivers_file":    f"data/shp_zip/hydrol.zip",
        "driveway_file":  f"data/shp_zip/UB_Rds.zip",
        "show_walkway": False,
        "show_driveway": True,
        "show_lakes_and_rivers": False,
        "commuter_speed": mesa.visualization.Slider(
            "Commuter Walking Speed (m/s)",
            value=0.5,
            min_value=0.1,
            max_value=1.5,
            step=0.1,
        ),
    }
    map_element = mg.visualization.MapModule(agent_draw, map_height=600, map_width=600)

    server = mesa.visualization.ModularServer(
        CampusWalkModel,
        #[clock_element, status_chart],
        [map_element, clock_element, status_chart],
        "Campus Walking",
        model_params,
    )
    server.launch()

