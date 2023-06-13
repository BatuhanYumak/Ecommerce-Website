def contact(request):
 template = loader.get_template('contact.html')
  return HttpResponse(template.render())
if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                # do something after form is submitted
        else:
            form = ContactForm()

        return render(request, 'contact.html', {'form': form})