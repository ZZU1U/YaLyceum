import sqlite3


def kindness(*cities, symp_kind=0):
    con = sqlite3.connect("actions.db")

    cur = con.cursor()
    cities = [f'"{i}"' for i in cities]

    people = cur.execute(f"SELECT People.name, Acts.act FROM People INNER JOIN Acts ON \
    People.act_id == Acts.id WHERE People.city_id IN (SELECT Cities.id FROM Cities \
    WHERE Cities.city IN ({', '.join(cities)}) AND \
    Acts.kindness_level + Acts.symp_level >= {symp_kind})").fetchall()

    people.sort(key=lambda x: [len(x[1]), x[0]])

    con.close()

    return list([i[0] for i in people])
