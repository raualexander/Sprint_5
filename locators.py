class Locators:

    account_page_open_link = '//a[@href="/account"]'  # ссылка для перехода в личный кабинет
    register_page_link = '//*[@id="root"]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]'  # ссылка для  перехода на страницу регистрации
    name_input_register = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  # поле ввода имени при регистрации
    email_input_register = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # поле ввода почты для регистрации
    password_input_register = '//input[@name="Пароль"]'  # поле ввода пароля для регистрации
    registration_button = '//*[@id="root"]/div/main/div/form/button'  # кнопка "зарегистрироваться"
    email_input_signin = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  # поле ввода email для входа
    password_input_signin = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'  # поле ввода пароля для входа
    signin_button = '//*[@id="root"]/div/main/div/form/button'  # кнопка "войти"
    order_history_link = '//a[@href="/account/order-history"]' #пункт меню в профиле(используется для ожидания)
    incorrect_password_warning = '//p[@class="input__error text_type_main-default"]'
    signin_button_from_main_page = '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    signin_form = '//form[@class="Auth_form__3qKeq mb-20"]' #форма авторизации
    signin_link = '//a[@class="Auth_link__1fOlj"]' #ссылка на страницу аввторизации
    forgot_password_link = '//a[@href="/forgot-password"]' #ссылка на страницу восстановлениия пароля
    constructor_link = '//a[@href="/" and @class="AppHeader_header__link__3D_hX"]' #ссылка на раздел конструктор(главная)
    logo_link = '//a[@href="/"]' #ссылка на главную в логотипе
    constructor_header = '//h1[@class="text text_type_main-large mb-5 mt-10"]' # заголовок "Конструктор" на главной
    logout_button = '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]' # кнопка выхода из аккаунта
    sauces = '//*[@id="root"]/div[1]/main[1]/section[1]/div[1]/div[2]' # раздел "соусы" в меню конмтруктора
    sauce_item = '//*[@id="root"]/div[1]/main[1]/section[1]/div[2]/ul[2]/a[1]' #один из элементов раздела соусы
    buns = '//*[@id="root"]/div[1]/main[1]/section[1]/div[1]/div[1]' #раздел "булки" в меню конструктора
    buns_item = '//*[@id="root"]/div[1]/main[1]/section[1]/div[2]/ul[1]/a[1]' #один из элементоа раздела булки
    fillings = '//*[@id="root"]/div[1]/main[1]/section[1]/div[1]/div[3]' #раздел "начинки" в меню конструктора
    fillings_item = '//*[@id="root"]/div[1]/main[1]/section[1]/div[2]/ul[3]/a[1]' #один из элементов раздела начинки
    item_name_in_card = '//p[1][@class="text text_type_main-medium mb-8"]' #название ингридиента в карточке ингридиента
