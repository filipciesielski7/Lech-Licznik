buffers = [{"sector": 'A4', "stand": 1}, {"sector": 'B3', "stand": 1}, {"sector": 'A3', "stand": 1}, {"sector": 'A2', "stand": 1}, {
    "sector": 'A1', "stand": 1}, {"sector": 'J1', "stand": 4}, {"sector": 'I1', "stand": 4}, {"sector": 'L2', "stand": 4}]

guests = [{"sector": 'U2', "stand": 4}, {"sector": 'N1', "stand": 4}, {"sector": 'T2', "stand": 4}, {"sector": 'S2', "stand": 4}, {"sector": 'R2', "stand": 4}, {"sector": 'P2', "stand": 4}, {
    "sector": 'M1', "stand": 4}, {"sector": 'L1', "stand": 4}, {"sector": 'O2', "stand": 4}, {"sector": 'K1', "stand": 4}, {"sector": 'N2', "stand": 4}, {"sector": 'M2', "stand": 4}]

golds = [{"sector": 'E', "stand": 1}, {"sector": 'F', "stand": 1}, {
    "sector": 'G', "stand": 1}, {"sector": 'H', "stand": 1}]

skyboxes = [{"sector": '3', "stand": 1}, {"sector": '18', "stand": 1}, {"sector": '19', "stand": 1}, {"sector": '20', "stand": 1}, {"sector": '21', "stand": 1}, {"sector": '22', "stand": 1}, {"sector": '4', "stand": 2}, {"sector": '5', "stand": 2}, {"sector": '6', "stand": 2}, {"sector": '23', "stand": 2}, {"sector": '24', "stand": 2}, {"sector": '7', "stand": 3}, {
    "sector": '10', "stand": 3}, {"sector": '25', "stand": 3}, {"sector": '26', "stand": 3}, {"sector": '27', "stand": 3}, {"sector": '28', "stand": 3}, {"sector": '29', "stand": 3}, {"sector": 'B17', "stand": 3}, {"sector": 'SILVER', "stand": 3}, {"sector": '9', "stand": 4}, {"sector": '11', "stand": 4}, {"sector": '12', "stand": 4}, {"sector": '17', "stand": 4}]

third_level_kociol = [{"sector": 'A4', "stand": 2}, {"sector": 'B4', "stand": 2}, {"sector": 'C4', "stand": 2}, {"sector": 'D4', "stand": 2}, {"sector": 'E4', "stand": 2}, {"sector": 'F4', "stand": 2}, {"sector": 'G4', "stand": 2}, {"sector": 'H4', "stand": 2}, {"sector": 'I4', "stand": 2}, {
    "sector": 'J4', "stand": 2}, {"sector": 'K4', "stand": 2}, {"sector": 'L4', "stand": 2}, {"sector": 'M4', "stand": 2}, {"sector": 'N4', "stand": 2}, {"sector": 'O4', "stand": 2}, {"sector": 'P4', "stand": 2}, {"sector": 'R4', "stand": 2}, {"sector": 'S4', "stand": 2}]

third_level_anioly = [{"sector": 'N4', "stand": 1},
                      {"sector": 'M4', "stand": 1}, {"sector": 'L4', "stand": 1}, {"sector": 'K4', "stand": 1}, {"sector": 'J4', "stand": 1}, {"sector": 'I4', "stand": 1}, {"sector": 'H4', "stand": 1}, {"sector": 'G4', "stand": 1}, {"sector": 'F4', "stand": 1}, {"sector": 'E4', "stand": 1}, {"sector": 'D4', "stand": 1}, {"sector": 'C4', "stand": 1}, {"sector": 'B4', "stand": 1}]

not_in_sale = [{"sector": 'T3', "stand": 1}, {"sector": 'S3', "stand": 1}, {"sector": 'R3', "stand": 1}, {
    "sector": 'A3', "stand": 3}, {"sector": 'B3', "stand": 3}, {"sector": 'H3', "stand": 1}, {"sector": 'G3', "stand": 1}]


not_available_sectors = []
not_available_sectors.extend(buffers)
not_available_sectors.extend(guests)
not_available_sectors.extend(golds)
not_available_sectors.extend(skyboxes)
not_available_sectors.extend(third_level_kociol)
not_available_sectors.extend(third_level_anioly)
not_available_sectors.extend(not_in_sale)
