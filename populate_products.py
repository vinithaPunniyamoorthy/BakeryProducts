import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bakery_api.settings')
import django
django.setup()

from products.models import Product

# Delete existing products
Product.objects.all().delete()

# Product data
products = [
    {
        'name': 'Artisan Bread Loaf',
        'category': 'Bread',
        'price': 5.99,
        'description': 'Freshly baked artisan bread with a crispy crust and soft interior.',
        'image': 'https://via.placeholder.com/300x200/DEB887/000000?text=Artisan+Bread',
        'ingredients': 'Flour, Water, Yeast, Salt',
        'nutrition': 'calories: 250, protein: 8, carbs: 50, fat: 2'
    },
    {
        'name': 'Sourdough Bread',
        'category': 'Bread',
        'price': 6.49,
        'description': 'Tangy sourdough bread made with natural fermentation.',
        'image': 'https://via.placeholder.com/300x200/D2B48C/000000?text=Sourdough+Bread',
        'ingredients': 'Flour, Water, Sourdough Starter, Salt',
        'nutrition': 'calories: 220, protein: 7, carbs: 45, fat: 1'
    },
    {
        'name': 'Chocolate Cake',
        'category': 'Cake',
        'price': 12.99,
        'description': 'Rich and moist chocolate cake topped with chocolate ganache.',
        'image': 'https://via.placeholder.com/300x200/8B4513/FFFFFF?text=Chocolate+Cake',
        'ingredients': 'Flour, Sugar, Cocoa Powder, Eggs, Butter, Chocolate',
        'nutrition': 'calories: 350, protein: 5, carbs: 45, fat: 18'
    },
    {
        'name': 'Vanilla Cupcake',
        'category': 'Cake',
        'price': 3.99,
        'description': 'Light and fluffy vanilla cupcake with buttercream frosting.',
        'image': 'https://via.placeholder.com/300x200/FFF8DC/000000?text=Vanilla+Cupcake',
        'ingredients': 'Flour, Sugar, Butter, Eggs, Vanilla Extract',
        'nutrition': 'calories: 280, protein: 3, carbs: 38, fat: 12'
    },
    {
        'name': 'Chocolate Chip Cookies',
        'category': 'Cookie',
        'price': 2.49,
        'description': 'Classic chocolate chip cookies with gooey centers.',
        'image': 'https://via.placeholder.com/300x200/D2691E/FFFFFF?text=Chocolate+Chip+Cookies',
        'ingredients': 'Flour, Butter, Sugar, Chocolate Chips, Eggs',
        'nutrition': 'calories: 180, protein: 2, carbs: 25, fat: 8'
    },
    {
        'name': 'Oatmeal Raisin Cookies',
        'category': 'Cookie',
        'price': 2.49,
        'description': 'Chewy oatmeal cookies studded with raisins.',
        'image': 'https://via.placeholder.com/300x200/CD853F/FFFFFF?text=Oatmeal+Raisin+Cookies',
        'ingredients': 'Oats, Flour, Butter, Raisins, Cinnamon',
        'nutrition': 'calories: 160, protein: 3, carbs: 28, fat: 6'
    },
    {
        'name': 'Croissant',
        'category': 'Pastry',
        'price': 4.99,
        'description': 'Buttery, flaky croissant perfect for breakfast.',
        'image': 'https://via.placeholder.com/300x200/F5DEB3/000000?text=Croissant',
        'ingredients': 'Flour, Butter, Milk, Yeast, Sugar',
        'nutrition': 'calories: 230, protein: 5, carbs: 25, fat: 12'
    },
    {
        'name': 'Danish Pastry',
        'category': 'Pastry',
        'price': 5.49,
        'description': 'Sweet Danish pastry filled with fruit or custard.',
        'image': 'https://via.placeholder.com/300x200/FFE4B5/000000?text=Danish+Pastry',
        'ingredients': 'Flour, Butter, Sugar, Fruit Filling, Yeast',
        'nutrition': 'calories: 300, protein: 6, carbs: 35, fat: 15'
    },
    {
        'name': 'Assorted Bakery Mix',
        'category': 'Assorted',
        'price': 15.99,
        'description': 'A selection of our finest bakery products.',
        'image': 'https://via.placeholder.com/300x200/FAF0E6/000000?text=Assorted+Bakery+Mix',
        'ingredients': 'Various',
        'nutrition': 'calories: 250, protein: 5, carbs: 40, fat: 10'
    }
]

# Create products
for product_data in products:
    Product.objects.create(**product_data)

print('Products created successfully')
