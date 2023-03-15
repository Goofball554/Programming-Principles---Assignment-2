import random

class Application:

    def getCode():
        # Asks the user to input the Product Code and checks whether the input is valid.
        codeCheck = False
        while codeCheck == False:
            code = input("Please enter the Product Code: ")
            if float(code) == int(code) and int(code) >= 100 and int(code) <= 1000:
                codeCheck = True

            else:
                code = input("Please enter the Product Code: ")
        return code

    def getName():
        #Asks the user to input the Product Name.
        name = input("Please enter the Product Name: ")

        return name

    def getSale():
        #Asks the user to input the Product Sale Price and checks whether the input is valid.
        saleCheck = False
        while saleCheck == False:
            sale = input("Please enter the Product Sale Price: ")
            if float(sale) > 0:
                saleCheck = True

        return sale

    def getCost():
        #Asks the user to input the Product Manufacture Cost and checks whether the input is valid.
        costCheck = False
        while costCheck == False:
            cost = input("Please enter the Product Manufacture Cost: ")
            if float(cost) > 0:
                costCheck = True

        return cost

    def getStock():
        #Asks the user to input the Stock Level and checks whether the input is valid.
        stockCheck = False
        while stockCheck == False:
            stock = input("Please enter the Stock Level: ")
            if float(stock) == int(stock) and int(stock) > 0:
                stockCheck = True

        return stock

    def getEstimate():
        #Asks the user to input the Estimated Monthly Units Manufactured and checks whether the input is valid. 
        estimateCheck = False
        while estimateCheck == False:
            estimate = input("Please enter the Estimated Monthly Units Manufactured: ")
            if float(estimate) == int(estimate) and int(estimate) >= 0:
                estimateCheck = True

        return estimate

    
    code = getCode()
    name = getName()
    cost = getCost()
    sale = getSale()
    stock = getStock()
    estimate = getEstimate()

class Logic(Application):
    def printStocks():
        #Prints the first half of the stock statement.
        print("******* Programming Principles Sample Stock Statenent *******")
        print("Product Code: ", Application.code)
        print("Product Name: ", Application.name)
        print("Sale Price: ", Application.sale, " CAD")
        print("Manufacture Cost: ", Application.cost, " CAD")
        print("Monthly Production: ", Application.estimate, " units (Approx.)")

        estimate = Application.estimate
        stock = Application.stock
        sale = Application.sale
        cost = Application.cost
        totalSold = 0

        #Prints the monthly portion of the stock statement.
        for i in range(12):
            sold = random.randrange(int(estimate) - 10, int(estimate) + 11)
            stock = int(stock) + int(estimate) - int(sold)
            totalSold = totalSold + int(sold)
            print("Month ", i + 1, ":")
            print("*     Manufactured: ", estimate)
            print("*     Sold: ", sold)
            print("*     Stock:", stock)
            
        #Prints the net profit of the stock statement.
        netProfit = round((totalSold * float(sale)) - (int(estimate) * 12 * float(cost)), 2)
        print("Net Profit: ", netProfit, " CAD")

    printStocks()

runProgram = Application()
printStock = Logic()
