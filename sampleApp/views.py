from django.shortcuts import render

from django.views import View

from .models import sampleModel
from .forms import sampleForms

class samplePage(View):
    template_name='index.html'

    def get(self, request, pk):
        sampleRecord=sampleModel.objects.get(id=pk)
        sampleForm=sampleForms(instance=sampleRecord)
        dcContext={'sampleForm': sampleForm}
        return render(request, self.template_name, context=dcContext)

    def post(self, request, pk):
        sampleRecord=sampleModel.objects.get(id=pk)
        sampleForm=sampleForms(request.POST, instance=sampleRecord)
        if sampleForm.has_changed():
            print(f'Record has changed - {sampleForm.changed_data}')
        dcContext={'sampleForm': sampleForm}
        return render(request, self.template_name, context=dcContext)
