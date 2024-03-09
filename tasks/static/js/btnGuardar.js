document.addEventListener('DOMContentLoaded', function () {
    const btnGuardar = document.querySelectorAll('.btnGuardar');

    btnGuardar.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            Swal.fire({
                title: '¿Estas seguro?',
                text: "No podrás revertir esta acción!",
                icon: 'success',
                showCancelButton: true,
                confirmButtonColor: '#00b91f',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si, Guardar!',
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: () => {
                    // Realizar cualquier acción adicional antes de la redirección

                    // Redirigir a la página de Django 'prestamo/'
                    window.location.href = '{% url "cumpu" %}'; 
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false
            });
        });
    });
});
