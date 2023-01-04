from CourseRegistrationSimulation import CourseRegistrationSimulation
import logging

logging.basicConfig(
     filename='app.log',
     level=logging.DEBUG, 
     format= '[%(asctime)s] %(lineno)d %(levelname)s - %(message)s',
     datefmt='%H:%M:%S',filemode='w'
 )

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger(__name__)

logger.info('main')






simulation = CourseRegistrationSimulation()
simulation.startSimulation()








