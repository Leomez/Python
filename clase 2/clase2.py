# Solicitar al usuario que ingrese su Nombre, Apellido, Edad y Correo electronico

nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
edad = input("Ingrese su edad: ");
correo = input("Ingrese su correo electronico: ");
#Mostrar los datos ingresados por la persona en forma de tarjeta:

print("\nTarjeta de Presentacion");
print("------------------------------");
print("Nombre: ",nombre);
print("Apellido: ",apellido);
print("Edad: ",edad);
print("Correo: ",correo);
print("------------------------------");

#Mostrar los datos ingresados por la persona en forma de tabla:
print("\nTabla de Presentacion");
print("----------------------------------------------------------");
print("| Nombre  | Apellido | Edad | Correo              |");
print("--------------------------");
print("|", nombre, "|", apellido, "    |", edad, "|", correo, "|"); 
print("---------------------------------------------------------");


