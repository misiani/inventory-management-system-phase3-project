# lib/helpers.py
from models.category import Category
from models.product import Product

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_categories():
    categories = Category.get_all()
    for category in categories:
        print(category)


def create_category():
    name = input("Enter the category's name: ")
    try:
        category = Category.create(name)
        print(f'Success: {category}')
    except Exception as exc:
        print("Error creating category: ", exc)

def find_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)
    print(category) if category else print(
        f'category {name} not found')
    
def find_category_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the category's id: ")
    category = Category.find_by_id(id_)
    print(category) if category else print(f'category {id_} not found')

def update_category():
    id_ = input("Enter the category's id: ")
    if category := Category.find_by_id(id_):
        try:
            name = input("Enter the category's new name: ")
            category.name = name

            category.update()
            print(f'Success: {category}')
        except Exception as exc:
            print("Error updating category: ", exc)
    else:
        print(f'Category {id_} not found')

def delete_category():
    id_ = input("Enter the department's id: ")
    if department := Category.find_by_id(id_):
        department.delete()
        print(f'Category {id_} deleted')
    else:
        print(f'Category {id_} not found')


## Product Functions

def create_product():
    name = input("Enter the product's name: ")
    price = int(input("Enter the product's price: "))
    stock = int(input("Enter the product's stock: "))
    category_id = int(input("Enter the product's category id: "))
    try:
        product = Product.create_product(name, price, stock, category_id)
        print(f'Success: {product}')
    except Exception as exc:
        print("Error creating product: ", exc)
    
def list_products():
    products = Product.get_all_products()
    for product in products:
        print(product)

def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    print(product) if product else print(
        f'Product {name} not found')


def find_Product_by_id():
    id_ = input("Enter the Product's id: ")
    product = Product.find_product_by_id(id_)
    print(product) if product else print(f'Product {id_} not found')