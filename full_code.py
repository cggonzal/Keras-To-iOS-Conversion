from keras.models import load_model
import coremltools

model.save('your_model.h5')

output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
your_model = coremltools.converters.keras.convert('your_model.h5', input_names=['image'], output_names=['output'], 
                                                   class_labels=output_labels, image_input_names='image')

#your_model.author = 'your name'
#your_model.short_description = 'Digit Recognition with MNIST'
#your_model.input_description['image'] = 'Takes as input an image'
#your_model.output_description['output'] = 'Prediction of Digit'

your_model.save('your_model_name.mlmodel')
