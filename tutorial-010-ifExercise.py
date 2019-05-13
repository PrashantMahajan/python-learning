house_cost = 1000000
credit = 79

if credit > 80:
    print(f'Please put {house_cost/10}');
elif 60 < credit < 80:
    print(f'Please put {house_cost // 9}');
else:
    print(f'Please Put {house_cost/5}');