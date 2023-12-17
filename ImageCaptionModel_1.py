import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pickle import load
from keras.applications.xception import Xception #to get pre-trained model Xception
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from tqdm.notebook import tqdm as tqdm #to check loop progress

def extract_features(filename, model):
  try:
    image = Image.open(filename)
  except:
    print("ERROR: Can't open image! Ensure that image path and extension is correct")
  image = image.resize((299,299))
  image = np.array(image)
  # for 4 channels images, we need to convert them into 3 channels
  if image.shape[2] == 4:
    image = image[..., :3]
  image = np.expand_dims(image, axis=0)
  image = image/127.5
  image = image - 1.0
  feature = model.predict(image)
  return feature
def word_for_id(integer, tokenizer):
  for word, index in tokenizer.word_index.items():
    if index == integer:
      return word
  return None
def generate_desc(model, tokenizer, photo, max_length):
  in_text = ''
  for i in range(max_length):
    sequence = tokenizer.texts_to_sequences([in_text])[0]
    sequence = pad_sequences([sequence], maxlen=max_length)
    pred = model.predict([photo,sequence], verbose=0)
    pred = np.argmax(pred)
    word = word_for_id(pred, tokenizer)
    if word is None:
      break
    if word == 'end':
      break
    in_text += ' ' + word
  return in_text

max_length = 32
tokenizer = load(open("models/tokenizer.p","rb"))
model = load_model('models/model_9.h5')
xception_model = Xception(include_top=False, pooling="avg")

def img2text(fname):
  img_path = f'{fname}.png'
  photo = extract_features(img_path, xception_model)
  # img = Image.open(img_path)
  description = generate_desc(model, tokenizer, photo, max_length)
  # plt.imshow(img)

  return description