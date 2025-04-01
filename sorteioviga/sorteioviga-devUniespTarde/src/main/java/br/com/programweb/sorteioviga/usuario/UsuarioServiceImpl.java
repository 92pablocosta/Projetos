package br.com.programweb.sorteioviga.usuario;

import br.com.programweb.sorteioviga.exception.NegocioException;
import br.com.programweb.sorteioviga.exception.RecursoDuplicadoException;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;
import java.util.regex.Pattern;

@Service
@RequiredArgsConstructor
public class UsuarioServiceImpl implements UsuarioService {

    private final UsuarioRepository usuarioRepository;

    @Override
    public void cadastrarUsuario(Usuario usuario) {
        if (usuarioRepository.existsByCpf(usuario.getCpf())) {
            throw new NegocioException("Usuário já cadastrado na base de dados!");
        }

        usuarioRepository.save(usuario);
    }



    @Override
    public List<Usuario> listarUsuarios() {
        return usuarioRepository.findAll();
    }

    public Usuario atualizarUsuario(Long id, Usuario dadosAtualizados) {
    Usuario usuarioExistente = usuarioRepository.findById(id)
            .orElseThrow(() -> new NegocioException("Não é possível atualizar: usuário não encontrado."));

    if (!usuarioExistente.getEmail().equals(dadosAtualizados.getEmail())) {
        if (usuarioRepository.existsByEmail(dadosAtualizados.getEmail())) {
            throw new RecursoDuplicadoException(
                    "Já existe um usuário cadastrado com o e-mail: " + dadosAtualizados.getEmail());
        }
        usuarioExistente.setEmail(dadosAtualizados.getEmail());
    }

    if (!usuarioExistente.getCpf().equals(dadosAtualizados.getCpf())) {
        if (usuarioRepository.existsByCpf(dadosAtualizados.getCpf())) {
            throw new RecursoDuplicadoException(
                    "Já existe um usuário cadastrado com o CPF: " + dadosAtualizados.getCpf());
        }
        usuarioExistente.setCpf(dadosAtualizados.getCpf());
    }

    if (dadosAtualizados.getDataNascimento() != null) {
        if (dadosAtualizados.getDataNascimento().isAfter(LocalDate.now())) {
            throw new NegocioException("A data de nascimento não pode ser no futuro.");
        }
        usuarioExistente.setDataNascimento(dadosAtualizados.getDataNascimento());
    }

    if (dadosAtualizados.getTelefone() != null && !dadosAtualizados.getTelefone().isBlank()) {
        Pattern pattern = Pattern.compile("^[+]?\\d{8,15}$");
        if (!pattern.matcher(dadosAtualizados.getTelefone()).matches()) {
            throw new NegocioException("Telefone inválido. " +
                    "Formato aceito: apenas dígitos e opcional +, com 8 a 15 dígitos.");
        }
        usuarioExistente.setTelefone(dadosAtualizados.getTelefone());
    } else {
        usuarioExistente.setTelefone(null);
    }

    usuarioExistente.setNome(dadosAtualizados.getNome());

    return usuarioRepository.save(usuarioExistente);
}


    public void deletarUsuario(Long id) {
        if (!usuarioRepository.existsById(id)) {
            throw new NegocioException("Não é possível deletar: usuário não encontrado.");
        }
        usuarioRepository.deleteById(id);
    }


}
