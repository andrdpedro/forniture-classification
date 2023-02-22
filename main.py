from train import Training
from classifier import Classifier

def run_model():
    training = Training()
    model = training.model
    class_names = training.class_names
    return model, class_names

def classification(file_name: str, model, class_names):
    classifier = Classifier(model, file_name, class_names)
    classifier.classifie_image()
    
    return classifier.score, classifier.classified_class

if __name__ == "__main__":
    model, class_names = run_model()
    classification("cama.jpg", model, class_names)