from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserInput, Dataset
from .serializers import UserInputSerializer, DatasetSerializer
from .nlp_analysis import perform_nlp_analysis
from rest_framework.throttling import UserRateThrottle

class UserInputListCreateView(generics.ListCreateAPIView):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            user_input = serializer.validated_data['objective']

            # Create a UserInput instance with the validated data
            user_input_instance = UserInput(objective=user_input)
            user_input_instance.save()  # Save the instance to the database
            
            # Call the select_model function to determine the suitable model
            selected_model = perform_nlp_analysis(user_input)

            return Response(
                {
                    'id': user_input_instance.id,
                    'objective': user_input,
                    'selected_model': selected_model
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DatasetListCreateView(generics.ListCreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
