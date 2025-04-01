package br.com.programweb.sorteioviga.usuario;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Controlador que expõe a API REST para a entidade Usuario.
 * Aqui se aplica:
 * - Verbos HTTP (GET, POST, PUT, DELETE)
 * - URL base "/usuarios"
 * - Uso de clientes HTTP (ex: Postman) para testar os endpoints
 */
@RestController
@RequestMapping("/usuarios")
@RequiredArgsConstructor
public class UsuarioController {

    private final UsuarioService usuarioService;

    @PostMapping
    public ResponseEntity<Void> cadastrar(@RequestBody @Valid Usuario usuario) {
        usuarioService.cadastrarUsuario(usuario);
        return ResponseEntity.status(HttpStatus.CREATED).build();
    }


    // TODO chamada: www.sorteioviga.com/usuarios/todos  Tipo: GET
    @GetMapping("/todos")
    public List<Usuario> listarUsuarios() {
        return usuarioService.listarUsuarios();
    }
}
