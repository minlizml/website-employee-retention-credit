
avg_num_employ_2020 = 3
avg_monthly_pay_2020 = 3333.3333
avg_monthly_health_2020 = 0


sum = (avg_monthly_pay_2020 + (avg_monthly_health_2020 * avg_num_employ_2020)) * 12
limit = 10000 * avg_num_employ_2020
estimate = (sum * 0.5) if sum < limit else (limit *0.5)

text_to_flash = "Estimated credit: $ {amount:,.2f}"
print(text_to_flash.format(amount=estimate))