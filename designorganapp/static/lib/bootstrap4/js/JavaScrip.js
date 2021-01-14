$(function() {
    $('#dtBasicExample').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'sercharraydata',
            }, // parametros
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "Actions" },
            { "data": "code_client" },
            { "data": "surname", "name" },
            { "data": "gender" },
            { "data": "mobile" },
            { "data": "phone" },
            { "data": "email" },
            { "data": "address" },
            { "data": "department" },
            { "data": "neighborhood" },
            { "data": "locality" },
            { "data": "province" },
            { "data": "postal_code" },
        ],
        columnDefs: [{
            targets: [0],
            class: 'text-center',
            orderable: true,
            render: function(data, type, row) {
                return data;
            }
        }, ],
        initComplete: function(settings, json) {
            alert('Tabla cargada')
        }
    });
});


/*
function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function() {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function(data) {
                        console.log(data);
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function(jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function(data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function() {

                }
            },
        }
    })
};*/