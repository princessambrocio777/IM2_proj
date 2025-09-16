def convert_usd(usd):
    inr = usd * 88.043      
    gbp = usd * 0.7377  
    cny = usd * 7.1247    
    return inr, gbp, cny

while True:
    s = input("Enter dollar ($) (* to exit): ")
    if s == "*":
        print("Bye")
        break
    
    dollars = s.split("@")
    print(f"{'Dollar($)':<12}{'Rupee(R)':<15}{'Pound(P)':<15}{'Yuan(Y)':<15}")
    for d in dollars:
        usd = float(d)
        inr, gbp, cny = convert_usd(usd)
        print(f"{usd:<12.2f}{inr:<15.2f}{gbp:<15.2f}{cny:<15.2f}")