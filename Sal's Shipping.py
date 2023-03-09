weight = 41.5
## “Ground Shipping”.
if weight <= 2:
  cost = weight * 1.5 + 20
  print('the cost of ground shipping '+ str(cost))
elif weight > 2 and weight <= 6:
  cost = weight * 3.0 + 20
  print('the cost of ground shipping: '+ str(cost))
elif weight > 6 and weight <= 10:
  cost = weight * 4.0 + 20
  print('the cost of ground shipping: '+ str(cost))
elif weight > 10 :
  cost = weight * 4.75 + 20
  print('the cost of ground shipping: '+ str(cost))

  ## premium ground shipping
premium_shipping= 125.00
print('the cost of premium ground shipping: '+ str(premium_shipping))

## Drone Shipping
if weight <= 2:
  cost = weight * 4.5 
  print('the cost of Drone Shipping '+ str(cost))
elif weight > 2 and weight <= 6:
  cost = weight * 9
  print('the cost of Drone Shipping: '+ str(cost))
elif weight > 6 and weight <= 10:
  cost = weight * 12
  print('the cost of Drone Shipping: '+ str(cost))
elif weight > 10 :
  cost = weight * 14.25
  print('the cost of Drone Shipping: '+ str(cost))
