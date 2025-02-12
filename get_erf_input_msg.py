from erftools.preprocessing import WRFInputDeck

wrf = WRFInputDeck('namelist.input')
wrf.process_initial_conditions('wrfinput_d01',
                               landuse_table_path='/home/mgomez/NumericalModels/WRF/WRF_test_compile_fromConfig/WRF_versions/WRF/run/LANDUSE.TBL') #,
                              # write_hgt='terrain_height.txt',
                              # write_z0='roughness_height.txt')
wrf.write_inputfile('inputs')

