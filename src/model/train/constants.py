WRITE_LOGS_TO_GOOGLE_DRIVE = False
DEVICE = 'cpu'

DATA_DIR = '../../data'
LOGS_DIR = '../../logs'
IMG_DIR = '../../img'
MODELS_DIR = '../../models'

SOS_TOKEN = 0
EOS_TOKEN = 1
UNK_TOKEN = 2
PAD_TOKEN = 3

MAX_LENGTH = 50

TRAIN_PROP = 0.7
VALID_PROP = 0.1
TEST_PROP = 0.2

HIDDEN_SIZE = 256
LEARNING_RATE = 0.01
TEACHER_FORCING_RATIO = 0.5

NUM_ITER = 100000
LOG_EVERY = 1000