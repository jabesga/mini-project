import datetime
import MySQLdb

# AUTHOR: JON ANDER BESGA

def insert_into_core_log(card_id):
    db = MySQLdb.connect(user='root', passwd='root', host='localhost', db='RCWI')
    cursor = db.cursor()

    query = "INSERT INTO core_log (time_detected, card_detected_id) VALUES (\'%s\',  %s)" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), card_id)
    cursor.execute(query)
    db.commit()

    cursor.close()
    db.close()

    print "New log created succesfully"

def insert_into_core_card(sn0, sn1, sn2, sn3, cb):

    db = MySQLdb.connect(user='root', passwd='root', host='localhost', db='RCWI')
    cursor = db.cursor()

    query = "INSERT INTO core_card (serial_number0, serial_number1, serial_number2, serial_number3, check_byte) VALUES (%s, %s, %s, %s, %s);" % (sn0, sn1, sn2, sn3, cb)
    cursor.execute(query)
    db.commit()

    cursor.close()
    db.close()

    print "Card inserted succesfully"

def insert_into_core_owner(first_name, last_name, card_owned, access_granted):

    db = MySQLdb.connect(user='root', passwd='root', host='localhost', db='RCWI')
    cursor = db.cursor()

    card_id = is_on_db_by_id(card_owned)

    query = "INSERT INTO core_owner (first_name, last_name, card_owned_id, access_granted) VALUES (\'%s\', \'%s\', %s, %s);" % (first_name, last_name, card_id, access_granted)
    cursor.execute(query)
    db.commit()

    cursor.close()
    db.close()

    print "Owner inserted succesfully"

def is_on_db_by_id(card_id):
    db = MySQLdb.connect(user='root', passwd='root', host='localhost', db='RCWI')
    cursor = db.cursor()

    query = "SELECT id FROM core_card WHERE id=%s;" % (card_id)
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    db.close()

    if str(data) == '()':
        return False
    else:
        return str(data[0][0])


def is_on_db(sn0, sn1, sn2, sn3, cb): # Return the ID of the card in the core_card table or False if is not on DB

    db = MySQLdb.connect(user='root', passwd='root', host='localhost', db='RCWI')
    cursor = db.cursor()

    query = "SELECT id FROM core_card WHERE serial_number0=%s AND serial_number1=%s AND serial_number2=%s AND serial_number3=%s AND check_byte=%s;" % (sn0, sn1, sn2, sn3, cb)
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    db.close()

    if str(data) == '()':
        return False
    else:
        return str(data[0][0])

def has_granted_access(card_id):

    db = MySQLdb.connect(user='root', passwd='root', host='localhost', db='RCWI')
    cursor = db.cursor()

    query = "SELECT access_granted FROM core_owner WHERE card_owned_id = %s;" % card_id
    cursor.execute(query)
    data = cursor.fetchall()

    if str(data) == '()':
        return False
    else:
        if str(data[0][0]) == '0':
            return False
        else:
            return True

    cursor.close()
    db.close()

def check(sn0, sn1, sn2, sn3, cb):
    print "-"*20
    print "Looking if card is on the DB..."
    card_id = is_on_db(sn0, sn1, sn2, sn3, cb)

    if card_id == False:
        print "This card is not on the DB. Creating new entry for this card..."
        insert_into_core_card(sn0, sn1, sn2, sn3, cb)

        card_id = is_on_db(sn0, sn1, sn2, sn3, cb)

    print "Creating log..."
    insert_into_core_log(card_id)

    print "Checking access permissions..."
    result = has_granted_access(card_id)
    print "-"*20
    return result
