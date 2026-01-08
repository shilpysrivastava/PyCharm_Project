from pages.LoginPage import LoginPage

#("Rahul","Sheety","RahulS","RahulS@123")

def test_bookStore(setup):
    driver = setup
    login_page = LoginPage(driver)
    load_profile = login_page.login("RahulS","Rahul@123")
    load_profile.userProfile()

    # newUser=login_page.open_registration_form()
    # if driver.current_url == "https://demoqa.com/register" :
    #   newUser.register_user("Tripti","Sharma","TriptiS","TriptiS@123")


