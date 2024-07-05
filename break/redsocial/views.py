from django.shortcuts import render
from .models import Genero, Alumno

#declaracion de objeto
class persona:#objeto persona
    def __init__(self, nombre, edad):#dos propiedades nombre y edad
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def index(request):#definicion idex
    hijo=persona("Juan Perez", "7")#llenar el objeto

    lista=["Hamburguesas", "Papas fritas", "Completo"]#lista python

    alumnos= Alumno.objects.all()

    context = {"hijo":hijo, "nombre" : "Claudia Sofia", "comidas": lista, "alumnos":alumnos} #contexto= diccionario python

    return render(request, 'alumnos/index.html', context)#respuesta de index


def crud(request):#crud
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):#agregar alumnos
    if request.method != "POST":
        #no es un POST, por lo tanto se muestra el formulario para agregrar
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        #Es un POST, por lo tanto se recuperan los datos del formulario 
        #y se graban en la tabla.
        rut=request.POST["rut"] 
        nombre=request.POST["nombre"] 
        aPaterno=request.POST["paterno"] 
        aMaterno=request.POST["materno"] 
        fechaNac=request.POST["fechaNac"] 
        genero=request.POST["genero"]
        telefono = request.POST["telefono"] 
        email=request.POST["email"] 
        direccion=request.POST["direccion"] 
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero, 
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1 )
        obj.save()
        context={'mensaje': "Ok, datos grabados..."}

        return render(request, 'alumnos/alumnos_add.html', context)
    


def alumnos_del(request, pk): # eliminar alumno
    context={}
    try:

        alumno = Alumno.objects.get(rut=pk)
        
        alumno.delete()
        mensaje = "Bien, alumno eliminado..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje = "Error, rut no existe..."
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    

def alumnos_findEdit(request, pk): # editar alumno

    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()
        
        print(type(alumno.id_genero.genero))

        context = {'alumno': alumno, 'generos': generos}
        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            context = {'mensaje':"Error, rut no existe..."}
            return render(request, 'alumnos/alumnos_edit.html', context)



def alumnosUpdate(request): # editar alumno

    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["aPaterno"]
        aMaterno=request.POST["aMaterno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero = Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.nombre = nombre
        alumno.apellido_paterno = aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero = objGenero
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo = 1
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'generos':generos,'alumno':alumno }
        return render(request, 'alumnos/alumnos_edit.html', context)
    else:
        alumnos=Alumno.objects.all()
        context={'alumno':alumno }
        return render(request, 'alumnos/alumnos_list.html', context)
