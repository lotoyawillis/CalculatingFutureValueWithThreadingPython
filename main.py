# Name: Lotoya Willis
# Date: 11/12/2023
# Assignment: 10
# Due Date: 11/12/2023
# About this project: Build a small scale real-world application that uses
# techniques involving secure, distributed, and parallel computing
# Assumptions: Assumes that the total number of payments is the number of
# compounding periods per year times the number of years
# All work below was performed by Lotoya Willis

import random
import time
from concurrent.futures import ThreadPoolExecutor


# global list variable
li = []


def future_value(pv, i, n, t):
    # calculates the future value based on present value, interest rate
    # per period, the number of compounding periods per year,
    # and the number of years. The number of years and future values are
    # appended to "li" and the function returns the future value

    fv = pv * (1 + (i/n))**(n*t)
    payment_num = n*t
    li.append(payment_num)
    li.append(fv)

    return fv


def main():
    random.seed(time.time())

    # present value
    pv = 100000

    # interest values
    r1 = random.uniform(.05, .1)
    r2 = random.uniform(.05, .1)
    r3 = random.uniform(.05, .1)

    # I left these here just in case the grader wants to see
    # the different interest values

    # print(r1)
    # print(r2)
    # print(r3)

    # number of compounding periods per year
    n = 1

    # number of years
    t = 2

    # initializes "highest"
    highest = 0

    # creates a ThreadPoolExecutor with max_workers=3,
    # submits the tasks, and saves the values to "values"
    with ThreadPoolExecutor(max_workers=3) as exe:
        values = [exe.submit(future_value, pv, r1, n, t), exe.submit(future_value, pv, r2, n, t),
                  exe.submit(future_value, pv, r3, n, t)]

        # calculates the highest fv
        for value in values:
            if highest < value.result():
                highest = value.result()

    # displays the values of "li" and the highest future value
    for i in range(6):
        if i % 2 == 0:
            print("total number of payments: "+str(li[i])+" Future Value: {:0.2f}".format(li[i+1]))

    print("Highest future value: {:0.2f}".format(highest))


if __name__ == '__main__':
    main()
