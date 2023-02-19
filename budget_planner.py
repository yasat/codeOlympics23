# Budget planner
import numpy as np

def budget_planner(monthly_income, bills, optional_expenses, priority):

    fixed_expenses = {'rent': 600, 'utilities': 200, 'phone': 50, 'internet': 50}
    

    remaining_budget = monthly_income - sum(fixed_expenses.values()) - sum(bills.values())
    

    if priority == 'high':
        optional_budget = remaining_budget * 0.5
    elif priority == 'medium':
        optional_budget = remaining_budget * 0.3
    else:
        optional_budget = remaining_budget * 0.2
    

    total_optional_cost = sum(optional_expenses.values())
    

    if total_optional_cost > optional_budget:
        print("You cannot afford all of your optional expenses this month.")
        print("Consider cutting back on some of your expenses or increasing your income.")
        return

    budget_plans = []
    for i in range(5):
        plan = {'fixed_expenses': fixed_expenses.copy(), 'bills': bills.copy(), 'optional_expenses': {}}
        remaining_budget = monthly_income
        

        optional_choices = list(optional_expenses.keys())
        while True:
            selected_choices = set(np.random.choice(optional_choices, size=3, replace=False))
            selected_expenses = {k:v for k,v in optional_expenses.items() if k in selected_choices}
            if sum(selected_expenses.values()) <= optional_budget:
                break
        plan['optional_expenses'] = selected_expenses
        remaining_budget -= sum(selected_expenses.values())
        

        for bill, cost in bills.items():
            if np.random.choice([True, False]):
                plan['bills'][bill] = cost
                remaining_budget -= cost
        

        if np.random.choice([True, False]):
            expense = np.random.choice(list(fixed_expenses.keys()))
            plan['fixed_expenses'][expense] = 0
            remaining_budget += fixed_expenses[expense]
        

        if np.random.choice([True, False]):
            splurge_cost = remaining_budget * 0.2
            plan['optional_expenses']['guilty pleasure'] = splurge_cost
            remaining_budget -= splurge_cost
        

        consequences = []
        if remaining_budget < 0:
            consequences.append('You will go into debt.')
        if sum(plan['fixed_expenses'].values()) != sum(fixed_expenses.values()):
            consequences.append('You may face consequences for missing a fixed expense.')
        if sum(plan['bills'].values()) != sum(bills.values()):
            consequences.append('You may face consequences for missing a bill.')
        if 'guilty pleasure' in plan['optional_expenses']:
            consequences.append('You may feel guilty about spending money on a splurge.')

        budget_plans.append((plan, consequences))
    

    for i, (plan, consequences) in enumerate(budget_plans):
        print(f"Budget Plan {i+1}:")
        print(f"Fixed Expenses: {plan['fixed_expenses']}")
        print(f"Bills: {plan['bills']}")
        print(f"Optional Expenses: {plan['optional_expenses']}")
        print(f"Consequences: {', '.join(consequences)}")
        print()







# User Inputs
monthly_income = 2000
bills = {'gas': 100, 'electricity': 80, 'water': 50}
optional_expenses = {'clothing': 10, 'entertainment': 75, 'dining out': 12, 'travel': 20, 'netflix': 12}
priority = 'medium'

# monthly_income = int(input())

# bills_names = list()
# bills_prices = list()

# biils_c = int(input())
# for i in range(bills_c):
#     bills_names.append(input())
# for i in range(biils_c):
#     bills_prices.append(int(input()))
    
# bills = dict(zip(bills_names, bills_prices))

# op_names = list()
# op_prices = list()

# op_c = int(input())
# for i in range(op_c):
#    op_names.append(input())
# for i in range(op_c):
#     op_prices.append(int(input()))
    
# optional_expenses = dict(zip(op_names, op_prices))

# priority = input()

# if(priority not in ["high", "medium","low"]):
#     priority = "medium"

budget_planner(monthly_income, bills, optional_expenses, priority)
