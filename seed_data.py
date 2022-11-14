from blog.models import Post

Post(titulo="blog de prueba", resumen="short-content ", contenido="contenido del blog",
fecha="date_published", autor="seed_data").save()

print("se cargo con éxito la información")