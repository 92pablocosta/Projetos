package br.com.programweb.sorteioviga.usuario;

import br.com.programweb.sorteioviga.bilhete.BilheteService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.validation.Valid;
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
    private final BilheteService bilheteService; // adiciona a interface ao usuario

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

    @GetMapping("/{id}")
    public ResponseEntity<Usuario> buscarPorID(@PathVariable Long id) {
        Usuario usuario = usuarioService.buscarPorId(id);
        return ResponseEntity.ok(usuario);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Usuario> atualizar(@PathVariable Long id, @RequestBody @Valid Usuario usuario) {
        Usuario atualizado = usuarioService.atualizarUsuario(id, usuario);
        return ResponseEntity.ok(atualizado);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletar(@PathVariable Long id) {
        usuarioService.deletarUsuario(id);
        return ResponseEntity.noContent().build();
    }

    // Implementação bilhete

    @PostMapping("/{id}/bilhetes")
    public ResponseEntity<Void> cadastrarBilhete(
            @PathVariable Long id,
            @RequestBody Integer numero) {

        Usuario usuario = usuarioService.buscarPorId(id);
        bilheteService.cadastrarBilhete(numero, usuario);

        return ResponseEntity.status(HttpStatus.CREATED).build();
    }

}
