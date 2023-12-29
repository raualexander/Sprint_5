class Locators:

    account_page_open_link = '//a[@href="/account"]'  # ссылка для перехода в личный кабинет
    register_page_link = '//a[@class="Auth_link__1fOlj" and @href="/register"]'  # ссылка для  перехода на страницу регистрации
    name_input_register = '//fieldset[1]/div/div/input[@class ="text input__textfield text_type_main-default"]'  # поле ввода имени при регистрации
    email_input_register = '//fieldset[2]/div/div/input[@class="text input__textfield text_type_main-default"]'  # поле ввода почты для регистрации
    password_input_register = '//input[@name="Пароль"]'  # поле ввода пароля для регистрации
    registration_button = '//button[text()="Зарегистрироваться"]'  # кнопка "зарегистрироваться"
    email_input_signin = '//input[@name="name" and @type="text"]'  # поле ввода email для входа
    password_input_signin = '//input[@type="password"]'  # поле ввода пароля для входа
    signin_button = '//button[text()="Войти"]'  # кнопка "войти"
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
    sauces = '//span[text()="Соусы"]' # раздел "соусы" в меню конмтруктора
    sauce_item = '//*[@id="root"]/div[1]/main[1]/section[1]/div[2]/ul[2]/a[1]' #один из элементов раздела соусы
    buns = '//span[text()="Булки"]' #раздел "булки" в меню конструктора
    buns_item = '//*[@id="root"]/div[1]/main[1]/section[1]/div[2]/ul[1]/a[1]' #один из элементоа раздела булки
    fillings = '//span[text()="Начинки"]' #раздел "начинки" в меню конструктора
    fillings_item = '//*[@id="root"]/div[1]/main[1]/section[1]/div[2]/ul[3]/a[1]' #один из элементов раздела начинки
    item_name_in_card = '//p[1][@class="text text_type_main-medium mb-8"]' #название ингридиента в карточке ингридиента
