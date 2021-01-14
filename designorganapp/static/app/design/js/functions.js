$(function() {
    // TABLE
    $('#dtBasicExample').DataTable({
        "scrollX": true,
        "scrollX": 400,
        "scrollY": 400,
        paging: true,
        responsive: true,
        //autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla =(",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            "buttons": {
                "copy": "Copiar",
                "colvis": "Visibilidad"
            }
        },

    });


    // Buscardo de datos y detección de erores. Carga datos más rápido en tabla
    $('#btnloadlistdesign').on('click', function() {
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                id: 1,
                //    'action': 'search_products',
                //    'term': request.term
            },
            dataType: 'json',
        }).done(function(data) {
            console.log(data);
            //response(data);
        }).fail(function(jqXHR, textStatus, errorThrown) {
            //alert('Error en la busqueda de datos');
            alert(textStatus + ' - ' + errorThrown)
        }).always(function(data) {
            alert('Completo el proceso Diseño');
        });
    });

});