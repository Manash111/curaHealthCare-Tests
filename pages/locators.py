

class Locators():
    base_url = "https://katalon-demo-cura.herokuapp.com"
    url_login=f"{base_url}/profile.php#login"

    #login locators
    input_username = "//input[@id='txt-username']"
    input_password = "//input[@id='txt-password']"
    btn_login = "//button[@id='btn-login']"

    #Appointment locators
    select_facility = "//select[@id='combo_facility']"
    checkBox_readmission = "//input[@id='chk_hospotal_readmission']"

    radio_medicare = "//*[@id='radio_program_medicare']"
    radio_medicaid = "//input[@id='radio_program_medicaid']"
    radio_none = "//input[@id='radio_program_none']"

    date_visitDate = "//input[@id='txt_visit_date']"
    textarea_comment = "//textarea[@id='txt_comment']"

    btn_bookAppointment = "//button[@id='btn-book-appointment']"

    #menu
    menu_toggle = "//a[@id='menu-toggle']"

    #logout
    link_logout = "//a[normalize-space()='Logout']"

    #history
    link_history = "//a[normalize-space()='History']"

    no_appointment = "//p[normalize-space()='No appointment.']"