import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def gender_count(data):
    plt.figure(figsize=(14,5))
    plt.style.use('fivethirtyeight')
    a= sns.countplot(x='Gender', data=data , palette = 'Set3')
    a.set_xlabel(xlabel= "Gender",fontsize=18)
    a.set_ylabel(ylabel = "Gender count", fontsize = 18)
    a.set_title(label = "Gender Count in E-Commerce Platform", fontsize = 20)
    plt.savefig("static/gender_count.png")


def type_of_customers(data):
    plt.style.use('ggplot')
    plt.figure(figsize= (14,5))
    a = sns.countplot(x = "Customer type", data = data, palette = "dark")
    a.set_xlabel("Customer type", fontsize = 16)
    a.set_ylabel("Customer Count", fontsize = 16)
    a.set_title("Type of customers", fontsize = 25)
    plt.savefig("static/type_of_customers.png")


def type_of_customers_in_branches(data):
    plt.figure(figsize=(14,5))
    plt.style.use('classic')
    a = sns.countplot(x = "Customer type", hue = "Branch", data = data, palette= "Set3")
    a.set_xlabel(xlabel = "Branches", fontsize = 16)
    a.set_ylabel(ylabel = "Customer Count", fontsize = 16)
    a.set_title(label = "Customer type in different branches", fontsize = 25)
    plt.savefig("static/type_of_customers_in_branches.png")

def payment_methods(data):
    plt.figure(figsize = (14,5))
    a = sns.countplot(x = "Payment", data = data, palette = "tab10")
    a.set_xlabel(xlabel = "Customer's Payment method", fontsize = 16)
    a.set_ylabel(ylabel = " Customer Count", fontsize = 16)
    a.set_title(label = "Payment Methods", fontsize= 25)
    plt.savefig("static/payment_methods.png")


def payment_distribution(data):
    plt.figure(figsize = (14,5))
    plt.style.use('classic')
    a = sns.countplot(x="Payment", hue = "Branch", data = data, palette= "Set3")
    a.set_xlabel(xlabel = "Payment method", fontsize = 16)
    a.set_ylabel(ylabel = "Peple Count", fontsize = 16)
    a.set_title(label = "Payment Distribution of all branches", fontsize= 25)
    plt.savefig("static/payment_distribution.png")

def rating_distribution(data):
    plt.figure(figsize=(14,5)) 
    a = sns.boxplot(x="Branch", y = "Rating" ,data =data, palette= "hls")
    a.set_xlabel(xlabel = "Branches", fontsize = 16)
    a.set_ylabel(ylabel = "Rating distribution", fontsize = 16)
    a.set_title("Rating distribution across branches", fontsize = 25)
    plt.savefig("static/rating_distribution.png")

def sales_per_hour(data):
    data["Time"]= pd.to_datetime(data["Time"])
    data["Hour"]= (data["Time"]).dt.hour
    plt.figure(figsize=(14,5))
    plt.style.use('classic')
    SalesTime = sns.lineplot(x="Hour", y ="Quantity", data = data).set_title("Sales per Hour")
    plt.savefig("static/sales_per_hour.png")

def average_sales(data):
    plt.figure(figsize=(14,5))
    plt.style.use('classic')
    a = sns.boxenplot(x = "Quantity", y = "Product line", data = data)
    a.set_xlabel(xlabel = "Qunatity Sales",fontsize = 16)
    a.set_ylabel(ylabel = "Product Line", fontsize = 16)
    a.set_title(label = "Average sales of all lines of products", fontsize = 25)
    plt.savefig("static/average_sales.png")


def sales_product_count(data):
    plt.figure(figsize=(14,5))
    plt.style.use('classic')
    a = sns.countplot(y='Product line', data=data, order = data['Product line'].value_counts().index)
    a.set_xlabel(xlabel = "Sales count", fontsize = 16)
    a.set_ylabel(ylabel= "Product Line", fontsize = 16)
    a.set_title(label = "Products Sales Count", fontsize = 25)
    plt.savefig("static/sales_product_count.png")


def product_total_sales(data):
    plt.figure(figsize=(14,5))
    plt.style.use('classic')
    a = sns.boxenplot(y= "Product line", x= "Total", data = data)
    a.set_xlabel(xlabel = "Total sales", fontsize = 16)
    a.set_ylabel(ylabel = "Product Line", fontsize = 16)
    a.set_title(label = " Product Total Sales", fontsize = 25)
    plt.savefig("static/product_total_sales.png")


def average_ratings_product(data):
    plt.figure(figsize = (14,5))
    plt.style.use('classic')
    a = sns.boxenplot(y = "Product line", x = "Rating", data = data)
    a.set_xlabel("Rating", fontsize = 16)
    a.set_ylabel("Product line", fontsize = 16)
    a.set_title("Average rating of product line", fontsize = 25)
    plt.savefig("static/average_ratings_product.png")


def product_sales_by_gender(data):
    plt.style.use('classic')
    plt.figure(figsize = (14,5))
    a= sns.stripplot(y= "Product line", x = "Total", hue = "Gender", data = data)
    a.set_xlabel(xlabel = " Total sales of products")
    a.set_ylabel(ylabel = "Product Line")
    a.set_title(label = "Product sales on the basis of gender")
    plt.savefig("static/product_sales_by_gender.png")



graphs={
    "gender_count":gender_count,
    "type_of_customers":type_of_customers,
    "type_of_customers_in_branches":type_of_customers_in_branches,
    "payment_methods":payment_methods,
    "payment_distribution":payment_distribution,
    "rating_distribution":rating_distribution,
    "sales_per_hour":sales_per_hour,
    "product_sales_by_gender":product_sales_by_gender,
    "average_ratings_product":average_ratings_product,
    "product_total_sales":product_total_sales,
    "sales_product_count":sales_product_count,
    "average_sales":average_sales
}