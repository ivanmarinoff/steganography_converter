from django.shortcuts import render, redirect
from .models import Post
from .forms import TextForm, ImageForm, AudioForm
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .text_encrypt import text_encrypt, text_decrypt
from .audio_encrypt import audio_encrypt, music, audio_decrypt

@login_required
def history(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'audio_steg/history.html', context)


def about(request):
    return render(request, 'audio_steg/about.html', {'title': 'About'})


def encryptresult(request):
    return render(request, 'audio_steg/encryptresult.html')


class HistoryListView(ListView):
    model = Post
    template_name = 'audio_steg/history.html'
    context_object_name = 'posts'
    ordering = ['-date']

# Views

def steg_base(request):
    return render(request, '../templates/audio_steg/base.html')


def steg_welcome(request):
    return render(request, '../templates/audio_steg/welcome.html')


class StegAudioView(TemplateView):
    template_name = '../templates/audio_steg/audio_input.html'

    def get_context_data(self, **kwargs):
        form = AudioForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AudioForm(request.POST)

        if form.is_valid():
            Type = form.cleaned_data.get('stegtype')
            HiddenText = form.cleaned_data.get('hiddentext')
            choice_field = form.cleaned_data.get('choice_field')

            result = 'Invalid Form Input. Try Again!'
            if choice_field == '1':
                result1 = audio_encrypt(HiddenText)
                result2 = music(HiddenText)
                result = {'octalval': result1, 'notes': result2}

            elif choice_field == '2':
                result1 = audio_decrypt(HiddenText)
                result = {'notes': result1}
                print(result1)

        args = {'form': form, 'result': result, 'choice': choice_field}
        return render(request, self.template_name, args)


class StegTextView(TemplateView):
    template_name = '../templates/audio_steg/text_input.html'
    success_url = encryptresult

    def get_context_data(self, **kwargs):
        form = TextForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = TextForm(request.POST)

        if form.is_valid():
            stegtype = form.cleaned_data.get('stegtype')
            plaintext = form.cleaned_data.get('plaintext')
            hiddentext = form.cleaned_data.get('hiddentext')
            choice_field = form.cleaned_data.get('choice_field')
            result = 'Invalid Form Input. Try Again!'

            if choice_field == '1':
                result = text_encrypt(plaintext, hiddentext)
            elif choice_field == '2':
                # result = text_decrypt(plaintext)
                result = text_decrypt(self.success_url)

            # Update the form with the result (assuming you have a result field in your form)
            # form.instance.stegtype = result
            result = form.instance.stegtype

        args = {'form': form, 'result': result}

        return render(request, self.template_name, args)



class StegImageView(TemplateView):
    template_name = '../templates/audio_steg/image_input.html'

    def get_context_data(self, **kwargs):
        form = ImageForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)

        result = None  # Initialize the result variable

        if form.is_valid():
            Type = form.cleaned_data.get('stegtype')
            PlainText = form.cleaned_data.get('plaintext')
            HiddenText = form.cleaned_data.get('hiddentext')
            result = text_encrypt(PlainText, HiddenText)

        args = {'form': form, 'result': result}
        return render(request, self.template_name, args)