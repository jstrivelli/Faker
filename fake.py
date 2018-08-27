import os
import boto3
from faker import Faker

faker = Faker()

# create new provider class
class MyProvider(BaseProvider):
    #catagory = ''
    a = rand.choice(string.letters)
   
    driversLicenseFormats = ('#######', a + '######', 'D########', '0########', '#########', a + '#######', a + '############', a + '##############')
    def driversLicenseNumber(self):
        return self.bothify(self.random_element(self.driversLicenseFormats))

    def employeeIdentificationNumber(self):
        employeeIdentificationFormat = ('##-#######',)
        return self.bothify(self.random_element(employeeIdentificationFormat))

    def billingAccountNumber(self):
        billingAccountFormat = ('#########', )
        return self.bothify(self.random_element(billingAccountFormat))
    #Generates Random file name with a given name to add in the begining foilowed by 4 random numbers
    def fileNameGen(self, catagory):
        formatStruct = catagory + '######' + '.html'
        fileFormat = (formatStruct,)
        return self.bothify(self.random_element(fileFormat))
    
# then add new provider to faker instance
faker.add_provider(MyProvider)


def lambda_handler(event, context):
        client = boto3.client('s3')
        bucketName = os.environ['BUCKETNAME']
        client.put_object(
        Bucket = bucketName,
        ACL = 'public-read',
        Body = "HELLO WORLD",
        Key= 'hello3.txt'
        )
        s3 = boto3.resource('s3')
        s3.Bucket(bucketName).put_object(Key='www/red-hat.txt', Body="YOYOYOYOYOYOY")
        return
