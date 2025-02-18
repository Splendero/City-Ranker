import csv

# Define the tax brackets as a dictionary
tax_brackets = {
    "Alberta": [
        (148269, 0.10),
        (177922, 0.12),
        (237230, 0.13),
        (355845, 0.14),
        (float('inf'), 0.15)
    ],
    "British Columbia": [
        (47937, 0.0506),
        (95875, 0.077),
        (110076, 0.105),
        (133664, 0.1229),
        (181232, 0.147),
        (252752, 0.168),
        (float('inf'), 0.205)
    ],
    "Manitoba": [
        (47000, 0.108),
        (100000, 0.1275),
        (float('inf'), 0.174)
    ],
    "New Brunswick": [
        (49958, 0.094),
        (99916, 0.14),
        (185064, 0.16),
        (float('inf'), 0.195)
    ],
    "Newfoundland and Labrador": [
        (43198, 0.087),
        (86395, 0.145),
        (154244, 0.158),
        (215943, 0.178),
        (275870, 0.198),
        (551739, 0.208),
        (1103478, 0.213),
        (float('inf'), 0.218)
    ],
    "Northwest Territories": [
        (50597, 0.059),
        (101198, 0.086),
        (164525, 0.122),
        (float('inf'), 0.1405)
    ],
    "Nova Scotia": [
        (29590, 0.0879),
        (59180, 0.1495),
        (93000, 0.1667),
        (150000, 0.175),
        (float('inf'), 0.21)
    ],
    "Nunavut": [
        (53268, 0.04),
        (106537, 0.07),
        (173205, 0.09),
        (float('inf'), 0.115)
    ],
    "Ontario": [
        (51446, 0.0505),
        (102894, 0.0915),
        (150000, 0.1116),
        (220000, 0.1216),
        (float('inf'), 0.1316)
    ],
    "Prince Edward Island": [
        (32656, 0.0965),
        (64313, 0.1363),
        (105000, 0.1665),
        (140000, 0.18),
        (float('inf'), 0.1875)
    ],
    "Quebec": [
        (51780, 0.14),
        (103545, 0.19),
        (126000, 0.24),
        (float('inf'), 0.2575)
    ],
    "Saskatchewan": [
        (52057, 0.105),
        (148734, 0.125),
        (float('inf'), 0.145)
    ],
    "Yukon": [
        (55867, 0.064),
        (111733, 0.09),
        (173205, 0.109),
        (500000, 0.128),
        (float('inf'), 0.15)
    ]
}

def calculate_tax(salary, province):
    """
    Calculate the total tax based on the salary and province.
    """
    if province not in tax_brackets:
        raise ValueError("Province not found in tax brackets.")
    
    brackets = tax_brackets[province]
    total_tax = 0
    remaining_income = salary

    for bracket in brackets:
        limit, rate = bracket
        if remaining_income <= 0:
            break
        taxable_amount = min(remaining_income, limit)
        total_tax += taxable_amount * rate
        remaining_income -= limit

    return total_tax

# Federal tax brackets
federal_tax_brackets = [
    (57375, 0.15),
    (114750, 0.205),
    (177882, 0.26),
    (253414, 0.29),
    (float('inf'), 0.33)
]

def calculate_federal_tax(salary):
    """
    Calculate the federal tax based on the salary.
    """
    total_tax = 0
    remaining_income = salary

    for bracket in federal_tax_brackets:
        limit, rate = bracket
        if remaining_income <= 0:
            break
        taxable_amount = min(remaining_income, limit)
        total_tax += taxable_amount * rate
        remaining_income -= limit

    return total_tax

def calculate_total_tax(salary, province):
    """
    Calculate the total tax (federal + provincial) based on the salary and province.
    """
    federal_tax = calculate_federal_tax(salary)
    provincial_tax = calculate_tax(salary, province)
    total_tax = federal_tax + provincial_tax
    return total_tax

def calculate_net_income(salary, province):
    """
    Calculate the net income after deducting federal and provincial taxes.
    """
    total_tax = calculate_total_tax(salary, province)
    net_income = salary - total_tax
    return net_income