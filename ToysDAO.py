import mysql.connector
import dbconfig as cfg

class ToysDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect( 
        host= cfg.mysql["host"],
        user= cfg.mysql["user"],
        password=cfg.mysql["password"],
        database=cfg.mysql["database"]
)
        print("connection made Fiona")

    def create(self, toys):
        cursor = self.db.cursor()
        sql="insert into toys (name, maker, model, colour, quantity) values (%s,%s,%s,%s,%s)" 
        values = [
                toys['name'],
                toys['maker'],
                toys['model'],
                toys['colour'],
                toys['quantity']
                ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    def createDispatches(self, dispatches):
        cursor = self.db.cursor()
        sql="insert \
            INTO dispatches (name, address, product_id) \
            values(%s, %s,\
            (select id from toys where name = %s))" 
        values = [
                dispatches['name'],
                dispatches['address'],
                dispatches['toyname']
                ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        cursor = self.db.cursor() 
        sql="select toys.*, 'Yes' AS 'hasdispatches' \
            FROM toys where \
            exists (select 1 from dispatches \
            where dispatches.product_id = toys.id) \
            UNION \
            select toys.*, 'No' AS 'hasdispatches' \
            from toys where \
            NOT exists (select 1 from dispatches \
            where dispatches.product_id = toys.id)" 
        cursor.execute(sql)
        results = cursor.fetchall() 
        returnArray = []
        # print(results)
        for result in results:
            resultsAsDict = self.convertToDict(result)
            returnArray.append(resultsAsDict)

        return returnArray 

    def getAllToyNames(self):
        cursor = self.db.cursor() 
        sql="select distinct(name) from toys where quantity > 0 order by name" 
        cursor.execute(sql)
        results = cursor.fetchall() 
        returnArray = []
        print(results)
        for result in results:
            resultsAsDict = self.convertToyNamesToDict(result)
            returnArray.append(resultsAsDict)

        return returnArray   
         

        
    
    

    def getAllDispatches(self):
        cursor = self.db.cursor() 

        sql = "SELECT \
            dispatches.dispatch_id AS dispatch_id, \
            dispatches.name AS name, \
            dispatches.address AS address, \
            toys.name AS toyname  \
            FROM dispatches \
            INNER JOIN toys ON dispatches.product_id = id \
            ORDER by dispatches.dispatch_id"
        cursor.execute(sql)
        results = cursor.fetchall() 
        returnArray = []
        # print(results)
        for result in results:
            resultsAsDict = self.convertDispatchesToDict(result)
            returnArray.append(resultsAsDict)

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select toys.*, 'Yes' AS 'hasdispatches' \
            FROM toys where \
            toys.id = %s \
            AND exists (select 1 from dispatches \
            where dispatches.product_id = toys.id) \
            UNION \
            select toys.*, 'No' AS 'hasdispatches' \
            from toys where \
            toys.id = %s \
            AND NOT exists (select 1 from dispatches \
            where dispatches.product_id = toys.id)" 

        # sql="select * from toys where id = %s"
        values = (id,id)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def findDispatchByID(self, dispatch_id):
        cursor = self.db.cursor()
        sql = "SELECT \
            dispatches.dispatch_id AS dispatch_id, \
            dispatches.name AS name, \
            dispatches.address AS address, \
            toys.name AS toyname  \
            FROM dispatches \
            INNER JOIN toys ON dispatches.product_id = id \
            WHERE dispatches.dispatch_id = %s"
        values = (dispatch_id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertDispatchesToDict(result)



    def update(self,values):
        cursor = self.db.cursor()
        sql="update toys set maker= %s, model = %s, colour =%s, quantity= %s where id= %s" 
        cursor.execute(sql, values)
        self.db.commit()
        print("updated", id)
        cursor.close()
    
    def updateStock(self, dispatch_id):
        print(dispatch_id)
        cursor = self.db.cursor()
        sql="update toys set quantity= quantity -1 \
            where id IN \
            (select product_id from dispatches \
            where dispatch_id = %s)" 
        values =(dispatch_id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("updated stock", values)
        cursor.close()
        

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from toys where id = %s" 
        values = (id,)

        cursor.execute(sql, values) 
        self.db.commit()
        print("delete done for toy with ", id) 
    

    def convertToDict(self, result):
        colnames = ['id','name', 'maker', 'model', 'colour', 'quantity', 'hasdispatches']
        toys = {}

        if result: 
            for i, colname in enumerate(colnames):
                value = result[i]
                toys[colname] = value
        return toys


    def convertToyNamesToDict(self, result):
        colnames = ['toyname']
        toynames = {}

        if result: 
            for i, colname in enumerate(colnames):
                value = result[i]
                toynames[colname] = value
        return toynames

    def convertDispatchesToDict(self, result):
        colnames = ['dispatch_id','name', 'address', 'toyname']
        dispatches = {}

        if result: 
            for i, colname in enumerate(colnames):
                value = result[i]
                dispatches[colname] = value
        return dispatches



toysDAO = ToysDAO()