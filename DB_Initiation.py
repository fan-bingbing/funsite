import sqlite3
conn = sqlite3.connect('db.sqlite3')

FEPs = [('Centre_frequency', '459.075', 'MHz'),
       ('Span_frequency', '300', 'Hz'),
       ('RBW', '10', 'Hz'),
       ('VBW', '30', 'Hz'),
       ('RF_level', '50', 'NULL'),
       ('Attenuation', '35', 'NULL'),
       ('RefLev_offset', '30.3', 'NULL'),
       ('Trace_peak', 'DET POS', 'NULL'),
       ('Transducer1', 'HSA029914302', 'NULL'),
       ('Trans1_ON?', 'ON', 'NULL'),
       ('Transducer2', 'PE7388-30-30DB', 'NULL'),
       ('Trans2_ON?', 'OFF', 'NULL'),
       ('Transducer3', 'NHP-700', 'NULL'),
       ('Trans3_ON?', 'OFF', 'NULL'),
       ('Limit_line_1', 'ASNZS4365_CONSPUR_TX', 'NULL'),
       ('Limit_line_1_ON?', 'OFF', 'NULL'),
       ('Limit_line_2', 'ASNZS4295_CONSPUR_TX', 'NULL'),
       ('Limit_line_2_ON?', 'OFF', 'NULL'),
       ('Sweep_points', '10001', 'NULL'),
      ]

conn.execute("create table FEP(parameter text, content text, unit text)")


conn.executemany("insert into manual_fep(parameter, content, unit) values (?,?,?)", FEPs)



for row in conn.execute("select parameter, content, unit from manual_fep"):
    print(row)

conn.commit()

conn.close()

# https://www.pythoncentral.io/introduction-to-sqlite-in-python/
