### **Project Overview**

This project is an automated testing suite for core features of an e-commerce website, including adding products to the cart, 
selecting categories, removing items from the cart and more. It was developed with Selenium for browser automation, Pytest for test structuring, 
and Allure for reporting.

### **Installation steps:**

Clone the repository.
Create a virtual environment: 

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install all packages and dependencies outlined in the requirements.txt file:

```bash
pip install -r requirements.txt or pip3 install -r requirements.txt
```

Run the tests using pytest and allure:

```bash
pytest --alluredir=reports/allure-results
```

Open the generated allure reports:

```bash
allure serve reports/allure-results
```

### **Project structure:**

```plaintext
├── base/
│   └── base_test.py
├── config/
│ ├── config.yaml
│ ├── configuration.py
│ └── driver_manager.py
├── locators/
│ ├── category_page_locators.py
│ ├── home_page_locators.py
│ ├── product_page_locators.py
│ └── sgopping_cart_locators.py
├── pages/
│ ├── base_page.py
│ ├── cart_side_menu_page.py
│ ├── category_page.py
│ ├── empty_cart_page.py
│ ├── home_page.py
│ ├── product_page.py
│ └── shopping_cart_page.py
├── reports/
├── tests/
│   ├── test_add_to_cart.py
│   ├── test_category_selection.py
│   ├── test_item_search.py
│   ├── test_remove_product_from_cart.py
│   └── test_update_product_quantity_in_cart.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

### **Video:**


https://github.com/user-attachments/assets/b9df54d3-ad44-493f-a1fd-727617a6aa8d





