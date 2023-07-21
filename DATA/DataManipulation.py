import random

import DATA.MongoDb as mongo_db

hospital_type_code = ['a', 'b', 'c']
hospital_region_code = ['A', 'B', 'C', 'Z']
department = ['anesthesia', 'radiotherapy', 'gynecology']
ward_type = ['G','D','O']
ward_facility_code = ['F','A','R']
bed_grade = ['2.0','4.0','3.0']



#  Database value keys
db_keys = []
for value in mongo_db.collection_name.find({'case_id' : '1'}):
    dict_keys = value.keys()
    for key in dict_keys:
        db_keys.append(key)


# insert empty data
def insert_empty_data():
    counter = 1
    for value in mongo_db.collection_name.find():
        if value.get('case_id') == f"{counter}":
            if value[db_keys[2]] == "":
                mongo_db.collection_name.update_one({db_keys[2]: ""}, {"$set": {db_keys[2]: f"{random.randint(1,20)}"}})
            if value[db_keys[3]] == "":
                mongo_db.collection_name.update_one({db_keys[3]: ""}, {"$set": {db_keys[3]: f"{random.choice(hospital_type_code)}"}})
            if value[db_keys[4]] == "":
                mongo_db.collection_name.update_one({db_keys[4]: ""}, {"$set": {db_keys[4]: f"{random.randint(1,50)}"}})
            if value[db_keys[5]] == "":
                mongo_db.collection_name.update_one({db_keys[5]: ""}, {"$set": {db_keys[5]: f"{random.choice(hospital_region_code)}"}})
            if value[db_keys[6]] == "":
                mongo_db.collection_name.update_one({db_keys[6]: ""}, {"$set": {db_keys[6]: f"{random.randint(1,3)}"}})
            if value[db_keys[7]] == "":
                mongo_db.collection_name.update_one({db_keys[7]: ""}, {"$set": {db_keys[7]: f"{random.choice(department)}"}})
            if value[db_keys[8]] == "":
                mongo_db.collection_name.update_one({db_keys[8]: ""}, {"$set": {db_keys[8]: f"{random.choice(ward_type)}"}})
            if value[db_keys[9]] == "":
                mongo_db.collection_name.update_one({db_keys[9]: ""}, {"$set": {db_keys[9]: f"{random.choice(ward_facility_code)}"}})
            if value[db_keys[10]] == "":
                mongo_db.collection_name.update_one({db_keys[10]: ""}, {"$set": {db_keys[10]: f"{random.choice(bed_grade)}"}})
        counter = counter + 1


# random db value insert
def random_change_db_value():
    random_case_id = 1 #random.randint(1, 10001)
    new_db = []
    for i in mongo_db.collection_name.find():
        new_db.append(i)

    for value in new_db:
        if value.get('case_id') == f"{random_case_id}":
            if value[db_keys[2]] != "":
                value[db_keys[2]] = f"{random.randint(1, 20)}"

            if value[db_keys[3]] != "":
                value[db_keys[3]] = f"{random.choice(hospital_type_code)}"

            if value[db_keys[4]] != "":
                value[db_keys[4]] = f"{random.randint(1, 50)}"

            if value[db_keys[5]] != "":
                value[db_keys[5]] = f"{random.choice(hospital_region_code)}"

            if value[db_keys[6]] != "":
                value[db_keys[6]] = f"{random.randint(1,3)}"

            if value[db_keys[7]] != "":
                value[db_keys[7]] = f"{random.choice(department)}"

            if value[db_keys[8]] != "":
                value[db_keys[8]] = f"{random.choice(ward_type)}"

            if value[db_keys[9]] != "":
                value[db_keys[9]] = f"{random.choice(ward_facility_code)}"

            if value[db_keys[10]] != "":
                value[db_keys[10]] = f"{random.choice(bed_grade)}"
    return new_db





