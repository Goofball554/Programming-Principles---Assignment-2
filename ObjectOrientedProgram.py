import random
codeCheck = False
saleCheck = False
costCheck = False
stockCheck = False
estimateCheck = False

totalSold = 0



# Asks the user to input the Product Code and checks whether the input is valid.
while codeCheck == False:
    code = input("Please enter the Product Code: ")

    if float(code) == int(code) and int(code) >= 100 and int(code) <= 1000:
        codeCheck = True

#Asks the user to input the Product Name.
name = input("Please enter the Product Name: ")

#Asks the user to input the Product Sale Price and checks whether the input is valid.
while saleCheck == False:
    sale = input("Please enter the Product Sale Price: ")

    if float(sale) > 0:
        saleCheck = True

#Asks the user to input the Product Manufacture Cost and checks whether the input is valid.
while costCheck == False:
    cost = input("Please enter the Product Manufacture Cost: ")

    if float(cost) > 0:
        costCheck = True

#Asks the user to input the Stock Level and checks whether the input is valid.
while stockCheck == False:
    stock = input("Please enter the Stock Level: ")

    if float(stock) == int(stock) and int(stock) > 0:
        stockCheck = True

#Asks the user to input the Estimated Monthly Units Manufactured and checks whether the input is valid. 
while estimateCheck == False:
    estimate = input("Please enter the Estimated Monthly Units Manufactured: ")

    if float(estimate) == int(estimate) and int(estimate) >= 0:
        estimateCheck = True

    print("******* Programming Principles Sample Stock Statenent *******")
    print("Product Code: ", code)
    print("Product Name: ", name)
    print("Sale Price: ", sale, " CAD")
    print("Manufacture Cost: ", cost, " CAD")
    print("Monthly Production: ", estimate, " units (Approx.)")

    for i in range(12):
        sold = random.randrange(int(estimate) - 10, int(estimate) + 11)
        stock = int(stock) + int(estimate) - int(sold)
        totalSold = totalSold + int(sold)
        print("Month ", i + 1, ":")
        print("*     Manufactured: ", estimate)
        print("*     Sold: ", sold)
        print("*     Stock:", stock)

    netProfit = totalSold * (float(sale) - float(cost))
    print("Net Profit: ", netProfit, " CAD")
