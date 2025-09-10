function confirmarGuardar() {
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Esta seguro de guardar el producto",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí,",
    cancelButtonText: "No,",
  }).then((result) => {
    if (result.isConfirmed) {
      const form = document.getElementById("form-guardar-producto");
      if (form) {
        form.submit();
      } else {
        console.error("Formulario no encontrado: form-guardar-producto");
      }
    }
  });
}

function confirmarEliminar(e, codigo) {
  if (e && e.preventDefault) e.preventDefault();
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Esta seguro de eliminar el producto",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "No, cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/eliminar/" + codigo;
    }
  });
}

function confirmarEditar(codigo) {
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Se modificara el producto",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí,",
    cancelButtonText: "No,",
  }).then((result) => {
    if (result.isConfirmed) {
      document.querySelector(`#form-editar-${codigo}`).submit();
    }
  });
}
