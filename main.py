import DATA.MongoDb as mongo_db
import DATA.DataManipulation as db_operations


#insert Empty data
db_operations.insert_empty_data()

# random change db value
new_db = db_operations.random_change_db_value()

# delete all db value
mongo_db.delete_all_db_value()

# update db
mongo_db.insert_db(new_db)























