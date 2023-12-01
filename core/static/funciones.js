function obtenerDatos(event) {
    event.preventDefault();
    var destino = document.getElementById('texto').value;
    var opcs = document.getElementById('opcs');
    var cantidad = document.getElementById('texto2').value;
    var estado = document.getElementById('checkbox1');
    var tipo = document.getElementById('checkbox2');
    var limpia = estado.checked ? 'Limpia' : 'Sucia';
    var ingreso = tipo.checked ? 'Ingreso' : 'Egreso';

    var valorOpcion = opcs.value;

    var ropa;

    if (valorOpcion === 'value1') {
        ropa = 'Camiseta';
    } else if (valorOpcion === 'value2') {
        ropa = 'Pantalón';
    } else if (valorOpcion === 'value3') {
        ropa = 'Pantuflas';
    } else if (valorOpcion === 'value4') {
        ropa = 'Bata';
    } else if (valorOpcion === 'value5') {
        ropa = 'Cofia';
    }

    console.log(destino, ropa, cantidad, limpia, ingreso);
}