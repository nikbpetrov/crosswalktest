**NB:** must have geopandas installed otherwise errors are likely to occur, see https://geopandas.org/getting_started/install.html

# Install

`pip install crosswalktest`

or

`conda install -c nikbpetrov crosswalktest`

[conda recommended as installing geopandas is easier in anaconda - see above link]

# Import

`from crosswalktest import *`

or

`import crosswalktest as cw`

[examples given with the latter, if the former is chosen, skip the 'cw.' prefix on the functions]

# Use

`cw.crosswalk(source_filepath, source_shape_id, target_filepath, target_shape_id, 
				tolerance_percent = 10, tolerance_units = None, 
				export = False, export_filename = None)`

-- **Input**: *explanation coming soon*

-- **Output**: 2 return values -> `intersect` (i.e. the intersection between the two files) and `diagnostics_obj` (an object containing diagnostics of the intersection)

`cw.print_diagnostics(diagnostics_obj)`

-- **Input**: the `diagnostics_obj` returned by the `crosswalk` function

-- **Ouput**: Readable diagnostics into your console

`cw.save_diagnostics_to_word(diagnostics_obj, output_type, filename = None)`

-- **Input**: the `diagnostics_obj` returned by the `crosswalk` function, `output_type` (either 'table' or 'text'), `filename` of the to-be-saved document

-- **Output**: word file with diagnostics information (in either table or text format as specified in the `output_type` argument)
