// Tipos de datos en JavaScript
/*
Esto siver para comentaios
*/

var nombre = "Ariel"; // Tipo String
console.log(typeof nombre)
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000;// Tipo Numèrico
console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893"
}
console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera);

// Tipo de dato funcion 
function mifuncion(){};
console.log(typeof mifuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

// Tipos de dato clase
class persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

//Null: significa ausencia de valor
var y = null; //null no es tipo de dato pero es de tipo objet
console.log(typeof y);

//Tipo de dato array y empty string
var autos = ["Citroen","Audi","BMW","Ford"];
console.log(typeof autos);

var z = '';
console.log(z); //Esto se refiere a una cadena vacia
console.log(typeof z);