 # import the MongoAdmin base class
from mongonaut.sites import MongoAdmin
###import your custom models###
from polls.models import Employee
# instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Employee.mongoadmin = MongoAdmin()