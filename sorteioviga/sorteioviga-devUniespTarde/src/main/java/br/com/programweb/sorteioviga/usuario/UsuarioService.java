package br.com.programweb.sorteioviga.usuario;

import java.util.List;

public interface UsuarioService {

    void cadastrarUsuario(Usuario usuario);

    List<Usuario> listarUsuarios();

    Usuario buscarPorId(Long id);

}
