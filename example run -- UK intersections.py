import crosswalktest as cw
import geopandas as gpd
import random

# -----------------------------------------------------------Postal Sectors to MSOA
source_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\UK_Postal_Sectors\\PostalSector.shp'
source_shape_id = 'RMSect'
target_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\UK_MSOA\\UK_2011_Census_Boundaries__MSOA.shp'
target_shape_id = 'AREA_ID'

# add made up population and personality columns
source_population_col_id = 'source_population'
source_col_id_to_weigh_by_population = 'source_personality'
source_shape = gpd.GeoDataFrame.from_file(source_filepath)
target_shape = gpd.GeoDataFrame.from_file(target_filepath)
source_shape[source_population_col_id] = random.sample(range(10000, 100000), len(source_shape))
source_shape[source_col_id_to_weigh_by_population] = [round(random.uniform(0, 5), 2) for _ in range(len(source_shape))]

# if tolerance_units are set, then those will be used, and  the corresponding percent will be calculated
# 3500 tolerance units set post-hoc after examining a solution where tolerance percent was set to 10
intersect, diagnostics_obj = cw.crosswalk(source_shape, source_shape_id, target_shape, target_shape_id, 
											source_population_col_id = source_population_col_id, source_col_id_to_weigh_by_population = source_col_id_to_weigh_by_population,
											tolerance_percent = None, tolerance_units = 3500,
											export = True, export_filename = 'Exports/20210623_Postal Sectors to MSOA_Intersection')


# cw.print_diagnostics(diagnostics_obj) -- optional; prints text diagnostics to console
cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'text', filename = 'Exports/20210623_Post Sectors to MSOA_Diagnostics text')
cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'table', filename = 'Exports/20210623_Post Sectors to MSOA_Diagnostics table')


# # -----------------------------------------------------------Postal Sectors to Westminster
# source_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\UK_Postal_Sectors\\PostalSector.shp'
# source_shape_id = 'RMSect'
# target_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\Westminster_Districts\\Westminster_Parliamentary_Constituencies_(December_2015)_Boundaries.shp'
# target_shape_id = 'pcon15cd'

# # if tolerance_units are set, then those will be used, and  the corresponding percent will be calculated
# # 3500 tolerance units set post-hoc after examining a solution where tolerance percent was set to 10
# intersect, diagnostics_obj = cw.crosswalk(source_filepath, source_shape_id, target_filepath, target_shape_id, 
# 																					tolerance_percent = None, tolerance_units = 3500,
# 																					export = True, export_filename = 'Exports/20210607_Postal Sectors to Westminster districts_Intersection')


# # cw.print_diagnostics(diagnostics_obj) -- optional; prints text diagnostics to console
# cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'text', filename = 'Exports/20210607_Post Sectors to Westminster distrincts_Diagnostics text')
# cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'table', filename = 'Exports/20210607_Post Sectors to Westminster distrincts_Diagnostics table')


# # -----------------------------------------------------------Postal Sectors to England & Wales Wards
# source_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\UK_Postal_Sectors\\PostalSector.shp'
# source_shape_id = 'RMSect'
# target_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\England_Wales_Wards\\Census_Merged_Wards_(December_2011)_Boundaries.shp'
# target_shape_id = 'cmwd11cd'

# # if tolerance_units are set, then those will be used, and  the corresponding percent will be calculated
# # 3500 tolerance units set post-hoc after examining a solution where tolerance percent was set to 10
# intersect, diagnostics_obj = cw.crosswalk(source_filepath, source_shape_id, target_filepath, target_shape_id, 
# 																					tolerance_percent = None, tolerance_units = 3500,
# 																					export = True, export_filename = 'Exports/20210607_Postal Sectors to England and Wales wards_Intersection')


# # cw.print_diagnostics(diagnostics_obj) -- optional; prints text diagnostics to console
# cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'text', filename = 'Exports/20210607_Post Sectors to England and Wales wards_Diagnostics text')
# cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'table', filename = 'Exports/20210607_Post Sectors to England and Wales wards_Diagnostics table')


# # -----------------------------------------------------------Postal Sectors to England & Wales Wards
# source_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\UK_Postal_Sectors\\PostalSector.shp'
# source_shape_id = 'RMSect'
# target_filepath = 'D:\\.Active projects\\crosswalktest\\Shapefiles\\Scotland_Wards\\All_Scotland_wards_4th.shp'
# target_shape_id = 'CODE'

# intersect, diagnostics_obj = cw.crosswalk(source_filepath, source_shape_id, target_filepath, target_shape_id, 
# 																					tolerance_percent = 10, tolerance_units = None,
# 																					export = True, export_filename = 'Exports/20210607_Postal Sectors to Scotland wards_Intersection')


# # cw.print_diagnostics(diagnostics_obj) -- optional; prints text diagnostics to console
# cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'text', filename = 'Exports/20210607_Post Sectors to Scotland wards_Diagnostics text')
# cw.save_diagnostics_to_word(diagnostics_obj, output_type = 'table', filename = 'Exports/20210607_Post Sectors to Scotland wards_Diagnostics table')
