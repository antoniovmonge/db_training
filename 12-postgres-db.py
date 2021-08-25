import psycopg2

conn = psycopg2.connect(
    database='red30',
    user='antonio',
    password='password',
    host='localhost',
    port='5432'
    )

cursor = conn.cursor()

################
# CREATE TABLE #
################

# cursor.execute(
#     '''
#     CREATE TABLE Sales(
#       ORDER_NUM INT PRIMARY KEY,
# 		ORDER_TYPE TEXT,
# 		CUST_NAME TEXT,
# 		PROD_NUMBER TEXT,
# 		PROD_NAME TEXT,
# 		QUANTITY INT,
# 		PRICE REAL,
# 		DISCOUNT REAL,
# 		ORDER_TOTAL REAL
#     );
#     '''
# )

# cursor.execute('SELECT * FROM SALES LIMIT 10')
# # print(cursor.fetchall())
# for i in cursor.fetchall():
#     print(i)

#################
# INSERT VALUES #
#################

cursor.execute(
    '''
    INSERT INTO sales(
        ORDER_NUM,
        ORDER_TYPE,
		CUST_NAME,
		PROD_NUMBER,
		PROD_NAME,
		QUANTITY,
		PRICE,
		DISCOUNT,
    	ORDER_TOTAL
    )
    VALUES(
        1105910,
        'Retail',
        'Syman Mapstone',
        'EB521',
        'Understanding Artificial Inteligence',
        3,
        19.5,
        0,
        58.5
    )
    '''
)

conn.commit()

cursor.execute(
    '''
    SELECT CUST_NAME, ORDER_TOTAL FROM SALES
    WHERE ORDER_NUM=1105910
    '''
)

rows = cursor.fetchall()
for row in rows:
    print('CUST_NAME =', row[0])
    print('ORDER TOTAL =', row[1], '\n')

conn.close()
