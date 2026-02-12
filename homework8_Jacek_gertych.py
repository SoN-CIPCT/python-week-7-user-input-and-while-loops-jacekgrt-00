pizza_orders = ["pepperoni", "hawaiian", "sausage", "supreme", "veggie"]
finished_pizzas = []

ordercount = 0
for pizzas in pizza_orders:
    if ordercount < 5:
          print("Your pizza pie is finished!")
          finished_pizzas.append(pizza_orders[ordercount])
          ordercount = ordercount + 1
    if ordercount == 5:
         finishedcount = 0
         while finishedcount < 5:
              print("The",finished_pizzas[finishedcount],"pizza was made.")
              finishedcount = finishedcount + 1