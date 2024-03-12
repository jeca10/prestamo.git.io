  // Esperar a que el DOM esté completamente cargado
  document.addEventListener("DOMContentLoaded", function() {
    // Buscar el elemento de mensaje de error
    var errorMessage = document.getElementById("error");

    // Verificar si el mensaje de error existe
    if (errorMessage) {
      // Obtener el texto del mensaje de error
      var errorText = errorMessage.textContent.trim();

      // Mostrar el mensaje de error utilizando SweetAlert
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: errorText,
        confirmButtonColor: '#00b91f',
      });
    }
  });

