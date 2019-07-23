class MinioClient():
    def __init__(self):
        self.__isConnected  = False
        self.__isCacheReady = False

    def login(self, host, port, accesskey, secretkey):
        # verifylogin
        from minio import Minio
        import urllib3

        if self.__isConnected:
            return Session(host, port, self)
        hostport = host + ":"+str(port)
        try:
            httpClient = urllib3.PoolManager(cert_reqs='CERT_NONE')
            urllib3.disable_warnings()
            self.__minioClient = Minio(hostport, access_key=accesskey, secret_key=secretkey, http_client=httpClient)
            self.__isConnected = True
            print ("Connected to minio "+hostport)
            return Session(host, port, self)
        except Exception as ex:
            print (ex)
            print ("Error: Unable to connect to "+hostport)
            sys.exit(1)

    def make_bucket(self):
        pass
        
    def list_buckets(self):
        return self.__minioClient.list_buckets()
        
    def bucket_exists(self):
        pass
        
    def remove_bucket(self):
        pass
        
    def list_objects(self, bucket_name, prefix=None, recursive=False):
        return self.__minioClient.list_objects(bucket_name, prefix, recursive)
        
    def list_objects_v2(self):
        pass
        
    def list_incomplete_uploads(self):
        pass
        
    def get_object(self):
        pass
        
    def put_object(self):
        pass
        
    def stat_object(self):
        pass
        
    def copy_object(self):
        pass
        
    def get_partial_object(self):
        pass
        
    def remove_object(self):
        pass
        
    def remove_objects(self):
        pass
        
    def remove_incomplete_upload(self):
        pass


from terminio.outputprinter import OutputPrinter

class Session():
    def __init__(self, host, port, client):
        self.host = host
        self.port = port
        self.client = client
        self.printer = OutputPrinter()
        

    def get_prompt(self):
        return "{}:{}".format(self.host, self.port)

class Cache():
    pass

class LoginError(Exception):
    pass