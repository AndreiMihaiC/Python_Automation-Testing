<h1>Automation Project for saucedemo</h1>

The purpose of this project is to use all acquired Python automated testing knowledge and apply it, such as: to ensure correct and optimal functionality, user authentication, product search, purchase process and overall site performance- of the web.

Application under test: SINSAY

Tools used: Unittest

<ol>
<h2> Test Plan </h2>
<br>

           1.Page opening verification test:  

Test Type: Smoke test  

Action: Accessing the website https://www.saucedemo.com/  

Expected Result: The page opens correctly or not. 
           
           2. Login test:  

           a) Valid login test:  

Test Type: Positive test  

Action: Entering correct username and password at login  

Expected Result: Successful login  

           b) Invalid login test:  

Test Type: Negative test  

Action: Entering incorrect username and password  

Expected Result: Display message  

          c) Error message login test:  

Test Type: Negative test  

Action: Entering incorrect username and/or password  

Expected Result: Display error message 

           3. Logout test:  

Test Type: Functional test  

Action: Clicking the logout button  

Expected Result: Successful logout 

           4. Sidebar menu opening and closing test:  

Test Type: Functional test  

Action: Opening and then closing the sidebar menu  

Expected Result: Sidebar menu opens and closes correctly 

           5. Product adding test:  

Test Type: Functional test  

Action: Adding a product to the cart  

Expected Result: Product added successfully to the cart 

           6. Product deletion test:  

Test Type: Functional test  

Action: Deleting a product from the cart  

Expected Result: Product deleted correctly from the cart or the cart is empty 

           7. Product ordering test:  

Test Type: End-to-end test  

Action: Adding a product to the cart and completing the order  

Expected Result: Order placed successfully 

           8. Accessing the product details page test:  

Test Type: Functional test  

Action: Accessing the page with the details of a product  

Expected Result: The product details page opens correctly 

           9. Changing the quantity of the added product in the cart test:  

Test Type: Functional test  

Action: Changing the quantity of the added product in the cart  

Expected Result: Changing the quantity of the product 

           10. Accessing the main page by the "Back to products" button test:  

Test Type: Functional test  

Action: Clicking the "Back to products" button on a product page  

Expected Result: Redirecting to the main page of the site 

 
  


<ol>
<h2> Test Case </h2>
<br>

           Test Case 1: Verify page opening  

Procedure: Access https://www.saucedemo.com/  

Expected Result: The page should load correctly or display an error message  

           Test Case 2a: Login with correct username and password  

Procedure: Enter a correct username and password at login  

Expected Result: Successful login  

           Test Case 2b: Login with incorrect username and password  

Procedure: Enter an incorrect username and password at login  

Expected Result: Display an error message  

           Test Case 3: Logout  

Procedure: Click on the logout button  

Expected Result: Successful logout  

           Test Case 4: Open and close the side menu  

Procedure: Open and close the side menu  

Expected Result: The side menu should open and close correctly  

           Test Case 5: Add product to cart  

Procedure: Add a product to the cart  

Expected Result: The product should be successfully added to the cart  

           Test Case 6: Remove product from cart  

Procedure: Remove a product from the cart  

Expected Result: The product should be removed from the cart or the cart should be empty  

           Test Case 7: Place an order for a product  

Procedure: Add a product to the cart and complete the order  

Expected Result: The order should be successfully placed  

           Test Case 8: Access product details page  

Procedure: Access the page with the details of a product  

Expected Result: The page with the product details should open correctly  

           Test Case 9: Modify the quantity of a product  

Procedure: Modify the quantity and input the desired number of the same product Expected Result: Able to modify the quantity of the product added to the cart  

           Test Case 10: Access the main page through the "Back to products" button  

Procedure: Click on the "Back to products" button on a product page  

Expected Result: Redirect to the main page of the website 



<ol>
<h2> Bug Report </h2>
<br>

 	I. Title: Order placed successfully even if the cart is empty  

           Description: I noticed a bug on the site where I was able to place an order even though the cart was empty.  

           Steps to replicate the bug: 

1. Access the site and log in to your account: 

site: https://www.saucedemo.com/       username: standard_user      password: secret_sauce 

2. Go to the shopping cart button and access it without having anything in it. 

3. Click on the "Checkout" button 

4. Access the payment page and fill in the necessary details to place the order, then click on the "Continue" button 

5. Click on the "Finish" button. 

           Result obtained: The order was successfully placed, even though my cart was empty. And I received an order confirmation message.  

           Expected result: It should not be possible to place an order without having products in the cart.  

           Operating System: Windows 10 Browser: Google Chrome  

           Priority: High  

 

           II. Title: Modifying the quantity of the product added to the cart: 

           Description: I noticed a bug on the site where I couldn't modify the quantity of the desired product. You cannot add 2 or more products to the cart from the same product.  

           Steps to replicate the bug: 

1. Access the site and log in to your account: 

site: https://www.saucedemo.com/ username: standard_user password: secret_sauce 

2. Choose a desired product and click on "Add to cart" to add it to the cart 

3. Click on the shopping cart icon, located in the top right of the page 

4. Try to modify the desired quantity, located under "QTY"  

           Result obtained: The product was added to the cart, but when you try to modify the quantity, you cannot make any changes, the quantity is always '1'.  

           Expected result: When you view the products in your cart, you should be able to modify the desired quantity.  

           Operating System: Windows 10 Browser: Google Chrome  

           Priority: High 

 


