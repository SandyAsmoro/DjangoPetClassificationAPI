import os
import pickle
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Path ke model yang disimpan
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pickle')

# Load model saat server dijalankan
with open(MODEL_PATH, 'rb') as file:
    knn_model = pickle.load(file)

class AnimalClassifier(APIView):
    def post(self, request):
        data = request.data
        try:
            height = float(data.get("height"))
            weight = float(data.get("weight"))
            length = float(data.get("length"))
            furlength = float(data.get("furlength"))
            pawsize = float(data.get("pawsize"))
            earshape = float(data.get("earshape"))

            # Format input ke array numpy
            input_data = np.array([[height, weight, length, furlength, pawsize, earshape]])

            # Prediksi menggunakan model
            prediction = knn_model.predict(input_data)

            # Interpretasi hasil prediksi
            animal = "Cat" if prediction[0] == 0 else "Dog"

            # Response hasil
            return Response({"animal": animal}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
