from django.db import models

import mysql.connector
from datetime import date

# Define your classes
class Club:
    def __init__(self, club_id, name, number_of_players, cups, stadium, date_of_establishment):
        self.club_id = club_id
        self.name = name
        self.date_of_establishment = date_of_establishment
        self.stadium = stadium
        self.cups = cups
        self.number_of_players = number_of_players

    def __str__(self):
        return f"{self.name} ({self.club_id}) - Established: {self.date_of_establishment}, Stadium: {self.stadium}, Cups: {self.cups}, Players: {self.number_of_players}"


class Coach:
    def __init__(self, coach_id, name, surname, age, experience, number_of_cups, club_id, category_id):
        self.coach_id = coach_id
        self.name = name
        self.surname = surname
        self.age = age
        self.experience = experience
        self.number_of_cups = number_of_cups
        self.club_id = club_id
        self.category_id = category_id

    def __str__(self):
        return f"{self.name} {self.surname} - Age: {self.age}, Experience: {self.experience}, Cups: {self.number_of_cups}, Club ID: {self.club_id}, Category ID: {self.category_id}"


class Category:
    def __init__(self, category_id, level, cups, number_of_players, club_id):
        self.category_id = category_id
        self.level = level
        self.cups = cups
        self.number_of_players = number_of_players
        self.club_id = club_id

    def __str__(self):
        return f"Category ID: {self.category_id}, Level: {self.level}, Cups: {self.cups}, Number of Players: {self.number_of_players}, Club ID: {self.club_id}"


class Contract:
    def __init__(self, player_id, start_date, end_date, penal_clause, salary, club_id):
        self.player_id = player_id
        self.start_date = start_date
        self.end_date = end_date
        self.penal_clause = penal_clause
        self.salary = salary
        self.club_id = club_id

    def __str__(self):
        return f"Player ID: {self.player_id}, Start Date: {self.start_date}, End Date: {self.end_date}, Penal Clause: {self.penal_clause}, Salary: {self.salary}, Club ID: {self.club_id}"


class Player:
    def __init__(self, player_id, name, surname, club_id, category_id):
        self.player_id = player_id
        self.name = name
        self.surname = surname
        self.club_id = club_id
        self.category_id = category_id

    def __str__(self):
        return f"Player ID: {self.player_id}, Name: {self.name}, Surname: {self.surname}, Club ID: {self.club_id}, Category ID: {self.category_id}"


class PlayerInfo:
    def __init__(self, player_id, position, foot, height, weight, goals, assists, matches, yellow_card, red_card):
        self.player_id = player_id
        self.position = position
        self.foot = foot
        self.height = height
        self.weight = weight
        self.goals = goals
        self.assists = assists
        self.matches = matches
        self.yellow_card = yellow_card
        self.red_card = red_card

    def __str__(self):
        return f"Player ID: {self.player_id}, Position: {self.position}, Foot: {self.foot}, Height: {self.height}, Weight: {self.weight}, Goals: {self.goals}, Assists: {self.assists}, Matches: {self.matches}, Yellow Cards: {self.yellow_card}, Red Cards: {self.red_card}"


class Worker:
    def __init__(self, worker_id, name, surname, occupation, salary, tel, club_id):
        self.worker_id = worker_id
        self.name = name
        self.surname = surname
        self.occupation = occupation
        self.salary = salary
        self.tel = tel
        self.club_id = club_id

    def __str__(self):
        return f"Worker ID: {self.worker_id}, Name: {self.name}, Surname: {self.surname}, Occupation: {self.occupation}, Salary: {self.salary}, Telephone: {self.tel}, Club ID: {self.club_id}"


# Function to establish and close connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aziz112211",
        database="footballclub"
    )


def retrieve_data():
    try:
        # Establishing a connection to the database
        connection = get_connection()

        if connection.is_connected():
            print("Connection successful")

            # Creating a cursor object
            cursor = connection.cursor()

            # Retrieve data from the club table
            cursor.execute("SELECT * FROM club")
            rows = cursor.fetchall()
            clubs = [Club(*row) for row in rows]

            # Retrieve data from the coach table
            cursor.execute("SELECT * FROM coach")
            rows = cursor.fetchall()
            coaches = [Coach(*row) for row in rows]

            # Retrieve data from the category table
            cursor.execute("SELECT * FROM category")
            rows = cursor.fetchall()
            categories = [Category(*row) for row in rows]

            # Retrieve data from the contract table
            cursor.execute("SELECT * FROM contract")
            rows = cursor.fetchall()
            contracts = [Contract(*row) for row in rows]

            # Retrieve data from the player table
            cursor.execute("SELECT * FROM player")
            rows = cursor.fetchall()
            players = [Player(*row) for row in rows]
            print(players[0])
            # Retrieve data from the player_info table
            cursor.execute("SELECT * FROM player_info")
            rows = cursor.fetchall()
            player_infos = [PlayerInfo(*row) for row in rows]

            # Retrieve data from the worker table
            cursor.execute("SELECT * FROM worker")
            rows = cursor.fetchall()
            workers = [Worker(*row) for row in rows]

            # Closing the cursor and connection
            cursor.close()
            connection.close()
            print("Connection closed")

            return clubs, coaches, categories, contracts, players, player_infos, workers

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")


# Function to call the INSERT_PLAYER procedure
def call_insert_player_procedure(name, surname, club_id, category_id):
    try:
        # Establishing a connection to the MySQL database
        conn = get_connection()

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("INSERT_PLAYER", [name, surname, club_id, category_id])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# Function to call the INSERT_PLAYER_INFO procedure
def call_insert_player_info(player_id, position, foot, height, weight, goals, assists, matches, yellow_card, red_card):
    try:
        # Establishing a connection to the MySQL database
        conn = get_connection()

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("INSERT_PLAYER_INFO", [player_id, position, foot, height, weight, goals, assists, matches, yellow_card, red_card])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def call_insert_category_procedure(level, cups, players, club_id):
    try:
        conn = get_connection()

        cursor = conn.cursor()
        cursor.callproc("INSERT_CATEGORY", [level, cups, players, club_id])
        conn.commit()
        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()


def call_insert_club_procedure(name, cups, num_players, stadium, doe):
    try:
        # Establishing a connection to the MySQL database
        conn = get_connection()

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("INSERT_CLUB", [name, cups, num_players, stadium, doe])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        # Closing the cursor and connection
        if 'conn' in locals():
            cursor.close()
            conn.close()



def call_insert_coach_procedure(name, surname, age, experience, cups, club_id, category_id):
    try:
        # Establishing a connection to the MySQL database
        conn = get_connection()

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("INSERT_COACH", [name, surname, age, experience, cups, club_id, category_id])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        # Closing the cursor and connection
        if 'conn' in locals():
            cursor.close()
            conn.close()



def call_insert_contract_procedure(player_id, start_date, end_date, penal_clause, salary, club_id):
    try:
        # Establishing a connection to the MySQL database
        conn = get_connection()
        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("INSERT_CONTRACT", [player_id, start_date, end_date, penal_clause, salary, club_id])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        # Closing the cursor and connection
        if 'conn' in locals():
            cursor.close()
            conn.close()


def call_insert_worker_procedure(name, surname, occupation, salary, tel, club_id):
    try:
        # Establishing a connection to the MySQL database
        conn = get_connection()

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("INSERT_WORKER", [name, surname, occupation, salary, tel, club_id])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        # Closing the cursor and connection
        if 'conn' in locals():
            cursor.close()
            conn.close()


def call_update_table_values_procedure(table_name, column_name, new_value, condition_column, condition_operator, condition_value):
    try:
        # Establishing a connection to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aziz112211",
            database="footballclub"
        )

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("update_table_values", [table_name, column_name, new_value, condition_column, condition_operator, condition_value])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        # Closing the cursor and connection
        if 'conn' in locals():
            cursor.close()
            conn.close()


import mysql.connector

def call_delete_from_table_procedure(table_name, condition_column, condition_operator, condition_value):
    try:
        # Establishing a connection to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aziz112211",
            database="footballclub"
        )

        # Creating a cursor object
        cursor = conn.cursor()

        # Calling the procedure with parameters
        cursor.callproc("delete_from_table", [table_name, condition_column, condition_operator, condition_value])

        # Committing the transaction
        conn.commit()

        print("Procedure called successfully!")

    except mysql.connector.Error as error:
        print(f"Error calling procedure: {error}")

    finally:
        # Closing the cursor and connection
        if 'conn' in locals():
            cursor.close()
            conn.close()


# Example usage
clubs, coaches, categories, contracts, players, player_infos, workers = retrieve_data()
call_delete_from_table_procedure("club", "CLUB_ID", "=",21)





