from CourseRegistrationSimulation import CourseRegistrationSimulation
import logging



def main():

 configureLogger()
 simulation = CourseRegistrationSimulation()
 simulation.startSimulation()


def configureLogger():
 logging.basicConfig(
     filename='app.log',
     level=logging.DEBUG, 
     format= '[%(asctime)s] %(lineno)d %(levelname)s - %(message)s',
     datefmt='%H:%M:%S',filemode='w',encoding='utf-8'
 )
 console = logging.StreamHandler()
 console.setLevel(logging.DEBUG)
 formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
 console.setFormatter(formatter)
 logging.getLogger('').addHandler(console)

if __name__=="__main__":
    main()






