# assigning the arn value to the variable my_arn
my_arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"
# aws_account extraction
aws_account_number = my_arn[13:25] 

print(f"the aws account number is {aws_account_number}")