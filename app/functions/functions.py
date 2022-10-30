def handle_uploaded_file(f):
    with open('app/static/images'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)