print("===== FOOD DELIVERY ORDER DECISION AND RISK ASSESSMENT SYSTEM =====")
order_amount = float(input("Enter order amount: "))
delivery_distance = float(input("Enter delivery distance in km: "))
customer_type = input("Enter customer type (Regular/Premium/New): ").strip().lower()
customer_rating = float(input("Enter customer rating (1-5): "))
restaurant_rating = float(input("Enter restaurant rating (1-5): "))
preparation_time = int(input("Enter preparation time in minutes: "))
payment_method = input("Enter payment method (Online/COD): ").strip().lower()
weather_condition = input("Enter weather condition (Normal/Rain/Storm): ").strip().lower()
demand_level = input("Enter demand level (Low/Medium/High): ").strip().lower()
peak_hour = input("Is it peak hour? (Yes/No): ").strip().lower()
previous_cancellations = int(input("Enter number of previous cancellations: "))
if order_amount < 100:
    order_status = "Rejected"
    decision_reason = "Order amount is below the minimum order value."
elif delivery_distance > 20:
    order_status = "Rejected"
    decision_reason = "Delivery distance is beyond the serviceable limit."
elif restaurant_rating < 2.5:
    order_status = "Rejected"
    decision_reason = "Restaurant rating is too low."
elif preparation_time > 90:
    order_status = "Manual Review"
    decision_reason = "Restaurant preparation time is unusually high."
else:
    order_status = "Accepted"
    decision_reason = "Order satisfies the basic acceptance conditions."
if delivery_distance <= 5:
    delivery_charge = 30
elif delivery_distance <= 10:
    delivery_charge = 50
elif delivery_distance <= 15:
    delivery_charge = 80
else:
    delivery_charge = 120
if weather_condition == "storm":
    delivery_charge = delivery_charge + 50
elif weather_condition == "rain":
    delivery_charge = delivery_charge + 20
if peak_hour == "yes":
    delivery_charge = delivery_charge + 20
discount = 0
if customer_type == "premium":
    discount = order_amount * 0.15
elif customer_type == "regular":
    if order_amount >= 1000:
        discount = order_amount * 0.10
    elif order_amount >= 500:
        discount = order_amount * 0.05
elif customer_type == "new":
    if order_amount >= 500:
        discount = order_amount * 0.10
    else:
        discount = order_amount * 0.05
if peak_hour == "yes" and demand_level == "high":
    priority_status = "High Priority"
elif weather_condition == "storm":
    priority_status = "High Priority"
elif customer_type == "premium":
    priority_status = "Priority"
else:
    priority_status = "Normal Priority"
if previous_cancellations >= 5:
    cancellation_risk = "High"
elif previous_cancellations >= 3:
    cancellation_risk = "Medium"
else:
    cancellation_risk = "Low"
if weather_condition == "storm" and cancellation_risk == "Low":
    cancellation_risk = "Medium"
if delivery_distance > 15 and previous_cancellations >= 3:
    cancellation_risk = "High"
if restaurant_rating >= 4.5 and preparation_time <= 30:
    restaurant_status = "Excellent and Fast"
elif restaurant_rating >= 4.0 and preparation_time <= 45:
    restaurant_status = "Good"
elif restaurant_rating >= 3.0 and preparation_time <= 60:
    restaurant_status = "Average"
else:
    restaurant_status = "Needs Attention"
manual_review = False
manual_review_reason = "No manual review required."
if cancellation_risk == "High":
    manual_review = True
    manual_review_reason = "High previous cancellation risk."
elif customer_rating < 2.5:
    manual_review = True
    manual_review_reason = "Low customer rating."
elif payment_method == "cod" and order_amount >= 2000:
    manual_review = True
    manual_review_reason = "High-value Cash on Delivery order."
elif weather_condition == "storm":
    manual_review = True
    manual_review_reason = "Severe weather condition."
elif preparation_time > 90:
    manual_review = True
    manual_review_reason = "Very high preparation time."
if order_status == "Rejected":
    final_order_category = "Rejected Order"
elif manual_review:
    final_order_category = "Manual Review Order"
elif cancellation_risk == "High":
    final_order_category = "High Risk Order"
elif priority_status == "High Priority":
    final_order_category = "Priority Order"
elif customer_type == "premium":
    final_order_category = "Premium Order"
else:
    final_order_category = "Standard Order"
final_payable_amount = order_amount + delivery_charge - discount
if final_payable_amount < 0:
    final_payable_amount = 0
print("\n" + "=" * 65)
print("                 FINAL FOOD DELIVERY ORDER REPORT")
print("=" * 65)
print("\nOrder Amount: Rs.", round(order_amount, 2))
print("Delivery Distance:", delivery_distance, "km")
print("Customer Type:", customer_type.title())
print("Customer Rating:", customer_rating, "/ 5")
print("Restaurant Rating:", restaurant_rating, "/ 5")
print("Preparation Time:", preparation_time, "minutes")
print("Payment Method:", payment_method.upper())
print("Weather Condition:", weather_condition.title())
print("Demand Level:", demand_level.title())
print("Peak Hour:", peak_hour.title())
print("Previous Cancellations:", previous_cancellations)
print("\n" + "-" * 65)
print("Order Status:", order_status)
print("Decision Reason:", decision_reason)
print("Delivery Charge: Rs.", round(delivery_charge, 2))
print("Discount: Rs.", round(discount, 2))
print("Priority Delivery Status:", priority_status)
print("Cancellation Risk:", cancellation_risk)
print("Restaurant Status:", restaurant_status)
if manual_review:
    print("Manual Review Status: Manual Review Required")
else:
    print("Manual Review Status: No Manual Review Required")

print("Manual Review Reason:", manual_review_reason)
print("Final Order Category:", final_order_category)
print("Final Payable Amount: Rs.", round(final_payable_amount, 2))
print("\n" + "=" * 65)
print("                    END OF ORDER REPORT")
print("=" * 65)
