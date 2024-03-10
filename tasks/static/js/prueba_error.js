document.addEventListener('', function() {
    const error = document.querySelectorAll('.error');

    Swal.fire({
        title: '¿Algo esta mal?',
        text: "La contraseña debe tener al menos una mayúscula, una minúscula, un número y un carácter especia!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#00b91f',
        cancelButtonColor: '#d33',
        confirmButtonText: '!',
        backdrop: true,
        showLoaderOnConfirm: true,
       
        allowOutsideClick: () => false,
        allowEscapekey: () => false

    })
    
});