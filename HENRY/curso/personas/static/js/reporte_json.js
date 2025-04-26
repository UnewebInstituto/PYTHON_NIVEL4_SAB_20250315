/* 
Antes de usar jQuery 
const mostrarContenido = () =>{
    var contenido = document.getElementById('parrafo1').innerHTML;
    alert(contenido);
}
*/
// Equivalente a lo anterior
/*
function mostrarContenido(){
    alert(contenido);
}
*/

/**
 * Ahora empleando jQuery
 * Ubicación: https://jquery.com/
 * https://htmlcheatsheet.com/jquery/
 */
$(document).ready(function(){

    $('#btnMostrar').click(function(){
        var contenido = $('#parrafo1').html();
        console.log(contenido);
        alert(contenido);
    })

    $('#btnObtener').click(function(){
        mensaje = { datos : '' };
        $.ajax({
            data: mensaje,
            url: 'http://localhost:8000/personas_api_json/',
            type: 'get',
            beforeSend:function(){
                $('#resultado').html('Procesando solicitud de datos...');
            },
            success:function(response){
                console.log(response);
                if (response && response.datos && Array.isArray(response.datos)) {
                    let tablaHTML = '<table class="table table-bordered table-hover table-striped">';
                    tablaHTML += '<thead><tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>Correo</th><th>Teléfono</th></tr></thead><tbody>';
    
                    $.each(response.datos, function(index, persona){
                        tablaHTML += '<tr>';
                        tablaHTML += '<td>' + persona.id + '</td>';
                        tablaHTML += '<td>' + persona.nombre + '</td>';
                        tablaHTML += '<td>' + persona.apellido + '</td>';
                        tablaHTML += '<td>' + persona.correo + '</td>';
                        tablaHTML += '<td>' + persona.telefono + '</td>';
                        tablaHTML += '</tr>';
                    });
    
                    tablaHTML += '</tbody></table>';
                    $('#resultado').html(tablaHTML);
                } else {
                    $('#resultado').html('No se encontraron datos válidos en la respuesta.');
                }
            },
            error: function(xhr, status, error) {
                console.error("Error en la petición AJAX:", status, error);
                $('#resultado').html('Ocurrió un error al obtener los datos.');
            }
        });
    })
})


