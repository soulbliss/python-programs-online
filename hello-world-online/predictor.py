# this is an example for cortex release 0.21 and may not deploy correctly on other releases of cortex


class PythonPredictor:
    def __init__(self, config):
        print('initializing systems for the first time 🙂!')

    def predict(self, payload):
        
        print('received a new request ⚡')

        input = payload["name"]
        answer = payload["text"]
        

        output = "Hello world, welcome {}!".format(input)
        
        # process input
        
        output_string = answer*10



        # run you algorithm our here



        # process input end

        return {"greeting": output, "result": output_string}
