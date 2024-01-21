from DB_FUNCTIONS.db_connection import connectToDb
from flask import session


def ListUsers():
    connection = connectToDb()
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM sportform;')
    players = cursor.fetchall()
    
    cursor.close()
    connection.close()

    # List of Tuples to List of Dictionaries
    formatted_players = []

    for player in players:
        id,name,sport = player

        # formatted_players.append(dict_players)
        formatted_players.append({'id':id,'name':name,'sport':sport})
        # print('function sport dict',formatted_players)

    return formatted_players


def CreateUser(name:str,sport:str):
    connection = connectToDb()
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO sportform(player_name,sport) VALUES (%s,%s)
            ''',(name,sport))
    
    connection.commit()
    cursor.close()
    connection.close()


    # print('id is',id)
    # print(type(id))

def deleteUser(id:str):
    connection = connectToDb()
    cursor = connection.cursor()

    cursor.execute('DELETE FROM sportform WHERE id = %s',(id,))
    connection.commit()
    cursor.close()
    connection.close()





# ADD TO CART
def AllMoviesCart():
    connection = connectToDb()

    cursor = connection.cursor()

    cursor.execute('select * from movies_cart')

    all_movies = cursor.fetchall()
    # Converting tuple to dictionary
    formatted_movies = [{'id':movie[0],'title':movie[1]} for movie in all_movies]

    cursor.close()
    connection.close()

    return formatted_movies


def findCartItems(cart):
    # print('session cart',session['cart'])
    connection = connectToDb()
    cursor = connection.cursor()

    cartItems = []
    # for items in session['cart']:
    for items in cart:
        print('items no. are',items)
        cursor.execute('SELECT * FROM movies_cart WHERE id = %s',(items,))
        cartItems.append(cursor.fetchone())

    print(cartItems)
    formatted_cartItems = [items[1] for items in cartItems]
    cursor.close()
    connection.close()
    print('cartItems are: ',formatted_cartItems)
    return formatted_cartItems