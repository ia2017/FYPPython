# files: direct solution
if 'DIRECT' in files:
    name = files['DIRECT']
    name = su2io.expand_zones(name, konfig)  # --- New addition
    name = su2io.expand_time(name, konfig)
    link.extend(name)

# files: adjoint solution
if ADJ_NAME in files:
    name = files[ADJ_NAME]
    name = su2io.expand_zones(name, konfig)  # --- New addition
    name = su2io.expand_time(name, konfig)
    link.extend(name)
else:
    konfig['RESTART_SOL'] = 'NO'