from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig"


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/eligibility")
def eligibility():
    return render_template("eligibility.html")

@app.route("/estimate")
def estimate():
    return render_template("estimate.html")

@app.route("/FAQ")
def faq():
    return render_template("FAQ.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/calc20", methods=["POST", "GET"])
def calc20():
    # flash(f"Thank you, {str(request.form['name_input'])}, here is your estimate!")

    # year_in_question = int(request.form['year_input'])
    # flash(f"Year requesting credit = {year_in_question}")

    # est_company_size = str(request.form['company_size_input'])
    # flash(f"General size of company = {est_company_size}")

    # pct_health_cvg = int(request.form['percent_health_input'])
    # flash(f"Employee health plan coverage = {pct_health_cvg}")

    # num_weeks_impact = int(request.form['weeks_impacted_input'])
    # flash(f"Number of weeks impacted by policies = {num_weeks_impact}")

    # pct_wages_no_serve = int(request.form['percent_wagepay_input'])
    # flash(f"Percent of wages paid with no service = {pct_wages_no_serve}")

    # num_employ_furlough = int(request.form['num_furloughed_input'])
    # flash(f"Number of employees furloughed = {num_employ_furlough}")

    # avg_weeks_furlough = int(request.form['weeks_furloughed_input'])
    # flash(f"Average number of furlough weeks = {avg_weeks_furlough}")

    # amt_loan_received = int(request.form['loan_amount_input'])
    # flash(f"Amount of PPP loan(s) received = {amt_loan_received}")
    
    # num_weeks_overlap = int(request.form['weeks_overlap_input'])
    # flash(f"Number of weeks overlapped with PPP coverage = {num_weeks_overlap}")

    avg_num_employ_2020 = int(request.form['num_employees_input_2020'])
    avg_monthly_pay_2020 = int(request.form['monthly_pay_input_2020'])
    avg_monthly_health_2020 = int(request.form['avg_health_cost_input_2020'])

    sum = (avg_monthly_pay_2020 + (avg_monthly_health_2020 * avg_num_employ_2020)) * 12
    limit = 10000 * avg_num_employ_2020
    estimate = (sum * 0.5) if sum < limit else (limit *0.5)

    text_to_flash = "Your estimated Qualified Wages are: $ {amount:,.2f}"
    flash(text_to_flash.format(amount=sum))

    text_to_flash = "Your estimated Employee Retention Credit is: $ {amount:,.2f}"
    flash(text_to_flash.format(amount=estimate))

    flash("Please contact and schedule a full audit today!")

    return render_template("estimate.html", visible="hidden")


@app.route("/calc21", methods=["POST", "GET"])
def calc21():

    avg_num_employ_2021 = int(request.form['num_employees_input_2021'])
    avg_monthly_pay_2021 = int(request.form['monthly_pay_input_2021'])
    avg_monthly_health_2021 = int(request.form['avg_health_cost_input_2021'])

    sum = (avg_monthly_pay_2021 + (avg_monthly_health_2021 * avg_num_employ_2021)) * 12
    limit = 10000 * avg_num_employ_2021
    estimate = (sum * 0.5) if sum < limit else (limit *0.5)

    text_to_flash = "Your estimated Qualified Wages are: $ {amount:,.2f}"
    flash(text_to_flash.format(amount=sum))

    text_to_flash = "Your estimated Employee Retention Credit is: $ {amount:,.2f}"
    flash(text_to_flash.format(amount=estimate))

    flash("Please contact and schedule a full audit today!")
    
    return render_template("estimate.html", visible="hidden")


@app.route("/calcElig", methods=["POST", "GET"])
def calcElig():

    quarters2019 = []
    quarters2019.append(int(request.form['input_2019_Q1']))
    quarters2019.append(int(request.form['input_2019_Q2']))
    quarters2019.append(int(request.form['input_2019_Q3']))
    quarters2019.append(int(request.form['input_2019_Q4']))
    quarters2020 = []
    quarters2020.append(int(request.form['input_2020_Q1']))
    quarters2020.append(int(request.form['input_2020_Q2']))
    quarters2020.append(int(request.form['input_2020_Q3']))
    quarters2020.append(int(request.form['input_2020_Q4']))
    quarters2021 = []
    quarters2021.append(int(request.form['input_2021_Q1']))
    quarters2021.append(int(request.form['input_2021_Q2']))
    quarters2021.append(int(request.form['input_2021_Q3']))
    quarters2021.append(int(request.form['input_2021_Q4']))

    eligible_quarters = []
    is_next_eligible = False
    for q in range(len(quarters2019)):
        if ((quarters2019[q] - quarters2020[q]) / quarters2019[q]) > 0.5:
            eligible_quarters.append(quarters2020[q])
            is_next_eligible = True
        else:
            if is_next_eligible:    
                eligible_quarters.append(quarters2020[q])
            is_next_eligible = False

    flash(f"{len(eligible_quarters)} eligible quarters in 2020")

    eligible_quarters.clear()
    for q in range(len(quarters2019)-1):
        if ((quarters2019[q] - quarters2021[q]) / quarters2019[q]) > 0.2:
            eligible_quarters.append(quarters2021[q])
            is_next_eligible = True
        else:
            if is_next_eligible:
                eligible_quarters.append(quarters2021[q])
            is_next_eligible = False

    flash(f"{len(eligible_quarters)} eligible quarters in 2021")


    return render_template("eligibility.html", visible="hidden")

