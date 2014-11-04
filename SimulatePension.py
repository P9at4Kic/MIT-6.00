#
# Problem 1
#

def applyIntrest(f, change, growthRate):
    try:
        f.append(f[-1]*(growthRate*0.01+1)+change)
    except:
        f.append(change)

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """

    assert salary > 0, "invaled salary, not positive"
    assert save >= 0, "invaled save, negitive"
    assert growthRate >= 0, "invaled growthRate, negitive"
    assert years > 0, "invaled years, not positive"
    
    f = []
    change = salary * save * 0.01
    for y in range(years):
        applyIntrest(f, change, growthRate)
    return f

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    #print (nestEggFixed(-10, 0.5, 0.5, 1))
    #print (nestEggFixed(10, -0.5, 0.5, 1))
    #print (nestEggFixed(10, 0.5, -0.5, 1))
    #print (nestEggFixed(10, 0.5, 0.5, 0))
    
# testNestEggFixed()

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    
    assert salary > 0, "invaled salary, not positive"
    assert save >= 0, "invaled save, negitive"
    assert len (growthRates) != 0, "invaled growthRate, no elements"
        
    f = []
    change = salary * save * 0.01
    for g in growthRates:
        applyIntrest(f, change, g)
    return f

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # print (nestEggVariable(salary, save, []))

# testNestEggVariable()

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """

    assert savings > 0, "invaled savings, not positive"
    assert len (growthRates) != 0, "invaled growthRate, no elements"
    assert expenses >= 0, "invaled expenses, negitive"
    
    f = [savings]
    change = -expenses
    for g in growthRates:
        applyIntrest(f, change, g)
    return f
    

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

# testPostRetirement()

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """

    
    totalSaved = nestEggVariable(salary, save, preRetireGrowthRates)
    maxGuess = totalSaved[-1]
    minGuess = 0
    for i in range (100):
        guess = (maxGuess + minGuess) / 2.0
        pr = postRetirement(totalSaved[-1], postRetireGrowthRates, guess)
        if abs(pr[-1]) < epsilon:
            return guess
        elif pr[-1] > 0:
            minGuess = guess
        else:
            maxGuess = guess
    else: print("exided iteration limit")

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
testFindMaxExpenses()
